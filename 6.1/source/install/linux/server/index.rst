
.. index::
   single: Installation; OpenERP Server (Linux)
   single: OpenERP Server; Installation (Linux)
..

.. linux-server-link:

OpenERP Server Installation
===========================

Installing the required packages
--------------------------------

Python 2.6 or later is required for OpenERP 6.1. It is built-in in Ubuntu version 10.04 and above.
A few Python libraries are also required, as listed below.

On a Debian-based Linux distribution you can install all required dependencies with this single
command::

    apt-get install python-dateutil python-feedparser python-gdata python-ldap \
        python-libxslt1 python-lxml python-mako python-openid python-psycopg2 \
        python-pybabel python-pychart python-pydot python-pyparsing python-reportlab \
        python-simplejson python-tz python-vatnumber python-vobject python-webdav \
        python-werkzeug python-xlwt python-yaml python-zsi


* :guilabel:`dateutil` : provides powerful extensions to the standard datetime module, available in Python 2.3+. ::

                    sudo apt-get install python-dateutil

* :guilabel:`feedparser` : universal Feed Parser for Python ::

                    sudo apt-get install python-feedparser

* :guilabel:`gdata` : Google Data Python client library ::

                    sudo apt-get install python-gdata

* :guilabel:`ldap` : LDAP interface module ::

                    sudo apt-get install python-ldap

* :guilabel:`libxslt1` : Python bindings for XSLT transformation library ::

                    sudo apt-get install python-libxslt1

* :guilabel:`lxml` : lxml is the most feature-rich and easy-to-use library for working with XML and HTML in the Python language. ::

					sudo apt-get install python-lxml

* :guilabel:`mako` : fast and lightweight templating for the Python platform. ::

					sudo apt-get install python-mako

* :guilabel:`openid` : OpenID authentication support for servers and consumers  ::

                    sudo apt-get install python-openid

* :guilabel:`psycopg2` : the most popular PostgreSQL adapter for the Python programming language. ::

					sudo apt-get install python-psycopg2

* :guilabel:`babel` : tools for internationalizing Python applications ::

                    sudo apt-get install python-pybabel

* :guilabel:`pychart` : library for creating high quality Encapsulated Postscript, PDF, PNG, or SVG charts. ::

					sudo apt-get install python-pychart

* :guilabel:`pydot` : provides a full interface to create, handle, modify and process graphs in Graphviz's dot language. ::

					sudo apt-get install python-pydot

* :guilabel:`pyparsing` : library for parsing Python code ::

                    sudo apt-get install python-pyparsing

* :guilabel:`reportlab` : The ReportLab Toolkit is the time-proven, ultra-robust, open-source engine for programmatically creating PDF documents and forms the foundation of RML. It also contains a library for creating platform-independent vector graphics. It is a fast, flexible, cross-platform solution written in Python. ::

                    sudo apt-get install python-reportlab

* :guilabel:`simplejson` : simple, fast, extensible JSON encoder/decoder ::

                    sudo apt-get install python-simplejson

* :guilabel:`vatnumber` :  module to validate VAT numbers for European countries ::

                    sudo apt-get install python-vatnumber

* :guilabel:`vobject` : VObject simplifies the process of parsing and creating iCalendar and vCard objects. ::

                    sudo apt-get install python-vobject

* :guilabel:`pytz` : World Timezone Definitions for Python ::

					sudo apt-get install python-tz

* :guilabel:`webdav` : WebDAV server implementation in Python ::

                    sudo apt-get install python-webdav

* :guilabel:`werkzeug` : collection of utilities for WSGI applications ::

                    sudo apt-get install python-werkzeug

* :guilabel:`yaml` : YAML parser and emitter for Python. ::

					sudo apt-get install python-yaml

* :guilabel:`xlwt` : module for reading/writing Microsoft Excel spreadsheet files ::

                    sudo apt-get install python-xlwt

* :guilabel:`zsi` :  Zolera Soap client infrastructure ::

                    sudo apt-get install python-zsi


Downloading the OpenERP Server
------------------------------

The OpenERP server can be downloaded from
the `OpenERP website's download page <http://www.openerp.com/downloads>`_

Testing the OpenERP Server
--------------------------

If you only want to test the server, you do not need to install it. Just unpack the archive and start
the openerp-server executable: ::

        tar -xzf openerp-6.1-latest.tar.gz
        cd openerp-6.1-*
        ./openerp-server

The list of available command line parameters can be obtained with the ``-h``
command-line switch: ::

    openerp-server -h

Installing the OpenERP Server
-----------------------------

The OpenERP Server can be installed very easily using the *setup.py* file: ::

    tar -xzf openerp-6.1-latest.tar.gz
    cd openerp-6.1-*
    sudo python setup.py install

If your PostgreSQL server is up and running, you can now run the server using
the following command: ::

    openerp-server

If you do not already have a PostgreSQL server up and running, you can read
:ref:`installation-postgresql-server`.


Creating a configuration file for OpenERP Server
------------------------------------------------

You can start the OpenERP server with the ``-s`` option to create a configuration file
with default options, then modify it. The configuration parameters are similar to
the server startup parameters, so have a look at the output of ``openerp -h`` if
you're not sure what a given parameter does::

    ./openerp-server -s -c <config_file_path>
    # now edit the config file at <config_file_path>
    # and check the -h output for more details...
    ./openerp-server -h
    (...)
    # finally start the server with the desired config file
    ./openerp-server -c <config_file_path>


Default Configuration file
++++++++++++++++++++++++++
The default OpenERP configuration file is located in ``$HOME/.openerp_serverrc``,
that is a file named ``.openerp_serverrc`` in the home directory of the
system user under which OpenERP runs.
This is the default value for the ``-c`` startup parameter. 
