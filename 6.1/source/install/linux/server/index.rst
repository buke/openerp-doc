
.. i18n: .. index::
.. i18n:    single: Installation; OpenERP Server (Linux)
.. i18n:    single: OpenERP Server; Installation (Linux)
.. i18n: ..
..

.. index::
   single: Installation; OpenERP Server (Linux)
   single: OpenERP Server; Installation (Linux)
..

.. i18n: .. linux-server-link:
..

.. linux-server-link:

.. i18n: OpenERP Server Installation
.. i18n: ===========================
..

OpenERP Server Installation
===========================

.. i18n: Installing the required packages
.. i18n: --------------------------------
..

Installing the required packages
--------------------------------

.. i18n: Python 2.6 or later is required for OpenERP 6.1. It is built-in in Ubuntu version 10.04 and above.
.. i18n: A few Python libraries are also required, as listed below.
..

Python 2.6 or later is required for OpenERP 6.1. It is built-in in Ubuntu version 10.04 and above.
A few Python libraries are also required, as listed below.

.. i18n: On a Debian-based Linux distribution you can install all required dependencies with this single
.. i18n: command::
.. i18n: 
.. i18n:     apt-get install python-dateutil python-feedparser python-gdata python-ldap \
.. i18n:         python-libxslt1 python-lxml python-mako python-openid python-psycopg2 \
.. i18n:         python-pybabel python-pychart python-pydot python-pyparsing python-reportlab \
.. i18n:         python-simplejson python-tz python-vatnumber python-vobject python-webdav \
.. i18n:         python-werkzeug python-xlwt python-yaml python-zsi
..

On a Debian-based Linux distribution you can install all required dependencies with this single
command::

    apt-get install python-dateutil python-feedparser python-gdata python-ldap \
        python-libxslt1 python-lxml python-mako python-openid python-psycopg2 \
        python-pybabel python-pychart python-pydot python-pyparsing python-reportlab \
        python-simplejson python-tz python-vatnumber python-vobject python-webdav \
        python-werkzeug python-xlwt python-yaml python-zsi

.. i18n: * :guilabel:`dateutil` : provides powerful extensions to the standard datetime module, available in Python 2.3+. ::
.. i18n: 
.. i18n:                     sudo apt-get install python-dateutil
.. i18n: 
.. i18n: * :guilabel:`feedparser` : universal Feed Parser for Python ::
.. i18n: 
.. i18n:                     sudo apt-get install python-feedparser
.. i18n: 
.. i18n: * :guilabel:`gdata` : Google Data Python client library ::
.. i18n: 
.. i18n:                     sudo apt-get install python-gdata
.. i18n: 
.. i18n: * :guilabel:`ldap` : LDAP interface module ::
.. i18n: 
.. i18n:                     sudo apt-get install python-ldap
.. i18n: 
.. i18n: * :guilabel:`libxslt1` : Python bindings for XSLT transformation library ::
.. i18n: 
.. i18n:                     sudo apt-get install python-libxslt1
.. i18n: 
.. i18n: * :guilabel:`lxml` : lxml is the most feature-rich and easy-to-use library for working with XML and HTML in the Python language. ::
.. i18n: 
.. i18n: 					sudo apt-get install python-lxml
.. i18n: 
.. i18n: * :guilabel:`mako` : fast and lightweight templating for the Python platform. ::
.. i18n: 
.. i18n: 					sudo apt-get install python-mako
.. i18n: 
.. i18n: * :guilabel:`openid` : OpenID authentication support for servers and consumers  ::
.. i18n: 
.. i18n:                     sudo apt-get install python-openid
.. i18n: 
.. i18n: * :guilabel:`psycopg2` : the most popular PostgreSQL adapter for the Python programming language. ::
.. i18n: 
.. i18n: 					sudo apt-get install python-psycopg2
.. i18n: 
.. i18n: * :guilabel:`babel` : tools for internationalizing Python applications ::
.. i18n: 
.. i18n:                     sudo apt-get install python-pybabel
.. i18n: 
.. i18n: * :guilabel:`pychart` : library for creating high quality Encapsulated Postscript, PDF, PNG, or SVG charts. ::
.. i18n: 
.. i18n: 					sudo apt-get install python-pychart
.. i18n: 
.. i18n: * :guilabel:`pydot` : provides a full interface to create, handle, modify and process graphs in Graphviz's dot language. ::
.. i18n: 
.. i18n: 					sudo apt-get install python-pydot
.. i18n: 
.. i18n: * :guilabel:`pyparsing` : library for parsing Python code ::
.. i18n: 
.. i18n:                     sudo apt-get install python-pyparsing
.. i18n: 
.. i18n: * :guilabel:`reportlab` : The ReportLab Toolkit is the time-proven, ultra-robust, open-source engine for programmatically creating PDF documents and forms the foundation of RML. It also contains a library for creating platform-independent vector graphics. It is a fast, flexible, cross-platform solution written in Python. ::
.. i18n: 
.. i18n:                     sudo apt-get install python-reportlab
.. i18n: 
.. i18n: * :guilabel:`simplejson` : simple, fast, extensible JSON encoder/decoder ::
.. i18n: 
.. i18n:                     sudo apt-get install python-simplejson
.. i18n: 
.. i18n: * :guilabel:`vatnumber` :  module to validate VAT numbers for European countries ::
.. i18n: 
.. i18n:                     sudo apt-get install python-vatnumber
.. i18n: 
.. i18n: * :guilabel:`vobject` : VObject simplifies the process of parsing and creating iCalendar and vCard objects. ::
.. i18n: 
.. i18n:                     sudo apt-get install python-vobject
.. i18n: 
.. i18n: * :guilabel:`pytz` : World Timezone Definitions for Python ::
.. i18n: 
.. i18n: 					sudo apt-get install python-tz
.. i18n: 
.. i18n: * :guilabel:`webdav` : WebDAV server implementation in Python ::
.. i18n: 
.. i18n:                     sudo apt-get install python-webdav
.. i18n: 
.. i18n: * :guilabel:`werkzeug` : collection of utilities for WSGI applications ::
.. i18n: 
.. i18n:                     sudo apt-get install python-werkzeug
.. i18n: 
.. i18n: * :guilabel:`yaml` : YAML parser and emitter for Python. ::
.. i18n: 
.. i18n: 					sudo apt-get install python-yaml
.. i18n: 
.. i18n: * :guilabel:`xlwt` : module for reading/writing Microsoft Excel spreadsheet files ::
.. i18n: 
.. i18n:                     sudo apt-get install python-xlwt
.. i18n: 
.. i18n: * :guilabel:`zsi` :  Zolera Soap client infrastructure ::
.. i18n: 
.. i18n:                     sudo apt-get install python-zsi
..

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

.. i18n: Downloading the OpenERP Server
.. i18n: ------------------------------
..

Downloading the OpenERP Server
------------------------------

.. i18n: The OpenERP server can be downloaded from
.. i18n: the `OpenERP website's download page <http://www.openerp.com/downloads>`_
..

The OpenERP server can be downloaded from
the `OpenERP website's download page <http://www.openerp.com/downloads>`_

.. i18n: Testing the OpenERP Server
.. i18n: --------------------------
..

Testing the OpenERP Server
--------------------------

.. i18n: If you only want to test the server, you do not need to install it. Just unpack the archive and start
.. i18n: the openerp-server executable: ::
.. i18n: 
.. i18n:         tar -xzf openerp-6.1-latest.tar.gz
.. i18n:         cd openerp-6.1-*
.. i18n:         ./openerp-server
..

If you only want to test the server, you do not need to install it. Just unpack the archive and start
the openerp-server executable: ::

        tar -xzf openerp-6.1-latest.tar.gz
        cd openerp-6.1-*
        ./openerp-server

.. i18n: The list of available command line parameters can be obtained with the ``-h``
.. i18n: command-line switch: ::
.. i18n: 
.. i18n:     openerp-server -h
..

The list of available command line parameters can be obtained with the ``-h``
command-line switch: ::

    openerp-server -h

.. i18n: Installing the OpenERP Server
.. i18n: -----------------------------
..

Installing the OpenERP Server
-----------------------------

.. i18n: The OpenERP Server can be installed very easily using the *setup.py* file: ::
.. i18n: 
.. i18n:     tar -xzf openerp-6.1-latest.tar.gz
.. i18n:     cd openerp-6.1-*
.. i18n:     sudo python setup.py install
..

The OpenERP Server can be installed very easily using the *setup.py* file: ::

    tar -xzf openerp-6.1-latest.tar.gz
    cd openerp-6.1-*
    sudo python setup.py install

.. i18n: If your PostgreSQL server is up and running, you can now run the server using
.. i18n: the following command: ::
.. i18n: 
.. i18n:     openerp-server
..

If your PostgreSQL server is up and running, you can now run the server using
the following command: ::

    openerp-server

.. i18n: If you do not already have a PostgreSQL server up and running, you can read
.. i18n: :ref:`installation-postgresql-server`.
..

If you do not already have a PostgreSQL server up and running, you can read
:ref:`installation-postgresql-server`.

.. i18n: Creating a configuration file for OpenERP Server
.. i18n: ------------------------------------------------
..

Creating a configuration file for OpenERP Server
------------------------------------------------

.. i18n: You can start the OpenERP server with the ``-s`` option to create a configuration file
.. i18n: with default options, then modify it. The configuration parameters are similar to
.. i18n: the server startup parameters, so have a look at the output of ``openerp -h`` if
.. i18n: you're not sure what a given parameter does::
.. i18n: 
.. i18n:     ./openerp-server -s -c <config_file_path>
.. i18n:     # now edit the config file at <config_file_path>
.. i18n:     # and check the -h output for more details...
.. i18n:     ./openerp-server -h
.. i18n:     (...)
.. i18n:     # finally start the server with the desired config file
.. i18n:     ./openerp-server -c <config_file_path>
..

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

.. i18n: Default Configuration file
.. i18n: ++++++++++++++++++++++++++
.. i18n: The default OpenERP configuration file is located in ``$HOME/.openerp_serverrc``,
.. i18n: that is a file named ``.openerp_serverrc`` in the home directory of the
.. i18n: system user under which OpenERP runs.
.. i18n: This is the default value for the ``-c`` startup parameter. 
..

Default Configuration file
++++++++++++++++++++++++++
The default OpenERP configuration file is located in ``$HOME/.openerp_serverrc``,
that is a file named ``.openerp_serverrc`` in the home directory of the
system user under which OpenERP runs.
This is the default value for the ``-c`` startup parameter. 
