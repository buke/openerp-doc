
.. index::
   single: database; create
   single: database

.. _sect-dbcreate:

Database Creation
=================

Use the technique outlined in this section to create a new database, \ ``openerp_ch01`` \. This
database will contain the demonstration data provided with OpenERP and a large proportion of the
core OpenERP functionality. You will need to know your super administrator password for this – or
you will have to find somebody who does have it to create this database.

.. index::
   single: password; super-administrator
   single: password; superadmin

.. note:: The Super-administrator Password

   Anyone who knows the super-administrator password has complete access to the data on the server
   – able to read, change and delete any of the data in any of the databases there.

   After first installation, the password is ``admin``. This is the hard-coded default, and
   is used if there is no accessible server configuration file. If your system has been 
   set up so that the server configuration file can be written to by the server, then
   you can change the password through the client. Or you could deliberately make the 
   configuration file read-only so that there is no prospect of changing it from the client.
   Either way, a server systems administrator can change it if you forget it.
   
   So if your system is set to allow it, you can change the superadmin password through the GTK client
   from the menu :menuselection:`File --> Databases --> Administrator Password`, or through the
   web client by logging out (click the :guilabel:`Logout` link), clicking :guilabel:`Databases` on the
   login screen, and then clicking the :guilabel:`Password` button on the Management screen. 
   
   The location of the server configuration file is typically defined by starting the server with 
   the ``--config`` command line option.

.. figure:: images/change_superadmin_pwd.png
   :scale: 65
   :align: center

   *Changing the super-administrator password through the web client*

.. _sect-creatingdb:

Creating the Database
---------------------

If you are using the GTK client, choose :menuselection:`File --> Databases --> New database`  in
the menu at the top left. Enter the super-administrator password, then the name of the new database
you are creating.

.. figure:: images/create_new_db_GTK.png
   :scale: 75
   :align: center

   *Creating a new database through the GTK client*  

If you are using the web client, click :guilabel:`Databases` on the login screen, then
:guilabel:`Create` on the database management page. Enter the super-administrator password, and the
name of the new database you are creating.
  
In both cases, you will see a checkbox that determines whether you load demonstration data or not.
The consequences of checking this box or not affect the **whole use** of this database.

In both cases, you will also see that you can choose the Administrator password. This makes your 
database quite secure because you can ensure that it is unique from the outset.
(In fact many people find it hard to resist ``admin`` as their password!)

Database openerp_ch01
---------------------

.. index::
   pair: account; user

Wait for the message showing that the database has been successfully created, along with the user
accounts and passwords (\ ``admin/XXXX``\   and \ ``demo/demo``\  ). Now that you have created this
database, you can extend it without having to know the super-administrator password.

.. index::
   single: access; LDAP
   single: LDAP
   pair: password; username
   single: access; user

.. tip::   User Access

	The combination of username/password is specific to a single database. If you have administrative
	rights to a database you can modify all users.

 	.. index::
	   single: module; users_ldap

	Alternatively, you can install the :mod:`users_ldap` module, which manages the authentication of users
	in LDAP (the Lightweight Directory Access Protocol, a standard system), and connect it to several
	OpenERP databases. Using this, many databases can share the same user account details.

.. note::  Failure to Create a Database

	How do you know if you have successfully created your new database?
	You are told if the database creation has been unsuccessful.
	If you have entered a database name using prohibited characters (or no name, or too short a name),
	you will be alerted by the dialog box :guilabel:`Bad database name!` explaining how to correct the error.
	If you have entered the wrong super-administrator password or a name already in use
	(some names can be reserved without your knowledge), you will be alerted by the dialog box
	:guilabel:`Error during database creation!`.

Since this is the first time you have connected to this database, you will be asked a series of questions to
define the database parameters. You may choose to :guilabel:`Skip Configuration Wizards` or
:guilabel:`Start Configuration`. If you choose to configure your application, you may proceed with the
following steps:

	#.  :guilabel:`Configure Your Interface` : select \ ``Simplified`` \ and click :guilabel:`Next`.

	#.  :guilabel:`Configure Your Company Information` : replace the proposed default of \ ``OpenERP S.A.`` \
	    by your own company name, complete as much of your address as you like. You can set the currency that
	    your company uses or leave the default setting. You may also add your company logo which will
	    be visible on reports and other documents. Click :guilabel:`Next`.

	#.  :guilabel:`Install Applications` : check the applications you need and then click :guilabel:`Install`.
	    For now, do not install any application.

Once configuration is complete, you are connected to your OpenERP system. Its functionality is very
limited because you have selected a :guilabel:`Simplified` interface with no application installed,
but this is sufficient to demonstrate that your installation is working.

.. figure:: images/define_main_co_dlg.png
   :align: center
   :scale: 80

   *Defining your company during initial database configuration*

.. index::
   single: database; manage

.. _sect-dbmanage:

Managing Databases
------------------

As a super-administrator, you do not only have rights to create new databases, but also to:

* backup databases,

* delete databases,

* restore databases.

All of these operations can be carried out from the menu :menuselection:`File --> Databases...`
in the GTK client, or from the :guilabel:`Databases` button in the web client's 
:guilabel:`Login` screen.

.. index::
   single: database; backup

.. tip:: Backup (copy) a Database

        To make a copy of a database, go to the web :guilabel:`Login` screen and click the :guilabel:`Databases` button.
        Then click the :guilabel:`Backup` button, select the database you want to copy and enter the super-administrator
	password. Click the :guilabel:`Backup` button to confirm that you want to copy the database.

.. index::
   single: database; drop

.. tip:: Drop (delete) a Database

        To delete a database, go to the web :guilabel:`Login` screen and click the :guilabel:`Databases` button.
        Then click the :guilabel:`Drop` button, select the database you want to delete and enter the super-administrator
	password. Click the :guilabel:`Drop` button to confirm that you want to delete the database.

.. index::
   single: database; restore

.. tip:: Restore a Database

        To restore a database, go to the web :guilabel:`Login` screen and click the :guilabel:`Databases` button.
        Then click the :guilabel:`Restore` button, click the :guilabel:`Choose File` button to select the database
        you want to restore. Give the database a name and enter the super-administrator	password.
	Click the :guilabel:`Restore` button to confirm that you want to install a new copy of the selected database.
	To restore a database, you need to have an existing copy, of course.

.. index::
   single: database; duplicate

.. tip::   Duplicating a Database

	To duplicate a database, you can:

        #. make a backup file on your PC from this database.

        #. restore this database from the backup file on your PC, and give it a new name.

	This can be a useful way of making a test database from a production database. You can try out the
	operation of a new configuration, new modules, or just the import of new data.

.. index::
   single: access

A system administrator can configure OpenERP to restrict access to some of these database functions
so that your security is enhanced in normal production use.

You are now ready to use databases from your installation to familiarize yourself with the
administration and use of OpenERP.

New OpenERP Functionality
=========================

The database you have created and managed so far is based on the core OpenERP functionality that you
installed. The core system is installed in the file system of your OpenERP application server, but
only installed into an OpenERP database as you require it, as is described in the next chapter, :ref:`ch-guided`.

What if you want to update what is there, or extend what is there with additional modules?

* To update what you have, you would install a new instance of OpenERP using the same techniques as
  described earlier in this section, :ref:`sect-dbcreate`.

* To extend what you have, you would install new modules in the ``addons`` directory of your current
  OpenERP installation. There are several ways of doing that.

.. index::
   pair:  system; administrator

In both cases you will need to be a \ ``root`` \ user or \ ``Administrator`` \ of your
OpenERP application server.

Extending OpenERP
-----------------

To extend OpenERP you will need to copy modules into the \ ``addons`` \ directory. That is in
your server's \ ``openerp-server`` \ directory (which differs between Windows, Mac and some of the
various Linux distributions and not available at all in the Windows all-in-one installer).

.. index::
   single: module; product
   single: module; purchase

If you look there you will see existing modules such as :mod:`product` and :mod:`purchase`. A
module can be provided in the form of files within a directory or a a zip-format file containing
that same directory structure.

You can add modules in two main ways – through the server, or through the client.

.. index::
   pair:  system; administration

To add new modules through the server is a conventional system administration task. As \ ``root`` \
user or another suitable user, you would put the module in the \ ``addons`` \ directory and change its
permissions to match those of the other modules.

To add new modules through the client you must first change the permissions of the \ ``addons`` \
directory of the server, so that it is writeable by the server. That will enable you to install
OpenERP modules using the OpenERP client (a task ultimately carried out on the application
server by the server software).

.. index::
   pair:  filesystem; permissions

.. tip:: Changing Permissions

	A very simple way of changing permissions on the Linux system you are using to develop an OpenERP
	application is to execute the command sudo chmod 777 <path_to_addons> (where <path_to_addons> is
	the full path to the addons directory, a location like /usr/lib/python2.5/site-packages/openerp-
	server/addons).

Any user of OpenERP who has access to the relevant administration menus can then upload any new
functionality, so you would certainly disable this capability for production use. You will see examples of
this uploading as you make your way through this book.


.. Copyright © Open Object Press. All rights reserved.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the OpenERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. Published by Open Object Press, Grand Rosière, Belgium

