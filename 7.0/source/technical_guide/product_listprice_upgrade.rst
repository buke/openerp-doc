
.. module:: product_listprice_upgrade
    :synopsis: Product listprice upgrade 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/product_listprice_upgrade"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Product listprice upgrade (*product_listprice_upgrade*)
=======================================================
:Module: product_listprice_upgrade
:Name: Product listprice upgrade
:Version: 5.0.1.0
:Author: Tiny
:Directory: product_listprice_upgrade
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  The aim of this module is to allow the automatic upgrade of the field 'List Price' on each product.
      * added a new price type called 'Internal Pricelist' (currently, we have only 2 price types: Sale and Purchase Pricelist)
      * Created a wizard button in the menu Products>Pricelist called 'Upgrade Product List Price'
      * When we have completed the wizard and click on 'Upgrade', it will change the field 'List Price' for all products contained in the categories that we have selected in the wizard

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/product_listprice_upgrade.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/product_listprice_upgrade.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`product`

Reports
-------

None


Menus
-------

 * Products/Pricelists
 * Products/Pricelists/Upgrade Product List price

Views
-----


None



Objects
-------

None
