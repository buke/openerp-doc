
.. module:: profile_business_game
    :synopsis: Business Game (Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/profile_business_game"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Business Game (*profile_business_game*)
========================================
:Module: profile_business_game
:Name: Business Game
:Version: 5.0.1.0
:Author: Tiny
:Directory: profile_business_game
:Web: 
:Official module: no
:Quality certified: yes

Description
-----------

::

  This business game will help you to discover OpenERP and it's enterprise management processes.
  The game is based on a company called 'GoodSound' selling audio and video hardware and organising sonorisation events.
  
  The game is structured into two phases:
     1. You will discover the OpenERP interface through a complete sale flow: from the quotation to the invoice,
     2. The goal of the next phase is to make some strategic choices in the system to increase company's profitability
        within a few turns of one year each.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/profile_business_game.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/profile_business_game.zip>`_


Dependencies
------------

 * :mod:`board`
 * :mod:`base`
 * :mod:`account`
 * :mod:`game_scenario`
 * :mod:`purchase_approve`
 * :mod:`sale`
 * :mod:`sale_wo_production`
 * :mod:`stock_planning`
 * :mod:`crm_configuration`
 * :mod:`mrp_jit`
 * :mod:`l10n_fr`
 * :mod:`account_budget`
 * :mod:`sale_forecast`
 * :mod:`product_margin`

Reports
-------

None


Menus
-------

 * Dashboards/Business Game
 * Dashboards/Business Game/Business Game Scenario

Views
-----

 * bank.loan.wiz (form)
 * bank.loan.tree (tree)
 * profile.game.phase2.form (form)
 * profile.game.phase2.tree (tree)
 * Configuration of Business Game (form)
 * profile.game.phase1.form (form)
 * profile.game.phase1.tree (tree)
 * \* INHERIT account.budget.inherit (form)


Objects
-------

Object: profile.game.phase1 (profile.game.phase1)
#################################################



:step1_so_id: Quotation / Sale Order, many2one, readonly





:state: State, selection, required, readonly





:step10: Print Customer Invoice, boolean, readonly





:step7: Receive Products from Supplier, boolean, readonly





:step6: Confirm Request for Quotation, boolean, readonly





:step5: Change Supplier Price, boolean, readonly





:step4: Print Request for Quotation, boolean, readonly





:step3: Confirm Sale Order, boolean, readonly





:step2: Print Customer Quotation, boolean, readonly





:step1: Create Quotation, boolean, readonly





:step9: Confirm Draft Invoice, boolean, readonly





:step8: Deliver Products to Customer, boolean, readonly




Object: Bank Loan (bank.loan)
#############################



:reimburse_principle_amt_with_int: Reimburse amount [with Interest], float

    *Reimburse loan amount per month with interest*



:name: Name, char





:months_left: # of months left, float

    *Number of months left*



:fiscal_year: Fiscal Year, many2one, required, readonly

    *Year in which loan is taken*



:interest_per_month: Interest amount per month, float

    *Interest amount per month*



:rate: Interest Rate, float, readonly

    *Interest Rate*



:loan_duration: # of Years, float

    *Loan duration in years*



:reimburse_principle_amt_without_int: Reimburse amount[without Interest], float

    *Reimburse loan amount per month without interest*



:loan_amount: Loan Amount, float

    *Loan Amount*



:total_amount: Total Amount, float, readonly

    *Total Amount to be paid*


Object: profile.game.phase2 (profile.game.phase2)
#################################################



:logistic_user_id: Name of Logistic Manager, many2one, readonly





:loan_total_reimburse: Total to Reimburse, float, readonly

    *Total loan amount to reimburse*



:last_turnover: Turnover in last year, float, readonly

    *Turnover in last year*



:years: Number of Turns, selection





:last_total_sale: Total Sales in Last Year, float, readonly

    *Total Sales in Last Year*



:margin_forcast: Margin Forecast, float, readonly

    *Margin Forecast*



:turnover_growth: Turnover Growth, float, readonly

    *Turnover Growth*



:cy_traceback: Traceback [Current Year], text





:sales_user_id: Name of Sales Manager, many2one, readonly





:products_growth: Growth Products, float, readonly

    *Growth Products*



:objectives: Objectives, selection





:avg_stock_forcast: Avg. Stock Forecast, float, readonly

    *Avg. Stock Forecast*



:state: Number of Players, selection





:current_treasury: Current treasury, float, readonly

    *Balance of all Cash Accounts*



:last_total_purchase: Total Purchases in Last year, float, readonly

    *Total Purchases in Last year*



:warn_error: Warnings & Errors, text





:sale_forcast: Sales Forecast, float, readonly

    *Sales Forecast*



:total_reimburse: Total to Reimburse, float, readonly

    *Total to Reimburse*



:difficulty: Difficulty, selection





:loan_total_reimburse_this_year: Total to Reimburse this year, float, readonly

    *Total loan amount to reimburse this year*



:finance_user_id: Name of Financial Manager, many2one, readonly





:hr_user_id: Name of HR Manager, many2one, readonly





:name: Name, char





:cost_purchase_forcast: Costs of Purchases Forecast, float, readonly

    *Costs of Purchases Forecast*



:total_sold_products: # of Products Sold, float, readonly

    *# of Products Sold*



:hr_budget: HR Budget, float, readonly

    *HR Budget*



:total_benefit: Total Benefits, float, readonly

    *Total Benefits*



:benefits_growth: Benefits Growth, float, readonly

    *Benefits Growth*



:ay_traceback: Traceback [All Years], text




Object: profile.game.config.wizard (profile.game.config.wizard)
###############################################################



:logistic_email: Email of Logistic Manager, char





:sale_name: Name of Sales Manager, char, required





:sale_email: Email of Sales Manager, char





:logistic_name: Name of Logistic Manager, char, required





:objectives: Objectives, selection, required





:years: Number of Turns, selection, required





:difficulty: Difficulty, selection, required





:state: Number of Players, selection, required





:hr_email: Email of Human Resource Manager, char, readonly





:finance_name: Name of Financial Manager, char, required





:finance_email: Email of Financial Manager, char





:hr_name: Name of Human Resource Manager, char, readonly


