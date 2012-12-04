
.. module:: carrier_picking
    :synopsis: Carrier picking adds carrier contact information 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/carrier_picking"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Carrier picking adds carrier contact information (*carrier_picking*)
====================================================================
:Module: carrier_picking
:Name: Carrier picking adds carrier contact information
:Version: 5.0.0.1
:Author: Zikzakmedia
:Directory: carrier_picking
:Web: www.zikzakmedia.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Carrier picking module:
  
  * Adds contact carrier in picking lists and a field to store additional information (like vehicle's plate) in partner addresses and picking lists

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/carrier_picking.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/carrier_picking.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`stock`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT stock.picking.form.v1 (form)
 * \* INHERIT stock.picking.delivery.form.v1 (form)
 * \* INHERIT stock.picking.in.form.v1 (form)
 * \* INHERIT stock.picking.out.form.v1 (form)
 * \* INHERIT stock.picking.tree.v1 (tree)
 * \* INHERIT stock.picking.delivery.tree.v1 (tree)
 * \* INHERIT stock.picking.in.tree.v1 (tree)
 * \* INHERIT stock.picking.out.tree.v1 (tree)
 * \* INHERIT res.partner.form.v1 (form)
 * \* INHERIT res.partner.address.form.v1 (form)


Objects
-------

None
