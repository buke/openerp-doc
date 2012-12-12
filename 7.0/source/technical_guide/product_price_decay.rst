
.. module:: product_price_decay
    :synopsis: Product Decay - work in progress 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Product Decay - work in progress (*product_price_decay*)
========================================================
:Module: product_price_decay
:Name: Product Decay - work in progress
:Version: 0.1
:Author: Smile.fr
:Directory: product_price_decay
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  Product Decay
  the goal of this module, is to estimate the average price of the remaining product stock using the following assertions:
  - the remaining stock is based on the invoiced products only (from purchases and sales)
  - everything happen like if we sale first the more expensive remaining products
  
  So it's a bit like FIFO (if prices were always falling it would look like FIFO) but it's certainly not a
  legal way of valuing your stocks.
  
  Actually this module only gives you an indicative price that you could base your sale margin upon, so that:
  - you always ensure a given margin
  - you make sure your sale price will follow the market, meaning decay hopefully
      
Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/product_price_decay.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/product_price_decay.zip>`_

Dependencies
------------

 * :mod:`product`
 * :mod:`account`

Reports
-------

None


Menus
-------


None


Views
-----


None



Objects
-------

None
