
.. module:: hotel_reservation
    :synopsis: Hotel Reservation Management 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hotel_reservation"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Hotel Reservation Management (*hotel_reservation*)
==================================================
:Module: hotel_reservation
:Name: Hotel Reservation Management
:Version: 5.0.1.0
:Author: Tiny
:Directory: hotel_reservation
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  Module for Hotel/Resort/Property management. You can manage:
      * Guest Reservation
      * Group Reservation
        Different reports are also provided, mainly for hotel statistics.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/hotel_reservation.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/hotel_reservation.zip>`_


Dependencies
------------

 * :mod:`hotel`

Reports
-------

 * Reservation Detail

 * CheckOut Detail

 * Max Room Detail

Menus
-------

 * Hotel Management/All Reservation
 * Hotel Management/All Reservation/New Reservation
 * Hotel Management/All Reservation/All Draft Reservation
 * Hotel Management/All Reservation/All Confirm Reservation
 * Hotel Management/All Reservation/All Done Reservation
 * Hotel Management/Reports/Hotel Reservation Report

Views
-----

 * hotel.reservation.form (form)
 * hotel.reservation.tree (tree)
 * hotel.reservation.graph (graph)
 * Room Reservation (calendar)


Objects
-------

Object: Reservation (hotel.reservation)
#######################################



:dummy: Dummy, datetime





:childs: Childs, integer, readonly





:adults: Adults, integer, readonly





:partner_shipping_id: Shipping Address, many2one, required, readonly





:folio_id: Folio, many2many





:checkin: Expected-Date-Arrival, datetime, required, readonly





:reservation_line: Reservation Line, one2many





:partner_order_id: Ordering Contact, many2one, required, readonly

    *The name and address of the contact that requested the order or quotation.*



:state: State, selection, readonly





:shop_id: Shop, many2one, required, readonly





:checkout: Expected-Date-Departure, datetime, required, readonly





:partner_invoice_id: Invoice Address, many2one, required, readonly





:pricelist_id: Pricelist, many2one, required, readonly





:date_order: Date Ordered, datetime, required, readonly





:partner_id: Guest Name, many2one, required, readonly





:reservation_no: Reservation No, char, required




Object: Reservation Line (hotel_reservation.line)
#################################################



:line_id: unknown, many2one





:categ_id: Room Type, many2one





:reserve: unknown, many2many


