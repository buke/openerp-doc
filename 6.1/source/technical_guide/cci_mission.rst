
.. i18n: .. module:: cci_mission
.. i18n:     :synopsis: CCI mission 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: cci_mission
    :synopsis: CCI mission 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/cci_mission"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/cci_mission"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: CCI mission (*cci_mission*)
.. i18n: ===========================
.. i18n: :Module: cci_mission
.. i18n: :Name: CCI mission
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: cci_mission
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   specific module for cci project.
..

::

  specific module for cci project.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/cci_mission.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/cci_mission.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/cci_mission.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/cci_mission.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`crm`
.. i18n:  * :mod:`cci_partner`
.. i18n:  * :mod:`product`
.. i18n:  * :mod:`membership`
.. i18n:  * :mod:`sale`
.. i18n:  * :mod:`cci_event`
.. i18n:  * :mod:`cci_account`
.. i18n:  * :mod:`cci_translation`
.. i18n:  * :mod:`cci_country`
..

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

.. i18n:  * Missions
.. i18n:  * Missions/Configuration/Dossier Types
.. i18n:  * Missions/Configuration/Site
.. i18n:  * Missions/Configuration/Search Entries/Dossier
.. i18n:  * Missions/Embassy Folder
.. i18n:  * Missions/Configuration/Search Entries/Embassy Folder Lines
.. i18n:  * Missions/Configuration/Custom Codes
.. i18n:  * Missions/Legalizations
.. i18n:  * Missions/Certificates
.. i18n:  * Missions/Configuration/ATA Usage
.. i18n:  * Missions/Configuration/Search Entries/Letters Log
.. i18n:  * Missions/ATA Carnet
.. i18n:  * Missions/Incompleted Certificates
.. i18n:  * Financial Management/Periodical Processing/Group Draft Invoices for Missions and Events
..

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

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT res.partner.form (form)
.. i18n:  * cci_missions.dossier_type.form (form)
.. i18n:  * cci_missions.dossier_type.tree (tree)
.. i18n:  * cci_missions.site.form (form)
.. i18n:  * cci_missions.site.tree (tree)
.. i18n:  * cci_missions.dossier.form (form)
.. i18n:  * cci_missions.dossier.tree (tree)
.. i18n:  * cci_missions.embassy_folder.form (form)
.. i18n:  * cci_missions.embassy_folder.tree (tree)
.. i18n:  * cci_missions.embassy_folder_line.form (form)
.. i18n:  * cci_missions.embassy_folder_line.tree (tree)
.. i18n:  * cci_missions.custom_code.form (form)
.. i18n:  * cci_missions.custom_code.tree (tree)
.. i18n:  * cci_missions.legalization.form (form)
.. i18n:  * cci_missions.legalization.tree (tree)
.. i18n:  * cci_missions.certificate.form (form)
.. i18n:  * cci_missions.certificate.tree (tree)
.. i18n:  * cci_missions.ata_usage.form (form)
.. i18n:  * cci_missions.ata_usage.tree (tree)
.. i18n:  * cci_missions.letters_log.form (form)
.. i18n:  * cci_missions.letters_log.tree (tree)
.. i18n:  * cci_missions.ata_carnet.form (form)
.. i18n:  * cci_missions.ata_carnet.tree (tree)
.. i18n:  * product.lines.tree (tree)
.. i18n:  * product.lines.form (form)
..

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

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: cci_missions.site (cci_missions.site)
.. i18n: #############################################
..

Object: cci_missions.site (cci_missions.site)
#############################################

.. i18n: :name: Name of the Site, char, required
..

:name: Name of the Site, char, required

.. i18n: :embassy_sequence_id: Sequence for Embassy Folder, many2one, required
..

:embassy_sequence_id: Sequence for Embassy Folder, many2one, required

.. i18n: :official_name_4: Official Name of the Site, char
..

:official_name_4: Official Name of the Site, char

.. i18n: :official_name_1: Official Name of the Site, char, required
..

:official_name_1: Official Name of the Site, char, required

.. i18n: :official_name_3: Official Name of the Site, char
..

:official_name_3: Official Name of the Site, char

.. i18n: :official_name_2: Official Name of the Site, char
..

:official_name_2: Official Name of the Site, char

.. i18n: Object: cci_missions.embassy_folder (cci_missions.embassy_folder)
.. i18n: #################################################################
..

Object: cci_missions.embassy_folder (cci_missions.embassy_folder)
#################################################################

.. i18n: :date_closed: Closed, datetime, readonly
..

:date_closed: Closed, datetime, readonly

.. i18n: :history_line: Communication, one2many, readonly
..

:history_line: Communication, one2many, readonly

.. i18n: :ref2: Reference 2, reference
..

:ref2: Reference 2, reference

.. i18n: :create_date: Created, datetime, readonly
..

:create_date: Created, datetime, readonly

.. i18n: :description: Your action, text
..

:description: Your action, text

.. i18n: :probability: Probability (%), float
..

:probability: Probability (%), float

.. i18n: :canal_id: Channel, many2one
..

:canal_id: Channel, many2one

.. i18n: :date_action_last: Last Action, datetime, readonly
..

:date_action_last: Last Action, datetime, readonly

.. i18n: :planned_cost: Planned Costs, float
..

:planned_cost: Planned Costs, float

.. i18n: :partner_address_id: Partner Contact, many2one
..

:partner_address_id: Partner Contact, many2one

.. i18n: :som: State of Mind, many2one
..

:som: State of Mind, many2one

.. i18n: :section_id: Section, many2one, required
..

:section_id: Section, many2one, required

.. i18n: :customer_reference: Folders Reference for the Customer, char
..

:customer_reference: Folders Reference for the Customer, char

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :member_price: Member Price Allowed, boolean
..

:member_price: Member Price Allowed, boolean

.. i18n: :destination_id: Destination Country, many2one
..

:destination_id: Destination Country, many2one

.. i18n: :date: Date, datetime
..

:date: Date, datetime

.. i18n: :invoice_note: Note to Display on the Invoice, text
..

:invoice_note: Note to Display on the Invoice, text

.. i18n:     *to display as the last embassy_folder_line of this embassy_folder.*
..

    *to display as the last embassy_folder_line of this embassy_folder.*

.. i18n: :crm_case_id: Case, many2one
..

:crm_case_id: Case, many2one

.. i18n: :planned_revenue: Planned Revenue, float
..

:planned_revenue: Planned Revenue, float

.. i18n: :id: ID, integer, readonly
..

:id: ID, integer, readonly

.. i18n: :date_action_next: Next Action, datetime, readonly
..

:date_action_next: Next Action, datetime, readonly

.. i18n: :invoice_id: Invoice, many2one
..

:invoice_id: Invoice, many2one

.. i18n: :link_ids: Linked Documents, one2many
..

:link_ids: Linked Documents, one2many

.. i18n: :user_id: Responsible, many2one
..

:user_id: Responsible, many2one

.. i18n: :name: Description, char, required
..

:name: Description, char, required

.. i18n: :date_deadline: Deadline, datetime
..

:date_deadline: Deadline, datetime

.. i18n: :invoice_date: Invoice Date, datetime, readonly
..

:invoice_date: Invoice Date, datetime, readonly

.. i18n: :partner_id: Partner, many2one
..

:partner_id: Partner, many2one

.. i18n: :embassy_folder_line_ids: Details, one2many
..

:embassy_folder_line_ids: Details, one2many

.. i18n: :categ_id: Category, many2one
..

:categ_id: Category, many2one

.. i18n: :priority: Priority, selection
..

:priority: Priority, selection

.. i18n: :state: Status, selection, readonly
..

:state: Status, selection, readonly

.. i18n: :site_id: Site, many2one, required
..

:site_id: Site, many2one, required

.. i18n: :email_last: Latest E-Mail, text, readonly
..

:email_last: Latest E-Mail, text, readonly

.. i18n: :email_cc: Watchers Emails, char
..

:email_cc: Watchers Emails, char

.. i18n: :internal_note: Internal Note, text
..

:internal_note: Internal Note, text

.. i18n: :ref: Reference, reference
..

:ref: Reference, reference

.. i18n: :email_from: Partner Email, char
..

:email_from: Partner Email, char

.. i18n: :log_ids: Logs History, one2many, readonly
..

:log_ids: Logs History, one2many, readonly

.. i18n: Object: cci_missions.embassy_folder_line  (cci_missions.embassy_folder_line)
.. i18n: ############################################################################
..

Object: cci_missions.embassy_folder_line  (cci_missions.embassy_folder_line)
############################################################################

.. i18n: :awex_amount: AWEX Amount, float, readonly
..

:awex_amount: AWEX Amount, float, readonly

.. i18n: :credit_line_id: Credit Line, many2one, readonly
..

:credit_line_id: Credit Line, many2one, readonly

.. i18n: :name: Description, char, required
..

:name: Description, char, required

.. i18n: :type: Type, selection, required
..

:type: Type, selection, required

.. i18n: :awex_eligible: AWEX Eligible, boolean
..

:awex_eligible: AWEX Eligible, boolean

.. i18n: :tax_rate: Tax Rate, many2one
..

:tax_rate: Tax Rate, many2one

.. i18n: :folder_id: Related Embassy Folder, many2one, required
..

:folder_id: Related Embassy Folder, many2one, required

.. i18n: :courier_cost: Couriers Costs, float
..

:courier_cost: Couriers Costs, float

.. i18n: :customer_amount: Invoiced Amount, float
..

:customer_amount: Invoiced Amount, float

.. i18n: :account_id: Account, many2one, required
..

:account_id: Account, many2one, required

.. i18n: Object: cci_missions.dossier_type (cci_missions.dossier_type)
.. i18n: #############################################################
..

Object: cci_missions.dossier_type (cci_missions.dossier_type)
#############################################################

.. i18n: :code: Code, char, required
..

:code: Code, char, required

.. i18n: :name: Description, char, required
..

:name: Description, char, required

.. i18n: :copy_product_id: Reference for Copies, many2one, required
..

:copy_product_id: Reference for Copies, many2one, required

.. i18n:     *for the association with a pricelist*
..

    *for the association with a pricelist*

.. i18n: :id_letter: ID Letter, char
..

:id_letter: ID Letter, char

.. i18n:     *for identify the type of certificate by the federation*
..

    *for identify the type of certificate by the federation*

.. i18n: :section: Type, selection, required
..

:section: Type, selection, required

.. i18n: :site_id: Site, many2one, required
..

:site_id: Site, many2one, required

.. i18n: :sequence_id: Sequence, many2one, required
..

:sequence_id: Sequence, many2one, required

.. i18n:     *for association with a sequence*
..

    *for association with a sequence*

.. i18n: :warranty_product_2: Warranty product for ATA carnet if not own Risk, many2one
..

:warranty_product_2: Warranty product for ATA carnet if not own Risk, many2one

.. i18n: :warranty_product_1: Warranty product for ATA carnet if Own Risk, many2one
..

:warranty_product_1: Warranty product for ATA carnet if Own Risk, many2one

.. i18n: :original_product_id: Reference for Original Copies, many2one, required
..

:original_product_id: Reference for Original Copies, many2one, required

.. i18n:     *for the association with a pricelist*
..

    *for the association with a pricelist*

.. i18n: Object: cci_missions.dossier (cci_missions.dossier)
.. i18n: ###################################################
..

Object: cci_missions.dossier (cci_missions.dossier)
###################################################

.. i18n: :goods: Goods Description, char
..

:goods: Goods Description, char

.. i18n: :embassy_folder_id: Related Embassy Folder, many2one
..

:embassy_folder_id: Related Embassy Folder, many2one

.. i18n: :name: Reference, char, required
..

:name: Reference, char, required

.. i18n: :quantity_original: Quantity of Originals, integer, required
..

:quantity_original: Quantity of Originals, integer, required

.. i18n: :type_id: Dossier Type, many2one, required
..

:type_id: Dossier Type, many2one, required

.. i18n: :sender_name: Sender Name, char
..

:sender_name: Sender Name, char

.. i18n: :invoiced_amount: Total, float
..

:invoiced_amount: Total, float

.. i18n: :sub_total: Sub Total for Extra Products, float, readonly
..

:sub_total: Sub Total for Extra Products, float, readonly

.. i18n: :order_partner_id: Billed Customer, many2one, required
..

:order_partner_id: Billed Customer, many2one, required

.. i18n: :to_bill: To Be Billed, boolean
..

:to_bill: To Be Billed, boolean

.. i18n: :state: State, selection
..

:state: State, selection

.. i18n: :product_ids: Products, one2many
..

:product_ids: Products, one2many

.. i18n: :destination_id: Destination Country, many2one
..

:destination_id: Destination Country, many2one

.. i18n: :invoice_id: Invoice, many2one
..

:invoice_id: Invoice, many2one

.. i18n: :date: Creation Date, date, required
..

:date: Creation Date, date, required

.. i18n: :quantity_copies: Number of Copies, integer
..

:quantity_copies: Number of Copies, integer

.. i18n: :text_on_invoice: Text to Display on the Invoice, text
..

:text_on_invoice: Text to Display on the Invoice, text

.. i18n: :id: ID, integer, readonly
..

:id: ID, integer, readonly

.. i18n: :asker_name: Asker Name, char
..

:asker_name: Asker Name, char

.. i18n: :goods_value: Value of the Sold Goods, float
..

:goods_value: Value of the Sold Goods, float

.. i18n: Object: cci_missions.custom_code (cci_missions.custom_code)
.. i18n: ###########################################################
..

Object: cci_missions.custom_code (cci_missions.custom_code)
###########################################################

.. i18n: :meaning: Meaning, text, required
..

:meaning: Meaning, text, required

.. i18n: :official: Official Code, boolean
..

:official: Official Code, boolean

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: Object: cci_missions.certificate (cci_missions.certificate)
.. i18n: ###########################################################
..

Object: cci_missions.certificate (cci_missions.certificate)
###########################################################

.. i18n: :embassy_folder_id: Related Embassy Folder, many2one
..

:embassy_folder_id: Related Embassy Folder, many2one

.. i18n: :legalization_ids: Related Legalizations, one2many
..

:legalization_ids: Related Legalizations, one2many

.. i18n: :type_id: Dossier Type, many2one, required
..

:type_id: Dossier Type, many2one, required

.. i18n: :sender_name: Sender Name, char
..

:sender_name: Sender Name, char

.. i18n: :invoiced_amount: Total, float
..

:invoiced_amount: Total, float

.. i18n: :asker_name: Asker Name, char
..

:asker_name: Asker Name, char

.. i18n: :sub_total: Sub Total for Extra Products, float, readonly
..

:sub_total: Sub Total for Extra Products, float, readonly

.. i18n: :asker_zip_id: Asker Zip Code, many2one
..

:asker_zip_id: Asker Zip Code, many2one

.. i18n: :asker_address: Asker Address, char
..

:asker_address: Asker Address, char

.. i18n: :origin_ids: Origin Countries, many2many
..

:origin_ids: Origin Countries, many2many

.. i18n: :destination_id: Destination Country, many2one
..

:destination_id: Destination Country, many2one

.. i18n: :date: Creation Date, date, required
..

:date: Creation Date, date, required

.. i18n: :total: Total, float, readonly
..

:total: Total, float, readonly

.. i18n: :text_on_invoice: Text to Display on the Invoice, text
..

:text_on_invoice: Text to Display on the Invoice, text

.. i18n: :id: ID, integer, readonly
..

:id: ID, integer, readonly

.. i18n: :special_reason: For special cases, selection
..

:special_reason: For special cases, selection

.. i18n: :goods: Goods Description, char
..

:goods: Goods Description, char

.. i18n: :name: Reference, char, required
..

:name: Reference, char, required

.. i18n: :quantity_original: Quantity of Originals, integer, required
..

:quantity_original: Quantity of Originals, integer, required

.. i18n: :invoice_id: Invoice, many2one
..

:invoice_id: Invoice, many2one

.. i18n: :customs_ids: Custom Codes, many2many
..

:customs_ids: Custom Codes, many2many

.. i18n: :state: State, selection
..

:state: State, selection

.. i18n: :dossier_id: Dossier, many2one
..

:dossier_id: Dossier, many2one

.. i18n: :order_partner_id: Billed Customer, many2one, required
..

:order_partner_id: Billed Customer, many2one, required

.. i18n: :sending_spf: SPF Sending Date, date
..

:sending_spf: SPF Sending Date, date

.. i18n:     *Date of the sending of this record to the external database*
..

    *Date of the sending of this record to the external database*

.. i18n: :quantity_copies: Number of Copies, integer
..

:quantity_copies: Number of Copies, integer

.. i18n: :goods_value: Value of the Sold Goods, float
..

:goods_value: Value of the Sold Goods, float

.. i18n: :to_bill: To Be Billed, boolean
..

:to_bill: To Be Billed, boolean

.. i18n: :product_ids: Products, one2many
..

:product_ids: Products, one2many

.. i18n: Object: cci_missions.legalization (cci_missions.legalization)
.. i18n: #############################################################
..

Object: cci_missions.legalization (cci_missions.legalization)
#############################################################

.. i18n: :embassy_folder_id: Related Embassy Folder, many2one
..

:embassy_folder_id: Related Embassy Folder, many2one

.. i18n: :type_id: Dossier Type, many2one, required
..

:type_id: Dossier Type, many2one, required

.. i18n: :sender_name: Sender Name, char
..

:sender_name: Sender Name, char

.. i18n: :invoiced_amount: Total, float
..

:invoiced_amount: Total, float

.. i18n: :asker_name: Asker Name, char
..

:asker_name: Asker Name, char

.. i18n: :sub_total: Sub Total for Extra Products, float, readonly
..

:sub_total: Sub Total for Extra Products, float, readonly

.. i18n: :partner_member_state: Member State of the Partner, selection, readonly
..

:partner_member_state: Member State of the Partner, selection, readonly

.. i18n: :member_price: Apply the Member Price, boolean
..

:member_price: Apply the Member Price, boolean

.. i18n: :destination_id: Destination Country, many2one
..

:destination_id: Destination Country, many2one

.. i18n: :date: Creation Date, date, required
..

:date: Creation Date, date, required

.. i18n: :total: Total, float, readonly
..

:total: Total, float, readonly

.. i18n: :text_on_invoice: Text to Display on the Invoice, text
..

:text_on_invoice: Text to Display on the Invoice, text

.. i18n: :id: ID, integer, readonly
..

:id: ID, integer, readonly

.. i18n: :goods: Goods Description, char
..

:goods: Goods Description, char

.. i18n: :name: Reference, char, required
..

:name: Reference, char, required

.. i18n: :quantity_original: Quantity of Originals, integer, required
..

:quantity_original: Quantity of Originals, integer, required

.. i18n: :invoice_id: Invoice, many2one
..

:invoice_id: Invoice, many2one

.. i18n: :state: State, selection
..

:state: State, selection

.. i18n: :dossier_id: Dossier, many2one
..

:dossier_id: Dossier, many2one

.. i18n: :order_partner_id: Billed Customer, many2one, required
..

:order_partner_id: Billed Customer, many2one, required

.. i18n: :certificate_id: Related Certificate, many2one
..

:certificate_id: Related Certificate, many2one

.. i18n: :quantity_copies: Number of Copies, integer
..

:quantity_copies: Number of Copies, integer

.. i18n: :goods_value: Value of the Sold Goods, float
..

:goods_value: Value of the Sold Goods, float

.. i18n: :to_bill: To Be Billed, boolean
..

:to_bill: To Be Billed, boolean

.. i18n: :product_ids: Products, one2many
..

:product_ids: Products, one2many

.. i18n: Object: cci_missions.courier_log (cci_missions.courier_log)
.. i18n: ###########################################################
..

Object: cci_missions.courier_log (cci_missions.courier_log)
###########################################################

.. i18n: :documents_certificate: List of Certificates, text
..

:documents_certificate: List of Certificates, text

.. i18n: :embassy_folder_id: Related Embassy Folder, many2one, required
..

:embassy_folder_id: Related Embassy Folder, many2one, required

.. i18n: :qtty_to_print: Number of Sheets, integer
..

:qtty_to_print: Number of Sheets, integer

.. i18n: :copy_cba: Photocopy Before CBA, boolean
..

:copy_cba: Photocopy Before CBA, boolean

.. i18n: :cba: CBA, boolean
..

:cba: CBA, boolean

.. i18n: :message: Message to the Courier, text
..

:message: Message to the Courier, text

.. i18n: :address_street: Street, char
..

:address_street: Street, char

.. i18n: :documents: Number of Documents to Legalize, integer
..

:documents: Number of Documents to Legalize, integer

.. i18n: :address_name_1: Company Name, char
..

:address_name_1: Company Name, char

.. i18n: :address_name_2: Contact Name, char
..

:address_name_2: Contact Name, char

.. i18n: :consulate_name: Consulate Name, char
..

:consulate_name: Consulate Name, char

.. i18n: :documents_invoice: List of Invoices, text
..

:documents_invoice: List of Invoices, text

.. i18n: :partner_address_id: Courier, many2one
..

:partner_address_id: Courier, many2one

.. i18n: :copy_ministry: Photocopy Before Ministry, boolean
..

:copy_ministry: Photocopy Before Ministry, boolean

.. i18n: :others: Others, char
..

:others: Others, char

.. i18n: :translation: Translation, boolean
..

:translation: Translation, boolean

.. i18n: :address_city: City, char
..

:address_city: City, char

.. i18n: :ministry: Ministry, boolean
..

:ministry: Ministry, boolean

.. i18n: :return_address: Address of Return, selection, required
..

:return_address: Address of Return, selection, required

.. i18n: :embassy_name: Embassy Name, char
..

:embassy_name: Embassy Name, char

.. i18n: :documents_others: Others, text
..

:documents_others: Others, text

.. i18n: :copy_embassy_consulate: Photocopy Before Embassy or Consulate, boolean
..

:copy_embassy_consulate: Photocopy Before Embassy or Consulate, boolean

.. i18n: Object: cci_missions.ata_usage (cci_missions.ata_usage)
.. i18n: #######################################################
..

Object: cci_missions.ata_usage (cci_missions.ata_usage)
#######################################################

.. i18n: :name: Usage, char, required
..

:name: Usage, char, required

.. i18n: Object: cci_missions.ata_carnet (cci_missions.ata_carnet)
.. i18n: #########################################################
..

Object: cci_missions.ata_carnet (cci_missions.ata_carnet)
#########################################################

.. i18n: :warranty: Warranty, float, readonly
..

:warranty: Warranty, float, readonly

.. i18n: :area_id: Area, many2one, required
..

:area_id: Area, many2one, required

.. i18n: :type_id: Related Type of Carnet, many2one, required
..

:type_id: Related Type of Carnet, many2one, required

.. i18n: :member_price: Apply the Member Price, boolean
..

:member_price: Apply the Member Price, boolean

.. i18n: :partner_member_state: Member State of the Partner, selection, readonly
..

:partner_member_state: Member State of the Partner, selection, readonly

.. i18n: :creation_date: Emission Date, date, required
..

:creation_date: Emission Date, date, required

.. i18n: :ok_state_date: Date of Closure, date
..

:ok_state_date: Date of Closure, date

.. i18n: :partner_id: Partner, many2one, required
..

:partner_id: Partner, many2one, required

.. i18n: :id: ID, integer, readonly
..

:id: ID, integer, readonly

.. i18n: :usage_id: Usage, many2one, required
..

:usage_id: Usage, many2one, required

.. i18n: :federation_sending_date: Date of Sending to the Federation, date, readonly
..

:federation_sending_date: Date of Sending to the Federation, date, readonly

.. i18n: :representer_name: Representer Name, char
..

:representer_name: Representer Name, char

.. i18n: :representer_city: Representer City, char
..

:representer_city: Representer City, char

.. i18n: :warranty_product_id: Related Warranty Product, many2one, required
..

:warranty_product_id: Related Warranty Product, many2one, required

.. i18n: :initial_pages: Initial Number of Pages, integer, required
..

:initial_pages: Initial Number of Pages, integer, required

.. i18n: :state: State, selection, required, readonly
..

:state: State, selection, required, readonly

.. i18n: :representer_address: Representer Address, char
..

:representer_address: Representer Address, char

.. i18n: :insurer_agreement: Insurer Agreement, char
..

:insurer_agreement: Insurer Agreement, char

.. i18n: :double_signature: Double Signature, boolean
..

:double_signature: Double Signature, boolean

.. i18n: :additional_pages: Additional Number of Pages, integer
..

:additional_pages: Additional Number of Pages, integer

.. i18n: :goods_value: Goods Value, float, required
..

:goods_value: Goods Value, float, required

.. i18n: :holder_name: Holder Name, char
..

:holder_name: Holder Name, char

.. i18n: :sub_total: Subtotal of Extra Products, float, readonly
..

:sub_total: Subtotal of Extra Products, float, readonly

.. i18n: :validity_date: Validity Date, date, required
..

:validity_date: Validity Date, date, required

.. i18n: :holder_city: Holder City, char
..

:holder_city: Holder City, char

.. i18n: :product_ids: Products, one2many
..

:product_ids: Products, one2many

.. i18n: :holder_address: Holder Address, char
..

:holder_address: Holder Address, char

.. i18n: :letter_ids: Letters, one2many
..

:letter_ids: Letters, one2many

.. i18n: :goods: Goods, char
..

:goods: Goods, char

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :invoice_id: Invoice, many2one
..

:invoice_id: Invoice, many2one

.. i18n: :partner_insurer_id: Insurer ID of the Partner, float, readonly
..

:partner_insurer_id: Insurer ID of the Partner, float, readonly

.. i18n: :return_date: Date of Return, date
..

:return_date: Date of Return, date

.. i18n: :own_risk: Own Risks, boolean
..

:own_risk: Own Risks, boolean

.. i18n: Object: cci_missions.letters_log (cci_missions.letters_log)
.. i18n: ###########################################################
..

Object: cci_missions.letters_log (cci_missions.letters_log)
###########################################################

.. i18n: :date: Date of Sending, date, required
..

:date: Date of Sending, date, required

.. i18n: :letter_type: Type of Letter, selection, required
..

:letter_type: Type of Letter, selection, required

.. i18n: :ata_carnet_id: Related ATA Carnet, many2one, required
..

:ata_carnet_id: Related ATA Carnet, many2one, required

.. i18n: Object: Product Lines (product.lines)
.. i18n: #####################################
..

Object: Product Lines (product.lines)
#####################################

.. i18n: :uos_id: Unit, many2one
..

:uos_id: Unit, many2one

.. i18n: :name: Description, char, required
..

:name: Description, char, required

.. i18n: :product_line_id: Product Ref, many2one
..

:product_line_id: Product Ref, many2one

.. i18n: :price_unit: Unit Price, float, required
..

:price_unit: Unit Price, float, required

.. i18n: :price_subtotal: Subtotal, float, readonly
..

:price_subtotal: Subtotal, float, readonly

.. i18n: :dossier_product_line_id: Product Ref, many2one
..

:dossier_product_line_id: Product Ref, many2one

.. i18n: :quantity: Quantity, float, required
..

:quantity: Quantity, float, required

.. i18n: :product_id: Product, many2one, required
..

:product_id: Product, many2one, required

.. i18n: :account_id: Account, many2one, required
..

:account_id: Account, many2one, required
