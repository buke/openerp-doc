
.. i18n: .. module:: hr_timesheet_invoice
.. i18n:     :synopsis: Invoice on analytic lines (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: hr_timesheet_invoice
    :synopsis: Invoice on analytic lines (Official, Quality Certified)
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:       <br />
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />
..

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: .. tip:: This module is part of the OpenERP software, the leading Open Source 
.. i18n:   enterprise management system. If you want to discover OpenERP, check our 
.. i18n:   `screencasts <http://openerp.tv>`_ or download 
.. i18n:   `OpenERP <http://openerp.com>`_ directly.
..

.. tip:: This module is part of the OpenERP software, the leading Open Source 
  enterprise management system. If you want to discover OpenERP, check our 
  `screencasts <http://openerp.tv>`_ or download 
  `OpenERP <http://openerp.com>`_ directly.

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hr_timesheet_invoice"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hr_timesheet_invoice"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Invoice on analytic lines (*hr_timesheet_invoice*)
.. i18n: ==================================================
.. i18n: :Module: hr_timesheet_invoice
.. i18n: :Name: Invoice on analytic lines
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: hr_timesheet_invoice
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

Invoice on analytic lines (*hr_timesheet_invoice*)
==================================================
:Module: hr_timesheet_invoice
:Name: Invoice on analytic lines
:Version: 5.0.1.0
:Author: Tiny
:Directory: hr_timesheet_invoice
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Module to generate invoices based on costs (human resources, expenses, ...).
.. i18n:   You can define price lists in analytic account, make some theoretical revenue
.. i18n:   reports, eso.
..

::

  Module to generate invoices based on costs (human resources, expenses, ...).
  You can define price lists in analytic account, make some theoretical revenue
  reports, eso.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/hr_timesheet_invoice.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/hr_timesheet_invoice.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/hr_timesheet_invoice.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/hr_timesheet_invoice.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/hr_timesheet_invoice.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/hr_timesheet_invoice.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`account`
.. i18n:  * :mod:`hr_timesheet`
..

 * :mod:`account`
 * :mod:`hr_timesheet`

.. i18n: Reports
.. i18n: -------
..

Reports
-------

.. i18n:  * Cost Ledger
.. i18n: 
.. i18n:  * Timesheet Profit
..

 * Cost Ledger

 * Timesheet Profit

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Financial Management/Periodical Processing/Entries to invoice
.. i18n:  * Financial Management/Periodical Processing/Entries to invoice/Uninvoiced Entries
.. i18n:  * Financial Management/Periodical Processing/Entries to invoice/My Uninvoiced Entries
.. i18n:  * Financial Management/Configuration/Analytic Accounting/Analytic Accounts/Analytic Chart of Accounts/Open Analytic Accounts
.. i18n:  * .../Configuration/Analytic Accounting/Analytic Accounts/Analytic Chart of Accounts/Open Analytic Accounts/Unclosed Invoiceable Accounts
.. i18n:  * Financial Management/Configuration/Analytic Accounting/Analytic Accounts/Analytic Chart of Accounts/Draft Analytic Accounts
.. i18n:  * Financial Management/Configuration/Analytic Accounting/Analytic Accounts/Analytic Chart of Accounts/Pending Analytic Accounts
.. i18n:  * Financial Management/Configuration/Analytic Accounting/Analytic Accounts/Types of Invoicing
.. i18n:  * Human Resources/Reporting/Timesheet Profit
..

 * Financial Management/Periodical Processing/Entries to invoice
 * Financial Management/Periodical Processing/Entries to invoice/Uninvoiced Entries
 * Financial Management/Periodical Processing/Entries to invoice/My Uninvoiced Entries
 * Financial Management/Configuration/Analytic Accounting/Analytic Accounts/Analytic Chart of Accounts/Open Analytic Accounts
 * .../Configuration/Analytic Accounting/Analytic Accounts/Analytic Chart of Accounts/Open Analytic Accounts/Unclosed Invoiceable Accounts
 * Financial Management/Configuration/Analytic Accounting/Analytic Accounts/Analytic Chart of Accounts/Draft Analytic Accounts
 * Financial Management/Configuration/Analytic Accounting/Analytic Accounts/Analytic Chart of Accounts/Pending Analytic Accounts
 * Financial Management/Configuration/Analytic Accounting/Analytic Accounts/Types of Invoicing
 * Human Resources/Reporting/Timesheet Profit

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT account.analytic.account.invoice.form (form)
.. i18n:  * \* INHERIT hr.analytic.timesheet.form (form)
.. i18n:  * \* INHERIT hr.analytic.timesheet.form2 (form)
.. i18n:  * \* INHERIT hr.analytic.timesheet.tree (tree)
.. i18n:  * \* INHERIT hr.analytic.timesheet.tree2 (tree)
.. i18n:  * \* INHERIT account.analytic.line.tree.to_invoice (tree)
.. i18n:  * \* INHERIT account.analytic.line.form.to_invoice (form)
.. i18n:  * hr_timesheet_invoice.factor.form (form)
.. i18n:  * hr_timesheet_invoice.factor.tree (tree)
..

 * \* INHERIT account.analytic.account.invoice.form (form)
 * \* INHERIT hr.analytic.timesheet.form (form)
 * \* INHERIT hr.analytic.timesheet.form2 (form)
 * \* INHERIT hr.analytic.timesheet.tree (tree)
 * \* INHERIT hr.analytic.timesheet.tree2 (tree)
 * \* INHERIT account.analytic.line.tree.to_invoice (tree)
 * \* INHERIT account.analytic.line.form.to_invoice (form)
 * hr_timesheet_invoice.factor.form (form)
 * hr_timesheet_invoice.factor.tree (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Invoice rate (hr_timesheet_invoice.factor)
.. i18n: ##################################################
..

Object: Invoice rate (hr_timesheet_invoice.factor)
##################################################

.. i18n: :factor: Discount (%), float, required
..

:factor: Discount (%), float, required

.. i18n: :name: Internal name, char, required
..

:name: Internal name, char, required

.. i18n: :customer_name: Visible name, char
..

:customer_name: Visible name, char
