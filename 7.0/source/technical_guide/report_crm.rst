
.. module:: report_crm
    :synopsis: CRM Management - Reporting (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_crm"></div>
    <script src="http://js-kit.com/ratings.js"></script>

CRM Management - Reporting (*report_crm*)
=========================================
:Module: report_crm
:Name: CRM Management - Reporting
:Version: 5.0.1.0
:Author: Tiny
:Directory: report_crm
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  A module that adds new reports based on CRM cases.
      Case By section, Case By category

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/report_crm.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/report_crm.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/report_crm.zip>`_


Dependencies
------------

 * :mod:`crm`

Reports
-------

None


Menus
-------

 * CRM & SRM/Reporting
 * CRM & SRM/Reporting/This Month
 * CRM & SRM/Reporting/This Month/Cases by user and section (this month)
 * CRM & SRM/Reporting/All Months
 * CRM & SRM/Reporting/All Months/Cases by User and Section
 * CRM & SRM/Reporting/This Month/My cases by section (this month)
 * CRM & SRM/Reporting/All Months/My cases by section
 * CRM & SRM/Reporting/This Month/Cases by categories and section (this month)
 * CRM & SRM/Reporting/All Months/Cases by Categories and Section

Views
-----

 * report.crm.case.user.tree (tree)
 * report.crm.case.user.form (form)
 * report.crm.case.user.graph (graph)
 * report.crm.case.categ.tree (tree)
 * report.crm.case.categ.form (form)
 * report.crm.case.section.tree (tree)
 * report.crm.case.section.graph (graph)
 * report.crm.case.service.dashboard.tree (tree)
 * report.crm.case.service.dashboard.tree (tree)


Objects
-------

Object: Cases by user and section (report.crm.case.user)
########################################################



:amount_revenue_prob: Est. Rev*Prob., float, readonly





:amount_costs: Est.Cost, float, readonly





:user_id: User, many2one, readonly





:name: Month, date, readonly





:probability: Avg. Probability, float, readonly





:nbr: # of Cases, integer, readonly





:section_id: Section, many2one, readonly





:state: Status, selection, readonly





:amount_revenue: Est.Revenue, float, readonly





:delay_close: Delay to close, char, readonly




Object: Cases by section and category (report.crm.case.categ)
#############################################################



:amount_revenue_prob: Est. Rev*Prob., float, readonly





:amount_costs: Est.Cost, float, readonly





:name: Month, date, readonly





:probability: Avg. Probability, float, readonly





:nbr: # of Cases, integer, readonly





:section_id: Section, many2one, readonly





:state: Status, selection, readonly





:amount_revenue: Est.Revenue, float, readonly





:delay_close: Delay Close, char, readonly





:categ_id: Category, many2one, readonly




Object: Cases by Section (report.crm.case.section)
##################################################



:nbr_cases: # of Cases, integer, readonly





:delay_close: Delay to close, char, readonly





:section_id: Section, many2one, readonly





:perc_cancel: %Cancel, float, readonly





:avg_answers: Avg. Answers, integer, readonly





:perc_done: %Done, float, readonly





:name: Month, date, readonly




Object: Report of Closed and Open CRM Cases within past 15 days (report.crm.case.service.dashboard)
###################################################################################################



:date_closed: Date Closed, datetime, readonly





:create_date: Create Date, datetime, readonly





:name: Description, char, readonly





:date_deadline: Deadline, datetime, readonly





:planned_revenue: Planned Revenue, float, readonly





:planned_cost: Planned Costs, float, readonly





:priority: Priority, char, readonly





:state: Status, selection, readonly





:date: Date, datetime, readonly





:user_id: Responsible, many2one, readonly





:partner_id: Partner, many2one, readonly


