
.. module:: product_variant_multi
    :synopsis: Products with multi-level variants 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/product_variant_multi"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Products with multi-level variants (*product_variant_multi*)
============================================================
:Module: product_variant_multi
:Name: Products with multi-level variants
:Version: 5.0.1.0
:Author: Tiny
:Directory: product_variant_multi
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  OpenERP is already supporting a product variants at the core level. But
  without this module, variants are only mono-axial. OpenERP indeed uses the product.template
  as the model object and the product.variant as the instance variant.
  Using this module, you can now easily deal with multi-axial variants.
  A product.template, now has a set of dimensions (like Color, Size, anything you want).
  For each dimension, a product.template has a set of dimension values (like Red, Green
  for the Color dimension). For each dimension, you can accept or not custom dimension
  values. The sale interface product configurator will take it into account.
  Once the product.template is set up, you can use a 'generator' button that will populate
  the space of the variants. You could also choose to populate only some combinations
  by hand instead.
  Each variant can have an extra price that will be taken into account when computing
  the base listed price. Yet to be implemented: a price extra per variant dimension value.
  Finally, this module is better used along with the product_variant_configurator which
  will help the salesman selecting the appropriate variant in the sale order line
  using dimension criteria instead of having to crawl the full space of variants.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/product_variant_multi.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/product_variant_multi.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`product`

Reports
-------

None


Menus
-------

 * Products/Products/Product Templates
 * Products/Products/Product Variants
 * Products/Configuration/Variant Dimensions
 * Products/Configuration/Variant Dimensions/Dimension Types
 * Products/Configuration/Variant Dimensions/Dimension Values

Views
-----

 * product_variant_multi.variant_value.tree (tree)
 * product_variant_multi.variant_value.form (form)
 * product_variant_multi.variant_type.tree (tree)
 * product_variant_multi.variant_type.form (form)
 * \* INHERIT product_variant_multi.product.template.form (form)
 * \* INHERIT product_variant_multi.product.product.form (form)


Objects
-------

Object: Dimension Type (product.variant.dimension.type)
#######################################################



:product_tmpl_id: Product Template, many2one, required





:allow_custom_value: Allow Custom Value, boolean

    *If true, custom values can be entered in the product configurator*



:name: Dimension, char





:value_ids: Dimension Values, one2many





:sequence: Sequence, integer

    *The product 'variants' code will use this to order the dimension values*


Object: Dimension Value (product.variant.dimension.value)
#########################################################



:name: Dimension Value, char, required





:sequence: Sequence, integer





:dimension_id: Dimension Type, many2one, required





:dimension_sequence: Related Dimension Sequence, float





:price_extra: Price Extra, float





:product_tmpl_id: Product Template, many2one





:price_margin: Price Margin, float


