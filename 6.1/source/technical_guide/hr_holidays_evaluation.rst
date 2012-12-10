
.. i18n: .. module:: hr_holidays_evaluation
.. i18n:     :synopsis: Hr holidays evaluation 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: hr_holidays_evaluation
    :synopsis: Hr holidays evaluation 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hr_holidays_evaluation"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hr_holidays_evaluation"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Hr holidays evaluation (*hr_holidays_evaluation*)
.. i18n: =================================================
.. i18n: :Module: hr_holidays_evaluation
.. i18n: :Name: Hr holidays evaluation
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: hr_holidays_evaluation
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Computation of holidays for employee
..

::

  Computation of holidays for employee

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/hr_holidays_evaluation.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/hr_holidays_evaluation.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/hr_holidays_evaluation.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/hr_holidays_evaluation.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`hr_holidays`
.. i18n:  * :mod:`hr_contract`
.. i18n:  * :mod:`hr_attendance`
..

 * :mod:`hr_holidays`
 * :mod:`hr_contract`
 * :mod:`hr_attendance`

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

.. i18n:  * Human Resources/Holidays Management/Holidays Evaluation
.. i18n:  * Human Resources/Holidays Management/Holidays Evaluation/Count Holiday For Employee
..

 * Human Resources/Holidays Management/Holidays Evaluation
 * Human Resources/Holidays Management/Holidays Evaluation/Count Holiday For Employee

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * Notes (form)
.. i18n:  * Notes (tree)
.. i18n:  * \* INHERIT hr.holidays.per.user.form.inherited (form)
.. i18n:  * Holidays Evaluation Wizard (form)
..

 * Notes (form)
 * Notes (tree)
 * \* INHERIT hr.holidays.per.user.form.inherited (form)
 * Holidays Evaluation Wizard (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Holidays note (hr.holidays.note)
.. i18n: ########################################
..

Object: Holidays note (hr.holidays.note)
########################################

.. i18n: :employee_id: Employee Name, many2one
..

:employee_id: Employee Name, many2one

.. i18n: :prev_number: Previous Holiday Number, float
..

:prev_number: Previous Holiday Number, float

.. i18n: :holiday_per_user_id: Holiday Status, many2one, required
..

:holiday_per_user_id: Holiday Status, many2one, required

.. i18n: :date: Date, char, required
..

:date: Date, char, required

.. i18n: :diff: Difference, float, readonly
..

:diff: Difference, float, readonly

.. i18n: :new_number: New Holiday Number, float, required
..

:new_number: New Holiday Number, float, required

.. i18n: Object: wizard.hr.holidays.evaluation (wizard.hr.holidays.evaluation)
.. i18n: #####################################################################
..

Object: wizard.hr.holidays.evaluation (wizard.hr.holidays.evaluation)
#####################################################################

.. i18n: :hr_timesheet_group_id: Timesheet Group, many2one, required
..

:hr_timesheet_group_id: Timesheet Group, many2one, required

.. i18n:     *This field allow you to filter on only the employees that have a contract using this working hour.*
..

    *This field allow you to filter on only the employees that have a contract using this working hour.*

.. i18n: :float_time: Time, float, required
..

:float_time: Time, float, required

.. i18n:     *This time depicts the amount per day earned by an employee working a day. The computation is: total earned = time * number of working days*
..

    *This time depicts the amount per day earned by an employee working a day. The computation is: total earned = time * number of working days*

.. i18n: :holiday_status_id: Holiday Status, many2one, required
..

:holiday_status_id: Holiday Status, many2one, required

.. i18n:     *This is where you specify the holiday type to synchronize. It will create the "holidays per employee" accordingly if necessary, or replace the value "Max leaves allowed" into the existing one.*
..

    *This is where you specify the holiday type to synchronize. It will create the "holidays per employee" accordingly if necessary, or replace the value "Max leaves allowed" into the existing one.*

.. i18n: :date_current: Date, date
..

:date_current: Date, date

.. i18n:     *This field allow you to choose the date to use, for forecast matter e.g*
..

    *This field allow you to choose the date to use, for forecast matter e.g*
