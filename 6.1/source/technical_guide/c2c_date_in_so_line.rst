
.. module:: c2c_date_in_so_line
    :synopsis: Date in SO lines 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/c2c_date_in_so_line"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Date in SO lines (*c2c_date_in_so_line*)
========================================
:Module: c2c_date_in_so_line
:Name: Date in SO lines
:Version: 5.0.1.0
:Author: Camptocamp SA
:Directory: c2c_date_in_so_line
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  This module allows to set planned execution date in Sale order
      When the SO is confirmed the delay is automatically computed, you do not have to use 
      day for computing Delivery date of generated picking. If a date is set on the SO, it will automatically be taken in SO line, if not it will recompute a date based on the product customer lead time !!!Warning this module overwrites the SO line product_id_change function and add a parameters in signature. If another module does the same they will conflict

Download links
--------------

You can download this module as a zip file in the following version:

(No download links available)


Dependencies
------------

 * :mod:`base`
 * :mod:`sale`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT sale.order.form (form)
 * \* INHERIT sale.order.form (form)
 * \* INHERIT sale.order.form (form)


Objects
-------

None
