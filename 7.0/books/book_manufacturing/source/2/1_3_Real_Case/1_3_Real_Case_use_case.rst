Business Example
================

In this example, you will configure a system that enables you to:

* buy products from a supplier,

* stock the products in a warehouse,

* sell these products to a customer.

The system should support all aspects of invoicing, payments to suppliers and receipts from
customers.

Basic Settings
==============

For this business case, you will have to model:

* accounts and account types,

* the suppliers and a supplier category,

* the customers and a customer category,

* some products and a product category,

* an inventory,

* a purchase order,

* a sales order,

* invoices,

* payments.

To test the system, you will need at least one supplier, one customer, one product, a warehouse, a
minimal chart of accounts and a bank account.

Get your Database Up and Running without Demo Data
==================================================

Please note that the new database you have to create, will *not* include demo data and only the minimally required functionality as a starting point. You will need to know your super administrator password for this – or you will have to ask your ICT manager for the password to be able to create this database.

Please refer to :ref:`part2-man-start` for more information about how to create a new database that you will give the name of your company.

As a reminder, please find the steps below, without further explanation.

Start by creating a new database from the :guilabel:`Welcome` page by clicking :guilabel:`Databases` and then completing the following fields on the :guilabel:`Create Database` form.

*  :guilabel:`Super admin password` : by default it is \ ``admin`` \, if you or your system
   administrator have not changed it,

*  :guilabel:`New database name` : \ ``YourCompany``\,

*  :guilabel:`Load Demonstration data` checkbox: \ ``unchecked``\,

*  :guilabel:`Default Language` : \ ``English (US)``\,

*  :guilabel:`Administrator password` : \ ``admin``\,

*  :guilabel:`Confirm password` : \ ``admin``\.

Press `Create` to start creating the database.

OpenERP suggests that you configure your database using a series of questions. In the software, these series of questions are managed through so-called ``Configuration Wizards``.

Click the ``Start Configuration`` button to continue.

The next configuration wizard will help you to decide what your user interface will look like, whether the screens will only show the most important fields - ``Simplified`` - or whether you also want to see the fields for the more advanced users, the ``Extended`` view. Select ``Extended`` and click :guilabel:`Next` to continue.

.. tip:: User Preferences

       You can easily switch from Simplified to Extended view by changing your `User Preferences`.

In the next wizard, you can fill your company data, select your company's base currency and add your company logo which can be printed on reports. Fill out the required data and click :guilabel:`Next` to continue.

Select the ``Warehouse Management``, ``Purchase Management``, ``Sales Management``, ``Manufacturing`` and ``Accounting & Finance`` business applications for installation and click :guilabel:`Install`. Now OpenERP will start to install these five applications, allowing you to do a complete  cycle, from sales / warehouse / purchase / manufacturing to invoice. You will have to wait for the next configuration wizard to be displayed (*Loading* will appear).

.. figure:: images/apps.png
   :scale: 80
   :align: center

   *Selecting the Required Functionality*

.. tip:: Reconfigure

      Keep in mind that you can change or reconfigure the system any time, for instance through the `Reconfigure` option in the main bar.

When you choose a business application for installation, OpenERP will automatically propose to add or configure related (smaller) applications to enrich your system. When you install Sales, OpenERP will also ask you whether you want to install Invoicing Journals for instance.

:guilabel:`Skip` the step that asks you to configure your Accounting Chart, because you will learn how to create accounts. 

In the Purchases Application Configuration screen, simply click ``Configure`` to continue the database creation. 

The following wizards will appear:

* Configure your *Sales Management* application: click ``Configure`` to accept the default settings (no options checked).

* Configure your *MRP Application Configuration* application: click ``Configure`` to accept the default settings.

* Configure your *Accounting* application: click ``Configure`` to accept the default settings.

* Configure *Sales Order Logistics*: click ``Next`` to accept the default settings.

OpenERP's menu will be displayed, because your system is now ready for actual configuration. 

.. note:: Setup Wizard

        You will have to go through the Setup wizard in steps. You have two options:

        1. If you click the `Start Configuration` button, OpenERP guides you through a series of steps to: :guilabel:`Configure Your Interface` - proceed with ``Simplified`` (the other option is ``Extended``); and :guilabel:`Configure Your Company Information` - enter a :guilabel:`Company Name` and select a :guilabel:`Currency` for your company. Then OpenERP helps you to install various applications with different functionality through wizards.

        - OR -

        2. When you click the button `Skip Configuration Wizards`, you can have the screen as shown in screenshot :ref:`fig-oech03st`. Then you can start working with this minimal database (*we will not use this option here*).

.. _fig-oech03st:

.. figure::  images/openerp_ch03_start.png
   :scale: 65
   :align: center

   *Starting the minimal database*



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

