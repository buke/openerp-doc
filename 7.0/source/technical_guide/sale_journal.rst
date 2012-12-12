
.. module:: sale_journal
    :synopsis: Managing sales and deliveries by journal (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/sale_journal"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Managing sales and deliveries by journal (*sale_journal*)
=========================================================
:Module: sale_journal
:Name: Managing sales and deliveries by journal
:Version: 5.0.1.0
:Author: Tiny
:Directory: sale_journal
:Web: http://www.openerp.com
:Official module: yes
:Quality certified: yes

Description
-----------

::

  The sale journal modules allows you to categorise your
      sales and deliveries (packing lists) between different journals.
      This module is very helpful for bigger companies that
      works by departments.
  
      You can use journal for different purposes, some examples:
      * isolate sales of different departments
      * journals for deliveries by truck or by UPS
  
      Journals have a responsible and evolves between different status:
      * draft, open, cancel, done.
  
      Batch operations can be processed on the different journals to
      confirm all sales at once, to validate or invoice packing, ...
  
      It also supports batch invoicing methods that can be configured by
      partners and sales orders, examples:
      * daily invoicing,
      * monthly invoicing, ...
  
      Some statistics by journals are provided.

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/sale_journal.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/sale_journal.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/sale_journal.zip>`_


Dependencies
------------

 * :mod:`stock`
 * :mod:`sale`

Reports
-------

None


Menus
-------

 * Sales Management/Configuration/Invoicing Methods
 * Sales Management/Configuration/Sales Journals
 * Sales Management/Sales by Journal
 * Sales Management/Sales by Journal/My Open Journals
 * Sales Management/Sales by Journal/All Open Journals
 * Sales Management/Reporting
 * Sales Management/Reporting/This Month
 * Sales Management/Reporting/This Month/Sales by Journal
 * Sales Management/Reporting/All Months
 * Sales Management/Reporting/All Months/Sales by Journal
 * Stock Management/Configuration/Packing Journals
 * Stock Management/Packing by Journal
 * Stock Management/Packing by Journal/My Open Journals
 * Stock Management/Packing by Journal/All Open Journals
 * Stock Management/Outgoing Products/Packing to Invoice
 * Stock Management/Outgoing Products/Packing to Invoice/Packing by Invoice Method
 * Stock Management/Reporting/Packing Journal
 * Stock Management/Reporting/Packing Journal/This Month
 * Stock Management/Reporting/Packing Journal/This Month/Packing by Invoice Method
 * Stock Management/Reporting/Packing Journal/All Months
 * Stock Management/Reporting/Packing Journal/All Months/Packing by Invoice Method
 * Stock Management/Reporting/Packing Journal/This Month/Packing by Journal
 * Stock Management/Reporting/Packing Journal/All Months/Packing by Journal

Views
-----

 * sale_journal.invoice.type.form (form)
 * sale_journal.invoice.type.tree (tree)
 * sale_journal.sale.journal.form (form)
 * sale_journal.sale.journal.tree (tree)
 * \* INHERIT sale.order.journal.view.form (form)
 * \* INHERIT sale.order.journal.view.tree (tree)
 * \* INHERIT stock.picking.journal.view.form (form)
 * \* INHERIT stock.picking.journal.view.tree (tree)
 * \* INHERIT stock.picking.journal.view.form (form)
 * \* INHERIT stock.picking.journal.view.tree (tree)
 * \* INHERIT stock.picking.journal.view.form (form)
 * \* INHERIT stock.picking.journal.view.tree (tree)
 * \* INHERIT stock.picking.journal.view.form (form)
 * \* INHERIT stock.picking.journal.view.tree (tree)
 * sale_journal.sale.stats.tree (tree)
 * sale_journal.sale.stats.form (form)
 * \* INHERIT res.partner.journal.property.form.inherit (form)
 * sale_journal.picking.journal.form (form)
 * sale_journal.picking.journal.tree (tree)
 * sale_journal.invoice.type.stats.form (form)
 * sale_journal.invoice.type.stats.tree (tree)
 * sale_journal.picking.stats.form (form)
 * sale_journal.picking.stats.tree (tree)


Objects
-------

Object: Invoice Types (sale_journal.invoice.type)
#################################################



:active: Active, boolean





:note: Note, text





:invoicing_method: Invoicing method, selection, required





:name: Invoice Type, char, required




Object: Sale Journal (sale_journal.sale.journal)
################################################



:code: Code, char, required





:user_id: Responsible, many2one, required





:name: Journal, char, required





:note: Note, text





:sale_stats_ids: Sale Stats, one2many, readonly





:state: State, selection, required





:date: Journal date, date, required





:date_created: Creation date, date, required, readonly





:date_validation: Validation date, date, readonly




Object: Packing Journal (sale_journal.picking.journal)
######################################################



:code: Code, char, required





:user_id: Responsible, many2one, required





:name: Journal, char, required





:note: Note, text





:state: Creation date, selection, required





:picking_stats_ids: Journal Stats, one2many, readonly





:date: Journal date, date, required





:date_created: Creation date, date, required, readonly





:date_validation: Validation date, date, readonly




Object: Sales Orders by Journal (sale_journal.sale.stats)
#########################################################



:count: # of Lines, integer, readonly





:price_total: Total Price, float, readonly





:name: Month, date, readonly





:state: Order State, selection, readonly





:journal_id: Journal, many2one, readonly





:price_average: Average Price, float, readonly





:quantity: Quantities, float, readonly




Object: Stats on packing by invoice method (sale_journal.invoice.type.stats)
############################################################################



:count: # of Lines, integer, readonly





:price_total: Total Price, float, readonly





:name: Month, date, readonly





:state: State, selection, readonly





:invoice_state: Invoice state, selection, readonly





:price_average: Average Price, float, readonly





:invoice_type_id: Invoicing method, many2one, readonly





:quantity: Quantities, float, readonly




Object: Packing lists by Journal (sale_journal.picking.stats)
#############################################################



:count: # of Lines, integer, readonly





:price_total: Total Price, float, readonly





:name: Month, date, readonly





:state: State, selection, readonly





:journal_id: Journal, many2one, readonly





:price_average: Average Price, float, readonly





:quantity: Quantities, float, readonly


