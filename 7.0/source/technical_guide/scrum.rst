
.. module:: scrum
    :synopsis: Scrum, Agile Development Method (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/scrum"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Scrum, Agile Development Method (*scrum*)
=========================================
:Module: scrum
:Name: Scrum, Agile Development Method
:Version: 5.0.1.0
:Author: Tiny
:Directory: scrum
:Web: 
:Official module: yes
:Quality certified: yes

Description
-----------

::

  This modules implements all concepts defined by the scrum project
      management methodology for IT companies:
      * Project with sprints, product owner, scrum master
      * Sprints with reviews, daily meetings, feedback
      * Product backlog
      * Sprint backlog
  
      It adds some concepts to the project management module:
      * Mid-term, long-term road-map
      * Customers/functional requests VS technical ones
  
      It also create a new reporting:
      * Burn-down chart
  
      The scrum projects and tasks inherits from the real projects and
      tasks, so you can continue working on normal tasks that will also
      include tasks from scrum projects.
  
      More information on the methodology:
      * http://controlchaos.com

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/scrum.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/scrum.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/scrum.zip>`_


Dependencies
------------

 * :mod:`project`
 * :mod:`process`

Reports
-------

None


Menus
-------

 * Project Management/Scrum
 * Project Management/Scrum/Projects
 * Project Management/Scrum/Projects/Edit Projects
 * Project Management/Scrum/Backlogs
 * Project Management/Scrum/Backlogs/Draft Backlogs
 * Project Management/Scrum/Backlogs/Opened Backlogs
 * Project Management/Scrum/Sprint
 * Project Management/Scrum/Sprint/Opened Sprints
 * Project Management/Scrum/Sprint/Draft Sprints
 * Project Management/Scrum/Sprint/Sprints Done
 * Project Management/Scrum/Sprint/My Sprints (Product Owner)
 * Project Management/Scrum/Sprint/My Sprints (Scrum Master)
 * Project Management/Scrum/Sprint/My Sprints (Product Owner)/My opened sprints (Product Owner)
 * Project Management/Scrum/Sprint/My Sprints (Scrum Master)/My opened sprints (Scrum Master)
 * Project Management/Scrum/Scrum Meeting
 * Project Management/Scrum/All Tasks
 * Project Management/Scrum/All Tasks/My tasks
 * Project Management/Scrum/All Tasks/My tasks/My opened tasks
 * Project Management/Tasks/All Tasks/Opened tasks

Views
-----

 * \* INHERIT scrum.project.form (form)
 * scrum.project.tree (tree)
 * scrum.product.backlog.tree (tree)
 * scrum.product.backlog.form (form)
 * scrum.sprint.tree (tree)
 * scrum.sprint.form (form)
 * scrum.meeting.tree (tree)
 * Scrum Meeting (form)
 * \* INHERIT scrum.task.form (form)


Objects
-------

Object: Scrum Team (scrum.team)
###############################



:users_id: Users, many2many





:name: Team Name, char




Object: Scrum Project (scrum.project)
#####################################



:tasks: Scrum Tasks, one2many





:date_end: Expected End, date





:contact_id: Contact, many2one





:effective_hours: Time Spent, float, readonly

    *Sum of spent hours of all tasks related to this project.*



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





:parent_id: Parent project, many2one





:state: State, selection, required, readonly





:complete_name: Project Name, char, readonly





:timesheet_id: Working Time, many2one

    *Timetable working hours to adjust the gantt diagram report*



:scrum: Is Scrum, integer





:members: Project Members, many2many

    *Project's member. Not used in any computation, just for information purpose.*



:active: Active, boolean





:sprint_size: Sprint Days, integer





:name: Project Name, char, required





:notes: Notes, text

    *Internal description of the project.*



:warn_header: Mail Header, text

    *Header added at the beginning of the email for the warning message sent to the customer when a task is closed.*



:total_hours: Total Time, float, readonly

    *Sum of total hours of all tasks related to this project.*



:product_owner_id: Product Owner, many2one





:category_id: Analytic Account, many2one

    *Link this project to an analytic account if you need financial management on projects. It enables you to connect projects with budgets, planning, cost and revenue analysis, timesheets on projects, etc.*



:progress_rate: Progress, float, readonly

    *Percent of tasks closed according to the total of tasks todo.*


Object: Scrum Sprint (scrum.sprint)
###################################



:date_stop: Ending Date, date, required





:planned_hours: Planned Hours, float, readonly





:name: Sprint Name, char, required





:retrospective: Sprint Retrospective, text





:backlog_ids: Sprint Backlog, one2many





:review: Sprint Review, text





:date_start: Starting Date, date, required





:scrum_master_id: Scrum Master, many2one, required





:state: Status, selection, required





:meetings_id: Daily Scrum, one2many





:effective_hours: Effective hours, float, readonly





:progress: Progress (0-100), float, readonly





:project_id: Project, many2one, required





:product_owner_id: Product Owner, many2one, required




Object: Product Backlog (scrum.product.backlog)
###############################################



:priority: Priority, selection





:planned_hours: Planned Hours, float, readonly





:user_id: User, many2one





:name: Feature, char, required





:tasks_id: Tasks Details, one2many





:sequence: Sequence, integer





:note: Note, text





:effective_hours: Effective hours, float, readonly





:state: Status, selection, required





:sprint_id: Sprint, many2one





:active: Active, boolean





:progress: Progress (0-100), float, readonly





:project_id: Scrum Project, many2one, required




Object: Scrum Task (scrum.task)
###############################



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





:scrum: Is Scrum, integer





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



:product_backlog_id: Product Backlog, many2one





:history: Task Details, text, readonly





:remaining_hours: Remaining Hours, float

    *Total remaining time, can be re-estimated periodically by the assignee of the task.*


Object: Scrum Meeting (scrum.meeting)
#####################################



:question_blocks: Blocks encountered, text





:question_yesterday: Tasks since yesterday, text





:name: Meeting Name, char, required





:question_today: Tasks for today, text





:question_backlog: Backlog Accurate, text





:sprint_id: Sprint, many2one, required





:date: Meeting Date, date, required


