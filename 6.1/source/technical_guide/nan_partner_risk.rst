
.. i18n: .. module:: nan_partner_risk
.. i18n:     :synopsis: Partner Risk Analysis 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: nan_partner_risk
    :synopsis: Partner Risk Analysis 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/nan_partner_risk"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/nan_partner_risk"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Partner Risk Analysis (*nan_partner_risk*)
.. i18n: ==========================================
.. i18n: :Module: nan_partner_risk
.. i18n: :Name: Partner Risk Analysis
.. i18n: :Version: 5.0.0.1
.. i18n: :Author: NaN for Trod y Avia, S.L.
.. i18n: :Directory: nan_partner_risk
.. i18n: :Web: http://www.NaN-tic.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module adds a new button in the partner form to analyze current state of a partner risk.
.. i18n:   It reports current information regarding amount of debt in invoices, orders, etc.
.. i18n:   
.. i18n:   It also modifies the workflow of sale orders by adding a new step when partner's risk is exceeded.
..

::

  This module adds a new button in the partner form to analyze current state of a partner risk.
  It reports current information regarding amount of debt in invoices, orders, etc.
  
  It also modifies the workflow of sale orders by adding a new step when partner's risk is exceeded.

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
.. i18n:  * :mod:`account`
.. i18n:  * :mod:`sale`
.. i18n:  * :mod:`account_payment`
..

 * :mod:`base`
 * :mod:`account`
 * :mod:`sale`
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

.. i18n:  * Sales Management/Sales Orders/Waiting Risk Approval
..

 * Sales Management/Sales Orders/Waiting Risk Approval

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT res.partner.form.risk (form)
.. i18n:  * \* INHERIT sale.order.form.risk (form)
..

 * \* INHERIT res.partner.form.risk (form)
 * \* INHERIT sale.order.form.risk (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: None
..

None
