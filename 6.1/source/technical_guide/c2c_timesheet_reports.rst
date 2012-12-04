
.. module:: c2c_timesheet_reports
    :synopsis: Timesheet Reports 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/c2c_timesheet_reports"></div>
    <script src="http://js-kit.com/ratings.js"></script>

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

Description
-----------

::

  Timesheet Reports Module:
              * Add a report "/HR/report/Timesheets/Timesheet Status" that displays the timesheet status for each user: "confirmed", "draft", "missing". 
                It displays 5 periods' status previous to a given date
              * Add a field "ended" to the employee form to define when the employee stopped working for the company
              * Add a tool "/HR/Configuration/Timesheet Reminder" to send automatic emails to those who did not complete their timesheet and add a boolean field to employees to define if they should receive this message or not

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/c2c_timesheet_reports.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/c2c_timesheet_reports.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/c2c_timesheet_reports.zip>`_


Dependencies
------------

 * :mod:`hr_timesheet_sheet`
 * :mod:`hr`
 * :mod:`c2c_reporting_tools`

Reports
-------

 * Timesheet Status

Menus
-------

 * Human Resources/Reporting/Timesheet/Timesheets Status
 * Human Resources/Configuration/Timesheet Reminder

Views
-----

 * \* INHERIT hr.employee.end.date.form (form)


Objects
-------

Object: Handle the scheduling of messages (c2c_timesheet_reports.reminder)
##########################################################################



:reply_to: Reply To, char





:message: Message, text





:subject: Subject, char


