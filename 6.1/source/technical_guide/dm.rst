
.. module:: dm
    :synopsis: Direct Marketing 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/dm"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Direct Marketing (*dm*)
=======================
:Module: dm
:Name: Direct Marketing
:Version: 5.0.1.0
:Author: Tiny
:Directory: dm
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Marketing Campaign Management Module
  
          This module allows to :
  
          * Commercial Offers :
              - Create  Multimedia Commercial Offers
              - View a graphical representation of the offer steps
              - Create offers from offer models and offer ideas
  
          * Marketing Campaign
              - Plan your Marketing Campaign and Commercial Propositions
              - Generate the Retro planning (automatically creates all the tasks necessary to launch your campaign)
              - Assign automatic prices to the items of your commercial propositions
              - Auto generate the purchase orders for all the items of the campaign
              - Manage Customers Fils, segments and segmentation criteria
              - Create campaigns from campaign models
              - Manage copywriters, brokers, dealers, addresses deduplicators and cleaners

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/dm.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/dm.zip>`_


Dependencies
------------

 * :mod:`project_retro_planning`
 * :mod:`purchase_tender`
 * :mod:`base_language`
 * :mod:`document`
 * :mod:`base_report_designer`
 * :mod:`sale`
 * :mod:`base_partner_gender`

Reports
-------

 * Offer

 * Offer Model

 * PreOffer

 * Offer Graph

 * Campaign

Menus
-------

 * Direct Marketing
 * Direct Marketing/Configuration
 * Direct Marketing/Offers
 * Direct Marketing/Configuration/Offers
 * Direct Marketing/Offers/All Offers
 * Direct Marketing/Offers/All Offers/Open Offers
 * Direct Marketing/Offers/All Offers/Draft Offers
 * Direct Marketing/Offers/All Offers/Closed Offers
 * Direct Marketing/Offers/My Offers
 * Direct Marketing/Offers/My Offers/My Open Offers
 * Direct Marketing/Offers/My Offers/My Draft Offers
 * Direct Marketing/Offers/My Offers/My Closed Offers
 * Direct Marketing/Configuration/Offers/All Offer Models
 * Direct Marketing/Configuration/Offers/All Copywriters
 * Direct Marketing/Offers/All Offer Ideas
 * Direct Marketing/Offers/My Offer Ideas
 * Direct Marketing/Configuration/Offers/Edit Categories
 * Direct Marketing/Offers/Offer Categories
 * Direct Marketing/Configuration/Offers/Offer Steps
 * Direct Marketing/Configuration/Offers/Offer Steps/All Offer Step Types
 * Direct Marketing/Configuration/Offers/Offer Steps/All Offer Steps
 * Direct Marketing/Configuration/Offers/Offer Steps/All Transition Triggers
 * Direct Marketing/Configuration/Offers/Offer Steps/All Medias
 * Direct Marketing/Configuration/Offers/Offer Steps/All Offer Step Action
 * Direct Marketing/Configuration/Campaigns
 * Direct Marketing/Configuration/Customers Lists
 * Direct Marketing/Campaigns
 * Direct Marketing/Configuration/Low Level
 * Direct Marketing/Configuration/Low Level/Campaign Documents
 * Direct Marketing/Campaigns/All Campaigns
 * Direct Marketing/Campaigns/All Campaigns/Open Campaigns
 * Direct Marketing/Campaigns/All Campaigns/Draft Campaigns
 * Direct Marketing/Campaigns/All Campaigns/Closed Campaigns
 * Direct Marketing/Campaigns/My Campaigns
 * Direct Marketing/Campaigns/My Campaigns/My Open Campaigns
 * Direct Marketing/Campaigns/My Campaigns/My Draft Campaigns
 * Direct Marketing/Campaigns/My Campaigns/My Closed Campaigns
 * Direct Marketing/Configuration/Campaigns/All Campaign Models
 * Direct Marketing/Campaigns/All Campaign Propositions
 * Direct Marketing/Campaigns/My Campaign Propositions
 * Direct Marketing/Configuration/Campaigns/All Segments
 * Direct Marketing/Campaigns/All Campaign Groups
 * Direct Marketing/Campaigns/My Campaign Groups
 * Direct Marketing/Configuration/Campaigns/All Campaign Types
 * Direct Marketing/Configuration/Campaigns/All Overlays
 * Direct Marketing/Configuration/Campaigns/All Dealers
 * Direct Marketing/Configuration/Customers Lists/All Customers Lists Brokers
 * Direct Marketing/Configuration/Customers Lists/All Deduplicator
 * Direct Marketing/Configuration/Campaigns/All Campaign Prices Progression
 * Direct Marketing/Configuration/Campaigns/All Purchase Lines
 * Direct Marketing/Configuration/Customers Lists/All Customers Lists
 * Direct Marketing/Configuration/Customers Lists/All Customers List Type
 * Direct Marketing/Configuration/Customers Lists/All Customers List Recruiting Origin
 * Direct Marketing/Configuration/Low Level/Campaign Documents/All Campaign Document Types
 * Direct Marketing/Configuration/Low Level/Campaign Documents/All Campaign Documents
 * Direct Marketing/Configuration/Customers Lists/All Customers Files
 * Direct Marketing/Configuration/Campaigns/Overlay Payment Rule
 * Direct Marketing/Configuration/Customers
 * Direct Marketing/Configuration/Customers/All Customers
 * Direct Marketing/Configuration/Customers/All Customer Orders
 * Direct Marketing/Configuration/Customers/All Orders
 * Direct Marketing/Configuration/Customers/All Customers Genders
 * Direct Marketing/Configuration/Low Level/All Workitems
 * Direct Marketing/Configuration/Customers/All Segmentations
 * Direct Marketing/Configuration/Low Level/Edit Events
 * Direct Marketing/Configuration/Campaigns/All Trademarks
 * Direct Marketing/Configuration/Documents
 * Direct Marketing/Configuration/Documents/Edit DTP Documents Categories
 * Direct Marketing/Configuration/Documents/All DTP Documents
 * Direct Marketing/Configuration/Documents/All DTP Plugins Template
 * Direct Marketing/Configuration/Documents/All DTP Plugins
 * Direct Marketing/Configuration/Customers/All Plugins Values
 * Direct Marketing/Configuration/Mail Service
 * Direct Marketing/Configuration/Mail Service/All Mail Services

Views
-----

 * dm.offer.list (tree)
 * dm.offer.tree (tree)
 * dm.offer.form (form)
 * dm.offer.model.tree (tree)
 * dm.offer.model.form (form)
 * dm.preoffer.form (form)
 * dm.offer.category.form (form)
 * dm.offer.category.list (tree)
 * dm.offer.category.tree (tree)
 * dm.offer.history.form (form)
 * dm.offer.history.tree (tree)
 * dm.offer.step.type.form (form)
 * dm.offer.step.type.tree (tree)
 * dm.offer.step.tree (tree)
 * dm.offer.step.form (form)
 * dm.offer.step.transition.trigger.form (form)
 * dm.offer.step.transition.trigger.tree (tree)
 * dm.media.form (form)
 * dm.meida.tree (tree)
 * \* INHERIT product.normal.form.inherit (form)
 * \* INHERIT ir.actions.server.inherit (form)
 * dm.offer.step.action.form (form)
 * dm.offer.step.action.tree (tree)
 * dm.campaign.calendar (calendar)
 * dm.campaign.tree (tree)
 * dm.campaign.form (form)
 * dm.campaign.model.tree (tree)
 * dm.campaign.model.form (form)
 * dm.campaign.proposition.form (form)
 * dm.campaign.proposition.tree (tree)
 * dm.campaign.proposition.calendar (calendar)
 * dm.campaign.proposition.segment.form (form)
 * dm.campaign.proposition.segment.tree (tree)
 * dm.campaign.group.form (form)
 * dm.campaign.group.tree (tree)
 * dm.campaign.type.form (form)
 * dm.campaign.type.tree (tree)
 * dm.overlay.form (form)
 * dm.overlay.tree (tree)
 * dm.campaign.proposition.prices_progression.form (form)
 * dm.campaign.proposition.prices_progression.tree (tree)
 * dm.campaign.purchase_line_tree (tree)
 * dm.campaign.purchase_line_form (form)
 * dm.customers_list.form (form)
 * dm.customers_list.tree (tree)
 * dm.customers_list.type.form (form)
 * dm.customers_list.type.tree (tree)
 * dm.customers_list.recruit_origin.form (form)
 * dm.customers_list.recruit_origin.tree (tree)
 * dm.campaign.document.type.form (form)
 * dm.campaign.document.type.tree (tree)
 * dm.campaign.document.form (form)
 * dm.campaign.document.tree (tree)
 * dm.customers_file.form (form)
 * dm.customers_file.tree (tree)
 * \* INHERIT res.country.form.inherit (form)
 * \* INHERIT res.partner.form.inherit (form)
 * dm.overlay.payment_rule.form (form)
 * dm.overlay.payment_rule.tree (tree)
 * dm.customer.form (form)
 * dm.customer.tree (tree)
 * dm.customer.order.form (form)
 * dm.customer.order.tree (tree)
 * dm.order.form (form)
 * dm.order.tree (tree)
 * dm.customer.gender.form (form)
 * dm.customer.gender.tree (tree)
 * dm.worktitem.form (form)
 * dm.workitem.tree (tree)
 * dm.customer.segmentation.form (form)
 * dm.customer.segmentation.tree (tree)
 * dm.event.tree (tree)
 * dm.event.form (form)
 * dm.trademark.tree (tree)
 * dm.trademark.form (form)
 * dm.offer.document.category.form (form)
 * dm.offer.document.category.tree (tree)
 * dm.offer.document.form (form)
 * dm.offer.document.tree (tree)
 * dm.document.template.form (form)
 * dm.document.template.tree (tree)
 * dm.ddf.plugin.form (form)
 * dm.ddf.plugin.tree (tree)
 * dm.plugins.value.form (form)
 * dm.plugins.value.tree (tree)
 * dm.mail_service.form (form)
 * dm.mail_service.tree (tree)


Objects
-------

Object: dm.media (dm.media)
###########################



:code: Code, char, required





:name: Name, char, required




Object: dm.trademark (dm.trademark)
###################################



:code: Code, char, required





:media_id: Media, many2one





:name: Name, char, required





:header: Header (.odt), binary





:signature: Signature, binary





:logo: Logo, binary





:partner_id: Partner, many2one




Object: dm.offer.category (dm.offer.category)
#############################################



:child_ids: Childs Category, one2many





:parent_id: Parent, many2one





:complete_name: Category, char, readonly





:name: Name, char, required




Object: dm.offer.production.cost (dm.offer.production.cost)
###########################################################



:name: Name, char, required




Object: dm.offer (dm.offer)
###########################



:code: Code, char, required





:purchase_note: Purchase Notes, text





:production_category_ids: Production Categories, many2many





:last_modification_date: Last Modification Date, char, readonly





:keywords: Keywords, text





:preoffer_type: Type, selection





:offer_origin_id: Original Offer, many2one





:production_cost_id: Production Cost, many2one





:copywriter_id: Copywriter, many2one





:forbidden_state_ids: Forbidden States, many2many





:category_ids: Categories, many2many





:preoffer_original_id: Original Offer Idea, many2one





:state: Status, selection, readonly





:version: Version, float





:history_ids: History, one2many, readonly





:type: Type, selection





:lang_orig_id: Original Language, many2one





:purchase_category_ids: Purchase Categories, many2many





:name: Name, char, required





:recommended_trademark_id: Recommended Trademark, many2one





:child_ids: Childs Category, one2many





:preoffer_offer_id: Offer, many2one





:translation_ids: Translations, one2many, readonly





:active: Active, boolean





:order_date: Order Date, date





:legal_state: Legal State, selection





:quotation: Quotation, char





:step_ids: Offer Steps, one2many





:offer_responsible_id: Responsible, many2one





:notes: General Notes, text





:fixed_date: Fixed Date, date





:planned_delivery_date: Planned Delivery Date, date





:forbidden_country_ids: Forbidden Countries, many2many





:delivery_date: Delivery Date, date




Object: dm.offer.translation (dm.offer.translation)
###################################################



:date: Date, date





:language_id: Language, many2one





:offer_id: Offer, many2one, required





:notes: Notes, text





:translator_id: Translator, many2one




Object: dm.offer.step.type (dm.offer.step.type)
###############################################



:name: Name, char, required





:code: Code, char, required





:description: Description, text





:flow_stop: Flow Stop, boolean





:flow_start: Flow Start, boolean




Object: dm.offer.step.action (dm.offer.step.action)
###################################################



:sms_server: SMS Server, many2one





:code: Python Code, text

    *Python code to be executed*



:media_id: Media, many2one, required





:sequence: Sequence, integer

    *Important when you deal with multiple actions, the execution order will be decided based on this, low number is higher priority.*



:child_ids: Other Actions, many2many





:trigger_name: Trigger Name, selection

    *Select the Signal name that is to be used as the trigger.*



:record_id: Create Id, many2one

    *Provide the field name where the record id is stored after the create operations. If it is empty, you can not track the new record.*



:write_id: Write Id, char

    *Provide the field name that the record id refers to for the write operation. If it is empty it will refer to the active id of the object.*



:srcmodel_id: Model, many2one

    *Object in which you want to create / write the object. If it is empty then refer to the Object field.*



:message: Message, text

    *Specify the message. You can use the fields from the object. e.g. `Dear [[ object.partner_id.name ]]`*



:dm_action: Action, boolean





:email_server: Email Server, many2one





:model_id: Object, many2one, required

    *Select the object on which the action will work (read, write, create).*



:subject: Subject, char

    *Specify the subject. You can use fields from the object, e.g. `Hello [[ object.partner_id.name ]]`*



:loop_action: Loop Action, many2one

    *Select the action that will be executed. Loop action will not be available inside loop.*



:fields_lines: Field Mappings., one2many





:trigger_obj_id: Trigger On, many2one

    *Select the object from the model on which the workflow will executed.*



:name: Action Name, char, required

    *Easy to Refer action by name e.g. One Sales Order -> Many Invoices*



:mobile: Mobile No, char

    *Provides fields that be used to fetch the mobile number, e.g. you select the invoice, then `object.invoice_address_id.mobile` is the field which gives the correct mobile number*



:expression: Loop Expression, char

    *Enter the field/expression that will return the list. E.g. select the sale order in Object, and you can have loop on the sales order line. Expression = `object.order_line`.*



:server_action_id: Server Action, many2one





:sms: SMS, char





:wkf_model_id: Workflow On, many2one

    *Workflow to be executed on this model.*



:state: Action Type, selection, required

    *Type of the Action that is to be executed*



:condition: Condition, char, required

    *Condition that is to be tested before action is executed, e.g. object.list_price > object.cost_price*



:usage: Action Usage, char





:type: Action Type, char, required





:email: Email Address, char

    *Provides the fields that will be used to fetch the email address, e.g. when you select the invoice, then `object.invoice_address_id.email` is the field which gives the correct address*



:action_id: Client Action, many2one

    *Select the Action Window, Report, Wizard to be executed.*


Object: dm.offer.step (dm.offer.step)
#####################################



:incoming_transition_ids: Incoming Transition, one2many, readonly





:manufacturing_constraint_ids: Mailing Manufacturing Products, many2many





:purchase_note: Purchase Notes, text





:seq: Step Type Sequence, integer





:type_id: Type, many2one, required





:flow_start: Flow Start, boolean





:code: Code, char, required





:item_ids: Items, many2many





:origin_id: Origin, many2one





:parent_id: Parent, many2one





:state: Status, selection, readonly





:outgoing_transition_ids: Outgoing Transition, one2many





:desc: Description, text





:trademark_note: Trademark Notes, text





:action_id: Action, many2one, required





:document_ids: DTP Documents, one2many





:media_id: Media, many2one, required





:offer_id: Offer, many2one, required





:production_note: Production Notes, text





:doc_number: Number of documents of the mailing, integer





:split_mode: Split mode, selection





:mailing_at_dates: Mailing at dates, boolean





:legal_state: Legal State, char





:quotation: Quotation, char





:dtp_category_ids: DTP Categories, many2many





:name: Name, char, required





:floating_date: Floating date, boolean





:notes: Notes, text





:trademark_category_ids: Trademark Categories, many2many





:dtp_note: DTP Notes, text





:interactive: Interactive, boolean





:planning_note: Planning Notes, text




Object: dm.offer.step.transition.trigger (dm.offer.step.transition.trigger)
###########################################################################



:in_act_cond: Action Condition, text, required





:code: Code, char, required





:name: Trigger Name, char, required





:gen_next_wi: Auto Generate Next Workitems, boolean




Object: dm.offer.step.transition (dm.offer.step.transition)
###########################################################



:delay: Offer Delay, integer, required





:delay_type: Delay type, selection, required





:step_to_id: To Offer Step, many2one, required





:condition_id: Trigger Condition, many2one, required





:step_from_id: From Offer Step, many2one, required




Object: dm.overlay.payment_rule (dm.overlay.payment_rule)
#########################################################



:account_id: Account, many2one





:move: Move, selection





:country_id: Country, many2one





:journal_id: Journal, many2one





:currency_id: Currency, many2one





:country_default: Default for Country, boolean




Object: dm.campaign.group (dm.campaign.group)
#############################################



:code: Code, char, readonly





:name: Campaign group name, char, required





:campaign_ids: Campaigns, one2many, readonly





:quantity_wanted_total: Total Wanted Quantity, char, readonly





:quantity_usable_total: Total Usable Quantity, char, readonly





:project_id: Project, many2one, readonly





:purchase_line_ids: Purchase Lines, one2many





:quantity_delivered_total: Total Delivered Quantity, char, readonly




Object: dm.campaign.type (dm.campaign.type)
###########################################



:code: Code, char, required





:name: Description, char, required





:description: Description, text




Object: dm.overlay (dm.overlay)
###############################



:trademark_id: Trademark, many2one, required





:dealer_id: Dealer, many2one, required





:country_ids: Country, many2many, required





:code: Code, char, readonly





:payment_method_rule_ids: Payment Method Rules, many2many





:bank_account_id: Account, many2one




Object: dm.campaign (dm.campaign)
#################################



:code: Account Code, char





:cleaner_id: Cleaner, many2one

    *The cleaner is a partner responsible for removing bad addresses from the customers list*



:contact_id: Contact, many2one





:address_ids: Partners Contacts, many2many





:crossovered_budget_line: Budget Lines, one2many





:quantity_usable_total: Total Usable Quantity, char, readonly





:proposition_ids: Proposition, one2many





:last_worked_date: Date of Last Cost/Work, date, readonly

    *Date of the latest work done on this account.*



:dealer_id: Dealer, many2one

    *The dealer is the partner the campaign is planned for*



:manufacturing_cost_ids: Manufacturing Costs, one2many





:company_id: Company, many2one, required





:parent_id: Parent Analytic Account, many2one





:pricelist_id: Sale Pricelist, many2one





:project_id: Project, many2one, readonly

    *Generating the Retro Planning will create and assign the different tasks used to plan and manage the campaign*



:ca_to_invoice: Uninvoiced Amount, float, readonly

    *If invoice from analytic account, the remaining amount you can invoice to the customer based on the total costs.*



:cust_file_task_ids: Customer Files tasks, one2many





:payment_method_ids: Payment Methods, many2many





:child_ids: Child Accounts, one2many





:quantity_wanted_total: Total Wanted Quantity, char, readonly





:user_ids: User, many2many, readonly





:campaign_group_id: Campaign group, many2one





:item_task_ids: Items Procurement tasks, one2many





:theorical_margin: Theorical Margin, float, readonly

    *Computed using the formula: Theorial Revenue - Total Costs*



:dtp_task_ids: DTP tasks, one2many





:name: Account Name, char, required





:notes: Notes, text





:translation_state: Translation Status, selection, readonly





:quantity_planned_total: Total planned Quantity, char, readonly





:remaining_hours: Remaining Hours, float, readonly

    *Computed using the formula: Maximum Quantity - Hours Tot.*



:last_worked_invoiced_date: Date of Last Invoiced Cost, date, readonly

    *If invoice from the costs, this is the date of the latest work or cost that have been invoiced.*



:manufacturing_product_id: Manufacturing Product, many2one





:customer_file_state: Customers Files Status, selection, readonly





:last_invoice_date: Last Invoice Date, date, readonly

    *Date of the last invoice created for this analytic account.*



:dtp_purchase_line_ids: DTP Purchase Lines, one2many





:package_ok: Used in Package, boolean





:partner_id: Associated Partner, many2one





:analytic_account_id: Analytic Account, many2one





:revenue_per_hour: Revenue per Hours (real), float, readonly

    *Computed using the formula: Invoiced Amount / Hours Tot.*



:total_cost: Total Costs, float, readonly

    *Total of costs for this account. It includes real costs (from invoices) and indirect costs, like time spent on timesheets.*



:country_id: Country, many2one, required

    *The language and currency will be automatically assigned if they are defined for the country*



:state: State, selection, required





:debit: Debit, float, readonly





:amount_invoiced: Invoiced Amount, float, readonly

    *Total invoiced*



:planning_state: Planning Status, selection, readonly





:user_product_ids: Users/Products Rel., one2many





:manufacturing_responsible_id: Responsible, many2one





:overlay_id: Overlay, many2one





:active: Active, boolean





:mail_service_ids: Mailing Service, one2many





:real_margin_rate: Real Margin Rate (%), float, readonly

    *Computes using the formula: (Real Margin / Total Costs) * 100.*



:credit: Credit, float, readonly





:month_ids: Month, many2many, readonly





:line_ids: Analytic Entries, one2many





:items_state: Items Status, selection, readonly





:trademark_id: Trademark, many2one





:amount_max: Max. Invoice Price, float





:dtp_state: DTP Status, selection, readonly





:user_id: Account Manager, many2one





:dtp_responsible_id: Responsible, many2one





:manufacturing_purchase_line_ids: Manufacturing Purchase Lines, one2many





:type: Account Type, selection





:offer_id: Offer, many2one, required

    *Choose the commercial offer to use with this campaign, only offers in ready to plan or open state can be assigned*



:ca_invoiced: Invoiced Amount, float, readonly

    *Total customer invoiced amount for this account.*



:campaign_type_id: Type, many2one





:hours_quantity: Hours Tot, float, readonly

    *Number of hours you spent on the analytic account (from timesheet). It computes on all journal of type 'general'.*



:manufacturing_state: Manufacturing Status, selection, readonly





:ca_theorical: Theorical Revenue, float, readonly

    *Based on the costs you had on the project, what would the revenue have been if all these costs were invoiced at the normal sale price given by the pricelist.*



:currency_id: Currency, many2one





:dtp_making_time: Making Time, float, readonly





:to_invoice: Reinvoice Costs, many2one

    *Check this field if you plan to automatically generate invoices based on the costs in this analytic account: timesheets, expenses, ...You can configure an automatic invoice rate on analytic accounts.*



:balance: Balance, float, readonly





:quantity_delivered_total: Total Delivered Quantity, char, readonly





:item_responsible_id: Responsible, many2one





:quantity_max: Maximum Quantity, float





:deduplicator_id: Deduplicator, many2one

    *The deduplicator is a partner responsible for removing identical addresses from the customers list*



:company_currency_id: Currency, many2one, readonly





:hours_qtt_non_invoiced: Uninvoiced Hours, float, readonly

    *Number of hours (from journal of type 'general') that can be invoiced if you invoice based on analytic account.*



:files_responsible_id: Responsible, many2one





:date_start: Date Start, date





:forwarding_charge: Forwarding Charge, float





:lang_id: Language, many2one





:complete_name: Full Account Name, char, readonly





:real_margin: Real Margin, float, readonly

    *Computed using the formula: Invoiced Amount - Total Costs.*



:hours_qtt_invoiced: Invoiced Hours, float, readonly

    *Number of hours that can be invoiced plus those that already have been invoiced.*



:router_id: Router, many2one

    *The router is the partner who will send the mailing to the final customer*



:description: Description, text





:manufacturing_task_ids: Manufacturing tasks, one2many





:remaining_ca: Remaining Revenue, float, readonly

    *Computed using the formula: Max Invoice Price - Invoiced Amount.*



:responsible_id: Responsible, many2one





:date: Date End, date





:item_purchase_line_ids: Items Purchase Lines, one2many





:code1: Code, char, readonly





:cust_file_purchase_line_ids: Customer Files Purchase Lines, one2many





:journal_rate_ids: Invoicing Rate per Journal, one2many





:quantity: Quantity, float, readonly




Object: dm.campaign.proposition (dm.campaign.proposition)
#########################################################



:initial_proposition_id: Initial proposition, many2one





:code: Account Code, char





:last_worked_invoiced_date: Date of Last Invoiced Cost, date, readonly

    *If invoice from the costs, this is the date of the latest work or cost that have been invoiced.*



:ca_to_invoice: Uninvoiced Amount, float, readonly

    *If invoice from analytic account, the remaining amount you can invoice to the customer based on the total costs.*



:quantity_max: Maximum Quantity, float





:quantity_wanted: Wanted Quantity, char, readonly

    *The wanted quantity is the number of addresses you wish to get for that segment.
    This is usually the quantity used to order Customers Lists
    The wanted quantity could be AAA for All Addresses Available*



:contact_id: Contact, many2one





:company_currency_id: Currency, many2one, readonly





:date: Date End, date





:last_invoice_date: Last Invoice Date, date, readonly

    *Date of the last invoice created for this analytic account.*



:crossovered_budget_line: Budget Lines, one2many





:amount_max: Max. Invoice Price, float





:package_ok: Used in Package, boolean





:hours_qtt_non_invoiced: Uninvoiced Hours, float, readonly

    *Number of hours (from journal of type 'general') that can be invoiced if you invoice based on analytic account.*



:keep_prices: Keep Prices At Duplication, boolean





:partner_id: Associated Partner, many2one





:proposition_type: Type, selection





:analytic_account_id: Analytic Account, many2one





:last_worked_date: Date of Last Cost/Work, date, readonly

    *Date of the latest work done on this account.*



:starting_mail_price: Starting Mail Price, float





:user_id: Account Manager, many2one





:item_ids: Catalogue, one2many





:to_invoice: Reinvoice Costs, many2one

    *Check this field if you plan to automatically generate invoices based on the costs in this analytic account: timesheets, expenses, ...You can configure an automatic invoice rate on analytic accounts.*



:total_cost: Total Costs, float, readonly

    *Total of costs for this account. It includes real costs (from invoices) and indirect costs, like time spent on timesheets.*



:date_start: Date Start, date





:company_id: Company, many2one, required





:segment_ids: Segment, one2many





:parent_id: Parent Analytic Account, many2one





:state: State, selection, required





:quantity_planned: Planned Quantity, integer

    *The planned quantity is an estimation of the usable quantity of addresses you  will get after delivery, deduplication and cleaning
    This is usually the quantity used to order the manufacturing of the mailings*



:complete_name: Full Account Name, char, readonly





:real_margin: Real Margin, float, readonly

    *Computed using the formula: Invoiced Amount - Total Costs.*



:debit: Debit, float, readonly





:forwarding_charge: Forwarding Charge, float





:pricelist_id: Sale Pricelist, many2one





:type: Account Type, selection





:quantity: Quantity, float, readonly





:manufacturing_costs: Manufacturing Costs, float





:journal_rate_ids: Invoicing Rate per Journal, one2many





:payment_method_ids: Payment Methods, many2many





:description: Description, text





:amount_invoiced: Invoiced Amount, float, readonly

    *Total invoiced*



:forwarding_charges: Forwarding Charges, float





:credit: Credit, float, readonly





:child_ids: Child Accounts, one2many





:user_product_ids: Users/Products Rel., one2many





:ca_invoiced: Invoiced Amount, float, readonly

    *Total customer invoiced amount for this account.*



:sale_rate: Sale Rate (%), float

    *This is the planned sale rate (in percent) for this commercial proposition*



:user_ids: User, many2many, readonly





:remaining_ca: Remaining Revenue, float, readonly

    *Computed using the formula: Max Invoice Price - Invoiced Amount.*



:quantity_delivered: Delivered Quantity, char, readonly

    *The delivered quantity is the number of addresses you receive from the broker.*



:code1: Code, char, readonly





:hours_qtt_invoiced: Invoiced Hours, float, readonly

    *Number of hours that can be invoiced plus those that already have been invoiced.*



:active: Active, boolean





:hours_quantity: Hours Tot, float, readonly

    *Number of hours you spent on the analytic account (from timesheet). It computes on all journal of type 'general'.*



:theorical_margin: Theorical Margin, float, readonly

    *Computed using the formula: Theorial Revenue - Total Costs*



:quantity_usable: Usable Quantity, char, readonly

    *The usable quantity is the number of addresses you have after delivery, deduplication and cleaning.*



:ca_theorical: Theorical Revenue, float, readonly

    *Based on the costs you had on the project, what would the revenue have been if all these costs were invoiced at the normal sale price given by the pricelist.*



:force_sm_price: Force Starting Mail Price, boolean





:sm_price: Starting Mail Price, float





:keep_segments: Keep Segments, boolean





:name: Account Name, char, required





:customer_pricelist_id: Product Pricelist, many2one





:notes: Notes, text





:address_ids: Partners Contacts, many2many





:real_margin_rate: Real Margin Rate (%), float, readonly

    *Computes using the formula: (Real Margin / Total Costs) * 100.*



:revenue_per_hour: Revenue per Hours (real), float, readonly

    *Computed using the formula: Invoiced Amount / Hours Tot.*



:month_ids: Month, many2many, readonly





:quantity_real: Real Quantity, char, readonly

    *The real quantity is the actual number of addresses you get in the file.*



:price_prog_use: Price Progression, boolean





:line_ids: Analytic Entries, one2many





:balance: Balance, float, readonly





:camp_id: Campaign, many2one, required





:remaining_hours: Remaining Hours, float, readonly

    *Computed using the formula: Maximum Quantity - Hours Tot.*


Object: The origin of the addresses of a list (dm.customers_list.recruit_origin)
################################################################################



:code: Code, char, required





:name: Name, char, required




Object: Type of the adress list (dm.customers_list.type)
########################################################



:code: Code, char, required





:name: Name, char, required




Object: A list of addresses proposed by an addresses broker (dm.customers_list)
###############################################################################



:other_cost: Other Cost, float





:selection_cost: Selection Cost Per Thousand, float





:broker_cost: Broker Cost, float

    *The amount given to the broker for the list renting*



:code: Code, char, required





:list_type_id: Type, many2one





:per_thousand_price: Price per Thousand, float





:update_frq: Update Frequency, integer





:currency_id: Currency, many2one





:country_id: Country, many2one





:name: Name, char, required





:broker_discount: Broker Discount (%), float





:recruiting_origin_id: Recruiting Origin, many2one

    *Origin of the recruiting of the addresses*



:broker_id: Broker, many2one





:delivery_cost: Delivery Cost, float





:invoice_base: Invoicing based on, selection

    *Net or raw quantity on which the final invoice is based depending on the term negotiated with the broker.
    Net : Usable quantity after deduplication
    Raw : Delivered quantity
    Real : Realy used quantity*



:owner_id: Owner, many2one





:notes: Description, text





:product_id: Product, many2one, required




Object: A File of addresses (dm.customers_file)
###############################################



:address_ids: Customers File Addresses, many2many





:code: Code, char, required





:name: Name, char, required





:case_ids: CRM Cases, many2many





:note: Notes, text





:source: Source, selection, required





:customers_list_id: Customers List, many2one





:delivery_date: Delivery Date, date





:segment_ids: Segments, one2many, readonly




Object: A subset of addresses coming from a customers file (dm.campaign.proposition.segment)
############################################################################################



:code: Account Code, char





:last_worked_invoiced_date: Date of Last Invoiced Cost, date, readonly

    *If invoice from the costs, this is the date of the latest work or cost that have been invoiced.*



:ca_to_invoice: Uninvoiced Amount, float, readonly

    *If invoice from analytic account, the remaining amount you can invoice to the customer based on the total costs.*



:analytic_account_id: Analytic Account, many2one





:quantity_cleaned_cleaner: Cleaned Quantity, integer

    *The quantity of wrong addresses removed by the cleaner.*



:segmentation_criteria: Segmentation Criteria, text





:quantity_dedup_cleaner: Deduplication Quantity, integer

    *The quantity of duplicated addresses removed by the cleaner.*



:quantity_max: Maximum Quantity, float





:quantity_usable: Usable Quantity, integer, readonly

    *The usable quantity is the number of addresses you have after delivery, deduplication and cleaning.*



:contact_id: Contact, many2one





:company_currency_id: Currency, many2one, readonly





:date: Date End, date





:last_invoice_date: Last Invoice Date, date, readonly

    *Date of the last invoice created for this analytic account.*



:crossovered_budget_line: Budget Lines, one2many





:amount_max: Max. Invoice Price, float





:package_ok: Used in Package, boolean





:hours_qtt_non_invoiced: Uninvoiced Hours, float, readonly

    *Number of hours (from journal of type 'general') that can be invoiced if you invoice based on analytic account.*



:partner_id: Associated Partner, many2one





:all_add_avail: All Addresses Available, boolean

    *Used to order all addresses available in the customers list based on the segmentation criteria*



:split_id: Split, many2one





:note: Notes, text





:last_worked_date: Date of Last Cost/Work, date, readonly

    *Date of the latest work done on this account.*



:start_census: Start Census, integer

    *The recency is the time since the last purchase.
    For example : A 0-30 recency means all the customers that have purchased in the last 30 days*



:user_id: Account Manager, many2one





:to_invoice: Reinvoice Costs, many2one

    *Check this field if you plan to automatically generate invoices based on the costs in this analytic account: timesheets, expenses, ...You can configure an automatic invoice rate on analytic accounts.*



:total_cost: Total Costs, float, readonly

    *Total of costs for this account. It includes real costs (from invoices) and indirect costs, like time spent on timesheets.*



:quantity_purged: Purged Quantity, integer, readonly

    *The purged quantity is the number of addresses removed from deduplication and cleaning.*



:date_start: Date Start, date





:customers_file_id: Customers File, many2one





:company_id: Company, many2one, required





:proposition_id: Proposition, many2one





:reuse_id: Reuse, many2one





:parent_id: Parent Analytic Account, many2one





:state: State, selection, required





:customers_list_id: Customers List, many2one





:complete_name: Full Account Name, char, readonly





:real_margin: Real Margin, float, readonly

    *Computed using the formula: Invoiced Amount - Total Costs.*



:debit: Debit, float, readonly





:pricelist_id: Sale Pricelist, many2one





:type_src: Type, selection





:type: Account Type, selection





:quantity: Quantity, float, readonly





:quantity_cleaned_dedup: Cleaned Quantity, integer

    *The quantity of wrong addresses removed by the deduplicator.*



:journal_rate_ids: Invoicing Rate per Journal, one2many





:description: Description, text





:amount_invoiced: Invoiced Amount, float, readonly

    *Total invoiced*



:quantity_planned: planned Quantity, integer

    *The planned quantity is an estimation of the usable quantity of addresses you  will get after delivery, deduplication and cleaning
    This is usually the quantity used to order the manufacturing of the mailings*



:credit: Credit, float, readonly





:child_ids: Child Accounts, one2many





:user_product_ids: Users/Products Rel., one2many





:ca_invoiced: Invoiced Amount, float, readonly

    *Total customer invoiced amount for this account.*



:user_ids: User, many2many, readonly





:remaining_ca: Remaining Revenue, float, readonly

    *Computed using the formula: Max Invoice Price - Invoiced Amount.*



:quantity_delivered: Delivered Quantity, integer

    *The delivered quantity is the number of addresses you receive from the broker.*



:code1: Code, char, readonly





:hours_qtt_invoiced: Invoiced Hours, float, readonly

    *Number of hours that can be invoiced plus those that already have been invoiced.*



:active: Active, boolean





:hours_quantity: Hours Tot, float, readonly

    *Number of hours you spent on the analytic account (from timesheet). It computes on all journal of type 'general'.*



:deduplication_level: Deduplication Level, integer

    *The deduplication level defines the order in which the deduplication takes place.*



:theorical_margin: Theorical Margin, float, readonly

    *Computed using the formula: Theorial Revenue - Total Costs*



:ca_theorical: Theorical Revenue, float, readonly

    *Based on the costs you had on the project, what would the revenue have been if all these costs were invoiced at the normal sale price given by the pricelist.*



:quantity_wanted: Wanted Quantity, integer

    *The wanted quantity is the number of addresses you wish to get for that segment.
    This is usually the quantity used to order Customers Lists
    The wanted quantity could be AAA for All Addresses Available*



:type_census: Census Type, selection





:name: Account Name, char, required





:end_census: End Census, integer





:address_ids: Partners Contacts, many2many





:real_margin_rate: Real Margin Rate (%), float, readonly

    *Computes using the formula: (Real Margin / Total Costs) * 100.*



:revenue_per_hour: Revenue per Hours (real), float, readonly

    *Computed using the formula: Invoiced Amount / Hours Tot.*



:quantity_dedup_dedup: Deduplication Quantity, integer

    *The quantity of duplicated addresses removed by the deduplicator.*



:month_ids: Month, many2many, readonly





:quantity_real: Real Quantity, integer

    *The real quantity is the actual number of addresses in the customers file (by counting).*



:line_ids: Analytic Entries, one2many





:balance: Balance, float, readonly





:remaining_hours: Remaining Hours, float, readonly

    *Computed using the formula: Maximum Quantity - Hours Tot.*


Object: dm.campaign.proposition.item (dm.campaign.proposition.item)
###################################################################



:product_id: Product, many2one, required





:price: Sale Price, float





:qty_real: Real Quantity, integer





:proposition_id: Commercial Proposition, many2one





:qty_planned: Planned Quantity, integer





:item_type: Product Type, selection





:offer_step_type_id: Offer Step Type, many2one





:notes: Notes, text




Object: dm.campaign.purchase_line (dm.campaign.purchase_line)
#############################################################



:type_document: Document Type, selection





:campaign_group_id: Campaign Group, many2one





:product_id: Product, many2one, required





:togroup: Apply to Campaign Group, boolean





:product_category: Product Category, selection





:trigger: Trigger, selection





:notes: Notes, text





:date_planned: Scheduled date, datetime, required





:campaign_id: Campaign, many2one





:date_delivery: Delivery Date, datetime, readonly





:uom_id: UOM, many2one, required





:desc_from_offer: Insert Description from Offer, boolean





:state: State, selection, readonly





:type_quantity: Quantity Type, selection





:quantity_warning: Warning, char, readonly





:purchase_order_ids: Campaign Purchase Line, one2many





:date_order: Order date, datetime, readonly





:type: Type, selection





:quantity: Total Quantity, integer, required




Object: dm.campaign.manufacturing_cost (dm.campaign.manufacturing_cost)
#######################################################################



:amount: Amount, float





:name: Description, char, required





:campaign_id: Campaign, many2one




Object: dm.campaign.proposition.prices_progression (dm.campaign.proposition.prices_progression)
###############################################################################################



:percent_prog: Percentage Prices Progression, float





:fixed_prog: Fixed Prices Progression, float





:name: Name, char, required




Object: dm.campaign.document.type (dm.campaign.document.type)
#############################################################



:code: Code, char, required





:name: Name, char, required




Object: dm.campaign.document (dm.campaign.document)
###################################################



:segment_id: Segment, many2one, required





:name: Name, char, required





:type_id: Format, many2one, required




Object: dm.order (dm.order)
###########################



:customer_code: Customer Code, char





:zip: Zip Code, char





:segment_code: Segment Code, char





:country: Country, char





:offer_step_code: Offer Step Code, char





:title: Title, char





:customer_firstname: First Name, char





:customer_add4: Address4, char





:state: Status, selection, readonly





:zip_summary: Zip Summary, char





:customer_lastname: Last Name, char





:customer_add1: Address1, char





:raw_datas: Raw Data, char





:distribution_office: Distribution Office, char





:customer_add2: Address2, char





:customer_add3: Address3, char




Object: Sale Order (dm.customer.order)
######################################



:origin: Origin, char





:order_line: Order Lines, one2many, readonly





:picking_policy: Packing Policy, selection, required

    *If you don't have enough stock available to deliver all at once, do you accept partial shipments or not?*



:order_policy: Shipping Policy, selection, required, readonly

    *The Shipping Policy is used to synchronise invoice and delivery operations.
    - The 'Pay before delivery' choice will first generate the invoice and then generate the packing order after the payment of this invoice.
    - The 'Shipping & Manual Invoice' will create the packing order directly and wait for the user to manually click on the 'Invoice' button to generate the draft invoice.
    - The 'Invoice on Order After Delivery' choice will generate the draft invoice based on sale order after all packing lists have been finished.
    - The 'Invoice from the packing' choice is used to create an invoice during the packing process.*



:invoice_ids: Invoice, many2many

    *This is the list of invoices that have been generated for this sale order. The same sale order may have been invoiced in several times (by line for example).*



:shop_id: Shop, many2one, required, readonly





:client_order_ref: Customer Ref, char





:date_order: Date Ordered, date, required, readonly





:partner_id: Customer, many2one, readonly





:invoiced: Paid, boolean, readonly





:note: Notes, text





:fiscal_position: Fiscal Position, many2one





:user_id: Salesman, many2one





:payment_term: Payment Term, many2one





:amount_tax: Taxes, float, readonly





:offer_step_id: Offer Step, many2one





:state: Status, selection, readonly





:abstract_line_ids: Order Lines, one2many, readonly





:invoiced_rate: Invoiced, float, readonly





:pricelist_id: Pricelist, many2one, required, readonly





:advertising_agency: Advertising Agency, many2one





:project_id: Analytic Account, many2one, readonly





:incoterm: Incoterm, selection





:published_customer: Published Customer, many2one





:partner_order_id: Ordering Contact, many2one, required, readonly

    *The name and address of the contact that requested the order or quotation.*



:picked_rate: Picked, float, readonly





:partner_invoice_id: Invoice Address, many2one, required, readonly





:amount_untaxed: Untaxed Amount, float, readonly





:picking_ids: Related Packing, one2many, readonly

    *This is the list of picking list that have been generated for this invoice*



:amount_total: Total, float, readonly





:customer_id: Customer, many2one





:name: Order Description, char, required





:partner_shipping_id: Shipping Address, many2one, required, readonly





:segment_id: Segment, many2one





:price_type: Price method, selection, required





:shipped: Picked, boolean, readonly





:invoice_quantity: Invoice on, selection, required

    *The sale order will automatically create the invoice proposition (draft invoice). Ordered and delivered quantities may not be the same. You have to choose if you invoice based on ordered or shipped quantities. If the product is a service, shipped quantities means hours spent on the associated tasks.*



:discount_campaign: Discount Campaign, many2one





:margin: Margin, float, readonly




Object: dm.customer.gender (dm.customer.gender)
###############################################



:code: Code, char, readonly





:name: Name, char





:to_gender_id: To Gender, many2one, required





:lang_id: Language, many2one





:from_gender_id: From Gender, many2one





:description: Description, text




Object: workitem (dm.workitem)
##############################



:action_time: Action Time, datetime





:address_id: Customer Address, many2one





:segment_id: Segments, many2one





:source: Source, selection, required





:state: Status, selection





:case_id: CRM Case, many2one





:tr_from_id: Source Transition, many2one





:step_id: Offer Step, many2one





:error_msg: System Message, text




Object: Segmentation (dm.customer.segmentation)
###############################################



:customer_date_criteria_ids: Customers Date Criteria, one2many





:order_text_criteria_ids: Customers Order Textual Criteria, one2many





:code: Code, char, required





:name: Name, char, required





:notes: Description, text





:order_boolean_criteria_ids: Customers Order Boolean Criteria, one2many





:order_numeric_criteria_ids: Customers Order Numeric Criteria, one2many





:customer_numeric_criteria_ids: Customers Numeric Criteria, one2many





:customer_boolean_criteria_ids: Customers Boolean Criteria, one2many





:sql_query: SQL Query, text





:order_date_criteria_ids: Customers Order Date Criteria, one2many





:customer_text_criteria_ids: Customers Textual Criteria, one2many




Object: Customer Segmentation Textual Criteria (dm.customer.text_criteria)
##########################################################################



:operator: Operator, selection





:segmentation_id: Segmentation, many2one





:field_id: Customers Field, many2one





:value: Value, char




Object: Customer Segmentation Numeric Criteria (dm.customer.numeric_criteria)
#############################################################################



:operator: Operator, selection





:segmentation_id: Segmentation, many2one





:field_id: Customers Field, many2one





:value: Value, float




Object: Customer Segmentation Boolean Criteria (dm.customer.boolean_criteria)
#############################################################################



:operator: Operator, selection





:segmentation_id: Segmentation, many2one





:field_id: Customers Field, many2one





:value: Value, selection




Object: Customer Segmentation Date Criteria (dm.customer.date_criteria)
#######################################################################



:operator: Operator, selection





:segmentation_id: Segmentation, many2one





:field_id: Customers Field, many2one





:value: Date, date




Object: Customer Order Segmentation Textual Criteria (dm.customer.order.text_criteria)
######################################################################################



:operator: Operator, selection





:segmentation_id: Segmentation, many2one





:field_id: Customers Field, many2one





:value: Value, char




Object: Customer Order Segmentation Numeric Criteria (dm.customer.order.numeric_criteria)
#########################################################################################



:operator: Operator, selection





:segmentation_id: Segmentation, many2one





:field_id: Customers Field, many2one





:value: Value, float




Object: Customer Order Segmentation Boolean Criteria (dm.customer.order.boolean_criteria)
#########################################################################################



:operator: Operator, selection





:segmentation_id: Segmentation, many2one





:field_id: Customers Field, many2one





:value: Value, selection




Object: Customer Order Segmentation Date Criteria (dm.customer.order.date_criteria)
###################################################################################



:operator: Operator, selection





:segmentation_id: Segmentation, many2one





:field_id: Customers Field, many2one





:value: Date, date




Object: dm.offer.history (dm.offer.history)
###########################################



:date: Drop Date, date





:offer_id: Offer, many2one, required





:code: Code, char





:campaign_id: Name, many2one





:responsible_id: Responsible, many2one




Object: dm.event (dm.event)
###########################



:address_id: Address, many2one





:segment_id: Segment, many2one, required





:campaign_id: Campaign, many2one





:source: Source, selection, required





:trigger_type_id: Trigger Condition, many2one, required





:step_id: Offer Step, many2one, required




Object: dm.ddf.plugin (dm.ddf.plugin)
#####################################



:model_id: Object, many2one





:code: Code, char, required





:name: DDF Plugin Name, char





:store_value: Store Value, boolean





:field_id: Customers Field, many2one





:note: Description, text





:argument_ids: Argument List, one2many





:file_id: File Content, binary





:file_fname: Filename, char





:type: Type, selection, required




Object: Argument List (dm.plugin.argument)
##########################################



:name: Argument Name, char, required





:stored_plugin: Value from plugin, boolean





:value: Argument Value, text





:note: Description, text, readonly





:plugin_id: Plugin, many2one





:custome_plugin_id: Plugin For Value, many2one




Object: dm.document.template (dm.document.template)
###################################################



:plugin_ids: Plugin, many2many





:note: Description, text





:name: Template Name, char




Object: dm.plugins.value (dm.plugins.value)
###########################################



:date: Date, date





:plugin_id: Plugin, many2one





:customer_id: Customer Name, many2one





:value: Value, char




Object: dm.offer.document.category (dm.offer.document.category)
###############################################################



:parent_id: Parent, many2one





:complete_name: Category, char, readonly





:name: Name, char, required




Object: dm.offer.document (dm.offer.document)
#############################################



:gender_id: Gender, many2one





:code: Code, char, required





:media_id: Media, char





:name: Name, char, required





:document_template_plugin_ids: Dynamic Plugins, many2many





:lang_id: Language, many2one





:content: Content, text





:state: Status, selection, readonly





:copywriter_id: Copywriter, many2one





:editor: Editor, selection





:has_attachment: Has Attachment, char, readonly





:document_template_id: Document Template, many2one





:step_id: Offer Step, many2one





:category_id: Category, many2one





:note: Description, text





:subject: Subject, char




Object: dm.mail_service (dm.mail_service)
#########################################



:unit_interval: Interval Unit, selection





:media_id: Media, many2one





:action_interval: Interval, integer





:default_for_media: Default Mail Service for Media, boolean





:action_id: Server Action, many2one





:partner_id: Partner, many2one





:name: Name, char, readonly




Object: dm.campaign.mail_service (dm.campaign.mail_service)
###########################################################



:offer_step_id: Offer Step, many2one





:mail_service_id: Mail Service, many2one





:campaign_id: Campaign, many2one


