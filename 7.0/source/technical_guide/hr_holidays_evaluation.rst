
.. module:: hr_holidays_evaluation
    :synopsis: Hr holidays evaluation 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hr_holidays_evaluation"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Hr holidays evaluation (*hr_holidays_evaluation*)
=================================================
:Module: hr_holidays_evaluation
:Name: Hr holidays evaluation
:Version: 5.0.1.0
:Author: Tiny
:Directory: hr_holidays_evaluation
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Computation of holidays for employee

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/hr_holidays_evaluation.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/hr_holidays_evaluation.zip>`_


Dependencies
------------

 * :mod:`hr_holidays`
 * :mod:`hr_contract`
 * :mod:`hr_attendance`

Reports
-------

None


Menus
-------

 * Human Resources/Holidays Management/Holidays Evaluation
 * Human Resources/Holidays Management/Holidays Evaluation/Count Holiday For Employee

Views
-----

 * Notes (form)
 * Notes (tree)
 * \* INHERIT hr.holidays.per.user.form.inherited (form)
 * Holidays Evaluation Wizard (form)


Objects
-------

Object: Holidays note (hr.holidays.note)
########################################



:employee_id: Employee Name, many2one





:prev_number: Previous Holiday Number, float





:holiday_per_user_id: Holiday Status, many2one, required





:date: Date, char, required





:diff: Difference, float, readonly





:new_number: New Holiday Number, float, required




Object: wizard.hr.holidays.evaluation (wizard.hr.holidays.evaluation)
#####################################################################



:hr_timesheet_group_id: Timesheet Group, many2one, required

    *This field allow you to filter on only the employees that have a contract using this working hour.*



:float_time: Time, float, required

    *This time depicts the amount per day earned by an employee working a day. The computation is: total earned = time * number of working days*



:holiday_status_id: Holiday Status, many2one, required

    *This is where you specify the holiday type to synchronize. It will create the "holidays per employee" accordingly if necessary, or replace the value "Max leaves allowed" into the existing one.*



:date_current: Date, date

    *This field allow you to choose the date to use, for forecast matter e.g*
