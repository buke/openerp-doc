How to proceed for your database migration?
===========================================

.. figure:: images/migration.png
   :scale: 70
   :align: center

   *Migration Process*

We describe below the 3 or 4 steps you must follow for your database migration. We suggest, as a best practice advice, to run this process at least twice (but you can do it as often as you want): the first time, after sending us your database, you will get it back migrated to the version of your choice. You will then have to do some tests, checking that the data and process are still correct and work normally. After your tests' validation, you are ready for effective migration. Send us an up-to-date version of your database. We will reapply the migration process and you will then get the migrated database to install and use in production.

We remind you, that you are in charge of your database cleaning, and that the migration warranty concerns all certified modules only. If you made some specific developments and want to keep them, be sure that they are grouped in a certified module. (For further information, have a look at our OpenERP Publisher's Warranty or contact our technical team at support@openerp.com or +32 81 81 37 00 if you want to certify your modules.)

Migration Process
-----------------

* **Step 1: You upload your database**

  Create a backup of your database and upload it. You can anonymize your data before uploading the database. For further information, see :ref:`sect-db` and :ref:`anonym`.


* **Step 2: We migrate and test your database**

  Once we receive your database, we run our migration process and test your database.

    * If the migration process ended without any problem, you will receive an email within a few hours, with a link where you can download your migrated database. You may then go directly to step 4.
    * If the migration process does not end automatically, you will receive an email within a few hours, explaining that the migration process encountered some difficulties and that a manual intervention is necessary. More details are available in step 3.

* **Step 3: We customize our migration process to your database**

  Our migration process is automated as much as possible, but some manual work may be necessary, depending on your data's complexity. It is possible, during step 2, that the migration process did not complete correctly and that we need to customize our scripts for your database. This operation may take 2-4 weeks, depending on the complexity of your database. After the migration script adaptation, you will receive an email with a link where you can download your migrated database.

* **Step 4: You reinstall the migrated database**

  You can download your migrated database and reinstall it on your new OpenERP version. If you executed the anonymisation process at step 1, you will have to reverse it to recover your real data.

.. _sect-db:

How to restore a database?
--------------------------

As a super-administrator, you have rights to create new databases, and can also:

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

.. _anonym:

How to keep your data confidential?
-----------------------------------

We offer an option to anonymise your data through our :mod:`anonymization` module.
This module allows you to keep your data confidential for a given database. This process is useful if you want to use the migration process and protect your own or your customers' confidential data. The principle is that you run an anonymization tool which will hide your confidential data (they are replaced by 'XXX' characters). Then you can send the anonymized database to the migration team. Once you get back your migrated database, you restore it and reverse the anonymisation process to recover your previous data.

We suggest you to work on a copy of your database, so be sure to make a backup before starting the anonymisation process.

The first step is to install and configure the :mod:`anonymization` module. The menus are located in :menuselection:`Administration --> Database anonymization`.

*Anonymization History* 
^^^^^^^^^^^^^^^^^^^^^^^

This is the history of all the anonymisation (and the reverse process) that occurred on a particular database. 

*Anonymize database*
^^^^^^^^^^^^^^^^^^^^ 

This is the wizard that will actually anonymise the database. This wizard is also responsible to reverse the anonymization process. 

*Anonymized Fields*
^^^^^^^^^^^^^^^^^^^

**Pre-defined fields**

On module installation, OpenERP will create some fields considered as important to anonymise, these are:
 
  * Partner: Name 

  * Partner: Reference 
  
  * Partner Addresses: Contact Name 

  * Partner Addresses: City 
	
  * Partner Addresses: Street 
	
  * Partner Addresses: Street2 

  * Partner Addresses: Zip 

  * Partner Addresses: Phone 

  * Partner Addresses: Fax 

  * Partner Addresses: Mobile 

  * Partner Addresses: E-Mail 

  * Invoice: Untaxed (amount_untaxed) 

  * Invoice: Tax 

  * Invoice: Total (amount_total) 

  * Invoice: Total (check_total) 

  * Invoice: Residual 

  * Invoice line: Unit Price 

  * Invoice line: Subtotal 

  * Invoice move line: Debit 

  * Invoice move line: Credit 

  * Invoice move line: Tax/Base Amount 

  * Invoice move line: Amount Currency 

  * Invoice move line: Taxed Amount 

  * Sale order: amount_tax 

  * Sale order: amount_untaxed 

  * Sale order: amount_total 

  * Sale order line: price unit 

  * Sale order line: discount 
 
  * Purchase order: amount_tax 

  * Purchase order: amount_untaxed 

  * Purchase order: amount_total 

  * Purchase order line: price_unit 

The anonymised values are: 

  * char field: xxx + record id 
  * text field: xxx + record id 
  * selection field: xxx + record id 
  * integer field: 1 
  * float field:  0.0 
  * date field: 2011-11-11 
  * datetime field: 2011-11-11 11:11:11 

All attachment object contents are replaced by an empty string in the database. 

**Create new fields to anonymize**

You also have the possibility to add other fields that you want to keep confidential. You have to create them manually.

First choose an object by using the popup (:guilabel:`Object` field). You can also enter the object model name directly into the :guilabel:`Object Name` field, if you know it. These two fields are linked to each other; fill out one of both and the other one will be filled automatically. 

You then choose the field by using the popup (:guilabel:`Field` field). You can also enter the field name directly if you know it (:guilabel:`Field Name` field). These two fields are linked to each other in the same way as described above. 

The :guilabel:`State` field values are: 

* :guilabel:`Clear`: the field values have their original status in the database 

* :guilabel:`Anonymized`: the field values are anonymised in the database 

* :guilabel:`Not Existing`: the field does not exist in the database.
  This is probably a field which comes from the module's data file. For example, the data file creates some predefined anonymized fields, but the module might not be installed. These fields are ignored by the anonymisation process. 


