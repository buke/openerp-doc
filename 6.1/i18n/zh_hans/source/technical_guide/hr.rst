
.. i18n: .. module:: hr
.. i18n:     :synopsis: Human Resources (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: hr
    :synopsis: Human Resources (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hr"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hr"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Human Resources (*hr*)
.. i18n: ======================
.. i18n: :Module: hr
.. i18n: :Name: Human Resources
.. i18n: :Version: 5.0.1.1
.. i18n: :Author: Tiny
.. i18n: :Directory: hr
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Module for human resource management. You can manage:
.. i18n:       * Employees and hierarchies
.. i18n:       * Work hours sheets
.. i18n:       * Attendances and sign in/out system
.. i18n:   
.. i18n:       Different reports are also provided, mainly for attendance statistics.
..

::

  Module for human resource management. You can manage:
      * Employees and hierarchies
      * Work hours sheets
      * Attendances and sign in/out system
  
      Different reports are also provided, mainly for attendance statistics.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/hr.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/hr.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/hr.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/hr.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/hr.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/hr.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`process`
..

 * :mod:`base`
 * :mod:`process`

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
.. i18n:  * Human Resources/Reporting
.. i18n:  * Human Resources/Configuration
.. i18n:  * Human Resources/Employees
.. i18n:  * Human Resources/Employees/Employees Structure
.. i18n:  * Human Resources/Employees/All Employees
.. i18n:  * Human Resources/Employees/New Employee
.. i18n:  * Human Resources/Configuration/Working Time Categories
.. i18n:  * Human Resources/Configuration/Categories of Employee
.. i18n:  * Human Resources/Configuration/Categories of Employee/Categories structure
.. i18n:  * Administration/Users/Departments
.. i18n:  * Administration/Users/Departments/Departments
..

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

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * hr.employee.form (form)
.. i18n:  * hr.employee.tree (tree)
.. i18n:  * hr.employee.tree (tree)
.. i18n:  * hr.timesheet.group.form (form)
.. i18n:  * hr.timesheet.tree (tree)
.. i18n:  * hr.timesheet.form (form)
.. i18n:  * hr.employee.category.form (form)
.. i18n:  * hr.employee.category.list (tree)
.. i18n:  * hr.employee.category.tree (tree)
.. i18n:  * hr.department.form (form)
.. i18n:  * hr.department.tree (tree)
.. i18n:  * \* INHERIT res.users.form (form)
..

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

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Working Time (hr.timesheet.group)
.. i18n: #########################################
..

Object: Working Time (hr.timesheet.group)
#########################################

.. i18n: :timesheet_id: Working Time, one2many
..

:timesheet_id: Working Time, one2many

.. i18n: :manager: Workgroup manager, many2one
..

:manager: Workgroup manager, many2one

.. i18n: :name: Group name, char, required
..

:name: Group name, char, required

.. i18n: Object: Employee Category (hr.employee.category)
.. i18n: ################################################
..

Object: Employee Category (hr.employee.category)
################################################

.. i18n: :parent_id: Parent Category, many2one
..

:parent_id: Parent Category, many2one

.. i18n: :child_ids: Child Categories, one2many
..

:child_ids: Child Categories, one2many

.. i18n: :name: Category, char, required
..

:name: Category, char, required

.. i18n: Object: Employee (hr.employee)
.. i18n: ##############################
..

Object: Employee (hr.employee)
##############################

.. i18n: :company_id: Company, many2one
..

:company_id: Company, many2one

.. i18n: :otherid: Other ID, char
..

:otherid: Other ID, char

.. i18n: :country_id: Nationality, many2one
..

:country_id: Nationality, many2one

.. i18n: :user_id: Related User, many2one
..

:user_id: Related User, many2one

.. i18n: :work_location: Office Location, char
..

:work_location: Office Location, char

.. i18n: :name: Employee, char, required
..

:name: Employee, char, required

.. i18n: :parent_id: Manager, many2one
..

:parent_id: Manager, many2one

.. i18n: :work_phone: Work Phone, char
..

:work_phone: Work Phone, char

.. i18n: :gender: Gender, selection
..

:gender: Gender, selection

.. i18n: :ssnid: SSN No, char
..

:ssnid: SSN No, char

.. i18n: :child_ids: Subordinates, one2many
..

:child_ids: Subordinates, one2many

.. i18n: :address_id: Working Address, many2one
..

:address_id: Working Address, many2one

.. i18n: :marital: Marital Status, selection
..

:marital: Marital Status, selection

.. i18n: :sinid: SIN No, char
..

:sinid: SIN No, char

.. i18n: :birthday: Birthday, date
..

:birthday: Birthday, date

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :category_id: Category, many2one
..

:category_id: Category, many2one

.. i18n: :work_email: Work Email, char
..

:work_email: Work Email, char

.. i18n: :notes: Notes, text
..

:notes: Notes, text

.. i18n: :address_home_id: Home Address, many2one
..

:address_home_id: Home Address, many2one

.. i18n: Object: Timesheet Line (hr.timesheet)
.. i18n: #####################################
..

Object: Timesheet Line (hr.timesheet)
#####################################

.. i18n: :dayofweek: Day of week, selection
..

:dayofweek: Day of week, selection

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :tgroup_id: Employee's timesheet group, many2one
..

:tgroup_id: Employee's timesheet group, many2one

.. i18n: :date_from: Starting date, date
..

:date_from: Starting date, date

.. i18n: :hour_from: Work from, float, required
..

:hour_from: Work from, float, required

.. i18n: :hour_to: Work to, float, required
..

:hour_to: Work to, float, required

.. i18n: Object: hr.department (hr.department)
.. i18n: #####################################
..

Object: hr.department (hr.department)
#####################################

.. i18n: :member_ids: Members, many2many
..

:member_ids: Members, many2many

.. i18n: :name: Department Name, char, required
..

:name: Department Name, char, required

.. i18n: :child_ids: Child Departments, one2many
..

:child_ids: Child Departments, one2many

.. i18n: :company_id: Company, many2one, required
..

:company_id: Company, many2one, required

.. i18n: :note: Note, text
..

:note: Note, text

.. i18n: :parent_id: Parent Department, many2one
..

:parent_id: Parent Department, many2one

.. i18n: :manager_id: Manager, many2one, required
..

:manager_id: Manager, many2one, required
