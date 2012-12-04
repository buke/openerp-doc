
.. i18n: .. module:: report_project
.. i18n:     :synopsis: Sales Management - Reporting (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: report_project
    :synopsis: Sales Management - Reporting (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_project"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_project"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Sales Management - Reporting (*report_project*)
.. i18n: ===============================================
.. i18n: :Module: report_project
.. i18n: :Name: Sales Management - Reporting
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: report_project
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   A module that adds some reports on projects.
.. i18n:       Closed Tasks (By User and By Project), Finished Task (By User and By Project)
..

::

  A module that adds some reports on projects.
      Closed Tasks (By User and By Project), Finished Task (By User and By Project)

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/report_project.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/report_project.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/report_project.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/report_project.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/report_project.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/report_project.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`project`
.. i18n:  * :mod:`report_task`
..

 * :mod:`project`
 * :mod:`report_task`

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

.. i18n:  * Project Management/Reporting/This Month
.. i18n:  * Project Management/Reporting/This Month/Tasks finished by project and user (this month)
.. i18n:  * Project Management/Reporting/All Months/Tasks Closed by Project and User
.. i18n:  * Project Management/Reporting/This Month/Tasks finished by project (this month)
.. i18n:  * Project Management/Reporting/All Months/Tasks Closed by Project
..

 * Project Management/Reporting/This Month
 * Project Management/Reporting/This Month/Tasks finished by project and user (this month)
 * Project Management/Reporting/All Months/Tasks Closed by Project and User
 * Project Management/Reporting/This Month/Tasks finished by project (this month)
 * Project Management/Reporting/All Months/Tasks Closed by Project

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * report.project.task.user.form (form)
.. i18n:  * report.project.task.user.tree (tree)
.. i18n:  * report.project.task.form (form)
.. i18n:  * report.project.task.tree (tree)
..

 * report.project.task.user.form (form)
 * report.project.task.user.tree (tree)
 * report.project.task.form (form)
 * report.project.task.tree (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Tasks by user and project (report.project.task.user)
.. i18n: ############################################################
..

Object: Tasks by user and project (report.project.task.user)
############################################################

.. i18n: :hours_effective: Effective Hours, float, readonly
..

:hours_effective: Effective Hours, float, readonly

.. i18n: :user_id: User, many2one, readonly
..

:user_id: User, many2one, readonly

.. i18n: :name: Month, date, readonly
..

:name: Month, date, readonly

.. i18n: :closing_days: Avg Closing Delay, char, readonly
..

:closing_days: Avg Closing Delay, char, readonly

.. i18n: :task_closed: Task Closed, integer, readonly
..

:task_closed: Task Closed, integer, readonly

.. i18n: :project_id: Project, many2one, readonly
..

:project_id: Project, many2one, readonly

.. i18n: :hours_delay: Avg. Plan.-Eff., float, readonly
..

:hours_delay: Avg. Plan.-Eff., float, readonly

.. i18n: :hours_planned: Planned Hours, float, readonly
..

:hours_planned: Planned Hours, float, readonly

.. i18n: Object: Tasks by project (report.project.task)
.. i18n: ##############################################
..

Object: Tasks by project (report.project.task)
##############################################

.. i18n: :hours_effective: Effective Hours, float, readonly
..

:hours_effective: Effective Hours, float, readonly

.. i18n: :name: Month, date, readonly
..

:name: Month, date, readonly

.. i18n: :closing_days: Avg Closing Delay, char, readonly
..

:closing_days: Avg Closing Delay, char, readonly

.. i18n: :task_closed: Task Closed, integer, readonly
..

:task_closed: Task Closed, integer, readonly

.. i18n: :project_id: Project, many2one, readonly
..

:project_id: Project, many2one, readonly

.. i18n: :hours_delay: Avg. Plan.-Eff., float, readonly
..

:hours_delay: Avg. Plan.-Eff., float, readonly

.. i18n: :hours_planned: Planned Hours, float, readonly
..

:hours_planned: Planned Hours, float, readonly
