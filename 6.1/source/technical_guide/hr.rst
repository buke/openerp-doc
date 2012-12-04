
.. module:: hr
    :synopsis: Human Resources (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hr"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Human Resources (*hr*)
======================
:Module: hr
:Name: Human Resources
:Version: 5.0.1.1
:Author: Tiny
:Directory: hr
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  Module for human resource management. You can manage:
      * Employees and hierarchies
      * Work hours sheets
      * Attendances and sign in/out system
  
      Different reports are also provided, mainly for attendance statistics.

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/hr.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/hr.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/hr.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`process`

Reports
-------

None


Menus
-------

 * Human Resources
 * Human Resources/Reporting
 * Human Resources/Configuration
 * Human Resources/Employees
 * Human Resources/Employees/Employees Structure
 * Human Resources/Employees/All Employees
 * Human Resources/Employees/New Employee
 * Human Resources/Configuration/Working Time Categories
 * Human Resources/Configuration/Categories of Employee
 * Human Resources/Configuration/Categories of Employee/Categories structure
 * Administration/Users/Departments
 * Administration/Users/Departments/Departments

Views
-----

 * hr.employee.form (form)
 * hr.employee.tree (tree)
 * hr.employee.tree (tree)
 * hr.timesheet.group.form (form)
 * hr.timesheet.tree (tree)
 * hr.timesheet.form (form)
 * hr.employee.category.form (form)
 * hr.employee.category.list (tree)
 * hr.employee.category.tree (tree)
 * hr.department.form (form)
 * hr.department.tree (tree)
 * \* INHERIT res.users.form (form)


Objects
-------

Object: Working Time (hr.timesheet.group)
#########################################



:timesheet_id: Working Time, one2many





:manager: Workgroup manager, many2one





:name: Group name, char, required




Object: Employee Category (hr.employee.category)
################################################



:parent_id: Parent Category, many2one





:child_ids: Child Categories, one2many





:name: Category, char, required




Object: Employee (hr.employee)
##############################



:company_id: Company, many2one





:otherid: Other ID, char





:country_id: Nationality, many2one





:user_id: Related User, many2one





:work_location: Office Location, char





:name: Employee, char, required





:parent_id: Manager, many2one





:work_phone: Work Phone, char





:gender: Gender, selection





:ssnid: SSN No, char





:child_ids: Subordinates, one2many





:address_id: Working Address, many2one





:marital: Marital Status, selection





:sinid: SIN No, char





:birthday: Birthday, date





:active: Active, boolean





:category_id: Category, many2one





:work_email: Work Email, char





:notes: Notes, text





:address_home_id: Home Address, many2one




Object: Timesheet Line (hr.timesheet)
#####################################



:dayofweek: Day of week, selection





:name: Name, char, required





:tgroup_id: Employee's timesheet group, many2one





:date_from: Starting date, date





:hour_from: Work from, float, required





:hour_to: Work to, float, required




Object: hr.department (hr.department)
#####################################



:member_ids: Members, many2many





:name: Department Name, char, required





:child_ids: Child Departments, one2many





:company_id: Company, many2one, required





:note: Note, text





:parent_id: Parent Department, many2one





:manager_id: Manager, many2one, required


