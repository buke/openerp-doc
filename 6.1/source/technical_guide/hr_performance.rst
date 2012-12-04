
.. module:: hr_performance
    :synopsis: Performance Review 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hr_performance"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Performance Review (*hr_performance*)
=====================================
:Module: hr_performance
:Name: Performance Review
:Version: 5.0.1.0
:Author: Tiny
:Directory: hr_performance
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  A module that Check Performance For the Company Employees.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/hr_performance.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/hr_performance.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`hr`

Reports
-------

 * Performance report

Menus
-------

 * Human Resources/Performance Review/Performance HR
 * Human Resources/Performance Review/Review Attributes HR

Views
-----

 * hr.performance.form (form)
 * hr.performance.tree (tree)
 * hr.attribute.line.form (form)
 * hr.attribute.line.tree (tree)
 * hr.performance.line.attribute.form (form)
 * hr.performance.line.attribute.tree (tree)


Objects
-------

Object: Employee Performance  (hr.performance)
##############################################



:user_id: User, many2one, readonly





:name: Description, char





:reviewer_id: Employee, many2one, readonly





:date_from: Date From, date, required





:state: State, selection, readonly





:date_to: Date To, date, required





:performance_id: Performance, one2many




Object: Performance Review Points (hr.performance.line)
#######################################################



:employee_id: Employee, many2one, required, readonly





:name: Description, char





:attribute_line: Attributes, one2many





:performance: Performance in (%), float, readonly





:total: Total, float, readonly





:performance_id: Review Point, many2one




Object: Review Attributes (hr.performance.line.attribute)
#########################################################



:note: Description, text





:name: Attribute Name, char, required





:total_point: Total Point, integer, required




Object: Attributes Lines (attribute.line)
#########################################



:total_marks: Total Marks, float, readonly





:name: Description, char





:obtained_marks: Obtained Marks, float, required





:attribute_id: Attribute, many2one, required, readonly





:performance_line_id: Performance Line, many2one, readonly





:description: Description, text


