.. i18n: .. index::
.. i18n:    single: Sales Management
..

.. index::
   single: Sales Management

.. i18n: .. _ch-sales:
.. i18n: 
.. i18n: ******************
.. i18n: Driving your Sales
.. i18n: ******************
..

.. _ch-sales:

******************
为你的销售提供助力
******************

.. i18n:   *This chapter describes OpenERP's sales management, following the complete sales order process from
.. i18n:   quotation to customer order, including the management of deliveries and invoicing. 
.. i18n:   It does not look at customer relations and pre-sales, which are handled by the CRM
.. i18n:   (Customer Relationship Management) modules described in an earlier part of the book.*
.. i18n:   
.. i18n:   *It also describes the management of carriers, margin control and reporting,
.. i18n:   price management and the handling of various types of sales discount campaigns.*
.. i18n:   
.. i18n: For this chapter you should start with a fresh database that includes demonstration data,
.. i18n: with :mod:`sale` and its dependencies installed and no particular chart of accounts configured. 
..

  *这一章主要讲述Openerp的销售管理，包括从报价到客户订单的销售订单处理过程，以及发货管理及发票。 
  这一章并不包含客户关系及售前管理，这两个功能呢个由CRM（客户关系管理）模块处理，在本书的早期章节中已经有所描述。*
  
  *It also describes the management of carriers, margin control and reporting,
  price management and the handling of various types of sales discount campaigns.*
  
For this chapter you should start with a fresh database that includes demonstration data,
with :mod:`sale` and its dependencies installed and no particular chart of accounts configured. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <div class="all-toctree">
..

.. raw:: html

    <div class="all-toctree">

.. i18n: .. toctree::
.. i18n: 
.. i18n:     6_16_Sales_quotations
.. i18n:     6_16_Sales_packing
.. i18n:     6_16_Sales_alerts
.. i18n:     6_16_Sales_control
.. i18n:     6_16_Sales_carriers
.. i18n:     6_16_Sales_margins
.. i18n:     6_16_Sales_pricing
.. i18n:     6_16_Sales_rebates
.. i18n:     6_16_Sales_open
.. i18n:     6_16_Sales_layout
..

.. toctree::

    6_16_Sales_quotations
    6_16_Sales_packing
    6_16_Sales_alerts
    6_16_Sales_control
    6_16_Sales_carriers
    6_16_Sales_margins
    6_16_Sales_pricing
    6_16_Sales_rebates
    6_16_Sales_open
    6_16_Sales_layout

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     </div>
..

.. raw:: html

    </div>

.. i18n: .. Copyright © Open Object Press. All rights reserved.
..

.. Copyright © Open Object Press. All rights reserved.

.. i18n: .. You may take electronic copy of this publication and distribute it if you don't
.. i18n: .. change the content. You can also print a copy to be read by yourself only.
..

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. i18n: .. We have contracts with different publishers in different countries to sell and
.. i18n: .. distribute paper or electronic based versions of this book (translated or not)
.. i18n: .. in bookstores. This helps to distribute and promote the OpenERP product. It
.. i18n: .. also helps us to create incentives to pay contributors and authors using author
.. i18n: .. rights of these sales.
..

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the OpenERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. i18n: .. Due to this, grants to translate, modify or sell this book are strictly
.. i18n: .. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. i18n: .. written authorisation for this.
..

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. i18n: .. Many of the designations used by manufacturers and suppliers to distinguish their
.. i18n: .. products are claimed as trademarks. Where those designations appear in this book,
.. i18n: .. and Open Object Press was aware of a trademark claim, the designations have been
.. i18n: .. printed in initial capitals.
..

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. i18n: .. While every precaution has been taken in the preparation of this book, the publisher
.. i18n: .. and the authors assume no responsibility for errors or omissions, or for damages
.. i18n: .. resulting from the use of the information contained herein.
..

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. i18n: .. Published by Open Object Press, Grand Rosière, Belgium
..

.. Published by Open Object Press, Grand Rosière, Belgium
