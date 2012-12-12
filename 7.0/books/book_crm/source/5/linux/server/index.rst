
.. index::
   single: Installation; OpenERP Server (Linux)
   single: OpenERP Server; Installation (Linux)
..

.. linux-server-link:

OpenERP Server Installation
===========================

*Installing the required packages*

You need to have Python (at least 2.5 for OpenERP v6.0) in your Ubuntu system, which is in-built in Ubuntu version 10.04
and above.

You also need to install the following Python libraries, because OpenERP Server uses these packages.

To install the required libraries on your Ubuntu system, you can do the following in your favourite shell:

* :guilabel:`lxml` : lxml is the most feature-rich and easy-to-use library for working with XML and HTML in the Python language. ::

					sudo apt-get install python-lxml

* :guilabel:`mako` : Hyperfast and lightweight templating for the Python platform. ::

					sudo apt-get install python-mako

* :guilabel:`mxdatetime` : Provides the most natural and robust way of dealing with date/time values in Python. ::

					sudo apt-get install python-egenix-mxdatetime

* :guilabel:`python-dateutil` : The dateutil module provides powerful extensions to the standard datetime module, available in Python 2.3+. ::

					sudo apt-get install python-dateutil

* :guilabel:`psycopg2` : Psycopg is the most popular PostgreSQL adapter for the Python programming language. ::

					sudo apt-get install python-psycopg2

* :guilabel:`pychart` : PyChart is a Python library for creating high quality Encapsulated Postscript, PDF, PNG, or SVG charts. ::

					sudo apt-get install python-pychart

* :guilabel:`pydot` : This module provides a full interface to create, handle, modify and process graphs in Graphviz's dot language. ::

					sudo apt-get install python-pydot

* :guilabel:`pytz` : World Timezone Definitions for Python. ::

					sudo apt-get install python-tz

* :guilabel:`reportlab` : The ReportLab Toolkit is the time-proven, ultra-robust, open-source engine for programmatically creating PDF documents and forms the foundation of RML. It also contains a library for creating platform-independent vector graphics. It is a fast, flexible, cross-platform solution written in Python. ::

					sudo apt-get install python-reportlab

* :guilabel:`pyyaml` : PyYAML is a YAML parser and emitter for Python. ::

					sudo apt-get install python-yaml

* :guilabel:`vobject` : VObject simplifies the process of parsing and creating iCalendar and vCard objects. ::

					sudo apt-get install python-vobject

*Downloading the OpenERP Server*

The OpenERP server can be downloaded from the OpenERP website's download page <http://www.openerp.com/downloads>.

*Testing the OpenERP Server*

If you only want to test the server, you do not need to install it. Just unpack the archive and start
the openerp-server executable: ::

        tar -xzf openerp-server-6.0.0.tar.gz
        cd openerp-server-6.0.0/bin
        python openerp-server.py

The list of available command line parameters can be obtained with the ``-h``
command-line switch: ::

    python openerp-server.py -h

*Installing the OpenERP Server*

The OpenERP Server can be installed very easily using the *setup.py* file: ::

    tar -xzf openerp-server-6.0.0.tar.gz
    cd openerp-server-6.0.0
    sudo python setup.py install

If your PostgreSQL server is up and running, you can now run the server using
the following command: ::

    openerp-server

If you do not already have a PostgreSQL server up and running, you can read
:ref:`installation-postgresql-server`.

You can find the OpenERP server configuration file
at ``~/openerp-server-6.0.0/doc/openerp-server.conf``.

