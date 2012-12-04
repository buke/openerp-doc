
.. module:: report_analytic_planning
    :synopsis: Analytic planning - Reporting (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_analytic_planning"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Analytic planning - Reporting (*report_analytic_planning*)
==========================================================
:Module: report_analytic_planning
:Name: Analytic planning - Reporting
:Version: 5.0.1.0
:Author: Tiny
:Directory: report_analytic_planning
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  Planning on analytic accounts.

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/report_analytic_planning.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/report_analytic_planning.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/report_analytic_planning.zip>`_


Dependencies
------------

 * :mod:`account`
 * :mod:`hr_timesheet_invoice`
 * :mod:`project`
 * :mod:`report_analytic_line`

Reports
-------

 * Planning

Menus
-------

 * Human Resources/Planning
 * Human Resources/Planning/Planning
 * Human Resources/Planning/My Planning
 * Human Resources/Planning/My Planning/My Current Planning
 * Human Resources/Planning/Planning/Current Planning
 * Human Resources/Planning/New Planning
 * Human Resources/Reporting/Planning
 * Human Resources/Reporting/Planning/Planning Statistics
 * Human Resources/Reporting/Planning/My Planning Statistics
 * Human Resources/Reporting/Planning/Planning Statistics of My Projects

Views
-----

 * report.account.analytic.planning.tree (tree)
 * report.account.analytic.planning.form (form)
 * report.account.analytic.planning.stat.form (form)
 * report.account.analytic.planning.stat.tree (tree)
 * report.account.analytic.planning.stat.graph (graph)


Objects
-------

Object: Planning (report_account_analytic.planning)
###################################################



:user_id: Responsible, many2one, required





:name: Planning Name, char, required





:date_from: Start Date, date, required





:line_ids: Planning lines, one2many





:stat_ids: Planning analysis, one2many, readonly





:state: Status, selection, required





:date_to: End Date, date, required





:stat_account_ids: Planning by account, one2many, readonly





:stat_user_ids: Planning by user, one2many, readonly




Object: Planning Line (report_account_analytic.planning.line)
#############################################################



:user_id: User, many2one





:account_id: Analytic account, many2one, required





:planning_id: Planning, many2one, required





:amount_unit: Qty UoM, many2one, required





:note: Note, text





:amount: Quantity, float, required




Object: Planning account stat (report_account_analytic.planning.stat.account)
#############################################################################



:sum_amount_real: Timesheet, float, readonly





:account_id: Analytic Account, many2one, required





:planning_id: Planning, many2one





:quantity: Planned, float, required




Object: Planning stat (report_account_analytic.planning.stat)
#############################################################



:user_id: User, many2one





:account_id: Account, many2one, required





:planning_id: Planning, many2one





:sum_amount_real: Timesheet, float, readonly





:sum_amount: Planned hours, float, required





:manager_id: Manager, many2one





:sum_amount_tasks: Tasks, float, readonly




Object: Planning user stat (report_account_analytic.planning.stat.user)
#######################################################################



:sum_amount_real: Timesheet, float, readonly





:user_id: User, many2one





:planning_id: Planning, many2one, required





:quantity: Planned, float, required


