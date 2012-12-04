
.. module:: hr_contract
    :synopsis: Human Resources Contracts (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hr_contract"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Human Resources Contracts (*hr_contract*)
=========================================
:Module: hr_contract
:Name: Human Resources Contracts
:Version: 5.0.1.0
:Author: Tiny
:Directory: hr_contract
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  Add all information on the employee form to manage contracts:
      * Martial status,
      * Security number,
      * Place of birth, birth date, ...
  
      You can assign several contracts per employee.

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/hr_contract.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/hr_contract.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/hr_contract.zip>`_


Dependencies
------------

 * :mod:`hr`

Reports
-------

None


Menus
-------

 * Human Resources/Configuration/Contract
 * Human Resources/Configuration/Contract/Contract Wage Type
 * Human Resources/Configuration/Contract/Wage period
 * Human Resources/Configuration/Marital Status
 * Human Resources/Contract

Views
-----

 * hr.contract.wage.type.period.view.form (form)
 * hr.hr.employee.marital.status (form)
 * hr.contract.wage.type.view.form (form)
 * hr.contract.wage.type.view.tree (tree)
 * \* INHERIT hr.hr.employee.view.form2 (form)
 * hr.contract.type.view.form (form)
 * hr.contract.view.form (form)
 * hr.contract.type.view.tree (tree)
 * hr.contract.view.tree (tree)


Objects
-------

Object: Employee Marital Status (hr.employee.marital.status)
############################################################



:name: Marital Status, char, required





:description: Status Description, text




Object: Wage Period (hr.contract.wage.type.period)
##################################################



:name: Period Name, char, required





:factor_days: Hours in the period, float, required

    *This field is used by the timesheet system to compute the price of an hour of work based on the contract of the employee*


Object: Wage Type (hr.contract.wage.type)
#########################################



:type: Type, selection, required





:period_id: Wage Period, many2one, required





:name: Wage Type Name, char, required





:factor_type: Factor for hour cost, float, required

    *This field is used by the timesheet system to compute the price of an hour of work based on the contract of the employee*


Object: Contract (hr.contract)
##############################



:function: Function, many2one





:wage_type_id: Wage Type, many2one, required





:employee_id: Employee, many2one, required





:name: Contract Name, char, required





:date_end: End Date, date





:date_start: Start Date, date, required





:wage: Wage, float, required





:notes: Notes, text





:working_hours_per_day: Working hours per day, integer


