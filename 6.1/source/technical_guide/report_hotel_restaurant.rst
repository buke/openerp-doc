
.. module:: report_hotel_restaurant
    :synopsis: Restaurant Management - Reporting 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_hotel_restaurant"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Restaurant Management - Reporting (*report_hotel_restaurant*)
=============================================================
:Module: report_hotel_restaurant
:Name: Restaurant Management - Reporting
:Version: 5.0.1.0
:Author: Tiny
:Directory: report_hotel_restaurant
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  Module shows the status of restaurant reservation
       * Current status of reserved tables
       * List status of tables as draft or done state

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/report_hotel_restaurant.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/report_hotel_restaurant.zip>`_


Dependencies
------------

 * :mod:`hotel_restaurant`

Reports
-------

None


Menus
-------

 * Hotel Management/Reports/This Month
 * Hotel Management/Reports/This Month/States By Restaurant

Views
-----

 * report.hotel.restaurant.status.tree (tree)
 * report.hotel.restaurant.status.form (form)
 * report.hotel.restaurant.status.graph (graph)
 * report.hotel.restaurant.status.graph (graph)


Objects
-------

Object: Reservation By State (report.hotel.restaurant.status)
#############################################################



:nbr: Reservation, integer, readonly





:state: State, selection, readonly





:reservation_id: Reservation No, char, readonly


