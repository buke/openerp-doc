
.. module:: project_gtd
    :synopsis: Getting Things Done - Time Management Module (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/project_gtd"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Getting Things Done - Time Management Module (*project_gtd*)
============================================================
:Module: project_gtd
:Name: Getting Things Done - Time Management Module
:Version: 5.0.1.0
:Author: Tiny
:Directory: project_gtd
:Web: 
:Official module: yes
:Quality certified: yes

Description
-----------

::

  This module implements all concepts defined by the Getting Things Done
  methodology. This world-wide used methodology is used for personal
  time management improvement.
  
  Getting Things Done (commonly abbreviated as GTD) is an action management
  method created by David Allen, and described in a book of the same name.
  
  GTD rests on the principle that a person needs to move tasks out of the mind by
  recording them externally. That way, the mind is freed from the job of
  remembering everything that needs to be done, and can concentrate on actually
  performing those tasks.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/project_gtd.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/project_gtd.zip>`_


Dependencies
------------

 * :mod:`project`

Reports
-------

None


Menus
-------

 * Project Management/Configuration/Time Management
 * Project Management/Configuration/Time Management/Contexts
 * Project Management/Configuration/Time Management/Timeboxes
 * Project Management/Configuration/Time Management/Timeboxes/My Timeboxes
 * Project Management/Time Management
 * Project Management/Time Management/My Inbox
 * Project Management/Time Management/My Timeboxes
 * Project Management/Time Management/My Daily Timebox

Views
-----

 * project.gtd.context.tree (tree)
 * project.gtd.context.form (form)
 * project.gtd.timebox.tree (tree)
 * project.gtd.timebox.form (form)
 * project.task.gtd.inbox.tree (tree)
 * project.gtd.timebox.treelist (tree)
 * \* INHERIT project.task.form.timebox (form)


Objects
-------

Object: Contexts (project.gtd.context)
######################################



:project_default_id: Default Project, many2one, required





:name: Context, char, required





:sequence: Sequence, integer




Object: project.gtd.timebox (project.gtd.timebox)
#################################################



:context6_id: Context 6, many2one





:task1_ids: Tasks, one2many





:col_effective_hours: Effective Hours, boolean





:task3_ids: Tasks, one2many





:task6_ids: Tasks, one2many





:task_ids: Tasks, one2many





:user_id: User, many2one, required





:context4_id: Context 4, many2one





:parent_id: Parent Timebox, many2one





:task2_ids: Tasks, one2many





:col_project: Project, boolean





:type: Type, selection, required





:col_date_start: Date Start, boolean





:col_priority: Priority, boolean





:task4_ids: Tasks, one2many





:child_ids: Child Timeboxes, one2many





:context2_id: Context 2, many2one





:task5_ids: Tasks, one2many





:context3_id: Context 3, many2one





:name: Timebox, char, required





:context5_id: Context 5, many2one





:context1_id: Context 1, many2one, required





:col_planned_hours: Planned Hours, boolean





:col_deadline: Deadline, boolean


