
.. index::
   single: analytic; accounts

Putting Analytic Accounts in Place
==================================

For the initial setup of good analytic accounts you should:

* set up the chart of accounts,

* create the different journals,

* link the analytic journals to your accounting journals.

Setting up the Chart of Accounts
--------------------------------

Start by choosing the most suitable analytic representation for your company before entering it into OpenERP. To create the different analytic accounts, use the menu :menuselection:`Accounting--> Configuration --> Analytic Accounting --> Analytic Accounts` and click the :guilabel:`Create` button.
Note that the data you see when creating an analytic account will depend upon the business applications installed.

.. figure::  images/account_analytic_form.png
   :scale: 75
   :align: center

   *Setting up an Analytic Account*

To create an analytic account, you have to complete the main fields:

* the :guilabel:`Account Name`,

* the :guilabel:`Code/Reference`: used as a shortcut for selecting the account,

* the :guilabel:`Parent Analytic Account`: use this field to define the hierarchy between the accounts.

* the :guilabel:`Account Type`: just like general accounts, the \ ``View``\ type is used for virtual accounts which are used only to create a hierarchical structure and for subtotals, and not to store accounting entries. The \ ``Normal``\ type will be used for analytic accounts containing entries.

If an analytic account (e.g. a project) is for a limited time, you can define a start and end date here.

The :guilabel:`Maximum Time` can be used for contracts with a fixed limit of hours to use.

.. index::
   single: invoicing

.. tip:: Invoicing

        You have several methods available to you in OpenERP for automated invoicing:

        * Service companies usually use invoicing from purchase orders, analytic accounts or
          project management tasks.

        * Manufacturing and trading companies more often use invoicing from deliveries or customer purchase
          orders.

        For more information about invoicing from projects, we refer to the book (soon to be released) about Project and Services Management.

Once you have defined the different analytic accounts, you can view your chart through the menu :menuselection:`Accounting --> Charts --> Chart of Analytic Accounts`. You can display analytic accounts for one or more periods or for an entire financial year.

.. figure::  images/account_analytic_chart.png
   :scale: 85
   :align: center

   *Analytic Chart of Accounts*

.. index::
   single: module; hr_timesheet_invoice
   single: module; account_analytic_analysis

.. tip:: Setting up an Analytic Account

        The setup screen for an analytic account can vary according to the modules installed in your database.
        For example, you will see information about recharging services only if you have the module :mod:`hr_timesheet_invoice` installed.

        Some of these modules add helpful management statistics to the analytic account. The most useful is probably the module :mod:`account_analytic_analysis`, which adds such information as indicators about your margins, invoicing amounts, and latest service dates and invoice dates.

Creating Journals
-----------------

Once the analytic chart has been created for your company, you have to create the different journals.
These journals enable you to categorise the different accounting entries by their type, such as:

* services,

* expense reimbursements,

* purchases of materials,

* miscellaneous expenditure,

* sales.


.. index::
   single: journal; minimal journals

.. note::  Minimal Journals

        At a minimum, you have to create one analytic journal for Sales and one for Purchases.
        If you do not create these two, OpenERP will not validate invoices linked to an analytic account,
        because it would not be able to create an analytic accounting entry automatically.

.. figure::  images/account_analytic_journal.png
   :scale: 85
   :align: center

   *Creating an Analytic Journal*

To define your analytic journals, use the menu :menuselection:`Accounting --> Configuration --> Analytic Accounting --> Analytic Journals` then click the :guilabel:`Create` button.

It is easy to create an analytic journal. Just give it a :guilabel:`Journal Name`, a :guilabel:`Journal Code` and a :guilabel:`Type`. The
types available are:

* \ ``Sale``\, for sales to customers and for credit notes,

* \ ``Purchase``\, for purchases and expenses,

* \ ``Cash``\, for financial entries,

* \ ``Situation``\, to adjust accounts when starting an activity, or at the end of the financial year,

* \ ``General``\, for all other entries.

The analytic journal now has to be linked to your general journals to allow OpenERP to post the analytic entries. For example, if you enter an invoice for a customer, OpenERP will automatically search for the analytic journal of type \ ``Sales``\ linked to your Sales Journal.
Go to :menuselection:`Accounting--> Configuration --> Financial Accounting --> Journals --> Journals` and select for instance the Sales journal. In the :guilabel:`Analytic Journal` select the analytic sales journal.

.. figure::  images/account_general_journal.png
   :scale: 85
   :align: center

   *Linking an Analytic Journal to a Journal*

Working with Analytic Defaults
------------------------------

You can work with analytic default accounts in OpenERP by installing the :mod:`account_analytic_default` module. Notice that this module is also linked with the :mod:`sale`, :mod:`stock` and :mod:`procurement` modules.

The system will automatically select analytic accounts according to the following criteria:

* Product
* Partner
* User
* Company
* Date

You can configure these criteria using the menu :menuselection:`Accounting --> Configuration --> Analytic Accounting --> Analytic Defaults` and clicking the `Create` button.
According to the criteria you define here, the correct analytic account will be proposed when creating an order or an invoice.

.. figure::  images/account_analytic_default.png
   :scale: 85
   :align: center

   *Specify Criteria to Automatically Select Analytic Account*

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

