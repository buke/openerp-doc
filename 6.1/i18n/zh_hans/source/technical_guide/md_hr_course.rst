
.. i18n: .. module:: md_hr_course
.. i18n:     :synopsis: Pilot Human Resources 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: md_hr_course
    :synopsis: Pilot Human Resources 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/md_hr_course"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/md_hr_course"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Pilot Human Resources (*md_hr_course*)
.. i18n: ======================================
.. i18n: :Module: md_hr_course
.. i18n: :Name: Pilot Human Resources
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: md_hr_course
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

Pilot Human Resources (*md_hr_course*)
======================================
:Module: md_hr_course
:Name: Pilot Human Resources
:Version: 5.0.1.0
:Author: Tiny
:Directory: md_hr_course
:Web: http://www.openerp.com
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

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/md_hr_course.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/md_hr_course.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/md_hr_course.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/md_hr_course.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`hr`
..

 * :mod:`hr`

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

.. i18n:  * Human Resources
.. i18n:  * Human Resources/Courses
.. i18n:  * Human Resources/Courses/Courses
.. i18n:  * Human Resources/Courses/Courses by Employee
..

 * Human Resources
 * Human Resources/Courses
 * Human Resources/Courses/Courses
 * Human Resources/Courses/Courses by Employee

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * md.hr.course.form (form)
.. i18n:  * md.hr.course.tree (tree)
.. i18n:  * md.hr.course.student.form (form)
.. i18n:  * md.hr.course.student.tree (tree)
..

 * md.hr.course.form (form)
 * md.hr.course.tree (tree)
 * md.hr.course.student.form (form)
 * md.hr.course.student.tree (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Course (md.hr.course)
.. i18n: #############################
..

Object: Course (md.hr.course)
#############################

.. i18n: :code: Code, char, required
..

:code: Code, char, required

.. i18n: :name: Course title, char, required
..

:name: Course title, char, required

.. i18n: Object: Course Student (md.hr.course.student)
.. i18n: #############################################
..

Object: Course Student (md.hr.course.student)
#############################################

.. i18n: :payback_clause_ends: Pay back clause ends, date
..

:payback_clause_ends: Pay back clause ends, date

.. i18n: :employee_id: Employee, many2one
..

:employee_id: Employee, many2one

.. i18n: :date: Date followed, date
..

:date: Date followed, date

.. i18n: :state: State, selection
..

:state: State, selection

.. i18n: :course_id: Course, many2one
..

:course_id: Course, many2one

.. i18n: :amount: Amount, float
..

:amount: Amount, float

.. i18n: :payback_clause: Pay back clause (in %), float
..

:payback_clause: Pay back clause (in %), float

.. i18n: :personal_contribution: Personal Contribution, boolean
..

:personal_contribution: Personal Contribution, boolean
