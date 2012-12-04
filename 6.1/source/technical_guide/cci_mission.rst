
.. module:: cci_mission
    :synopsis: CCI mission 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/cci_mission"></div>
    <script src="http://js-kit.com/ratings.js"></script>

CCI mission (*cci_mission*)
===========================
:Module: cci_mission
:Name: CCI mission
:Version: 5.0.1.0
:Author: Tiny
:Directory: cci_mission
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  specific module for cci project.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/cci_mission.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/cci_mission.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`crm`
 * :mod:`cci_partner`
 * :mod:`product`
 * :mod:`membership`
 * :mod:`sale`
 * :mod:`cci_event`
 * :mod:`cci_account`
 * :mod:`cci_translation`
 * :mod:`cci_country`

Reports
-------

None


Menus
-------

 * Missions
 * Missions/Configuration/Dossier Types
 * Missions/Configuration/Site
 * Missions/Configuration/Search Entries/Dossier
 * Missions/Embassy Folder
 * Missions/Configuration/Search Entries/Embassy Folder Lines
 * Missions/Configuration/Custom Codes
 * Missions/Legalizations
 * Missions/Certificates
 * Missions/Configuration/ATA Usage
 * Missions/Configuration/Search Entries/Letters Log
 * Missions/ATA Carnet
 * Missions/Incompleted Certificates
 * Financial Management/Periodical Processing/Group Draft Invoices for Missions and Events

Views
-----

 * \* INHERIT res.partner.form (form)
 * cci_missions.dossier_type.form (form)
 * cci_missions.dossier_type.tree (tree)
 * cci_missions.site.form (form)
 * cci_missions.site.tree (tree)
 * cci_missions.dossier.form (form)
 * cci_missions.dossier.tree (tree)
 * cci_missions.embassy_folder.form (form)
 * cci_missions.embassy_folder.tree (tree)
 * cci_missions.embassy_folder_line.form (form)
 * cci_missions.embassy_folder_line.tree (tree)
 * cci_missions.custom_code.form (form)
 * cci_missions.custom_code.tree (tree)
 * cci_missions.legalization.form (form)
 * cci_missions.legalization.tree (tree)
 * cci_missions.certificate.form (form)
 * cci_missions.certificate.tree (tree)
 * cci_missions.ata_usage.form (form)
 * cci_missions.ata_usage.tree (tree)
 * cci_missions.letters_log.form (form)
 * cci_missions.letters_log.tree (tree)
 * cci_missions.ata_carnet.form (form)
 * cci_missions.ata_carnet.tree (tree)
 * product.lines.tree (tree)
 * product.lines.form (form)


Objects
-------

Object: cci_missions.site (cci_missions.site)
#############################################



:name: Name of the Site, char, required





:embassy_sequence_id: Sequence for Embassy Folder, many2one, required





:official_name_4: Official Name of the Site, char





:official_name_1: Official Name of the Site, char, required





:official_name_3: Official Name of the Site, char





:official_name_2: Official Name of the Site, char




Object: cci_missions.embassy_folder (cci_missions.embassy_folder)
#################################################################



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





:customer_reference: Folders Reference for the Customer, char





:active: Active, boolean





:member_price: Member Price Allowed, boolean





:destination_id: Destination Country, many2one





:date: Date, datetime





:invoice_note: Note to Display on the Invoice, text

    *to display as the last embassy_folder_line of this embassy_folder.*



:crm_case_id: Case, many2one





:planned_revenue: Planned Revenue, float





:id: ID, integer, readonly





:date_action_next: Next Action, datetime, readonly





:invoice_id: Invoice, many2one





:link_ids: Linked Documents, one2many





:user_id: Responsible, many2one





:name: Description, char, required





:date_deadline: Deadline, datetime





:invoice_date: Invoice Date, datetime, readonly





:partner_id: Partner, many2one





:embassy_folder_line_ids: Details, one2many





:categ_id: Category, many2one





:priority: Priority, selection





:state: Status, selection, readonly





:site_id: Site, many2one, required





:email_last: Latest E-Mail, text, readonly





:email_cc: Watchers Emails, char





:internal_note: Internal Note, text





:ref: Reference, reference





:email_from: Partner Email, char





:log_ids: Logs History, one2many, readonly




Object: cci_missions.embassy_folder_line  (cci_missions.embassy_folder_line)
############################################################################



:awex_amount: AWEX Amount, float, readonly





:credit_line_id: Credit Line, many2one, readonly





:name: Description, char, required





:type: Type, selection, required





:awex_eligible: AWEX Eligible, boolean





:tax_rate: Tax Rate, many2one





:folder_id: Related Embassy Folder, many2one, required





:courier_cost: Couriers Costs, float





:customer_amount: Invoiced Amount, float





:account_id: Account, many2one, required




Object: cci_missions.dossier_type (cci_missions.dossier_type)
#############################################################



:code: Code, char, required





:name: Description, char, required





:copy_product_id: Reference for Copies, many2one, required

    *for the association with a pricelist*



:id_letter: ID Letter, char

    *for identify the type of certificate by the federation*



:section: Type, selection, required





:site_id: Site, many2one, required





:sequence_id: Sequence, many2one, required

    *for association with a sequence*



:warranty_product_2: Warranty product for ATA carnet if not own Risk, many2one





:warranty_product_1: Warranty product for ATA carnet if Own Risk, many2one





:original_product_id: Reference for Original Copies, many2one, required

    *for the association with a pricelist*


Object: cci_missions.dossier (cci_missions.dossier)
###################################################



:goods: Goods Description, char





:embassy_folder_id: Related Embassy Folder, many2one





:name: Reference, char, required





:quantity_original: Quantity of Originals, integer, required





:type_id: Dossier Type, many2one, required





:sender_name: Sender Name, char





:invoiced_amount: Total, float





:sub_total: Sub Total for Extra Products, float, readonly





:order_partner_id: Billed Customer, many2one, required





:to_bill: To Be Billed, boolean





:state: State, selection





:product_ids: Products, one2many





:destination_id: Destination Country, many2one





:invoice_id: Invoice, many2one





:date: Creation Date, date, required





:quantity_copies: Number of Copies, integer





:text_on_invoice: Text to Display on the Invoice, text





:id: ID, integer, readonly





:asker_name: Asker Name, char





:goods_value: Value of the Sold Goods, float




Object: cci_missions.custom_code (cci_missions.custom_code)
###########################################################



:meaning: Meaning, text, required





:official: Official Code, boolean





:name: Name, char, required




Object: cci_missions.certificate (cci_missions.certificate)
###########################################################



:embassy_folder_id: Related Embassy Folder, many2one





:legalization_ids: Related Legalizations, one2many





:type_id: Dossier Type, many2one, required





:sender_name: Sender Name, char





:invoiced_amount: Total, float





:asker_name: Asker Name, char





:sub_total: Sub Total for Extra Products, float, readonly





:asker_zip_id: Asker Zip Code, many2one





:asker_address: Asker Address, char





:origin_ids: Origin Countries, many2many





:destination_id: Destination Country, many2one





:date: Creation Date, date, required





:total: Total, float, readonly





:text_on_invoice: Text to Display on the Invoice, text





:id: ID, integer, readonly





:special_reason: For special cases, selection





:goods: Goods Description, char





:name: Reference, char, required





:quantity_original: Quantity of Originals, integer, required





:invoice_id: Invoice, many2one





:customs_ids: Custom Codes, many2many





:state: State, selection





:dossier_id: Dossier, many2one





:order_partner_id: Billed Customer, many2one, required





:sending_spf: SPF Sending Date, date

    *Date of the sending of this record to the external database*



:quantity_copies: Number of Copies, integer





:goods_value: Value of the Sold Goods, float





:to_bill: To Be Billed, boolean





:product_ids: Products, one2many




Object: cci_missions.legalization (cci_missions.legalization)
#############################################################



:embassy_folder_id: Related Embassy Folder, many2one





:type_id: Dossier Type, many2one, required





:sender_name: Sender Name, char





:invoiced_amount: Total, float





:asker_name: Asker Name, char





:sub_total: Sub Total for Extra Products, float, readonly





:partner_member_state: Member State of the Partner, selection, readonly





:member_price: Apply the Member Price, boolean





:destination_id: Destination Country, many2one





:date: Creation Date, date, required





:total: Total, float, readonly





:text_on_invoice: Text to Display on the Invoice, text





:id: ID, integer, readonly





:goods: Goods Description, char





:name: Reference, char, required





:quantity_original: Quantity of Originals, integer, required





:invoice_id: Invoice, many2one





:state: State, selection





:dossier_id: Dossier, many2one





:order_partner_id: Billed Customer, many2one, required





:certificate_id: Related Certificate, many2one





:quantity_copies: Number of Copies, integer





:goods_value: Value of the Sold Goods, float





:to_bill: To Be Billed, boolean





:product_ids: Products, one2many




Object: cci_missions.courier_log (cci_missions.courier_log)
###########################################################



:documents_certificate: List of Certificates, text





:embassy_folder_id: Related Embassy Folder, many2one, required





:qtty_to_print: Number of Sheets, integer





:copy_cba: Photocopy Before CBA, boolean





:cba: CBA, boolean





:message: Message to the Courier, text





:address_street: Street, char





:documents: Number of Documents to Legalize, integer





:address_name_1: Company Name, char





:address_name_2: Contact Name, char





:consulate_name: Consulate Name, char





:documents_invoice: List of Invoices, text





:partner_address_id: Courier, many2one





:copy_ministry: Photocopy Before Ministry, boolean





:others: Others, char





:translation: Translation, boolean





:address_city: City, char





:ministry: Ministry, boolean





:return_address: Address of Return, selection, required





:embassy_name: Embassy Name, char





:documents_others: Others, text





:copy_embassy_consulate: Photocopy Before Embassy or Consulate, boolean




Object: cci_missions.ata_usage (cci_missions.ata_usage)
#######################################################



:name: Usage, char, required




Object: cci_missions.ata_carnet (cci_missions.ata_carnet)
#########################################################



:warranty: Warranty, float, readonly





:area_id: Area, many2one, required





:type_id: Related Type of Carnet, many2one, required





:member_price: Apply the Member Price, boolean





:partner_member_state: Member State of the Partner, selection, readonly





:creation_date: Emission Date, date, required





:ok_state_date: Date of Closure, date





:partner_id: Partner, many2one, required





:id: ID, integer, readonly





:usage_id: Usage, many2one, required





:federation_sending_date: Date of Sending to the Federation, date, readonly





:representer_name: Representer Name, char





:representer_city: Representer City, char





:warranty_product_id: Related Warranty Product, many2one, required





:initial_pages: Initial Number of Pages, integer, required





:state: State, selection, required, readonly





:representer_address: Representer Address, char





:insurer_agreement: Insurer Agreement, char





:double_signature: Double Signature, boolean





:additional_pages: Additional Number of Pages, integer





:goods_value: Goods Value, float, required





:holder_name: Holder Name, char





:sub_total: Subtotal of Extra Products, float, readonly





:validity_date: Validity Date, date, required





:holder_city: Holder City, char





:product_ids: Products, one2many





:holder_address: Holder Address, char





:letter_ids: Letters, one2many





:goods: Goods, char





:name: Name, char, required





:invoice_id: Invoice, many2one





:partner_insurer_id: Insurer ID of the Partner, float, readonly





:return_date: Date of Return, date





:own_risk: Own Risks, boolean




Object: cci_missions.letters_log (cci_missions.letters_log)
###########################################################



:date: Date of Sending, date, required





:letter_type: Type of Letter, selection, required





:ata_carnet_id: Related ATA Carnet, many2one, required




Object: Product Lines (product.lines)
#####################################



:uos_id: Unit, many2one





:name: Description, char, required





:product_line_id: Product Ref, many2one





:price_unit: Unit Price, float, required





:price_subtotal: Subtotal, float, readonly





:dossier_product_line_id: Product Ref, many2one





:quantity: Quantity, float, required





:product_id: Product, many2one, required





:account_id: Account, many2one, required


