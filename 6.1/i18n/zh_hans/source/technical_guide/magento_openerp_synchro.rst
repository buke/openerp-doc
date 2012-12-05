
.. i18n: .. module:: magento_openerp_synchro
.. i18n:     :synopsis: Magento Synchro Smile 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: magento_openerp_synchro
    :synopsis: Magento Synchro Smile 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/magento_openerp_synchro"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/magento_openerp_synchro"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Magento Synchro Smile (*magento_openerp_synchro*)
.. i18n: =================================================
.. i18n: :Module: magento_openerp_synchro
.. i18n: :Name: Magento Synchro Smile
.. i18n: :Version: 5.0.0.9.9
.. i18n: :Author: Smile
.. i18n: :Directory: magento_openerp_synchro
.. i18n: :Web: http://code.google.com/p/magento-openerp-smile-synchro/
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Magento OpenERP Interface - This module allows product catalog 
.. i18n:   and sale orders synchronization between OpenERP and Magento.
.. i18n:   This module is contributed by the Smile French IT company (www.smile.fr)
.. i18n:   and Zikzakmedia (www.zikzakmedia.com)
..

::

  Magento OpenERP Interface - This module allows product catalog 
  and sale orders synchronization between OpenERP and Magento.
  This module is contributed by the Smile French IT company (www.smile.fr)
  and Zikzakmedia (www.zikzakmedia.com)

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/magento_openerp_synchro.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/magento_openerp_synchro.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/magento_openerp_synchro.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/magento_openerp_synchro.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/magento_openerp_synchro.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/magento_openerp_synchro.zip>`_

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

.. i18n:  * Magento
.. i18n:  * Magento/Magento Web
.. i18n:  * Magento/Synchronization
.. i18n:  * Magento/Synchronization/Synchronize products and stocks
.. i18n:  * Magento/Synchronization/Synchronize categories
.. i18n:  * Magento/Synchronization/Import sale orders
.. i18n:  * Magento/Synchronization/Correct sale orders
.. i18n:  * Magento/Synchronization/Update sale orders
..

 * Magento
 * Magento/Magento Web
 * Magento/Synchronization
 * Magento/Synchronization/Synchronize products and stocks
 * Magento/Synchronization/Synchronize categories
 * Magento/Synchronization/Import sale orders
 * Magento/Synchronization/Correct sale orders
 * Magento/Synchronization/Update sale orders

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT product.product.form.magento (form)
.. i18n:  * \* INHERIT product.product.tree.magento (tree)
.. i18n:  * \* INHERIT product.category.form.magento (form)
.. i18n:  * \* INHERIT product.category.tree.magento (tree)
.. i18n:  * \* INHERIT product.pricelist.form.magento (form)
.. i18n:  * \* INHERIT product.pricelist.tree.magento (tree)
.. i18n:  * \* INHERIT sale.order.form.magento (form)
.. i18n:  * \* INHERIT sale.order.tree.magento (tree)
.. i18n:  * \* INHERIT res.partner.form.magento (form)
.. i18n:  * \* INHERIT res.partner.tree.magento (tree)
.. i18n:  * \* INHERIT sale.shop.tree.magento (tree)
.. i18n:  * \* INHERIT sale.shop.form.inherit (form)
.. i18n:  * magento.web.form (form)
.. i18n:  * magento.web.tree (tree)
..

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

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Magento Web (magento.web)
.. i18n: #################################
..

Object: Magento Web (magento.web)
#################################

.. i18n: :api_pwd: Magento Api Password, char
..

:api_pwd: Magento Api Password, char

.. i18n: :api_user: Magento Api User, char
..

:api_user: Magento Api User, char

.. i18n: :auto_update: Auto update products and categories, boolean
..

:auto_update: Auto update products and categories, boolean

.. i18n:     *If auto update is checked, when you create, modify or delete products and categories in OpenERP, they are automatically created, modified or deleted in Magento. Also, if a existing product or category in OpenERP is checked as exportable, it is created in Magento. And when is unchecked as exportable, it is deleted in Magento.*
..

    *If auto update is checked, when you create, modify or delete products and categories in OpenERP, they are automatically created, modified or deleted in Magento. Also, if a existing product or category in OpenERP is checked as exportable, it is created in Magento. And when is unchecked as exportable, it is deleted in Magento.*

.. i18n: :magento_url: Magento Url, char
..

:magento_url: Magento Url, char

.. i18n:     *URL to Magento shop ending with /*
..

    *URL to Magento shop ending with /*

.. i18n: :magento_flag: Magento web flag, boolean
..

:magento_flag: Magento web flag, boolean

.. i18n:     *The Magento active web must have this box checked.*
..

    *The Magento active web must have this box checked.*

.. i18n: :magento_name: Magento web name, char
..

:magento_name: Magento web name, char
