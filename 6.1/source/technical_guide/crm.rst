
.. module:: crm
    :synopsis: Customer & Supplier Relationship Management (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/crm"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Customer & Supplier Relationship Management (*crm*)
===================================================
:Module: crm
:Name: Customer & Supplier Relationship Management
:Version: 5.0.1.0
:Author: Tiny
:Directory: crm
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  The generic OpenERP Customer Relationship Management
  system enables a group of people to intelligently and efficiently manage
  leads, opportunities, tasks, issues, requests, bugs, campaign, claims, etc.
  It manages key tasks such as communication, identification, prioritization,
  assignment, resolution and notification.
  
  OpenERP ensures that all cases are successfully tracked by users, customers and
  suppliers. It can automatically send reminders, escalate the request, trigger
  specific methods and lots of others actions based on your enterprise own rules.
  
  The greatest thing about this system is that users don't need to do anything
  special. They can just send email to the request tracker. OpenERP will take
  care of thanking them for their message, automatically routing it to the
  appropriate staff, and making sure all future correspondence gets to the right
  place.
  
  The CRM module has a email gateway for the synchronisation interface
  between mails and OpenERP.

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/crm.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/crm.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/crm.zip>`_


Dependencies
------------

 * :mod:`base`

Reports
-------

 * Business Opportunities

Menus
-------

 * CRM & SRM
 * CRM & SRM/Configuration
 * CRM & SRM/Configuration/Cases
 * CRM & SRM/Configuration/Cases/Sections
 * CRM & SRM/All Cases
 * CRM & SRM/All Cases/Cases by section
 * CRM & SRM/Configuration/Cases/Categories
 * CRM & SRM/Configuration/Cases/Rules
 * CRM & SRM/All Cases/All Cases
 * CRM & SRM/All Cases/All Cases/Open Cases
 * CRM & SRM/All Cases/My cases
 * CRM & SRM/All Cases/My cases/My Open Cases
 * CRM & SRM/All Cases/Cases Histories
 * CRM & SRM/All Cases/Cases Histories/All Histories
 * CRM & SRM/All Cases/Cases Histories/My Histories
 * CRM & SRM/Configuration/Segmentations
 * CRM & SRM/Configuration/Segmentations/Segmentations
 * CRM & SRM/Configuration/Create menus for a case section

Views
-----

 * res.partner.events.form (tree)
 * crm.case.section.form (form)
 * crm.case.section.tree (tree)
 * crm.case.categ.form (form)
 * crm.case.categ.tree (tree)
 * crm.case.rule.form (form)
 * crm.case.rule.tree (tree)
 * crm.case.log.tree (tree)
 * crm.case.history.tree (tree)
 * crm.case.calendar (calendar)
 * crm.case.tree (tree)
 * crm.case.form (form)
 * crm.case.history.form (form)
 * crm.segmentation.line.tree (tree)
 * crm.segmentation.line.form (form)
 * crm.segmentation.form (form)
 * crm.segmentation.tree (tree)


Objects
-------

Object: Case Section (crm.case.section)
#######################################



:code: Section Code, char





:user_id: Responsible User, many2one





:name: Case Section, char, required





:sequence: Sequence, integer





:child_ids: Child Sections, one2many





:parent_id: Parent Section, many2one





:reply_to: Reply-To, char

    *The email address put in the 'Reply-To' of all emails sent by OpenERP about cases in this section*



:allow_unlink: Allow Delete, boolean

    *Allows to delete non draft cases*



:active: Active, boolean




Object: Category of case (crm.case.categ)
#########################################



:name: Case Category Name, char, required





:probability: Probability (%), float, required





:section_id: Case Section, many2one




Object: Case Rule (crm.case.rule)
#################################



:trg_categ_id: Category, many2one





:trg_section_id: Section, many2one





:sequence: Sequence, integer





:act_remind_partner: Remind Partner, boolean

    *Check this if you want the rule to send a reminder by email to the partner.*



:trg_max_history: Maximum Communication History, integer





:trg_date_range_type: Delay type, selection





:act_section_id: Set section to, many2one





:trg_date_range: Delay after trigger date, integer





:act_remind_user: Remind responsible, boolean

    *Check this if you want the rule to send a reminder by email to the user.*



:trg_priority_from: Minimum Priority, selection





:trg_date_type: Trigger Date, selection





:act_method: Call Object Method, char





:act_email_cc: Add watchers (Cc), char

    *These people will receive a copy of the future communication between partner and users by email*



:act_priority: Set priority to, selection





:trg_state_to: Button Pressed, selection





:act_mail_to_email: Mail to these emails, char





:act_remind_attach: Remind with attachment, boolean

    *Check this if you want that all documents attached to the case be attached to the reminder email sent.*



:trg_user_id: Responsible, many2one





:act_state: Set state to, selection





:act_mail_to_partner: Mail to partner, boolean





:trg_priority_to: Maximum Priority, selection





:active: Active, boolean





:act_mail_to_watchers: Mail to watchers (Cc), boolean





:name: Rule Name, char, required





:trg_state_from: Case State, selection





:act_user_id: Set responsible to, many2one





:act_mail_to_user: Mail to responsible, boolean





:trg_partner_id: Partner, many2one





:trg_partner_categ_id: Partner Category, many2one





:act_mail_body: Mail body, text




Object: Case (crm.case)
#######################



:date_closed: Closed, datetime, readonly





:history_line: Communication, one2many, readonly





:create_date: Created, datetime, readonly





:probability: Probability (%), float





:canal_id: Channel, many2one





:partner_address_id: Partner Contact, many2one





:som: State of Mind, many2one





:date: Date, datetime





:planned_revenue: Planned Revenue, float





:id: ID, integer, readonly





:date_action_next: Next Action, datetime, readonly





:user_id: Responsible, many2one





:partner_id: Partner, many2one





:priority: Priority, selection





:state: Status, selection, readonly





:email_cc: Watchers Emails, char





:ref: Reference, reference





:log_ids: Logs History, one2many, readonly





:description: Your action, text





:date_action_last: Last Action, datetime, readonly





:planned_cost: Planned Costs, float





:ref2: Reference 2, reference





:section_id: Section, many2one, required





:active: Active, boolean





:categ_id: Category, many2one





:name: Description, char, required





:date_deadline: Deadline, datetime





:email_last: Latest E-Mail, text, readonly





:email_from: Partner Email, char




Object: Case Communication History (crm.case.log)
#################################################



:user_id: User Responsible, many2one, readonly





:name: Action, char





:canal_id: Channel, many2one





:som: State of Mind, many2one





:section_id: Section, many2one





:case_id: Case, many2one, required





:date: Date, datetime




Object: Case history (crm.case.history)
#######################################



:description: Description, text





:canal_id: Channel, many2one





:som: State of Mind, many2one





:section_id: Section, many2one





:date: Date, datetime





:user_id: User Responsible, many2one, readonly





:name: Action, char





:log_id: Log, many2one





:note: Description, text, readonly





:case_id: Case, many2one, required





:email: Email, char




Object: Partner Segmentation (crm.segmentation)
###############################################



:description: Description, text





:som_interval_max: Max Interval, integer

    *The computation is made on all events that occurred during this interval, the past X periods.*



:partner_id: Max Partner ID processed, integer





:som_interval_default: Default (0=None), float

    *Default state of mind for period preceding the 'Max Interval' computation. This is the starting state of mind by default if the partner has no event.*



:segmentation_line: Criteria, one2many, required





:som_interval_decrease: Decrease (0>1), float

    *If the partner has not purchased (or bought) during a period, decrease the state of mind by this factor. It's a multiplication*



:state: Execution Status, selection, readonly





:sales_purchase_active: Use The Sales Purchase Rules, boolean

    *Check if you want to use this tab as part of the segmentation rule. If not checked, the criteria beneath will be ignored*



:exclusif: Exclusive, boolean

    *Check if the category is limited to partners that match the segmentation criterions. If checked, remove the category from partners that doesn't match segmentation criterions*



:categ_id: Partner Category, many2one, required

    *The partner category that will be added to partners that match the segmentation criterions after computation.*



:som_interval: Days per Periode, integer

    *A period is the average number of days between two cycle of sale or purchase for this segmentation. It's mainly used to detect if a partner has not purchased or bought for too long a time, so we suppose that their state of mind has changed because they probably bought goods from another supplier. Use this functionality for recurring businesses.*



:name: Name, char, required

    *The name of the segmentation.*


Object: Segmentation line (crm.segmentation.line)
#################################################



:expr_operator: Operator, selection, required





:expr_value: Value, float, required





:expr_name: Control Variable, selection, required





:segmentation_id: Segmentation, many2one





:operator: Mandatory / Optional, selection, required





:name: Rule Name, char, required


