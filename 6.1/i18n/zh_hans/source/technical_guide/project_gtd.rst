
.. i18n: .. module:: project_gtd
.. i18n:     :synopsis: Getting Things Done - Time Management Module (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: project_gtd
    :synopsis: Getting Things Done - Time Management Module (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/project_gtd"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/project_gtd"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Getting Things Done - Time Management Module (*project_gtd*)
.. i18n: ============================================================
.. i18n: :Module: project_gtd
.. i18n: :Name: Getting Things Done - Time Management Module
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: project_gtd
.. i18n: :Web: 
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module implements all concepts defined by the Getting Things Done
.. i18n:   methodology. This world-wide used methodology is used for personal
.. i18n:   time management improvement.
.. i18n:   
.. i18n:   Getting Things Done (commonly abbreviated as GTD) is an action management
.. i18n:   method created by David Allen, and described in a book of the same name.
.. i18n:   
.. i18n:   GTD rests on the principle that a person needs to move tasks out of the mind by
.. i18n:   recording them externally. That way, the mind is freed from the job of
.. i18n:   remembering everything that needs to be done, and can concentrate on actually
.. i18n:   performing those tasks.
..

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

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/project_gtd.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/project_gtd.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/project_gtd.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/project_gtd.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`project`
..

 * :mod:`project`

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

.. i18n:  * Project Management/Configuration/Time Management
.. i18n:  * Project Management/Configuration/Time Management/Contexts
.. i18n:  * Project Management/Configuration/Time Management/Timeboxes
.. i18n:  * Project Management/Configuration/Time Management/Timeboxes/My Timeboxes
.. i18n:  * Project Management/Time Management
.. i18n:  * Project Management/Time Management/My Inbox
.. i18n:  * Project Management/Time Management/My Timeboxes
.. i18n:  * Project Management/Time Management/My Daily Timebox
..

 * Project Management/Configuration/Time Management
 * Project Management/Configuration/Time Management/Contexts
 * Project Management/Configuration/Time Management/Timeboxes
 * Project Management/Configuration/Time Management/Timeboxes/My Timeboxes
 * Project Management/Time Management
 * Project Management/Time Management/My Inbox
 * Project Management/Time Management/My Timeboxes
 * Project Management/Time Management/My Daily Timebox

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * project.gtd.context.tree (tree)
.. i18n:  * project.gtd.context.form (form)
.. i18n:  * project.gtd.timebox.tree (tree)
.. i18n:  * project.gtd.timebox.form (form)
.. i18n:  * project.task.gtd.inbox.tree (tree)
.. i18n:  * project.gtd.timebox.treelist (tree)
.. i18n:  * \* INHERIT project.task.form.timebox (form)
..

 * project.gtd.context.tree (tree)
 * project.gtd.context.form (form)
 * project.gtd.timebox.tree (tree)
 * project.gtd.timebox.form (form)
 * project.task.gtd.inbox.tree (tree)
 * project.gtd.timebox.treelist (tree)
 * \* INHERIT project.task.form.timebox (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Contexts (project.gtd.context)
.. i18n: ######################################
..

Object: Contexts (project.gtd.context)
######################################

.. i18n: :project_default_id: Default Project, many2one, required
..

:project_default_id: Default Project, many2one, required

.. i18n: :name: Context, char, required
..

:name: Context, char, required

.. i18n: :sequence: Sequence, integer
..

:sequence: Sequence, integer

.. i18n: Object: project.gtd.timebox (project.gtd.timebox)
.. i18n: #################################################
..

Object: project.gtd.timebox (project.gtd.timebox)
#################################################

.. i18n: :context6_id: Context 6, many2one
..

:context6_id: Context 6, many2one

.. i18n: :task1_ids: Tasks, one2many
..

:task1_ids: Tasks, one2many

.. i18n: :col_effective_hours: Effective Hours, boolean
..

:col_effective_hours: Effective Hours, boolean

.. i18n: :task3_ids: Tasks, one2many
..

:task3_ids: Tasks, one2many

.. i18n: :task6_ids: Tasks, one2many
..

:task6_ids: Tasks, one2many

.. i18n: :task_ids: Tasks, one2many
..

:task_ids: Tasks, one2many

.. i18n: :user_id: User, many2one, required
..

:user_id: User, many2one, required

.. i18n: :context4_id: Context 4, many2one
..

:context4_id: Context 4, many2one

.. i18n: :parent_id: Parent Timebox, many2one
..

:parent_id: Parent Timebox, many2one

.. i18n: :task2_ids: Tasks, one2many
..

:task2_ids: Tasks, one2many

.. i18n: :col_project: Project, boolean
..

:col_project: Project, boolean

.. i18n: :type: Type, selection, required
..

:type: Type, selection, required

.. i18n: :col_date_start: Date Start, boolean
..

:col_date_start: Date Start, boolean

.. i18n: :col_priority: Priority, boolean
..

:col_priority: Priority, boolean

.. i18n: :task4_ids: Tasks, one2many
..

:task4_ids: Tasks, one2many

.. i18n: :child_ids: Child Timeboxes, one2many
..

:child_ids: Child Timeboxes, one2many

.. i18n: :context2_id: Context 2, many2one
..

:context2_id: Context 2, many2one

.. i18n: :task5_ids: Tasks, one2many
..

:task5_ids: Tasks, one2many

.. i18n: :context3_id: Context 3, many2one
..

:context3_id: Context 3, many2one

.. i18n: :name: Timebox, char, required
..

:name: Timebox, char, required

.. i18n: :context5_id: Context 5, many2one
..

:context5_id: Context 5, many2one

.. i18n: :context1_id: Context 1, many2one, required
..

:context1_id: Context 1, many2one, required

.. i18n: :col_planned_hours: Planned Hours, boolean
..

:col_planned_hours: Planned Hours, boolean

.. i18n: :col_deadline: Deadline, boolean
..

:col_deadline: Deadline, boolean
