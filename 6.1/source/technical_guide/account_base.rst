
.. module:: account_base
    :synopsis: Accounting Base Properties 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_base"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Accounting Base Properties (*account_base*)
===========================================
:Module: account_base
:Name: Accounting Base Properties
:Version: 5.0.1.0
:Author: Tiny & Axelor
:Directory: account_base
:Web: http://tinyerpindia.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Accounting Base Properties is providing the,
      Basic properties for the Customer / Suppliers for the Accounting
      i.e. PAN No, TIN No, Sales Tax No, and Exise related Information

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/account_base.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/account_base.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`account`

Reports
-------

None


Menus
-------


None


Views
-----

 * \* INHERIT account_base.partner.form (form)
 * wizard.account.base.setup.form (form)


Objects
-------

Object: wizard.account.base.setup (wizard.account.base.setup)
#############################################################



:pan_no: PAN Number, char





:excise: Exices Number, char





:vat_no: VAT Number, char





:company_id: Company, many2one, required





:range: Range, char





:ser_tax: Service Tax Number, char





:div: Division, char





:partner_id: Partner, many2one





:cst_no: CST Number, char


