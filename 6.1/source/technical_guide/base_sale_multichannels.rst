
.. module:: base_sale_multichannels
    :synopsis: Base Sale MultiChannels 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/base_sale_multichannels"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Base Sale MultiChannels (*base_sale_multichannels*)
===================================================
:Module: base_sale_multichannels
:Name: Base Sale MultiChannels
:Version: 5.0.1.0
:Author: Raphaël Valyi (Akretion.com), Sharoon Thomas (Openlabs.co.in)
:Directory: base_sale_multichannels
:Web: http://www.akretion.com
:Official module: no
:Quality certified: no

Description
-----------

::

  This module provide an abstract common minimal base to multi-channels sales.
  Say you want to expose your product catalog to
  * several instances of flashy-sluggish Magento web sites
  * a cutting edge Spree web shop
  * a Neteven online Marketplace
  * EBay
  * Amazon
  * Google Base
  * an external Point Of Sale system
  * ...
  Then this module allows you to:
  * use several external references ids on every OpenERP object matching those all those external referentials
  * per referential instance, use several sale sub platform entities (ex: several Magento websites per instance)
  * per sub platform, use several shops (ex: several Magento web shops per website)
  
  For each sale shop (matching OpenERP sale.shop object), this module abstract the interfaces to:
  * export the catalog, shop warehouse stock level wise, shop pricelist wise
  * import the catalog
  * import orders
  * export orders/picking status

Download links
--------------

You can download this module as a zip file in the following version:

(No download links available)


Dependencies
------------

 * :mod:`sale`
 * :mod:`base_external_referentials`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT base_sale_multichannels_view_shop_form (form)
 * \* INHERIT simple_pos_view_account_journal_form (form)


Objects
-------

Object: External Referential Shop Group (external.shop.group)
#############################################################



:shop_ids: Sale Shops, one2many





:referential_id: Referential, many2one





:name: Name, char, required


