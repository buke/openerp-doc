
.. i18n: .. module:: hr_attendance
.. i18n:     :synopsis: Attendances Of Employees (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: hr_attendance
    :synopsis: Attendances Of Employees (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hr_attendance"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hr_attendance"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Attendances Of Employees (*hr_attendance*)
.. i18n: ==========================================
.. i18n: :Module: hr_attendance
.. i18n: :Name: Attendances Of Employees
.. i18n: :Version: 5.0.1.1
.. i18n: :Author: Tiny
.. i18n: :Directory: hr_attendance
.. i18n: :Web: 
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

Attendances Of Employees (*hr_attendance*)
==========================================
:Module: hr_attendance
:Name: Attendances Of Employees
:Version: 5.0.1.1
:Author: Tiny
:Directory: hr_attendance
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
.. i18n:   This module aims to manage employee's attendances.
..

::

  This module aims to manage employee's attendances.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/hr_attendance.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/hr_attendance.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/hr_attendance.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/hr_attendance.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`hr`
..

 * :mod:`base`
 * :mod:`hr`

.. i18n: Reports
.. i18n: -------
..

Reports
-------

.. i18n:  * Attendance Error Report
..

 * Attendance Error Report

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Human Resources/Attendances
.. i18n:  * Human Resources/Attendances/Attendances
.. i18n:  * Human Resources/Configuration/Attendance Reasons
.. i18n:  * Human Resources/Attendances/Sign in / Sign out
..

 * Human Resources/Attendances
 * Human Resources/Attendances/Attendances
 * Human Resources/Configuration/Attendance Reasons
 * Human Resources/Attendances/Sign in / Sign out

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * hr.attendance.form (form)
.. i18n:  * hr.attendance.tree (tree)
.. i18n:  * hr.attendance.tree (tree)
.. i18n:  * hr.action.reason.form (form)
.. i18n:  * hr.action.reason.tree (tree)
.. i18n:  * \* INHERIT hr.employee.form1 (form)
..

 * hr.attendance.form (form)
 * hr.attendance.tree (tree)
 * hr.attendance.tree (tree)
 * hr.action.reason.form (form)
 * hr.action.reason.tree (tree)
 * \* INHERIT hr.employee.form1 (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Action reason (hr.action.reason)
.. i18n: ########################################
..

Object: Action reason (hr.action.reason)
########################################

.. i18n: :name: Reason, char, required
..

:name: Reason, char, required

.. i18n: :action_type: Action's type, selection
..

:action_type: Action's type, selection

.. i18n: Object: Attendance (hr.attendance)
.. i18n: ##################################
..

Object: Attendance (hr.attendance)
##################################

.. i18n: :action: Action, selection, required
..

:action: Action, selection, required

.. i18n: :employee_id: Employee, many2one, required
..

:employee_id: Employee, many2one, required

.. i18n: :name: Date, datetime, required
..

:name: Date, datetime, required

.. i18n: :action_desc: Action reason, many2one
..

:action_desc: Action reason, many2one
