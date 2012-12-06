.. i18n: .. index::
.. i18n:    single: Installation; PostgreSQL (Windows)
.. i18n:    single: PostgreSQL; Installation (Windows)
.. i18n: .. 
..

.. index::
   single: Installation; PostgreSQL (Windows)
   single: PostgreSQL; Installation (Windows)
.. 

.. i18n: .. _installation-windows-postgresql-server:
.. i18n: 
.. i18n: PostgreSQL Server Installation and Configuration
.. i18n: ================================================
..

.. _installation-windows-postgresql-server:

PostgreSQL 数据库安装与配置
================================================

.. i18n: In this chapter, you will see how to configure PostgreSQL for its use with OpenERP. The following procedure is well-tested on PostgreSQL v9.0.
..

在本章节，你将看到如何配置PostgrSQL用于OpenERP。以下流程在PostgrSQLv9.0上很好地测试过。

.. i18n: Installing PostgreSQL Server
.. i18n: ----------------------------
..

PostgreSQL 数据库安装
----------------------------

.. i18n: You can download the Windows installer from
.. i18n: the `PostgreSQL download page <http://www.postgresql.org/download/windows>`__
..

你可以从这里下载Windows 安装包 `PostgreSQL download page <http://www.postgresql.org/download/windows>`__

.. i18n: Depending on your need, choose either the *One Click Installer* or the
.. i18n: *pgInstaller* and run the executable you have just downloaded.
..

依照你的需要，选择One Click安装包，或选择pgInstaller，然后运行你刚下载的可执行文件。

.. i18n: .. index::
.. i18n:    single: PostgreSQL; setup a user (Windows)
.. i18n:    single: PostgreSQL; setup a database (Windows)
.. i18n: .. 
..

.. index::
   single: PostgreSQL; setup a user (Windows)
   single: PostgreSQL; setup a database (Windows)
.. 

.. i18n: Setup a PostgreSQL User
.. i18n: -----------------------
..

配置PostgreSQL角色用户
-----------------------

.. i18n: When the required software installations are complete, you must create a
.. i18n: PostgreSQL user. OpenERP will use this user to connect to PostgreSQL.
..

当所需的软件安装完成，你必须设置一个PostgrSQL用户。OpenERP将使用这个用户连接到PostgreSQL。

.. i18n: Add a User
.. i18n: ++++++++++
..

新增用户
++++++++++

.. i18n: Start a Windows console (run the ``cmd`` command in the *Search programs and files* text box of the *Start* menu).
..

启动Windows控制台（在开始菜单的搜索程序和文件文本框运行 ''cmd'' 命令）。

.. i18n: Change the directory to the *PostgreSQL* ``bin`` directory
.. i18n: (e.g. ``C:\Program Files\PostgreSQL\9.0\bin``) or add this directory to 
.. i18n: your *PATH* environment variable.
..

变更目录到 *PostgreSQL* ``bin`` 目录
(例如 ``C:\Program Files\PostgreSQL\9.0\bin``) 或者将这个目录添加到你的 *PATH* 环境变量。

.. i18n: The default superuser for PostgreSQL is called *postgres*. The password was
.. i18n: chosen during the PostgreSQL installation.
..

PostgreSQL的默认超级用户叫 *postgres*。密码是你在安装过程中设置的。

.. i18n: In your Windows console, type::
.. i18n: 
.. i18n:     C:\Program Files\PostgreSQL\9.0\bin>createuser.exe --createdb --username postgres --no-createrole --pwprompt openpg
.. i18n:     Enter password for new role: openpgpwd
.. i18n:     Enter it again: openpgpwd
.. i18n:     Shall the new role be a superuser? (y/n) y
.. i18n:     Password: XXXXXXXXXX
.. i18n: 
.. i18n:   * line 1 is the command itself
.. i18n:   * line 2 asks you the new user's password
.. i18n:   * line 3 asks you to confirm the new user's password
.. i18n:   * line 4 new role is superuser or not?
.. i18n:   * line 5 asks you the *postgres* user's password
..

在你的 Windows 控制台，输入::

    C:\Program Files\PostgreSQL\9.0\bin>createuser.exe --createdb --username postgres --no-createrole --pwprompt openpg
    Enter password for new role: openpgpwd
    Enter it again: openpgpwd
    Shall the new role be a superuser? (y/n) y
    Password: XXXXXXXXXX

  * line 1 is the command itself
  * line 2 asks you the new user's password
  * line 3 asks you to confirm the new user's password
  * line 4 new role is superuser or not?
  * line 5 asks you the *postgres* user's password

.. i18n: Option explanations:
..

选项解释:

.. i18n:   * ``--createdb`` : the new user will be able to create new databases
.. i18n:   * ``--username postgres`` : *createuser* will use the *postgres* user (superuser)
.. i18n:   * ``--no-createrole`` : the new user will not be able to create new users
.. i18n:   * ``--pwprompt`` : *createuser* will ask you the new user's password
.. i18n:   * ``openpg`` : the new user's name. Alternatively, you may specify a different username.
.. i18n:   * ``openpgpwd`` : the new user's password. Alternatively, you may specify a different password.
..

  * ``--createdb`` : the new user will be able to create new databases
  * ``--username postgres`` : *createuser* will use the *postgres* user (superuser)
  * ``--no-createrole`` : the new user will not be able to create new users
  * ``--pwprompt`` : *createuser* will ask you the new user's password
  * ``openpg`` : the new user's name. Alternatively, you may specify a different username.
  * ``openpgpwd`` : the new user's password. Alternatively, you may specify a different password.

.. i18n: .. note:: Password
.. i18n: 
.. i18n:    In OpenERP v6, ``openpg`` and ``openpgpwd`` are the default username and password used during the OpenERP Server installation. If you plan to change these defaults for the server, or have already installed the server with different values, you have to use those user configuration values when you create a PostgreSQL user for OpenERP.
.. i18n:   
.. i18n: Now use *pgAdmin III* to create database "openerpdemo" with owner "openpg":: 
.. i18n:  
.. i18n:  CREATE DATABASE openerpdemo WITH OWNER = openpg ENCODING = 'UTF8';
.. i18n:  COMMENT ON DATABASE openerpdemo IS 'OpenERP Demo DB';
.. i18n:   
.. i18n: If you have installed the OpenERP Server, you can start it now. If needed, you can override the server configuration by starting the server at a Windows console and specifying command-line options. For more on this, refer the section :ref:`sect-custconf`.
..

.. note:: 密码

   在OpenERPv6，openpg和openpwd是OpenERP服务器安装过程使用的默认用户名和密码。如果你计划变更这些默认设置，或者已经用不同的值安装了服务器，你需要用那些用户配置值创建用于OpenERP的PostgreSQL用户。
  
Now use *pgAdmin III* to create database "openerpdemo" with owner "openpg":: 
 
 CREATE DATABASE openerpdemo WITH OWNER = openpg ENCODING = 'UTF8';
 COMMENT ON DATABASE openerpdemo IS 'OpenERP Demo DB';
  
If you have installed the OpenERP Server, you can start it now. If needed, you can override the server configuration by starting the server at a Windows console and specifying command-line options. For more on this, refer the section :ref:`sect-custconf`.

.. i18n: To change a user's password in any Windows version, execute the following::
.. i18n: 
.. i18n:   net user <accountname> <newpassword>
.. i18n:   e.g. net user postgres postgres
..

To change a user's password in any Windows version, execute the following::

  net user <accountname> <newpassword>
  e.g. net user postgres postgres

.. i18n: If it is a domain account, just add "/DOMAIN" at the end.
..

If it is a domain account, just add "/DOMAIN" at the end.

.. i18n: If you want to delete it, just execute::
.. i18n: 
.. i18n:   net user <accountname> /delete
..

If you want to delete it, just execute::

  net user <accountname> /delete

.. i18n: Case-Insensitive Search Issue
.. i18n: +++++++++++++++++++++++++++++
..

Case-Insensitive Search Issue
+++++++++++++++++++++++++++++

.. i18n: For an installation which needs full UTF8 character support, consider using
.. i18n: postgres >= 8.2.x. Using versions prior to this, OpenERP search will not return the
.. i18n: expected results for case-insensitive searches, which are used for searching
.. i18n: partners, products etc.
..

For an installation which needs full UTF8 character support, consider using
postgres >= 8.2.x. Using versions prior to this, OpenERP search will not return the
expected results for case-insensitive searches, which are used for searching
partners, products etc.

.. i18n: Example: ::
.. i18n: 
.. i18n:     SELECT 'x' FROM my_table WHERE 'bét' ilike 'BÉT'
.. i18n:     --matches only in 8.2.x
..

Example: ::

    SELECT 'x' FROM my_table WHERE 'bét' ilike 'BÉT'
    --matches only in 8.2.x
