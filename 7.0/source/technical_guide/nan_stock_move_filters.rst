
.. module:: nan_stock_move_filters
    :synopsis: Stock Move Filters 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/nan_stock_move_filters"></div>
    <script src="http://js-kit.com/ratings.js"></script>

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

Description
-----------

::

  This module adds filters to stock moves so only available locations, products and lots are shown in searches, easing the selection of the appropriate ones to the user.
  	
  This module provides a useful infrastructure for specific filters to be implemented in new modules.

Download links
--------------

You can download this module as a zip file in the following version:

(No download links available)


Dependencies
------------

 * :mod:`stock`

Reports
-------

None


Menus
-------


None


Views
-----

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


Objects
-------

None
