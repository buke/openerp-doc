
.. i18n: .. index::
.. i18n:    single: Installation; PostgreSQL
.. i18n:    single: PostgreSQL; Installation
.. i18n: ..
..

.. index::
   single: Installation; PostgreSQL
   single: PostgreSQL; Installation
..

.. i18n: .. _installation-postgresql-server:
.. i18n: 
.. i18n: PostgreSQL Server Installation and Configuration
.. i18n: ================================================
..

.. _installation-postgresql-server:

PostgreSQL Server Installation and Configuration
================================================

.. i18n: .. tip:: Methods
.. i18n: 
.. i18n:         The `PostgreSQL download page <http://www.postgresql.org/download/linux>`__ lists the available installation methods. Choose the one that best suits your needs.
..

.. tip:: Methods

        The `PostgreSQL download page <http://www.postgresql.org/download/linux>`__ lists the available installation methods. Choose the one that best suits your needs.

.. i18n: Example on Ubuntu
.. i18n: -----------------
..

Example on Ubuntu
-----------------

.. i18n: Use the following command at your system's command prompt to install the **postgresql** package: ::
.. i18n: 
.. i18n:   sudo apt-get install postgresql
..

Use the following command at your system's command prompt to install the **postgresql** package: ::

  sudo apt-get install postgresql

.. i18n: For example: ::
.. i18n: 
.. i18n:   openerp@openerp-desktop:/$ sudo apt-get install postgresql
..

For example: ::

  openerp@openerp-desktop:/$ sudo apt-get install postgresql

.. i18n: For a graphical user interface of **postgresql**, use the following command: ::
.. i18n: 
.. i18n:   sudo apt-get install pgadmin3
..

For a graphical user interface of **postgresql**, use the following command: ::

  sudo apt-get install pgadmin3

.. i18n: For example: ::
.. i18n: 
.. i18n:   openerp@openerp-desktop:/$ sudo apt-get install pgadmin3
..

For example: ::

  openerp@openerp-desktop:/$ sudo apt-get install pgadmin3

.. i18n: You can find the new menu item **pgAdmin III** in your Ubuntu system menu from
.. i18n: :menuselection:`Applications --> Programming --> pgAdmin III`.
..

You can find the new menu item **pgAdmin III** in your Ubuntu system menu from
:menuselection:`Applications --> Programming --> pgAdmin III`.

.. i18n: .. index::
.. i18n:    single: PostgreSQL; setup a user
.. i18n:    single: PostgreSQL; setup a database
.. i18n: ..
..

.. index::
   single: PostgreSQL; setup a user
   single: PostgreSQL; setup a database
..

.. i18n: Setup a PostgreSQL user for OpenERP
.. i18n: -----------------------------------
..

Setup a PostgreSQL user for OpenERP
-----------------------------------

.. i18n: When the installations of the required software are done, you must create a
.. i18n: PostgreSQL user. This user must be the same as your system user. OpenERP will use this user to
.. i18n: connect to PostgreSQL.
..

When the installations of the required software are done, you must create a
PostgreSQL user. This user must be the same as your system user. OpenERP will use this user to
connect to PostgreSQL.

.. i18n: .. figure:: ../../img/openerp_postgresql.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Figure demonstrating how OpenERP uses the PostgreSQL user to interact with it*
..

.. figure:: ../../img/openerp_postgresql.png
   :scale: 75
   :align: center

   *Figure demonstrating how OpenERP uses the PostgreSQL user to interact with it*

.. i18n: .. tip:: Database
.. i18n: 
.. i18n:         Without creating and configuring a PostgreSQL user for OpenERP as described below, you cannot create a database using OpenERP Client.
..

.. tip:: Database

        Without creating and configuring a PostgreSQL user for OpenERP as described below, you cannot create a database using OpenERP Client.

.. i18n: First Method
.. i18n: ++++++++++++
..

First Method
++++++++++++

.. i18n: The default superuser for PostgreSQL is called **postgres**. You may need to login as this
.. i18n: user first. ::
.. i18n: 
.. i18n:     openerp@openerp-desktop:/$ sudo su postgres
.. i18n:     password: XXXXXXXXXX
..

The default superuser for PostgreSQL is called **postgres**. You may need to login as this
user first. ::

    openerp@openerp-desktop:/$ sudo su postgres
    password: XXXXXXXXXX

.. i18n: Now create PostgreSQL user **openerp** using the following command: ::
.. i18n: 
.. i18n: 	postgres@openerp-desktop:/$ createuser openerp
.. i18n: 	Shall the new role be a superuser? (y/n) y
..

Now create PostgreSQL user **openerp** using the following command: ::

	postgres@openerp-desktop:/$ createuser openerp
	Shall the new role be a superuser? (y/n) y

.. i18n: Make this new user a superuser. Only then you can create a database using OpenERP Client.
.. i18n: In short, **openerp** is the new user created in PostgreSQL for OpenERP. This user is the owner
.. i18n: of all the tables created by OpenERP Client.
..

Make this new user a superuser. Only then you can create a database using OpenERP Client.
In short, **openerp** is the new user created in PostgreSQL for OpenERP. This user is the owner
of all the tables created by OpenERP Client.

.. i18n: Now check the list of tables created in PostgreSQL using following command: ::
.. i18n: 
.. i18n: 	postgres@openerp-desktop:/$ psql -l
..

Now check the list of tables created in PostgreSQL using following command: ::

	postgres@openerp-desktop:/$ psql -l

.. i18n: You can find the table **template1**, run the following command to use this table: ::
.. i18n: 
.. i18n: 	postgres@openerp-desktop:/$ psql template1
..

You can find the table **template1**, run the following command to use this table: ::

	postgres@openerp-desktop:/$ psql template1

.. i18n: To apply access rights to the role **openerp** for the database which will be created from OpenERP Client,
.. i18n: use the following command: ::
.. i18n: 
.. i18n: 	template1=# alter role openerp with password 'postgres';
.. i18n: 	ALTER ROLE
..

To apply access rights to the role **openerp** for the database which will be created from OpenERP Client,
use the following command: ::

	template1=# alter role openerp with password 'postgres';
	ALTER ROLE

.. i18n: Second Method
.. i18n: +++++++++++++
..

Second Method
+++++++++++++

.. i18n: Another option to create and configure a PostgreSQL user for OpenERP is shown below: ::
.. i18n: 
.. i18n:     postgres@openerp-desktop:/$ createuser --createdb --username postgres --no-createrole
.. i18n:     --pwprompt openerp
.. i18n:     Enter password for new role: XXXXXXXXXX
.. i18n:     Enter it again: XXXXXXXXXX
.. i18n:     Shall the new role be a superuser? (y/n) y
.. i18n:     CREATE ROLE
..

Another option to create and configure a PostgreSQL user for OpenERP is shown below: ::

    postgres@openerp-desktop:/$ createuser --createdb --username postgres --no-createrole
    --pwprompt openerp
    Enter password for new role: XXXXXXXXXX
    Enter it again: XXXXXXXXXX
    Shall the new role be a superuser? (y/n) y
    CREATE ROLE

.. i18n: .. note:: Password
.. i18n: 
.. i18n:         Note that the password is *postgres*.
..

.. note:: Password

        Note that the password is *postgres*.

.. i18n: Option explanations:
..

Option explanations:

.. i18n:   * ``--createdb`` : the new user will be able to create new databases
.. i18n:   * ``--username postgres`` : *createuser* will use the *postgres* user (superuser)
.. i18n:   * ``--no-createrole`` : the new user will not be able to create new users
.. i18n:   * ``--pwprompt`` : *createuser* will ask you the new user's password
.. i18n:   * ``openerp`` : the new user's name
..

  * ``--createdb`` : the new user will be able to create new databases
  * ``--username postgres`` : *createuser* will use the *postgres* user (superuser)
  * ``--no-createrole`` : the new user will not be able to create new users
  * ``--pwprompt`` : *createuser* will ask you the new user's password
  * ``openerp`` : the new user's name

.. i18n: To access your database using **pgAdmin III**, you must configure the database connection as shown in the following figure:
..

To access your database using **pgAdmin III**, you must configure the database connection as shown in the following figure:

.. i18n: .. figure:: ../../img/new_server_registration.png
.. i18n:    :scale: 50
.. i18n:    :align: center
..

.. figure:: ../../img/new_server_registration.png
   :scale: 50
   :align: center

.. i18n: You can now start OpenERP Server. You will probably need to modify the
.. i18n: OpenERP configuration file according to your needs which is normally
.. i18n: located in ``~/.openerprc``.
..

You can now start OpenERP Server. You will probably need to modify the
OpenERP configuration file according to your needs which is normally
located in ``~/.openerprc``.

.. i18n: .. tip:: Developer Book
.. i18n: 
.. i18n:         You can find information on configuration files in the Developer Book, section :ref:`Configuration <configuration-files-link>`
..

.. tip:: Developer Book

        You can find information on configuration files in the Developer Book, section :ref:`Configuration <configuration-files-link>`
