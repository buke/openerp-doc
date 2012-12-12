
.. module:: hr_contract_available
    :synopsis: Human Resources Contracts - Human resources Reservations Management 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hr_contract_available"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Human Resources Contracts - Human resources Reservations Management (*hr_contract_available*)
==============================================================================================
:Module: hr_contract_available
:Name: Human Resources Contracts - Human resources Reservations Management
:Version: 5.0.0.1
:Author: Tiny
:Directory: hr_contract_available
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  This module is a reservation system on employees.
  
      You can assign an employee to a poste or a department for a
      defined period. This module is used to track availability and
      reservations on human resources.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/hr_contract_available.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/hr_contract_available.zip>`_


Dependencies
------------

 * :mod:`hr_contract`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT hr.hr.employee.view.form2 (form)
 * \* INHERIT hr.employee.available.tree (tree)


Objects
-------

Object: Allocations (hr.allocation)
###################################



:function: Function, many2one





:employee_id: Employee, many2one, required





:name: Allocation Name, char, required





:date_end: End Date, date

    *Keep empty for unlimited allocation.*



:date_start: Start Date, date, required





:state: State, selection, required





:department_id: Department, many2one, required


