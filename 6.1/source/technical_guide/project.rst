
.. module:: project
    :synopsis: Project Management (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/project"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Project Management (*project*)
==============================
:Module: project
:Name: Project Management
:Version: 5.0.1.1
:Author: Tiny
:Directory: project
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  Project management module that track multi-level projects, tasks,
  works done on tasks, eso. It is able to render planning, order tasks, eso.

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/project.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/project.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/project.zip>`_


Dependencies
------------

 * :mod:`product`
 * :mod:`account`
 * :mod:`hr`
 * :mod:`process`

Reports
-------

 * Gantt Representation

 * Gantt Representation

Menus
-------

 * Project Management/Configuration
 * Project Management/Projects/New Project
 * Project Management
 * Project Management/Tasks
 * Project Management/Projects
 * Project Management/Projects/All projects
 * Project Management/Projects/All projects/Running projects
 * Project Management/Configuration/Template of Projects
 * Project Management/Projects/My Projects
 * Project Management/Projects/My Projects/My Running Projects
 * Project Management/Projects/Projects Structure
 * Project Management/Tasks/All Tasks
 * Project Management/Tasks/My Tasks
 * Project Management/Tasks/My Tasks/My Pending Tasks
 * Project Management/Tasks/My Tasks/My Current Tasks
 * Project Management/Tasks/My Tasks/My Current Tasks/My Tasks in Progress
 * Project Management/Tasks/My Tasks/My Current Tasks/My Draft Tasks
 * Project Management/Tasks/New Task
 * Project Management/Tasks/All Tasks/Tasks in Progress
 * Project Management/Tasks/All Tasks/Unassigned Tasks
 * Project Management/Configuration/Task Types

Views
-----

 * project.project.form (form)
 * project.project.list (tree)
 * project.project.tree (tree)
 * project.task.work.form (form)
 * project.task.work.tree (tree)
 * project.project.tree (tree)
 * Compute Remaining Hours  (form)
 * project.task.form (form)
 * project.task.tree (tree)
 * my.pending.task.tree (tree)
 * project.task.calendar (calendar)
 * project.task.gantt (gantt)
 * project.task.graph (graph)
 * project.task.type.form (form)
 * project.task.type.tree (tree)
 * \* INHERIT res.company.task.config (form)


Objects
-------

Object: Project (project.project)
#################################



:tasks: Project tasks, one2many





:date_end: Expected End, date





:contact_id: Contact, many2one





:timesheet_id: Working Time, many2one

    *Timetable working hours to adjust the gantt diagram report*



:manager: Project Manager, many2one





:child_id: Subproject, one2many





:planned_hours: Planned Time, float, readonly

    *Sum of planned hours of all tasks related to this project.*



:partner_id: Partner, many2one





:warn_footer: Mail Footer, text

    *Footer added at the beginning of the email for the warning message sent to the customer when a task is closed.*



:warn_manager: Warn Manager, boolean

    *If you check this field, the project manager will receive a request each time a task is completed by his team.*



:warn_customer: Warn Partner, boolean

    *If you check this, the user will have a popup when closing a task that propose a message to send by email to the customer.*



:date_start: Starting Date, date





:priority: Sequence, integer





:parent_id: Parent Project, many2one

    *If you have [?] in the name, it means there are no analytic account linked to project.*



:state: State, selection, required, readonly





:complete_name: Project Name, char, readonly





:members: Project Members, many2many

    *Project's member. Not used in any computation, just for information purpose.*



:effective_hours: Time Spent, float, readonly

    *Sum of spent hours of all tasks related to this project.*



:active: Active, boolean





:name: Project Name, char, required





:notes: Notes, text

    *Internal description of the project.*



:warn_header: Mail Header, text

    *Header added at the beginning of the email for the warning message sent to the customer when a task is closed.*



:total_hours: Total Time, float, readonly

    *Sum of total hours of all tasks related to this project.*



:category_id: Analytic Account, many2one

    *Link this project to an analytic account if you need financial management on projects. It enables you to connect projects with budgets, planning, cost and revenue analysis, timesheets on projects, etc.*



:progress_rate: Progress, float, readonly

    *Percent of tasks closed according to the total of tasks todo.*


Object: Project task type (project.task.type)
#############################################



:name: Type, char, required





:description: Description, text




Object: Tasks (project.task)
############################



:sequence: Sequence, integer





:effective_hours: Hours Spent, float, readonly

    *Computed using the sum of the task work done.*



:planned_hours: Planned Hours, float, required

    *Estimated time to do the task, usually set by the project manager when the task is in draft state.*



:partner_id: Partner, many2one





:user_id: Assigned to, many2one





:date_start: Starting Date, datetime





:priority: Importance, selection





:parent_id: Parent Task, many2one





:state: Status, selection, required, readonly





:progress: Progress (%), float, readonly

    *Computed as: Time Spent / Total Time.*



:project_id: Project, many2one

    *If you have [?] in the project name, it means there are no analytic account linked to this project.*



:type: Type, many2one





:description: Description, text





:child_ids: Delegated Tasks, one2many





:work_ids: Work done, one2many





:active: Active, boolean





:delay_hours: Delay Hours, float, readonly

    *Computed as: Total Time - Estimated Time. It gives the difference of the time estimated by the project manager and the real time to close the task.*



:delegated_user_id: Delegated To, many2one





:name: Task summary, char, required





:date_deadline: Deadline, datetime





:notes: Notes, text





:date_close: Date Closed, datetime, readonly





:total_hours: Total Hours, float, readonly

    *Computed as: Time Spent + Remaining Time.*



:history: Task Details, text, readonly





:remaining_hours: Remaining Hours, float

    *Total remaining time, can be re-estimated periodically by the assignee of the task.*


Object: Task Work (project.task.work)
#####################################



:date: Date, datetime





:hours: Time Spent, float





:user_id: Done by, many2one, required





:name: Work summary, char





:task_id: Task, many2one, required




Object: config.compute.remaining (config.compute.remaining)
###########################################################



:remaining_hours: Remaining Hours, float

    *Total remaining time, can be re-estimated periodically by the assignee of the task.*
