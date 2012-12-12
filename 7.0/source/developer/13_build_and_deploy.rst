================
Build and deploy
================

This page describes how to build a custom version of OpenERP for Windows.

Building
========

Dependencies
------------

The first step is to build the dependencies. To do so, grab the Windows installer branch::

    bzr branch lp:~openerp-groupes/openerp/win-installer-trunk

and install the packages:

    * 7z465.msi
    * python-2.5.2.msi
    * setuptools-0.6c9.win32-py2.5.exe
    * Beaker-1.4.1.tar.gz
    * Mako-0.2.4.tar.gz
    * pytz-2010l.win32.exe

Server
++++++

Install the packages:

    * lxml-2.1.2.win32-py2.5.exe
    * PIL-1.1.6.win32-py2.5.exe
    * psycopg2-2.2.2.win32-py2.5-pg9.0.1-release.exe
    * PyChart-1.39.win32.exe
    * pydot-1.0.2.win32.exe
    * python-dateutil-1.5.tar.gz
    * pywin32-212.win32-py2.5.exe
    * PyYAML-3.09.win32-py2.5.exe
    * ReportLab-2.2.win32-py2.5.exe

Web
+++

Install the packages:

    * Babel-0.9.4-py2.5.egg
    * CherryPy-3.1.2.win32.exe
    * FormEncode-1.2.2.tar.gz
    * simplejson-2.0.9-py2.5-win32.egg
    * xlwt-0.7.2.win32.exe

Source distribution
-------------------

The second step is to build a source distribution on Linux.

Server
++++++

Let's assume you work on your own server branch named **6.0** and you want to build a server with the following modules:

    * base_setup
    * base_tools
    * board

This implies that these modules have been linked in *bin/addons* by a command similar to::

    ln -s ~/openerp/addons/6.0/{base_setup,base_tools,board} .

To build the server, go to the root directory and type::

    python setup.py sdist --format=zip

You now have a new file in the **dist** directory, called openerp-server-M.m.P.zip where:
    * **M** is the major version, example 6
    * **m** is the minor version, example 0
    * **p** is the patch version, example 1

Web
+++

To build the web client, go to the root directory and type::

    python setup.py sdist --format=zip

You now have a new file in the **dist** directory, called openerp-web-M.m.P.zip where:
    * **M** is the major version, example 6
    * **m** is the minor version, example 0
    * **p** is the patch version, example 1

Binary distribution
-------------------

The third step is to build a binary distribution on Windows.

Server
++++++

Open a command prompt and unzip the file::

    7z x openerp-server-M.m.P.zip -oC:\openerp

Go to the **win32** directory::

    cd C:\openerp\openerp-server-M.m.P\win32

Generate the service exe with::

    python setup.py py2exe

Go to the parent directory::

    cd ..

Generate the server exe with::

    python setup.py py2exe

Build the Windows installer with::

    makensis setup.nsi

You now have a new file in the root directory, called openerp-server-setup-M.m.P.exe. This file is the installer that you can use the install a custom version of OpenERP.

Web
+++

Open a command prompt and unzip the file::

    7z x openerp-web-M.m.P.zip -oC:\openerp

Go to the **win32** directory::

    cd C:\openerp\openerp-web-M.m.P\win32

Generate the service exe with::

    python setup.py py2exe

Go to the parent directory::

    cd ..

Generate the web exe with::

    python setup.py py2exe

Build the Windows installer with::

    makensis setup.nsi

You now have a new file in the root directory, called openerp-web-setup-M.m.P.exe. This file is the installer that you can use the install a custom version of OpenERP.


Deploy
======

This page describes how to deploy a custom version of OpenERP on Windows.

Package script
--------------

The first step is to grab the package script branch::

    bzr branch lp:~openerp-groupes/openerp/package-script

Batch
-----

Go to the *packaging* directory of the branch and copy the file *build.bat* to the *C:\\openerp* directory of your Windows machine.

SSH server
----------

You need to install a SSH server on Windows. You can for example install `freeSSHd <http://www.freesshd.com/>`_.

Fabric
------

You need to install the tool `Fabric <http://docs.fabfile.org/0.9.3/>`_ to run commands on Windows from Linux using SSH. Refer to your linux package manager to install it.

Configure
+++++++++

Go to the *packaging* directory of the branch and edit the file fabfile.py. Change what need to be changed.

Run
+++

run the command::

    fab -H host -u user server

where:
    * *host* is the Windows host name
    * *user* is the Windows user name

