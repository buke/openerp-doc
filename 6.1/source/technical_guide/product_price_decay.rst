
.. i18n: .. module:: product_price_decay
.. i18n:     :synopsis: Product Decay - work in progress 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: product_price_decay
    :synopsis: Product Decay - work in progress 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />
..

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: Product Decay - work in progress (*product_price_decay*)
.. i18n: ========================================================
.. i18n: :Module: product_price_decay
.. i18n: :Name: Product Decay - work in progress
.. i18n: :Version: 0.1
.. i18n: :Author: Smile.fr
.. i18n: :Directory: product_price_decay
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Product Decay
.. i18n:   the goal of this module, is to estimate the average price of the remaining product stock using the following assertions:
.. i18n:   - the remaining stock is based on the invoiced products only (from purchases and sales)
.. i18n:   - everything happen like if we sale first the more expensive remaining products
.. i18n:   
.. i18n:   So it's a bit like FIFO (if prices were always falling it would look like FIFO) but it's certainly not a
.. i18n:   legal way of valuing your stocks.
.. i18n:   
.. i18n:   Actually this module only gives you an indicative price that you could base your sale margin upon, so that:
.. i18n:   - you always ensure a given margin
.. i18n:   - you make sure your sale price will follow the market, meaning decay hopefully
.. i18n:       
.. i18n: Download links
.. i18n: --------------
..

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

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/product_price_decay.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/product_price_decay.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/product_price_decay.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/product_price_decay.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`product`
.. i18n:  * :mod:`account`
..

 * :mod:`product`
 * :mod:`account`

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

.. i18n: None
..

None

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: None
..

None
