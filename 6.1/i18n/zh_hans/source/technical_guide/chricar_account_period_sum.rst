
.. i18n: .. module:: chricar_account_period_sum
.. i18n:     :synopsis: Account Period Sum 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: chricar_account_period_sum
    :synopsis: Account Period Sum 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/chricar_account_period_sum"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/chricar_account_period_sum"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Account Period Sum (*chricar_account_period_sum*)
.. i18n: =================================================
.. i18n: :Module: chricar_account_period_sum
.. i18n: :Name: Account Period Sum
.. i18n: :Version: 5.0.0.9.5
.. i18n: :Author: ChriCar Beteiligungs und Beratungs GmbH
.. i18n: :Directory: chricar_account_period_sum
.. i18n: :Web: http://www.chricar.at/ChriCar
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module adds period sums for moves_lines
.. i18n:           of account_moves with state posted
.. i18n:           *) on update from draft to posted
.. i18n:              hence: account_move_lines must NOT be added to account_moves with state posted.
.. i18n:           *) balance carried forward is calculated for all subsequent fiscal years
.. i18n:              no account_move_lines are generated for these sums
.. i18n:              these sums always represent the balance of the preceding fiscal year.
.. i18n:           *) on creation of new fiscal years -> balance carried forward
.. i18n:           *) on change of deferral_method in general accounts
.. i18n:              it's subject to another check if and when changes of this field are allowed.
.. i18n:              IMHO not if at least one fiscal year is closed.
.. i18n:           *) the name of fiscal years not ending on Dec 31st is year-period (YYYY-MM) of the end of the fiscal year
.. i18n:           *) for every fiscal year beginning in the same calendar year a period sum with the name YYYY00 will be created,
.. i18n:              but associated to the correct fiscal year.
.. i18n:           *) the period sums will be deleted if the matching account_periods are deleted.
.. i18n:   
.. i18n:       standardizes account_period name generation to comply with this naming.
.. i18n:   
.. i18n:       In respect of functionality of the sums it's feature complete but must be tested
.. i18n:   
.. i18n:       Things to come:
.. i18n:       * eventually - adapting the accounting reporting to use this sums (2c2?)
..

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

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n: (No download links available)
..

(No download links available)

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`account`
.. i18n:  * :mod:`chricar_view_id`
..

 * :mod:`base`
 * :mod:`account`
 * :mod:`chricar_view_id`

.. i18n: Reports
.. i18n: -------
..

Reports
-------

.. i18n: None
..

None

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Financial Management/Charts/Accounts with Postings
..

 * Financial Management/Charts/Accounts with Postings

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * account.account_with_postings.tree_chricar_1 (tree)
.. i18n:  * account.account_with_postings.form_chricar_1 (form)
..

 * account.account_with_postings.tree_chricar_1 (tree)
 * account.account_with_postings.form_chricar_1 (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Account Period Sum (account.account_period_sum)
.. i18n: #######################################################
..

Object: Account Period Sum (account.account_period_sum)
#######################################################

.. i18n: :name: Period, char
..

:name: Period, char

.. i18n: :sum_fy_period_id: Account FY id, integer, required, readonly
..

:sum_fy_period_id: Account FY id, integer, required, readonly

.. i18n: :credit: Credit, float, required, readonly
..

:credit: Credit, float, required, readonly

.. i18n: :period_id: Period, many2one, required, readonly
..

:period_id: Period, many2one, required, readonly

.. i18n: :debit: Debit, float, required, readonly
..

:debit: Debit, float, required, readonly

.. i18n: :account_id: Account, many2one, required, readonly
..

:account_id: Account, many2one, required, readonly

.. i18n: Object: Account Fiscalyear Period Sum (account.account_fy_period_sum)
.. i18n: #####################################################################
..

Object: Account Fiscalyear Period Sum (account.account_fy_period_sum)
#####################################################################

.. i18n: :date_stop: Date Stop, date, readonly
..

:date_stop: Date Stop, date, readonly

.. i18n: :name: Period, char, readonly
..

:name: Period, char, readonly

.. i18n: :sum_fy_period_id: Account FY id, integer, readonly
..

:sum_fy_period_id: Account FY id, integer, readonly

.. i18n: :date_start: Date Start, date, readonly
..

:date_start: Date Start, date, readonly

.. i18n: :credit: Credit, float, readonly
..

:credit: Credit, float, readonly

.. i18n: :move_line_ids: Account_moves, one2many
..

:move_line_ids: Account_moves, one2many

.. i18n: :period_id: Period, many2one, readonly
..

:period_id: Period, many2one, readonly

.. i18n: :debit: Debit, float, readonly
..

:debit: Debit, float, readonly

.. i18n: :balance: Balance, float, readonly
..

:balance: Balance, float, readonly

.. i18n: :account_id: Account, many2one, readonly
..

:account_id: Account, many2one, readonly

.. i18n: Object: Account Fiscalyear Sum (account.account_fiscalyear_sum)
.. i18n: ###############################################################
..

Object: Account Fiscalyear Sum (account.account_fiscalyear_sum)
###############################################################

.. i18n: :date_stop: Date Stop, date, readonly
..

:date_stop: Date Stop, date, readonly

.. i18n: :account_id: Account, many2one, readonly
..

:account_id: Account, many2one, readonly

.. i18n: :sum_fy_period_ids: Fiscal Year Period Sum, one2many
..

:sum_fy_period_ids: Fiscal Year Period Sum, one2many

.. i18n: :date_start: Date Start, date, readonly
..

:date_start: Date Start, date, readonly

.. i18n: :credit: Credit, float, readonly
..

:credit: Credit, float, readonly

.. i18n: :fiscalyear_id: Fiscal Year, many2one, readonly
..

:fiscalyear_id: Fiscal Year, many2one, readonly

.. i18n: :debit: Debit, float, readonly
..

:debit: Debit, float, readonly

.. i18n: :balance: Balance, float, readonly
..

:balance: Balance, float, readonly

.. i18n: :name: Fiscal Year, char, readonly
..

:name: Fiscal Year, char, readonly

.. i18n: Object: Accounts with Postings (account.account_with_postings)
.. i18n: ##############################################################
..

Object: Accounts with Postings (account.account_with_postings)
##############################################################

.. i18n: :code: Code, char, readonly
..

:code: Code, char, readonly

.. i18n: :name: Name, char, readonly
..

:name: Name, char, readonly

.. i18n: :sum_fy_period_ids: Sum Fiscal Year Periods, one2many
..

:sum_fy_period_ids: Sum Fiscal Year Periods, one2many

.. i18n: :sum_period_ids: Sum Periods, one2many
..

:sum_period_ids: Sum Periods, one2many

.. i18n: :shortcut: Shortcut, char, readonly
..

:shortcut: Shortcut, char, readonly

.. i18n: :sum_fiscalyear_ids: Sum Fiscal Years, one2many
..

:sum_fiscalyear_ids: Sum Fiscal Years, one2many

.. i18n: :type: Account Type, selection, readonly
..

:type: Account Type, selection, readonly

.. i18n: Object: triggger (triggger)
.. i18n: ###########################
..

Object: triggger (triggger)
###########################
