
.. i18n: .. module:: stock_routings
.. i18n:     :synopsis: Stock Routings 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: stock_routings
    :synopsis: Stock Routings 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/stock_routings"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/stock_routings"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Stock Routings (*stock_routings*)
.. i18n: =================================
.. i18n: :Module: stock_routings
.. i18n: :Name: Stock Routings
.. i18n: :Version: 5.0.1.1
.. i18n: :Author: Axelor
.. i18n: :Directory: stock_routings
.. i18n: :Web: http://www.axelor.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

Stock Routings (*stock_routings*)
=================================
:Module: stock_routings
:Name: Stock Routings
:Version: 5.0.1.1
:Author: Axelor
:Directory: stock_routings
:Web: http://www.axelor.com
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This Module allows user to define different routings for goods from PO.
.. i18n:                         Goods will transport from one location to another as defined in routings
..

::

  This Module allows user to define different routings for goods from PO.
                        Goods will transport from one location to another as defined in routings

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

.. i18n:  * :mod:`stock`
.. i18n:  * :mod:`purchase`
..

 * :mod:`stock`
 * :mod:`purchase`

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

.. i18n:  * Stock Management/Configuration/Routings
..

 * Stock Management/Configuration/Routings

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT Purchase Order Form add Manager Group Cancel Button (form)
.. i18n:  * \* INHERIT Purchase Order Form State in Confirm Button (form)
.. i18n:  * \* INHERIT Purchase Order Form add RFQ Button (form)
.. i18n:  * \* INHERIT Purchase Order Form replace delivery page position (form)
.. i18n:  * \* INHERIT Picking Form add btn for change planned date (form)
.. i18n:  * \* INHERIT Picking Form add State in date fields (form)
.. i18n:  * \* INHERIT Picking Form add Transport Page in Incoming (form)
.. i18n:  * \* INHERIT Moves Form add btn for change planned date (form)
.. i18n:  * \* INHERIT Moves Form add Picking And System date (form)
.. i18n:  * \* INHERIT Internal Move From view Add Picking Date (form)
.. i18n:  * \* INHERIT Incoming Prod Internal Move From view Add Picking Date (form)
.. i18n:  * \* INHERIT Moves Form make planned date readonly (form)
.. i18n:  * \* INHERIT Picking Form add Transport Page in Internal Move (form)
.. i18n:  * stock.routing.tree (tree)
.. i18n:  * stock.routing.form (form)
.. i18n:  * stock.history.tree (tree)
.. i18n:  * stock.history.form (form)
..

 * \* INHERIT Purchase Order Form add Manager Group Cancel Button (form)
 * \* INHERIT Purchase Order Form State in Confirm Button (form)
 * \* INHERIT Purchase Order Form add RFQ Button (form)
 * \* INHERIT Purchase Order Form replace delivery page position (form)
 * \* INHERIT Picking Form add btn for change planned date (form)
 * \* INHERIT Picking Form add State in date fields (form)
 * \* INHERIT Picking Form add Transport Page in Incoming (form)
 * \* INHERIT Moves Form add btn for change planned date (form)
 * \* INHERIT Moves Form add Picking And System date (form)
 * \* INHERIT Internal Move From view Add Picking Date (form)
 * \* INHERIT Incoming Prod Internal Move From view Add Picking Date (form)
 * \* INHERIT Moves Form make planned date readonly (form)
 * \* INHERIT Picking Form add Transport Page in Internal Move (form)
 * stock.routing.tree (tree)
 * stock.routing.form (form)
 * stock.history.tree (tree)
 * stock.history.form (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: stock.routing (stock.routing)
.. i18n: #####################################
..

Object: stock.routing (stock.routing)
#####################################

.. i18n: :kind_transport: Kind Of Transport, selection
..

:kind_transport: Kind Of Transport, selection

.. i18n: :name: Routing Name, char, required
..

:name: Routing Name, char, required

.. i18n: :segment_sequence_ids: Segment Sequence, one2many
..

:segment_sequence_ids: Segment Sequence, one2many

.. i18n: :port_of_loading: Incoming Goods Location, many2one
..

:port_of_loading: Incoming Goods Location, many2one

.. i18n: :id: id, integer
..

:id: id, integer

.. i18n: :description: Description, char
..

:description: Description, char

.. i18n: Object: segment.sequence (segment.sequence)
.. i18n: ###########################################
..

Object: segment.sequence (segment.sequence)
###########################################

.. i18n: :kind_transport: Kind Of Transport, selection
..

:kind_transport: Kind Of Transport, selection

.. i18n: :name: Segment Name, char
..

:name: Segment Name, char

.. i18n: :sequence: Sequence, integer
..

:sequence: Sequence, integer

.. i18n: :chained_delay: Chained Delay (days), integer
..

:chained_delay: Chained Delay (days), integer

.. i18n: :port_of_loading: Depart From, many2one, required
..

:port_of_loading: Depart From, many2one, required

.. i18n: :routing_id: Routing, many2one
..

:routing_id: Routing, many2one

.. i18n: :port_of_destination: Destination, many2one, required
..

:port_of_destination: Destination, many2one, required

.. i18n: Object: stock.history (stock.history)
.. i18n: #####################################
..

Object: stock.history (stock.history)
#####################################

.. i18n: :description: Description/Explanation, char
..

:description: Description/Explanation, char

.. i18n: :new_plan_date: New Planned Date, date
..

:new_plan_date: New Planned Date, date

.. i18n: :prev_plan_date: Previous Planned Date, date
..

:prev_plan_date: Previous Planned Date, date

.. i18n: :user: User, char
..

:user: User, char

.. i18n: :date: Date, date
..

:date: Date, date

.. i18n: :history_id: History, many2one
..

:history_id: History, many2one
