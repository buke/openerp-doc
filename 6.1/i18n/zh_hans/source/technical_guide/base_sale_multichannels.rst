
.. i18n: .. module:: base_sale_multichannels
.. i18n:     :synopsis: Base Sale MultiChannels 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: base_sale_multichannels
    :synopsis: Base Sale MultiChannels 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/base_sale_multichannels"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/base_sale_multichannels"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Base Sale MultiChannels (*base_sale_multichannels*)
.. i18n: ===================================================
.. i18n: :Module: base_sale_multichannels
.. i18n: :Name: Base Sale MultiChannels
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Raphaël Valyi (Akretion.com), Sharoon Thomas (Openlabs.co.in)
.. i18n: :Directory: base_sale_multichannels
.. i18n: :Web: http://www.akretion.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module provide an abstract common minimal base to multi-channels sales.
.. i18n:   Say you want to expose your product catalog to
.. i18n:   * several instances of flashy-sluggish Magento web sites
.. i18n:   * a cutting edge Spree web shop
.. i18n:   * a Neteven online Marketplace
.. i18n:   * EBay
.. i18n:   * Amazon
.. i18n:   * Google Base
.. i18n:   * an external Point Of Sale system
.. i18n:   * ...
.. i18n:   Then this module allows you to:
.. i18n:   * use several external references ids on every OpenERP object matching those all those external referentials
.. i18n:   * per referential instance, use several sale sub platform entities (ex: several Magento websites per instance)
.. i18n:   * per sub platform, use several shops (ex: several Magento web shops per website)
.. i18n:   
.. i18n:   For each sale shop (matching OpenERP sale.shop object), this module abstract the interfaces to:
.. i18n:   * export the catalog, shop warehouse stock level wise, shop pricelist wise
.. i18n:   * import the catalog
.. i18n:   * import orders
.. i18n:   * export orders/picking status
..

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

.. i18n:  * :mod:`sale`
.. i18n:  * :mod:`base_external_referentials`
..

 * :mod:`sale`
 * :mod:`base_external_referentials`

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

.. i18n: None
..

None

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT base_sale_multichannels_view_shop_form (form)
.. i18n:  * \* INHERIT simple_pos_view_account_journal_form (form)
..

 * \* INHERIT base_sale_multichannels_view_shop_form (form)
 * \* INHERIT simple_pos_view_account_journal_form (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: External Referential Shop Group (external.shop.group)
.. i18n: #############################################################
..

Object: External Referential Shop Group (external.shop.group)
#############################################################

.. i18n: :shop_ids: Sale Shops, one2many
..

:shop_ids: Sale Shops, one2many

.. i18n: :referential_id: Referential, many2one
..

:referential_id: Referential, many2one

.. i18n: :name: Name, char, required
..

:name: Name, char, required
