
.. module:: c2c_project_activities
    :synopsis: Project activities 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/c2c_project_activities"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Project activities (*c2c_project_activities*)
=============================================
:Module: c2c_project_activities
:Name: Project activities
:Version: 5.0.1.0
:Author: Camptocamp
:Directory: c2c_project_activities
:Web: http://camptocamp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  None

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/c2c_project_activities.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/c2c_project_activities.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/c2c_project_activities.zip>`_


Dependencies
------------

 * :mod:`account`
 * :mod:`hr_timesheet_sheet`
 * :mod:`project`

Reports
-------

None


Menus
-------

 * Project Management/Configuration/Project activity/Project activity
 * Project Management/Configuration/Project activity/Activity tree
 * Project Management/Configuration/Project activity/Edit Project activity

Views
-----

 * project.activity_al.form (form)
 * project.activity_al.list (tree)
 * project.activity_al.tree (tree)
 * \* INHERIT account.analytic.account.form (form)
 * \* INHERIT hr.timesheet.sheet.form (form)
 * \* INHERIT account.analytic.line.form (form)
 * \* INHERIT account.analytic.line.tree (tree)


Objects
-------

Object: Project activity (project.activity_al)
##############################################



:parent_id: Parent activity, many2one





:code: Code, char, required





:child_ids: Childs Activity, one2many





:project_ids: Concerned project, many2many





:name: Activity, char, required


