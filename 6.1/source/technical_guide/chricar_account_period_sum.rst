
.. module:: chricar_account_period_sum
    :synopsis: Account Period Sum 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/chricar_account_period_sum"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Account Period Sum (*chricar_account_period_sum*)
=================================================
:Module: chricar_account_period_sum
:Name: Account Period Sum
:Version: 5.0.0.9.5
:Author: ChriCar Beteiligungs und Beratungs GmbH
:Directory: chricar_account_period_sum
:Web: http://www.chricar.at/ChriCar
:Official module: no
:Quality certified: no

Description
-----------

::

  This module adds period sums for moves_lines
          of account_moves with state posted
          *) on update from draft to posted
             hence: account_move_lines must NOT be added to account_moves with state posted.
          *) balance carried forward is calculated for all subsequent fiscal years
             no account_move_lines are generated for these sums
             these sums always represent the balance of the preceding fiscal year.
          *) on creation of new fiscal years -> balance carried forward
          *) on change of deferral_method in general accounts
             it's subject to another check if and when changes of this field are allowed.
             IMHO not if at least one fiscal year is closed.
          *) the name of fiscal years not ending on Dec 31st is year-period (YYYY-MM) of the end of the fiscal year
          *) for every fiscal year beginning in the same calendar year a period sum with the name YYYY00 will be created,
             but associated to the correct fiscal year.
          *) the period sums will be deleted if the matching account_periods are deleted.
  
      standardizes account_period name generation to comply with this naming.
  
      In respect of functionality of the sums it's feature complete but must be tested
  
      Things to come:
      * eventually - adapting the accounting reporting to use this sums (2c2?)

Download links
--------------

You can download this module as a zip file in the following version:

(No download links available)


Dependencies
------------

 * :mod:`base`
 * :mod:`account`
 * :mod:`chricar_view_id`

Reports
-------

None


Menus
-------

 * Financial Management/Charts/Accounts with Postings

Views
-----

 * account.account_with_postings.tree_chricar_1 (tree)
 * account.account_with_postings.form_chricar_1 (form)


Objects
-------

Object: Account Period Sum (account.account_period_sum)
#######################################################



:name: Period, char





:sum_fy_period_id: Account FY id, integer, required, readonly





:credit: Credit, float, required, readonly





:period_id: Period, many2one, required, readonly





:debit: Debit, float, required, readonly





:account_id: Account, many2one, required, readonly




Object: Account Fiscalyear Period Sum (account.account_fy_period_sum)
#####################################################################



:date_stop: Date Stop, date, readonly





:name: Period, char, readonly





:sum_fy_period_id: Account FY id, integer, readonly





:date_start: Date Start, date, readonly





:credit: Credit, float, readonly





:move_line_ids: Account_moves, one2many





:period_id: Period, many2one, readonly





:debit: Debit, float, readonly





:balance: Balance, float, readonly





:account_id: Account, many2one, readonly




Object: Account Fiscalyear Sum (account.account_fiscalyear_sum)
###############################################################



:date_stop: Date Stop, date, readonly





:account_id: Account, many2one, readonly





:sum_fy_period_ids: Fiscal Year Period Sum, one2many





:date_start: Date Start, date, readonly





:credit: Credit, float, readonly





:fiscalyear_id: Fiscal Year, many2one, readonly





:debit: Debit, float, readonly





:balance: Balance, float, readonly





:name: Fiscal Year, char, readonly




Object: Accounts with Postings (account.account_with_postings)
##############################################################



:code: Code, char, readonly





:name: Name, char, readonly





:sum_fy_period_ids: Sum Fiscal Year Periods, one2many





:sum_period_ids: Sum Periods, one2many





:shortcut: Shortcut, char, readonly





:sum_fiscalyear_ids: Sum Fiscal Years, one2many





:type: Account Type, selection, readonly




Object: triggger (triggger)
###########################
