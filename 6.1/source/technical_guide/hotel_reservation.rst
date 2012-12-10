
.. i18n: .. module:: hotel_reservation
.. i18n:     :synopsis: Hotel Reservation Management 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: hotel_reservation
    :synopsis: Hotel Reservation Management 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hotel_reservation"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/hotel_reservation"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Hotel Reservation Management (*hotel_reservation*)
.. i18n: ==================================================
.. i18n: :Module: hotel_reservation
.. i18n: :Name: Hotel Reservation Management
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: hotel_reservation
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Module for Hotel/Resort/Property management. You can manage:
.. i18n:       * Guest Reservation
.. i18n:       * Group Reservation
.. i18n:         Different reports are also provided, mainly for hotel statistics.
..

::

  Module for Hotel/Resort/Property management. You can manage:
      * Guest Reservation
      * Group Reservation
        Different reports are also provided, mainly for hotel statistics.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/hotel_reservation.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/hotel_reservation.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/hotel_reservation.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/hotel_reservation.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`hotel`
..

 * :mod:`hotel`

.. i18n: Reports
.. i18n: -------
..

Reports
-------

.. i18n:  * Reservation Detail
.. i18n: 
.. i18n:  * CheckOut Detail
.. i18n: 
.. i18n:  * Max Room Detail
..

 * Reservation Detail

 * CheckOut Detail

 * Max Room Detail

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Hotel Management/All Reservation
.. i18n:  * Hotel Management/All Reservation/New Reservation
.. i18n:  * Hotel Management/All Reservation/All Draft Reservation
.. i18n:  * Hotel Management/All Reservation/All Confirm Reservation
.. i18n:  * Hotel Management/All Reservation/All Done Reservation
.. i18n:  * Hotel Management/Reports/Hotel Reservation Report
..

 * Hotel Management/All Reservation
 * Hotel Management/All Reservation/New Reservation
 * Hotel Management/All Reservation/All Draft Reservation
 * Hotel Management/All Reservation/All Confirm Reservation
 * Hotel Management/All Reservation/All Done Reservation
 * Hotel Management/Reports/Hotel Reservation Report

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * hotel.reservation.form (form)
.. i18n:  * hotel.reservation.tree (tree)
.. i18n:  * hotel.reservation.graph (graph)
.. i18n:  * Room Reservation (calendar)
..

 * hotel.reservation.form (form)
 * hotel.reservation.tree (tree)
 * hotel.reservation.graph (graph)
 * Room Reservation (calendar)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Reservation (hotel.reservation)
.. i18n: #######################################
..

Object: Reservation (hotel.reservation)
#######################################

.. i18n: :dummy: Dummy, datetime
..

:dummy: Dummy, datetime

.. i18n: :childs: Childs, integer, readonly
..

:childs: Childs, integer, readonly

.. i18n: :adults: Adults, integer, readonly
..

:adults: Adults, integer, readonly

.. i18n: :partner_shipping_id: Shipping Address, many2one, required, readonly
..

:partner_shipping_id: Shipping Address, many2one, required, readonly

.. i18n: :folio_id: Folio, many2many
..

:folio_id: Folio, many2many

.. i18n: :checkin: Expected-Date-Arrival, datetime, required, readonly
..

:checkin: Expected-Date-Arrival, datetime, required, readonly

.. i18n: :reservation_line: Reservation Line, one2many
..

:reservation_line: Reservation Line, one2many

.. i18n: :partner_order_id: Ordering Contact, many2one, required, readonly
..

:partner_order_id: Ordering Contact, many2one, required, readonly

.. i18n:     *The name and address of the contact that requested the order or quotation.*
..

    *The name and address of the contact that requested the order or quotation.*

.. i18n: :state: State, selection, readonly
..

:state: State, selection, readonly

.. i18n: :shop_id: Shop, many2one, required, readonly
..

:shop_id: Shop, many2one, required, readonly

.. i18n: :checkout: Expected-Date-Departure, datetime, required, readonly
..

:checkout: Expected-Date-Departure, datetime, required, readonly

.. i18n: :partner_invoice_id: Invoice Address, many2one, required, readonly
..

:partner_invoice_id: Invoice Address, many2one, required, readonly

.. i18n: :pricelist_id: Pricelist, many2one, required, readonly
..

:pricelist_id: Pricelist, many2one, required, readonly

.. i18n: :date_order: Date Ordered, datetime, required, readonly
..

:date_order: Date Ordered, datetime, required, readonly

.. i18n: :partner_id: Guest Name, many2one, required, readonly
..

:partner_id: Guest Name, many2one, required, readonly

.. i18n: :reservation_no: Reservation No, char, required
..

:reservation_no: Reservation No, char, required

.. i18n: Object: Reservation Line (hotel_reservation.line)
.. i18n: #################################################
..

Object: Reservation Line (hotel_reservation.line)
#################################################

.. i18n: :line_id: unknown, many2one
..

:line_id: unknown, many2one

.. i18n: :categ_id: Room Type, many2one
..

:categ_id: Room Type, many2one

.. i18n: :reserve: unknown, many2many
..

:reserve: unknown, many2many
