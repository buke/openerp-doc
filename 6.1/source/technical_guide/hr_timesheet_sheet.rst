
.. module:: hr_timesheet_sheet
    :synopsis: Timesheets (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hr_timesheet_sheet"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Timesheets (*hr_timesheet_sheet*)
=================================
:Module: hr_timesheet_sheet
:Name: Timesheets
:Version: 5.0.1.0
:Author: Tiny
:Directory: hr_timesheet_sheet
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  This module help you easily encode and validate timesheet and attendances
  within the same view. The upper part of the view is for attendances and
  track (sign in/sign out) events. The lower part is for timesheet.
  
  Others tabs contains statistics views to help you analyse your
  time or the time of your team:
  * Time spent by day (with attendances)
  * Time spent by project
  
  This module also implement a complete timesheet validation process:
  * Draft sheet
  * Confirmation at the end of the period by the employee
  * Validation by the project manager
  
  The validation can be configured in te company:
  * Period size (day, week, month, year)
  * Maximal difference between timesheet and attendances

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/hr_timesheet_sheet.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/hr_timesheet_sheet.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/hr_timesheet_sheet.zip>`_


Dependencies
------------

 * :mod:`hr_timesheet`
 * :mod:`hr_timesheet_invoice`
 * :mod:`process`

Reports
-------

None


Menus
-------

 * Human Resources/Timesheets
 * Human Resources/Timesheets/Timesheets
 * Human Resources/Timesheets/My timesheets
 * Human Resources/Timesheets/My timesheets/My timesheets to confirm
 * Human Resources/Timesheets/My Department's Timesheet
 * Human Resources/Timesheets/My Department's Timesheet/My Department's Timesheet to Validate
 * Human Resources/Timesheets/My Department's Timesheet/My Department's Timesheet to Confirm
 * Human Resources/Timesheets/My timesheets/My Current Timesheet
 * Human Resources/Timesheets/Timesheets/Timesheets To Confirm
 * Human Resources/Timesheets/Timesheets/Timesheets To Validate
 * Human Resources/Timesheets/Timesheets/Unvalidated Timesheets

Views
-----

 * hr.timesheet.sheet.tree (tree)
 * hr.timesheet.account.form (form)
 * hr.timesheet.account.tree (tree)
 * hr.timesheet.day.form (form)
 * hr.timesheet.day.tree (tree)
 * hr.timesheet.sheet.form (form)
 * \* INHERIT res.company.sheet (form)
 * \* INHERIT hr.analytic.timesheet.form (form)
 * \* INHERIT hr.attendance.form (form)
 * \* INHERIT hr.attendance.tree (tree)
 * hr.timesheet.sheet.tree.simplified (tree)


Objects
-------

Object: hr_timesheet_sheet.sheet (hr_timesheet_sheet.sheet)
###########################################################



:total_attendance: Total Attendance, float, readonly





:timesheet_ids: Timesheet lines, one2many, readonly





:user_id: User, many2one, required





:name: Description, char





:total_timesheet: Total Timesheet, float, readonly





:date_from: Date from, date, required, readonly





:date_to: Date to, date, required, readonly





:attendances_ids: Attendances, one2many, readonly





:period_ids: Period, one2many, readonly





:total_difference: Difference, float, readonly





:total_difference_day: Difference, float, readonly





:state: Status, selection, required, readonly





:total_attendance_day: Total Attendance, float, readonly





:account_ids: Analytic accounts, one2many, readonly





:date_current: Current date, date, required





:state_attendance: Current Status, selection, readonly





:total_timesheet_day: Total Timesheet, float, readonly




Object: Timesheets by period (hr_timesheet_sheet.sheet.day)
###########################################################



:total_attendance: Attendance, float, readonly





:total_difference: Difference, float, readonly





:sheet_id: Sheet, many2one, readonly





:total_timesheet: Project Timesheet, float, readonly





:name: Date, date, readonly




Object: Timesheets by period (hr_timesheet_sheet.sheet.account)
###############################################################



:total: Total Time, float, readonly





:sheet_id: Sheet, many2one, readonly





:name: Analytic Account, many2one, readonly





:invoice_rate: Invoice rate, many2one, readonly


