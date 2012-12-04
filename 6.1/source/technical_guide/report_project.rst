
.. module:: report_project
    :synopsis: Sales Management - Reporting (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_project"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Sales Management - Reporting (*report_project*)
===============================================
:Module: report_project
:Name: Sales Management - Reporting
:Version: 5.0.1.0
:Author: Tiny
:Directory: report_project
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  A module that adds some reports on projects.
      Closed Tasks (By User and By Project), Finished Task (By User and By Project)

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/report_project.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/report_project.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/report_project.zip>`_


Dependencies
------------

 * :mod:`project`
 * :mod:`report_task`

Reports
-------

None


Menus
-------

 * Project Management/Reporting/This Month
 * Project Management/Reporting/This Month/Tasks finished by project and user (this month)
 * Project Management/Reporting/All Months/Tasks Closed by Project and User
 * Project Management/Reporting/This Month/Tasks finished by project (this month)
 * Project Management/Reporting/All Months/Tasks Closed by Project

Views
-----

 * report.project.task.user.form (form)
 * report.project.task.user.tree (tree)
 * report.project.task.form (form)
 * report.project.task.tree (tree)


Objects
-------

Object: Tasks by user and project (report.project.task.user)
############################################################



:hours_effective: Effective Hours, float, readonly





:user_id: User, many2one, readonly





:name: Month, date, readonly





:closing_days: Avg Closing Delay, char, readonly





:task_closed: Task Closed, integer, readonly





:project_id: Project, many2one, readonly





:hours_delay: Avg. Plan.-Eff., float, readonly





:hours_planned: Planned Hours, float, readonly




Object: Tasks by project (report.project.task)
##############################################



:hours_effective: Effective Hours, float, readonly





:name: Month, date, readonly





:closing_days: Avg Closing Delay, char, readonly





:task_closed: Task Closed, integer, readonly





:project_id: Project, many2one, readonly





:hours_delay: Avg. Plan.-Eff., float, readonly





:hours_planned: Planned Hours, float, readonly


