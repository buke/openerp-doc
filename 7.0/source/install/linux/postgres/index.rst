.. index::
   single: Installation; PostgreSQL
   single: PostgreSQL; Installation
..

.. _installation-postgresql-server:

PostgreSQL Server Installation and Configuration
================================================

.. tip:: Methods

        The `PostgreSQL download page <http://www.postgresql.org/download/linux>`__ lists the available installation methods. Choose the one that best suits your needs.

Example on Ubuntu
-----------------

Use the following command at your system's command prompt to install the **postgresql** package: ::

  sudo apt-get install postgresql

For example: ::

  openerp@openerp-desktop:/$ sudo apt-get install postgresql

For a graphical user interface of **postgresql**, use the following command: ::

  sudo apt-get install pgadmin3

For example: ::

  openerp@openerp-desktop:/$ sudo apt-get install pgadmin3

You can find the new menu item **pgAdmin III** in your Ubuntu system menu from
:menuselection:`Applications --> Programming --> pgAdmin III`.


.. index::
   single: PostgreSQL; setup a user
   single: PostgreSQL; setup a database
..

Setup a PostgreSQL user for OpenERP
-----------------------------------

When the installations of the required software are done, you must create a
PostgreSQL user. This user must be the same as your system user. OpenERP will use this user to
connect to PostgreSQL.

.. figure:: ../../img/openerp_postgresql.png
   :scale: 75
   :align: center

   *Figure demonstrating how OpenERP uses the PostgreSQL user to interact with it*

.. tip:: Database

        Without creating and configuring a PostgreSQL user for OpenERP as described below, you cannot create a database using OpenERP Client.

First Method
++++++++++++

The default superuser for PostgreSQL is called **postgres**. You may need to login as this
user first. ::

    openerp@openerp-desktop:/$ sudo su postgres
    password: XXXXXXXXXX

Now create PostgreSQL user **openerp** using the following command: ::

	postgres@openerp-desktop:/$ createuser openerp
	Shall the new role be a superuser? (y/n) y

Make this new user a superuser. Only then you can create a database using OpenERP Client.
In short, **openerp** is the new user created in PostgreSQL for OpenERP. This user is the owner
of all the tables created by OpenERP Client.

Now check the list of tables created in PostgreSQL using following command: ::

	postgres@openerp-desktop:/$ psql -l

You can find the table **template1**, run the following command to use this table: ::

	postgres@openerp-desktop:/$ psql template1

To apply access rights to the role **openerp** for the database which will be created from OpenERP Client,
use the following command: ::

	template1=# alter role openerp with password 'postgres';
	ALTER ROLE

Second Method
+++++++++++++

Another option to create and configure a PostgreSQL user for OpenERP is shown below: ::

    postgres@openerp-desktop:/$ createuser --createdb --username postgres --no-createrole
    --pwprompt openerp
    Enter password for new role: XXXXXXXXXX
    Enter it again: XXXXXXXXXX
    Shall the new role be a superuser? (y/n) y
    CREATE ROLE

.. note:: Password

        Note that the password is *postgres*.

Option explanations:

  * ``--createdb`` : the new user will be able to create new databases
  * ``--username postgres`` : *createuser* will use the *postgres* user (superuser)
  * ``--no-createrole`` : the new user will not be able to create new users
  * ``--pwprompt`` : *createuser* will ask you the new user's password
  * ``openerp`` : the new user's name


To access your database using **pgAdmin III**, you must configure the database connection as shown in the following figure:

.. figure:: ../../img/new_server_registration.png
   :scale: 50
   :align: center

You can now start OpenERP Server. You will probably need to modify the
OpenERP configuration file according to your needs which is normally
located in ``~/.openerprc``.

.. tip:: Developer Book

        You can find information on configuration files in the Developer Book, section :ref:`Configuration <configuration-files-link>`


