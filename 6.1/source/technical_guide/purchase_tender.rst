
.. i18n: .. module:: purchase_tender
.. i18n:     :synopsis: Purchase - Purchase Tender 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: purchase_tender
    :synopsis: Purchase - Purchase Tender 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/purchase_tender"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/purchase_tender"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Purchase - Purchase Tender (*purchase_tender*)
.. i18n: ==============================================
.. i18n: :Module: purchase_tender
.. i18n: :Name: Purchase - Purchase Tender
.. i18n: :Version: 5.0.0.1
.. i18n: :Author: Tiny
.. i18n: :Directory: purchase_tender
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

Purchase - Purchase Tender (*purchase_tender*)
==============================================
:Module: purchase_tender
:Name: Purchase - Purchase Tender
:Version: 5.0.0.1
:Author: Tiny
:Directory: purchase_tender
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
.. i18n:   This module allows you to manage your Purchase Tenders. When a purchase order is created, you now have the opportunity to save the related tender. 
.. i18n:       This new object will regroup and will allow you to easily keep track and order all your purchase orders.
..

::

  This module allows you to manage your Purchase Tenders. When a purchase order is created, you now have the opportunity to save the related tender. 
      This new object will regroup and will allow you to easily keep track and order all your purchase orders.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/purchase_tender.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/purchase_tender.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/purchase_tender.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/purchase_tender.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`purchase`
..

 * :mod:`purchase`

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

.. i18n:  * Purchase Management/Purchase Tenders
.. i18n:  * Purchase Management/Purchase Tenders/Purchase Tenders
.. i18n:  * Purchase Management/Purchase Tenders/Purchase Tenders/Draft Purchase Tenders
.. i18n:  * Purchase Management/Purchase Tenders/Purchase Tenders/Open Purchase Tenders
.. i18n:  * Purchase Management/Purchase Tenders/New Purchase Tenders
..

 * Purchase Management/Purchase Tenders
 * Purchase Management/Purchase Tenders/Purchase Tenders
 * Purchase Management/Purchase Tenders/Purchase Tenders/Draft Purchase Tenders
 * Purchase Management/Purchase Tenders/Purchase Tenders/Open Purchase Tenders
 * Purchase Management/Purchase Tenders/New Purchase Tenders

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT purchase.order.tree.inherit (tree)
.. i18n:  * \* INHERIT purchase.order.form.inherit (form)
.. i18n:  * purchase.tender.form (form)
.. i18n:  * purchase.tender.tree (tree)
..

 * \* INHERIT purchase.order.tree.inherit (tree)
 * \* INHERIT purchase.order.form.inherit (form)
 * purchase.tender.form (form)
 * purchase.tender.tree (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Purchase Tender (purchase.tender)
.. i18n: #########################################
..

Object: Purchase Tender (purchase.tender)
#########################################

.. i18n: :user_id: Responsible, many2one
..

:user_id: Responsible, many2one

.. i18n: :name: Tender Reference, char, required
..

:name: Tender Reference, char, required

.. i18n: :date_end: Date End, datetime
..

:date_end: Date End, datetime

.. i18n: :date_start: Date Start, datetime
..

:date_start: Date Start, datetime

.. i18n: :state: State, selection, required
..

:state: State, selection, required

.. i18n: :purchase_ids: Purchase Orders, one2many
..

:purchase_ids: Purchase Orders, one2many

.. i18n: :description: Description, text
..

:description: Description, text
