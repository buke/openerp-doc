
.. i18n: .. module:: fleet_maintenance
.. i18n:     :synopsis: Help managing maintenance contracts related to product fleet 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: fleet_maintenance
    :synopsis: Help managing maintenance contracts related to product fleet 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/fleet_maintenance"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/fleet_maintenance"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Help managing maintenance contracts related to product fleet (*fleet_maintenance*)
.. i18n: ==================================================================================
.. i18n: :Module: fleet_maintenance
.. i18n: :Name: Help managing maintenance contracts related to product fleet
.. i18n: :Version: 5.0.0.3
.. i18n: :Author: Smile for Anevia (Anevia.com)
.. i18n: :Directory: fleet_maintenance
.. i18n: :Web: http://www.smile.fr
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Manage the maintenance contracts of a product fleet (streaming servers originally).
.. i18n:   
.. i18n:   Now partners have fleets and sub-fleets for which they can buy products that can eventually
.. i18n:   be covered by paid maintenance contracts.
.. i18n:   
.. i18n:   Fleet: a stock.location for which all products have the same maintenance end date anniversary.
.. i18n:   Indeed, it's useful to have several maintenance contracts for a given partner with a single anniversary date
.. i18n:   for an eventual renewal.
.. i18n:   Meaning that if the customer wants a different end date anniversaries for two maintenance contracts,
.. i18n:   then he should have several Fleets.
.. i18n:   Products don't go in the Fleets actually, they go in their Sub-Fleets instead.
.. i18n:   
.. i18n:   Sub-Fleet: a stock.location child of a Fleet which might contains some purchased products.
.. i18n:   In a sub-fleet, ALL the maintenance contracts of the products have exactly the same start date and end date.
.. i18n:   Meaning that if a customer need several different start date or some years offset for the end date,
.. i18n:   then he should have several Sub-Fleets.
.. i18n:   
.. i18n:   This module also take care of proposing ideal maintenance dates given a few rules that might
.. i18n:   be changed in your specific case (Ideally they wouldn't be hardcoded or at least have some
.. i18n:   parameters externalized to the database).
.. i18n:   
.. i18n:   Finally, this module also takes care of after sale incidents, extending the native CRM and thus
.. i18n:   preserving all the CRM power.
.. i18n:   Given a product serial number (prodlot), it's able to retrieve the Fleet and Partner and know if a product is still covered
.. i18n:   by a maintenance contract or not. It also deals with reparation movements in a simple manner, that
.. i18n:   might later on made compatible with the mrp_repair module which was too complex for our first use here. 
.. i18n:   
.. i18n:   This module is also fully compliant with the native prodlot tracking of OpenERP to know
.. i18n:   where is a serial number, be it a finished product or only a part, and even after a replacement
.. i18n:   if movements are properly entered in the crm incident. For a better tracking experience, it's
.. i18n:   advised to use it along with the mrp_prodlot_autosplit module.
..

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

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/fleet_maintenance.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/fleet_maintenance.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/fleet_maintenance.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/fleet_maintenance.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`product`
.. i18n:  * :mod:`stock`
.. i18n:  * :mod:`sale`
.. i18n:  * :mod:`crm_configuration`
.. i18n:  * :mod:`account`
.. i18n:  * :mod:`delivery`
..

 * :mod:`base`
 * :mod:`product`
 * :mod:`stock`
 * :mod:`sale`
 * :mod:`crm_configuration`
 * :mod:`account`
 * :mod:`delivery`

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

.. i18n:  * Fleets
.. i18n:  * Fleets/Fleet Maintenance Contracts
.. i18n:  * Fleets/Fleets
.. i18n:  * Fleets/Fleet Extensions
.. i18n:  * Fleets/Production Lots
.. i18n:  * Fleets/Fleets/All Fleets
.. i18n:  * Fleets/Fleets/New Fleet
.. i18n:  * Fleets/Fleet Extensions/All Sub Fleets
.. i18n:  * Fleets/Fleet Extensions/New Fleet Extension
.. i18n:  * Fleets/Fleet Maintenance Contracts/All Maintenance Orders
.. i18n:  * Fleets/Fleet Maintenance Contracts/New Maintenance quotation
.. i18n:  * Fleets/Fleet Incidents
.. i18n:  * Fleets/Fleet Incidents/All Fleet Incidents
.. i18n:  * Fleets/Fleet Incidents/New Fleet Incident
..

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

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT product.form.fleet_maintenance.inherit (form)
.. i18n:  * \* INHERIT product.form.fleet_maintenance.inherit2 (form)
.. i18n:  * \* INHERIT product.form.fleet_maintenance.inherit3 (form)
.. i18n:  * \* INHERIT sale.order.form.fleet_maintenance.inherit (form)
.. i18n:  * \* INHERIT sale.order.form.fleet_maintenance2.inherit (form)
.. i18n:  * \* INHERIT sale.order.form.fleet_maintenance3.inherit (form)
.. i18n:  * \* INHERIT sale.order.form.fleet_maintenance4.inherit (form)
.. i18n:  * \* INHERIT sale.order.form.fleet_maintenance5.inherit (form)
.. i18n:  * \* INHERIT account.invoice.line.form.fleet_maintenace.inherit (form)
.. i18n:  * \* INHERIT account.invoice.line.tree.fleet_maintenace.inherit (tree)
.. i18n:  * account.invoice.line.calendar.fleet_maintenace.inherit (calendar)
.. i18n:  * stock.location.fleet.form.fleet_maintenance (form)
.. i18n:  * stock.location.fleet.form.sub_fleet_maintenance (form)
.. i18n:  * fleet_maintenance.tree (tree)
.. i18n:  * sub_fleet.tree (tree)
.. i18n:  * \* INHERIT stock.location.tree (tree)
.. i18n:  * stock.picking.incident.form (form)
.. i18n:  * \* INHERIT res.partner.form.fleet_maintenance.inherit (form)
.. i18n:  * \* INHERIT account.analytic.line.fleet_form (form)
.. i18n:  * crm.case.form.fleet_maintenance (form)
.. i18n:  * crm.case.tree.fleet_maintenance (tree)
..

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

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: None
..

None
