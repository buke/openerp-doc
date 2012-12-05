
.. i18n: .. module:: report_hotel_reservation
.. i18n:     :synopsis: Hotel Reservation Management - Reporting 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: report_hotel_reservation
    :synopsis: Hotel Reservation Management - Reporting 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_hotel_reservation"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_hotel_reservation"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Hotel Reservation Management - Reporting (*report_hotel_reservation*)
.. i18n: =====================================================================
.. i18n: :Module: report_hotel_reservation
.. i18n: :Name: Hotel Reservation Management - Reporting
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: report_hotel_reservation
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Module shows the status of room reservation
.. i18n:        * Current status of reserved room
.. i18n:        * List status of room as draft or done state
..

::

  Module shows the status of room reservation
       * Current status of reserved room
       * List status of room as draft or done state

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/report_hotel_reservation.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/report_hotel_reservation.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/report_hotel_reservation.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/report_hotel_reservation.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`hotel_reservation`
..

 * :mod:`hotel_reservation`

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

.. i18n:  * Hotel Management/Reports/This Month
.. i18n:  * Hotel Management/Reports/This Month/States By Reservation
..

 * Hotel Management/Reports/This Month
 * Hotel Management/Reports/This Month/States By Reservation

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * report.hotel.reservation.status.tree (tree)
.. i18n:  * report.hotel.reservation.status.form (form)
.. i18n:  * report.hotel.reservation.status.graph (graph)
.. i18n:  * report.hotel.reservation.status.graph (graph)
..

 * report.hotel.reservation.status.tree (tree)
 * report.hotel.reservation.status.form (form)
 * report.hotel.reservation.status.graph (graph)
 * report.hotel.reservation.status.graph (graph)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Reservation By State (report.hotel.reservation.status)
.. i18n: ##############################################################
..

Object: Reservation By State (report.hotel.reservation.status)
##############################################################

.. i18n: :nbr: Reservation, integer, readonly
..

:nbr: Reservation, integer, readonly

.. i18n: :state: State, selection, readonly
..

:state: State, selection, readonly

.. i18n: :reservation_no: Reservation No, char, readonly
..

:reservation_no: Reservation No, char, readonly
