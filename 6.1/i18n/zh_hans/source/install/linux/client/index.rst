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

OpenERP GTK 客户端安装
===============================

.. i18n: The native GTK client is available as a legacy interface for users who still require it, but the recommended way to access OpenERP 6.1 is the built-in web interface.
..

原生的GTK客户端是历史遗留物，会继续为仍有需要的用户服务，但推荐用内置的web界面来访问OpenERP 6.1。

.. i18n: Installing the required packages
.. i18n: --------------------------------
..

安装需要的包
--------------------------------

.. i18n: Python 2.6 or later is required for OpenERP 6.1. It is built-in in Ubuntu version 10.04 and above.
.. i18n: A few Python libraries are also required, as listed below.
..
 
OpenERP 6.1要求Python 2.6 或以上版本。 在Ubuntu 10.04 及以上版本系统已自带。 还有几个Python库是需要的，下面会列举出来。

.. i18n: On a Debian-based Linux distribution you can install all required dependencies with this single
.. i18n: command::
.. i18n: 
.. i18n:     apt-get install python-gtk2 python-glade2 python-matplotlib python-dateutil \
.. i18n:         python-lxml python-tz python-hippocanvas python-pydot
..

在基于 Debian 的 Linux 发行版中，可能用这样的单个命令来安装所有要求的依赖包::

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

* 任意的 PDF 浏览器，在系统中适度注册，以便能自动打开 PDF 文件 (例如 xpdf, kpdf, acroread, evince, 等等)。
  请看 :ref:`configure-pdf-viewer-link` 一节.

.. i18n: .. note:: RedHat-based distributions
.. i18n: 
.. i18n:     As an alternative to the above commands meant for Debian-based distributions, the
.. i18n:     following command should install the required dependencies for RedHat-based systems::
.. i18n: 
.. i18n:         yum install pygtk2 glade3 pydot python-dateutil python-matplotlib \
.. i18n:             python-lxml python-hippo-canvas python-tz
..

.. note:: 基于RedHat的发行版

    替代上面用在 基于Debian发行版的命令,
    下面的命令将安装基于RedHat 的系统所需要的依赖 ::

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

    替代上面用在 基于Debian发行版的命令,
    下面的命令将安装Mandriva系统所需要的依赖  ::

        yum install pygtk2 glade3 pydot python-dateutil python-matplotlib \
            python-lxml python-hippo-canvas python-tz

.. i18n: Downloading the OpenERP Client
.. i18n: ------------------------------
..

下载 OpenERP 客户端
------------------------------

.. i18n: The OpenERP client can be downloaded from
.. i18n: the `OpenERP website's download page <http://www.openerp.com/downloads>`_
..

OpenERP 客户端能从 `OpenERP 网站的下载页面 <http://www.openerp.com/downloads>`_  下载。

.. i18n: Testing the OpenERP Client
.. i18n: --------------------------
..

测试 OpenERP 客户端
--------------------------

.. i18n: If you only want to test the client, you do not need to install it. Just unpack the
.. i18n: archive and start the openerp-client executable: ::
.. i18n: 
.. i18n:         tar -xzf openerp-client-6.1-latest.tar.gz
.. i18n:         cd openerp-client-6.1-*/bin
.. i18n:         ./openerp-client.py
..

如果你只是要测试客户端, 你不必安装，只要解包并启动 openerp客户端的执行文件: ::

        tar -xzf openerp-client-6.1-latest.tar.gz
        cd openerp-client-6.1-*/bin
        ./openerp-client.py

.. i18n: The list of available command line parameters can be obtained with the ``-h``
.. i18n: command-line switch: ::
.. i18n: 
.. i18n:     ./openerp-client.py -h
..

使用 ``-h`` 命令行开关能获得一个可用的命令行参数的列表: ::

    ./openerp-client.py -h

.. i18n: Installing the OpenERP Client
.. i18n: -----------------------------
..

安装OpenERP 客户端
-----------------------------

.. i18n: The client can be installed very easily using the *setup.py* file: ::
.. i18n: 
.. i18n:   tar -xzf openerp-client-6.1-latest.tar.gz
.. i18n:   cd openerp-client-6.1-*
.. i18n:   sudo python setup.py install
..

客户端可以非常容易地用 *setup.py* 文件安装: ::

  tar -xzf openerp-client-6.1-latest.tar.gz
  cd openerp-client-6.1-*
  sudo python setup.py install

.. i18n: You can now run the client using the following command: ::
.. i18n: 
.. i18n:   openerp-client
..

你能用下列命令运行客户端: ::

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

配置 PDF 浏览器
------------------------

.. i18n: By default the OpenERP Client will use your default PDF application
.. i18n: for displaying PDF files  You may customize this behavior by configuring
.. i18n: a different default PDF application on your system.
..

默认时， OpenERP 客户端将使用默认的 PDF 应用程序来显
示 PDF 文件。你可以在系统中配置一个不一样的默认PDF应用来定制此行为。

.. i18n: Alternatively, you may also specify explicitly the PDF command to use to
.. i18n: display PDF files in the OpenERP configuration file, normally located in your
.. i18n: HOME directory, and named ``'.openerprc'``.
.. i18n: Find the ``[printer]`` section and edit the ``softpath`` parameter. For example: ::
.. i18n: 
.. i18n:     [printer]
.. i18n:     softpath = kpdf
..

作为选择，你也能在配置文件明确指定一个 PDF 指令用来显示PDF 文件，
通常此文件保存在HOME目录，命名为 ``'.openerprc'`` 。
找到 ``[printer]`` 节并编辑 ``softpath`` 参数。例如: ::

    [printer]
    softpath = kpdf
