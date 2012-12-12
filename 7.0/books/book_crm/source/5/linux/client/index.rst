
.. index::
   single: Installation; OpenERP Client (Linux)
   single: OpenERP Client; Installation (Linux)
..

.. linux-client-link:

OpenERP Client Installation
===========================

*Installing the required packages*

You need to have Python (at least 2.5 for OpenERP v6.0) in your Ubuntu system, which is in-built in Ubuntu version 10.04
and above.

You also need to install the following Python libraries, because OpenERP Client uses these packages.

To install the required libraries on your Ubuntu system, you can do the following in your favourite shell:


* :guilabel:`gtk` : GTK+ is a highly usable, feature-rich toolkit for creating graphical user interfaces which boosts cross-platform compatibility and an easy-to-use API. ::

					sudo apt-get install python-gtk2

* :guilabel:`glade` : Glade is a RAD tool to enable quick & easy development of user interfaces for the GTK+ toolkit and the GNOME desktop environment. ::

					sudo apt-get install python-glade2

* :guilabel:`matplotlib` : matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hard-copy formats and interactive environments across platforms. ::

					sudo apt-get install python-matplotlib

* :guilabel:`mxdatetime` : Provides the most natural and robust way of dealing with date/time values in Python. ::

					sudo apt-get install python-egenix-mxdatetime

* :guilabel:`xml` : XML support for Python platform. ::

					sudo apt-get install python-xml

* :guilabel:`tz` : World Timezone definitions for Python. ::

					sudo apt-get install python-tz

* :guilabel:`hippocanvas` : The Hippo Canvas is a Cairo/GObject/GTK+ based canvas, written in C with support for flexible layout, CSS styling, and initial work on animations. ::

					sudo apt-get install python-hippocanvas

* :guilabel:`pydot` : Python interface to Graphviz's Dot language. ::

                    sudo apt-get install python-pydot

.. note:: PDF Viewer

    You will also need a PDF viewer (e.g. xpdf, acroread, kpdf). See *Configuring a PDF Viewer* below.

*Downloading the OpenERP Client*

The OpenERP client can be downloaded from OpenERP website's download page <http://www.openerp.com/downloads>.

*Testing the OpenERP Client*

If you only want to test the client, you do not need to install it. Just unpack the
archive and start the openerp-client executable: ::

        tar -xzf openerp-client-6.0.0.tar.gz
        cd openerp-client-6.0.0/bin
        python openerp-client.py

The list of available command line parameters can be obtained with the ``-h``
command-line switch: ::

    python openerp-client.py -h

*Installing the OpenERP Client*

The client can be installed very easily using the *setup.py* file: ::

  tar -xzf openerp-client-6.0.0.tar.gz
  cd openerp-client-6.0.0
  sudo python setup.py install

You can now run the client using the following command: ::

  openerp-client

.. index::
   single: OpenERP Client; Configuring a PDF viewer
   single: PDF viewer
..

.. _configure-pdf-viewer-link:

*Configuring a PDF Viewer*

To preview PDF files, OpenERP Client by default supports:

 #. evince
 #. xpdf
 #. gpdf
 #. kpdf
 #. epdfview
 #. acroread

The client will try to find one of these executables (in this order) in
your system and open the PDF document with it.

.. note:: PDF

    For example, if *xpdf*, *kpdf* and *acroread* are the only PDF viewers installed
    on your system, the OpenERP client will use *xpdf* for previewing PDF documents.

If you  want to use another PDF viewer or if you do not want to use the first
one the client will find, you have to edit the OpenERP configuration file, normally
located in ``~/.openerprc``. Find the ``[printer]`` section and edit the
``softpath`` parameter. For example: ::

    [printer]
    softpath = kpdf

