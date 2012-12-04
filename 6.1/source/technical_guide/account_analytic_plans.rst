
.. module:: account_analytic_plans
    :synopsis: Multiple-plans management in Analytic Accounting (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_analytic_plans"></div>
    <script src="http://js-kit.com/ratings.js"></script>

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

Description
-----------

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

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/account_analytic_plans.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/account_analytic_plans.zip>`_


Dependencies
------------

 * :mod:`account`
 * :mod:`account_analytic_default`

Reports
-------

 * Crossovered Analytic

Menus
-------

 * Financial Management/Configuration/Analytic Accounting/Analytic Journal Definition/Analytic Distribution's models
 * Financial Management/Configuration/Analytic Accounting/Analytic Accounts/Analytic Plan

Views
-----

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


Objects
-------

Object: Analytic Plans (account.analytic.plan)
##############################################



:plan_ids: Analytic Plans, one2many





:name: Analytic Plan, char, required





:default_instance_id: Default Entries, many2one




Object: Analytic Plan Lines (account.analytic.plan.line)
########################################################



:min_required: Minimum Allowed (%), float





:plan_id: Analytic Plan, many2one





:name: Plan Name, char, required





:max_required: Maximum Allowed (%), float





:sequence: Sequence, integer





:root_analytic_id: Root Account, many2one, required

    *Root account of this plan.*


Object: Analytic Plan Instance (account.analytic.plan.instance)
###############################################################



:account5_ids: Account5 Id, one2many





:code: Distribution Code, char





:plan_id: Model's Plan, many2one





:name: Analytic Distribution, char





:account3_ids: Account3 Id, one2many





:journal_id: Analytic Journal, many2one, required





:account6_ids: Account6 Id, one2many





:account_ids: Account Id, one2many





:account4_ids: Account4 Id, one2many





:account2_ids: Account2 Id, one2many





:account1_ids: Account1 Id, one2many




Object: Analytic Instance Line (account.analytic.plan.instance.line)
####################################################################



:analytic_account_id: Analytic Account, many2one, required





:rate: Rate (%), float, required





:plan_id: Plan Id, many2one


