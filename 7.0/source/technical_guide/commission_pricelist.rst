
.. module:: commission_pricelist
    :synopsis: Sale agent Information 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/commission_pricelist"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Sale agent Information (*commission_pricelist*)
===============================================
:Module: commission_pricelist
:Name: Sale agent Information
:Version: 5.0.0.1
:Author: Tiny
:Directory: commission_pricelist
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  Sale agent Info

Download links
--------------

You can download this module as a zip file in the following version:

(No download links available)


Dependencies
------------

 * :mod:`base`
 * :mod:`product`
 * :mod:`sale`

Reports
-------

 * Basic Info.

Menus
-------

 * Sales Management
 * Sales Management/Commissions/Sales agent
 * Sales Management/Reporting
 * Sales Management/Reporting/This Month
 * Sales Management/Reporting/This Month/Commissions of This Month
 * Sales Management/Reporting/All Commissions
 * Sales Management/Reporting/All Commissions/Commissions

Views
-----

 * saleagent.info.tree (tree)
 * saleagent.info.form (form)
 * \* INHERIT res.partner.form.inherit (form)
 * commission.month.form (form)
 * commission.month.form.tree (tree)
 * commission.all.form (form)
 * commission.all.form.tree (tree)


Objects
-------

Object: Sale agent sale info (sale.agent)
#########################################



:customer: Customer, one2many





:active: Active, boolean





:partner_id: Partner, many2one, required





:name: Saleagent Name, char, required





:comprice_id: commission price list, many2one, required




Object: Commission of month (report.commission.month)
#####################################################



:inv_total: Invoice Amount, float, readonly





:name: Sales Agent Name, char, readonly





:pdate: Invoice Paid Date, date, readonly





:productname: Product Name, char, readonly





:comrate: Commission Rate (%), float, readonly





:sono: Sales Order No, integer, readonly





:commission: Commissions Amount, float, readonly





:state: Invoice State, char, readonly





:invno: Invoice Number, integer, readonly





:product_quantity: Product Quantity, integer, readonly





:in_date: Invoice Date, date, readonly


