
.. module:: nan_partner_risk
    :synopsis: Partner Risk Analysis 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/nan_partner_risk"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Partner Risk Analysis (*nan_partner_risk*)
==========================================
:Module: nan_partner_risk
:Name: Partner Risk Analysis
:Version: 5.0.0.1
:Author: NaN for Trod y Avia, S.L.
:Directory: nan_partner_risk
:Web: http://www.NaN-tic.com
:Official module: no
:Quality certified: no

Description
-----------

::

  This module adds a new button in the partner form to analyze current state of a partner risk.
  It reports current information regarding amount of debt in invoices, orders, etc.
  
  It also modifies the workflow of sale orders by adding a new step when partner's risk is exceeded.

Download links
--------------

You can download this module as a zip file in the following version:

(No download links available)


Dependencies
------------

 * :mod:`base`
 * :mod:`account`
 * :mod:`sale`
 * :mod:`account_payment`

Reports
-------

None


Menus
-------

 * Sales Management/Sales Orders/Waiting Risk Approval

Views
-----

 * \* INHERIT res.partner.form.risk (form)
 * \* INHERIT sale.order.form.risk (form)


Objects
-------

None
