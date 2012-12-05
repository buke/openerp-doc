
.. i18n: .. module:: sale_product_multistep_configurator
.. i18n:     :synopsis: MultiStep Product Configurator 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: sale_product_multistep_configurator
    :synopsis: MultiStep Product Configurator 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/sale_product_multistep_configurator"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/sale_product_multistep_configurator"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: MultiStep Product Configurator (*sale_product_multistep_configurator*)
.. i18n: ======================================================================
.. i18n: :Module: sale_product_multistep_configurator
.. i18n: :Name: MultiStep Product Configurator
.. i18n: :Version: 5.0.0.5
.. i18n: :Author: Smile
.. i18n: :Directory: sale_product_multistep_configurator
.. i18n: :Web: http://www.smile.fr
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Generic Multistep configurator
..

::

  Generic Multistep configurator

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/sale_product_multistep_configurator.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/sale_product_multistep_configurator.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/sale_product_multistep_configurator.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/sale_product_multistep_configurator.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`sale`
..

 * :mod:`sale`

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

.. i18n:  * Products/Configuration/Configurator Steps
..

 * Products/Configuration/Configurator Steps

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * product_multistep_configurator_step_list_view_form (form)
.. i18n:  * product_multistep_configurator_step_list_view_tree (tree)
.. i18n:  * \* INHERIT sale.order.form.configurator.inherit (form)
.. i18n:  * \* INHERIT sale.order.form.configurator.inherit2 (form)
.. i18n:  * \* INHERIT sale.order.form.configurator.inherit2 (form)
.. i18n:  * \* INHERIT sale_order_line_form_configurator2 (form)
.. i18n:  * \* INHERIT sale_order_line_form_configurator3 (form)
..

 * product_multistep_configurator_step_list_view_form (form)
 * product_multistep_configurator_step_list_view_tree (tree)
 * \* INHERIT sale.order.form.configurator.inherit (form)
 * \* INHERIT sale.order.form.configurator.inherit2 (form)
 * \* INHERIT sale.order.form.configurator.inherit2 (form)
 * \* INHERIT sale_order_line_form_configurator2 (form)
 * \* INHERIT sale_order_line_form_configurator3 (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: sale_product_multistep_configurator.configurator.step (sale_product_multistep_configurator.configurator.step)
.. i18n: #####################################################################################################################
..

Object: sale_product_multistep_configurator.configurator.step (sale_product_multistep_configurator.configurator.step)
#####################################################################################################################

.. i18n: :model_id: Object ID, many2one, required
..

:model_id: Object ID, many2one, required

.. i18n: :name: Value Name, char
..

:name: Value Name, char

.. i18n: :sequence: Sequence, integer
..

:sequence: Sequence, integer

.. i18n:     *Determine in which order step are executed*
..

    *Determine in which order step are executed*
