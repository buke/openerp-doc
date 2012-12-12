
.. module:: sale_product_multistep_configurator
    :synopsis: MultiStep Product Configurator 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/sale_product_multistep_configurator"></div>
    <script src="http://js-kit.com/ratings.js"></script>

MultiStep Product Configurator (*sale_product_multistep_configurator*)
======================================================================
:Module: sale_product_multistep_configurator
:Name: MultiStep Product Configurator
:Version: 5.0.0.5
:Author: Smile
:Directory: sale_product_multistep_configurator
:Web: http://www.smile.fr
:Official module: no
:Quality certified: no

Description
-----------

::

  Generic Multistep configurator

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/sale_product_multistep_configurator.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/sale_product_multistep_configurator.zip>`_


Dependencies
------------

 * :mod:`sale`

Reports
-------

None


Menus
-------

 * Products/Configuration/Configurator Steps

Views
-----

 * product_multistep_configurator_step_list_view_form (form)
 * product_multistep_configurator_step_list_view_tree (tree)
 * \* INHERIT sale.order.form.configurator.inherit (form)
 * \* INHERIT sale.order.form.configurator.inherit2 (form)
 * \* INHERIT sale.order.form.configurator.inherit2 (form)
 * \* INHERIT sale_order_line_form_configurator2 (form)
 * \* INHERIT sale_order_line_form_configurator3 (form)


Objects
-------

Object: sale_product_multistep_configurator.configurator.step (sale_product_multistep_configurator.configurator.step)
#####################################################################################################################



:model_id: Object ID, many2one, required





:name: Value Name, char





:sequence: Sequence, integer

    *Determine in which order step are executed*
