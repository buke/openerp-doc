.. i18n: How to proceed for your database migration?
.. i18n: ===========================================
..

如何进行数据库迁移?
===========================================

.. i18n: .. figure:: images/migration.png
.. i18n:    :scale: 70
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Migration Process*
..

.. figure:: images/migration.png
   :scale: 70
   :align: center

   *迁移步骤*

.. i18n: We describe below the 3 or 4 steps you must follow for your database migration. We suggest, as a best practice advice, to run this process at least twice (but you can do it as often as you want): the first time, after sending us your database, you will get it back migrated to the version of your choice. You will then have to do some tests, checking that the data and process are still correct and work normally. After your tests' validation, you are ready for effective migration. Send us an up-to-date version of your database. We will reapply the migration process and you will then get the migrated database to install and use in production.
..

We describe below the 3 or 4 steps you must follow for your database migration. We suggest, as a best practice advice, to run this process at least twice (but you can do it as often as you want): the first time, after sending us your database, you will get it back migrated to the version of your choice. You will then have to do some tests, checking that the data and process are still correct and work normally. After your tests' validation, you are ready for effective migration. Send us an up-to-date version of your database. We will reapply the migration process and you will then get the migrated database to install and use in production.

.. i18n: We remind you, that you are in charge of your database cleaning, and that the migration warranty concerns all certified modules only. If you made some specific developments and want to keep them, be sure that they are grouped in a certified module. (For further information, have a look at our OpenERP Publisher's Warranty or contact our technical team at support@openerp.com or +32 81 81 37 00 if you want to certify your modules.)
..

We remind you, that you are in charge of your database cleaning, and that the migration warranty concerns all certified modules only. If you made some specific developments and want to keep them, be sure that they are grouped in a certified module. (For further information, have a look at our OpenERP Publisher's Warranty or contact our technical team at support@openerp.com or +32 81 81 37 00 if you want to certify your modules.)

.. i18n: Migration Process
.. i18n: -----------------
..

迁移步骤
-----------------

.. i18n: * **Step 1: You upload your database**
..

* **第1步: 上传你的数据库**

.. i18n:   Create a backup of your database and upload it. You can anonymize your data before uploading the database. For further information, see :ref:`sect-db` and :ref:`anonym`.
..

  Create a backup of your database and upload it. You can anonymize your data before uploading the database. For further information, see :ref:`sect-db` and :ref:`anonym`.

.. i18n: * **Step 2: We migrate and test your database**
..

* **第2步: 我们迁移数据库操作，并做严格测试**

.. i18n:   Once we receive your database, we run our migration process and test your database.
..

  Once we receive your database, we run our migration process and test your database.

.. i18n:     * If the migration process ended without any problem, you will receive an email within a few hours, with a link where you can download your migrated database. You may then go directly to step 4.
.. i18n:     * If the migration process does not end automatically, you will receive an email within a few hours, explaining that the migration process encountered some difficulties and that a manual intervention is necessary. More details are available in step 3.
.. i18n: 
.. i18n: * **Step 3: We customize our migration process to your database**
..

    * If the migration process ended without any problem, you will receive an email within a few hours, with a link where you can download your migrated database. You may then go directly to step 4.
    * If the migration process does not end automatically, you will receive an email within a few hours, explaining that the migration process encountered some difficulties and that a manual intervention is necessary. More details are available in step 3.

* **第3步: 我们特别针对你的数据库定制迁移处理**

.. i18n:   Our migration process is automated as much as possible, but some manual work may be necessary, depending on your data's complexity. It is possible, during step 2, that the migration process did not complete correctly and that we need to customize our scripts for your database. This operation may take 2-4 weeks, depending on the complexity of your database. After the migration script adaptation, you will receive an email with a link where you can download your migrated database.
..

  Our migration process is automated as much as possible, but some manual work may be necessary, depending on your data's complexity. It is possible, during step 2, that the migration process did not complete correctly and that we need to customize our scripts for your database. This operation may take 2-4 weeks, depending on the complexity of your database. After the migration script adaptation, you will receive an email with a link where you can download your migrated database.

.. i18n: * **Step 4: You reinstall the migrated database**
..

* **第4步: 你重新部署迁移过的数据库**

.. i18n:   You can download your migrated database and reinstall it on your new OpenERP version. If you executed the anonymisation process at step 1, you will have to reverse it to recover your real data.
..

  You can download your migrated database and reinstall it on your new OpenERP version. If you executed the anonymisation process at step 1, you will have to reverse it to recover your real data.

.. i18n: .. _sect-db:
.. i18n: 
.. i18n: How to restore a database?
.. i18n: --------------------------
..

.. _sect-db:

如何恢复数据库备份?
--------------------------

.. i18n: As a super-administrator, you have rights to create new databases, and can also:
..

做为超级管理员的角色，你能够创建一个帐套，当然也能做下面的操作:

.. i18n: * backup databases,
.. i18n: 
.. i18n: * delete databases,
.. i18n: 
.. i18n: * restore databases.
..

* 备份数据库(帐套),

* 删除数据库(帐套),

* 恢复数据库(帐套).

.. i18n: All of these operations can be carried out from the menu :menuselection:`File --> Databases...`
.. i18n: in the GTK client, or from the :guilabel:`Databases` button in the web client's 
.. i18n: :guilabel:`Login` screen.
..

All of these operations can be carried out from the menu :menuselection:`File --> Databases...`
in the GTK client, or from the :guilabel:`Databases` button in the web client's 
:guilabel:`Login` screen.

.. i18n: .. index::
.. i18n:    single: database; backup
..

.. index::
   single: database; backup

.. i18n: .. tip:: Backup (copy) a Database
.. i18n: 
.. i18n:         To make a copy of a database, go to the web :guilabel:`Login` screen and click the :guilabel:`Databases` button.
.. i18n:         Then click the :guilabel:`Backup` button, select the database you want to copy and enter the super-administrator
.. i18n: 	password. Click the :guilabel:`Backup` button to confirm that you want to copy the database.
..

.. tip:: 备份(复制)数据库(帐套)

        To make a copy of a database, go to the web :guilabel:`Login` screen and click the :guilabel:`Databases` button.
        Then click the :guilabel:`Backup` button, select the database you want to copy and enter the super-administrator
	password. Click the :guilabel:`Backup` button to confirm that you want to copy the database.

.. i18n: .. index::
.. i18n:    single: database; drop
..

.. index::
   single: database; drop

.. i18n: .. tip:: Drop (delete) a Database
.. i18n: 
.. i18n:         To delete a database, go to the web :guilabel:`Login` screen and click the :guilabel:`Databases` button.
.. i18n:         Then click the :guilabel:`Drop` button, select the database you want to delete and enter the super-administrator
.. i18n: 	password. Click the :guilabel:`Drop` button to confirm that you want to delete the database.
..

.. tip:: 删除数据库(帐套)

        To delete a database, go to the web :guilabel:`Login` screen and click the :guilabel:`Databases` button.
        Then click the :guilabel:`Drop` button, select the database you want to delete and enter the super-administrator
	password. Click the :guilabel:`Drop` button to confirm that you want to delete the database.

.. i18n: .. index::
.. i18n:    single: database; restore
..

.. index::
   single: database; restore

.. i18n: .. tip:: Restore a Database
.. i18n: 
.. i18n:         To restore a database, go to the web :guilabel:`Login` screen and click the :guilabel:`Databases` button.
.. i18n:         Then click the :guilabel:`Restore` button, click the :guilabel:`Choose File` button to select the database
.. i18n:         you want to restore. Give the database a name and enter the super-administrator	password.
.. i18n: 	Click the :guilabel:`Restore` button to confirm that you want to install a new copy of the selected database.
.. i18n: 	To restore a database, you need to have an existing copy, of course.
..

.. tip:: 恢复数据库(帐套)

        To restore a database, go to the web :guilabel:`Login` screen and click the :guilabel:`Databases` button.
        Then click the :guilabel:`Restore` button, click the :guilabel:`Choose File` button to select the database
        you want to restore. Give the database a name and enter the super-administrator	password.
	Click the :guilabel:`Restore` button to confirm that you want to install a new copy of the selected database.
	To restore a database, you need to have an existing copy, of course.

.. i18n: .. index::
.. i18n:    single: database; duplicate
..

.. index::
   single: database; duplicate

.. i18n: .. tip::   Duplicating a Database
.. i18n: 
.. i18n: 	To duplicate a database, you can:
.. i18n: 
.. i18n:         #. make a backup file on your PC from this database.
.. i18n: 
.. i18n:         #. restore this database from the backup file on your PC, and give it a new name.
.. i18n: 
.. i18n: 	This can be a useful way of making a test database from a production database. You can try out the
.. i18n: 	operation of a new configuration, new modules, or just the import of new data.
..

.. tip::   复制数据库(帐套)

	To duplicate a database, you can:

        #. make a backup file on your PC from this database.

        #. restore this database from the backup file on your PC, and give it a new name.

	This can be a useful way of making a test database from a production database. You can try out the
	operation of a new configuration, new modules, or just the import of new data.

.. i18n: .. index::
.. i18n:    single: access
..

.. index::
   single: access

.. i18n: A system administrator can configure OpenERP to restrict access to some of these database functions
.. i18n: so that your security is enhanced in normal production use.
..

A system administrator can configure OpenERP to restrict access to some of these database functions
so that your security is enhanced in normal production use.

.. i18n: .. _anonym:
.. i18n: 
.. i18n: How to keep your data confidential?
.. i18n: -----------------------------------
..

.. _anonym:

如何保证数据库数据安全?
-----------------------------------

.. i18n: We offer an option to anonymise your data through our :mod:`anonymization` module.
.. i18n: This module allows you to keep your data confidential for a given database. This process is useful if you want to use the migration process and protect your own or your customers' confidential data. The principle is that you run an anonymization tool which will hide your confidential data (they are replaced by 'XXX' characters). Then you can send the anonymized database to the migration team. Once you get back your migrated database, you restore it and reverse the anonymisation process to recover your previous data.
..

我们提供了一个的选项，让您的数据通过我们的 :mod:`anonymization` 模块来隐匿起来.这个模块可以让你保持一个指定数据库的数据机密性。 这是非常有用的功能，在你要迁移数据的过程中保护您自己或您的客户的机密数据。其原理是，你运行一个隐匿数据的工具，它会隐藏你的机密数据（它们被替换为'XXX'字符）。然后，您就可以发送已经经过隐匿的数据给你的数据库迁移团队。一旦你数据库迁移完成，可以还原和恢复回以前的隐匿数据。

.. i18n: We suggest you to work on a copy of your database, so be sure to make a backup before starting the anonymisation process.
..

We suggest you to work on a copy of your database, so be sure to make a backup before starting the anonymisation process.

.. i18n: The first step is to install and configure the :mod:`anonymization` module. The menus are located in :menuselection:`Administration --> Database anonymization`.
..

The first step is to install and configure the :mod:`anonymization` module. The menus are located in :menuselection:`Administration --> Database anonymization`.

.. i18n: *Anonymization History* 
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^
..

*Anonymization History* 
^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: This is the history of all the anonymisation (and the reverse process) that occurred on a particular database. 
..

This is the history of all the anonymisation (and the reverse process) that occurred on a particular database. 

.. i18n: *Anonymize database*
.. i18n: ^^^^^^^^^^^^^^^^^^^^ 
..

*Anonymize database*
^^^^^^^^^^^^^^^^^^^^ 

.. i18n: This is the wizard that will actually anonymise the database. This wizard is also responsible to reverse the anonymization process. 
..

This is the wizard that will actually anonymise the database. This wizard is also responsible to reverse the anonymization process. 

.. i18n: *Anonymized Fields*
.. i18n: ^^^^^^^^^^^^^^^^^^^
..

*Anonymized Fields*
^^^^^^^^^^^^^^^^^^^

.. i18n: **Pre-defined fields**
..

**Pre-defined fields**

.. i18n: On module installation, OpenERP will create some fields considered as important to anonymise, these are:
.. i18n:  
.. i18n:   * Partner: Name 
..

On module installation, OpenERP will create some fields considered as important to anonymise, these are:
 
  * Partner: Name 

.. i18n:   * Partner: Reference 
.. i18n:   
.. i18n:   * Partner Addresses: Contact Name 
.. i18n: 
.. i18n:   * Partner Addresses: City 
.. i18n: 	
.. i18n:   * Partner Addresses: Street 
.. i18n: 	
.. i18n:   * Partner Addresses: Street2 
.. i18n: 
.. i18n:   * Partner Addresses: Zip 
.. i18n: 
.. i18n:   * Partner Addresses: Phone 
.. i18n: 
.. i18n:   * Partner Addresses: Fax 
.. i18n: 
.. i18n:   * Partner Addresses: Mobile 
.. i18n: 
.. i18n:   * Partner Addresses: E-Mail 
.. i18n: 
.. i18n:   * Invoice: Untaxed (amount_untaxed) 
.. i18n: 
.. i18n:   * Invoice: Tax 
.. i18n: 
.. i18n:   * Invoice: Total (amount_total) 
.. i18n: 
.. i18n:   * Invoice: Total (check_total) 
.. i18n: 
.. i18n:   * Invoice: Residual 
.. i18n: 
.. i18n:   * Invoice line: Unit Price 
.. i18n: 
.. i18n:   * Invoice line: Subtotal 
.. i18n: 
.. i18n:   * Invoice move line: Debit 
.. i18n: 
.. i18n:   * Invoice move line: Credit 
.. i18n: 
.. i18n:   * Invoice move line: Tax/Base Amount 
.. i18n: 
.. i18n:   * Invoice move line: Amount Currency 
.. i18n: 
.. i18n:   * Invoice move line: Taxed Amount 
.. i18n: 
.. i18n:   * Sale order: amount_tax 
.. i18n: 
.. i18n:   * Sale order: amount_untaxed 
.. i18n: 
.. i18n:   * Sale order: amount_total 
.. i18n: 
.. i18n:   * Sale order line: price unit 
.. i18n: 
.. i18n:   * Sale order line: discount 
.. i18n:  
.. i18n:   * Purchase order: amount_tax 
.. i18n: 
.. i18n:   * Purchase order: amount_untaxed 
.. i18n: 
.. i18n:   * Purchase order: amount_total 
.. i18n: 
.. i18n:   * Purchase order line: price_unit 
..

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

.. i18n: The anonymised values are: 
..

The anonymised values are: 

.. i18n:   * char field: xxx + record id 
.. i18n:   * text field: xxx + record id 
.. i18n:   * selection field: xxx + record id 
.. i18n:   * integer field: 1 
.. i18n:   * float field:  0.0 
.. i18n:   * date field: 2011-11-11 
.. i18n:   * datetime field: 2011-11-11 11:11:11 
..

  * char field: xxx + record id 
  * text field: xxx + record id 
  * selection field: xxx + record id 
  * integer field: 1 
  * float field:  0.0 
  * date field: 2011-11-11 
  * datetime field: 2011-11-11 11:11:11 

.. i18n: All attachment object contents are replaced by an empty string in the database. 
..

All attachment object contents are replaced by an empty string in the database. 

.. i18n: **Create new fields to anonymize**
..

**Create new fields to anonymize**

.. i18n: You also have the possibility to add other fields that you want to keep confidential. You have to create them manually.
..

You also have the possibility to add other fields that you want to keep confidential. You have to create them manually.

.. i18n: First choose an object by using the popup (:guilabel:`Object` field). You can also enter the object model name directly into the :guilabel:`Object Name` field, if you know it. These two fields are linked to each other; fill out one of both and the other one will be filled automatically. 
..

First choose an object by using the popup (:guilabel:`Object` field). You can also enter the object model name directly into the :guilabel:`Object Name` field, if you know it. These two fields are linked to each other; fill out one of both and the other one will be filled automatically. 

.. i18n: You then choose the field by using the popup (:guilabel:`Field` field). You can also enter the field name directly if you know it (:guilabel:`Field Name` field). These two fields are linked to each other in the same way as described above. 
..

You then choose the field by using the popup (:guilabel:`Field` field). You can also enter the field name directly if you know it (:guilabel:`Field Name` field). These two fields are linked to each other in the same way as described above. 

.. i18n: The :guilabel:`State` field values are: 
..

The :guilabel:`State` field values are: 

.. i18n: * :guilabel:`Clear`: the field values have their original status in the database 
.. i18n: 
.. i18n: * :guilabel:`Anonymized`: the field values are anonymised in the database 
.. i18n: 
.. i18n: * :guilabel:`Not Existing`: the field does not exist in the database.
.. i18n:   This is probably a field which comes from the module's data file. For example, the data file creates some predefined anonymized fields, but the module might not be installed. These fields are ignored by the anonymisation process. 
..

* :guilabel:`Clear`: the field values have their original status in the database 

* :guilabel:`Anonymized`: the field values are anonymised in the database 

* :guilabel:`Not Existing`: the field does not exist in the database.
  This is probably a field which comes from the module's data file. For example, the data file creates some predefined anonymized fields, but the module might not be installed. These fields are ignored by the anonymisation process. 
