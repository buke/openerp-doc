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

In this chapter, you will see how to configure PostgreSQL for its use with OpenERP. The following procedure is well-tested on PostgreSQL v9.0.

.. i18n: Installing PostgreSQL Server
.. i18n: ----------------------------
..

PostgreSQL 数据库安装
----------------------------

.. i18n: You can download the Windows installer from
.. i18n: the `PostgreSQL download page <http://www.postgresql.org/download/windows>`__
..

You can download the Windows installer from
the `PostgreSQL download page <http://www.postgresql.org/download/windows>`__

.. i18n: Depending on your need, choose either the *One Click Installer* or the
.. i18n: *pgInstaller* and run the executable you have just downloaded.
..

Depending on your need, choose either the *One Click Installer* or the
*pgInstaller* and run the executable you have just downloaded.

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

When the required software installations are complete, you must create a
PostgreSQL user. OpenERP will use this user to connect to PostgreSQL.

.. i18n: Add a User
.. i18n: ++++++++++
..

新增用户
++++++++++

.. i18n: Start a Windows console (run the ``cmd`` command in the *Search programs and files* text box of the *Start* menu).
..

Start a Windows console (run the ``cmd`` command in the *Search programs and files* text box of the *Start* menu).

.. i18n: Change the directory to the *PostgreSQL* ``bin`` directory
.. i18n: (e.g. ``C:\Program Files\PostgreSQL\9.0\bin``) or add this directory to 
.. i18n: your *PATH* environment variable.
..

Change the directory to the *PostgreSQL* ``bin`` directory
(e.g. ``C:\Program Files\PostgreSQL\9.0\bin``) or add this directory to 
your *PATH* environment variable.

.. i18n: The default superuser for PostgreSQL is called *postgres*. The password was
.. i18n: chosen during the PostgreSQL installation.
..

The default superuser for PostgreSQL is called *postgres*. The password was
chosen during the PostgreSQL installation.

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

In your Windows console, type::

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

Option explanations:

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

.. note:: Password

   In OpenERP v6, ``openpg`` and ``openpgpwd`` are the default username and password used during the OpenERP Server installation. If you plan to change these defaults for the server, or have already installed the server with different values, you have to use those user configuration values when you create a PostgreSQL user for OpenERP.
  
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
