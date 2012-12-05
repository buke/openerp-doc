
.. i18n: .. module:: sale_payment
.. i18n:     :synopsis: Sale payment type 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: sale_payment
    :synopsis: Sale payment type 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/sale_payment"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/sale_payment"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Sale payment type (*sale_payment*)
.. i18n: ==================================
.. i18n: :Module: sale_payment
.. i18n: :Name: Sale payment type
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Zikzakmedia
.. i18n: :Directory: sale_payment
.. i18n: :Web: www.zikzakmedia.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

Sale payment type (*sale_payment*)
==================================
:Module: sale_payment
:Name: Sale payment type
:Version: 5.0.1.0
:Author: Zikzakmedia
:Directory: sale_payment
:Web: www.zikzakmedia.com
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Adds payment type and bank account to sale process.
.. i18n:   
.. i18n:   The sale order inherits payment type and bank account (if the payment type is related to bank accounts) from partner as default. Next, the invoice based on this sale order inherits the payment information from it.
.. i18n:   
.. i18n:   Also computes payment type and bank account of invoices created from picking lists (extracted from partner info).
.. i18n:   
.. i18n:   Based on previous work of Readylan (version for 4.2).
..

::

  Adds payment type and bank account to sale process.
  
  The sale order inherits payment type and bank account (if the payment type is related to bank accounts) from partner as default. Next, the invoice based on this sale order inherits the payment information from it.
  
  Also computes payment type and bank account of invoices created from picking lists (extracted from partner info).
  
  Based on previous work of Readylan (version for 4.2).

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/sale_payment.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/sale_payment.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/sale_payment.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/sale_payment.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`account_payment`
.. i18n:  * :mod:`account_payment_extension`
.. i18n:  * :mod:`sale`
.. i18n:  * :mod:`stock`
..

 * :mod:`account_payment`
 * :mod:`account_payment_extension`
 * :mod:`sale`
 * :mod:`stock`

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

.. i18n: None
..

None

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT sale.order.form.sale_paytype (form)
..

 * \* INHERIT sale.order.form.sale_paytype (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: None
..

None
