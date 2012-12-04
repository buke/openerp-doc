
.. module:: report_account
    :synopsis: Account Reporting - Reporting (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_account"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Account Reporting - Reporting (*report_account*)
================================================
:Module: report_account
:Name: Account Reporting - Reporting
:Version: 5.0.1.0
:Author: Tiny
:Directory: report_account
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  A module that adds new reports based on the account module.

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/report_account.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/report_account.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/report_account.zip>`_


Dependencies
------------

 * :mod:`account`

Reports
-------

None


Menus
-------

 * Financial Management/Reporting/Balance by Type of Account

Views
-----

 * report.account.receivable.graph (graph)
 * report.account.receivable.tree (tree)
 * report.account.receivable.form (form)
 * report.aged.receivable.graph (graph)
 * report.aged.receivable.tree (tree)
 * report.invoice.created.tree (tree)


Objects
-------

Object: Receivable accounts (report.account.receivable)
#######################################################



:credit: Credit, float, readonly





:balance: Balance, float, readonly





:type: Account Type, selection, required





:name: Week of Year, char, readonly





:debit: Debit, float, readonly




Object: A Temporary table used for Dashboard view (temp.range)
##############################################################



:name: Range, char




Object: Aged Receivable Till Today (report.aged.receivable)
###########################################################



:balance: Balance, float, readonly





:name: Month Range, char, readonly




Object: Report of Invoices Created within Last 15 days (report.invoice.created)
###############################################################################



:origin: Origin, char, readonly





:currency_id: Currency, many2one, readonly





:date_due: Due Date, date, readonly





:create_date: Create Date, datetime, readonly





:name: Description, char, readonly





:partner_id: Partner, many2one, readonly





:residual: Residual, float, readonly





:number: Invoice Number, char, readonly





:date_invoice: Date Invoiced, date, readonly





:state: State, selection, readonly





:amount_untaxed: Untaxed, float, readonly





:type: Type, selection, readonly





:amount_total: Total, float, readonly


