
.. module:: hr_holidays_request
    :synopsis: HR Holiday Request 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hr_holidays_request"></div>
    <script src="http://js-kit.com/ratings.js"></script>

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

Description
-----------

::

  None

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/hr_holidays_request.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/hr_holidays_request.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`hr`
 * :mod:`hr_holidays`

Reports
-------

 * Holidays Report

 * Holidays Report Form

Menus
-------

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

Views
-----

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


Objects
-------

Object: Holidays history (hr.holidays.history)
##############################################



:employee_id: Employee, many2one, readonly





:user_id: Employee_id, many2one, readonly





:name: Description, char, readonly





:date_to1: To, date, readonly





:notes: Notes, text, readonly





:date_from1: From, date, readonly





:contactno: Contact no, char, readonly





:state: State, selection, readonly





:total_full: Total Full Leave, integer, readonly





:manager_id: Holiday manager, many2one, readonly





:holiday_id: Holiday's days list, one2many, readonly





:total_hour: Total Hours, integer, readonly





:total_half: Total Half Leave, integer, readonly





:validated_id: Validated By, many2one, readonly




Object: Holidays history (days.holidays.days)
#############################################



:date1: Date, date, required, readonly





:user_id: User_id, many2one, readonly





:name: Date, char





:public_h: Public Holiday, boolean, readonly





:state: State, selection, readonly





:hourly_leave: Hourly Leave, float, readonly





:holiday_id: Holiday Ref, many2one





:half_day: Half Leave, boolean, readonly





:full_day: Full Leave, boolean, readonly





:holiday_status: Holiday's Status, many2one




Object: Public Holidays (public.holidays.days)
##############################################



:reason: Reason, text, required





:name: Date, date, required




Object: Holidays history (days.holidays.days.history)
#####################################################



:date1: Date, date, readonly





:user_id: User_id, many2one, readonly





:name: Date, char, readonly





:public_h: Public Holiday, boolean, readonly





:state: State, selection, readonly





:hourly_leave: Hourly Leave, float, readonly





:holiday_id: Holiday Ref, many2one, readonly





:half_day: Half Leave, boolean, readonly





:full_day: Full Leave, boolean, readonly





:holiday_status: Holiday's Status, selection, readonly


