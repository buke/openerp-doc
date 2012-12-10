
.. i18n: .. module:: report_task
.. i18n:     :synopsis: Report on tasks by user for projects (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: report_task
    :synopsis: Report on tasks by user for projects (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_task"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_task"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Report on tasks by user for projects (*report_task*)
.. i18n: ====================================================
.. i18n: :Module: report_task
.. i18n: :Name: Report on tasks by user for projects
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: report_task
.. i18n: :Web: 
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Gives statistics on tasks by user on projects to check the pipeline of users.
..

::

  Gives statistics on tasks by user on projects to check the pipeline of users.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/report_task.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/report_task.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/report_task.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/report_task.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/report_task.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/report_task.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`project`
.. i18n:  * :mod:`hr_timesheet_sheet`
..

 * :mod:`base`
 * :mod:`project`
 * :mod:`hr_timesheet_sheet`

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

.. i18n:  * Project Management/Reporting
.. i18n:  * Project Management/Reporting/All Months
.. i18n:  * Project Management/Reporting/All Months/Tasks by User
.. i18n:  * Human Resources/Reporting/Timesheet / Task Hours Per Month
..

 * Project Management/Reporting
 * Project Management/Reporting/All Months
 * Project Management/Reporting/All Months/Tasks by User
 * Human Resources/Reporting/Timesheet / Task Hours Per Month

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * report.project.task.form (form)
.. i18n:  * report.project.task.graph (graph)
.. i18n:  * report.project.task.tree (tree)
.. i18n:  * report.closed.task.tree (tree)
.. i18n:  * report.timesheet.task.user.tree (tree)
..

 * report.project.task.form (form)
 * report.project.task.graph (graph)
 * report.project.task.tree (tree)
 * report.closed.task.tree (tree)
 * report.timesheet.task.user.tree (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Tasks by user and project (report.task.user.pipeline.open)
.. i18n: ##################################################################
..

Object: Tasks by user and project (report.task.user.pipeline.open)
##################################################################

.. i18n: :user_id: User, many2one, readonly
..

:user_id: User, many2one, readonly

.. i18n: :task_progress: Task Progress, float, readonly
..

:task_progress: Task Progress, float, readonly

.. i18n: :task_hrs: Task Hours, float, readonly
..

:task_hrs: Task Hours, float, readonly

.. i18n: :task_nbr: Task Number, float, readonly
..

:task_nbr: Task Number, float, readonly

.. i18n: :company_id: Company, many2one
..

:company_id: Company, many2one

.. i18n: :task_state: Status, selection, readonly
..

:task_state: Status, selection, readonly

.. i18n: Object: Closed Task Report (report.closed.task)
.. i18n: ###############################################
..

Object: Closed Task Report (report.closed.task)
###############################################

.. i18n: :planned_hours: Planned Hours, float, readonly
..

:planned_hours: Planned Hours, float, readonly

.. i18n: :user_id: Assigned to, many2one, readonly
..

:user_id: Assigned to, many2one, readonly

.. i18n: :name: Task summary, char, readonly
..

:name: Task summary, char, readonly

.. i18n: :date_deadline: Deadline, datetime, readonly
..

:date_deadline: Deadline, datetime, readonly

.. i18n: :sequence: Sequence, integer, readonly
..

:sequence: Sequence, integer, readonly

.. i18n: :date_close: Date Closed, datetime, readonly
..

:date_close: Date Closed, datetime, readonly

.. i18n: :priority: Importance, selection, readonly
..

:priority: Importance, selection, readonly

.. i18n: :state: Status, selection, readonly
..

:state: Status, selection, readonly

.. i18n: :progress: Progress (%), float, readonly
..

:progress: Progress (%), float, readonly

.. i18n: :project_id: Project, many2one, readonly
..

:project_id: Project, many2one, readonly

.. i18n: :delay_hours: Delay Hours, float, readonly
..

:delay_hours: Delay Hours, float, readonly

.. i18n: :remaining_hours: Remaining Hours, float, readonly
..

:remaining_hours: Remaining Hours, float, readonly

.. i18n: Object: report.timesheet.task.user (report.timesheet.task.user)
.. i18n: ###############################################################
..

Object: report.timesheet.task.user (report.timesheet.task.user)
###############################################################

.. i18n: :task_hrs: Task Hours, float, readonly
..

:task_hrs: Task Hours, float, readonly

.. i18n: :user_id: User, many2one, readonly
..

:user_id: User, many2one, readonly

.. i18n: :name: Month, date, readonly
..

:name: Month, date, readonly

.. i18n: :timesheet_hrs: Timesheet Hours, float, readonly
..

:timesheet_hrs: Timesheet Hours, float, readonly
