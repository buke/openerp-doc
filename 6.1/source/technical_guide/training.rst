
.. module:: training
    :synopsis: Training Management 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/training"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Training Management (*training*)
================================
:Module: training
:Name: Training Management
:Version: 5.0.0.0.1
:Author: Tiny SPRL
:Directory: training
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  From the conception of a project to the elaboration of your catalog, our training management allows you to create easily courses and to organize the sessions.
  With the analytic account support, you can know the costs of your training.
  
  * Manage the subscriptions
  * Manage the courses
  * Manage the offers (for a planning)
  * Manage the sessions
  * Manage the support of course

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/training.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/training.zip>`_


Dependencies
------------

 * :mod:`account`
 * :mod:`base_contact_team`
 * :mod:`base_iban`
 * :mod:`product`
 * :mod:`mrp`

Reports
-------

 * Support Booking

 * Presence List

 * Classroom Booking

 * Cancellation Letter

 * Validation Letter

 * Presence Certificate

 * Course Description

 * Financial Statistics

 * Support Delivery

 * Seance - Cancellation

 * Session - Cancellation

 * Training Hiring Form

 * Evaluation From SkateHolder

 * Evaluation From Participant

Menus
-------

 * Partners/Configuration/Contacts
 * Partners/Configuration/Contacts/Technical Skills
 * Training Management
 * Training Management/Configuration
 * Training Management/Configuration/Library
 * Training Management/Configuration/Library/Types
 * Training Management/Configuration/Library/Product Lines
 * Training Management/Library
 * Training Management/Library/Courses
 * Training Management/Library/Courses/Courses
 * Training Management/Library/Courses/Courses/Current Courses
 * Training Management/Library/Courses/Courses/Draft Courses
 * Training Management/Library/Courses/Courses/Deprecated Courses
 * Training Management/Library/Courses/Courses/New course
 * Training Management/Library/Courses/Courses By Category
 * Training Management/Library/Offers
 * Training Management/Library/Offers/Open Offers
 * Training Management/Library/Offers/New Offer
 * Training Management/Catalogs
 * Training Management/Catalogs/Catalogs
 * Training Management/Catalogs/Catalogs/Old Catalogs
 * Training Management/Catalogs/Catalogs/Current Catalogs
 * Training Management/Catalogs/Catalogs/New Catalog
 * Training Management/Plannings
 * Training Management/Plannings/Sessions
 * Training Management/Plannings/Sessions/Draft Sessions
 * Training Management/Plannings/Sessions/Sessions - Report
 * Training Management/Plannings/Sessions/Sessions to Confirm
 * Training Management/Plannings/Sessions/Sessions to Deduplicate
 * Training Management/Plannings/Sessions/New Session
 * Training Management/Plannings/Seances
 * Training Management/Plannings/Seances/Seances - Report
 * Training Management/Plannings/Seances/Calendar of Seances
 * Training Management/Plannings/Seances/Seances to Confirm
 * Training Management/Plannings/Seances/Seances to Deduplicate
 * Training Management/Plannings/Seances/New Seance
 * Training Management/Subscriptions
 * Training Management/Subscriptions/Subscriptions
 * Training Management/Subscriptions/Subscriptions/Subscriptions to Validate
 * Training Management/Subscriptions/Subscriptions to Treat
 * Training Management/Subscriptions/Subscriptions/Subscriptions to Invoice
 * Training Management/Subscriptions/New Subscription
 * Training Management/Subscriptions/Subscription Lines
 * Training Management/Subscriptions/Subscription Lines/Uninvoiced Subscription Lines
 * Training Management/Participation
 * Training Management/Participation/Participations of the Participants
 * Training Management/Participation/Evaluation Form
 * Dummy
 * Dummy/Support Deliveries

Views
-----

 * res.partner.contact.technical.skill.tree (tree)
 * res.partner.contact.technical.skill.form (form)
 * \* INHERIT res.partner.team.form.inherited (form)
 * \* INHERIT res.partner.view.form.inherited (form)
 * \* INHERIT res.partner.contact.form.inherit (form)
 * \* INHERIT res.partner.contact.form.inherit (form)
 * \* INHERIT res.partner.contact.form.inherit3 (form)
 * training.course_category.form (form)
 * training.course_category.tree (tree)
 * training.course_type.form (form)
 * training.course_type.tree (tree)
 * training.course.form (form)
 * training.course.list (tree)
 * training.catalog.form (form)
 * training.catalog.tree (tree)
 * training.session.form (form)
 * training.session.tree (tree)
 * training.session.tree (tree)
 * training.session.tree (tree)
 * training.session.calendar (calendar)
 * training.seance.form (form)
 * training.seance.tree (tree)
 * training.seance.tree (tree)
 * training.seance.calendar (calendar)
 * training.subscription.form (form)
 * training.subscription.tree (tree)
 * training.subscription.tree (tree)
 * training.subscription.line.tree (tree)
 * training.offer.form (form)
 * training.offer.tree (tree)
 * training.participation.form (form)
 * training.participation.tree (tree)
 * training.participation.skateholder.form (form)
 * training.participation.skateholder.tree (tree)
 * view.dummy.support.delivery.form (form)


Objects
-------

Object: res.partner.contact_technical_skill (res.partner.contact_technical_skill)
#################################################################################



:name: Name, char, required




Object: training.course_category (training.course_category)
###########################################################



:code: Account Code, char





:description: Description, text

    *Description of the course category*



:child_ids: Children, one2many, readonly





:quantity_max: Maximum Quantity, float





:contact_id: Contact, many2one





:company_currency_id: Currency, many2one, readonly





:date: Date End, date





:active: Active, boolean





:partner_id: Associated Partner, many2one





:analytic_account_id: Analytic Account, many2one





:user_id: Account Manager, many2one





:name: Account Name, char, required





:credit: Credit, float, readonly





:date_start: Date Start, date





:company_id: Company, many2one, required





:parent_id: Parent Analytic Account, many2one





:state: State, selection, required





:complete_name: Full Account Name, char, readonly





:debit: Debit, float, readonly





:line_ids: Analytic Entries, one2many





:balance: Balance, float, readonly





:type: Account Type, selection





:quantity: Quantity, float, readonly




Object: The type of a course (training.course_type)
###################################################



:objective: Objective, text

    *Allows to the user to write the objectives of the course type*



:min_limit: Minimum Threshold, integer, required

    *The minimum threshold is the minimum for this type of course*



:max_limit: Maximum Threshold, integer, required

    *The maximum threshold is the maximum for this type of course*



:name: Name, char, required

    *The course type's name*



:description: Description, text

    *Allows to the user to write the description of the course type*


Object: training.course (training.course)
#########################################



:code: Account Code, char





:course_type_id: Type, many2one, required





:description: Description, text





:total_duration: Total Duration, float, readonly

    *The total duration is computed if there is any subcourse*



:child_ids: Child Accounts, one2many





:duration: Duration, float, required

    *The duration for a standalone course*



:quantity_max: Maximum Quantity, float





:contact_id: Contact, many2one





:lecturer_ids: Lecturers, many2many

    *The lecturers who give the course*



:company_currency_id: Currency, many2one, readonly





:date: Date End, date





:reference_id: Master Course, many2one

    *The master course is necessary if the user wants to link certain courses together to simplify management*



:active: Active, boolean





:display_name: Display Name, char

    *Allows to show a short name for this course*



:offer_ids: Offers, many2many

    *The offers containing the course*



:partner_id: Associated Partner, many2one





:children: Children, one2many

    *A course can be completed with some subcourses*



:internal_note: Note, text

    *The user can write some internal note for this course*



:analytic_account_id: Account, many2one





:has_support: Has Support, boolean, readonly





:user_id: Account Manager, many2one





:name: Account Name, char, required





:credit: Credit, float, readonly





:target_public: Target Public, char

    *Allows to the participants to select a course whose can participate*



:purchase_line_ids: Supplier Commands, one2many

    *The purchase line helps to create a purchase order for the seance*



:date_start: Date Start, date





:p_id: Parent Course, many2one, readonly

    *The parent course*



:company_id: Company, many2one, required





:sequence: Sequence, integer

    *The sequence can help the user to reorganize the order of the courses*



:parent_id: Parent Analytic Account, many2one





:state: State, selection, required





:lang_id: Language, many2one, required

    *The language of the course*



:complete_name: Full Account Name, char, readonly





:state_course: State, selection, required, readonly

    *The state of the course*



:debit: Debit, float, readonly





:line_ids: Analytic Entries, one2many





:balance: Balance, float, readonly





:type: Account Type, selection





:complementary_course_ids: Complementary Courses, many2many





:preliminary_course_ids: Preliminary Courses, many2many





:quantity: Quantity, float, readonly




Object: training.course.purchase_line (training.course.purchase_line)
#####################################################################



:course_id: course, many2one, required

    *The course attached to this purchase line*



:product_uom_id: Product UoM, many2one, required

    *The unit of measure for this product*



:product_id: Product, many2one, required

    *The product for this purchase line*



:product_qty: Quantity, integer, required

    *The quantity of this product*


Object: training.offer (training.offer)
#######################################



:analytic_account_id: Analytic Account, many2one





:kind: Kind, selection, required





:description: Description, text

    *Allows to write the description of the course*



:profit: Profit, float, readonly





:course_ids: Courses, many2many

    *An offer can contain some courses*



:profit_margin: Profit Margin, float, readonly





:state: State, selection, required, readonly

    *The status of the course*



:costs: Costs, float, readonly





:objective: Objective, text

    *Allows to write the objectives of the course*



:revenues: Revenues, float, readonly





:product_id: Product, many2one

    *An offer can be a product for invoicing*



:name: Name, char, required

    *The name's offer*


Object: Catalog (training.catalog)
##################################



:note: Note, text

    *Allows to write a note for the catalog*



:state: State, selection, required, readonly

    *The status of the catalog*



:session_ids: Sessions, one2many

    *The sessions in the catalog*



:year: Year, integer, required

    *The year when the catalog has been published*


Object: training.seance (training.seance)
#########################################



:max_limit: Maximum Limit, integer





:reserved: Reserved, boolean





:presence_form: Presence Form, boolean





:duration: Duration, float





:invoice: Invoice, boolean





:participant_ids: Participants, many2many





:course_id: Course, many2one, required





:purchase_line_ids: Supplier Commands, one2many





:draft_seats: Draft Seats, integer





:user_id: Responsible, many2one, required





:min_limit: Minimum Limit, integer





:state: State, selection, required, readonly





:location: Location, char





:partner_ids: StakeHolders, many2many





:evaluation: Evaluation, boolean





:participant_count: Number of Participants, integer, readonly





:available_seats: Available Seats, integer





:session_ids: Sessions, many2many





:date: Date, datetime





:layout: Layout, char





:room: Room, char





:support_received: Support Received, boolean, readonly





:name: Name, char, required





:group_id: Group, many2one




Object: Session (training.session)
##################################



:seance_ids: Seances, many2many

    *List of the events in the session*



:name: Name, char, required

    *The session's name*



:offer_id: Offer, many2one, required

    *Allows to select a validated offer for the session*



:draft_seats: Draft Seats, integer





:available_seats: Available Seats, integer





:state: State, selection, required, readonly

    *The status of the session*



:catalog_id: Catalog, many2one

    *Allows to select a published catalog*



:date: Date, datetime, required

    *The date of the planned session*



:user_id: Responsible, many2one, required





:purchase_line_ids: Supplier Commands, one2many

    *The supplier commands will create a purchase order for each command for the session*



:is_intra: Is Intra, boolean, readonly




Object: training.session.purchase_line (training.session.purchase_line)
#######################################################################



:product_uom_id: Product UoM, many2one, required

    *The unit of measure for the product*



:product_id: Product, many2one, required

    *The product for the purchase order*



:session_id: Session, many2one, required

    *The session for this purchase order*



:product_qty: Quantity, integer, required

    *The quantity of the product for the purchase order*


Object: Mass Subscription Wizard (wizard.training.mass.subscription)
####################################################################



:partner_ids: Partners, many2many, required





:session_ids: Sessions, many2many, required




Object: Group (training.group)
##############################



:name: Name, char, required

    *The group's name*


Object: training.subscription (training.subscription)
#####################################################



:origin: Origin, char





:address_id: Invoice Address, many2one, required





:create_date: Creation Date, datetime, readonly





:name: Reference, char, required, readonly

    *The unique identifier is generated by the system (customizable)*



:notification_text: Kind, char, readonly





:payment_term_id: Payment Term, many2one





:subscription_line_ids: Subscription Lines, one2many





:draft_seats: Draft Seats, integer





:max_seats: Maximum Seats, integer





:state: State, selection, required, readonly





:rest_seats: Rest Seats, integer





:responsible_id: Responsible, many2one, required





:pricelist_id: Pricelist, many2one





:partner_id: Partner, many2one, required





:notification_active: Active, boolean




Object: Participation (training.participation)
##############################################



:contact_id: Contact, many2one, readonly





:seance_id: Seance, many2one, required, readonly





:date: Date, datetime, readonly





:subscription_id: Subscription, many2one, required, readonly





:partner_id: Partner, many2one, readonly





:present: Present, boolean

    *Allows to know if a participant was present or not*


Object: training.seance.purchase_line (training.seance.purchase_line)
#####################################################################



:product_uom_id: Product UoM, many2one, required





:procurement_id: unknown, many2one, readonly





:product_id: Product, many2one, required





:seance_id: Seance, many2one, required





:product_qty: Quantity, integer, required




Object: Subscription Line (training.subscription.line)
######################################################



:contact_id: Contact, many2one, required





:invoice_id: Invoice, many2one





:paid: Paid, boolean





:contact_email: Email, char





:session_id: Session, many2one, required





:subscription_id: Subscription, many2one, required





:group_id: Group, many2one





:partner_id: unknown, many2one





:invoiced: Invoiced, boolean




Object: training.participation.skateholder (training.participation.skateholder)
###############################################################################



:partner_id: Partner, many2one





:skateholder_id: Contact, many2one





:date: Date, datetime, readonly





:seance_id: Seance, many2one





:payment_mode: Payment Mode, selection





:evaluation: Evaluation, integer





:course_id: Course, many2one, readonly




Object: dummy.support.delivery (dummy.support.delivery)
#######################################################



:name: Name, char


