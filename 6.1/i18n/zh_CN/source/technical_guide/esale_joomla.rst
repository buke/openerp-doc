
.. i18n: .. module:: esale_joomla
.. i18n:     :synopsis: eSale Interface - Joomla 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: esale_joomla
    :synopsis: eSale Interface - Joomla 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/esale_joomla"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/esale_joomla"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: eSale Interface - Joomla (*esale_joomla*)
.. i18n: =========================================
.. i18n: :Module: esale_joomla
.. i18n: :Name: eSale Interface - Joomla
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: esale_joomla
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Joomla (Virtuemart) eCommerce interface synchronisation.
.. i18n:   Users can order on the website, orders are automatically imported into OpenERP.
.. i18n:   
.. i18n:   You can export products, product categories, account taxes, stock level and create links between
.. i18n:   categories of products, taxes and languages.
.. i18n:   
.. i18n:   If your product has an image attached, it sends the image to the Joomla website.
..

::

  Joomla (Virtuemart) eCommerce interface synchronisation.
  Users can order on the website, orders are automatically imported into OpenERP.
  
  You can export products, product categories, account taxes, stock level and create links between
  categories of products, taxes and languages.
  
  If your product has an image attached, it sends the image to the Joomla website.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/esale_joomla.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/esale_joomla.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/esale_joomla.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/esale_joomla.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/esale_joomla.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/esale_joomla.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`product`
.. i18n:  * :mod:`stock`
.. i18n:  * :mod:`sale`
.. i18n:  * :mod:`account`
.. i18n:  * :mod:`account_tax_include`
..

 * :mod:`product`
 * :mod:`stock`
 * :mod:`sale`
 * :mod:`account`
 * :mod:`account_tax_include`

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

.. i18n:  * Sales Management/eSale
.. i18n:  * Sales Management/eSale/Definition
.. i18n:  * Sales Management/eSale/Definition/Web Shop
.. i18n:  * Sales Management/eSale/Definition/Web Product
.. i18n:  * Sales Management/eSale/eSale Orders
.. i18n:  * Sales Management/eSale/eSale Orders/Draft eSale Orders
.. i18n:  * Sales Management/eSale/Synchronisation
.. i18n:  * Sales Management/eSale/Synchronisation/Website Export log
.. i18n:  * Sales Management/eSale/Synchronisation/Export Product Categories
.. i18n:  * Sales Management/eSale/Synchronisation/Export Tax
.. i18n:  * Sales Management/eSale/Synchronisation/Export Products
.. i18n:  * Sales Management/eSale/Synchronisation/Export Inventory Level
.. i18n:  * Sales Management/eSale/Synchronisation/Import eSales Orders
..

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

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT product.normal.form (form)
.. i18n:  * esale_joomla.web.form (form)
.. i18n:  * esale_joomla.product.form (form)
.. i18n:  * esale_joomla.product.tree (tree)
.. i18n:  * esale_joomla.order.tree (tree)
.. i18n:  * esale_joomla.order.form (form)
.. i18n:  * esale_joomla.order.line.form (form)
.. i18n:  * esale_joomla.order.line.tree (tree)
.. i18n:  * esale_joomla.web.exportlog.form (form)
.. i18n:  * esale_joomla.web.exportlog.tree (tree)
..

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

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: eCommerce Website (esale_joomla.web)
.. i18n: ############################################
..

Object: eCommerce Website (esale_joomla.web)
############################################

.. i18n: :taxes_included_ids: Taxes included, many2many
..

:taxes_included_ids: Taxes included, many2many

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :url: URL, char, required
..

:url: URL, char, required

.. i18n: :language_id: Language, many2one
..

:language_id: Language, many2one

.. i18n: :category_ids: Categories, one2many
..

:category_ids: Categories, one2many

.. i18n: :shop_id: Sale Shop, many2one, required
..

:shop_id: Sale Shop, many2one, required

.. i18n: :product_ids: Products, one2many
..

:product_ids: Products, one2many

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :tax_ids: Taxes, one2many
..

:tax_ids: Taxes, one2many

.. i18n: Object: eSale Tax (esale_joomla.tax)
.. i18n: ####################################
..

Object: eSale Tax (esale_joomla.tax)
####################################

.. i18n: :web_id: Website, many2one
..

:web_id: Website, many2one

.. i18n: :name: Tax name, char, required
..

:name: Tax name, char, required

.. i18n: :esale_joomla_id: eSale id, integer
..

:esale_joomla_id: eSale id, integer

.. i18n: :tax_id: Tax, many2one
..

:tax_id: Tax, many2one

.. i18n: Object: eSale Category (esale_joomla.category)
.. i18n: ##############################################
..

Object: eSale Category (esale_joomla.category)
##############################################

.. i18n: :include_childs: Include Childs, boolean
..

:include_childs: Include Childs, boolean

.. i18n:     *If checked, OpenERP will also export products from categories that are children of this one.*
..

    *If checked, OpenERP will also export products from categories that are children of this one.*

.. i18n: :category_id: Category, many2one
..

:category_id: Category, many2one

.. i18n: :web_id: Website, many2one
..

:web_id: Website, many2one

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :esale_joomla_id: Web ID, integer, required, readonly
..

:esale_joomla_id: Web ID, integer, required, readonly

.. i18n: Object: eSale Product (esale_joomla.product)
.. i18n: ############################################
..

Object: eSale Product (esale_joomla.product)
############################################

.. i18n: :esale_joomla_tax_id: eSale tax, many2one
..

:esale_joomla_tax_id: eSale tax, many2one

.. i18n: :web_id: Web Ref, many2one
..

:web_id: Web Ref, many2one

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :esale_joomla_id: eSale product id, integer
..

:esale_joomla_id: eSale product id, integer

.. i18n: :product_id: Product, many2one, required
..

:product_id: Product, many2one, required

.. i18n: Object: eSale Language (esale_joomla.lang)
.. i18n: ##########################################
..

Object: eSale Language (esale_joomla.lang)
##########################################

.. i18n: :web_id: Website, many2one
..

:web_id: Website, many2one

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :esale_joomla_id: Web ID, integer, required
..

:esale_joomla_id: Web ID, integer, required

.. i18n: :language_id: Language, many2one
..

:language_id: Language, many2one

.. i18n: Object: eShop Partner (esale_joomla.partner)
.. i18n: ############################################
..

Object: eShop Partner (esale_joomla.partner)
############################################

.. i18n: :city: City, char
..

:city: City, char

.. i18n: :address_id: Partner Address, many2one
..

:address_id: Partner Address, many2one

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :zip: Zip, char
..

:zip: Zip, char

.. i18n: :country: Country, char
..

:country: Country, char

.. i18n: :state: State, char
..

:state: State, char

.. i18n: :esale_id: eSale ID, char
..

:esale_id: eSale ID, char

.. i18n: :address: Address, char
..

:address: Address, char

.. i18n: :email: Mail, char
..

:email: Mail, char

.. i18n: Object: esale_joomla.order (esale_joomla.order)
.. i18n: ###############################################
..

Object: esale_joomla.order (esale_joomla.order)
###############################################

.. i18n: :web_id: Web Shop, many2one, required
..

:web_id: Web Shop, many2one, required

.. i18n: :name: Order Description, char, required
..

:name: Order Description, char, required

.. i18n: :epartner_shipping_id: Joomla Shipping Address, many2one, required
..

:epartner_shipping_id: Joomla Shipping Address, many2one, required

.. i18n: :order_id: Sale Order, many2one
..

:order_id: Sale Order, many2one

.. i18n: :partner_id: Contact Address, many2one
..

:partner_id: Contact Address, many2one

.. i18n: :web_ref: Web Ref, integer
..

:web_ref: Web Ref, integer

.. i18n: :note: Notes, text
..

:note: Notes, text

.. i18n: :state: Order State, selection
..

:state: Order State, selection

.. i18n: :partner_shipping_id: Shipping Address, many2one
..

:partner_shipping_id: Shipping Address, many2one

.. i18n: :partner_invoice_id: Invoice Address, many2one
..

:partner_invoice_id: Invoice Address, many2one

.. i18n: :date_order: Date Ordered, date, required
..

:date_order: Date Ordered, date, required

.. i18n: :epartner_invoice_id: Joomla Invoice Address, many2one, required
..

:epartner_invoice_id: Joomla Invoice Address, many2one, required

.. i18n: :order_lines: Order Lines, one2many
..

:order_lines: Order Lines, one2many

.. i18n: Object: eSale Order line (esale_joomla.order.line)
.. i18n: ##################################################
..

Object: eSale Order line (esale_joomla.order.line)
##################################################

.. i18n: :product_id: Product, many2one
..

:product_id: Product, many2one

.. i18n: :order_id: eOrder Ref, many2one
..

:order_id: eOrder Ref, many2one

.. i18n: :product_uom_id: Unit of Measure, many2one, required
..

:product_uom_id: Unit of Measure, many2one, required

.. i18n: :price_unit: Unit Price, float, required
..

:price_unit: Unit Price, float, required

.. i18n: :product_qty: Quantity, float, required
..

:product_qty: Quantity, float, required

.. i18n: :name: Order Line, char, required
..

:name: Order Line, char, required

.. i18n: Object: eSale webshop Synchronisation log (esale_joomla.web.exportlog)
.. i18n: ######################################################################
..

Object: eSale webshop Synchronisation log (esale_joomla.web.exportlog)
######################################################################

.. i18n: :log_date: Log date, datetime, required
..

:log_date: Log date, datetime, required

.. i18n: :user_id: Exported By, many2one, required
..

:user_id: Exported By, many2one, required

.. i18n: :web_id: Web Ref, many2one
..

:web_id: Web Ref, many2one

.. i18n: :name: Synchronisation Log, char, required
..

:name: Synchronisation Log, char, required

.. i18n: :log_type: Export type, selection, readonly
..

:log_type: Export type, selection, readonly
