
.. module:: mrp_prodlot_autosplit
    :synopsis: Unique serial number management 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/mrp_prodlot_autosplit"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Unique serial number management (*mrp_prodlot_autosplit*)
=========================================================
:Module: mrp_prodlot_autosplit
:Name: Unique serial number management
:Version: 5.0.0.9.0
:Author: Raphaël Valyi
:Directory: mrp_prodlot_autosplit
:Web: http://www.akretion.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Turns production lot tracking numbers into unique per product instance code (serial number).
      Moreover, it
      1) adds a new checkbox on the product form to enable or disable this behavior (you should also enable in/out tracking)
      2) then forbids to perform a move if a move involves more than one product instance
      3) automagically splits up picking list movements into one movement per product instance
      4) turns incoming pickings into an editable grid where you can directly type the code
      of a new production number/code to create and associate to the move (it also checks it
      doesn't exist yet)
      
      Important Note 1: serial numbers are more easily encode using an editable tree grid, including a special field with new serial to be created.
      However, there is currently a limitation in the OpenObject framework preventing from easily changing non editable trees to editable trees
      by simple extension. Rather than overwriting all views, we prefer give only one example: the active customised view for easy serial encoding
      is available using Stock Management > Incoming Products. Looking at that view definition, the same thing is easily achieved in
      other picking list, like out going products for instance. However it's not "on" by default, you would need to work it out for your case.
      Meanwhile, we hope Tiny add a third "merge_attributes" view extension point to the 3 existing ones: "before", "after" and "replace".
      It would basically simply merge the attributes given (redefined) in the original view XML and let inner content unchanged.
      Blueprint is registered here: https://blueprints.launchpad.net/openobject-server/+spec/merge-attributes-view-extension-point
      
      Important Note 2: this module doesn't split product bill of materials in MRP since they don't use pickings
      A good workaround when generating production orders manually one by one is to define several lines of individual products in nomemclatures
      and produce 1 by 1 (if possible) to make it easier to encode unique prodlot in production orders too.
      We would also like to extend this module to split automatic production orders (from MRP engine) into several individual production orders in order
      to make it easy to encode the serial numbers in the production. Let us know if you would like that simple extension to be made.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/mrp_prodlot_autosplit.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/mrp_prodlot_autosplit.zip>`_


Dependencies
------------

 * :mod:`product`
 * :mod:`stock`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT product.normal.stock.form.unique_production_number.inherit (form)
 * \* INHERIT view.picking.in.form.unique_production_number (form)
 * \* INHERIT view_production_lot_form_unique_production_number (form)


Objects
-------

None
