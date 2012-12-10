
.. i18n: .. module:: commission_pricelist
.. i18n:     :synopsis: Sale agent Information 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: commission_pricelist
    :synopsis: Sale agent Information 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/commission_pricelist"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/commission_pricelist"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Sale agent Information (*commission_pricelist*)
.. i18n: ===============================================
.. i18n: :Module: commission_pricelist
.. i18n: :Name: Sale agent Information
.. i18n: :Version: 5.0.0.1
.. i18n: :Author: Tiny
.. i18n: :Directory: commission_pricelist
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Sale agent Info
..

::

  Sale agent Info

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n: (No download links available)
..

(No download links available)

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`product`
.. i18n:  * :mod:`sale`
..

 * :mod:`base`
 * :mod:`product`
 * :mod:`sale`

.. i18n: Reports
.. i18n: -------
..

Reports
-------

.. i18n:  * Basic Info.
..

 * Basic Info.

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Sales Management
.. i18n:  * Sales Management/Commissions/Sales agent
.. i18n:  * Sales Management/Reporting
.. i18n:  * Sales Management/Reporting/This Month
.. i18n:  * Sales Management/Reporting/This Month/Commissions of This Month
.. i18n:  * Sales Management/Reporting/All Commissions
.. i18n:  * Sales Management/Reporting/All Commissions/Commissions
..

 * Sales Management
 * Sales Management/Commissions/Sales agent
 * Sales Management/Reporting
 * Sales Management/Reporting/This Month
 * Sales Management/Reporting/This Month/Commissions of This Month
 * Sales Management/Reporting/All Commissions
 * Sales Management/Reporting/All Commissions/Commissions

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * saleagent.info.tree (tree)
.. i18n:  * saleagent.info.form (form)
.. i18n:  * \* INHERIT res.partner.form.inherit (form)
.. i18n:  * commission.month.form (form)
.. i18n:  * commission.month.form.tree (tree)
.. i18n:  * commission.all.form (form)
.. i18n:  * commission.all.form.tree (tree)
..

 * saleagent.info.tree (tree)
 * saleagent.info.form (form)
 * \* INHERIT res.partner.form.inherit (form)
 * commission.month.form (form)
 * commission.month.form.tree (tree)
 * commission.all.form (form)
 * commission.all.form.tree (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Sale agent sale info (sale.agent)
.. i18n: #########################################
..

Object: Sale agent sale info (sale.agent)
#########################################

.. i18n: :customer: Customer, one2many
..

:customer: Customer, one2many

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :partner_id: Partner, many2one, required
..

:partner_id: Partner, many2one, required

.. i18n: :name: Saleagent Name, char, required
..

:name: Saleagent Name, char, required

.. i18n: :comprice_id: commission price list, many2one, required
..

:comprice_id: commission price list, many2one, required

.. i18n: Object: Commission of month (report.commission.month)
.. i18n: #####################################################
..

Object: Commission of month (report.commission.month)
#####################################################

.. i18n: :inv_total: Invoice Amount, float, readonly
..

:inv_total: Invoice Amount, float, readonly

.. i18n: :name: Sales Agent Name, char, readonly
..

:name: Sales Agent Name, char, readonly

.. i18n: :pdate: Invoice Paid Date, date, readonly
..

:pdate: Invoice Paid Date, date, readonly

.. i18n: :productname: Product Name, char, readonly
..

:productname: Product Name, char, readonly

.. i18n: :comrate: Commission Rate (%), float, readonly
..

:comrate: Commission Rate (%), float, readonly

.. i18n: :sono: Sales Order No, integer, readonly
..

:sono: Sales Order No, integer, readonly

.. i18n: :commission: Commissions Amount, float, readonly
..

:commission: Commissions Amount, float, readonly

.. i18n: :state: Invoice State, char, readonly
..

:state: Invoice State, char, readonly

.. i18n: :invno: Invoice Number, integer, readonly
..

:invno: Invoice Number, integer, readonly

.. i18n: :product_quantity: Product Quantity, integer, readonly
..

:product_quantity: Product Quantity, integer, readonly

.. i18n: :in_date: Invoice Date, date, readonly
..

:in_date: Invoice Date, date, readonly
