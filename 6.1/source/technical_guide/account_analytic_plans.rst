
.. i18n: .. module:: account_analytic_plans
.. i18n:     :synopsis: Multiple-plans management in Analytic Accounting (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: account_analytic_plans
    :synopsis: Multiple-plans management in Analytic Accounting (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_analytic_plans"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_analytic_plans"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Multiple-plans management in Analytic Accounting (*account_analytic_plans*)
.. i18n: ===========================================================================
.. i18n: :Module: account_analytic_plans
.. i18n: :Name: Multiple-plans management in Analytic Accounting
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: account_analytic_plans
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

Multiple-plans management in Analytic Accounting (*account_analytic_plans*)
===========================================================================
:Module: account_analytic_plans
:Name: Multiple-plans management in Analytic Accounting
:Version: 5.0.1.0
:Author: Tiny
:Directory: account_analytic_plans
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module allows to use several analytic plans, according to the general journal,
.. i18n:   so that multiple analytic lines are created when the invoice or the entries
.. i18n:   are confirmed.
.. i18n:   
.. i18n:   For example, you can define the following analytic structure:
.. i18n:     Projects
.. i18n:         Project 1
.. i18n:             SubProj 1.1
.. i18n:             SubProj 1.2
.. i18n:         Project 2
.. i18n:     Salesman
.. i18n:         Eric
.. i18n:         Fabien
.. i18n:   
.. i18n:   Here, we have two plans: Projects and Salesman. An invoice line must
.. i18n:   be able to write analytic entries in the 2 plans: SubProj 1.1 and
.. i18n:   Fabien. The amount can also be split. The following example is for
.. i18n:   an invoice that touches the two subproject and assigned to one salesman:
.. i18n:   
.. i18n:   Plan1:
.. i18n:       SubProject 1.1 : 50%
.. i18n:       SubProject 1.2 : 50%
.. i18n:   Plan2:
.. i18n:       Eric: 100%
.. i18n:   
.. i18n:   So when this line of invoice will be confirmed, it will generate 3 analytic lines,
.. i18n:   for one account entry.
..

::

  This module allows to use several analytic plans, according to the general journal,
  so that multiple analytic lines are created when the invoice or the entries
  are confirmed.
  
  For example, you can define the following analytic structure:
    Projects
        Project 1
            SubProj 1.1
            SubProj 1.2
        Project 2
    Salesman
        Eric
        Fabien
  
  Here, we have two plans: Projects and Salesman. An invoice line must
  be able to write analytic entries in the 2 plans: SubProj 1.1 and
  Fabien. The amount can also be split. The following example is for
  an invoice that touches the two subproject and assigned to one salesman:
  
  Plan1:
      SubProject 1.1 : 50%
      SubProject 1.2 : 50%
  Plan2:
      Eric: 100%
  
  So when this line of invoice will be confirmed, it will generate 3 analytic lines,
  for one account entry.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/account_analytic_plans.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/account_analytic_plans.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/account_analytic_plans.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/account_analytic_plans.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`account`
.. i18n:  * :mod:`account_analytic_default`
..

 * :mod:`account`
 * :mod:`account_analytic_default`

.. i18n: Reports
.. i18n: -------
..

Reports
-------

.. i18n:  * Crossovered Analytic
..

 * Crossovered Analytic

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Financial Management/Configuration/Analytic Accounting/Analytic Journal Definition/Analytic Distribution's models
.. i18n:  * Financial Management/Configuration/Analytic Accounting/Analytic Accounts/Analytic Plan
..

 * Financial Management/Configuration/Analytic Accounting/Analytic Journal Definition/Analytic Distribution's models
 * Financial Management/Configuration/Analytic Accounting/Analytic Accounts/Analytic Plan

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT account.journal.form.inherit (form)
.. i18n:  * \* INHERIT account.move.form.inherit (form)
.. i18n:  * \* INHERIT account.move.line.form.inherit (form)
.. i18n:  * \* INHERIT account.invoice.line.form.inherit (form)
.. i18n:  * \* INHERIT account.invoice.supplier.form.inherit (form)
.. i18n:  * account.analytic.plan.instance.form (form)
.. i18n:  * account.analytic.plan.instance.tree (tree)
.. i18n:  * account.analytic.plan.instance.line.form (form)
.. i18n:  * account.analytic.plan.instance.line.tree (tree)
.. i18n:  * account.analytic.plan.form (form)
.. i18n:  * account.analytic.plan.tree (tree)
.. i18n:  * account.analytic.plan.line.form (form)
.. i18n:  * account.analytic.plan.line.tree (tree)
.. i18n:  * \* INHERIT account.analytic.default.form.plans (form)
.. i18n:  * \* INHERIT account.analytic.default.tree.plans (tree)
..

 * \* INHERIT account.journal.form.inherit (form)
 * \* INHERIT account.move.form.inherit (form)
 * \* INHERIT account.move.line.form.inherit (form)
 * \* INHERIT account.invoice.line.form.inherit (form)
 * \* INHERIT account.invoice.supplier.form.inherit (form)
 * account.analytic.plan.instance.form (form)
 * account.analytic.plan.instance.tree (tree)
 * account.analytic.plan.instance.line.form (form)
 * account.analytic.plan.instance.line.tree (tree)
 * account.analytic.plan.form (form)
 * account.analytic.plan.tree (tree)
 * account.analytic.plan.line.form (form)
 * account.analytic.plan.line.tree (tree)
 * \* INHERIT account.analytic.default.form.plans (form)
 * \* INHERIT account.analytic.default.tree.plans (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Analytic Plans (account.analytic.plan)
.. i18n: ##############################################
..

Object: Analytic Plans (account.analytic.plan)
##############################################

.. i18n: :plan_ids: Analytic Plans, one2many
..

:plan_ids: Analytic Plans, one2many

.. i18n: :name: Analytic Plan, char, required
..

:name: Analytic Plan, char, required

.. i18n: :default_instance_id: Default Entries, many2one
..

:default_instance_id: Default Entries, many2one

.. i18n: Object: Analytic Plan Lines (account.analytic.plan.line)
.. i18n: ########################################################
..

Object: Analytic Plan Lines (account.analytic.plan.line)
########################################################

.. i18n: :min_required: Minimum Allowed (%), float
..

:min_required: Minimum Allowed (%), float

.. i18n: :plan_id: Analytic Plan, many2one
..

:plan_id: Analytic Plan, many2one

.. i18n: :name: Plan Name, char, required
..

:name: Plan Name, char, required

.. i18n: :max_required: Maximum Allowed (%), float
..

:max_required: Maximum Allowed (%), float

.. i18n: :sequence: Sequence, integer
..

:sequence: Sequence, integer

.. i18n: :root_analytic_id: Root Account, many2one, required
..

:root_analytic_id: Root Account, many2one, required

.. i18n:     *Root account of this plan.*
..

    *Root account of this plan.*

.. i18n: Object: Analytic Plan Instance (account.analytic.plan.instance)
.. i18n: ###############################################################
..

Object: Analytic Plan Instance (account.analytic.plan.instance)
###############################################################

.. i18n: :account5_ids: Account5 Id, one2many
..

:account5_ids: Account5 Id, one2many

.. i18n: :code: Distribution Code, char
..

:code: Distribution Code, char

.. i18n: :plan_id: Model's Plan, many2one
..

:plan_id: Model's Plan, many2one

.. i18n: :name: Analytic Distribution, char
..

:name: Analytic Distribution, char

.. i18n: :account3_ids: Account3 Id, one2many
..

:account3_ids: Account3 Id, one2many

.. i18n: :journal_id: Analytic Journal, many2one, required
..

:journal_id: Analytic Journal, many2one, required

.. i18n: :account6_ids: Account6 Id, one2many
..

:account6_ids: Account6 Id, one2many

.. i18n: :account_ids: Account Id, one2many
..

:account_ids: Account Id, one2many

.. i18n: :account4_ids: Account4 Id, one2many
..

:account4_ids: Account4 Id, one2many

.. i18n: :account2_ids: Account2 Id, one2many
..

:account2_ids: Account2 Id, one2many

.. i18n: :account1_ids: Account1 Id, one2many
..

:account1_ids: Account1 Id, one2many

.. i18n: Object: Analytic Instance Line (account.analytic.plan.instance.line)
.. i18n: ####################################################################
..

Object: Analytic Instance Line (account.analytic.plan.instance.line)
####################################################################

.. i18n: :analytic_account_id: Analytic Account, many2one, required
..

:analytic_account_id: Analytic Account, many2one, required

.. i18n: :rate: Rate (%), float, required
..

:rate: Rate (%), float, required

.. i18n: :plan_id: Plan Id, many2one
..

:plan_id: Plan Id, many2one
