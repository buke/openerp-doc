
.. i18n: .. module:: stock_rma
.. i18n:     :synopsis: stock rma 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: stock_rma
    :synopsis: stock rma 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/stock_rma"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/stock_rma"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: stock rma (*stock_rma*)
.. i18n: =======================
.. i18n: :Module: stock_rma
.. i18n: :Name: stock rma
.. i18n: :Version: 5.0.0.1
.. i18n: :Author: Akretion.com
.. i18n: :Directory: stock_rma
.. i18n: :Web: http://www.akretion.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Return Material Authorization
..

::

  Return Material Authorization

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n: (No download links available)
..

(No download links available)

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`stock`
.. i18n:  * :mod:`crm`
.. i18n:  * :mod:`crm_configuration`
.. i18n:  * :mod:`sale`
..

 * :mod:`stock`
 * :mod:`crm`
 * :mod:`crm_configuration`
 * :mod:`sale`

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

.. i18n:  * CRM & SRM/RMA
.. i18n:  * CRM & SRM/RMA/All RMA
.. i18n:  * CRM & SRM/RMA/New RMA
..

 * CRM & SRM/RMA
 * CRM & SRM/RMA/All RMA
 * CRM & SRM/RMA/New RMA

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * crm.rma.form.rma (form)
.. i18n:  * crm.rma.tree.rma (tree)
.. i18n:  * stock.picking.rma.form (form)
..

 * crm.rma.form.rma (form)
 * crm.rma.tree.rma (tree)
 * stock.picking.rma.form (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: crm.rma (crm.rma)
.. i18n: #########################
..

Object: crm.rma (crm.rma)
#########################

.. i18n: :date_closed: Closed, datetime, readonly
..

:date_closed: Closed, datetime, readonly

.. i18n: :history_line: Communication, one2many, readonly
..

:history_line: Communication, one2many, readonly

.. i18n: :create_date: Created, datetime, readonly
..

:create_date: Created, datetime, readonly

.. i18n: :outgoing_picking_id: Outgoing Picking, many2one
..

:outgoing_picking_id: Outgoing Picking, many2one

.. i18n: :probability: Probability (%), float
..

:probability: Probability (%), float

.. i18n: :canal_id: Channel, many2one
..

:canal_id: Channel, many2one

.. i18n: :partner_address_id: Partner Contact, many2one
..

:partner_address_id: Partner Contact, many2one

.. i18n: :som: State of Mind, many2one
..

:som: State of Mind, many2one

.. i18n: :date: Date, datetime
..

:date: Date, datetime

.. i18n: :warning: Warning, char, readonly
..

:warning: Warning, char, readonly

.. i18n: :category2_id: Category Name, many2one
..

:category2_id: Category Name, many2one

.. i18n: :duration: Duration, float
..

:duration: Duration, float

.. i18n: :out_supplier_picking_id: Return From Supplier Picking, many2one
..

:out_supplier_picking_id: Return From Supplier Picking, many2one

.. i18n: :planned_revenue: Planned Revenue, float
..

:planned_revenue: Planned Revenue, float

.. i18n: :id: ID, integer, readonly
..

:id: ID, integer, readonly

.. i18n: :date_action_next: Next Action, datetime, readonly
..

:date_action_next: Next Action, datetime, readonly

.. i18n: :note: Note, text
..

:note: Note, text

.. i18n: :user_id: Responsible, many2one
..

:user_id: Responsible, many2one

.. i18n: :partner_name: Employee Name, char
..

:partner_name: Employee Name, char

.. i18n: :partner_id: Partner, many2one
..

:partner_id: Partner, many2one

.. i18n: :priority: Priority, selection
..

:priority: Priority, selection

.. i18n: :state: Status, selection, readonly
..

:state: Status, selection, readonly

.. i18n: :case_id: Related Case, many2one
..

:case_id: Related Case, many2one

.. i18n: :rma_ref: Incident Ref, char, required
..

:rma_ref: Incident Ref, char, required

.. i18n: :in_supplier_picking_id: Return To Supplier Picking, many2one
..

:in_supplier_picking_id: Return To Supplier Picking, many2one

.. i18n: :new_invoice_id: Invoice, many2one
..

:new_invoice_id: Invoice, many2one

.. i18n: :email_cc: Watchers Emails, char
..

:email_cc: Watchers Emails, char

.. i18n: :incoming_picking_id: Incoming Picking, many2one
..

:incoming_picking_id: Incoming Picking, many2one

.. i18n: :ref: Reference, reference
..

:ref: Reference, reference

.. i18n: :log_ids: Logs History, one2many, readonly
..

:log_ids: Logs History, one2many, readonly

.. i18n: :description: Your action, text
..

:description: Your action, text

.. i18n: :date_action_last: Last Action, datetime, readonly
..

:date_action_last: Last Action, datetime, readonly

.. i18n: :planned_cost: Planned Costs, float
..

:planned_cost: Planned Costs, float

.. i18n: :ref2: Reference 2, reference
..

:ref2: Reference 2, reference

.. i18n: :section_id: Section, many2one, required
..

:section_id: Section, many2one, required

.. i18n: :prodlot_id: Serial / Lot Number, many2one
..

:prodlot_id: Serial / Lot Number, many2one

.. i18n: :partner_name2: Employee Email, char
..

:partner_name2: Employee Email, char

.. i18n: :partner_mobile: Mobile, char
..

:partner_mobile: Mobile, char

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :categ_id: Category, many2one
..

:categ_id: Category, many2one

.. i18n: :product_id: Product, many2one
..

:product_id: Product, many2one

.. i18n: :invoice_id: Invoice, many2one
..

:invoice_id: Invoice, many2one

.. i18n: :stage_id: Stage, many2one
..

:stage_id: Stage, many2one

.. i18n: :related_incoming_picking_state: Related Picking State, char, readonly
..

:related_incoming_picking_state: Related Picking State, char, readonly

.. i18n: :name: Description, char, required
..

:name: Description, char, required

.. i18n: :date_deadline: Deadline, datetime
..

:date_deadline: Deadline, datetime

.. i18n: :email_last: Latest E-Mail, text, readonly
..

:email_last: Latest E-Mail, text, readonly

.. i18n: :related_outgoing_picking_state: Related Picking State, char, readonly
..

:related_outgoing_picking_state: Related Picking State, char, readonly

.. i18n: :partner_phone: Phone, char
..

:partner_phone: Phone, char

.. i18n: :extra_note: Note, text
..

:extra_note: Note, text

.. i18n: :guarantee_limit: Warranty limit, date, readonly
..

:guarantee_limit: Warranty limit, date, readonly

.. i18n:     *The warranty limit is computed as: invoice date + warranty defined on selected product.*
..

    *The warranty limit is computed as: invoice date + warranty defined on selected product.*

.. i18n: :email_from: Partner Email, char
..

:email_from: Partner Email, char

.. i18n: :crm_id: CRM case, many2one, required
..

:crm_id: CRM case, many2one, required
