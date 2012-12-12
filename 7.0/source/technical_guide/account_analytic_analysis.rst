
.. module:: account_analytic_analysis
    :synopsis: report_account_analytic (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_analytic_analysis"></div>
    <script src="http://js-kit.com/ratings.js"></script>

report_account_analytic (*account_analytic_analysis*)
=====================================================
:Module: account_analytic_analysis
:Name: report_account_analytic
:Version: 5.0.1.1
:Author: Camptocamp
:Directory: account_analytic_analysis
:Web: http://www.camptocamp.com/
:Official module: yes
:Quality certified: yes

Description
-----------

::

  Modify account analytic view to show
  important data for project manager of services companies.
  Add menu to show relevant information for each manager.

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/account_analytic_analysis.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/account_analytic_analysis.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/account_analytic_analysis.zip>`_


Dependencies
------------

 * :mod:`account`
 * :mod:`hr_timesheet`
 * :mod:`hr_timesheet_invoice`
 * :mod:`project`

Reports
-------

None


Menus
-------

 * Project Management/Financial Project Management
 * Project Management/Financial Project Management/Analytic Accounts
 * Project Management/Financial Project Management/Invoicing
 * Project Management/Financial Project Management/Analytic Accounts/My Accounts
 * Project Management/Financial Project Management/Invoicing/All Uninvoiced Entries
 * Project Management/Financial Project Management/Invoicing/My Uninvoiced Entries
 * Project Management/Financial Project Management/Analytic Accounts/My Accounts/My Current Accounts
 * Project Management/Financial Project Management/Analytic Accounts/My Accounts/My Pending Accounts
 * Project Management/Financial Project Management/Analytic Accounts/New Analytic Account
 * Project Management/Financial Project Management/Analytic Accounts/All Analytic Accounts
 * Project Management/Financial Project Management/Invoicing/Overpassed Accounts
 * Project Management/Financial Project Management/Analytic Accounts/All Analytic Accounts/Current Analytic Accounts
 * Project Management/Financial Project Management/Analytic Accounts/All Analytic Accounts/Pending Analytic Accounts

Views
-----

 * \* INHERIT account.analytic.account.tree (tree)
 * \* INHERIT account.analytic.account.tree (tree)
 * account.analytic.account.simplified.tree (tree)


Objects
-------

Object: Hours summary by user (account_analytic_analysis.summary.user)
######################################################################



:account_id: Analytic Account, many2one, readonly





:unit_amount: Total Time, float, readonly





:user: User, many2one




Object: Hours summary by month (account_analytic_analysis.summary.month)
########################################################################



:account_id: Analytic Account, many2one, readonly





:unit_amount: Total Time, float, readonly





:month: Month, char, readonly


