
.. module:: crm_configuration
    :synopsis: Customer Relationship Management (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/crm_configuration"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Customer Relationship Management (*crm_configuration*)
======================================================
:Module: crm_configuration
:Name: Customer Relationship Management
:Version: 5.0.1.0
:Author: Tiny
:Directory: crm_configuration
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  The OpenERP case and request tracker enables a group of
  people to intelligently and efficiently manage tasks, issues,
  and requests. It manages key tasks such as communication, 
  identification, prioritization, assignment, resolution and notification.
  
  This module provide screens like: jobs hiring process, leads, business
  opportunities, fund raising tracking, support & helpdesk, calendar of
  meetings, eso.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/crm_configuration.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/crm_configuration.zip>`_


Dependencies
------------

 * :mod:`crm`
 * :mod:`report_crm`
 * :mod:`process`

Reports
-------

None


Menus
-------

 * CRM & SRM/Configuration/Cases/Stages
 * CRM & SRM/Reporting/This Month/Cases by Section and Type
 * CRM & SRM/Reporting/All Months/Cases by Section and Type
 * CRM & SRM/Reporting/This Month/Cases by Section and Stage
 * CRM & SRM/Reporting/All Months/Cases by Section and Stage
 * CRM & SRM/Reporting/This Month/Cases by Section, Category and Stage
 * CRM & SRM/Reporting/All Months/Cases by Section, Category and Stage
 * CRM & SRM/Reporting/This Month/Cases by Section, Category and Type
 * CRM & SRM/Reporting/All Months/Cases by Section, Category and Type

Views
-----

 * Configure Menu for Sections (form)
 * CRM -Graph (graph)
 * crm.case.stage.tree (tree)
 * crm.case.stage.form (form)
 * CRM - Bug Tracker Form (form)
 * CRM - Bug Tracker Tree (tree)
 * CRM - Bug Tracker Calendar (calendar)
 * CRM - Jobs Requests Tree (tree)
 * CRM - Jobs Requests Form (form)
 * CRM - Jobs Requests Calendar (calendar)
 * CRM - Leads Form (form)
 * CRM - Leads Tree (tree)
 * CRM - Leads Calendar (calendar)
 * CRM - Meetings Form (form)
 * CRM - Meetings Tree (tree)
 * CRM - Meetings Calendar (calendar)
 * CRM - Opportunities Form (form)
 * CRM - Opportunities Tree (tree)
 * CRM - Opportunities Calendar (calendar)
 * CRM - Funds Tree (tree)
 * CRM - Funds Form (form)
 * CRM - Funds Calendar (calendar)
 * CRM - Funds Graph (graph)
 * CRM - Claims Tree (tree)
 * CRM - Claims Form (form)
 * CRM - Claims Calendar (calendar)
 * CRM - Phone Calls Tree (tree)
 * CRM - Phone Call Form (form)
 * CRM - Phone Calls Calendar (calendar)
 * CRM Report - Sections and Type(Tree) (tree)
 * CRM Report - Sections and Type(Form) (form)
 * CRM Report - Sections and Type(Graph) (graph)
 * CRM Report - Sections and Stage(Tree) (tree)
 * CRM Report - Sections and Stage(Form) (form)
 * CRM Report - Sections and Stage(Graph) (graph)
 * CRM Report - Section, Category and Stage(Tree) (tree)
 * CRM Report - Section, Category and Stage(Form) (form)
 * CRM Report - Section, Category and Type(Tree) (tree)
 * CRM Report - Section, Category and Type(Form) (form)


Objects
-------

Object: Category2 of case (crm.case.category2)
##############################################



:name: Case Category2 Name, char, required





:section_id: Case Section, many2one




Object: Stage of case (crm.case.stage)
######################################



:sequence: Sequence, integer





:section_id: Case Section, many2one





:name: Stage Name, char, required




Object: crm.menu.config_wizard (crm.menu.config_wizard)
#######################################################



:jobs: Jobs Hiring Process, boolean

    *Help you to organise the jobs hiring process: evaluation, meetings, email integration...*



:name: Name, char





:lead: Leads, boolean

    *Allows you to track and manage leads which are pre-sales requests or contacts, the very first contact with a customer request.*



:document_ics: Shared Calendar, boolean

    *Will allow you to synchronise your OpenERP calendars with your phone, outlook, Sunbird, ical, ...*



:helpdesk: Helpdesk, boolean

    *Manages an Helpdesk service.*



:phonecall: Phone Calls, boolean

    *Help you to encode the result of a phone call or to plan a list of phone calls to process.*



:bugs: Bug Tracking, boolean

    *Used by companies to track bugs and support requests on software*



:fund: Fund Raising Operations, boolean

    *This may help associations in their fund raising process and tracking.*



:meeting: Calendar of Meetings, boolean

    *Manages the calendar of meetings of the users.*



:claims: Claims, boolean

    *Manages the supplier and customers claims, including your corrective or preventive actions.*



:opportunity: Business Opportunities, boolean

    *Tracks identified business opportunities for your sales pipeline.*


Object: Cases by section and category2 (report.crm.case.section.categ2)
#######################################################################



:stage_id: Stage, many2one, readonly





:user_id: User, many2one, readonly





:name: Month, date, readonly





:nbr: # of Cases, integer, readonly





:section_id: Section, many2one, readonly





:state: State, selection, readonly





:amount_revenue: Est.Revenue, float, readonly





:category2_id: Type, many2one, readonly





:delay_close: Delay Close, char, readonly




Object: Cases by section and stage (report.crm.case.section.stage)
##################################################################



:stage_id: Stage, many2one, readonly





:user_id: User, many2one, readonly





:name: Month, date, readonly





:nbr: # of Cases, integer, readonly





:section_id: Section, many2one, readonly





:state: State, selection, readonly





:amount_revenue: Est.Revenue, float, readonly





:delay_close: Delay Close, char, readonly





:categ_id: Category, many2one, readonly




Object: Cases by section, Category and stage (report.crm.case.section.categ.stage)
##################################################################################



:stage_id: Stage, many2one, readonly





:user_id: User, many2one, readonly





:name: Month, date, readonly





:nbr: # of Cases, integer, readonly





:section_id: Section, many2one, readonly





:state: State, selection, readonly





:delay_close: Delay Close, char, readonly





:categ_id: Category, many2one, readonly




Object: Cases by section, Category and Category2 (report.crm.case.section.categ.categ2)
#######################################################################################



:stage_id: Stage, many2one, readonly





:user_id: User, many2one, readonly





:name: Month, date, readonly





:nbr: # of Cases, integer, readonly





:section_id: Section, many2one, readonly





:state: State, selection, readonly





:category2_id: Type, many2one, readonly





:delay_close: Delay Close, char, readonly





:categ_id: Category, many2one, readonly


