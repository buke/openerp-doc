
.. i18n: .. module:: stock_location
.. i18n:     :synopsis: Stock Location Paths (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: stock_location
    :synopsis: Stock Location Paths (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/stock_location"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/stock_location"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Stock Location Paths (*stock_location*)
.. i18n: =======================================
.. i18n: :Module: stock_location
.. i18n: :Name: Stock Location Paths
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: stock_location
.. i18n: :Web: 
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

Stock Location Paths (*stock_location*)
=======================================
:Module: stock_location
:Name: Stock Location Paths
:Version: 5.0.1.0
:Author: Tiny
:Directory: stock_location
:Web: 
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Manages product's path in locations.
.. i18n:   
.. i18n:   This module may be useful for different purposes:
.. i18n:   * Manages the product in his whole manufacturing chain
.. i18n:   * Manages different default locations by products
.. i18n:   * Define paths within the warehouse to route products based on operations:
.. i18n:      - Quality Control
.. i18n:      - After Sales Services
.. i18n:      - Supplier Return
.. i18n:   * Manage products to be rent.
..

::

  Manages product's path in locations.
  
  This module may be useful for different purposes:
  * Manages the product in his whole manufacturing chain
  * Manages different default locations by products
  * Define paths within the warehouse to route products based on operations:
     - Quality Control
     - After Sales Services
     - Supplier Return
  * Manage products to be rent.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/stock_location.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/stock_location.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/stock_location.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/stock_location.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`stock`
..

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

.. i18n:  * stock.location.path.tree (tree)
.. i18n:  * stock.location.path.form (form)
.. i18n:  * \* INHERIT product.product.form (form)
..

 * stock.location.path.tree (tree)
 * stock.location.path.form (form)
 * \* INHERIT product.product.form (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: stock.location.path (stock.location.path)
.. i18n: #################################################
..

Object: stock.location.path (stock.location.path)
#################################################

.. i18n: :location_from_id: Source Location, many2one
..

:location_from_id: Source Location, many2one

.. i18n: :product_id: Products, many2one
..

:product_id: Products, many2one

.. i18n: :auto: Automatic Move, selection, required
..

:auto: Automatic Move, selection, required

.. i18n:     *This is used to define paths the product has to follow within the location tree.
.. i18n:     The 'Automatic Move' value will create a stock move after the current one that will be validated automatically. With 'Manual Operation', the stock move has to be validated by a worker. With 'Automatic No Step Added', the location is replaced in the original move.*
..

    *This is used to define paths the product has to follow within the location tree.
    The 'Automatic Move' value will create a stock move after the current one that will be validated automatically. With 'Manual Operation', the stock move has to be validated by a worker. With 'Automatic No Step Added', the location is replaced in the original move.*

.. i18n: :delay: Delay (days), integer
..

:delay: Delay (days), integer

.. i18n:     *Number of days to do this transition*
..

    *Number of days to do this transition*

.. i18n: :location_dest_id: Destination Location, many2one
..

:location_dest_id: Destination Location, many2one

.. i18n: :name: Operation, char
..

:name: Operation, char
