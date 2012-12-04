
.. module:: report_task
    :synopsis: Report on tasks by user for projects (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_task"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Report on tasks by user for projects (*report_task*)
====================================================
:Module: report_task
:Name: Report on tasks by user for projects
:Version: 5.0.1.0
:Author: Tiny
:Directory: report_task
:Web: 
:Official module: yes
:Quality certified: yes

Description
-----------

::

  Gives statistics on tasks by user on projects to check the pipeline of users.

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/report_task.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/report_task.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/report_task.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`project`
 * :mod:`hr_timesheet_sheet`

Reports
-------

None


Menus
-------

 * Project Management/Reporting
 * Project Management/Reporting/All Months
 * Project Management/Reporting/All Months/Tasks by User
 * Human Resources/Reporting/Timesheet / Task Hours Per Month

Views
-----

 * report.project.task.form (form)
 * report.project.task.graph (graph)
 * report.project.task.tree (tree)
 * report.closed.task.tree (tree)
 * report.timesheet.task.user.tree (tree)


Objects
-------

Object: Tasks by user and project (report.task.user.pipeline.open)
##################################################################



:user_id: User, many2one, readonly





:task_progress: Task Progress, float, readonly





:task_hrs: Task Hours, float, readonly





:task_nbr: Task Number, float, readonly





:company_id: Company, many2one





:task_state: Status, selection, readonly




Object: Closed Task Report (report.closed.task)
###############################################



:planned_hours: Planned Hours, float, readonly





:user_id: Assigned to, many2one, readonly





:name: Task summary, char, readonly





:date_deadline: Deadline, datetime, readonly





:sequence: Sequence, integer, readonly





:date_close: Date Closed, datetime, readonly





:priority: Importance, selection, readonly





:state: Status, selection, readonly





:progress: Progress (%), float, readonly





:project_id: Project, many2one, readonly





:delay_hours: Delay Hours, float, readonly





:remaining_hours: Remaining Hours, float, readonly




Object: report.timesheet.task.user (report.timesheet.task.user)
###############################################################



:task_hrs: Task Hours, float, readonly





:user_id: User, many2one, readonly





:name: Month, date, readonly





:timesheet_hrs: Timesheet Hours, float, readonly


