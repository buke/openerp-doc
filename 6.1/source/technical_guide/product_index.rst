
.. module:: product_index
    :synopsis: Manage indexes on products prices 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/product_index"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Manage indexes on products prices (*product_index*)
===================================================
:Module: product_index
:Name: Manage indexes on products prices
:Version: 5.0.1.0
:Author: Tiny
:Directory: product_index
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  None

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/product_index.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/product_index.zip>`_


Dependencies
------------

 * :mod:`product`

Reports
-------

None


Menus
-------

 * Products/Configuration/Indexes
 * Products/Configuration/Indexes/New index

Views
-----

 * product.index.tree (tree)
 * product.index.form (form)
 * \* INHERIT product.normal.form (form)


Objects
-------

Object: Index (product.index)
#############################



:rate_ids: Rates, one2many





:code: Index code, char





:name: Index name, char, required





:rounding: Rounding factor, float





:rate: Current rate, float, readonly





:active: Active, boolean




Object: Index Rate (product.index.rate)
#######################################



:rate: Rate, float, required





:index_id: index, many2one, readonly





:name: Date, date, required


