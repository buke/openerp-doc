
.. module:: document_ics
    :synopsis: Support for iCal based on Document Management System (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/document_ics"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Support for iCal based on Document Management System (*document_ics*)
=====================================================================
:Module: document_ics
:Name: Support for iCal based on Document Management System
:Version: 5.0.1.0
:Author: Tiny
:Directory: document_ics
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  Allows to synchronise calendars with others applications.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/document_ics.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/document_ics.zip>`_


Dependencies
------------

 * :mod:`document`
 * :mod:`crm_configuration`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT document.directory (form)
 * \* INHERIT crm.case.code.form (form)
 * \* INHERIT crm.case.inherit.form1 (form)
 * Configure Calendars for Sections (form)


Objects
-------

Object: document.directory.ics.fields (document.directory.ics.fields)
#####################################################################



:content_id: Content, many2one, required





:field_id: OpenERP Field, many2one, required





:name: ICS Value, selection, required




Object: document.ics.crm.wizard (document.ics.crm.wizard)
#########################################################



:jobs: Jobs Hiring Process, boolean

    *Help you to organise the jobs hiring process: evaluation, meetings, email integration...*



:name: Name, char





:lead: Prospect, boolean

    *Allows you to track and manage prospects which are pre-sales requests or contacts, the very first contact with a customer request.*



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
