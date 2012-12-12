
.. module:: hr_timesheet_invoice
    :synopsis: Invoice on analytic lines (Official, Quality Certified)
    :noindex:
.. 

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. tip:: This module is part of the OpenERP software, the leading Open Source 
  enterprise management system. If you want to discover OpenERP, check our 
  `screencasts <http://openerp.tv>`_ or download 
  `OpenERP <http://openerp.com>`_ directly.

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hr_timesheet_invoice"></div>
    <script src="http://js-kit.com/ratings.js"></script>

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

Description
-----------

::

  Module to generate invoices based on costs (human resources, expenses, ...).
  You can define price lists in analytic account, make some theoretical revenue
  reports, eso.

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/hr_timesheet_invoice.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/hr_timesheet_invoice.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/hr_timesheet_invoice.zip>`_


Dependencies
------------

 * :mod:`account`
 * :mod:`hr_timesheet`

Reports
-------

 * Cost Ledger

 * Timesheet Profit

Menus
-------

 * Financial Management/Periodical Processing/Entries to invoice
 * Financial Management/Periodical Processing/Entries to invoice/Uninvoiced Entries
 * Financial Management/Periodical Processing/Entries to invoice/My Uninvoiced Entries
 * Financial Management/Configuration/Analytic Accounting/Analytic Accounts/Analytic Chart of Accounts/Open Analytic Accounts
 * .../Configuration/Analytic Accounting/Analytic Accounts/Analytic Chart of Accounts/Open Analytic Accounts/Unclosed Invoiceable Accounts
 * Financial Management/Configuration/Analytic Accounting/Analytic Accounts/Analytic Chart of Accounts/Draft Analytic Accounts
 * Financial Management/Configuration/Analytic Accounting/Analytic Accounts/Analytic Chart of Accounts/Pending Analytic Accounts
 * Financial Management/Configuration/Analytic Accounting/Analytic Accounts/Types of Invoicing
 * Human Resources/Reporting/Timesheet Profit

Views
-----

 * \* INHERIT account.analytic.account.invoice.form (form)
 * \* INHERIT hr.analytic.timesheet.form (form)
 * \* INHERIT hr.analytic.timesheet.form2 (form)
 * \* INHERIT hr.analytic.timesheet.tree (tree)
 * \* INHERIT hr.analytic.timesheet.tree2 (tree)
 * \* INHERIT account.analytic.line.tree.to_invoice (tree)
 * \* INHERIT account.analytic.line.form.to_invoice (form)
 * hr_timesheet_invoice.factor.form (form)
 * hr_timesheet_invoice.factor.tree (tree)


Objects
-------

Object: Invoice rate (hr_timesheet_invoice.factor)
##################################################



:factor: Discount (%), float, required





:name: Internal name, char, required





:customer_name: Visible name, char


