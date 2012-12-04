
.. module:: hr_timesheet
    :synopsis: Human Resources (Timesheet encoding) (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hr_timesheet"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Human Resources (Timesheet encoding) (*hr_timesheet*)
=====================================================
:Module: hr_timesheet
:Name: Human Resources (Timesheet encoding)
:Version: 5.0.1.0
:Author: Tiny
:Directory: hr_timesheet
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  This module implement a timesheet system. Each employee can encode and
  track their time spent on the different projects. A project is an
  analytic account and the time spent on a project generate costs on
  the analytic account.
  
  Lots of reporting on time and employee tracking are provided.
  
  It is completely integrated with the cost accounting module. It allows you
  to set up a management by affair.

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/hr_timesheet.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/hr_timesheet.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/hr_timesheet.zip>`_


Dependencies
------------

 * :mod:`account`
 * :mod:`hr`
 * :mod:`base`
 * :mod:`hr_attendance`
 * :mod:`process`

Reports
-------

 * Employee timesheet

 * Employees Timesheet

Menus
-------

 * Human Resources/Working Hours
 * Human Resources/Working Hours/My Working Hours
 * Human Resources/Working Hours/My Working Hours/My Working Hours of The Day
 * Human Resources/Working Hours/Working Hours
 * Human Resources/Working Hours/Working Hours/Working Hours of The Day
 * Human Resources/Reporting/Timesheet
 * Human Resources/Reporting/Timesheet/Employee Timesheet
 * Human Resources/Reporting/Timesheet/Print My Timesheet
 * Human Resources/Reporting/Timesheet/Employees Timesheet
 * Human Resources/Attendances/Sign in / Sign out by project

Views
-----

 * hr.analytic.timesheet.tree (tree)
 * hr.analytic.timesheet.form (form)
 * \* INHERIT hr.timesheet.employee.extd_form (form)


Objects
-------

Object: Timesheet line (hr.analytic.timesheet)
##############################################



:code: Code, char





:user_id: User, many2one





:account_id: Analytic Account, many2one, required





:general_account_id: General Account, many2one, required





:product_uom_id: UoM, many2one





:journal_id: Analytic Journal, many2one, required





:name: Description, char, required





:line_id: Analytic line, many2one





:amount: Amount, float, required





:unit_amount: Quantity, float





:date: Date, date, required





:ref: Ref., char





:move_id: Move Line, many2one





:product_id: Product, many2one


