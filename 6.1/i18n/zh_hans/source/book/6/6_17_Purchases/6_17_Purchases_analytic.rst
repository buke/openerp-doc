.. i18n: Analytic Accounts
.. i18n: =================
..

辅助核算
=================

.. i18n: To manage purchases by project, you should use analytic accounts. 
.. i18n: You can set an analytic account on each line of a supplier order. 
.. i18n: The analytic costs linked to this purchase will be managed
.. i18n: by OpenERP from the goods receipt and confirmation of the supplier invoice.
..

使用辅助核算可以协助你更好地管理采购. 一般只需要在采购单的明细上设置对应的辅助核算项. 这时, 一但确认并开出供应商发票后,
这一笔采购相关的辅助核算成本就会被记录下来.

.. i18n: .. index::
.. i18n:    single: module; hr_timesheet_invoice
..

.. index::
   single: module; hr_timesheet_invoice

.. i18n: The :mod:`hr_timesheet_invoice` module lets you re-invoice the analytic costs automatically using
.. i18n: parameters in the analytic accounts such as sale pricelist, associated partner company, and maximum amount.
..

The :mod:`hr_timesheet_invoice` module lets you re-invoice the analytic costs automatically using
parameters in the analytic accounts such as sale pricelist, associated partner company, and maximum amount.

.. i18n: So you can put an invoice order with a defined invoice workflow in place based on the analytic accounts. If you are
.. i18n: working ``Make to Order``, the workflow will be:
..

So you can put an invoice order with a defined invoice workflow in place based on the analytic accounts. If you are
working ``Make to Order``, the workflow will be:

.. i18n: #. Customer Order,
.. i18n: 
.. i18n: #. Procurement Order on supplier,
.. i18n: 
.. i18n: #. Receive invoice and goods from the supplier,
.. i18n: 
.. i18n: #. Delivery and invoicing to the customer.
..

#. 客户下订单,

#. 给供应商下达采购订单,

#. 供应商送货并开具供应商发票,

#. 发货给客户并开具客户发票.

.. i18n: When re-invoicing based on costs you would get the following workflow:
..

When re-invoicing based on costs you would get the following workflow:

.. i18n: #. Enter the customer contract conditions from the analytic accounts,
.. i18n: 
.. i18n: #. Purchase raw materials and write the services performed into the timesheets,
.. i18n: 
.. i18n: #. Receive the supplier invoice and the products,
.. i18n: 
.. i18n: #. Invoice these costs to the customer.
..

#. Enter the customer contract conditions from the analytic accounts,

#. Purchase raw materials and write the services performed into the timesheets,

#. Receive the supplier invoice and the products,

#. Invoice these costs to the customer.

.. i18n: .. index::
.. i18n:    single: module; purchase_analytic_plans
..

.. index::
   single: module; purchase_analytic_plans

.. i18n: .. tip:: Analytic Multi-plans
.. i18n: 
.. i18n:    If you want several analysis plans, you should install the module :mod:`purchase_analytic_plans`.
.. i18n:    These let you split a line on a supplier purchase order into several accounts and analytic
.. i18n:    plans.
.. i18n:    Look at :ref:`ch-accts` for more information on the use of analytic accounts.
..

.. tip:: 辅助核算方案

   如果你有几种辅助核算方案, 你就需要安装模块 :mod:`purchase_analytic_plans`. 这个模块可以实现将采购单的明细再
   按你设定的核算方案进行拆分.
   参阅 :ref:`ch-accts` 了解更多关于辅助核算的内容.

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
