
.. module:: event
    :synopsis: Event (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/event"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Event (*event*)
===============
:Module: event
:Name: Event
:Version: 5.0.0.1
:Author: Tiny
:Directory: event
:Web: 
:Official module: yes
:Quality certified: yes

Description
-----------

::

  Organization and management of events.
  
      This module allow you
          * to manage your events and their registrations
          * to use emails to automatically confirm and send acknowledgements for any registration to an event
          * ...
  
      Note that:
      - You can define new types of events in
                  Events / Configuration / Types of Events
      - You can access predefined reports about number of registration per event or per event category in :
                  Events / Reporting

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/event.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/event.zip>`_


Dependencies
------------

 * :mod:`crm`
 * :mod:`base_contact`
 * :mod:`account`

Reports
-------

None


Menus
-------

 * Events Organisation
 * Events Organisation/Configuration
 * Events Organisation/Configuration/Types of Events
 * Events Organisation/Events by Categories
 * Events Organisation/New event
 * Events Organisation/All Events
 * Events Organisation/All Events/Draft Events
 * Events Organisation/All Events/Confirmed Events
 * Events Organisation/All Registrations
 * Events Organisation/All Registrations/Unconfirmed Registrations
 * Events Organisation/All Registrations/Confirmed Registrations
 * Events Organisation/Reporting
 * Events Organisation/Reporting/Events On Registrations
 * Events Organisation/Reporting/Registration By Event Types

Views
-----

 * Event type (form)
 * Event type (tree)
 * Events (form)
 * event.event.tree (tree)
 * event.registration.tree (tree)
 * event.registration.form (form)
 * report.event.registration.tree (tree)
 * report.event.registration.graph (graph)
 * report.event.type.registration.tree (tree)
 * report.event.type.registration.graph (graph)


Objects
-------

Object: Event type (event.type)
###############################



:name: Event type, char, required




Object: Event (event.event)
###########################



:code: Section Code, char





:sequence: Sequence, integer





:date_end: Ending date, datetime, required





:register_max: Maximum Registrations, integer





:mail_registr: Registration Email, text

    *This email will be sent when someone subscribes to the event.*



:mail_auto_confirm: Mail Auto Confirm, boolean

    *Check this box if you want ot use the automatic confirmation emailing or the reminder*



:user_id: Responsible User, many2one





:mail_auto_registr: Mail Auto Register, boolean

    *Check this box if you want to use the automatic mailing for new registration*



:register_min: Minimum Registrations, integer





:parent_id: Parent Section, many2one





:state: Status, selection, required, readonly





:mail_confirm: Confirmation Email, text

    *This email will be sent when the event gets confirmed or when someone subscribes to a confirmed event. This is also the email sent to remind someone about the event.*



:register_prospect: Unconfirmed Registrations, float, readonly





:type: Type, many2one





:child_ids: Child Sections, one2many





:section_id: Case section, many2one, required





:active: Active, boolean





:date_begin: Beginning date, datetime, required





:product_id: Product, many2one, required





:name: Case Section, char, required





:register_current: Confirmed Registrations, float, readonly





:reply_to: Reply-To, char

    *The email address put in the 'Reply-To' of all emails sent by OpenERP about cases in this section*



:allow_unlink: Allow Delete, boolean

    *Allows to delete non draft cases*


Object: Event Registration (event.registration)
###############################################



:date_closed: Closed, datetime, readonly





:history_line: Communication, one2many, readonly





:ref2: Reference 2, reference





:create_date: Created, datetime, readonly





:description: Your action, text





:probability: Probability (%), float





:canal_id: Channel, many2one





:date_action_last: Last Action, datetime, readonly





:planned_cost: Planned Costs, float





:partner_address_id: Partner Contact, many2one





:som: State of Mind, many2one





:section_id: Section, many2one, required





:contact_id: Partner Contact, many2one





:active: Active, boolean





:badge_title: Badge Title, char





:badge_name: Badge Name, char





:date: Date, datetime





:tobe_invoiced: To be Invoiced, boolean





:nb_register: Number of Registration, integer, readonly





:planned_revenue: Planned Revenue, float





:id: ID, integer, readonly





:date_action_next: Next Action, datetime, readonly





:invoice_id: Invoice, many2one





:user_id: Responsible, many2one





:name: Description, char, required





:date_deadline: Deadline, datetime





:partner_invoice_id: Partner Invoiced, many2one





:event_id: Event Related, many2one, required





:partner_id: Partner, many2one





:categ_id: Category, many2one





:unit_price: Unit Price, float





:badge_partner: Badge Partner, char





:priority: Priority, selection





:state: Status, selection, readonly





:case_id: Case, many2one





:email_last: Latest E-Mail, text, readonly





:email_cc: Watchers Emails, char





:invoice_label: Label Invoice, char, required





:ref: Reference, reference





:email_from: Partner Email, char





:log_ids: Logs History, one2many, readonly




Object: Events on registrations (report.event.registration)
###########################################################



:date_begin: Beginning date, datetime, required





:name: Event, char





:confirm_state: Confirm Registration, integer





:draft_state: Draft Registration, integer





:date_end: Ending date, datetime, required





:register_max: Maximum Registrations, integer




Object: Event type on registration (report.event.type.registration)
###################################################################



:draft_state: Draft Registrations, integer





:confirm_state: Confirm Registrations, integer





:name: Event Type, char





:nbevent: Number Of Events, integer


