
.. i18n: .. module:: product_images_olbs
.. i18n:     :synopsis: Product Image Gallery 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: product_images_olbs
    :synopsis: Product Image Gallery 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/product_images_olbs"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/product_images_olbs"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Product Image Gallery (*product_images_olbs*)
.. i18n: =============================================
.. i18n: :Module: product_images_olbs
.. i18n: :Name: Product Image Gallery
.. i18n: :Version: 5.0.0.1 
.. i18n: :Author: Sharoon Thomas, Open Labs Business Solutions
.. i18n: :Directory: product_images_olbs
.. i18n: :Web: http://openlabs.co.in/
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

Product Image Gallery (*product_images_olbs*)
=============================================
:Module: product_images_olbs
:Name: Product Image Gallery
:Version: 5.0.0.1 
:Author: Sharoon Thomas, Open Labs Business Solutions
:Directory: product_images_olbs
:Web: http://openlabs.co.in/
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This Module implements an Image Gallery for products.
.. i18n:       You can add images against every product.
.. i18n:       
.. i18n:       This module is generic but built for Magento ERP connector and
.. i18n:       the upcoming e-commerce system for OpenERP by Open Labs
..

::

  This Module implements an Image Gallery for products.
      You can add images against every product.
      
      This module is generic but built for Magento ERP connector and
      the upcoming e-commerce system for OpenERP by Open Labs

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n: (No download links available)
..

(No download links available)

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

.. i18n: None
..

None

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * product.images.form (form)
.. i18n:  * product.images.tree (tree)
.. i18n:  * \* INHERIT product.product.images (tree)
..

 * product.images.form (form)
 * product.images.tree (tree)
 * \* INHERIT product.product.images (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Products Image gallery (product.images)
.. i18n: ###############################################
..

Object: Products Image gallery (product.images)
###############################################

.. i18n: :product_id: Product, many2one
..

:product_id: Product, many2one

.. i18n: :image: Image, binary
..

:image: Image, binary

.. i18n: :comments: Comments, text
..

:comments: Comments, text

.. i18n: :filename: File Location, char
..

:filename: File Location, char

.. i18n: :link: Link?, boolean
..

:link: Link?, boolean

.. i18n:     *Images can be linked from files on your file system or remote (Preferred)*
..

    *Images can be linked from files on your file system or remote (Preferred)*

.. i18n: :preview: unknown, binary, readonly
..

:preview: unknown, binary, readonly

.. i18n: :name: Image Title, char, required
..

:name: Image Title, char, required
