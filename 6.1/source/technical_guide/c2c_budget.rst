
.. module:: c2c_budget
    :synopsis: Advanced Budget 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/c2c_budget"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Advanced Budget (*c2c_budget*)
==============================
:Module: c2c_budget
:Name: Advanced Budget
:Version: 5.0.5.0
:Author: Camptocamp SA (aw)
:Directory: c2c_budget
:Web: http://camptocamp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Budget Module:
      * Create budget, budget items and budget versions.
      * Base your budget on analytics accounts
      * Budget versions are multi currencies and multi companies.
  
      This module is for advanced budget use, if the additional functionality is not needed it is best to use the standard modules.

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/c2c_budget.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/c2c_budget.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/c2c_budget.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`account`
 * :mod:`c2c_reporting_tools`

Reports
-------

None


Menus
-------

 * Financial Management/Budgets
 * Financial Management/Budgets/Budgets
 * Financial Management/Budgets/Budgets Versions
 * Financial Management/Budgets/Budgets Lines
 * Financial Management/Budgets/Budgets Items
 * Financial Management/Budgets/Budgets Structures
 * Financial Management/Budgets/Budget Lines Search

Views
-----

 * c2c_budget.form (form)
 * c2c_budget.version.form (form)
 * c2c_budget.item.form (form)
 * c2c_budget.list (tree)
 * c2c_budget.version.list (tree)
 * c2c_budget.version.list (tree)
 * c2c_budget.item.list (tree)
 * c2c_budget.item.tree (tree)
 * c2c_budget.line.list.in.budget.version (tree)
 * c2c_budget.line.list (tree)
 * c2c_budget.line.list (form)
 * c2c_budget.analytic_line.list (tree)


Objects
-------

Object: Budget items (c2c_budget.item)
######################################



:children_ids: Children Items, one2many





:code: Code, char, required





:name: Name, char, required





:sequence: Sequence, integer





:calculation: Calculation, text





:style: Style, selection, required





:note: Notes, text





:parent_id: Parent Item, many2one





:active: Active, boolean





:account: Financial Account, many2many





:type: Type, selection, required




Object: Budget (c2c_budget)
###########################



:code: Code, char





:create_date: Creation Date, datetime, readonly





:name: Name, char, required





:end_date: End Date, date, required





:note: Notes, text





:budget_item_id: Budget Structure, many2one, required





:budget_version_ids: Budget Versions, one2many, readonly





:active: Active, boolean





:start_date: Start Date, date, required




Object: Budget versions (c2c_budget.version)
############################################



:currency_id: Currency, many2one, required





:code: Code, char





:create_date: Creation Date, datetime, readonly





:name: Version Name, char, required





:budget_line_ids: Budget Lines, one2many





:company_id: Company, many2one, required





:ref_date: Reference Date, date, required





:note: Notes, text





:budget_id: Budget, many2one, required





:user_id: User In Charge, many2one




Object: Budget Lines (c2c_budget.line)
######################################



:analytic_account_id: Analytic Account, many2one





:budget_version_id: Budget Version, many2one, required





:name: Description, char





:amount_in_budget_currency: In Budget's Currency, float, readonly





:currency_id: Currency, many2one, required





:amount: Amount, float, required





:budget_item_id: Budget Item, many2one, required





:period_id: Period, many2one, required




Object: Wizard Abstraction (c2c_budget.wizard_abstraction)
##########################################################


Object: Report Abstraction (c2c_budget.report_abstraction)
##########################################################
