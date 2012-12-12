
.. module:: stock_rma
    :synopsis: stock rma 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/stock_rma"></div>
    <script src="http://js-kit.com/ratings.js"></script>

stock rma (*stock_rma*)
=======================
:Module: stock_rma
:Name: stock rma
:Version: 5.0.0.1
:Author: Akretion.com
:Directory: stock_rma
:Web: http://www.akretion.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Return Material Authorization

Download links
--------------

You can download this module as a zip file in the following version:

(No download links available)


Dependencies
------------

 * :mod:`stock`
 * :mod:`crm`
 * :mod:`crm_configuration`
 * :mod:`sale`

Reports
-------

None


Menus
-------

 * CRM & SRM/RMA
 * CRM & SRM/RMA/All RMA
 * CRM & SRM/RMA/New RMA

Views
-----

 * crm.rma.form.rma (form)
 * crm.rma.tree.rma (tree)
 * stock.picking.rma.form (form)


Objects
-------

Object: crm.rma (crm.rma)
#########################



:date_closed: Closed, datetime, readonly





:history_line: Communication, one2many, readonly





:create_date: Created, datetime, readonly





:outgoing_picking_id: Outgoing Picking, many2one





:probability: Probability (%), float





:canal_id: Channel, many2one





:partner_address_id: Partner Contact, many2one





:som: State of Mind, many2one





:date: Date, datetime





:warning: Warning, char, readonly





:category2_id: Category Name, many2one





:duration: Duration, float





:out_supplier_picking_id: Return From Supplier Picking, many2one





:planned_revenue: Planned Revenue, float





:id: ID, integer, readonly





:date_action_next: Next Action, datetime, readonly





:note: Note, text





:user_id: Responsible, many2one





:partner_name: Employee Name, char





:partner_id: Partner, many2one





:priority: Priority, selection





:state: Status, selection, readonly





:case_id: Related Case, many2one





:rma_ref: Incident Ref, char, required





:in_supplier_picking_id: Return To Supplier Picking, many2one





:new_invoice_id: Invoice, many2one





:email_cc: Watchers Emails, char





:incoming_picking_id: Incoming Picking, many2one





:ref: Reference, reference





:log_ids: Logs History, one2many, readonly





:description: Your action, text





:date_action_last: Last Action, datetime, readonly





:planned_cost: Planned Costs, float





:ref2: Reference 2, reference





:section_id: Section, many2one, required





:prodlot_id: Serial / Lot Number, many2one





:partner_name2: Employee Email, char





:partner_mobile: Mobile, char





:active: Active, boolean





:categ_id: Category, many2one





:product_id: Product, many2one





:invoice_id: Invoice, many2one





:stage_id: Stage, many2one





:related_incoming_picking_state: Related Picking State, char, readonly





:name: Description, char, required





:date_deadline: Deadline, datetime





:email_last: Latest E-Mail, text, readonly





:related_outgoing_picking_state: Related Picking State, char, readonly





:partner_phone: Phone, char





:extra_note: Note, text





:guarantee_limit: Warranty limit, date, readonly

    *The warranty limit is computed as: invoice date + warranty defined on selected product.*



:email_from: Partner Email, char





:crm_id: CRM case, many2one, required


