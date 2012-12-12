
.. module:: fleet_maintenance
    :synopsis: Help managing maintenance contracts related to product fleet 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/fleet_maintenance"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Help managing maintenance contracts related to product fleet (*fleet_maintenance*)
==================================================================================
:Module: fleet_maintenance
:Name: Help managing maintenance contracts related to product fleet
:Version: 5.0.0.3
:Author: Smile for Anevia (Anevia.com)
:Directory: fleet_maintenance
:Web: http://www.smile.fr
:Official module: no
:Quality certified: no

Description
-----------

::

  Manage the maintenance contracts of a product fleet (streaming servers originally).
  
  Now partners have fleets and sub-fleets for which they can buy products that can eventually
  be covered by paid maintenance contracts.
  
  Fleet: a stock.location for which all products have the same maintenance end date anniversary.
  Indeed, it's useful to have several maintenance contracts for a given partner with a single anniversary date
  for an eventual renewal.
  Meaning that if the customer wants a different end date anniversaries for two maintenance contracts,
  then he should have several Fleets.
  Products don't go in the Fleets actually, they go in their Sub-Fleets instead.
  
  Sub-Fleet: a stock.location child of a Fleet which might contains some purchased products.
  In a sub-fleet, ALL the maintenance contracts of the products have exactly the same start date and end date.
  Meaning that if a customer need several different start date or some years offset for the end date,
  then he should have several Sub-Fleets.
  
  This module also take care of proposing ideal maintenance dates given a few rules that might
  be changed in your specific case (Ideally they wouldn't be hardcoded or at least have some
  parameters externalized to the database).
  
  Finally, this module also takes care of after sale incidents, extending the native CRM and thus
  preserving all the CRM power.
  Given a product serial number (prodlot), it's able to retrieve the Fleet and Partner and know if a product is still covered
  by a maintenance contract or not. It also deals with reparation movements in a simple manner, that
  might later on made compatible with the mrp_repair module which was too complex for our first use here. 
  
  This module is also fully compliant with the native prodlot tracking of OpenERP to know
  where is a serial number, be it a finished product or only a part, and even after a replacement
  if movements are properly entered in the crm incident. For a better tracking experience, it's
  advised to use it along with the mrp_prodlot_autosplit module.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/fleet_maintenance.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/fleet_maintenance.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`product`
 * :mod:`stock`
 * :mod:`sale`
 * :mod:`crm_configuration`
 * :mod:`account`
 * :mod:`delivery`

Reports
-------

None


Menus
-------

 * Fleets
 * Fleets/Fleet Maintenance Contracts
 * Fleets/Fleets
 * Fleets/Fleet Extensions
 * Fleets/Production Lots
 * Fleets/Fleets/All Fleets
 * Fleets/Fleets/New Fleet
 * Fleets/Fleet Extensions/All Sub Fleets
 * Fleets/Fleet Extensions/New Fleet Extension
 * Fleets/Fleet Maintenance Contracts/All Maintenance Orders
 * Fleets/Fleet Maintenance Contracts/New Maintenance quotation
 * Fleets/Fleet Incidents
 * Fleets/Fleet Incidents/All Fleet Incidents
 * Fleets/Fleet Incidents/New Fleet Incident

Views
-----

 * \* INHERIT product.form.fleet_maintenance.inherit (form)
 * \* INHERIT product.form.fleet_maintenance.inherit2 (form)
 * \* INHERIT product.form.fleet_maintenance.inherit3 (form)
 * \* INHERIT sale.order.form.fleet_maintenance.inherit (form)
 * \* INHERIT sale.order.form.fleet_maintenance2.inherit (form)
 * \* INHERIT sale.order.form.fleet_maintenance3.inherit (form)
 * \* INHERIT sale.order.form.fleet_maintenance4.inherit (form)
 * \* INHERIT sale.order.form.fleet_maintenance5.inherit (form)
 * \* INHERIT account.invoice.line.form.fleet_maintenace.inherit (form)
 * \* INHERIT account.invoice.line.tree.fleet_maintenace.inherit (tree)
 * account.invoice.line.calendar.fleet_maintenace.inherit (calendar)
 * stock.location.fleet.form.fleet_maintenance (form)
 * stock.location.fleet.form.sub_fleet_maintenance (form)
 * fleet_maintenance.tree (tree)
 * sub_fleet.tree (tree)
 * \* INHERIT stock.location.tree (tree)
 * stock.picking.incident.form (form)
 * \* INHERIT res.partner.form.fleet_maintenance.inherit (form)
 * \* INHERIT account.analytic.line.fleet_form (form)
 * crm.case.form.fleet_maintenance (form)
 * crm.case.tree.fleet_maintenance (tree)


Objects
-------

None
