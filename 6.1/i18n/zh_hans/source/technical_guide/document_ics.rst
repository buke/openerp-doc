
.. i18n: .. module:: document_ics
.. i18n:     :synopsis: Support for iCal based on Document Management System (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: document_ics
    :synopsis: Support for iCal based on Document Management System (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/document_ics"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/document_ics"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Support for iCal based on Document Management System (*document_ics*)
.. i18n: =====================================================================
.. i18n: :Module: document_ics
.. i18n: :Name: Support for iCal based on Document Management System
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: document_ics
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Allows to synchronise calendars with others applications.
..

::

  Allows to synchronise calendars with others applications.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/document_ics.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/document_ics.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/document_ics.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/document_ics.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`document`
.. i18n:  * :mod:`crm_configuration`
..

 * :mod:`document`
 * :mod:`crm_configuration`

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

.. i18n: None
..

None

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT document.directory (form)
.. i18n:  * \* INHERIT crm.case.code.form (form)
.. i18n:  * \* INHERIT crm.case.inherit.form1 (form)
.. i18n:  * Configure Calendars for Sections (form)
..

 * \* INHERIT document.directory (form)
 * \* INHERIT crm.case.code.form (form)
 * \* INHERIT crm.case.inherit.form1 (form)
 * Configure Calendars for Sections (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: document.directory.ics.fields (document.directory.ics.fields)
.. i18n: #####################################################################
..

Object: document.directory.ics.fields (document.directory.ics.fields)
#####################################################################

.. i18n: :content_id: Content, many2one, required
..

:content_id: Content, many2one, required

.. i18n: :field_id: OpenERP Field, many2one, required
..

:field_id: OpenERP Field, many2one, required

.. i18n: :name: ICS Value, selection, required
..

:name: ICS Value, selection, required

.. i18n: Object: document.ics.crm.wizard (document.ics.crm.wizard)
.. i18n: #########################################################
..

Object: document.ics.crm.wizard (document.ics.crm.wizard)
#########################################################

.. i18n: :jobs: Jobs Hiring Process, boolean
..

:jobs: Jobs Hiring Process, boolean

.. i18n:     *Help you to organise the jobs hiring process: evaluation, meetings, email integration...*
..

    *Help you to organise the jobs hiring process: evaluation, meetings, email integration...*

.. i18n: :name: Name, char
..

:name: Name, char

.. i18n: :lead: Prospect, boolean
..

:lead: Prospect, boolean

.. i18n:     *Allows you to track and manage prospects which are pre-sales requests or contacts, the very first contact with a customer request.*
..

    *Allows you to track and manage prospects which are pre-sales requests or contacts, the very first contact with a customer request.*

.. i18n: :document_ics: Shared Calendar, boolean
..

:document_ics: Shared Calendar, boolean

.. i18n:     *Will allow you to synchronise your OpenERP calendars with your phone, outlook, Sunbird, ical, ...*
..

    *Will allow you to synchronise your OpenERP calendars with your phone, outlook, Sunbird, ical, ...*

.. i18n: :helpdesk: Helpdesk, boolean
..

:helpdesk: Helpdesk, boolean

.. i18n:     *Manages an Helpdesk service.*
..

    *Manages an Helpdesk service.*

.. i18n: :phonecall: Phone Calls, boolean
..

:phonecall: Phone Calls, boolean

.. i18n:     *Help you to encode the result of a phone call or to plan a list of phone calls to process.*
..

    *Help you to encode the result of a phone call or to plan a list of phone calls to process.*

.. i18n: :bugs: Bug Tracking, boolean
..

:bugs: Bug Tracking, boolean

.. i18n:     *Used by companies to track bugs and support requests on software*
..

    *Used by companies to track bugs and support requests on software*

.. i18n: :fund: Fund Raising Operations, boolean
..

:fund: Fund Raising Operations, boolean

.. i18n:     *This may help associations in their fund raising process and tracking.*
..

    *This may help associations in their fund raising process and tracking.*

.. i18n: :meeting: Calendar of Meetings, boolean
..

:meeting: Calendar of Meetings, boolean

.. i18n:     *Manages the calendar of meetings of the users.*
..

    *Manages the calendar of meetings of the users.*

.. i18n: :claims: Claims, boolean
..

:claims: Claims, boolean

.. i18n:     *Manages the supplier and customers claims, including your corrective or preventive actions.*
..

    *Manages the supplier and customers claims, including your corrective or preventive actions.*

.. i18n: :opportunity: Business Opportunities, boolean
..

:opportunity: Business Opportunities, boolean

.. i18n:     *Tracks identified business opportunities for your sales pipeline.*
..

    *Tracks identified business opportunities for your sales pipeline.*
