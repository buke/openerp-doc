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

OpenERP 服务器安装
===========================

.. i18n: Installing the required packages
.. i18n: --------------------------------
..

安装所需要的包
--------------------------------

.. i18n: Python 2.6 or later is required for OpenERP 6.1. It is built-in in Ubuntu version 10.04 and above.
.. i18n: A few Python libraries are also required, as listed below.
..

OpenERP 6.1要求Python 2.6 或更新. 这已经内建在 Ubuntu 10.04 及之上.
还需有几个Python库，已经列表于下.

.. i18n: On a Debian-based Linux distribution you can install all required dependencies with this single
.. i18n: command::
.. i18n: 
.. i18n:     apt-get install python-dateutil python-feedparser python-gdata python-ldap \
.. i18n:         python-libxslt1 python-lxml python-mako python-openid python-psycopg2 \
.. i18n:         python-pybabel python-pychart python-pydot python-pyparsing python-reportlab \
.. i18n:         python-simplejson python-tz python-vatnumber python-vobject python-webdav \
.. i18n:         python-werkzeug python-xlwt python-yaml python-zsi
..

在基于Debian 的 Linux 发行版，你能用下面一条指令安装所有依赖::

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

* :guilabel:`dateutil` : 此模块提供了强大的扩展以处理标准日期时间，用于 Python 2.3+. ::

                    sudo apt-get install python-dateutil

* :guilabel:`feedparser` : 用于Python 的通用聚合解析器 ::

                    sudo apt-get install python-feedparser

* :guilabel:`gdata` : Google Data Python 客户端库 ::

                    sudo apt-get install python-gdata

* :guilabel:`ldap` : LDAP 接口 module ::

                    sudo apt-get install python-ldap

* :guilabel:`libxslt1` : Python bindings for XSLT transformation library ::

                    sudo apt-get install python-libxslt1

* :guilabel:`lxml` : lxml 是个具有丰富特性且易用的库， 用于 Python 语言处理 XML 和 HTML. ::

					sudo apt-get install python-lxml

* :guilabel:`mako` : 用于 python平台的快速、轻量的模版. ::

					sudo apt-get install python-mako

* :guilabel:`openid` : OpenID 身份认证，支持服务器和消费者 ::

                    sudo apt-get install python-openid

* :guilabel:`psycopg2` : 最大众化的python PostgreSQL 接口. ::

					sudo apt-get install python-psycopg2

* :guilabel:`babel` : Python 应用的国际化工具 ::

                    sudo apt-get install python-pybabel

* :guilabel:`pychart` :  封装了 Postscript, PDF, PNG, or SVG charts 的高质量的库. ::

					sudo apt-get install python-pychart

* :guilabel:`pydot` :  提供了 Graphviz's dot language的完整的特性，包括创建，保存，修改，处理图像. ::

					sudo apt-get install python-pydot

* :guilabel:`pyparsing` : 解析 Python 代码的库 ::

                    sudo apt-get install python-pyparsing

* :guilabel:`reportlab` : ReportLab 工具是个经时间证明，超强，开源的引擎，以 RML 为基础，用于 编程创建 PDF 文档和 and 表格L. 也包括了一个创建平台无关的向量图像的库.是用 python 写成的一个快速、灵活、可伸缩、交叉平台解决方案。 ::

                    sudo apt-get install python-reportlab

* :guilabel:`simplejson` : 简单，快速，可扩展的 JSON 编码和解码器 ::

                    sudo apt-get install python-simplejson

* :guilabel:`vatnumber` :  用于欧洲国家的检查 VAT（增值税号）的模块 ::

                    sudo apt-get install python-vatnumber

* :guilabel:`vobject` : VObject simplifies the process of parsing and creating iCalendar and vCard objects. ::

                    sudo apt-get install python-vobject

* :guilabel:`pytz` : 用于的 世界时区定义 ::

					sudo apt-get install python-tz

* :guilabel:`webdav` : 用python 实现的 WebDAV 服务器 ::

                    sudo apt-get install python-webdav

* :guilabel:`werkzeug` : WSGI应用程序 工具集合 ::

                    sudo apt-get install python-werkzeug

* :guilabel:`yaml` : 用于 Python 的 YAML 解析器和发射器。 ::

					sudo apt-get install python-yaml

* :guilabel:`xlwt` : 读写 Microsoft Excel 电子表格文件的模块 ::

                    sudo apt-get install python-xlwt

* :guilabel:`zsi` :  Zolera Soap 客户端基础 ::

                    sudo apt-get install python-zsi

.. i18n: Downloading the OpenERP Server
.. i18n: ------------------------------
..

下载 OpenERP 服务器
------------------------------

.. i18n: The OpenERP server can be downloaded from
.. i18n: the `OpenERP website's download page <http://www.openerp.com/downloads>`_
..

OpenERP 服务器可从这里下
载 `OpenERP 网站的下载页面 <http://www.openerp.com/downloads>`_

.. i18n: Testing the OpenERP Server
.. i18n: --------------------------
..

测试 OpenERP 服务器
--------------------------

.. i18n: If you only want to test the server, you do not need to install it. Just unpack the archive and start
.. i18n: the openerp-server executable: ::
.. i18n: 
.. i18n:         tar -xzf openerp-6.1-latest.tar.gz
.. i18n:         cd openerp-6.1-*
.. i18n:         ./openerp-server
..

如果你只想测试服务器, 你不需要安装它.仅仅解包并
启动  openerp-server 执行文件即可: ::

        tar -xzf openerp-6.1-latest.tar.gz
        cd openerp-6.1-*
        ./openerp-server

.. i18n: The list of available command line parameters can be obtained with the ``-h``
.. i18n: command-line switch: ::
.. i18n: 
.. i18n:     openerp-server -h
..

可用的下面的命令行参数列表能通过 命令行开关 ``-h`` 获得: ::

    openerp-server -h

.. i18n: Installing the OpenERP Server
.. i18n: -----------------------------
..

安装 OpenERP 服务器
-----------------------------

.. i18n: The OpenERP Server can be installed very easily using the *setup.py* file: ::
.. i18n: 
.. i18n:     tar -xzf openerp-6.1-latest.tar.gz
.. i18n:     cd openerp-6.1-*
.. i18n:     sudo python setup.py install
..

OpenERP 服务器能非常容易地使用 *setup.py* 文件安装: ::

    tar -xzf openerp-6.1-latest.tar.gz
    cd openerp-6.1-*
    sudo python setup.py install

.. i18n: If your PostgreSQL server is up and running, you can now run the server using
.. i18n: the following command: ::
.. i18n: 
.. i18n:     openerp-server
..

如果 PostgreSQL 服务器已经启动并正在运行，你能用下列命令运行OpenERP 服务器: ::

    openerp-server

.. i18n: If you do not already have a PostgreSQL server up and running, you can read
.. i18n: :ref:`installation-postgresql-server`.
..

如果你还没有启动 PostgreSQL 服务器并运行，请参阅 :ref:`installation-postgresql-server`.

.. i18n: Creating a configuration file for OpenERP Server
.. i18n: ------------------------------------------------
..

创建 OpenERP 服务器配置文件
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

你能用 ``-s`` 选项启动OpenERP服务器 用默认的选项 创建一个配置文件，然后进行修改。 
配置文件参数类似服务器的启动参数。如果你不能确定一个参数是干啥的，可以用命
令 ``openerp -h`` 看看该参数是干啥的 ::

    ./openerp-server -s -c <config_file_path>
    # 现在编辑 <config_file_path> 中的配置文件
    # 用 -h 选项输出更多的明细说明...
    ./openerp-server -h
    (...)
    # 最后，用所需的配置文件启动服务器
    ./openerp-server -c <config_file_path>

.. i18n: Default Configuration file
.. i18n: ++++++++++++++++++++++++++
.. i18n: The default OpenERP configuration file is located in ``$HOME/.openerp_serverrc``,
.. i18n: that is a file named ``.openerp_serverrc`` in the home directory of the
.. i18n: system user under which OpenERP runs.
.. i18n: This is the default value for the ``-c`` startup parameter. 
..

默认的配置文件
++++++++++++++++++++++++++
默认的OpenERP文件存放于 ``$HOME/.openerp_serverrc``,
是运行OpenERP的系统用户的Home 目录中，其名称为 ``.openerp_serverrc`` 。
这是 ``-c`` 启动参数的默认值。
