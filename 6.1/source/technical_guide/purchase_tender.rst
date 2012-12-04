
.. module:: purchase_tender
    :synopsis: Purchase - Purchase Tender 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/purchase_tender"></div>
    <script src="http://js-kit.com/ratings.js"></script>

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

Description
-----------

::

  This module allows you to manage your Purchase Tenders. When a purchase order is created, you now have the opportunity to save the related tender. 
      This new object will regroup and will allow you to easily keep track and order all your purchase orders.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/purchase_tender.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/purchase_tender.zip>`_


Dependencies
------------

 * :mod:`purchase`

Reports
-------

None


Menus
-------

 * Purchase Management/Purchase Tenders
 * Purchase Management/Purchase Tenders/Purchase Tenders
 * Purchase Management/Purchase Tenders/Purchase Tenders/Draft Purchase Tenders
 * Purchase Management/Purchase Tenders/Purchase Tenders/Open Purchase Tenders
 * Purchase Management/Purchase Tenders/New Purchase Tenders

Views
-----

 * \* INHERIT purchase.order.tree.inherit (tree)
 * \* INHERIT purchase.order.form.inherit (form)
 * purchase.tender.form (form)
 * purchase.tender.tree (tree)


Objects
-------

Object: Purchase Tender (purchase.tender)
#########################################



:user_id: Responsible, many2one





:name: Tender Reference, char, required





:date_end: Date End, datetime





:date_start: Date Start, datetime





:state: State, selection, required





:purchase_ids: Purchase Orders, one2many





:description: Description, text


