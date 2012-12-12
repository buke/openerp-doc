
.. index::
   single: Installation; PostgreSQL (Windows)
   single: PostgreSQL; Installation (Windows)
.. 

.. _installation-windows-postgresql-server:

PostgreSQL Server Installation and Configuration
================================================

In this chapter, you will see how to configure PostgreSQL for its use with OpenERP. The following procedure is well-tested on PostgreSQL v9.0.

*Installing PostgreSQL Server*

You can download the Windows installer from
the `PostgreSQL download page <http://www.postgresql.org/download/windows>`__

Depending on your need, choose either the *One Click Installer* or the
*pgInstaller* and run the executable you have just downloaded.

.. index::
   single: PostgreSQL; setup a user (Windows)
   single: PostgreSQL; setup a database (Windows)
.. 

*Set up a PostgreSQL User*

When the installations of the required software are done, you have to create a
PostgreSQL user. OpenERP will use this user to connect to PostgreSQL.

*Add a User*

Start a Windows console (run the ``cmd`` command in the *Search programs and files* text box of the *Start* menu).

Change the directory to the *PostgreSQL* ``bin`` directory
(e.g. ``C:\Program Files\PostgreSQL\9.0\bin``) or add this directory to 
your *PATH* environment variable.

The default superuser for PostgreSQL is called *postgres*. His password was
chosen during the PostgreSQL installation.

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

Option explanations:

  * ``--createdb`` : the new user will be able to create new databases
  * ``--username postgres`` : *createuser* will use the *postgres* user (superuser)
  * ``--no-createrole`` : the new user will not be able to create new users
  * ``--pwprompt`` : *createuser* will ask you the new user's password
  * ``openpg`` : the new user's name. Alternatively, you may specify a different username.
  * ``openpgpwd`` : the new user's password. Alternatively, you may specify a different password.

.. note:: Password

   In OpenERP v6, ``openpg`` and ``openpgpwd`` are the default username and password used during the OpenERP Server installation. If you plan to change these defaults for the server, or have already installed the server with different values, you have to use those user configuration values when you create a PostgreSQL user for OpenERP.
  
Now use *pgAdmin III* to create database "openerpdemo" with owner "openpg":: 
 
 CREATE DATABASE openerpdemo WITH OWNER = openpg ENCODING = 'UTF8';
 COMMENT ON DATABASE openerpdemo IS 'OpenERP Demo DB';
  
If you have installed the OpenERP Server, you can start it now. If needed, you can override the server configuration by starting the server at a Windows console and specifying command-line options. For more on this, refer the section :ref:`sect-custconf`.

To change a user's password in any Windows version, execute the following::

  net user <accountname> <newpassword>
  e.g. net user postgres postgres

If it is a domain account, just add "/DOMAIN" at the end.

If you want to delete it, just execute::

  net user <accountname> /delete

*Case-Insensitive Search Issue*

For an installation which needs full UTF8 character support, consider using
postgres >= 8.2.x. Using versions prior to this, OpenERP search will eventually not return the
expected results for case-insensitive searches, which are used for searching
partners, products etc.

Example: ::

    SELECT 'x' FROM my_table WHERE 'bét' ilike 'BÉT'
    --matches only in 8.2.x

