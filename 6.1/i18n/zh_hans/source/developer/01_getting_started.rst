.. i18n: =========================================
.. i18n: Getting starting with OpenERP development
.. i18n: =========================================
..

=================
OpenERP 开发入门
=================

.. i18n: .. toctree::
.. i18n:     :maxdepth: 1
..

.. toctree::
    :maxdepth: 1

.. i18n: Installation
.. i18n: ============
..

安装
============

.. i18n: Windows
.. i18n: -------
..

Windows下安装
-------------

.. i18n: Windows install:
.. i18n:  - executable location
.. i18n:  - howto
..

Windows 下安装:
 - 执行位置
 - 步骤

.. i18n: Debian/Ubuntu
.. i18n: -------------
..

Debian/Ubuntu安装
-----------------

.. i18n: How to get .deb packages
..

 .deb packages安装包下载

.. i18n: Sources
.. i18n: -------
..

源码
----

.. i18n: In order to get the sources, you will need Bazaar version control to pull the source from Launchpad. Check how to get Bazaar according to your development environment. After having installed and configured Bazaar, setup your development environment by typing::
.. i18n: 
.. i18n:   mkdir source;cd source
..

为了获取源代码,您将需要使用版本控制工具从Launchpad检出源码。根据你的开发环境检查如何得到Bazaar。Bazaar,安装和配置后,设置您的开发环境中通过输入如下命令（自行定义目录名称）::

  mkdir source;cd source

.. i18n: Get the setup script of OpenERP by typing::
.. i18n: 
.. i18n:   bzr cat -d lp:~openerp-dev/openerp-tools/trunk setup.sh | sh
..

输入下面的命令从官网源码获取安装脚本::

  bzr cat -d lp:~openerp-dev/openerp-tools/trunk setup.sh | sh

.. i18n: Get the current trunk version of OpenERP by typing::
.. i18n: 
.. i18n:   make init-trunk
..

下面命令从官网源码获取当前代码分支::

  make init-trunk

.. i18n: The makefile contains other options. For details about options, please type::
.. i18n: 
.. i18n:   make
..

mark命令通过如下命令可以查看其它关于mark命令的选项::

  make

.. i18n: Some dependencies are necessary to use OpenERP. Depending on your environment, you might have to install the following packets::
.. i18n: 
.. i18n:   sudo apt-get install graphviz ghostscript postgresql python-imaging python-matplotlib 
..

为使用 OpenERP 需要安装一些依赖包。根据您的环境，可能需要安装以下包::
  sudo apt-get install graphviz ghostscript postgresql python-imaging python-matplotlib 

.. i18n: You then have to initialise the database. This will create a new openerp role::
.. i18n: 
.. i18n:   make db-setup
..

然后你需要初始化一个数据库.这样将创建一个新的openerp角色::

  make db-setup

.. i18n: Finally, launch the OpenERP server::
.. i18n: 
.. i18n:   make server
..

最后运行 OpenERP 服务::

  make server

.. i18n: Testing your installation can be done on http://localhost:8069/
..

可以通过 http://localhost:8069/ 可以测试你的安装

.. i18n: Development version
.. i18n: -------------------
..

开发版
-------------------

.. i18n: Location of development version + specifics if necessary to precise
..

如需要精确位置，开发版本+细节。

.. i18n: Configuration
.. i18n: =============
..

配置
=============

.. i18n: .. _configuration-files-link:
.. i18n: 
.. i18n: Two configuration files are available:
..

.. _configuration-files-link:

有2种配置文件：

.. i18n:     * one for the client: ~/.openerprc
.. i18n:     * one for the server: ~/.openerp_serverrc
..

    * 客户端配置: ~/.openerprc
    * 服务端配置: ~/.openerp_serverrc

.. i18n: Those files follow the convention used by python's ConfigParser module.
..

这些文件按照 python ConfigParser 模块惯例设置。

.. i18n: Lines beginning with "#" or ";" are comments.
..

以"#"或者";"进行行注释。

.. i18n: The client configuration file is automatically generated upon the first start. The one of the server can automatically be created using the command: ::
.. i18n: 
.. i18n:   openerp-server.py -s
..

客户端第一次启动会自动生成配置文件。
服务端配置文件可以使用下面命令生成: ::
  openerp-server.py -s

.. i18n: If they are not found, the server and the client will start with the default configuration.
..

如果上面的配置文件不存在，服务端和客户端将按照默认配置启动。

.. i18n: **Server Configuration File**
..

**Server 配置文件**

.. i18n: The server configuration file .openerp_serverrc is used to save server startup options. Here is the list of the available options:
..

服务端配置文件  .openerp_serverrc  用于保存服务启动参数。
以下是可用的参数:

.. i18n: :interface:
.. i18n:     Address to which the server will be bound 
..

:interface:
    绑定监听IP地址

.. i18n: :port:
.. i18n:     Port the server will listen on 
..

:port:
    监听端口

.. i18n: :database:
.. i18n:     Name of the database to use 
..

:database:
    数据库名称

.. i18n: :user:
.. i18n:     Username used when connecting to the database 
..

:user:
    数据库连接帐号用户名

.. i18n: :translate_in:
.. i18n:     File used to translate OpenERP to your language 
..

:translate_in:
    导入翻译文件

.. i18n: :translate_out:
.. i18n:     File used to export the language OpenERP use 
..

:translate_out:
    导出翻译文件

.. i18n: :language:
.. i18n:     Use this language as the language of the server. This must be specified as an ISO country code, as specified by the W3C. 
..

:language:
    默认载入语言. 必须是符合 W3C 标准的 ISO 国家代码，

.. i18n: :verbose:
.. i18n:     Enable debug output 
..

:verbose:
    开启调试输出

.. i18n: :init:
.. i18n:     init a module (use "all" for all modules) 
..

:init:
    初始化模块("all"为所有模块)

.. i18n: :update:
.. i18n:     update a module (use "all" for all modules) 
..

:update:
    更新模块("all"为所有模块)

.. i18n: :upgrade:
.. i18n:     Upgrade/install/uninstall modules 
..

:upgrade:
    升级/安装/卸载 模块

.. i18n: :db_name:
.. i18n:     specify the database name 
..

:db_name:
    指定数据库名称

.. i18n: :db_user:
.. i18n:     specify the database user name 
..

:db_user:
    指定数据库用户名

.. i18n: :db_password:
.. i18n:     specify the database password 
..

:db_password:
    指定数据库用户密码

.. i18n: :pg_path:
.. i18n:     specify the pg executable path 
..

:pg_path:
    指定PostgreSQL数据库维护可执行文件路径

.. i18n: :db_host:
.. i18n:     specify the database host 
..

:db_host:
    PG数据库主机名

.. i18n: :db_port:
.. i18n:     specify the database port 
..

:db_port:
    PG 数据库端口

.. i18n: :translate_modules:
.. i18n:     Specify modules to export. Use in combination with --i18n-export 
..

:translate_modules:
    指定导出模块，与 --i18n-export 参数一起使用

.. i18n: You can create your own configuration file by specifying -s or --save on the server command line. If you would like to write an alternative configuration file, use -c <config file> or --config=<config file>
.. i18n: Here is a basic configuration for a server::
.. i18n: 
.. i18n:         [options]
.. i18n:         verbose = False
.. i18n:         xmlrpc = True
.. i18n:         database = terp
.. i18n:         update = {}
.. i18n:         port = 8069
.. i18n:         init = {}
.. i18n:         interface = 127.0.0.1
.. i18n:         reportgz = False
..

通过指定  -s 或 --save 参数从命令行启动服务，可以创建你自己的配置文件。
你也可以使用 -c <配置文件路径> 或 --config=<配置文件路径> 参数，加载配置文件启动服务。
以下是基本的服务端配置::

        [options]
        verbose = False
        xmlrpc = True
        database = terp
        update = {}
        port = 8069
        init = {}
        interface = 127.0.0.1
        reportgz = False

.. i18n: Full Example for Server V5.0 ::
.. i18n: 
.. i18n:         [printer]
.. i18n:         path = none
.. i18n:         softpath_html = none
.. i18n:         preview = True
.. i18n:         softpath = none
.. i18n: 
.. i18n:         [logging]
.. i18n:         output = stdout
.. i18n:         logger = 
.. i18n:         verbose = True
.. i18n:         level = error
.. i18n: 
.. i18n:         [help]
.. i18n:         index = http://www.openerp.com/documentation/user-manual/
.. i18n:         context = http://www.openerp.com/scripts/context_index.php
.. i18n: 
.. i18n:         [form]
.. i18n:         autosave = False
.. i18n:         toolbar = True
.. i18n: 
.. i18n:         [support]
.. i18n:         recipient = support@openerp.com
.. i18n:         support_id = 
.. i18n: 
.. i18n:         [tip]
.. i18n:         position = 0
.. i18n:         autostart = False
.. i18n: 
.. i18n:         [client]
.. i18n:         lang = en_US
.. i18n:         default_path = /home/user
.. i18n:         filetype = {}
.. i18n:         theme = none
.. i18n:         toolbar = icons
.. i18n:         form_tab_orientation = 0
.. i18n:         form_tab = top
.. i18n: 
.. i18n:         [survey]
.. i18n:         position = 3
.. i18n: 
.. i18n:         [path]
.. i18n:         pixmaps = /usr/share/pixmaps/openerp-client/
.. i18n:         share = /usr/share/openerp-client/
.. i18n: 
.. i18n:         [login]
.. i18n:         db = eo2
.. i18n:         login = admin
.. i18n:         protocol = http://
.. i18n:         port = 8069
.. i18n:         server = localhost
..

完整例子 Server V5.0 ::

        [printer]
        path = none
        softpath_html = none
        preview = True
        softpath = none

        [logging]
        output = stdout
        logger = 
        verbose = True
        level = error

        [help]
        index = http://www.openerp.com/documentation/user-manual/
        context = http://www.openerp.com/scripts/context_index.php

        [form]
        autosave = False
        toolbar = True

        [support]
        recipient = support@openerp.com
        support_id = 

        [tip]
        position = 0
        autostart = False

        [client]
        lang = en_US
        default_path = /home/user
        filetype = {}
        theme = none
        toolbar = icons
        form_tab_orientation = 0
        form_tab = top

        [survey]
        position = 3

        [path]
        pixmaps = /usr/share/pixmaps/openerp-client/
        share = /usr/share/openerp-client/

        [login]
        db = eo2
        login = admin
        protocol = http://
        port = 8069
        server = localhost

.. i18n: Command line options
.. i18n: ====================
..

指定运行时命令行参数
====================

.. i18n: General Options
.. i18n: ---------------
..

常规参数
---------------

.. i18n:   --version             show program version number and exit
.. i18n:   -h, --help            show this help message and exit
.. i18n:   -c CONFIG, --config=CONFIG
.. i18n:                         specify alternate config file
.. i18n:   -s, --save            save configuration to ~/.terp_serverrc
.. i18n:   -v, --verbose         enable debugging
.. i18n:   --pidfile=PIDFILE     file where the server pid will be stored
.. i18n:   --logfile=LOGFILE     file where the server log will be stored
.. i18n:   -n INTERFACE, --interface=INTERFACE
.. i18n:                         specify the TCP IP address
.. i18n:   -p PORT, --port=PORT  specify the TCP port
.. i18n:   --net_interface=NETINTERFACE
.. i18n:                         specify the TCP IP address for netrpc
.. i18n:   --net_port=NETPORT    specify the TCP port for netrpc
.. i18n:   --no-netrpc           disable netrpc
.. i18n:   --no-xmlrpc           disable xmlrpc
.. i18n:   -i INIT, --init=INIT  init a module (use "all" for all modules)
.. i18n:   --without-demo=WITHOUT_DEMO
.. i18n:                         load demo data for a module (use "all" for all
.. i18n:                         modules)
.. i18n:   -u UPDATE, --update=UPDATE
.. i18n:                         update a module (use "all" for all modules)
.. i18n:   --stop-after-init     stop the server after it initializes
.. i18n:   --debug               enable debug mode
.. i18n:   -S, --secure          launch server over https instead of http
.. i18n:   --smtp=SMTP_SERVER    specify the SMTP server for sending mail
.. i18n:  
.. i18n: Database related options:
.. i18n: -------------------------
.. i18n:  
.. i18n:   -d DB_NAME, --database=DB_NAME
.. i18n:                         specify the database name
.. i18n:   -r DB_USER, --db_user=DB_USER
.. i18n:                         specify the database user name
.. i18n:   -w DB_PASSWORD, --db_password=DB_PASSWORD
.. i18n:                         specify the database password
.. i18n:   --pg_path=PG_PATH   specify the pg executable path
.. i18n:   --db_host=DB_HOST   specify the database host
.. i18n:   --db_port=DB_PORT   specify the database port
.. i18n:  
.. i18n: Internationalization options:
.. i18n: -----------------------------
..

  --version             显示版本信息，然后结束
  -h, --help            显示帮助信息，然后结束
  -c CONFIG, --config=CONFIG
                        指定配置文件
  -s, --save            保存配置文件到 ~/.terp_serverrc
  -v, --verbose         开启调试模式
  --pidfile=PIDFILE     存储服务启动的 PID 文件
  --logfile=LOGFILE     存储LOG的文件
  -n INTERFACE, --interface=INTERFACE
                        监听IP地址
  -p PORT, --port=PORT  监听 TCP 端口
  --net_interface=NETINTERFACE
                        netrpc 监听IP地址
  --net_port=NETPORT    netrpc 监听端口
  --no-netrpc           禁止 netrpc 协议
  --no-xmlrpc           禁止 xmlrpc 协议
  -i INIT, --init=INIT  初始化模块 ("all" 参数为初始化所有模块)
  --without-demo=WITHOUT_DEMO
                        加载 demo 数据 ( "all" 参数为加载所有模块的demo 数据)
  -u UPDATE, --update=UPDATE
                        升级模块 ( "all" 参数为升级所有模块)
  --stop-after-init     初始化后停止运行
  --debug               开启调试模式
  -S, --secure          https 协议
  --smtp=SMTP_SERVER    SMTP 服务器
 
数据库相关参数:
-------------------------
 
  -d DB_NAME, --database=DB_NAME
                        指定数据库名
  -r DB_USER, --db_user=DB_USER
                        数据库用户名
  -w DB_PASSWORD, --db_password=DB_PASSWORD
                        数据库密码
  --pg_path=PG_PATH   PG bin 路径
  --db_host=DB_HOST   数据库主机名或IP地址
  --db_port=DB_PORT   数据库端口
 
多语言相关参数:
-----------------------------

.. i18n:     Use these options to translate OpenERP to another language. See i18n
.. i18n:     section of the user manual. Option '-l' is mandatory.
.. i18n:  
.. i18n:   -l LANGUAGE, --language=LANGUAGE
.. i18n:                        specify the language of the translation file. Use it
.. i18n:                        with --i18n-export and --i18n-import
.. i18n:   --i18n-export=TRANSLATE_OUT
.. i18n:                        export all sentences to be translated to a CSV file
.. i18n:                        and exit
.. i18n:   --i18n-import=TRANSLATE_IN
.. i18n:                        import a CSV file with translations and exit
.. i18n:   --modules=TRANSLATE_MODULES
.. i18n:                        specify modules to export. Use in combination with
.. i18n:                        --i18n-export
..

    Use these options to translate OpenERP to another language. See i18n
    section of the user manual. Option '-l' is mandatory.
 
  -l LANGUAGE, --language=LANGUAGE
                       指定翻译文件。与 --i18n-export 或 --i18n-import一起使用。
  --i18n-export=TRANSLATE_OUT
                       导出翻译语言为CSV文件，然后结束
  --i18n-import=TRANSLATE_IN
                       导入CSV翻译文件，然后结束
  --modules=TRANSLATE_MODULES
                       指定要导出模块翻译。与 --i18n-export 一起使用

.. i18n: Options from previous versions:
.. i18n: -------------------------------
.. i18n: Some options were removed in version 6. For example, ``price_accuracy`` is now
.. i18n: configured through the :ref:`decimal_accuracy` screen.
..

其它兼容旧版源码参数:
-------------------------------
某些参数在OE6中被移除。如 ``price_accuracy`` 现在是通过  :ref:`decimal_accuracy`  配置。
