
.. module:: md_hr_course
    :synopsis: Pilot Human Resources 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/md_hr_course"></div>
    <script src="http://js-kit.com/ratings.js"></script>

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

Description
-----------

::

  None

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/md_hr_course.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/md_hr_course.zip>`_


Dependencies
------------

 * :mod:`hr`

Reports
-------

None


Menus
-------

 * Human Resources
 * Human Resources/Courses
 * Human Resources/Courses/Courses
 * Human Resources/Courses/Courses by Employee

Views
-----

 * md.hr.course.form (form)
 * md.hr.course.tree (tree)
 * md.hr.course.student.form (form)
 * md.hr.course.student.tree (tree)


Objects
-------

Object: Course (md.hr.course)
#############################



:code: Code, char, required





:name: Course title, char, required




Object: Course Student (md.hr.course.student)
#############################################



:payback_clause_ends: Pay back clause ends, date





:employee_id: Employee, many2one





:date: Date followed, date





:state: State, selection





:course_id: Course, many2one





:amount: Amount, float





:payback_clause: Pay back clause (in %), float





:personal_contribution: Personal Contribution, boolean


