
.. i18n: .. module:: fashion
.. i18n:     :synopsis: Tiny TERP fashion module 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: fashion
    :synopsis: Tiny TERP fashion module 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/fashion"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/fashion"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Tiny TERP fashion module (*fashion*)
.. i18n: ====================================
.. i18n: :Module: fashion
.. i18n: :Name: Tiny TERP fashion module
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Manou
.. i18n: :Directory: fashion
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Product characteristics
..

::

  Product characteristics

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/fashion.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/fashion.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/fashion.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/fashion.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`product`
.. i18n:  * :mod:`mrp`
..

 * :mod:`base`
 * :mod:`product`
 * :mod:`mrp`

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

.. i18n:  * Production
.. i18n:  * Production/Definitions
.. i18n:  * Production/Definitions/Characteristics
.. i18n:  * Production/Definitions/Characteristics/Characteristic Groups
.. i18n:  * Production/Definitions/Characteristics/Characteristic
..

 * Production
 * Production/Definitions
 * Production/Definitions/Characteristics
 * Production/Definitions/Characteristics/Characteristic Groups
 * Production/Definitions/Characteristics/Characteristic

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * mrp.characteristic.group.tree (tree)
.. i18n:  * mrp.characteristic.group.form (form)
.. i18n:  * mrp.characteristic.tree (tree)
.. i18n:  * mrp.characteristic.form (form)
.. i18n:  * \* INHERIT product.variant.form (form)
.. i18n:  * \* INHERIT product.template.product.form (form)
.. i18n:  * \* INHERIT mrp.bom.form (form)
.. i18n:  * mrp.bom.variation.form (form)
.. i18n:  * mrp.bom.variation.tree (tree)
..

 * mrp.characteristic.group.tree (tree)
 * mrp.characteristic.group.form (form)
 * mrp.characteristic.tree (tree)
 * mrp.characteristic.form (form)
 * \* INHERIT product.variant.form (form)
 * \* INHERIT product.template.product.form (form)
 * \* INHERIT mrp.bom.form (form)
 * mrp.bom.variation.form (form)
 * mrp.bom.variation.tree (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Characteristic Group (mrp.characteristic.group)
.. i18n: #######################################################
..

Object: Characteristic Group (mrp.characteristic.group)
#######################################################

.. i18n: :axis: Preferred axis for layout, selection
..

:axis: Preferred axis for layout, selection

.. i18n: :description: Description, text
..

:description: Description, text

.. i18n: :name: Characteristic Group, char, required
..

:name: Characteristic Group, char, required

.. i18n: Object: Characteristic (mrp.characteristic)
.. i18n: ###########################################
..

Object: Characteristic (mrp.characteristic)
###########################################

.. i18n: :group_id: Characteristic Group, many2one, required
..

:group_id: Characteristic Group, many2one, required

.. i18n: :name: Characteristic, char, required
..

:name: Characteristic, char, required

.. i18n: :magnitude: Magnitude, float
..

:magnitude: Magnitude, float

.. i18n: :description: Description, text
..

:description: Description, text

.. i18n: Object: BOM characteristic variation (mrp.bom.variation)
.. i18n: ########################################################
..

Object: BOM characteristic variation (mrp.bom.variation)
########################################################

.. i18n: :product_characteristic_id: Component Characteristic, many2one
..

:product_characteristic_id: Component Characteristic, many2one

.. i18n: :characteristic_id: Parent Characteristic, many2one
..

:characteristic_id: Parent Characteristic, many2one

.. i18n: :product_qty: Product Qty, float
..

:product_qty: Product Qty, float

.. i18n: :bom_id: BOM, many2one, required
..

:bom_id: BOM, many2one, required

.. i18n: :exclude: Exclude, boolean
..

:exclude: Exclude, boolean

.. i18n: :characteristic_group_id: characteristic group, string, readonly
..

:characteristic_group_id: characteristic group, string, readonly
