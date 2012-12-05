
.. i18n: .. module:: hr_timesheet
.. i18n:     :synopsis: Human Resources (Timesheet encoding) (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: hr_timesheet
    :synopsis: Human Resources (Timesheet encoding) (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hr_timesheet"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hr_timesheet"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Human Resources (Timesheet encoding) (*hr_timesheet*)
.. i18n: =====================================================
.. i18n: :Module: hr_timesheet
.. i18n: :Name: Human Resources (Timesheet encoding)
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: hr_timesheet
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module implement a timesheet system. Each employee can encode and
.. i18n:   track their time spent on the different projects. A project is an
.. i18n:   analytic account and the time spent on a project generate costs on
.. i18n:   the analytic account.
.. i18n:   
.. i18n:   Lots of reporting on time and employee tracking are provided.
.. i18n:   
.. i18n:   It is completely integrated with the cost accounting module. It allows you
.. i18n:   to set up a management by affair.
..

::

  This module implement a timesheet system. Each employee can encode and
  track their time spent on the different projects. A project is an
  analytic account and the time spent on a project generate costs on
  the analytic account.
  
  Lots of reporting on time and employee tracking are provided.
  
  It is completely integrated with the cost accounting module. It allows you
  to set up a management by affair.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/hr_timesheet.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/hr_timesheet.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/hr_timesheet.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/hr_timesheet.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/hr_timesheet.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/hr_timesheet.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`account`
.. i18n:  * :mod:`hr`
.. i18n:  * :mod:`base`
.. i18n:  * :mod:`hr_attendance`
.. i18n:  * :mod:`process`
..

 * :mod:`account`
 * :mod:`hr`
 * :mod:`base`
 * :mod:`hr_attendance`
 * :mod:`process`

.. i18n: Reports
.. i18n: -------
..

Reports
-------

.. i18n:  * Employee timesheet
.. i18n: 
.. i18n:  * Employees Timesheet
..

 * Employee timesheet

 * Employees Timesheet

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Human Resources/Working Hours
.. i18n:  * Human Resources/Working Hours/My Working Hours
.. i18n:  * Human Resources/Working Hours/My Working Hours/My Working Hours of The Day
.. i18n:  * Human Resources/Working Hours/Working Hours
.. i18n:  * Human Resources/Working Hours/Working Hours/Working Hours of The Day
.. i18n:  * Human Resources/Reporting/Timesheet
.. i18n:  * Human Resources/Reporting/Timesheet/Employee Timesheet
.. i18n:  * Human Resources/Reporting/Timesheet/Print My Timesheet
.. i18n:  * Human Resources/Reporting/Timesheet/Employees Timesheet
.. i18n:  * Human Resources/Attendances/Sign in / Sign out by project
..

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

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * hr.analytic.timesheet.tree (tree)
.. i18n:  * hr.analytic.timesheet.form (form)
.. i18n:  * \* INHERIT hr.timesheet.employee.extd_form (form)
..

 * hr.analytic.timesheet.tree (tree)
 * hr.analytic.timesheet.form (form)
 * \* INHERIT hr.timesheet.employee.extd_form (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Timesheet line (hr.analytic.timesheet)
.. i18n: ##############################################
..

Object: Timesheet line (hr.analytic.timesheet)
##############################################

.. i18n: :code: Code, char
..

:code: Code, char

.. i18n: :user_id: User, many2one
..

:user_id: User, many2one

.. i18n: :account_id: Analytic Account, many2one, required
..

:account_id: Analytic Account, many2one, required

.. i18n: :general_account_id: General Account, many2one, required
..

:general_account_id: General Account, many2one, required

.. i18n: :product_uom_id: UoM, many2one
..

:product_uom_id: UoM, many2one

.. i18n: :journal_id: Analytic Journal, many2one, required
..

:journal_id: Analytic Journal, many2one, required

.. i18n: :name: Description, char, required
..

:name: Description, char, required

.. i18n: :line_id: Analytic line, many2one
..

:line_id: Analytic line, many2one

.. i18n: :amount: Amount, float, required
..

:amount: Amount, float, required

.. i18n: :unit_amount: Quantity, float
..

:unit_amount: Quantity, float

.. i18n: :date: Date, date, required
..

:date: Date, date, required

.. i18n: :ref: Ref., char
..

:ref: Ref., char

.. i18n: :move_id: Move Line, many2one
..

:move_id: Move Line, many2one

.. i18n: :product_id: Product, many2one
..

:product_id: Product, many2one
