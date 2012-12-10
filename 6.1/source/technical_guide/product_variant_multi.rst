
.. i18n: .. module:: product_variant_multi
.. i18n:     :synopsis: Products with multi-level variants 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: product_variant_multi
    :synopsis: Products with multi-level variants 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/product_variant_multi"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/product_variant_multi"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Products with multi-level variants (*product_variant_multi*)
.. i18n: ============================================================
.. i18n: :Module: product_variant_multi
.. i18n: :Name: Products with multi-level variants
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: product_variant_multi
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   OpenERP is already supporting a product variants at the core level. But
.. i18n:   without this module, variants are only mono-axial. OpenERP indeed uses the product.template
.. i18n:   as the model object and the product.variant as the instance variant.
.. i18n:   Using this module, you can now easily deal with multi-axial variants.
.. i18n:   A product.template, now has a set of dimensions (like Color, Size, anything you want).
.. i18n:   For each dimension, a product.template has a set of dimension values (like Red, Green
.. i18n:   for the Color dimension). For each dimension, you can accept or not custom dimension
.. i18n:   values. The sale interface product configurator will take it into account.
.. i18n:   Once the product.template is set up, you can use a 'generator' button that will populate
.. i18n:   the space of the variants. You could also choose to populate only some combinations
.. i18n:   by hand instead.
.. i18n:   Each variant can have an extra price that will be taken into account when computing
.. i18n:   the base listed price. Yet to be implemented: a price extra per variant dimension value.
.. i18n:   Finally, this module is better used along with the product_variant_configurator which
.. i18n:   will help the salesman selecting the appropriate variant in the sale order line
.. i18n:   using dimension criteria instead of having to crawl the full space of variants.
..

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

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/product_variant_multi.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/product_variant_multi.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/product_variant_multi.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/product_variant_multi.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`product`
..

 * :mod:`base`
 * :mod:`product`

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

.. i18n:  * Products/Products/Product Templates
.. i18n:  * Products/Products/Product Variants
.. i18n:  * Products/Configuration/Variant Dimensions
.. i18n:  * Products/Configuration/Variant Dimensions/Dimension Types
.. i18n:  * Products/Configuration/Variant Dimensions/Dimension Values
..

 * Products/Products/Product Templates
 * Products/Products/Product Variants
 * Products/Configuration/Variant Dimensions
 * Products/Configuration/Variant Dimensions/Dimension Types
 * Products/Configuration/Variant Dimensions/Dimension Values

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * product_variant_multi.variant_value.tree (tree)
.. i18n:  * product_variant_multi.variant_value.form (form)
.. i18n:  * product_variant_multi.variant_type.tree (tree)
.. i18n:  * product_variant_multi.variant_type.form (form)
.. i18n:  * \* INHERIT product_variant_multi.product.template.form (form)
.. i18n:  * \* INHERIT product_variant_multi.product.product.form (form)
..

 * product_variant_multi.variant_value.tree (tree)
 * product_variant_multi.variant_value.form (form)
 * product_variant_multi.variant_type.tree (tree)
 * product_variant_multi.variant_type.form (form)
 * \* INHERIT product_variant_multi.product.template.form (form)
 * \* INHERIT product_variant_multi.product.product.form (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Dimension Type (product.variant.dimension.type)
.. i18n: #######################################################
..

Object: Dimension Type (product.variant.dimension.type)
#######################################################

.. i18n: :product_tmpl_id: Product Template, many2one, required
..

:product_tmpl_id: Product Template, many2one, required

.. i18n: :allow_custom_value: Allow Custom Value, boolean
..

:allow_custom_value: Allow Custom Value, boolean

.. i18n:     *If true, custom values can be entered in the product configurator*
..

    *If true, custom values can be entered in the product configurator*

.. i18n: :name: Dimension, char
..

:name: Dimension, char

.. i18n: :value_ids: Dimension Values, one2many
..

:value_ids: Dimension Values, one2many

.. i18n: :sequence: Sequence, integer
..

:sequence: Sequence, integer

.. i18n:     *The product 'variants' code will use this to order the dimension values*
..

    *The product 'variants' code will use this to order the dimension values*

.. i18n: Object: Dimension Value (product.variant.dimension.value)
.. i18n: #########################################################
..

Object: Dimension Value (product.variant.dimension.value)
#########################################################

.. i18n: :name: Dimension Value, char, required
..

:name: Dimension Value, char, required

.. i18n: :sequence: Sequence, integer
..

:sequence: Sequence, integer

.. i18n: :dimension_id: Dimension Type, many2one, required
..

:dimension_id: Dimension Type, many2one, required

.. i18n: :dimension_sequence: Related Dimension Sequence, float
..

:dimension_sequence: Related Dimension Sequence, float

.. i18n: :price_extra: Price Extra, float
..

:price_extra: Price Extra, float

.. i18n: :product_tmpl_id: Product Template, many2one
..

:product_tmpl_id: Product Template, many2one

.. i18n: :price_margin: Price Margin, float
..

:price_margin: Price Margin, float
