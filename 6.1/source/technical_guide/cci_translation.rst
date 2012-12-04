
.. module:: cci_translation
    :synopsis: CCI Translation 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/cci_translation"></div>
    <script src="http://js-kit.com/ratings.js"></script>

CCI Translation (*cci_translation*)
===================================
:Module: cci_translation
:Name: CCI Translation
:Version: 5.0.1.0
:Author: Tiny
:Directory: cci_translation
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  cci translation

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/cci_translation.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/cci_translation.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`cci_account`

Reports
-------

None


Menus
-------

 * Translation
 * Translation/Translation Dossier
 * Translation/Credit Line
 * Translation/Letter of Credence

Views
-----

 * translation.folder.form (form)
 * translation.folder.tree (tree)
 * credit.line.form (form)
 * credit.line.tree (tree)
 * letter.credence.form (form)
 * letter.credence.tree (tree)
 * \* INHERIT res.partner.form.translation (form)


Objects
-------

Object: Credit line (credit.line)
#################################



:from_date: From Date, date, required





:customer_credit: Customer Max Credit, float, required





:to_date: To Date, date, required





:name: Name, char, required





:global_credit: Global Credit, float, required




Object: Translation Folder (translation.folder)
###############################################



:awex_amount: AWEX Amount, float, readonly





:credit_line_id: Credit Line, many2one, readonly





:name: Name, text, required





:invoice_id: Invoice, many2one





:order_desc: Description, char, required





:base_amount: Base Amount, float, required, readonly





:purchase_order: Purchase Order, many2one





:awex_eligible: AWEX Eligible, boolean, readonly





:state: State, selection, readonly





:order_date: Order Date, date, required





:partner_id: Partner, many2one, required




Object: Letter of Credence (letter.credence)
############################################



:emission_date: Emission Date, date, required





:asked_amount: Asked Amount, float, required


