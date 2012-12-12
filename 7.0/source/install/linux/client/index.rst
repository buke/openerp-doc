
.. index::
   single: Installation; OpenERP Client (Linux)
   single: OpenERP Client; Installation (Linux)
..

.. linux-client-link:

OpenERP GTK Client Installation
===============================

The native GTK client is available as a legacy interface for users who still require it, but the recommended way to access OpenERP 6.1 is the built-in web interface.


Installing the required packages
--------------------------------

Python 2.6 or later is required for OpenERP 6.1. It is built-in in Ubuntu version 10.04 and above.
A few Python libraries are also required, as listed below.

On a Debian-based Linux distribution you can install all required dependencies with this single
command::

    apt-get install python-gtk2 python-glade2 python-matplotlib python-dateutil \
        python-lxml python-tz python-hippocanvas python-pydot


* :guilabel:`gtk` : GTK+ is a highly usable, feature-rich toolkit for creating graphical user interfaces which boosts cross-platform compatibility and an easy-to-use API. ::

					sudo apt-get install python-gtk2

* :guilabel:`glade` : Glade is a RAD tool to enable quick & easy development of user interfaces for the GTK+ toolkit and the GNOME desktop environment. ::

					sudo apt-get install python-glade2

* :guilabel:`matplotlib` : matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hard-copy formats and interactive environments across platforms. ::

					sudo apt-get install python-matplotlib

* :guilabel:`dateutil` : Provides date/time values in Python ::

					sudo apt-get install python-dateutil

* :guilabel:`lxml` : XML support for Python platform. ::

					sudo apt-get install python-lxml

* :guilabel:`tz` : World Timezone definitions for Python. ::

					sudo apt-get install python-tz

* :guilabel:`hippocanvas` : The Hippo Canvas is a Cairo/GObject/GTK+ based canvas, written in C with support for flexible layout, CSS styling, and initial work on animations. ::

					sudo apt-get install python-hippocanvas

* :guilabel:`pydot` : Python interface to Graphviz's Dot language. ::

                    sudo apt-get install python-pydot

* Any PDF viewer, properly registered in your system to automatically open PDF files (e.g. xpdf, kpdf, acroread, evince, etc..).
  See the :ref:`configure-pdf-viewer-link` section.

.. note:: RedHat-based distributions

    As an alternative to the above commands meant for Debian-based distributions, the
    following command should install the required dependencies for RedHat-based systems::

        yum install pygtk2 glade3 pydot python-dateutil python-matplotlib \
            python-lxml python-hippo-canvas python-tz

.. note:: Mandriva

    As an alternative to the above commands meant for Debian-based distributions, the
    following command should install the required dependencies for Mandriva::

        yum install pygtk2 glade3 pydot python-dateutil python-matplotlib \
            python-lxml python-hippo-canvas python-tz

Downloading the OpenERP Client
------------------------------

The OpenERP client can be downloaded from
the `OpenERP website's download page <http://www.openerp.com/downloads>`_

Testing the OpenERP Client
--------------------------

If you only want to test the client, you do not need to install it. Just unpack the
archive and start the openerp-client executable: ::

        tar -xzf openerp-client-6.1-latest.tar.gz
        cd openerp-client-6.1-*/bin
        ./openerp-client.py

The list of available command line parameters can be obtained with the ``-h``
command-line switch: ::

    ./openerp-client.py -h

Installing the OpenERP Client
-----------------------------

The client can be installed very easily using the *setup.py* file: ::

  tar -xzf openerp-client-6.1-latest.tar.gz
  cd openerp-client-6.1-*
  sudo python setup.py install

You can now run the client using the following command: ::

  openerp-client

.. index::
   single: OpenERP Client; Configuring a PDF viewer
   single: PDF viewer
..

.. _configure-pdf-viewer-link:

Configuring a PDF Viewer
------------------------

By default the OpenERP Client will use your default PDF application
for displaying PDF files  You may customize this behavior by configuring
a different default PDF application on your system.

Alternatively, you may also specify explicitly the PDF command to use to
display PDF files in the OpenERP configuration file, normally located in your
HOME directory, and named ``'.openerprc'``.
Find the ``[printer]`` section and edit the ``softpath`` parameter. For example: ::

    [printer]
    softpath = kpdf

