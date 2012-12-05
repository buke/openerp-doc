.. i18n: .. index::
.. i18n:    single: analytic; records
.. i18n: ..
..

.. index::
   single: analytic; records
..

.. i18n: Analytic Entries
.. i18n: ================
..

辅助核算凭证
================

.. i18n: Integrated with General Accounting
.. i18n: ----------------------------------
..

Integrated with General Accounting
----------------------------------

.. i18n: Just as in general accounting, analytic entries should be related to an account and an analytic journal.
..

Just as in general accounting, analytic entries should be related to an account and an analytic journal.

.. i18n: Analytic records can be distinguished from general records by the following characteristics:
..

Analytic records can be distinguished from general records by the following characteristics:

.. i18n: * they are not necessarily legal accounting documents,
.. i18n: 
.. i18n: * they do not necessarily belong to an existing accounting period,
.. i18n: 
.. i18n: * they are managed according to their date and not an accounting period,
.. i18n: 
.. i18n: * they do not generate both a debit and a credit entry, but a positive amount (income) or a negative amount (cost).
..

* they are not necessarily legal accounting documents,

* they do not necessarily belong to an existing accounting period,

* they are managed according to their date and not an accounting period,

* they do not generate both a debit and a credit entry, but a positive amount (income) or a negative amount (cost).

.. i18n: .. _fig-accanmv:
.. i18n: 
.. i18n: .. figure::  images/account_analytic_move.png
.. i18n:    :scale: 85
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Analytic Account Records for a Customer Project*
..

.. _fig-accanmv:

.. figure::  images/account_analytic_move.png
   :scale: 85
   :align: center

   *Analytic Account Records for a Customer Project*

.. i18n: The figure :ref:`fig-accanmv` represents the entries in an analytic account for a customer project.
..

The figure :ref:`fig-accanmv` represents the entries in an analytic account for a customer project.

.. i18n: You can see there:
..

You can see there:

.. i18n: * the service costs for staff working on the project,
.. i18n: 
.. i18n: * the costs for reimbursing the expenses of a return journey to the customer,
.. i18n: 
.. i18n: * purchases of goods that have been delivered to the customer,
.. i18n: 
.. i18n: * sales for recharging these costs.
..

* the service costs for staff working on the project,

* the costs for reimbursing the expenses of a return journey to the customer,

* purchases of goods that have been delivered to the customer,

* sales for recharging these costs.

.. i18n: Manual Entries
.. i18n: --------------
..

手工录入凭证
--------------

.. i18n: Even though most analytic entries are produced automatically by the other OpenERP documents, it is sometimes necessary to record manual entries. It is usually needed for certain analytic operations which have no counterpart in the general accounts.
..

Even though most analytic entries are produced automatically by the other OpenERP documents, it is sometimes necessary to record manual entries. It is usually needed for certain analytic operations which have no counterpart in the general accounts.

.. i18n: To record manual entries, go to the menu :menuselection:`Accounting --> Journal Entries --> Analytic Journal Items` and click the :guilabel:`Create` button.
..

To record manual entries, go to the menu :menuselection:`Accounting --> Journal Entries --> Analytic Journal Items` and click the :guilabel:`Create` button.

.. i18n: .. index::
.. i18n:    single: analytic; entries
..

.. index::
   single: analytic; entries

.. i18n: .. note:: Analytic Entries
.. i18n: 
.. i18n:         To make an analytic entry, OpenERP asks you to specify a general account. This is given only for information in the different cross-reports. It will not create any new entries in the general accounts.
..

.. note:: Analytic Entries

        To make an analytic entry, OpenERP asks you to specify a general account. This is given only for information in the different cross-reports. It will not create any new entries in the general accounts.

.. i18n: Select a journal and complete the different fields. Write an expense as a negative amount and income as a positive amount.
..

Select a journal and complete the different fields. Write an expense as a negative amount and income as a positive amount.

.. i18n: .. index::
.. i18n:    pair: cost; allocation
..

.. index::
   pair: cost; allocation

.. i18n: .. tip::  Entering a Date
.. i18n: 
.. i18n:         To enter a date in the editable list you can use the calendar widget in the web client or, in the
.. i18n:         GTK client, if you enter just the day of the month OpenERP automatically completes the month and
.. i18n:         year when you press the :kbd:`Tab` key.
..

.. tip::  Entering a Date

        To enter a date in the editable list you can use the calendar widget in the web client or, in the
        GTK client, if you enter just the day of the month OpenERP automatically completes the month and
        year when you press the :kbd:`Tab` key.

.. i18n: .. note:: Example Cost Redistribution
.. i18n: 
.. i18n:         One of the uses of manual data entry for analytic operations is reallocation of costs. For
.. i18n:         example, if a development has been done for a given project, but can be used again for another
.. i18n:         project, you can reallocate part of the cost to the other project.
.. i18n: 
.. i18n:         In this case, make a positive entry on the first account and a negative entry for the same
.. i18n:         amount on the account of the second project.
..

.. note:: Example Cost Redistribution

        One of the uses of manual data entry for analytic operations is reallocation of costs. For
        example, if a development has been done for a given project, but can be used again for another
        project, you can reallocate part of the cost to the other project.

        In this case, make a positive entry on the first account and a negative entry for the same
        amount on the account of the second project.

.. i18n: Automated Entries
.. i18n: -----------------
..

自动生成凭证
-----------------

.. i18n: Analytic accounting is totally integrated with the other OpenERP modules, so you never have to re-enter the records. They are automatically generated by the following operations:
..

Analytic accounting is totally integrated with the other OpenERP modules, so you never have to re-enter the records. They are automatically generated by the following operations:

.. i18n: * confirmation of an invoice generates analytic entries for sales or purchases connected to the
.. i18n:   account shown in the invoice line,
.. i18n: 
.. i18n: * the entry of a service generates an analytic entry for the cost of this service to the given project,
.. i18n: 
.. i18n: * the manufacturing of a product generates an entry for the manufacturing cost of each operation in the product range.
..

* confirmation of an invoice generates analytic entries for sales or purchases connected to the
  account shown in the invoice line,

* the entry of a service generates an analytic entry for the cost of this service to the given project,

* the manufacturing of a product generates an entry for the manufacturing cost of each operation in the product range.

.. i18n: Other documents linked to one of these three operations produce analytic records indirectly. For example, when you are entering a customer sales order, you can link it to the customer's analytic account. When you are managing by case or project, mark the project with that order. This order will then generate a customer invoice, which will be linked to the analytic account. When the invoice is validated, it will automatically create general and analytic accounting records for the corresponding project.
..

Other documents linked to one of these three operations produce analytic records indirectly. For example, when you are entering a customer sales order, you can link it to the customer's analytic account. When you are managing by case or project, mark the project with that order. This order will then generate a customer invoice, which will be linked to the analytic account. When the invoice is validated, it will automatically create general and analytic accounting records for the corresponding project.

.. i18n: Expense receipts from an employee can be linked to an analytic account for reimbursement. When a receipt is approved by the company, a purchase invoice is created. This invoice represents a debit on the company in favour of the employee. Each line of the purchase invoice is then linked to an analytic account which automatically allocates the costs for that receipt to the corresponding project.
..

Expense receipts from an employee can be linked to an analytic account for reimbursement. When a receipt is approved by the company, a purchase invoice is created. This invoice represents a debit on the company in favour of the employee. Each line of the purchase invoice is then linked to an analytic account which automatically allocates the costs for that receipt to the corresponding project.

.. i18n: To visualise the general entries following these different actions, you can use one of the following menus:
..

To visualise the general entries following these different actions, you can use one of the following menus:

.. i18n:         #. To see all of the entries, :menuselection:`Accounting --> Journal Entries --> Analytic Journal Items`
.. i18n: 
.. i18n:         #. To see the entries per account, per user, per product or per partner, you can use the menu :menuselection:`Accounting --> Reporting --> Statistic Reports --> Analytic Entries Analysis`.
..

        #. To see all of the entries, :menuselection:`Accounting --> Journal Entries --> Analytic Journal Items`

        #. To see the entries per account, per user, per product or per partner, you can use the menu :menuselection:`Accounting --> Reporting --> Statistic Reports --> Analytic Entries Analysis`.

.. i18n: .. figure::  images/account_analytic_analysis2.png
.. i18n:    :scale: 85
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Analytic Entries Analysis*
..

.. figure::  images/account_analytic_analysis2.png
   :scale: 85
   :align: center

   *Analytic Entries Analysis*

.. i18n: Analytic Models
.. i18n: ---------------
..

Analytic Models
---------------

.. i18n: Standard OpenERP allows you to post analytic entries to one chart at a time. Using the `Analytic Model` concept (install the option ``Multiple Analytic Plans`` from the `Add New Features` wizard), you can distribute your income or expenses to one or several analytic charts of account at the same time.
.. i18n: You can define the combination of analytic plans through the menu :menuselection:`Accounting --> Configuration --> Analytic Accounting --> Multi Plans --> Analytic Plan.`
..

Standard OpenERP allows you to post analytic entries to one chart at a time. Using the `Analytic Model` concept (install the option ``Multiple Analytic Plans`` from the `Add New Features` wizard), you can distribute your income or expenses to one or several analytic charts of account at the same time.
You can define the combination of analytic plans through the menu :menuselection:`Accounting --> Configuration --> Analytic Accounting --> Multi Plans --> Analytic Plan.`

.. i18n: .. figure::  images/account_analytic_plan_61.png
.. i18n:    :scale: 85
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Definition of Analytic Plan*
..

.. figure::  images/account_analytic_plan_61.png
   :scale: 85
   :align: center

   *Definition of Analytic Plan*

.. i18n: Using the link `Distribution Models` at the right side of the `Analytic Plan` form, you can define the distribution of either your expenses while creating a supplier invoice, or revenue when defining customer invoices.
.. i18n: Thanks to these models, you can have one amount distributed amongst several analytic accounts. Models can be reused, and they can be applied to one analytic chart of accounts, but also to a combination of various charts of account, such as projects and cost centers.
..

Using the link `Distribution Models` at the right side of the `Analytic Plan` form, you can define the distribution of either your expenses while creating a supplier invoice, or revenue when defining customer invoices.
Thanks to these models, you can have one amount distributed amongst several analytic accounts. Models can be reused, and they can be applied to one analytic chart of accounts, but also to a combination of various charts of account, such as projects and cost centers.

.. i18n: .. figure::  images/account_distribution_model_61.png
.. i18n:    :scale: 85
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Definition of Distribution Models*
..

.. figure::  images/account_distribution_model_61.png
   :scale: 85
   :align: center

   *Definition of Distribution Models*

.. i18n: For example, when you create the invoice (suppose 1000 EUR) for the product ``Client Project`` with the analytic distribution defined above.
..

For example, when you create the invoice (suppose 1000 EUR) for the product ``Client Project`` with the analytic distribution defined above.

.. i18n: When the invoice has been validated, you can find the Analytic Journal Entries with the amount distributed amongst the analytic accounts through the menu :menuselection:`Accounting --> Journal Entries --> Analytic Journal Items.`
..

When the invoice has been validated, you can find the Analytic Journal Entries with the amount distributed amongst the analytic accounts through the menu :menuselection:`Accounting --> Journal Entries --> Analytic Journal Items.`

.. i18n: .. figure::  images/analytic_journal_entry_analytic_distribution_61.png
.. i18n:    :scale: 85
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Journal Entries with Distributed Amount*
..

.. figure::  images/analytic_journal_entry_analytic_distribution_61.png
   :scale: 85
   :align: center

   *Journal Entries with Distributed Amount*

.. i18n: You can also specify a default `Analytic Distribution` for a particular product, partner, user and company for a specific time interval using the menu :menuselection:`Accounting --> Configuration --> Analytic Accounting --> Analytic Defaults.`
..

You can also specify a default `Analytic Distribution` for a particular product, partner, user and company for a specific time interval using the menu :menuselection:`Accounting --> Configuration --> Analytic Accounting --> Analytic Defaults.`

.. i18n: .. Copyright © Open Object Press. All rights reserved.
..

.. Copyright © Open Object Press. All rights reserved.

.. i18n: .. You may take electronic copy of this publication and distribute it if you don't
.. i18n: .. change the content. You can also print a copy to be read by yourself only.
..

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. i18n: .. We have contracts with different publishers in different countries to sell and
.. i18n: .. distribute paper or electronic based versions of this book (translated or not)
.. i18n: .. in bookstores. This helps to distribute and promote the OpenERP product. It
.. i18n: .. also helps us to create incentives to pay contributors and authors using author
.. i18n: .. rights of these sales.
..

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the OpenERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. i18n: .. Due to this, grants to translate, modify or sell this book are strictly
.. i18n: .. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. i18n: .. written authorisation for this.
..

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. i18n: .. Many of the designations used by manufacturers and suppliers to distinguish their
.. i18n: .. products are claimed as trademarks. Where those designations appear in this book,
.. i18n: .. and Open Object Press was aware of a trademark claim, the designations have been
.. i18n: .. printed in initial capitals.
..

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. i18n: .. While every precaution has been taken in the preparation of this book, the publisher
.. i18n: .. and the authors assume no responsibility for errors or omissions, or for damages
.. i18n: .. resulting from the use of the information contained herein.
..

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. i18n: .. Published by Open Object Press, Grand Rosière, Belgium
..

.. Published by Open Object Press, Grand Rosière, Belgium
