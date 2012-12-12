
.. module:: product_variant_configurator
    :synopsis: Products with multi-level variants configurator 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/product_variant_configurator"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Products with multi-level variants configurator (*product_variant_configurator*)
================================================================================
:Module: product_variant_configurator
:Name: Products with multi-level variants configurator
:Version: 5.0.0.5
:Author: Smile.fr
:Directory: product_variant_configurator
:Web: http://www.smile.fr
:Official module: no
:Quality certified: no

Description
-----------

::

  Product Variant Configurator. Assists the product variant selection in the sale order form.
  For each product template dimension a dimension value is asked. Then the matching product variants
  are proposed for selection.
  Should be used along with the product_variant_multi module.
  Might not work well in the web-client due to web-client current limitations.
  
  Please notice that the product configurator user interface could me more user friendly
  if some OpenObject framework enhancements were implemented, especially:
  - allow select box widget to select dimension values instead of many2one popups:
  https://blueprints.launchpad.net/openobject-server/+spec/dynamic-domain-on-selection-widget
  - automatically select the product variant if unique once dimensions are set:
  https://blueprints.launchpad.net/openobject-server/+spec/form-parent-field-update-on-change

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/product_variant_configurator.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/product_variant_configurator.zip>`_


Dependencies
------------

 * :mod:`product_variant_multi`
 * :mod:`sale`
 * :mod:`sale_product_multistep_configurator`

Reports
-------

None


Menus
-------


None


Views
-----

 * view_product_variant_configurator (form)
 * \* INHERIT product_variant_configurator.sale_order_form_view (form)
 * \* INHERIT product_variant_configurator.sale_order_line_form_view (form)


Objects
-------

Object: sale.order.line.dimension_custom_values (sale.order.line.dimension_custom_values)
#########################################################################################



:mrp_production_id: Production Order, many2one





:sale_order_line_id: Sale Order Line, many2one





:custom_value: Custom Value, char





:dimension_type_id: Dimension Type, many2one




Object: product_variant_configurator.line (product_variant_configurator.line)
#############################################################################



:dimension_type_id: Dimension Type, many2one





:dimension_custom_value: Custom Value, char





:allow_custom_value: Allow custom values ?, boolean





:dimension_type_value_id: Dimension Value, many2one





:configurator_id: product_variant_configurator Test, many2one




Object: product_variant_configurator.configurator (product_variant_configurator.configurator)
#############################################################################################



:product_tmpl_id: Product Template, many2one





:dimension_configuration_line_ids: Configurator Lines, one2many





:product_variant_id: Product Variant, many2one, required


