
.. i18n: .. index::
.. i18n:    single: Installation; OpenERP Client (Linux)
.. i18n:    single: OpenERP Client; Installation (Linux)
.. i18n: ..
..

.. index::
   single: Installation; OpenERP Client (Linux)
   single: OpenERP Client; Installation (Linux)
..

.. i18n: .. linux-client-link:
..

.. linux-client-link:

.. i18n: OpenERP GTK Client Installation
.. i18n: ===============================
..

OpenERP GTK Client Installation
===============================

.. i18n: The native GTK client is available as a legacy interface for users who still require it, but the recommended way to access OpenERP 6.1 is the built-in web interface.
..

The native GTK client is available as a legacy interface for users who still require it, but the recommended way to access OpenERP 6.1 is the built-in web interface.

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
.. i18n:     apt-get install python-gtk2 python-glade2 python-matplotlib python-dateutil \
.. i18n:         python-lxml python-tz python-hippocanvas python-pydot
..

On a Debian-based Linux distribution you can install all required dependencies with this single
command::

    apt-get install python-gtk2 python-glade2 python-matplotlib python-dateutil \
        python-lxml python-tz python-hippocanvas python-pydot

.. i18n: * :guilabel:`gtk` : GTK+ is a highly usable, feature-rich toolkit for creating graphical user interfaces which boosts cross-platform compatibility and an easy-to-use API. ::
.. i18n: 
.. i18n: 					sudo apt-get install python-gtk2
.. i18n: 
.. i18n: * :guilabel:`glade` : Glade is a RAD tool to enable quick & easy development of user interfaces for the GTK+ toolkit and the GNOME desktop environment. ::
.. i18n: 
.. i18n: 					sudo apt-get install python-glade2
.. i18n: 
.. i18n: * :guilabel:`matplotlib` : matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hard-copy formats and interactive environments across platforms. ::
.. i18n: 
.. i18n: 					sudo apt-get install python-matplotlib
.. i18n: 
.. i18n: * :guilabel:`dateutil` : Provides date/time values in Python ::
.. i18n: 
.. i18n: 					sudo apt-get install python-dateutil
.. i18n: 
.. i18n: * :guilabel:`lxml` : XML support for Python platform. ::
.. i18n: 
.. i18n: 					sudo apt-get install python-lxml
.. i18n: 
.. i18n: * :guilabel:`tz` : World Timezone definitions for Python. ::
.. i18n: 
.. i18n: 					sudo apt-get install python-tz
.. i18n: 
.. i18n: * :guilabel:`hippocanvas` : The Hippo Canvas is a Cairo/GObject/GTK+ based canvas, written in C with support for flexible layout, CSS styling, and initial work on animations. ::
.. i18n: 
.. i18n: 					sudo apt-get install python-hippocanvas
.. i18n: 
.. i18n: * :guilabel:`pydot` : Python interface to Graphviz's Dot language. ::
.. i18n: 
.. i18n:                     sudo apt-get install python-pydot
.. i18n: 
.. i18n: * Any PDF viewer, properly registered in your system to automatically open PDF files (e.g. xpdf, kpdf, acroread, evince, etc..).
.. i18n:   See the :ref:`configure-pdf-viewer-link` section.
..

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

.. i18n: .. note:: RedHat-based distributions
.. i18n: 
.. i18n:     As an alternative to the above commands meant for Debian-based distributions, the
.. i18n:     following command should install the required dependencies for RedHat-based systems::
.. i18n: 
.. i18n:         yum install pygtk2 glade3 pydot python-dateutil python-matplotlib \
.. i18n:             python-lxml python-hippo-canvas python-tz
..

.. note:: RedHat-based distributions

    As an alternative to the above commands meant for Debian-based distributions, the
    following command should install the required dependencies for RedHat-based systems::

        yum install pygtk2 glade3 pydot python-dateutil python-matplotlib \
            python-lxml python-hippo-canvas python-tz

.. i18n: .. note:: Mandriva
.. i18n: 
.. i18n:     As an alternative to the above commands meant for Debian-based distributions, the
.. i18n:     following command should install the required dependencies for Mandriva::
.. i18n: 
.. i18n:         yum install pygtk2 glade3 pydot python-dateutil python-matplotlib \
.. i18n:             python-lxml python-hippo-canvas python-tz
..

.. note:: Mandriva

    As an alternative to the above commands meant for Debian-based distributions, the
    following command should install the required dependencies for Mandriva::

        yum install pygtk2 glade3 pydot python-dateutil python-matplotlib \
            python-lxml python-hippo-canvas python-tz

.. i18n: Downloading the OpenERP Client
.. i18n: ------------------------------
..

Downloading the OpenERP Client
------------------------------

.. i18n: The OpenERP client can be downloaded from
.. i18n: the `OpenERP website's download page <http://www.openerp.com/downloads>`_
..

The OpenERP client can be downloaded from
the `OpenERP website's download page <http://www.openerp.com/downloads>`_

.. i18n: Testing the OpenERP Client
.. i18n: --------------------------
..

Testing the OpenERP Client
--------------------------

.. i18n: If you only want to test the client, you do not need to install it. Just unpack the
.. i18n: archive and start the openerp-client executable: ::
.. i18n: 
.. i18n:         tar -xzf openerp-client-6.1-latest.tar.gz
.. i18n:         cd openerp-client-6.1-*/bin
.. i18n:         ./openerp-client.py
..

If you only want to test the client, you do not need to install it. Just unpack the
archive and start the openerp-client executable: ::

        tar -xzf openerp-client-6.1-latest.tar.gz
        cd openerp-client-6.1-*/bin
        ./openerp-client.py

.. i18n: The list of available command line parameters can be obtained with the ``-h``
.. i18n: command-line switch: ::
.. i18n: 
.. i18n:     ./openerp-client.py -h
..

The list of available command line parameters can be obtained with the ``-h``
command-line switch: ::

    ./openerp-client.py -h

.. i18n: Installing the OpenERP Client
.. i18n: -----------------------------
..

Installing the OpenERP Client
-----------------------------

.. i18n: The client can be installed very easily using the *setup.py* file: ::
.. i18n: 
.. i18n:   tar -xzf openerp-client-6.1-latest.tar.gz
.. i18n:   cd openerp-client-6.1-*
.. i18n:   sudo python setup.py install
..

The client can be installed very easily using the *setup.py* file: ::

  tar -xzf openerp-client-6.1-latest.tar.gz
  cd openerp-client-6.1-*
  sudo python setup.py install

.. i18n: You can now run the client using the following command: ::
.. i18n: 
.. i18n:   openerp-client
..

You can now run the client using the following command: ::

  openerp-client

.. i18n: .. index::
.. i18n:    single: OpenERP Client; Configuring a PDF viewer
.. i18n:    single: PDF viewer
.. i18n: ..
..

.. index::
   single: OpenERP Client; Configuring a PDF viewer
   single: PDF viewer
..

.. i18n: .. _configure-pdf-viewer-link:
.. i18n: 
.. i18n: Configuring a PDF Viewer
.. i18n: ------------------------
..

.. _configure-pdf-viewer-link:

Configuring a PDF Viewer
------------------------

.. i18n: By default the OpenERP Client will use your default PDF application
.. i18n: for displaying PDF files  You may customize this behavior by configuring
.. i18n: a different default PDF application on your system.
..

By default the OpenERP Client will use your default PDF application
for displaying PDF files  You may customize this behavior by configuring
a different default PDF application on your system.

.. i18n: Alternatively, you may also specify explicitly the PDF command to use to
.. i18n: display PDF files in the OpenERP configuration file, normally located in your
.. i18n: HOME directory, and named ``'.openerprc'``.
.. i18n: Find the ``[printer]`` section and edit the ``softpath`` parameter. For example: ::
.. i18n: 
.. i18n:     [printer]
.. i18n:     softpath = kpdf
..

Alternatively, you may also specify explicitly the PDF command to use to
display PDF files in the OpenERP configuration file, normally located in your
HOME directory, and named ``'.openerprc'``.
Find the ``[printer]`` section and edit the ``softpath`` parameter. For example: ::

    [printer]
    softpath = kpdf
