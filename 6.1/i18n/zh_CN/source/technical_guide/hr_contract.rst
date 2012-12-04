
.. i18n: .. module:: hr_contract
.. i18n:     :synopsis: Human Resources Contracts (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: hr_contract
    :synopsis: Human Resources Contracts (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hr_contract"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hr_contract"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Human Resources Contracts (*hr_contract*)
.. i18n: =========================================
.. i18n: :Module: hr_contract
.. i18n: :Name: Human Resources Contracts
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: hr_contract
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Add all information on the employee form to manage contracts:
.. i18n:       * Martial status,
.. i18n:       * Security number,
.. i18n:       * Place of birth, birth date, ...
.. i18n:   
.. i18n:       You can assign several contracts per employee.
..

::

  Add all information on the employee form to manage contracts:
      * Martial status,
      * Security number,
      * Place of birth, birth date, ...
  
      You can assign several contracts per employee.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/hr_contract.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/hr_contract.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/hr_contract.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/hr_contract.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/hr_contract.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/hr_contract.zip>`_

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

.. i18n:  * Human Resources/Configuration/Contract
.. i18n:  * Human Resources/Configuration/Contract/Contract Wage Type
.. i18n:  * Human Resources/Configuration/Contract/Wage period
.. i18n:  * Human Resources/Configuration/Marital Status
.. i18n:  * Human Resources/Contract
..

 * Human Resources/Configuration/Contract
 * Human Resources/Configuration/Contract/Contract Wage Type
 * Human Resources/Configuration/Contract/Wage period
 * Human Resources/Configuration/Marital Status
 * Human Resources/Contract

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * hr.contract.wage.type.period.view.form (form)
.. i18n:  * hr.hr.employee.marital.status (form)
.. i18n:  * hr.contract.wage.type.view.form (form)
.. i18n:  * hr.contract.wage.type.view.tree (tree)
.. i18n:  * \* INHERIT hr.hr.employee.view.form2 (form)
.. i18n:  * hr.contract.type.view.form (form)
.. i18n:  * hr.contract.view.form (form)
.. i18n:  * hr.contract.type.view.tree (tree)
.. i18n:  * hr.contract.view.tree (tree)
..

 * hr.contract.wage.type.period.view.form (form)
 * hr.hr.employee.marital.status (form)
 * hr.contract.wage.type.view.form (form)
 * hr.contract.wage.type.view.tree (tree)
 * \* INHERIT hr.hr.employee.view.form2 (form)
 * hr.contract.type.view.form (form)
 * hr.contract.view.form (form)
 * hr.contract.type.view.tree (tree)
 * hr.contract.view.tree (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Employee Marital Status (hr.employee.marital.status)
.. i18n: ############################################################
..

Object: Employee Marital Status (hr.employee.marital.status)
############################################################

.. i18n: :name: Marital Status, char, required
..

:name: Marital Status, char, required

.. i18n: :description: Status Description, text
..

:description: Status Description, text

.. i18n: Object: Wage Period (hr.contract.wage.type.period)
.. i18n: ##################################################
..

Object: Wage Period (hr.contract.wage.type.period)
##################################################

.. i18n: :name: Period Name, char, required
..

:name: Period Name, char, required

.. i18n: :factor_days: Hours in the period, float, required
..

:factor_days: Hours in the period, float, required

.. i18n:     *This field is used by the timesheet system to compute the price of an hour of work based on the contract of the employee*
..

    *This field is used by the timesheet system to compute the price of an hour of work based on the contract of the employee*

.. i18n: Object: Wage Type (hr.contract.wage.type)
.. i18n: #########################################
..

Object: Wage Type (hr.contract.wage.type)
#########################################

.. i18n: :type: Type, selection, required
..

:type: Type, selection, required

.. i18n: :period_id: Wage Period, many2one, required
..

:period_id: Wage Period, many2one, required

.. i18n: :name: Wage Type Name, char, required
..

:name: Wage Type Name, char, required

.. i18n: :factor_type: Factor for hour cost, float, required
..

:factor_type: Factor for hour cost, float, required

.. i18n:     *This field is used by the timesheet system to compute the price of an hour of work based on the contract of the employee*
..

    *This field is used by the timesheet system to compute the price of an hour of work based on the contract of the employee*

.. i18n: Object: Contract (hr.contract)
.. i18n: ##############################
..

Object: Contract (hr.contract)
##############################

.. i18n: :function: Function, many2one
..

:function: Function, many2one

.. i18n: :wage_type_id: Wage Type, many2one, required
..

:wage_type_id: Wage Type, many2one, required

.. i18n: :employee_id: Employee, many2one, required
..

:employee_id: Employee, many2one, required

.. i18n: :name: Contract Name, char, required
..

:name: Contract Name, char, required

.. i18n: :date_end: End Date, date
..

:date_end: End Date, date

.. i18n: :date_start: Start Date, date, required
..

:date_start: Start Date, date, required

.. i18n: :wage: Wage, float, required
..

:wage: Wage, float, required

.. i18n: :notes: Notes, text
..

:notes: Notes, text

.. i18n: :working_hours_per_day: Working hours per day, integer
..

:working_hours_per_day: Working hours per day, integer
