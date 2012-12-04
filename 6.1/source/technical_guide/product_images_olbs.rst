
.. module:: product_images_olbs
    :synopsis: Product Image Gallery 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/product_images_olbs"></div>
    <script src="http://js-kit.com/ratings.js"></script>

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

Description
-----------

::

  This Module implements an Image Gallery for products.
      You can add images against every product.
      
      This module is generic but built for Magento ERP connector and
      the upcoming e-commerce system for OpenERP by Open Labs

Download links
--------------

You can download this module as a zip file in the following version:

(No download links available)


Dependencies
------------

 * :mod:`base`
 * :mod:`product`

Reports
-------

None


Menus
-------


None


Views
-----

 * product.images.form (form)
 * product.images.tree (tree)
 * \* INHERIT product.product.images (tree)


Objects
-------

Object: Products Image gallery (product.images)
###############################################



:product_id: Product, many2one





:image: Image, binary





:comments: Comments, text





:filename: File Location, char





:link: Link?, boolean

    *Images can be linked from files on your file system or remote (Preferred)*



:preview: unknown, binary, readonly





:name: Image Title, char, required


