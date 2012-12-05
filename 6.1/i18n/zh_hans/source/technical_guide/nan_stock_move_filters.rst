
.. i18n: .. module:: nan_stock_move_filters
.. i18n:     :synopsis: Stock Move Filters 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: nan_stock_move_filters
    :synopsis: Stock Move Filters 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/nan_stock_move_filters"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/nan_stock_move_filters"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Stock Move Filters (*nan_stock_move_filters*)
.. i18n: =============================================
.. i18n: :Module: nan_stock_move_filters
.. i18n: :Name: Stock Move Filters
.. i18n: :Version: 5.0.0.1
.. i18n: :Author: NaN for Trod y Avia, S.L.
.. i18n: :Directory: nan_stock_move_filters
.. i18n: :Web: http://www.NaN-tic.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

Stock Move Filters (*nan_stock_move_filters*)
=============================================
:Module: nan_stock_move_filters
:Name: Stock Move Filters
:Version: 5.0.0.1
:Author: NaN for Trod y Avia, S.L.
:Directory: nan_stock_move_filters
:Web: http://www.NaN-tic.com
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module adds filters to stock moves so only available locations, products and lots are shown in searches, easing the selection of the appropriate ones to the user.
.. i18n:   	
.. i18n:   This module provides a useful infrastructure for specific filters to be implemented in new modules.
..

::

  This module adds filters to stock moves so only available locations, products and lots are shown in searches, easing the selection of the appropriate ones to the user.
  	
  This module provides a useful infrastructure for specific filters to be implemented in new modules.

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
..

 * :mod:`stock`

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

.. i18n:  * \* INHERIT stock.move.form.location_id (form)
.. i18n:  * \* INHERIT stock.move.form.location_dest_id (form)
.. i18n:  * \* INHERIT stock.move.form.product_id (form)
.. i18n:  * \* INHERIT stock.picking.form.location_id (form)
.. i18n:  * \* INHERIT stock.picking.form.location_dest_id (form)
.. i18n:  * \* INHERIT stock.picking.in.form.location_id (form)
.. i18n:  * \* INHERIT stock.picking.in.form.location_dest_id (form)
.. i18n:  * \* INHERIT stock.picking.out.form.location_id (form)
.. i18n:  * \* INHERIT stock.picking.out.form.location_dest_id (form)
.. i18n:  * \* INHERIT stock.picking.delivery.form.location_id (form)
.. i18n:  * \* INHERIT stock.picking.delivery.form.location_dest_id (form)
..

 * \* INHERIT stock.move.form.location_id (form)
 * \* INHERIT stock.move.form.location_dest_id (form)
 * \* INHERIT stock.move.form.product_id (form)
 * \* INHERIT stock.picking.form.location_id (form)
 * \* INHERIT stock.picking.form.location_dest_id (form)
 * \* INHERIT stock.picking.in.form.location_id (form)
 * \* INHERIT stock.picking.in.form.location_dest_id (form)
 * \* INHERIT stock.picking.out.form.location_id (form)
 * \* INHERIT stock.picking.out.form.location_dest_id (form)
 * \* INHERIT stock.picking.delivery.form.location_id (form)
 * \* INHERIT stock.picking.delivery.form.location_dest_id (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: None
..

None
