
.. module:: pos_tax_include
    :synopsis: Invoices and prices with taxes included 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/pos_tax_include"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Invoices and prices with taxes included (*pos_tax_include*)
===========================================================
:Module: pos_tax_include
:Name: Invoices and prices with taxes included
:Version: 5.0.1.0
:Author: Tiny
:Directory: pos_tax_include
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Allow the user to work tax included prices.
  Especially useful for b2c businesses.
  
  This module implement the modification on the pos order form.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/pos_tax_include.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/pos_tax_include.zip>`_


Dependencies
------------

 * :mod:`point_of_sale`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT pos.order.qty.view.form (form)
 * \* INHERIT pos.order.exlcuded.view.form (form)
 * \* INHERIT pos.order.qty.view.form (form)
 * \* INHERIT pos.order.qty.view.form (form)
 * \* INHERIT pos.order.discount.view.form (form)
 * \* INHERIT pos.order.discount.view.form (form)
 * \* INHERIT pos.order.price_ded.view.form (form)
 * \* INHERIT pos.order.price_ded.view.form (form)


Objects
-------

None
