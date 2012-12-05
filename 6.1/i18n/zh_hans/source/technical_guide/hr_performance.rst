
.. i18n: .. module:: hr_performance
.. i18n:     :synopsis: Performance Review 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: hr_performance
    :synopsis: Performance Review 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hr_performance"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hr_performance"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Performance Review (*hr_performance*)
.. i18n: =====================================
.. i18n: :Module: hr_performance
.. i18n: :Name: Performance Review
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: hr_performance
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   A module that Check Performance For the Company Employees.
..

::

  A module that Check Performance For the Company Employees.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/hr_performance.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/hr_performance.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/hr_performance.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/hr_performance.zip>`_

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

.. i18n:  * Performance report
..

 * Performance report

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Human Resources/Performance Review/Performance HR
.. i18n:  * Human Resources/Performance Review/Review Attributes HR
..

 * Human Resources/Performance Review/Performance HR
 * Human Resources/Performance Review/Review Attributes HR

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * hr.performance.form (form)
.. i18n:  * hr.performance.tree (tree)
.. i18n:  * hr.attribute.line.form (form)
.. i18n:  * hr.attribute.line.tree (tree)
.. i18n:  * hr.performance.line.attribute.form (form)
.. i18n:  * hr.performance.line.attribute.tree (tree)
..

 * hr.performance.form (form)
 * hr.performance.tree (tree)
 * hr.attribute.line.form (form)
 * hr.attribute.line.tree (tree)
 * hr.performance.line.attribute.form (form)
 * hr.performance.line.attribute.tree (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Employee Performance  (hr.performance)
.. i18n: ##############################################
..

Object: Employee Performance  (hr.performance)
##############################################

.. i18n: :user_id: User, many2one, readonly
..

:user_id: User, many2one, readonly

.. i18n: :name: Description, char
..

:name: Description, char

.. i18n: :reviewer_id: Employee, many2one, readonly
..

:reviewer_id: Employee, many2one, readonly

.. i18n: :date_from: Date From, date, required
..

:date_from: Date From, date, required

.. i18n: :state: State, selection, readonly
..

:state: State, selection, readonly

.. i18n: :date_to: Date To, date, required
..

:date_to: Date To, date, required

.. i18n: :performance_id: Performance, one2many
..

:performance_id: Performance, one2many

.. i18n: Object: Performance Review Points (hr.performance.line)
.. i18n: #######################################################
..

Object: Performance Review Points (hr.performance.line)
#######################################################

.. i18n: :employee_id: Employee, many2one, required, readonly
..

:employee_id: Employee, many2one, required, readonly

.. i18n: :name: Description, char
..

:name: Description, char

.. i18n: :attribute_line: Attributes, one2many
..

:attribute_line: Attributes, one2many

.. i18n: :performance: Performance in (%), float, readonly
..

:performance: Performance in (%), float, readonly

.. i18n: :total: Total, float, readonly
..

:total: Total, float, readonly

.. i18n: :performance_id: Review Point, many2one
..

:performance_id: Review Point, many2one

.. i18n: Object: Review Attributes (hr.performance.line.attribute)
.. i18n: #########################################################
..

Object: Review Attributes (hr.performance.line.attribute)
#########################################################

.. i18n: :note: Description, text
..

:note: Description, text

.. i18n: :name: Attribute Name, char, required
..

:name: Attribute Name, char, required

.. i18n: :total_point: Total Point, integer, required
..

:total_point: Total Point, integer, required

.. i18n: Object: Attributes Lines (attribute.line)
.. i18n: #########################################
..

Object: Attributes Lines (attribute.line)
#########################################

.. i18n: :total_marks: Total Marks, float, readonly
..

:total_marks: Total Marks, float, readonly

.. i18n: :name: Description, char
..

:name: Description, char

.. i18n: :obtained_marks: Obtained Marks, float, required
..

:obtained_marks: Obtained Marks, float, required

.. i18n: :attribute_id: Attribute, many2one, required, readonly
..

:attribute_id: Attribute, many2one, required, readonly

.. i18n: :performance_line_id: Performance Line, many2one, readonly
..

:performance_line_id: Performance Line, many2one, readonly

.. i18n: :description: Description, text
..

:description: Description, text
