
.. i18n: .. module:: account_payment_export
.. i18n:     :synopsis: Payment Order Export 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: account_payment_export
    :synopsis: Payment Order Export 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_payment_export"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/account_payment_export"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Payment Order Export (*account_payment_export*)
.. i18n: ===============================================
.. i18n: :Module: account_payment_export
.. i18n: :Name: Payment Order Export
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: account_payment_export
.. i18n: :Web: 
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module allows to export payment orders.
..

::

  This module allows to export payment orders.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/account_payment_export.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/account_payment_export.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/account_payment_export.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/account_payment_export.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base_vat`
.. i18n:  * :mod:`base_iban`
.. i18n:  * :mod:`account_payment`
..

 * :mod:`base_vat`
 * :mod:`base_iban`
 * :mod:`account_payment`

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

.. i18n:  * Financial Management/Configuration/Payment Export
.. i18n:  * Financial Management/Configuration/Payment Export/Payment Export Logs
.. i18n:  * Financial Management/Configuration/Payment/Payment Method
.. i18n:  * Financial Management/Configuration/Payment/Charges Code
..

 * Financial Management/Configuration/Payment Export
 * Financial Management/Configuration/Payment Export/Payment Export Logs
 * Financial Management/Configuration/Payment/Payment Method
 * Financial Management/Configuration/Payment/Charges Code

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT res.partner.form.code.inherit (form)
.. i18n:  * \* INHERIT res.partner.bank.form.code.inherit (form)
.. i18n:  * account.pay.tree (tree)
.. i18n:  * account.pay.form (form)
.. i18n:  * \* INHERIT res.bank.form.inherit (form)
.. i18n:  * payment.method.tree (tree)
.. i18n:  * payment.method.form (form)
.. i18n:  * charges.code.tree (tree)
.. i18n:  * charges.code.form (form)
..

 * \* INHERIT res.partner.form.code.inherit (form)
 * \* INHERIT res.partner.bank.form.code.inherit (form)
 * account.pay.tree (tree)
 * account.pay.form (form)
 * \* INHERIT res.bank.form.inherit (form)
 * payment.method.tree (tree)
 * payment.method.form (form)
 * charges.code.tree (tree)
 * charges.code.form (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Payment Export History (account.pay)
.. i18n: ############################################
..

Object: Payment Export History (account.pay)
############################################

.. i18n: :create_uid: Creation User, many2one, required, readonly
..

:create_uid: Creation User, many2one, required, readonly

.. i18n: :create_date: Creation Date, datetime, required, readonly
..

:create_date: Creation Date, datetime, required, readonly

.. i18n: :note: Creation Log, text, readonly
..

:note: Creation Log, text, readonly

.. i18n: :payment_order_id: Payment Order Reference, many2one, readonly
..

:payment_order_id: Payment Order Reference, many2one, readonly

.. i18n: :state: Status, selection, readonly
..

:state: Status, selection, readonly

.. i18n: :file: Saved File, binary, readonly
..

:file: Saved File, binary, readonly

.. i18n: Object: Payment Method For Export (payment.method)
.. i18n: ##################################################
..

Object: Payment Method For Export (payment.method)
##################################################

.. i18n: :name: Code, char, required
..

:name: Code, char, required

.. i18n: :description: Description, text
..

:description: Description, text

.. i18n: Object: Charges Codes For Export (charges.code)
.. i18n: ###############################################
..

Object: Charges Codes For Export (charges.code)
###############################################

.. i18n: :name: Code, char, required
..

:name: Code, char, required

.. i18n: :description: Description, text
..

:description: Description, text
