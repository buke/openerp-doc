
.. index::
   single: Installation; OpenERP Web (Linux)
   single: OpenERP Web; Installation (Linux)
..

.. _installation-linux-web-link:

OpenERP Web Installation
========================

*Downloading the OpenERP Web Client*

The OpenERP Web Client can be downloaded from OpenERP website's download page <http://www.openerp.com/downloads>.

*Installing the required packages*

You need to install the following Python libraries, because OpenERP Web Client uses these packages:

#. Python >= 2.4
#. CherryPy >= 3.1.2
#. Mako >= 0.2.4
#. Babel >= 0.9.4
#. FormEncode >= 1.2.2
#. simplejson >= 2.0.9
#. pyparsing >= 1.5.0

There is no need to install the above packages one by one. You can just run the following commands in your favourite shell: ::

    $ sudo apt-get install python python-dev build-essential
    $ sudo apt-get install python-setuptools

This will install dependencies required for the following: ::

    $ cd /path/to/openerp-web-6.0.0/lib
    $ ./populate.sh
    $ cd ..

This will install all required dependencies in private lib directory, and you
do not need to install anything.

*Testing the OpenERP Web Client*

If you only want to test the web client, you do not need to install it. Just unpack the archive and start
the openerp-web executable: ::

        tar -xzf openerp-web-6.0.0.tar.gz
        cd openerp-web-6.0.0/
        python openerp-web.py

The list of available command line parameters can be obtained with the ``-h``
command line switch: ::

    python openerp-web.py -h


*Installing the OpenERP Web Client*

The OpenERP Web Client can be installed very easily using the *setup.py* file: ::

    tar -xzf openerp-web-6.0.0.tar.gz
    cd openerp-web-6.0.0
    sudo python setup.py install

You can now run the OpenERP Web Client using the following command: ::

    openerp-web

You can find the OpenERP Web Client configuration file at ``~/openerp-web-6.0.0/doc/openerp-web.conf``.

*Web Browser Compatibilities*

Supported Browsers
++++++++++++++++++

*OpenERP Web Client* is known to work best with *Mozilla* based web browsers. Here is
a list of supported browsers:

#. Firefox >= 3.6
#. Internet Explorer >= 7.0
#. Safari >= 4.1
#. Google Chrome >= 9.0
#. Opera >= 10.0


*Flash Plugin*

Your browser should have the Flash plugin installed because *OpenERP Web Client* uses
some Flash components.

Apply the following command in order to install the Flash plugin on an Ubuntu system:

.. code-block:: bash

    $ sudo apt-get install flashplugin-nonfree


