
.. module:: fashion
    :synopsis: Tiny TERP fashion module 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/fashion"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Tiny TERP fashion module (*fashion*)
====================================
:Module: fashion
:Name: Tiny TERP fashion module
:Version: 5.0.1.0
:Author: Manou
:Directory: fashion
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  Product characteristics

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/fashion.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/fashion.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`product`
 * :mod:`mrp`

Reports
-------

None


Menus
-------

 * Production
 * Production/Definitions
 * Production/Definitions/Characteristics
 * Production/Definitions/Characteristics/Characteristic Groups
 * Production/Definitions/Characteristics/Characteristic

Views
-----

 * mrp.characteristic.group.tree (tree)
 * mrp.characteristic.group.form (form)
 * mrp.characteristic.tree (tree)
 * mrp.characteristic.form (form)
 * \* INHERIT product.variant.form (form)
 * \* INHERIT product.template.product.form (form)
 * \* INHERIT mrp.bom.form (form)
 * mrp.bom.variation.form (form)
 * mrp.bom.variation.tree (tree)


Objects
-------

Object: Characteristic Group (mrp.characteristic.group)
#######################################################



:axis: Preferred axis for layout, selection





:description: Description, text





:name: Characteristic Group, char, required




Object: Characteristic (mrp.characteristic)
###########################################



:group_id: Characteristic Group, many2one, required





:name: Characteristic, char, required





:magnitude: Magnitude, float





:description: Description, text




Object: BOM characteristic variation (mrp.bom.variation)
########################################################



:product_characteristic_id: Component Characteristic, many2one





:characteristic_id: Parent Characteristic, many2one





:product_qty: Product Qty, float





:bom_id: BOM, many2one, required





:exclude: Exclude, boolean





:characteristic_group_id: characteristic group, string, readonly


