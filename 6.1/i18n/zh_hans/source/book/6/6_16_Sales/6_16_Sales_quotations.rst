.. i18n: Managing your Sales Quotations
.. i18n: ==============================
..

管理销售报价单
==============================

.. i18n: In OpenERP, a quotation and an order are handled in the same form (a Sales Order), but in different states. You
.. i18n: can consider an order to be a quotation that has evolved, because it has been confirmed by the
.. i18n: customer. Or, conversely, that a quotation is an order that has not been validated or cancelled yet.
.. i18n: Both your quotations and sales orders can be opened using the menu :menuselection:`Sales
.. i18n: --> Sales --> Sales Orders`.
..

In OpenERP, a quotation and an order are handled in the same form (a Sales Order), but in different states. You
can consider an order to be a quotation that has evolved, because it has been confirmed by the
customer. Or, conversely, that a quotation is an order that has not been validated or cancelled yet.
Both your quotations and sales orders can be opened using the menu :menuselection:`Sales
--> Sales --> Sales Orders`.

.. i18n: To enter details of a new quotation, you can use the menu :menuselection:`Sales -->
.. i18n: Sales --> Sales Orders` and then select :guilabel:`New`. OpenERP opens a new window
.. i18n: allowing you to enter data into a new blank quotation form. You can also create a quotation directly from an opportunity, as explained in a previous chapter.
..

To enter details of a new quotation, you can use the menu :menuselection:`Sales -->
Sales --> Sales Orders` and then select :guilabel:`New`. OpenERP opens a new window
allowing you to enter data into a new blank quotation form. You can also create a quotation directly from an opportunity, as explained in a previous chapter.

.. i18n: .. figure:: images/sale_quotation_new.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *New Quotation*
..

.. figure:: images/sale_quotation_new.png
   :scale: 75
   :align: center

   *New Quotation*

.. i18n: Some information is automatically specified by the system:
..

Some information is automatically specified by the system:

.. i18n: * an internal reference for the quotation or order,
.. i18n: 
.. i18n: * the sales point that the order will be delivered from,
.. i18n: 
.. i18n: * the order date,
.. i18n: 
.. i18n: * the pricelist for the current sales order.
..

* an internal reference for the quotation or order,

* the sales point that the order will be delivered from,

* the order date,

* the pricelist for the current sales order.

.. i18n: You can modify any of that information before validating the quotation. The customer
.. i18n: reference is shown in the header of the order. This optional field is for the customer's own reference –
.. i18n: if the customer does not supply one, just leave it empty.
..

You can modify any of that information before validating the quotation. The customer
reference is shown in the header of the order. This optional field is for the customer's own reference –
if the customer does not supply one, just leave it empty.

.. i18n: You then enter all the data about the order in the :guilabel:`Sales Order` tab. Start by entering
.. i18n: the customer name, by selecting the correct customer from the list of customers in the system. From the quotation, you can
.. i18n: create a new customer on the fly if necessary – press :kbd:`<F1>` in the empty :guilabel:`Customer` field to do that, or type the name, press the `Tab` key and then click `Create`. Indeed, when you type a name or part of a name in the ``Customer`` field, and OpenERP does not find a corresponding customer, you will see the `Create` button appear to allow you to directly create the customer with the name you entered.
..

You then enter all the data about the order in the :guilabel:`Sales Order` tab. Start by entering
the customer name, by selecting the correct customer from the list of customers in the system. From the quotation, you can
create a new customer on the fly if necessary – press :kbd:`<F1>` in the empty :guilabel:`Customer` field to do that, or type the name, press the `Tab` key and then click `Create`. Indeed, when you type a name or part of a name in the ``Customer`` field, and OpenERP does not find a corresponding customer, you will see the `Create` button appear to allow you to directly create the customer with the name you entered.

.. i18n: Once the customer name has been selected, different fields of the order are completed
.. i18n: automatically, based on the configuration of the partner form for that customer:
..

Once the customer name has been selected, different fields of the order are completed
automatically, based on the configuration of the partner form for that customer:

.. i18n: * :guilabel:`Ordering Contact` : person handling the order at the customer end. By default, OpenERP
.. i18n:   proposes the Ordering Contact at the selected partner.
.. i18n: 
.. i18n: * :guilabel:`Delivery Address` : address used on the delivery order. By default, OpenERP proposes
.. i18n:   the delivery address from the partner form. If no specific delivery address is defined, the default
.. i18n:   address will be used instead.
.. i18n: 
.. i18n: * :guilabel:`Invoice Address` : address used to send the invoice to the customer. By default, OpenERP
.. i18n:   proposes the address labelled :guilabel:`Invoice` from the partner form. If no specific invoice address is defined, the default
.. i18n:   address will be used instead.
.. i18n: 
.. i18n: * :guilabel:`Pricelist` : will determine both the currency of the quotation and the price that will
.. i18n:   be used for each product.
.. i18n: 
.. i18n: * :guilabel:`Payment Term` : available in the :guilabel:`Other Information` tab, it shows the payment
.. i18n:   method that the customer will follow, for example ``30 Days End of Month``.
..

* :guilabel:`Ordering Contact` : person handling the order at the customer end. By default, OpenERP
  proposes the Ordering Contact at the selected partner.

* :guilabel:`Delivery Address` : address used on the delivery order. By default, OpenERP proposes
  the delivery address from the partner form. If no specific delivery address is defined, the default
  address will be used instead.

* :guilabel:`Invoice Address` : address used to send the invoice to the customer. By default, OpenERP
  proposes the address labelled :guilabel:`Invoice` from the partner form. If no specific invoice address is defined, the default
  address will be used instead.

* :guilabel:`Pricelist` : will determine both the currency of the quotation and the price that will
  be used for each product.

* :guilabel:`Payment Term` : available in the :guilabel:`Other Information` tab, it shows the payment
  method that the customer will follow, for example ``30 Days End of Month``.

.. i18n: You can modify any of these fields on the order as you go.
..

You can modify any of these fields on the order as you go.

.. i18n: You can also set an analytic account for your order. This account will be used during invoicing
.. i18n: to generate accounting entries corresponding to the invoice automatically. This is extremely useful
.. i18n: for assigning revenues to the project or case specified by this order.
..

You can also set an analytic account for your order. This account will be used during invoicing
to generate accounting entries corresponding to the invoice automatically. This is extremely useful
for assigning revenues to the project or case specified by this order.

.. i18n: .. tip::  Analytic Accounts
.. i18n: 
.. i18n:    If you are managing by task, the analytic account to be selected is the one that corresponds to
.. i18n:    the project for the order.
.. i18n:    The sales carried out by the order can be allocated to the project so that profitability
.. i18n:    calculations can be made.
..

.. tip::  Analytic Accounts

   If you are managing by task, the analytic account to be selected is the one that corresponds to
   the project for the order.
   The sales carried out by the order can be allocated to the project so that profitability
   calculations can be made.

.. i18n: Once the information has been entered, you can enter data for the order lines. To do that, create a
.. i18n: new order line as shown in the figure :ref:`fig-slinf`.
..

Once the information has been entered, you can enter data for the order lines. To do that, create a
new order line as shown in the figure :ref:`fig-slinf`.

.. i18n: .. _fig-slinf:
.. i18n: 
.. i18n: .. figure:: images/sale_line_form.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Entering a New Sales Order Line*
..

.. _fig-slinf:

.. figure:: images/sale_line_form.png
   :scale: 75
   :align: center

   *Entering a New Sales Order Line*

.. i18n: First of all, select the product that is to be sold to the customer. OpenERP shows some
.. i18n: useful information in the list of products to help you making a sales quotation:
..

First of all, select the product that is to be sold to the customer. OpenERP shows some
useful information in the list of products to help you making a sales quotation:

.. i18n: * :guilabel:`Real Stock` : physically present in your warehouses. This value depends on the Shop (sales
.. i18n:   point) selected in the order header. Different shops can be linked to different warehouses,
.. i18n:   giving different stock levels, or can use the same warehouse.
.. i18n: 
.. i18n: * :guilabel:`Virtual Stock` : shows a salesperson the quantity that can be sold, taking into account
.. i18n:   both stock reserved for other orders and the number of products planned to arrive in the short term.
.. i18n: 
.. i18n: * :guilabel:`Public Price` : the basic sales price for the given product. It provides a basis for the
.. i18n:   salesperson to be able to judge whether to offer a discount to the customer, and how much the
.. i18n:   discount should be.
.. i18n: 
.. i18n: * :guilabel:`Pricelist` : (may not be shown, depending on the installed modules) depends on the pricing conditions attached to the customer, calculated on the list price. This is the price that is proposed by default in the customer quotation, unless it has been modified by the salesperson.
.. i18n: 
.. i18n: * :guilabel:`Cost Price` : shows the cost price of the product. If the salesperson sells at less
.. i18n:   than this amount, the company incurs a loss.
..

* :guilabel:`Real Stock` : physically present in your warehouses. This value depends on the Shop (sales
  point) selected in the order header. Different shops can be linked to different warehouses,
  giving different stock levels, or can use the same warehouse.

* :guilabel:`Virtual Stock` : shows a salesperson the quantity that can be sold, taking into account
  both stock reserved for other orders and the number of products planned to arrive in the short term.

* :guilabel:`Public Price` : the basic sales price for the given product. It provides a basis for the
  salesperson to be able to judge whether to offer a discount to the customer, and how much the
  discount should be.

* :guilabel:`Pricelist` : (may not be shown, depending on the installed modules) depends on the pricing conditions attached to the customer, calculated on the list price. This is the price that is proposed by default in the customer quotation, unless it has been modified by the salesperson.

* :guilabel:`Cost Price` : shows the cost price of the product. If the salesperson sells at less
  than this amount, the company incurs a loss.

.. i18n: .. figure:: images/sale_product_list.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Selecting a Product in a Sales Order Line*
..

.. figure:: images/sale_product_list.png
   :scale: 75
   :align: center

   *Selecting a Product in a Sales Order Line*

.. i18n: Once the product to be sold to the customer has been selected, OpenERP automatically
.. i18n: completes all the other required fields: quantity, unit of measure, description, unit price,
.. i18n: discount, procurement method, lead times and applicable taxes. All of this information comes from
.. i18n: the product form.
..

Once the product to be sold to the customer has been selected, OpenERP automatically
completes all the other required fields: quantity, unit of measure, description, unit price,
discount, procurement method, lead times and applicable taxes. All of this information comes from
the product form.

.. i18n: .. index::
.. i18n:    single: module; product_visible_discount
..

.. index::
   single: module; product_visible_discount

.. i18n: .. tip:: Visible Discount
.. i18n: 
.. i18n:    If a discounted price is taken from a price list, by default that figure is shown as the
.. i18n:    sales price to the customer. He will see a discount of 0% along with the unit price that is different
.. i18n:    from the list price.
.. i18n:    If you install the module :mod:`product_visible_discount` from ``extra-addons``,
.. i18n:    you can configure whether you want to make the discount
.. i18n:    explicitly visible in an order form as a percentage difference from the list price,
.. i18n:    or just show a reduced unit price as in the default configuration.
..

.. tip:: Visible Discount

   If a discounted price is taken from a price list, by default that figure is shown as the
   sales price to the customer. He will see a discount of 0% along with the unit price that is different
   from the list price.
   If you install the module :mod:`product_visible_discount` from ``extra-addons``,
   you can configure whether you want to make the discount
   explicitly visible in an order form as a percentage difference from the list price,
   or just show a reduced unit price as in the default configuration.

.. i18n: When you enter a quotation, the selected product is presented in the language of the user so that he can see
.. i18n: what he is selling. The description of the product sold can also be expressed in the customer's language.
.. i18n: The translation to the customer's language is used on the quotation or order when it is printed.
..

When you enter a quotation, the selected product is presented in the language of the user so that he can see
what he is selling. The description of the product sold can also be expressed in the customer's language.
The translation to the customer's language is used on the quotation or order when it is printed.

.. i18n: .. figure:: images/sale_line_translation.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Selling a Product in a Partner Language that differs from the User Language*
..

.. figure:: images/sale_line_translation.png
   :scale: 75
   :align: center

   *Selling a Product in a Partner Language that differs from the User Language*

.. i18n: .. note:: One-off Sales
.. i18n: 
.. i18n:    If a product is sold to a customer only once, you do not have to create a completely new
.. i18n:    product form just for that sale.
.. i18n:    You can manually complete all the information in the order without actually creating a product:
.. i18n:    description, price, quantity, lead time, taxes.
.. i18n:    In this case, OpenERP will not generate a delivery note because the a pure description is not a product, and so it is not in stock.
..

.. note:: One-off Sales

   If a product is sold to a customer only once, you do not have to create a completely new
   product form just for that sale.
   You can manually complete all the information in the order without actually creating a product:
   description, price, quantity, lead time, taxes.
   In this case, OpenERP will not generate a delivery note because the a pure description is not a product, and so it is not in stock.

.. i18n: When all of the products are entered, you can print the quotation and send it to the customer. To do
.. i18n: this, click the :guilabel:`Quotation / Order` link in the :guilabel:`Reports` section to the right.
.. i18n: OpenERP opens the quotation in PDF to enable to you to check it before printing.
..

When all of the products are entered, you can print the quotation and send it to the customer. To do
this, click the :guilabel:`Quotation / Order` link in the :guilabel:`Reports` section to the right.
OpenERP opens the quotation in PDF to enable to you to check it before printing.

.. i18n: .. figure:: images/sale_print.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Printing a Sales Quotation*
..

.. figure:: images/sale_print.png
   :scale: 75
   :align: center

   *Printing a Sales Quotation*

.. i18n: When the order is confirmed by the customer, you can confirm the quotation to turn in into a sales order. You can also just cancel the window without confirming the order to leave it in quotation state. To see all the current quotations, you can use the menu :menuselection:`Sales --> Sales --> Sales Orders` and click the :guilabel:`Quotations` filter button.
..

When the order is confirmed by the customer, you can confirm the quotation to turn in into a sales order. You can also just cancel the window without confirming the order to leave it in quotation state. To see all the current quotations, you can use the menu :menuselection:`Sales --> Sales --> Sales Orders` and click the :guilabel:`Quotations` filter button.

.. i18n: To follow the process for your order, you can click on the process view (indicated by a question mark) from the order form. OpenERP
.. i18n: shows you an interactive process view of that order. For more information about its use,
.. i18n: look at :ref:`ch-process`.
..

To follow the process for your order, you can click on the process view (indicated by a question mark) from the order form. OpenERP
shows you an interactive process view of that order. For more information about its use,
look at :ref:`ch-process`.

.. i18n: .. figure:: images/sale_process.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Process View for a Sales order*
..

.. figure:: images/sale_process.png
   :scale: 75
   :align: center

   *Process View for a Sales order*

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
