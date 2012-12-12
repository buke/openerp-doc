
.. i18n: ================
.. i18n: Build and deploy
.. i18n: ================
..

================
Build and deploy
================

.. i18n: This page describes how to build a custom version of OpenERP for Windows.
..

This page describes how to build a custom version of OpenERP for Windows.

.. i18n: Building
.. i18n: ========
..

Building
========

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n: The first step is to build the dependencies. To do so, grab the Windows installer branch::
.. i18n: 
.. i18n:     bzr branch lp:~openerp-groupes/openerp/win-installer-trunk
..

The first step is to build the dependencies. To do so, grab the Windows installer branch::

    bzr branch lp:~openerp-groupes/openerp/win-installer-trunk

.. i18n: and install the packages:
..

and install the packages:

.. i18n:     * 7z465.msi
.. i18n:     * python-2.5.2.msi
.. i18n:     * setuptools-0.6c9.win32-py2.5.exe
.. i18n:     * Beaker-1.4.1.tar.gz
.. i18n:     * Mako-0.2.4.tar.gz
.. i18n:     * pytz-2010l.win32.exe
..

    * 7z465.msi
    * python-2.5.2.msi
    * setuptools-0.6c9.win32-py2.5.exe
    * Beaker-1.4.1.tar.gz
    * Mako-0.2.4.tar.gz
    * pytz-2010l.win32.exe

.. i18n: Server
.. i18n: ++++++
..

Server
++++++

.. i18n: Install the packages:
..

Install the packages:

.. i18n:     * lxml-2.1.2.win32-py2.5.exe
.. i18n:     * PIL-1.1.6.win32-py2.5.exe
.. i18n:     * psycopg2-2.2.2.win32-py2.5-pg9.0.1-release.exe
.. i18n:     * PyChart-1.39.win32.exe
.. i18n:     * pydot-1.0.2.win32.exe
.. i18n:     * python-dateutil-1.5.tar.gz
.. i18n:     * pywin32-212.win32-py2.5.exe
.. i18n:     * PyYAML-3.09.win32-py2.5.exe
.. i18n:     * ReportLab-2.2.win32-py2.5.exe
..

    * lxml-2.1.2.win32-py2.5.exe
    * PIL-1.1.6.win32-py2.5.exe
    * psycopg2-2.2.2.win32-py2.5-pg9.0.1-release.exe
    * PyChart-1.39.win32.exe
    * pydot-1.0.2.win32.exe
    * python-dateutil-1.5.tar.gz
    * pywin32-212.win32-py2.5.exe
    * PyYAML-3.09.win32-py2.5.exe
    * ReportLab-2.2.win32-py2.5.exe

.. i18n: Web
.. i18n: +++
..

Web
+++

.. i18n: Install the packages:
..

Install the packages:

.. i18n:     * Babel-0.9.4-py2.5.egg
.. i18n:     * CherryPy-3.1.2.win32.exe
.. i18n:     * FormEncode-1.2.2.tar.gz
.. i18n:     * simplejson-2.0.9-py2.5-win32.egg
.. i18n:     * xlwt-0.7.2.win32.exe
..

    * Babel-0.9.4-py2.5.egg
    * CherryPy-3.1.2.win32.exe
    * FormEncode-1.2.2.tar.gz
    * simplejson-2.0.9-py2.5-win32.egg
    * xlwt-0.7.2.win32.exe

.. i18n: Source distribution
.. i18n: -------------------
..

Source distribution
-------------------

.. i18n: The second step is to build a source distribution on Linux.
..

The second step is to build a source distribution on Linux.

.. i18n: Server
.. i18n: ++++++
..

Server
++++++

.. i18n: Let's assume you work on your own server branch named **6.0** and you want to build a server with the following modules:
..

Let's assume you work on your own server branch named **6.0** and you want to build a server with the following modules:

.. i18n:     * base_setup
.. i18n:     * base_tools
.. i18n:     * board
..

    * base_setup
    * base_tools
    * board

.. i18n: This implies that these modules have been linked in *bin/addons* by a command similar to::
.. i18n: 
.. i18n:     ln -s ~/openerp/addons/6.0/{base_setup,base_tools,board} .
..

This implies that these modules have been linked in *bin/addons* by a command similar to::

    ln -s ~/openerp/addons/6.0/{base_setup,base_tools,board} .

.. i18n: To build the server, go to the root directory and type::
.. i18n: 
.. i18n:     python setup.py sdist --format=zip
..

To build the server, go to the root directory and type::

    python setup.py sdist --format=zip

.. i18n: You now have a new file in the **dist** directory, called openerp-server-M.m.P.zip where:
.. i18n:     * **M** is the major version, example 6
.. i18n:     * **m** is the minor version, example 0
.. i18n:     * **p** is the patch version, example 1
..

You now have a new file in the **dist** directory, called openerp-server-M.m.P.zip where:
    * **M** is the major version, example 6
    * **m** is the minor version, example 0
    * **p** is the patch version, example 1

.. i18n: Web
.. i18n: +++
..

Web
+++

.. i18n: To build the web client, go to the root directory and type::
.. i18n: 
.. i18n:     python setup.py sdist --format=zip
..

To build the web client, go to the root directory and type::

    python setup.py sdist --format=zip

.. i18n: You now have a new file in the **dist** directory, called openerp-web-M.m.P.zip where:
.. i18n:     * **M** is the major version, example 6
.. i18n:     * **m** is the minor version, example 0
.. i18n:     * **p** is the patch version, example 1
..

You now have a new file in the **dist** directory, called openerp-web-M.m.P.zip where:
    * **M** is the major version, example 6
    * **m** is the minor version, example 0
    * **p** is the patch version, example 1

.. i18n: Binary distribution
.. i18n: -------------------
..

Binary distribution
-------------------

.. i18n: The third step is to build a binary distribution on Windows.
..

The third step is to build a binary distribution on Windows.

.. i18n: Server
.. i18n: ++++++
..

Server
++++++

.. i18n: Open a command prompt and unzip the file::
.. i18n: 
.. i18n:     7z x openerp-server-M.m.P.zip -oC:\openerp
..

Open a command prompt and unzip the file::

    7z x openerp-server-M.m.P.zip -oC:\openerp

.. i18n: Go to the **win32** directory::
.. i18n: 
.. i18n:     cd C:\openerp\openerp-server-M.m.P\win32
..

Go to the **win32** directory::

    cd C:\openerp\openerp-server-M.m.P\win32

.. i18n: Generate the service exe with::
.. i18n: 
.. i18n:     python setup.py py2exe
..

Generate the service exe with::

    python setup.py py2exe

.. i18n: Go to the parent directory::
.. i18n: 
.. i18n:     cd ..
..

Go to the parent directory::

    cd ..

.. i18n: Generate the server exe with::
.. i18n: 
.. i18n:     python setup.py py2exe
..

Generate the server exe with::

    python setup.py py2exe

.. i18n: Build the Windows installer with::
.. i18n: 
.. i18n:     makensis setup.nsi
..

Build the Windows installer with::

    makensis setup.nsi

.. i18n: You now have a new file in the root directory, called openerp-server-setup-M.m.P.exe. This file is the installer that you can use the install a custom version of OpenERP.
..

You now have a new file in the root directory, called openerp-server-setup-M.m.P.exe. This file is the installer that you can use the install a custom version of OpenERP.

.. i18n: Web
.. i18n: +++
..

Web
+++

.. i18n: Open a command prompt and unzip the file::
.. i18n: 
.. i18n:     7z x openerp-web-M.m.P.zip -oC:\openerp
..

Open a command prompt and unzip the file::

    7z x openerp-web-M.m.P.zip -oC:\openerp

.. i18n: Go to the **win32** directory::
.. i18n: 
.. i18n:     cd C:\openerp\openerp-web-M.m.P\win32
..

Go to the **win32** directory::

    cd C:\openerp\openerp-web-M.m.P\win32

.. i18n: Generate the service exe with::
.. i18n: 
.. i18n:     python setup.py py2exe
..

Generate the service exe with::

    python setup.py py2exe

.. i18n: Go to the parent directory::
.. i18n: 
.. i18n:     cd ..
..

Go to the parent directory::

    cd ..

.. i18n: Generate the web exe with::
.. i18n: 
.. i18n:     python setup.py py2exe
..

Generate the web exe with::

    python setup.py py2exe

.. i18n: Build the Windows installer with::
.. i18n: 
.. i18n:     makensis setup.nsi
..

Build the Windows installer with::

    makensis setup.nsi

.. i18n: You now have a new file in the root directory, called openerp-web-setup-M.m.P.exe. This file is the installer that you can use the install a custom version of OpenERP.
..

You now have a new file in the root directory, called openerp-web-setup-M.m.P.exe. This file is the installer that you can use the install a custom version of OpenERP.

.. i18n: Deploy
.. i18n: ======
..

Deploy
======

.. i18n: This page describes how to deploy a custom version of OpenERP on Windows.
..

This page describes how to deploy a custom version of OpenERP on Windows.

.. i18n: Package script
.. i18n: --------------
..

Package script
--------------

.. i18n: The first step is to grab the package script branch::
.. i18n: 
.. i18n:     bzr branch lp:~openerp-groupes/openerp/package-script
..

The first step is to grab the package script branch::

    bzr branch lp:~openerp-groupes/openerp/package-script

.. i18n: Batch
.. i18n: -----
..

Batch
-----

.. i18n: Go to the *packaging* directory of the branch and copy the file *build.bat* to the *C:\\openerp* directory of your Windows machine.
..

Go to the *packaging* directory of the branch and copy the file *build.bat* to the *C:\\openerp* directory of your Windows machine.

.. i18n: SSH server
.. i18n: ----------
..

SSH server
----------

.. i18n: You need to install a SSH server on Windows. You can for example install `freeSSHd <http://www.freesshd.com/>`_.
..

You need to install a SSH server on Windows. You can for example install `freeSSHd <http://www.freesshd.com/>`_.

.. i18n: Fabric
.. i18n: ------
..

Fabric
------

.. i18n: You need to install the tool `Fabric <http://docs.fabfile.org/0.9.3/>`_ to run commands on Windows from Linux using SSH. Refer to your linux package manager to install it.
..

You need to install the tool `Fabric <http://docs.fabfile.org/0.9.3/>`_ to run commands on Windows from Linux using SSH. Refer to your linux package manager to install it.

.. i18n: Configure
.. i18n: +++++++++
..

Configure
+++++++++

.. i18n: Go to the *packaging* directory of the branch and edit the file fabfile.py. Change what need to be changed.
..

Go to the *packaging* directory of the branch and edit the file fabfile.py. Change what need to be changed.

.. i18n: Run
.. i18n: +++
..

Run
+++

.. i18n: run the command::
.. i18n: 
.. i18n:     fab -H host -u user server
..

run the command::

    fab -H host -u user server

.. i18n: where:
.. i18n:     * *host* is the Windows host name
.. i18n:     * *user* is the Windows user name
..

where:
    * *host* is the Windows host name
    * *user* is the Windows user name
