
.. i18n: .. module:: cci_translation
.. i18n:     :synopsis: CCI Translation 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: cci_translation
    :synopsis: CCI Translation 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/cci_translation"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/cci_translation"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: CCI Translation (*cci_translation*)
.. i18n: ===================================
.. i18n: :Module: cci_translation
.. i18n: :Name: CCI Translation
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: cci_translation
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   cci translation
..

::

  cci translation

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/cci_translation.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/cci_translation.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/cci_translation.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/cci_translation.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`cci_account`
..

 * :mod:`base`
 * :mod:`cci_account`

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

.. i18n:  * Translation
.. i18n:  * Translation/Translation Dossier
.. i18n:  * Translation/Credit Line
.. i18n:  * Translation/Letter of Credence
..

 * Translation
 * Translation/Translation Dossier
 * Translation/Credit Line
 * Translation/Letter of Credence

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * translation.folder.form (form)
.. i18n:  * translation.folder.tree (tree)
.. i18n:  * credit.line.form (form)
.. i18n:  * credit.line.tree (tree)
.. i18n:  * letter.credence.form (form)
.. i18n:  * letter.credence.tree (tree)
.. i18n:  * \* INHERIT res.partner.form.translation (form)
..

 * translation.folder.form (form)
 * translation.folder.tree (tree)
 * credit.line.form (form)
 * credit.line.tree (tree)
 * letter.credence.form (form)
 * letter.credence.tree (tree)
 * \* INHERIT res.partner.form.translation (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Credit line (credit.line)
.. i18n: #################################
..

Object: Credit line (credit.line)
#################################

.. i18n: :from_date: From Date, date, required
..

:from_date: From Date, date, required

.. i18n: :customer_credit: Customer Max Credit, float, required
..

:customer_credit: Customer Max Credit, float, required

.. i18n: :to_date: To Date, date, required
..

:to_date: To Date, date, required

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :global_credit: Global Credit, float, required
..

:global_credit: Global Credit, float, required

.. i18n: Object: Translation Folder (translation.folder)
.. i18n: ###############################################
..

Object: Translation Folder (translation.folder)
###############################################

.. i18n: :awex_amount: AWEX Amount, float, readonly
..

:awex_amount: AWEX Amount, float, readonly

.. i18n: :credit_line_id: Credit Line, many2one, readonly
..

:credit_line_id: Credit Line, many2one, readonly

.. i18n: :name: Name, text, required
..

:name: Name, text, required

.. i18n: :invoice_id: Invoice, many2one
..

:invoice_id: Invoice, many2one

.. i18n: :order_desc: Description, char, required
..

:order_desc: Description, char, required

.. i18n: :base_amount: Base Amount, float, required, readonly
..

:base_amount: Base Amount, float, required, readonly

.. i18n: :purchase_order: Purchase Order, many2one
..

:purchase_order: Purchase Order, many2one

.. i18n: :awex_eligible: AWEX Eligible, boolean, readonly
..

:awex_eligible: AWEX Eligible, boolean, readonly

.. i18n: :state: State, selection, readonly
..

:state: State, selection, readonly

.. i18n: :order_date: Order Date, date, required
..

:order_date: Order Date, date, required

.. i18n: :partner_id: Partner, many2one, required
..

:partner_id: Partner, many2one, required

.. i18n: Object: Letter of Credence (letter.credence)
.. i18n: ############################################
..

Object: Letter of Credence (letter.credence)
############################################

.. i18n: :emission_date: Emission Date, date, required
..

:emission_date: Emission Date, date, required

.. i18n: :asked_amount: Asked Amount, float, required
..

:asked_amount: Asked Amount, float, required
