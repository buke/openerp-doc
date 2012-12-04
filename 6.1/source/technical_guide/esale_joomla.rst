
.. module:: esale_joomla
    :synopsis: eSale Interface - Joomla 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/esale_joomla"></div>
    <script src="http://js-kit.com/ratings.js"></script>

eSale Interface - Joomla (*esale_joomla*)
=========================================
:Module: esale_joomla
:Name: eSale Interface - Joomla
:Version: 5.0.1.0
:Author: Tiny
:Directory: esale_joomla
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Joomla (Virtuemart) eCommerce interface synchronisation.
  Users can order on the website, orders are automatically imported into OpenERP.
  
  You can export products, product categories, account taxes, stock level and create links between
  categories of products, taxes and languages.
  
  If your product has an image attached, it sends the image to the Joomla website.

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/esale_joomla.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/esale_joomla.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/esale_joomla.zip>`_


Dependencies
------------

 * :mod:`product`
 * :mod:`stock`
 * :mod:`sale`
 * :mod:`account`
 * :mod:`account_tax_include`

Reports
-------

None


Menus
-------

 * Sales Management/eSale
 * Sales Management/eSale/Definition
 * Sales Management/eSale/Definition/Web Shop
 * Sales Management/eSale/Definition/Web Product
 * Sales Management/eSale/eSale Orders
 * Sales Management/eSale/eSale Orders/Draft eSale Orders
 * Sales Management/eSale/Synchronisation
 * Sales Management/eSale/Synchronisation/Website Export log
 * Sales Management/eSale/Synchronisation/Export Product Categories
 * Sales Management/eSale/Synchronisation/Export Tax
 * Sales Management/eSale/Synchronisation/Export Products
 * Sales Management/eSale/Synchronisation/Export Inventory Level
 * Sales Management/eSale/Synchronisation/Import eSales Orders

Views
-----

 * \* INHERIT product.normal.form (form)
 * esale_joomla.web.form (form)
 * esale_joomla.product.form (form)
 * esale_joomla.product.tree (tree)
 * esale_joomla.order.tree (tree)
 * esale_joomla.order.form (form)
 * esale_joomla.order.line.form (form)
 * esale_joomla.order.line.tree (tree)
 * esale_joomla.web.exportlog.form (form)
 * esale_joomla.web.exportlog.tree (tree)


Objects
-------

Object: eCommerce Website (esale_joomla.web)
############################################



:taxes_included_ids: Taxes included, many2many





:name: Name, char, required





:url: URL, char, required





:language_id: Language, many2one





:category_ids: Categories, one2many





:shop_id: Sale Shop, many2one, required





:product_ids: Products, one2many





:active: Active, boolean





:tax_ids: Taxes, one2many




Object: eSale Tax (esale_joomla.tax)
####################################



:web_id: Website, many2one





:name: Tax name, char, required





:esale_joomla_id: eSale id, integer





:tax_id: Tax, many2one




Object: eSale Category (esale_joomla.category)
##############################################



:include_childs: Include Childs, boolean

    *If checked, OpenERP will also export products from categories that are children of this one.*



:category_id: Category, many2one





:web_id: Website, many2one





:name: Name, char, required





:esale_joomla_id: Web ID, integer, required, readonly




Object: eSale Product (esale_joomla.product)
############################################



:esale_joomla_tax_id: eSale tax, many2one





:web_id: Web Ref, many2one





:name: Name, char, required





:esale_joomla_id: eSale product id, integer





:product_id: Product, many2one, required




Object: eSale Language (esale_joomla.lang)
##########################################



:web_id: Website, many2one





:name: Name, char, required





:esale_joomla_id: Web ID, integer, required





:language_id: Language, many2one




Object: eShop Partner (esale_joomla.partner)
############################################



:city: City, char





:address_id: Partner Address, many2one





:name: Name, char, required





:zip: Zip, char





:country: Country, char





:state: State, char





:esale_id: eSale ID, char





:address: Address, char





:email: Mail, char




Object: esale_joomla.order (esale_joomla.order)
###############################################



:web_id: Web Shop, many2one, required





:name: Order Description, char, required





:epartner_shipping_id: Joomla Shipping Address, many2one, required





:order_id: Sale Order, many2one





:partner_id: Contact Address, many2one





:web_ref: Web Ref, integer





:note: Notes, text





:state: Order State, selection





:partner_shipping_id: Shipping Address, many2one





:partner_invoice_id: Invoice Address, many2one





:date_order: Date Ordered, date, required





:epartner_invoice_id: Joomla Invoice Address, many2one, required





:order_lines: Order Lines, one2many




Object: eSale Order line (esale_joomla.order.line)
##################################################



:product_id: Product, many2one





:order_id: eOrder Ref, many2one





:product_uom_id: Unit of Measure, many2one, required





:price_unit: Unit Price, float, required





:product_qty: Quantity, float, required





:name: Order Line, char, required




Object: eSale webshop Synchronisation log (esale_joomla.web.exportlog)
######################################################################



:log_date: Log date, datetime, required





:user_id: Exported By, many2one, required





:web_id: Web Ref, many2one





:name: Synchronisation Log, char, required





:log_type: Export type, selection, readonly


