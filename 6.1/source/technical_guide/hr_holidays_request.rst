
.. i18n: .. module:: hr_holidays_request
.. i18n:     :synopsis: HR Holiday Request 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: hr_holidays_request
    :synopsis: HR Holiday Request 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hr_holidays_request"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hr_holidays_request"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: HR Holiday Request (*hr_holidays_request*)
.. i18n: ==========================================
.. i18n: :Module: hr_holidays_request
.. i18n: :Name: HR Holiday Request
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny & Axelor
.. i18n: :Directory: hr_holidays_request
.. i18n: :Web: http://www.axelor.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

HR Holiday Request (*hr_holidays_request*)
==========================================
:Module: hr_holidays_request
:Name: HR Holiday Request
:Version: 5.0.1.0
:Author: Tiny & Axelor
:Directory: hr_holidays_request
:Web: http://www.axelor.com
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   None
..

::

  None

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/hr_holidays_request.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/hr_holidays_request.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/hr_holidays_request.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/hr_holidays_request.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`hr`
.. i18n:  * :mod:`hr_holidays`
..

 * :mod:`base`
 * :mod:`hr`
 * :mod:`hr_holidays`

.. i18n: Reports
.. i18n: -------
..

Reports
-------

.. i18n:  * Holidays Report
.. i18n: 
.. i18n:  * Holidays Report Form
..

 * Holidays Report

 * Holidays Report Form

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Human Resources/Holidays Request
.. i18n:  * Human Resources/Holidays Request/All Validated Holidays
.. i18n:  * Human Resources/Holidays Request/Public Holidays
.. i18n:  * Human Resources/Holidays Request/All Holidays Requests
.. i18n:  * Human Resources/Holidays Request/Holiday History
.. i18n:  * Human Resources/Holidays Request/My Holidays Request
.. i18n:  * Human Resources/Holidays Request/My Holidays Request/Draft
.. i18n:  * Human Resources/Holidays Request/My Holidays Request/Waiting confirmation
.. i18n:  * Human Resources/Holidays Request/My Holidays Request/Validated
.. i18n:  * Human Resources/Holidays Request/My Holidays Request/Refused
.. i18n:  * Human Resources/Holidays Request/My Holidays Request/Request waiting validation
.. i18n:  * Human Resources/Holidays Request/My Holidays Request/Holidays Report
..

 * Human Resources/Holidays Request
 * Human Resources/Holidays Request/All Validated Holidays
 * Human Resources/Holidays Request/Public Holidays
 * Human Resources/Holidays Request/All Holidays Requests
 * Human Resources/Holidays Request/Holiday History
 * Human Resources/Holidays Request/My Holidays Request
 * Human Resources/Holidays Request/My Holidays Request/Draft
 * Human Resources/Holidays Request/My Holidays Request/Waiting confirmation
 * Human Resources/Holidays Request/My Holidays Request/Validated
 * Human Resources/Holidays Request/My Holidays Request/Refused
 * Human Resources/Holidays Request/My Holidays Request/Request waiting validation
 * Human Resources/Holidays Request/My Holidays Request/Holidays Report

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT Holidays (form)
.. i18n:  * \* INHERIT hr.holidays.tree (tree)
.. i18n:  * holidays.days.list (tree)
.. i18n:  * Holidays_hr (form)
.. i18n:  * holidays.days.history.list (tree)
.. i18n:  * holidays.days.history.list (form)
.. i18n:  * holidays.days.list (form)
.. i18n:  * public.holidays.days.list (form)
.. i18n:  * hr.holidays.tree.2 (tree)
.. i18n:  * hr.holidays.tree.2.history (tree)
.. i18n:  * ask.holiday.history (form)
..

 * \* INHERIT Holidays (form)
 * \* INHERIT hr.holidays.tree (tree)
 * holidays.days.list (tree)
 * Holidays_hr (form)
 * holidays.days.history.list (tree)
 * holidays.days.history.list (form)
 * holidays.days.list (form)
 * public.holidays.days.list (form)
 * hr.holidays.tree.2 (tree)
 * hr.holidays.tree.2.history (tree)
 * ask.holiday.history (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Holidays history (hr.holidays.history)
.. i18n: ##############################################
..

Object: Holidays history (hr.holidays.history)
##############################################

.. i18n: :employee_id: Employee, many2one, readonly
..

:employee_id: Employee, many2one, readonly

.. i18n: :user_id: Employee_id, many2one, readonly
..

:user_id: Employee_id, many2one, readonly

.. i18n: :name: Description, char, readonly
..

:name: Description, char, readonly

.. i18n: :date_to1: To, date, readonly
..

:date_to1: To, date, readonly

.. i18n: :notes: Notes, text, readonly
..

:notes: Notes, text, readonly

.. i18n: :date_from1: From, date, readonly
..

:date_from1: From, date, readonly

.. i18n: :contactno: Contact no, char, readonly
..

:contactno: Contact no, char, readonly

.. i18n: :state: State, selection, readonly
..

:state: State, selection, readonly

.. i18n: :total_full: Total Full Leave, integer, readonly
..

:total_full: Total Full Leave, integer, readonly

.. i18n: :manager_id: Holiday manager, many2one, readonly
..

:manager_id: Holiday manager, many2one, readonly

.. i18n: :holiday_id: Holiday's days list, one2many, readonly
..

:holiday_id: Holiday's days list, one2many, readonly

.. i18n: :total_hour: Total Hours, integer, readonly
..

:total_hour: Total Hours, integer, readonly

.. i18n: :total_half: Total Half Leave, integer, readonly
..

:total_half: Total Half Leave, integer, readonly

.. i18n: :validated_id: Validated By, many2one, readonly
..

:validated_id: Validated By, many2one, readonly

.. i18n: Object: Holidays history (days.holidays.days)
.. i18n: #############################################
..

Object: Holidays history (days.holidays.days)
#############################################

.. i18n: :date1: Date, date, required, readonly
..

:date1: Date, date, required, readonly

.. i18n: :user_id: User_id, many2one, readonly
..

:user_id: User_id, many2one, readonly

.. i18n: :name: Date, char
..

:name: Date, char

.. i18n: :public_h: Public Holiday, boolean, readonly
..

:public_h: Public Holiday, boolean, readonly

.. i18n: :state: State, selection, readonly
..

:state: State, selection, readonly

.. i18n: :hourly_leave: Hourly Leave, float, readonly
..

:hourly_leave: Hourly Leave, float, readonly

.. i18n: :holiday_id: Holiday Ref, many2one
..

:holiday_id: Holiday Ref, many2one

.. i18n: :half_day: Half Leave, boolean, readonly
..

:half_day: Half Leave, boolean, readonly

.. i18n: :full_day: Full Leave, boolean, readonly
..

:full_day: Full Leave, boolean, readonly

.. i18n: :holiday_status: Holiday's Status, many2one
..

:holiday_status: Holiday's Status, many2one

.. i18n: Object: Public Holidays (public.holidays.days)
.. i18n: ##############################################
..

Object: Public Holidays (public.holidays.days)
##############################################

.. i18n: :reason: Reason, text, required
..

:reason: Reason, text, required

.. i18n: :name: Date, date, required
..

:name: Date, date, required

.. i18n: Object: Holidays history (days.holidays.days.history)
.. i18n: #####################################################
..

Object: Holidays history (days.holidays.days.history)
#####################################################

.. i18n: :date1: Date, date, readonly
..

:date1: Date, date, readonly

.. i18n: :user_id: User_id, many2one, readonly
..

:user_id: User_id, many2one, readonly

.. i18n: :name: Date, char, readonly
..

:name: Date, char, readonly

.. i18n: :public_h: Public Holiday, boolean, readonly
..

:public_h: Public Holiday, boolean, readonly

.. i18n: :state: State, selection, readonly
..

:state: State, selection, readonly

.. i18n: :hourly_leave: Hourly Leave, float, readonly
..

:hourly_leave: Hourly Leave, float, readonly

.. i18n: :holiday_id: Holiday Ref, many2one, readonly
..

:holiday_id: Holiday Ref, many2one, readonly

.. i18n: :half_day: Half Leave, boolean, readonly
..

:half_day: Half Leave, boolean, readonly

.. i18n: :full_day: Full Leave, boolean, readonly
..

:full_day: Full Leave, boolean, readonly

.. i18n: :holiday_status: Holiday's Status, selection, readonly
..

:holiday_status: Holiday's Status, selection, readonly
