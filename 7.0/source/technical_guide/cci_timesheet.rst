
.. module:: cci_timesheet
    :synopsis: CCI Timesheet 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/cci_timesheet"></div>
    <script src="http://js-kit.com/ratings.js"></script>

CCI Timesheet (*cci_timesheet*)
===============================
:Module: cci_timesheet
:Name: CCI Timesheet
:Version: 5.0.1.0
:Author: Tiny
:Directory: cci_timesheet
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  A Customised timesheet module.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/cci_timesheet.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/cci_timesheet.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`cci_partner`
 * :mod:`cci_crm`
 * :mod:`cci_base_contact`

Reports
-------

None


Menus
-------

 * Timesheet
 * Timesheet/Configuration
 * Timesheet/Timesheet
 * Timesheet/Configuration/Grant
 * Timesheet/Timesheet/Timesheet
 * Timesheet/Timesheet/Timesheet Lines
 * Timesheet/Timesheet/Timesheet Affectation
 * Timesheet/Reporting
 * Timesheet/Reporting/Timesheets per Employee
 * Timesheet/Create Timesheet Lines

Views
-----

 * cci_timesheet.grant.form (form)
 * cci_timesheet.grant.tree (tree)
 * cci_timesheet.form (form)
 * cci_timesheet.tree (tree)
 * cci_timesheet.line.form (form)
 * cci_timesheet.line.tree (tree)
 * cci_timesheet.affectation.form (form)
 * cci_timesheet.affectation.tree (tree)
 * Timesheets per Employee (Tree) (tree)
 * Timesheets per Employee (Form) (form)
 * Timesheets per Employee (Graph) (graph)
 * \* INHERIT crm.case.form.confidential2 (form)
 * \* INHERIT crm.case.form.confidential3 (form)
 * \* INHERIT project.task.work.form (form)
 * \* INHERIT project.task.work.form1 (form)
 * \* INHERIT project.task.work.tree (tree)


Objects
-------

Object: CCI Timesheet Grant (cci_timesheet.grant)
#################################################



:line_ids: Timesheet Lines, one2many





:affectation_ids: Affectation Lines, one2many





:name: Grant Name, char, required




Object: CCI Timesheet (cci.timesheet)
#####################################



:name: Name, char, required, readonly





:date_from: From Date, date, required





:sending_date: Sending Date, date





:asked_amount: Asked Amount, float





:state: State, selection, required, readonly





:date_to: To Date, date, required





:line_ids: Timesheet Lines, one2many





:grant_id: Grant, many2one, required, readonly





:accepted_amount: Accepted Amount, float




Object: CCI Timesheet Line (cci_timesheet.line)
###############################################



:suppl_cost: Supplementary Cost, float





:user_id: User, many2one, required





:description: Description, text





:diff_hours: Hour To - Hour From, float, readonly





:zip_id: Zip, many2one





:grant_id: Grant, many2one





:contact_id: Contact, many2one





:day_date: Date of the Day, date, required





:hour_from: Hour From, float, required





:hour_to: Hour To, float, required





:timesheet_id: Timesheet, many2one





:kms: Kilometers, integer





:partner_id: Partner, many2one





:name: Name, char, required




Object: Timesheet Affectation (cci_timesheet.affectation)
#########################################################



:hours_per_week: Hours Per Week, float, required





:user_id: User, many2one, required





:name: Name, char, required





:grant_id: Grant, many2one, required





:rate: Rate, float, required





:date_to: To Date, date, required





:percentage: Percentage, float, required





:date_from: From Date, date, required




Object: Report on Timesheet and Affectation (report.timesheet.affectation)
##########################################################################



:hours_per_week: Hours Per Week, float





:description: Description, text





:diff_hours: Hours, float





:date_from: From Date, date





:th_percentage: Percentage, float





:affectation_name: Affectation, char





:day_date: Date of the Day, date





:rate: Rate, float





:hour_from: Hour From, float





:hour_to: Hour To, float





:date_to: To Date, date





:timesheet_id: Timesheet Ref, integer





:grant_name: Grant, char





:user_name: Employee, char





:name: Name, char


