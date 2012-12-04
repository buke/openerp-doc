
.. module:: analytic_journal_billing_rate
    :synopsis: Analytic Journal Billing Rate (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/analytic_journal_billing_rate"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Analytic Journal Billing Rate (*analytic_journal_billing_rate*)
===============================================================
:Module: analytic_journal_billing_rate
:Name: Analytic Journal Billing Rate
:Version: 5.0.1.0
:Author: Tiny
:Directory: analytic_journal_billing_rate
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  This module allows you to define what is the default invoicing rate for a specific journal on a given account. This is mostly used when a user encode his timesheet: the values are retrieved and the fields are auto-filled... but the possibility to change these values is still available.
  
      Obviously if no data has been recorded for the current account, the default value is given as usual by the account data so that this module is perfectly compatible with older configurations.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/analytic_journal_billing_rate.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/analytic_journal_billing_rate.zip>`_


Dependencies
------------

 * :mod:`analytic_user_function`
 * :mod:`account`
 * :mod:`hr_timesheet_invoice`

Reports
-------

None


Menus
-------


None


Views
-----

 * analytic_journal_rate_grid.tree (tree)
 * analytic_journal_rate_grid.form (form)
 * \* INHERIT account.analytic.account.form (form)
 * \* INHERIT hr.timesheet.sheet.form (form)
 * \* INHERIT hr.analytic.timesheet.form (form)
 * \* INHERIT hr.analytic.timesheet.form (form)


Objects
-------

Object: Relation table between journals and billing rates (analytic_journal_rate_grid)
######################################################################################



:rate_id: Invoicing Rate, many2one





:journal_id: Analytic Journal, many2one, required





:account_id: Analytic Account, many2one, required


