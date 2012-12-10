
.. i18n: .. module:: c2c_budget
.. i18n:     :synopsis: Advanced Budget 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: c2c_budget
    :synopsis: Advanced Budget 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/c2c_budget"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/c2c_budget"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Advanced Budget (*c2c_budget*)
.. i18n: ==============================
.. i18n: :Module: c2c_budget
.. i18n: :Name: Advanced Budget
.. i18n: :Version: 5.0.5.0
.. i18n: :Author: Camptocamp SA (aw)
.. i18n: :Directory: c2c_budget
.. i18n: :Web: http://camptocamp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Budget Module:
.. i18n:       * Create budget, budget items and budget versions.
.. i18n:       * Base your budget on analytics accounts
.. i18n:       * Budget versions are multi currencies and multi companies.
.. i18n:   
.. i18n:       This module is for advanced budget use, if the additional functionality is not needed it is best to use the standard modules.
..

::

  Budget Module:
      * Create budget, budget items and budget versions.
      * Base your budget on analytics accounts
      * Budget versions are multi currencies and multi companies.
  
      This module is for advanced budget use, if the additional functionality is not needed it is best to use the standard modules.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/c2c_budget.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/c2c_budget.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/c2c_budget.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/c2c_budget.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/c2c_budget.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/c2c_budget.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`account`
.. i18n:  * :mod:`c2c_reporting_tools`
..

 * :mod:`base`
 * :mod:`account`
 * :mod:`c2c_reporting_tools`

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

.. i18n:  * Financial Management/Budgets
.. i18n:  * Financial Management/Budgets/Budgets
.. i18n:  * Financial Management/Budgets/Budgets Versions
.. i18n:  * Financial Management/Budgets/Budgets Lines
.. i18n:  * Financial Management/Budgets/Budgets Items
.. i18n:  * Financial Management/Budgets/Budgets Structures
.. i18n:  * Financial Management/Budgets/Budget Lines Search
..

 * Financial Management/Budgets
 * Financial Management/Budgets/Budgets
 * Financial Management/Budgets/Budgets Versions
 * Financial Management/Budgets/Budgets Lines
 * Financial Management/Budgets/Budgets Items
 * Financial Management/Budgets/Budgets Structures
 * Financial Management/Budgets/Budget Lines Search

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * c2c_budget.form (form)
.. i18n:  * c2c_budget.version.form (form)
.. i18n:  * c2c_budget.item.form (form)
.. i18n:  * c2c_budget.list (tree)
.. i18n:  * c2c_budget.version.list (tree)
.. i18n:  * c2c_budget.version.list (tree)
.. i18n:  * c2c_budget.item.list (tree)
.. i18n:  * c2c_budget.item.tree (tree)
.. i18n:  * c2c_budget.line.list.in.budget.version (tree)
.. i18n:  * c2c_budget.line.list (tree)
.. i18n:  * c2c_budget.line.list (form)
.. i18n:  * c2c_budget.analytic_line.list (tree)
..

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

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Budget items (c2c_budget.item)
.. i18n: ######################################
..

Object: Budget items (c2c_budget.item)
######################################

.. i18n: :children_ids: Children Items, one2many
..

:children_ids: Children Items, one2many

.. i18n: :code: Code, char, required
..

:code: Code, char, required

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :sequence: Sequence, integer
..

:sequence: Sequence, integer

.. i18n: :calculation: Calculation, text
..

:calculation: Calculation, text

.. i18n: :style: Style, selection, required
..

:style: Style, selection, required

.. i18n: :note: Notes, text
..

:note: Notes, text

.. i18n: :parent_id: Parent Item, many2one
..

:parent_id: Parent Item, many2one

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :account: Financial Account, many2many
..

:account: Financial Account, many2many

.. i18n: :type: Type, selection, required
..

:type: Type, selection, required

.. i18n: Object: Budget (c2c_budget)
.. i18n: ###########################
..

Object: Budget (c2c_budget)
###########################

.. i18n: :code: Code, char
..

:code: Code, char

.. i18n: :create_date: Creation Date, datetime, readonly
..

:create_date: Creation Date, datetime, readonly

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :end_date: End Date, date, required
..

:end_date: End Date, date, required

.. i18n: :note: Notes, text
..

:note: Notes, text

.. i18n: :budget_item_id: Budget Structure, many2one, required
..

:budget_item_id: Budget Structure, many2one, required

.. i18n: :budget_version_ids: Budget Versions, one2many, readonly
..

:budget_version_ids: Budget Versions, one2many, readonly

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :start_date: Start Date, date, required
..

:start_date: Start Date, date, required

.. i18n: Object: Budget versions (c2c_budget.version)
.. i18n: ############################################
..

Object: Budget versions (c2c_budget.version)
############################################

.. i18n: :currency_id: Currency, many2one, required
..

:currency_id: Currency, many2one, required

.. i18n: :code: Code, char
..

:code: Code, char

.. i18n: :create_date: Creation Date, datetime, readonly
..

:create_date: Creation Date, datetime, readonly

.. i18n: :name: Version Name, char, required
..

:name: Version Name, char, required

.. i18n: :budget_line_ids: Budget Lines, one2many
..

:budget_line_ids: Budget Lines, one2many

.. i18n: :company_id: Company, many2one, required
..

:company_id: Company, many2one, required

.. i18n: :ref_date: Reference Date, date, required
..

:ref_date: Reference Date, date, required

.. i18n: :note: Notes, text
..

:note: Notes, text

.. i18n: :budget_id: Budget, many2one, required
..

:budget_id: Budget, many2one, required

.. i18n: :user_id: User In Charge, many2one
..

:user_id: User In Charge, many2one

.. i18n: Object: Budget Lines (c2c_budget.line)
.. i18n: ######################################
..

Object: Budget Lines (c2c_budget.line)
######################################

.. i18n: :analytic_account_id: Analytic Account, many2one
..

:analytic_account_id: Analytic Account, many2one

.. i18n: :budget_version_id: Budget Version, many2one, required
..

:budget_version_id: Budget Version, many2one, required

.. i18n: :name: Description, char
..

:name: Description, char

.. i18n: :amount_in_budget_currency: In Budget's Currency, float, readonly
..

:amount_in_budget_currency: In Budget's Currency, float, readonly

.. i18n: :currency_id: Currency, many2one, required
..

:currency_id: Currency, many2one, required

.. i18n: :amount: Amount, float, required
..

:amount: Amount, float, required

.. i18n: :budget_item_id: Budget Item, many2one, required
..

:budget_item_id: Budget Item, many2one, required

.. i18n: :period_id: Period, many2one, required
..

:period_id: Period, many2one, required

.. i18n: Object: Wizard Abstraction (c2c_budget.wizard_abstraction)
.. i18n: ##########################################################
..

Object: Wizard Abstraction (c2c_budget.wizard_abstraction)
##########################################################

.. i18n: Object: Report Abstraction (c2c_budget.report_abstraction)
.. i18n: ##########################################################
..

Object: Report Abstraction (c2c_budget.report_abstraction)
##########################################################
