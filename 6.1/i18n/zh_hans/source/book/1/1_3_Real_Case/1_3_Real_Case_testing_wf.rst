.. i18n: Driving a Purchase / Sales Flow
.. i18n: ===============================
..

优化 采购/销售 业务流程
===============================

.. i18n: To familiarize yourself with the system workflow, you will test a purchase-sale workflow in two phases.
..

为了熟悉业务流程,下面我们以采购与销售两个业务做样例.

.. i18n: The first consists of product purchase, which requires the following operations:
..

首先是采购业务,我们要达成下面的目的:

.. i18n: 	#. Place a purchase order with Plumbing Component Suppliers for 10 Titanium Alloy Radiators at a
.. i18n: 	   unit price of 56.00.
.. i18n: 
.. i18n: 	#. Receive these products at your Goods In.
.. i18n: 
.. i18n: 	#. Generate a purchase invoice.
.. i18n: 
.. i18n: 	#. Pay your supplier.
..

	#. 从 元件供应商 那里以单价 56.00 采购 10 个 :guilabel:`钛合金散热器` .

	#. 做采购收货入库操作.

	#. 做供应商采购发票.

	#. 支付该发票.

.. i18n: Following this, you will sell some of these products, using this sequence:
..

然后,我们再做销售业务,以下面的数据为样例: 

.. i18n: 	#. Receive a sales order for 6 Titanium Alloy Radiators from Smith and Sons, sold at a unit price
.. i18n: 	   of 130.00.
.. i18n: 
.. i18n: 	#. Dispatch the products.
.. i18n: 
.. i18n: 	#. Invoice the customer.
.. i18n: 
.. i18n: 	#. Receive the payment.
..

	#. 向 :guilabel:`客户` Smith and Sons 以单价 130.00/个 销售 6 个 :guilabel:`钛合金散热器` .

	#. 安排发货送货.

	#. 开据客户发票.

	#. 并做客户收款.

.. i18n: .. _sect-PO:
.. i18n: 
.. i18n: Purchase Order
.. i18n: --------------
..

.. _sect-PO:

采购
--------------

.. i18n: To place a Purchase Order with your supplier, use the menu :menuselection:`Purchases --> Purchase Management -->
.. i18n: Purchase Orders` and click the `New` button.
..

要给供应商下达采购任务,菜单入口在 :menuselection:`Purchases --> Purchase Management --> Purchase Orders` 中文菜单项为 :menuselection:`采购 --> 采购管理 --> 采购订单`
点击 :guilabel:`新建` 按钮即可。

.. i18n: Complete the following field:
..

并填写采购订单中下面的字段:

.. i18n: *  :guilabel:`Supplier` : \ ``Plumbing Component Suppliers``\  .
..

*  :guilabel:`Supplier` : \ ``Plumbing Component Suppliers``\  .

.. i18n: As you complete the :guilabel:`Supplier` field, OpenERP automatically completes the
.. i18n: :guilabel:`Address` field and the :guilabel:`Pricelist` field from information it takes out of the
.. i18n: Partner record.
..

当你选择了 :guilabel:`供应商` 后, 采购订单会自动完成该供应商的 :guilabel:`地址` 及 :guilabel:`价格表` 字段。

.. i18n: Enter the following information
..

Enter the following information

.. i18n: *  :guilabel:`Product` : \ ``Titanium Alloy Radiator``\   - type in part of this name then
.. i18n:    press the tab key to complete it, or click the
.. i18n:    :guilabel:`Search` icon at the end of the line to bring a search box. (if product is previously configured)
..

*  :guilabel:`Product` : \ ``Titanium Alloy Radiator``\   - type in part of this name then
   press the tab key to complete it, or click the
   :guilabel:`Search` icon at the end of the line to bring a search box. (if product is previously configured)

.. i18n: When you have selected a product on the product line, OpenERP automatically completes the following
.. i18n: fields from information it finds in the Product record:
..

当你在采购明细行选择一个产品后，OpenERP会自动将该产品的其他下面的信息带出来:

.. i18n: * :guilabel:`Product UOM` : the unit of measure for this product,
.. i18n: 
.. i18n: * :guilabel:`Description` : the detailed description of the product,
.. i18n: 
.. i18n: * :guilabel:`Scheduled Date` : based on the product lead time,
.. i18n: 
.. i18n: * :guilabel:`Unit Price` : the unit price of the product,
.. i18n: 
.. i18n: * :guilabel:`Analytic account` : if any account is specified then it will appear on the order line (it is not in this example),
.. i18n: 
.. i18n: * :guilabel:`Taxes` : applicable taxes defined in the partner, if specified, otherwise in the
.. i18n:   product, if specified (there are not any in this example).
..

* :guilabel:`单位` : 产品的默认采购单位,

* :guilabel:`名称` : 产品的描述性名称,

* :guilabel:`交货日期` : 采购预计交付时间,

* :guilabel:`单价` : 产品的价格规则产生的默认采购价格,

* :guilabel:`辅助核算项` : 当你设置了辅助核算默认项值，会自动带出来。(本例没有设置相关辅助核算),

* :guilabel:`税` : applicable taxes defined in the partner, if specified, otherwise in the
  product, if specified (there are not any in this example).

.. i18n: You can edit any of these fields to suit the requirements of the purchase order at the time of
.. i18n: entry. Change the:
..

按上面的需求,修改采购订单中的数量及价格字段:

.. i18n: * :guilabel:`Quantity` : \ ``10``\ ,
.. i18n: 
.. i18n: * :guilabel:`Unit Price` to \ ``56.00``\ .
..

* :guilabel:`数量` : \ ``10``\ ,

* :guilabel:`价格`  \ ``56.00``\ .

.. i18n: Save the order line and close the :guilabel:`Order Line` window by clicking the
.. i18n: :guilabel:`Close` button. You can then confirm the whole one-line order by clicking
.. i18n: :guilabel:`Save`, which makes the form non-editable.
..

保存采购订单明细,点击 :guilabel:`关闭` 按钮关闭 :guilabel:`明细` 窗口. 点 :guilabel:`保存` 按钮, 可以保存数据并查看明细数据而不关闭窗口.

.. i18n: It is now in a state of \ ``Request for
.. i18n: Quotation``\ , so click :guilabel:`Convert to Purchase Order`, which corresponds to an approval from
.. i18n: a manager or from Accounts within your own company and moves the order into \ ``Approved`` \
.. i18n: state.
..

目前为止采购还仅是\ ``询价状态``\ ,现在你可以使用 \ ``采购经理``\ 或者 \ ``公司财务``\ 的角色 进到本采购单 点击 :guilabel:`转换为采购单` 的按钮, 批准该笔采购.

.. i18n: If you click the :guilabel:`Delivery & Invoicing` tab
.. i18n: you will see the delivery :guilabel:`Destination` is your own company's ``Stock`` location and that
.. i18n: the invoice was created from the order.
.. i18n: It is not entirely obvious at this stage, but the invoice is in a draft state so it can be
.. i18n: edited and, crucially, has no accounting impact yet: it is just ready for your accounting
.. i18n: group to activate it.
..

If you click the :guilabel:`Delivery & Invoicing` tab
you will see the delivery :guilabel:`Destination` is your own company's ``Stock`` location and that
the invoice was created from the order.
It is not entirely obvious at this stage, but the invoice is in a draft state so it can be
edited and, crucially, has no accounting impact yet: it is just ready for your accounting
group to activate it.

.. i18n: Receiving Goods
.. i18n: ---------------
..

收货
---------------

.. i18n: After confirming the order, you would wait for the delivery of the products from your supplier. Typically
.. i18n: this would be somebody in Stores, who would:
..

在确认采购后,就需要等供应商送货,并按下面的操作进行收货操作:

.. i18n: 	#. Open the menu :menuselection:`Warehouse --> Warehouse Management --> Incoming Shipments` using the expand/collapse icon.
..

	#. Open the menu :menuselection:`Warehouse --> Warehouse Management --> Incoming Shipments` using the expand/collapse icon.

.. i18n: 	   .. note:: From the Purchase Order
.. i18n: 
.. i18n: 	      You could have clicked the :guilabel:`Receptions` link to the right of the Purchase Order
.. i18n: 	      to reach the same screen, but this would confuse the purchasing role with the
.. i18n: 	      stores role. That link is very useful during testing and training, however.
.. i18n: 
.. i18n: 	#. When the :guilabel:`Incoming Shipments` window appears, select the name of the entry in the list
.. i18n: 	   (\ ``IN/00002``\)   to display the Packing List itself – you would usually do a search for the supplier name
.. i18n: 	   or order number in a list that was larger than this – then click :guilabel:`Process` to load the
.. i18n: 	   :guilabel:`Process Document` form.
.. i18n: 
.. i18n: 	#. Click :guilabel:`Validate` to indicate that you are receiving the whole quantity of 10 units.
..

	   .. note:: From the Purchase Order

	      You could have clicked the :guilabel:`Receptions` link to the right of the Purchase Order
	      to reach the same screen, but this would confuse the purchasing role with the
	      stores role. That link is very useful during testing and training, however.

	#. When the :guilabel:`Incoming Shipments` window appears, select the name of the entry in the list
	   (\ ``IN/00002``\)   to display the Packing List itself – you would usually do a search for the supplier name
	   or order number in a list that was larger than this – then click :guilabel:`Process` to load the
	   :guilabel:`Process Document` form.

	#. Click :guilabel:`Validate` to indicate that you are receiving the whole quantity of 10 units.

.. i18n: At this point you have accepted 10 units into your company, in a location that you have already seen.
..

当你收货确认这一刻,你应该可以在对应库存查询到公司该产品的相应库存量了. 恭喜恭喜...

.. i18n: Using the menu :menuselection:`Purchases --> Products --> Products` you can find the product `Titanium Alloy Radiators`
.. i18n: with `Real Stock` and `Virtual Stock` 10. From the product form click on the link at the right most side `Stock by Location`,
.. i18n: you can see the `Real Stock` and `Virtual Stock` of this product in various locations. Now click on the `Location Inventory Overview`
.. i18n: report to see the inventory valuation per location.
..

使用菜单 :menuselection:`采购 --> 产品 --> 产品展示` 你可以找到产品 :guilabel:`钛合金散热器` 实物库存和虚拟库存数量为10.0了。 单击该产品进入到产品 :guilabel:`表单` 页后,在右面最右侧的 :guilabel:`按库位查看库存` 链接可以直接查看该产品在各个物理库位与虚拟库位的数量分布情况。点击 :guilabel:`库位库存概要` 报表就可以查看到各库位各产品的详细库存情况。

.. i18n: .. _fig-lotsbyloc:
.. i18n: 
.. i18n: .. figure::  images/lots_by_location_pdf.png
.. i18n:    :scale: 65
.. i18n:    :align: center
.. i18n: 
.. i18n:    *List of products and their stock levels*
..

.. _fig-lotsbyloc:

.. figure::  images/lots_by_location_pdf.png
   :scale: 65
   :align: center

   *List of products and their stock levels*

.. i18n: .. tip:: Traceability in Double-entry
.. i18n: 
.. i18n:    OpenERP operates a double-entry stock transfer scheme similar to double-entry accounting.
.. i18n:    Because of this you can carry out various analyses of stock levels in your warehouse,
.. i18n:    along with the corresponding levels in Partner Location at your Supplier.
.. i18n:    The double-entry system, analogous to that of accounting, enables you to keep track
.. i18n:    of stock movements quite easily, and to resolve any errors that occur.
..

.. tip:: Traceability in Double-entry

   OpenERP operates a double-entry stock transfer scheme similar to double-entry accounting.
   Because of this you can carry out various analyses of stock levels in your warehouse,
   along with the corresponding levels in Partner Location at your Supplier.
   The double-entry system, analogous to that of accounting, enables you to keep track
   of stock movements quite easily, and to resolve any errors that occur.

.. i18n: Invoice Control
.. i18n: ---------------
..

开票管理
---------------

.. i18n: When you have received an invoice from your supplier (which would usually be sent to your Accounts department),
.. i18n: go to the menu :menuselection:`Accounting --> Suppliers --> Supplier Invoices`
.. i18n: to open a list of supplier invoices waiting for receipt.
.. i18n: These invoices enable your Accounts Department to match the price and quantities
.. i18n: ordered against the price and quantities on the supplier's invoice (and since it is not uncommon to receive
.. i18n: an invoice showing details more favourable to the supplier than those agreed at the time of
.. i18n: purchase, this is a useful function).
..

When you have received an invoice from your supplier (which would usually be sent to your Accounts department),
go to the menu :menuselection:`Accounting --> Suppliers --> Supplier Invoices`
to open a list of supplier invoices waiting for receipt.
These invoices enable your Accounts Department to match the price and quantities
ordered against the price and quantities on the supplier's invoice (and since it is not uncommon to receive
an invoice showing details more favourable to the supplier than those agreed at the time of
purchase, this is a useful function).

.. i18n: In this example, you created an invoice automatically when you confirmed the supplier's Purchase
.. i18n: Order. That is because the :guilabel:`Invoicing Control`  field on the order was set to \ ``From
.. i18n: Order``\ (the default option). Other options enable you to create invoices at the time of
.. i18n: receiving goods or manually. The initial state of an invoice is \ ``Draft``\  .
..

In this example, you created an invoice automatically when you confirmed the supplier's Purchase
Order. That is because the :guilabel:`Invoicing Control`  field on the order was set to \ ``From
Order``\ (the default option). Other options enable you to create invoices at the time of
receiving goods or manually. The initial state of an invoice is \ ``Draft``\  .

.. i18n: Now click the invoice for your order \ ``PO00001``\  to display its contents. You can compare the
.. i18n: goods that you have recorded there with the invoice received from your supplier. If there is a
.. i18n: difference, it is possible to change the order lines to, for example, add a delivery charge. Click
.. i18n: :guilabel:`Validate` to confirm the invoice and put it into the \ ``Open`` \   state.
..

Now click the invoice for your order \ ``PO00001``\  to display its contents. You can compare the
goods that you have recorded there with the invoice received from your supplier. If there is a
difference, it is possible to change the order lines to, for example, add a delivery charge. Click
:guilabel:`Validate` to confirm the invoice and put it into the \ ``Open`` \   state.

.. i18n: Accounting entries are generated automatically once the invoice is validated. To see the effects on
.. i18n: your chart of accounts, use the menu :menuselection:`Accounting --> Charts --> Chart of
.. i18n: Accounts` ,then click :guilabel:`Open Charts` at the :guilabel:`Chart of Accounts` page to see that you
.. i18n: have a debit of ``560.00`` in the ``Purchases`` account and a credit of ``560.00`` in
.. i18n: the ``Payable`` account.
..

Accounting entries are generated automatically once the invoice is validated. To see the effects on
your chart of accounts, use the menu :menuselection:`Accounting --> Charts --> Chart of
Accounts` ,then click :guilabel:`Open Charts` at the :guilabel:`Chart of Accounts` page to see that you
have a debit of ``560.00`` in the ``Purchases`` account and a credit of ``560.00`` in
the ``Payable`` account.

.. i18n: Paying the Supplier
.. i18n: -------------------
..

支付货款
-------------------

.. i18n: Select the menu :menuselection:`Accounting --> Suppliers --> Supplier Invoices` and click on the :guilabel:`Unpaid` button
.. i18n: for a list of supplier invoices that have not yet been paid. Write the
.. i18n: ``PO00001`` in  `Source Document` text itself to find the invoice.
.. i18n: In practice, you would search for the invoice by order number or,
.. i18n: more generally, for invoices nearing their payment date.
..

选择菜单 :menuselection:`Accounting --> Suppliers --> Supplier Invoices` and click on the :guilabel:`Unpaid` button
  for a list of supplier invoices that have not yet been paid. 写PO00001在源文档文本本身发现发票。在实践中,你将会寻找发票通过订单号,或更普遍而言,他们的付款日期为发票接近。

.. i18n: Click on :guilabel:`Pay Invoice` button in the supplier invoice form. It opens the
.. i18n: :guilabel:`Pay Invoice` window in new tab with a description of the payment.
..

Click on :guilabel:`Pay Invoice` button in the supplier invoice form. It opens the
:guilabel:`Pay Invoice` window in new tab with a description of the payment.

.. i18n: ``Supplier`` and ``Date`` comes automatically from invoice. You need to just enter the
.. i18n: ``Payment Method``.  After that, click on :guilabel:`Validate` button to post this entry.
..

``Supplier`` and ``Date`` comes automatically from invoice. You need to just enter the
``Payment Method``.  After that, click on :guilabel:`Validate` button to post this entry.

.. i18n: .. index::
.. i18n:    single: module; account
..

.. index::
   single: module; account

.. i18n: .. note:: Payment of an Invoice
.. i18n: 
.. i18n: 	The method described here is for companies that do not use their accounting system to pay bills –
.. i18n: 	just to record them.
.. i18n: 	If you are using the :mod:`account` module with all its features, other, more efficient, methods let you manage payments,
.. i18n: 	such as entering account statements, reconciling paperwork, using tools for preparing payments,
.. i18n: 	interfacing with banks.
..

.. note:: Payment of an Invoice

	

        这里描述的方法是为企业,不使用他们的会计系统付账单——
        只是来记录他们

	If you are using the :mod:`account` module with all its features, other, more efficient, methods let you manage payments,
	such as entering account statements, reconciling paperwork, using tools for preparing payments,
	interfacing with banks.

.. i18n: You can monitor the accounting impact of paying the invoice through the chart of accounts available
.. i18n: from the menu :menuselection:`Accounting --> Charts --> Chart of Accounts`. OpenERP
.. i18n: automatically creates accounting entries from the payment, and can reconcile the payment to the
.. i18n: invoice. You now have a new transaction that has debited the ``Payable`` account with ``560.00`` and
.. i18n: credited the ``Cash`` account.
..

You can monitor the accounting impact of paying the invoice through the chart of accounts available
from the menu :menuselection:`Accounting --> Charts --> Chart of Accounts`. OpenERP
automatically creates accounting entries from the payment, and can reconcile the payment to the
invoice. You now have a new transaction that has debited the ``Payable`` account with ``560.00`` and
credited the ``Cash`` account.

.. i18n: If you look in :menuselection:`Accounting --> Journal Entries --> Journal Entries` you will see both
.. i18n: accounting transactions, one in each of the ``Purchase`` Journal and ``Bank`` Journal in
.. i18n: ``Draft`` state.
..

If you look in :menuselection:`Accounting --> Journal Entries --> Journal Entries` you will see both
accounting transactions, one in each of the ``Purchase`` Journal and ``Bank`` Journal in
``Draft`` state.

.. i18n: From Sales Proposal to Sales Order
.. i18n: ----------------------------------
..

商机产生销售
----------------------------------

.. i18n: In OpenERP, sales proposals and sales orders are managed using documents that are based on the
.. i18n: same common functionality as purchase orders, so you will recognize the following documents in general
.. i18n: but see changes to their detail and to their workflows. To create a new sales proposal, use the
.. i18n: menu :menuselection:`Sales --> Sales --> Sales Orders` and click on `New` button which creates a new order in a state of \
.. i18n: ``Quotation``\  , then:
..

In OpenERP, sales proposals and sales orders are managed using documents that are based on the
same common functionality as purchase orders, so you will recognize the following documents in general
but see changes to their detail and to their workflows. To create a new sales proposal, use the
menu :menuselection:`Sales --> Sales --> Sales Orders` and click on `New` button which creates a new order in a state of \
``Quotation``\  , then:

.. i18n: 	#. Select the :guilabel:`Customer` \ ``Axelor`` \. This has the effect of automatically
.. i18n: 	   completing several other fields: :guilabel:`Ordering Contact`, :guilabel:`Invoice Address`,
.. i18n: 	   :guilabel:`Shipping Address`, and the :guilabel:`Pricelist` \ ``Public Pricelist (EUR)``\.  They are
.. i18n: 	   all only defaults, so these fields can be modified as you need.
.. i18n: 
.. i18n: 	#. Click the :guilabel:`New` button in :guilabel:`Sales Order Lines` section to open a :guilabel:`Sales Order Lines` window.
.. i18n: 
.. i18n: 	#. Select the product \ ``Titanium Alloy Radiator`` \. Although the :guilabel:`Product` field is not
.. i18n: 	   itself required, it is used by OpenERP to select the specific product so that several other fields
.. i18n: 	   can be automatically completed on the order line of the proposal, such as :guilabel:`Description`,
.. i18n: 	   :guilabel:`Unit of Measure`, :guilabel:`Unit Price`, :guilabel:`Procurement Method`,
.. i18n: 	   :guilabel:`Delivery Lead Time`, and :guilabel:`Taxes`.
.. i18n: 
.. i18n: 	#. Change the :guilabel:`Quantity (UoM)` to \ ``6``\  and the :guilabel:`Unit Price` to \ ``130.00``\.
.. i18n: 	   Then click :guilabel:`Save & Close` and the line appears on the quotation form.
.. i18n: 
.. i18n: 	#. On the :guilabel:`Other Information` tab of this Sales Order, select a
.. i18n: 	   :guilabel:`Picking Policy` of ``Complete Delivery`` and
.. i18n: 	   :guilabel:`Shipping Policy` of ``Invoice on Order After Delivery`` from their dropdown menu lists.
.. i18n: 
.. i18n: 	#. Return to the first tab :guilabel:`Sales Order` and validate the document by clicking
.. i18n: 	   :guilabel:`Confirm Order` which calculates prices and the changes the order's state from \
.. i18n: 	   ``Quotation``\  to \ ``In Progress`` \ as shown in screenshot :ref:`fig-ch03ord`.
.. i18n: 	   If you were in negotiation with the prospective customer,
.. i18n: 	   you would keep clicking :guilabel:`Compute` and :guilabel:`Save`, keeping the document in \
.. i18n: 	   ``Quotation``\  state for as long as necessary.
..

	#. Select the :guilabel:`Customer` \ ``Axelor`` \. This has the effect of automatically
	   completing several other fields: :guilabel:`Ordering Contact`, :guilabel:`Invoice Address`,
	   :guilabel:`Shipping Address`, and the :guilabel:`Pricelist` \ ``Public Pricelist (EUR)``\.  They are
	   all only defaults, so these fields can be modified as you need.

	#. Click the :guilabel:`New` button in :guilabel:`Sales Order Lines` section to open a :guilabel:`Sales Order Lines` window.

	#. Select the product \ ``Titanium Alloy Radiator`` \. Although the :guilabel:`Product` field is not
	   itself required, it is used by OpenERP to select the specific product so that several other fields
	   can be automatically completed on the order line of the proposal, such as :guilabel:`Description`,
	   :guilabel:`Unit of Measure`, :guilabel:`Unit Price`, :guilabel:`Procurement Method`,
	   :guilabel:`Delivery Lead Time`, and :guilabel:`Taxes`.

	#. Change the :guilabel:`Quantity (UoM)` to \ ``6``\  and the :guilabel:`Unit Price` to \ ``130.00``\.
	   Then click :guilabel:`Save & Close` and the line appears on the quotation form.

	#. On the :guilabel:`Other Information` tab of this Sales Order, select a
	   :guilabel:`Picking Policy` of ``Complete Delivery`` and
	   :guilabel:`Shipping Policy` of ``Invoice on Order After Delivery`` from their dropdown menu lists.

	#. Return to the first tab :guilabel:`Sales Order` and validate the document by clicking
	   :guilabel:`Confirm Order` which calculates prices and the changes the order's state from \
	   ``Quotation``\  to \ ``In Progress`` \ as shown in screenshot :ref:`fig-ch03ord`.
	   If you were in negotiation with the prospective customer,
	   you would keep clicking :guilabel:`Compute` and :guilabel:`Save`, keeping the document in \
	   ``Quotation``\  state for as long as necessary.

.. i18n: 	   .. _fig-ch03ord:
.. i18n: 
.. i18n: 	   .. figure:: images/order.png
.. i18n: 	      :scale: 75
.. i18n: 	      :align: center
.. i18n: 
.. i18n: 	      *Sales Order Form*
.. i18n: 
.. i18n: 	#. In the last tab of the order :guilabel:`History`, you can see the :guilabel:`Picking List`
.. i18n: 	   that has been created and you will be able to see any invoices that relate to this order when they are
.. i18n: 	   generated.
..

	   .. _fig-ch03ord:

	   .. figure:: images/order.png
	      :scale: 75
	      :align: center

	      *Sales Order Form*

	#. In the last tab of the order :guilabel:`History`, you can see the :guilabel:`Picking List`
	   that has been created and you will be able to see any invoices that relate to this order when they are
	   generated.

.. i18n: Go to :menuselection:`Sales --> Products --> Products` to display a list of
.. i18n: products: just the one, \ ``Titanium Alloy Radiator``\  , currently exists in this example. Its
.. i18n: :guilabel:`Real Stock` still shows \ ``10.00``\   but its :guilabel:`Virtual Stock` now shows \
.. i18n: ``4.00``\  to reflect the new future requirement of 6 units for dispatch.
..

Go to :menuselection:`Sales --> Products --> Products` to display a list of
products: just the one, \ ``Titanium Alloy Radiator``\  , currently exists in this example. Its
:guilabel:`Real Stock` still shows \ ``10.00``\   but its :guilabel:`Virtual Stock` now shows \
``4.00``\  to reflect the new future requirement of 6 units for dispatch.

.. i18n: Preparing Goods for Shipping to Customers
.. i18n: -----------------------------------------
..

发货备货
-----------------------------------------

.. i18n: The stores manager selects the menu :menuselection:`Warehouse --> Warehouse Management -->
.. i18n: Delivery Orders` to get a list of orders to dispatch. For this example, find the Delivery Order related
.. i18n: to the sale order which you have created.
..

The stores manager selects the menu :menuselection:`Warehouse --> Warehouse Management -->
Delivery Orders` to get a list of orders to dispatch. For this example, find the Delivery Order related
to the sale order which you have created.

.. i18n: .. index::
.. i18n:    single: module; mrp_jit
..

.. index::
   single: module; mrp_jit

.. i18n: .. tip::  Running Schedulers
.. i18n: 
.. i18n: 	At the moment, your Sales Order is waiting for products to be reserved to fulfil it.
.. i18n: 	A stock reservation activity takes place periodically to calculate the needs,
.. i18n: 	which also takes customer priorities into account.
.. i18n: 	The calculation can be started from the menu
.. i18n: 	:menuselection:`Warehouse --> Schedulers --> Compute Schedulers`.
.. i18n: 	Running this automatically reserves products.
.. i18n: 
.. i18n: 	If you do not want to have to work out your stock needs but have a lean workflow you can install the
.. i18n: 	:mod:`mrp_jit` (Just In Time) module.
..

.. tip::  Running Schedulers

	At the moment, your Sales Order is waiting for products to be reserved to fulfil it.
	A stock reservation activity takes place periodically to calculate the needs,
	which also takes customer priorities into account.
	The calculation can be started from the menu
	:menuselection:`Warehouse --> Schedulers --> Compute Schedulers`.
	Running this automatically reserves products.

	If you do not want to have to work out your stock needs but have a lean workflow you can install the
	:mod:`mrp_jit` (Just In Time) module.

.. i18n: Although OpenERP has automatically been made aware that items on this order will need to be
.. i18n: dispatched, it has not yet assigned any specific items from any location to fulfil it. It is ready to
.. i18n: move \ ``6.00``\  \ ``Titanium Alloy Radiators``\   from the :guilabel:`Stock` location to the :guilabel:`Customers`
.. i18n: location, so start this process by clicking
.. i18n: :guilabel:`Check Availability`. The :guilabel:`Move` line has now changed from the \ ``Confirmed``\   state to
.. i18n: the \ ``Available``\   state.
..

Although OpenERP has automatically been made aware that items on this order will need to be
dispatched, it has not yet assigned any specific items from any location to fulfil it. It is ready to
move \ ``6.00``\  \ ``Titanium Alloy Radiators``\   from the :guilabel:`Stock` location to the :guilabel:`Customers`
location, so start this process by clicking
:guilabel:`Check Availability`. The :guilabel:`Move` line has now changed from the \ ``Confirmed``\   state to
the \ ``Available``\   state.

.. i18n: Then click the :guilabel:`Process` button to reach the :guilabel:`Process Document` window, where
.. i18n: you click the :guilabel:`Validate` button to transfer the 6 radiators to the customer.
..

Then click the :guilabel:`Process` button to reach the :guilabel:`Process Document` window, where
you click the :guilabel:`Validate` button to transfer the 6 radiators to the customer.

.. i18n: To analyze stock movements that you have made during these operations, use
.. i18n: :menuselection:`Warehouse --> Product --> Product` and find this product, then click on the action
.. i18n: `Stock by Location` which is at the right most side to see that your stocks have reduced to
.. i18n: 4 radiators and the generic ``Customers`` location has a level of 6 radiators.
..

To analyze stock movements that you have made during these operations, use
:menuselection:`Warehouse --> Product --> Product` and find this product, then click on the action
`Stock by Location` which is at the right most side to see that your stocks have reduced to
4 radiators and the generic ``Customers`` location has a level of 6 radiators.

.. i18n: Invoicing Goods
.. i18n: ---------------
..

进销存
---------------

.. i18n: Use the menu :menuselection:`Accounting --> Customers --> Customer Invoices`
.. i18n: to open a list of Sales invoices generated by OpenERP. If they are in the \ ``Draft`` \
.. i18n: state, it means that they do not yet have any presence in the accounting system. You will find a
.. i18n: draft invoice has been created for the order \ ``SO00008``\   once you have dispatched the goods
.. i18n: because you had selected \ ``Invoice on Order After Delivery``\  .
..

Use the menu :menuselection:`Accounting --> Customers --> Customer Invoices`
to open a list of Sales invoices generated by OpenERP. If they are in the \ ``Draft`` \
state, it means that they do not yet have any presence in the accounting system. You will find a
draft invoice has been created for the order \ ``SO00008``\   once you have dispatched the goods
because you had selected \ ``Invoice on Order After Delivery``\  .

.. i18n: Once you confirm an invoice, OpenERP assigns it a unique number, and all of the corresponding
.. i18n: accounting entries are generated. So open the invoice and click :guilabel:`Validate` to do that and
.. i18n: move the invoice into an \ ``Open``\   state with a number of ``SAJ/2011/001``.
..

Once you confirm an invoice, OpenERP assigns it a unique number, and all of the corresponding
accounting entries are generated. So open the invoice and click :guilabel:`Validate` to do that and
move the invoice into an \ ``Open``\   state with a number of ``SAJ/2011/001``.

.. i18n: You can send your customer the invoice for payment at this stage. Click :guilabel:`Print Invoice`
.. i18n: to get a PDF document that can be printed or emailed to the customer.
..

You can send your customer the invoice for payment at this stage. Click :guilabel:`Print Invoice`
to get a PDF document that can be printed or emailed to the customer.

.. i18n: You can also attach the PDF document to the OpenERP invoice record. Save the PDF somewhere
.. i18n: convenient on your PC (such as on your desktop). Then click the :guilabel:`Add` button to the top right of
.. i18n: the invoice form (it looks like a clipboard). Browse to the
.. i18n: file you just saved (\ ``record.pdf``\   if you did not change its name).
.. i18n: This gives you a permanent non-editable record of your invoice on the OpenERP system.
..

You can also attach the PDF document to the OpenERP invoice record. Save the PDF somewhere
convenient on your PC (such as on your desktop). Then click the :guilabel:`Add` button to the top right of
the invoice form (it looks like a clipboard). Browse to the
file you just saved (\ ``record.pdf``\   if you did not change its name).
This gives you a permanent non-editable record of your invoice on the OpenERP system.

.. i18n: Review your chart of accounts to check the impact of these activities on your accounting. You will see
.. i18n: the new revenue line from the invoice.
..

Review your chart of accounts to check the impact of these activities on your accounting. You will see
the new revenue line from the invoice.

.. i18n: Customer Payment
.. i18n: ----------------
..

客户收款
----------------

.. i18n: Registering an invoice payment by a customer is essentially the same as the process of paying a
.. i18n: supplier. From the menu :menuselection:`Accounting --> Customers --> Customer Invoices`,
.. i18n: click the name of the invoice that you want to mark as paid:
..

Registering an invoice payment by a customer is essentially the same as the process of paying a
supplier. From the menu :menuselection:`Accounting --> Customers --> Customer Invoices`,
click the name of the invoice that you want to mark as paid:

.. i18n: 	#. Use the :guilabel:`Payment` button which opens a new window `Pay Invoice`.
.. i18n: 
.. i18n: 	#. Select the :guilabel:`Payment Method`, for this example select ``Cash`` then validate the entry.
..

	#. Use the :guilabel:`Payment` button which opens a new window `Pay Invoice`.

	#. Select the :guilabel:`Payment Method`, for this example select ``Cash`` then validate the entry.

.. i18n: .. _fig_ch03faminv:
.. i18n: 
.. i18n: .. figure::  images/familiarization_invoice.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Invoice Form*
..

.. _fig_ch03faminv:

.. figure::  images/familiarization_invoice.png
   :scale: 75
   :align: center

   *Invoice Form*

.. i18n: Check your Chart of Accounts as before to see that you now have a healthy bank balance in the \
.. i18n: ``Cash``\   account.
..

Check your Chart of Accounts as before to see that you now have a healthy bank balance in the \
``Cash``\   account.

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
