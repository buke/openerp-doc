
.. module:: account_payment_export
    :synopsis: Payment Order Export 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_payment_export"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Payment Order Export (*account_payment_export*)
===============================================
:Module: account_payment_export
:Name: Payment Order Export
:Version: 5.0.1.0
:Author: Tiny
:Directory: account_payment_export
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  This module allows to export payment orders.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/account_payment_export.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/account_payment_export.zip>`_


Dependencies
------------

 * :mod:`base_vat`
 * :mod:`base_iban`
 * :mod:`account_payment`

Reports
-------

None


Menus
-------

 * Financial Management/Configuration/Payment Export
 * Financial Management/Configuration/Payment Export/Payment Export Logs
 * Financial Management/Configuration/Payment/Payment Method
 * Financial Management/Configuration/Payment/Charges Code

Views
-----

 * \* INHERIT res.partner.form.code.inherit (form)
 * \* INHERIT res.partner.bank.form.code.inherit (form)
 * account.pay.tree (tree)
 * account.pay.form (form)
 * \* INHERIT res.bank.form.inherit (form)
 * payment.method.tree (tree)
 * payment.method.form (form)
 * charges.code.tree (tree)
 * charges.code.form (form)


Objects
-------

Object: Payment Export History (account.pay)
############################################



:create_uid: Creation User, many2one, required, readonly





:create_date: Creation Date, datetime, required, readonly





:note: Creation Log, text, readonly





:payment_order_id: Payment Order Reference, many2one, readonly





:state: Status, selection, readonly





:file: Saved File, binary, readonly




Object: Payment Method For Export (payment.method)
##################################################



:name: Code, char, required





:description: Description, text




Object: Charges Codes For Export (charges.code)
###############################################



:name: Code, char, required





:description: Description, text


