
.. module:: stock_routings
    :synopsis: Stock Routings 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/stock_routings"></div>
    <script src="http://js-kit.com/ratings.js"></script>

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

Description
-----------

::

  This Module allows user to define different routings for goods from PO.
                        Goods will transport from one location to another as defined in routings

Download links
--------------

You can download this module as a zip file in the following version:

(No download links available)


Dependencies
------------

 * :mod:`stock`
 * :mod:`purchase`

Reports
-------

None


Menus
-------

 * Stock Management/Configuration/Routings

Views
-----

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


Objects
-------

Object: stock.routing (stock.routing)
#####################################



:kind_transport: Kind Of Transport, selection





:name: Routing Name, char, required





:segment_sequence_ids: Segment Sequence, one2many





:port_of_loading: Incoming Goods Location, many2one





:id: id, integer





:description: Description, char




Object: segment.sequence (segment.sequence)
###########################################



:kind_transport: Kind Of Transport, selection





:name: Segment Name, char





:sequence: Sequence, integer





:chained_delay: Chained Delay (days), integer





:port_of_loading: Depart From, many2one, required





:routing_id: Routing, many2one





:port_of_destination: Destination, many2one, required




Object: stock.history (stock.history)
#####################################



:description: Description/Explanation, char





:new_plan_date: New Planned Date, date





:prev_plan_date: Previous Planned Date, date





:user: User, char





:date: Date, date





:history_id: History, many2one


