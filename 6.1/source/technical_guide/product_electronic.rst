
.. i18n: .. module:: product_electronic
.. i18n:     :synopsis: Products Attributes & Manufacturers 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: product_electronic
    :synopsis: Products Attributes & Manufacturers 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/product_electronic"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/product_electronic"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Products Attributes & Manufacturers (*product_electronic*)
.. i18n: ==========================================================
.. i18n: :Module: product_electronic
.. i18n: :Name: Products Attributes & Manufacturers
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: product_electronic
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

Products Attributes & Manufacturers (*product_electronic*)
==========================================================
:Module: product_electronic
:Name: Products Attributes & Manufacturers
:Version: 5.0.1.0
:Author: Tiny
:Directory: product_electronic
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
.. i18n:   A module that add manufacturers and attributes on the product form
..

::

  A module that add manufacturers and attributes on the product form

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/product_electronic.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/product_electronic.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/product_electronic.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/product_electronic.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/product_electronic.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/product_electronic.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`account`
.. i18n:  * :mod:`product`
.. i18n:  * :mod:`stock`
..

 * :mod:`base`
 * :mod:`account`
 * :mod:`product`
 * :mod:`stock`

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

.. i18n: None
..

None

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT product.normal.form (form)
.. i18n:  * product.electronic.attribute.tree (tree)
.. i18n:  * product.electronic.attribute.form (form)
..

 * \* INHERIT product.normal.form (form)
 * product.electronic.attribute.tree (tree)
 * product.electronic.attribute.form (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Product attributes (product.electronic.attribute)
.. i18n: #########################################################
..

Object: Product attributes (product.electronic.attribute)
#########################################################

.. i18n: :name: Attribute, char, required
..

:name: Attribute, char, required

.. i18n: :value: Value, char
..

:value: Value, char

.. i18n: :product_id: Product, many2one
..

:product_id: Product, many2one
