
.. module:: account_analytic_package
    :synopsis: Account Analytic Package - To configure Analytic Account for product packages 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_analytic_package"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Account Analytic Package - To configure Analytic Account for product packages (*account_analytic_package*)
==========================================================================================================
:Module: account_analytic_package
:Name: Account Analytic Package - To configure Analytic Account for product packages
:Version: 5.0.1.0
:Author: Tiny
:Directory: account_analytic_package
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  The Module allows to configure analytic account for product packages.
      Views for total and monthly product packages weight, Amount analysis.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/account_analytic_package.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/account_analytic_package.zip>`_


Dependencies
------------

 * :mod:`account`
 * :mod:`product`
 * :mod:`crm`

Reports
-------

None


Menus
-------

 * Financial Management/Reporting/Packages
 * Financial Management/Reporting/Packages/Service & Activity Units
 * Financial Management/Reporting/Packages/Service & Activity Units/Service Units
 * Financial Management/Reporting/Packages/Service & Activity Units/Activity Units
 * Financial Management/Reporting/Packages/Monthly Services & Activity Units
 * Financial Management/Reporting/Packages/Products Units

Views
-----

 * \* INHERIT account.analytic.account.package.form (form)
 * \* INHERIT crm.case.section.package.form (form)
 * \* INHERIT product.normal.package.form (form)
 * account.analytic.line.package.simplified.tree (tree)
 * account.analytic.line.package.form (form)
 * account.analytic.line.package.tree (tree)
 * account.analytic.line.package.month.graph (graph)
 * account.analytic.line.package.month.form (form)
 * account.analytic.line.package.month.tree (tree)
 * Products List (tree)


Objects
-------

Object: account.analytic.line.package (account.analytic.line.package)
#####################################################################



:account_id: Account, many2one, readonly





:unit_weight: Unit Weight, float, readonly





:name: Name, char, readonly





:total_weight: Total Weight, float, readonly





:unit_amount: Quantity, float, readonly





:date: Date, date, readonly





:partner_id: Partner, many2one, readonly





:product_id: Product, many2one, readonly




Object: account.analytic.line.package.month (account.analytic.line.package.month)
#################################################################################



:product_id: Product, many2one, readonly





:total_service: Total Service, float, readonly





:total_activity: Total Activity, float, readonly





:total_weight: Total Weight, float, readonly





:partner_id: Partner, many2one, readonly





:name: Date, date, readonly


