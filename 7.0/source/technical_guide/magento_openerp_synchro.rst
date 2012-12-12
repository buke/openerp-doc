
.. module:: magento_openerp_synchro
    :synopsis: Magento Synchro Smile 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/magento_openerp_synchro"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Magento Synchro Smile (*magento_openerp_synchro*)
=================================================
:Module: magento_openerp_synchro
:Name: Magento Synchro Smile
:Version: 5.0.0.9.9
:Author: Smile
:Directory: magento_openerp_synchro
:Web: http://code.google.com/p/magento-openerp-smile-synchro/
:Official module: no
:Quality certified: no

Description
-----------

::

  Magento OpenERP Interface - This module allows product catalog 
  and sale orders synchronization between OpenERP and Magento.
  This module is contributed by the Smile French IT company (www.smile.fr)
  and Zikzakmedia (www.zikzakmedia.com)

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/magento_openerp_synchro.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/magento_openerp_synchro.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/magento_openerp_synchro.zip>`_


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

 * Magento
 * Magento/Magento Web
 * Magento/Synchronization
 * Magento/Synchronization/Synchronize products and stocks
 * Magento/Synchronization/Synchronize categories
 * Magento/Synchronization/Import sale orders
 * Magento/Synchronization/Correct sale orders
 * Magento/Synchronization/Update sale orders

Views
-----

 * \* INHERIT product.product.form.magento (form)
 * \* INHERIT product.product.tree.magento (tree)
 * \* INHERIT product.category.form.magento (form)
 * \* INHERIT product.category.tree.magento (tree)
 * \* INHERIT product.pricelist.form.magento (form)
 * \* INHERIT product.pricelist.tree.magento (tree)
 * \* INHERIT sale.order.form.magento (form)
 * \* INHERIT sale.order.tree.magento (tree)
 * \* INHERIT res.partner.form.magento (form)
 * \* INHERIT res.partner.tree.magento (tree)
 * \* INHERIT sale.shop.tree.magento (tree)
 * \* INHERIT sale.shop.form.inherit (form)
 * magento.web.form (form)
 * magento.web.tree (tree)


Objects
-------

Object: Magento Web (magento.web)
#################################



:api_pwd: Magento Api Password, char





:api_user: Magento Api User, char





:auto_update: Auto update products and categories, boolean

    *If auto update is checked, when you create, modify or delete products and categories in OpenERP, they are automatically created, modified or deleted in Magento. Also, if a existing product or category in OpenERP is checked as exportable, it is created in Magento. And when is unchecked as exportable, it is deleted in Magento.*



:magento_url: Magento Url, char

    *URL to Magento shop ending with /*



:magento_flag: Magento web flag, boolean

    *The Magento active web must have this box checked.*



:magento_name: Magento web name, char


