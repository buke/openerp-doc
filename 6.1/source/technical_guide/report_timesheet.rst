
.. module:: report_timesheet
    :synopsis: Timesheet - Reporting (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_timesheet"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Timesheet - Reporting (*report_timesheet*)
==========================================
:Module: report_timesheet
:Name: Timesheet - Reporting
:Version: 5.0.1.0
:Author: Tiny
:Directory: report_timesheet
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  Module to add timesheet views like
      All Month, Timesheet By User, Timesheet Of Month, Timesheet By Account

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/report_timesheet.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/report_timesheet.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/report_timesheet.zip>`_


Dependencies
------------

 * :mod:`hr_timesheet`
 * :mod:`hr_timesheet_invoice`

Reports
-------

None


Menus
-------

 * Human Resources/Reporting/This Month
 * Human Resources/Reporting/This Month/Timesheet by user (this month)
 * Human Resources/Reporting/This Month/My Timesheet of the Month
 * Human Resources/Reporting/All Months
 * Human Resources/Reporting/All Months/Timesheet by User
 * Human Resources/Reporting/All Months/Timesheet by Invoice
 * Human Resources/Reporting/This Month/My timesheets to invoice
 * Human Resources/Reporting/All Months/Daily Timesheet by Account
 * Human Resources/Reporting/This Month/My daily timesheets by account
 * Human Resources/Reporting/All Months/Timesheet by Account
 * Human Resources/Reporting/This Month/My timesheets by account

Views
-----

 * report_timesheet.user.graph (graph)
 * report_timesheet.timesheet.user.form (form)
 * report_timesheet.timesheet.user.tree (tree)
 * report_timesheet.account.date.graph (graph)
 * report_timesheet.invoice.graph (graph)
 * report_timesheet.timesheet.invoice.form (form)
 * report_timesheet.timesheet.invoice.tree (tree)
 * report_timesheet.account.date.tree (tree)
 * report_timesheet.account.date.graph (graph)
 * report_timesheet.timesheet.account.date.form (form)
 * report_timesheet.account.tree (tree)
 * report_timesheet.account.graph (graph)
 * report_timesheet.timesheet.account.form (form)
 * report.random.timesheet.tree (tree)
 * random.timesheet.lines.tree (tree)


Objects
-------

Object: Timesheet per day (report_timesheet.user)
#################################################



:cost: Cost, float, readonly





:user_id: User, many2one, readonly





:name: Date, date, readonly





:quantity: Quantity, float, readonly




Object: Timesheet per account (report_timesheet.account)
########################################################



:quantity: Quantity, float, readonly





:user_id: User, many2one, readonly





:name: Month, date, readonly





:account_id: Analytic Account, many2one, readonly




Object: Daily timesheet per account (report_timesheet.account.date)
###################################################################



:quantity: Quantity, float, readonly





:user_id: User, many2one, readonly





:name: Date, date, readonly





:account_id: Analytic Account, many2one, readonly




Object: Costs to invoice (report_timesheet.invoice)
###################################################



:amount_invoice: To invoice, float, readonly





:quantity: Quantity, float, readonly





:user_id: User, many2one, readonly





:manager_id: Manager, many2one, readonly





:account_id: Project, many2one, readonly




Object: Random Timesheet Report (report.random.timesheet)
#########################################################



:analytic_account_id: Analytic Account, many2one, readonly





:date: Date, date, readonly





:user_id: User, many2one, readonly





:name: Description, char, readonly





:quantity: Quantity, float, readonly




Object: Random Timesheet Lines (random.timesheet.lines)
#######################################################



:analytic_account_id: Analytic Account, many2one, readonly





:user_id: User, many2one, readonly





:product_id: Product, many2one, readonly





:general_account_id: General Account, many2one, readonly





:uom_id: UoM, many2one, readonly





:name: Description, char, readonly





:to_invoice: Invoicing, many2one, readonly





:amount: Amount, float, readonly





:date: Date, date, readonly





:quantity: Quantity, float, readonly


