
.. module:: report_hotel_reservation
    :synopsis: Hotel Reservation Management - Reporting 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_hotel_reservation"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Hotel Reservation Management - Reporting (*report_hotel_reservation*)
=====================================================================
:Module: report_hotel_reservation
:Name: Hotel Reservation Management - Reporting
:Version: 5.0.1.0
:Author: Tiny
:Directory: report_hotel_reservation
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  Module shows the status of room reservation
       * Current status of reserved room
       * List status of room as draft or done state

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/report_hotel_reservation.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/report_hotel_reservation.zip>`_


Dependencies
------------

 * :mod:`hotel_reservation`

Reports
-------

None


Menus
-------

 * Hotel Management/Reports/This Month
 * Hotel Management/Reports/This Month/States By Reservation

Views
-----

 * report.hotel.reservation.status.tree (tree)
 * report.hotel.reservation.status.form (form)
 * report.hotel.reservation.status.graph (graph)
 * report.hotel.reservation.status.graph (graph)


Objects
-------

Object: Reservation By State (report.hotel.reservation.status)
##############################################################



:nbr: Reservation, integer, readonly





:state: State, selection, readonly





:reservation_no: Reservation No, char, readonly


