
.. module:: library
    :synopsis: Library Management 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/library"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Library Management (*library*)
==============================
:Module: library
:Name: Library Management
:Version: 5.0.1.0
:Author: Tiny
:Directory: library
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  Module to manage library.
      Books Information,
      Publisher and Author Information,
      Book Rack Tracking etc...

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/library.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/library.zip>`_


Dependencies
------------

 * :mod:`point_of_sale`
 * :mod:`report_intrastat`
 * :mod:`mrp`
 * :mod:`delivery`

Reports
-------

None


Menus
-------

 * Products/Authors
 * Products/Authors/New Author
 * Products/Books
 * Products/Books/Books to return before 30 days
 * Sales Management/Orders of the day
 * Sales Management/Orders of the day/My orders of the day
 * Partners/Editor - Suppliers Relations
 * Products/Books/New Book
 * Books/Configuration/Price Categories

Views
-----

 * product.product.tree (tree)
 * library.author.form (form)
 * library.author.tree (tree)
 * Library Rack (form)
 * product.book.tree.view (tree)
 * product.book.form.view (form)
 * sale.order.tree (tree)
 * account.invoice.tree (tree)
 * stock.picking.tree (tree)
 * library.price.category (tree)
 * library.price.category (form)
 * library.editor.supplier (form)
 * Editor - supplier relations (tree)
 * \* INHERIT mrp.procurement.form (form)
 * \* INHERIT Stock packing (form)
 * \* INHERIT Stock packing (form)
 * \* INHERIT purchase.order.line.form (form)
 * \* INHERIT sale.order.form (form)
 * \* INHERIT Sale line (form)
 * \* INHERIT Sale Lines (tree)
 * \* INHERIT product.supplierinfo.form.view (form)
 * \* INHERIT purchase.order.line.tree (tree)
 * \* INHERIT account.invoice.line.form (form)


Objects
-------

Object: Book Price Category (library.price.category)
####################################################



:price: Price, float, required





:name: Category, char, required





:product_ids: Books, one2many, readonly




Object: Library Rack (library.rack)
###################################



:active: Active, boolean





:code: Code, char





:name: Name, char, required




Object: Library Collection (library.collection)
###############################################



:code: Code, char





:name: Name, char, required




Object: Author (library.author)
###############################



:first_name: First Name, char





:name: Name, char, required





:editor_ids: Editors, many2many





:book_ids: Books, many2many





:death_date: Date of death, date





:note: Notes, text





:born_date: Date of birth, date





:biography: Biography, text




Object: author.book.rel (author.book.rel)
#########################################



:author_id: Author, many2one





:product_id: Book, many2one




Object: many2many view for editor relations (library.editor.supplier)
#####################################################################



:junk:  , text, readonly





:supplier_id: Supplier, many2one





:name: Editor, many2one





:sequence: Sequence, integer


