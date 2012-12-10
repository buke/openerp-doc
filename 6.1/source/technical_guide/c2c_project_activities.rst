
.. i18n: .. module:: c2c_project_activities
.. i18n:     :synopsis: Project activities 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: c2c_project_activities
    :synopsis: Project activities 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/c2c_project_activities"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/c2c_project_activities"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Project activities (*c2c_project_activities*)
.. i18n: =============================================
.. i18n: :Module: c2c_project_activities
.. i18n: :Name: Project activities
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Camptocamp
.. i18n: :Directory: c2c_project_activities
.. i18n: :Web: http://camptocamp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   None
..

::

  None

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/c2c_project_activities.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/c2c_project_activities.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/c2c_project_activities.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/c2c_project_activities.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/c2c_project_activities.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/c2c_project_activities.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`account`
.. i18n:  * :mod:`hr_timesheet_sheet`
.. i18n:  * :mod:`project`
..

 * :mod:`account`
 * :mod:`hr_timesheet_sheet`
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

.. i18n:  * Project Management/Configuration/Project activity/Project activity
.. i18n:  * Project Management/Configuration/Project activity/Activity tree
.. i18n:  * Project Management/Configuration/Project activity/Edit Project activity
..

 * Project Management/Configuration/Project activity/Project activity
 * Project Management/Configuration/Project activity/Activity tree
 * Project Management/Configuration/Project activity/Edit Project activity

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * project.activity_al.form (form)
.. i18n:  * project.activity_al.list (tree)
.. i18n:  * project.activity_al.tree (tree)
.. i18n:  * \* INHERIT account.analytic.account.form (form)
.. i18n:  * \* INHERIT hr.timesheet.sheet.form (form)
.. i18n:  * \* INHERIT account.analytic.line.form (form)
.. i18n:  * \* INHERIT account.analytic.line.tree (tree)
..

 * project.activity_al.form (form)
 * project.activity_al.list (tree)
 * project.activity_al.tree (tree)
 * \* INHERIT account.analytic.account.form (form)
 * \* INHERIT hr.timesheet.sheet.form (form)
 * \* INHERIT account.analytic.line.form (form)
 * \* INHERIT account.analytic.line.tree (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Project activity (project.activity_al)
.. i18n: ##############################################
..

Object: Project activity (project.activity_al)
##############################################

.. i18n: :parent_id: Parent activity, many2one
..

:parent_id: Parent activity, many2one

.. i18n: :code: Code, char, required
..

:code: Code, char, required

.. i18n: :child_ids: Childs Activity, one2many
..

:child_ids: Childs Activity, one2many

.. i18n: :project_ids: Concerned project, many2many
..

:project_ids: Concerned project, many2many

.. i18n: :name: Activity, char, required
..

:name: Activity, char, required
