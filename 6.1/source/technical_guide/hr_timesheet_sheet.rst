
.. i18n: .. module:: hr_timesheet_sheet
.. i18n:     :synopsis: Timesheets (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: hr_timesheet_sheet
    :synopsis: Timesheets (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hr_timesheet_sheet"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hr_timesheet_sheet"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Timesheets (*hr_timesheet_sheet*)
.. i18n: =================================
.. i18n: :Module: hr_timesheet_sheet
.. i18n: :Name: Timesheets
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: hr_timesheet_sheet
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module help you easily encode and validate timesheet and attendances
.. i18n:   within the same view. The upper part of the view is for attendances and
.. i18n:   track (sign in/sign out) events. The lower part is for timesheet.
.. i18n:   
.. i18n:   Others tabs contains statistics views to help you analyse your
.. i18n:   time or the time of your team:
.. i18n:   * Time spent by day (with attendances)
.. i18n:   * Time spent by project
.. i18n:   
.. i18n:   This module also implement a complete timesheet validation process:
.. i18n:   * Draft sheet
.. i18n:   * Confirmation at the end of the period by the employee
.. i18n:   * Validation by the project manager
.. i18n:   
.. i18n:   The validation can be configured in te company:
.. i18n:   * Period size (day, week, month, year)
.. i18n:   * Maximal difference between timesheet and attendances
..

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

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/hr_timesheet_sheet.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/hr_timesheet_sheet.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/hr_timesheet_sheet.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/hr_timesheet_sheet.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/hr_timesheet_sheet.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/hr_timesheet_sheet.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`hr_timesheet`
.. i18n:  * :mod:`hr_timesheet_invoice`
.. i18n:  * :mod:`process`
..

 * :mod:`hr_timesheet`
 * :mod:`hr_timesheet_invoice`
 * :mod:`process`

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

.. i18n:  * Human Resources/Timesheets
.. i18n:  * Human Resources/Timesheets/Timesheets
.. i18n:  * Human Resources/Timesheets/My timesheets
.. i18n:  * Human Resources/Timesheets/My timesheets/My timesheets to confirm
.. i18n:  * Human Resources/Timesheets/My Department's Timesheet
.. i18n:  * Human Resources/Timesheets/My Department's Timesheet/My Department's Timesheet to Validate
.. i18n:  * Human Resources/Timesheets/My Department's Timesheet/My Department's Timesheet to Confirm
.. i18n:  * Human Resources/Timesheets/My timesheets/My Current Timesheet
.. i18n:  * Human Resources/Timesheets/Timesheets/Timesheets To Confirm
.. i18n:  * Human Resources/Timesheets/Timesheets/Timesheets To Validate
.. i18n:  * Human Resources/Timesheets/Timesheets/Unvalidated Timesheets
..

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

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * hr.timesheet.sheet.tree (tree)
.. i18n:  * hr.timesheet.account.form (form)
.. i18n:  * hr.timesheet.account.tree (tree)
.. i18n:  * hr.timesheet.day.form (form)
.. i18n:  * hr.timesheet.day.tree (tree)
.. i18n:  * hr.timesheet.sheet.form (form)
.. i18n:  * \* INHERIT res.company.sheet (form)
.. i18n:  * \* INHERIT hr.analytic.timesheet.form (form)
.. i18n:  * \* INHERIT hr.attendance.form (form)
.. i18n:  * \* INHERIT hr.attendance.tree (tree)
.. i18n:  * hr.timesheet.sheet.tree.simplified (tree)
..

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

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: hr_timesheet_sheet.sheet (hr_timesheet_sheet.sheet)
.. i18n: ###########################################################
..

Object: hr_timesheet_sheet.sheet (hr_timesheet_sheet.sheet)
###########################################################

.. i18n: :total_attendance: Total Attendance, float, readonly
..

:total_attendance: Total Attendance, float, readonly

.. i18n: :timesheet_ids: Timesheet lines, one2many, readonly
..

:timesheet_ids: Timesheet lines, one2many, readonly

.. i18n: :user_id: User, many2one, required
..

:user_id: User, many2one, required

.. i18n: :name: Description, char
..

:name: Description, char

.. i18n: :total_timesheet: Total Timesheet, float, readonly
..

:total_timesheet: Total Timesheet, float, readonly

.. i18n: :date_from: Date from, date, required, readonly
..

:date_from: Date from, date, required, readonly

.. i18n: :date_to: Date to, date, required, readonly
..

:date_to: Date to, date, required, readonly

.. i18n: :attendances_ids: Attendances, one2many, readonly
..

:attendances_ids: Attendances, one2many, readonly

.. i18n: :period_ids: Period, one2many, readonly
..

:period_ids: Period, one2many, readonly

.. i18n: :total_difference: Difference, float, readonly
..

:total_difference: Difference, float, readonly

.. i18n: :total_difference_day: Difference, float, readonly
..

:total_difference_day: Difference, float, readonly

.. i18n: :state: Status, selection, required, readonly
..

:state: Status, selection, required, readonly

.. i18n: :total_attendance_day: Total Attendance, float, readonly
..

:total_attendance_day: Total Attendance, float, readonly

.. i18n: :account_ids: Analytic accounts, one2many, readonly
..

:account_ids: Analytic accounts, one2many, readonly

.. i18n: :date_current: Current date, date, required
..

:date_current: Current date, date, required

.. i18n: :state_attendance: Current Status, selection, readonly
..

:state_attendance: Current Status, selection, readonly

.. i18n: :total_timesheet_day: Total Timesheet, float, readonly
..

:total_timesheet_day: Total Timesheet, float, readonly

.. i18n: Object: Timesheets by period (hr_timesheet_sheet.sheet.day)
.. i18n: ###########################################################
..

Object: Timesheets by period (hr_timesheet_sheet.sheet.day)
###########################################################

.. i18n: :total_attendance: Attendance, float, readonly
..

:total_attendance: Attendance, float, readonly

.. i18n: :total_difference: Difference, float, readonly
..

:total_difference: Difference, float, readonly

.. i18n: :sheet_id: Sheet, many2one, readonly
..

:sheet_id: Sheet, many2one, readonly

.. i18n: :total_timesheet: Project Timesheet, float, readonly
..

:total_timesheet: Project Timesheet, float, readonly

.. i18n: :name: Date, date, readonly
..

:name: Date, date, readonly

.. i18n: Object: Timesheets by period (hr_timesheet_sheet.sheet.account)
.. i18n: ###############################################################
..

Object: Timesheets by period (hr_timesheet_sheet.sheet.account)
###############################################################

.. i18n: :total: Total Time, float, readonly
..

:total: Total Time, float, readonly

.. i18n: :sheet_id: Sheet, many2one, readonly
..

:sheet_id: Sheet, many2one, readonly

.. i18n: :name: Analytic Account, many2one, readonly
..

:name: Analytic Account, many2one, readonly

.. i18n: :invoice_rate: Invoice rate, many2one, readonly
..

:invoice_rate: Invoice rate, many2one, readonly
