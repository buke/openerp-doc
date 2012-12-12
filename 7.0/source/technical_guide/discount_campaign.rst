
.. module:: discount_campaign
    :synopsis: Discount on Marketing Campaigns 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/discount_campaign"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Discount on Marketing Campaigns (*discount_campaign*)
=====================================================
:Module: discount_campaign
:Name: Discount on Marketing Campaigns
:Version: 5.0.1.0
:Author: Tiny
:Directory: discount_campaign
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Marketing management module

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/discount_campaign.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/discount_campaign.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/discount_campaign.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`sale`

Reports
-------

None


Menus
-------

 * Sales Management/Configuration/Discount Campaign

Views
-----

 * \* INHERIT discountcampaign.sale.order.form.view (form)
 * \* INHERIT discount.campaign.partner.form.view (form)
 * discount.campaign.form (form)
 * discount.campaign.tree (tree)
 * discount.campaign.line.form (form)
 * discount.campaign.line.tree (tree)


Objects
-------

Object: discount.campaign (discount.campaign)
#############################################



:line_ids: Discount Lines, one2many





:date_stop: Stop Date, date, required





:date_start: Start Date, date, required





:name: Name, char





:state: State, selection, readonly




Object: discount.campaign.line (discount.campaign.line)
#######################################################



:condition_sale: Sale Condition, char





:name: Name, char





:sequence: Sequence, integer, required





:discount_id: Discount Lines, many2one





:discount: Discount, float





:condition_category_id: Category, many2one





:condition_quantity: Min. Quantity, float





:condition_product_id: Product, many2one


