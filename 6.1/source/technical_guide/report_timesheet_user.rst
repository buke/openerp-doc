
.. module:: report_timesheet_user
    :synopsis: Report for timesheet 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_timesheet_user"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Report for timesheet (*report_timesheet_user*)
==============================================
:Module: report_timesheet_user
:Name: Report for timesheet
:Version: 5.0.1.0
:Author: Tiny
:Directory: report_timesheet_user
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  New report for timesheet

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/report_timesheet_user.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/report_timesheet_user.zip>`_


Dependencies
------------

 * :mod:`hr_timesheet_sheet`
 * :mod:`multi_company`

Reports
-------

None


Menus
-------

 * Project
 * Project/Reporting
 * Project/Reporting/This Month
 * Project/Reporting/This Month/Timesheets by user and company
 * Project/Reporting/This Month/Timesheets by user and company/My Timesheets by company
 * Project/Reporting/All Months
 * Project/Reporting/All Months/Timesheets by user and company
 * Project/Reporting/All Months/Timesheets by user and company/My task by company
 * Project/Reporting/This Month/Timesheets by company
 * Project/Reporting/All Months/Timesheets by company

Views
-----

 * view.report.timesheet.user.user.form (form)
 * view.report.timesheet.user.user.tree (tree)
 * view.report.timesheet.user.form (form)
 * view.report.timesheet.user.tree (tree)


Objects
-------

Object: Tasks by user and company (report.timesheet.user.user)
##############################################################



:user_id: User, many2one, readonly





:name: Month, date, readonly





:total_cost: Task Cost, float, readonly





:company_id: Company Name, many2one, readonly





:total_hours: Task Hours, float, readonly





:user_company_id: User's Company, many2one, readonly




Object: Tasks by company (report.timesheet.user)
################################################



:total_cost: Task Cost, float, readonly





:total_hours: Task Hours, float, readonly





:user_company_id: User's Company, many2one, readonly





:name: Month, date, readonly





:company_id: Company Name, many2one, readonly


