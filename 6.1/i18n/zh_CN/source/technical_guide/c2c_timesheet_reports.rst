
.. i18n: .. module:: c2c_timesheet_reports
.. i18n:     :synopsis: Timesheet Reports 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: c2c_timesheet_reports
    :synopsis: Timesheet Reports 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/c2c_timesheet_reports"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/c2c_timesheet_reports"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Timesheet Reports (*c2c_timesheet_reports*)
.. i18n: ===========================================
.. i18n: :Module: c2c_timesheet_reports
.. i18n: :Name: Timesheet Reports
.. i18n: :Version: 5.0.1.1
.. i18n: :Author: camptocamp.com (aw)
.. i18n: :Directory: c2c_timesheet_reports
.. i18n: :Web: http://camptocamp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

Timesheet Reports (*c2c_timesheet_reports*)
===========================================
:Module: c2c_timesheet_reports
:Name: Timesheet Reports
:Version: 5.0.1.1
:Author: camptocamp.com (aw)
:Directory: c2c_timesheet_reports
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
.. i18n:   Timesheet Reports Module:
.. i18n:               * Add a report "/HR/report/Timesheets/Timesheet Status" that displays the timesheet status for each user: "confirmed", "draft", "missing". 
.. i18n:                 It displays 5 periods' status previous to a given date
.. i18n:               * Add a field "ended" to the employee form to define when the employee stopped working for the company
.. i18n:               * Add a tool "/HR/Configuration/Timesheet Reminder" to send automatic emails to those who did not complete their timesheet and add a boolean field to employees to define if they should receive this message or not
..

::

  Timesheet Reports Module:
              * Add a report "/HR/report/Timesheets/Timesheet Status" that displays the timesheet status for each user: "confirmed", "draft", "missing". 
                It displays 5 periods' status previous to a given date
              * Add a field "ended" to the employee form to define when the employee stopped working for the company
              * Add a tool "/HR/Configuration/Timesheet Reminder" to send automatic emails to those who did not complete their timesheet and add a boolean field to employees to define if they should receive this message or not

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/c2c_timesheet_reports.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/c2c_timesheet_reports.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/c2c_timesheet_reports.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/c2c_timesheet_reports.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/c2c_timesheet_reports.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/c2c_timesheet_reports.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`hr_timesheet_sheet`
.. i18n:  * :mod:`hr`
.. i18n:  * :mod:`c2c_reporting_tools`
..

 * :mod:`hr_timesheet_sheet`
 * :mod:`hr`
 * :mod:`c2c_reporting_tools`

.. i18n: Reports
.. i18n: -------
..

Reports
-------

.. i18n:  * Timesheet Status
..

 * Timesheet Status

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Human Resources/Reporting/Timesheet/Timesheets Status
.. i18n:  * Human Resources/Configuration/Timesheet Reminder
..

 * Human Resources/Reporting/Timesheet/Timesheets Status
 * Human Resources/Configuration/Timesheet Reminder

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT hr.employee.end.date.form (form)
..

 * \* INHERIT hr.employee.end.date.form (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Handle the scheduling of messages (c2c_timesheet_reports.reminder)
.. i18n: ##########################################################################
..

Object: Handle the scheduling of messages (c2c_timesheet_reports.reminder)
##########################################################################

.. i18n: :reply_to: Reply To, char
..

:reply_to: Reply To, char

.. i18n: :message: Message, text
..

:message: Message, text

.. i18n: :subject: Subject, char
..

:subject: Subject, char
