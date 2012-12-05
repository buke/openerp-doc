
.. i18n: Keep Track of your Margins
.. i18n: ==========================
..

Keep Track of your Margins
==========================

.. i18n: For every company, keeping a clear sight on and a good control of margins is crucial. Even if you have a good sales level, it will not guarantee company profitability if margins are not high enough. OpenERP provides a number of methods allowing you to monitor your sales margins. The main ones are:
..

For every company, keeping a clear sight on and a good control of margins is crucial. Even if you have a good sales level, it will not guarantee company profitability if margins are not high enough. OpenERP provides a number of methods allowing you to monitor your sales margins. The main ones are:

.. i18n: * Margins on a sales order,
.. i18n: 
.. i18n: * Margins by product,
.. i18n: 
.. i18n: * Margins by project,
.. i18n: 
.. i18n: * Using pricelists.
..

* Margins on a sales order,

* Margins by product,

* Margins by project,

* Using pricelists.

.. i18n: Margins on Sales Orders
.. i18n: -----------------------
..

Margins on Sales Orders
-----------------------

.. i18n: .. index::
.. i18n:    single: module; sale_margin
..

.. index::
   single: module; sale_margin

.. i18n: If you want to check your margins on sales orders, you can install the :mod:`sale_margin` module
.. i18n: by selecting :guilabel:`Margins in Sales Orders` for installation in the :guilabel:`Reconfigure` wizard.
.. i18n: This will add margins calculated on each order line and on the order total.
..

If you want to check your margins on sales orders, you can install the :mod:`sale_margin` module
by selecting :guilabel:`Margins in Sales Orders` for installation in the :guilabel:`Reconfigure` wizard.
This will add margins calculated on each order line and on the order total.

.. i18n: .. figure:: images/sale_margin.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *An order with the module sale_margin*
..

.. figure:: images/sale_margin.png
   :scale: 75
   :align: center

   *An order with the module sale_margin*

.. i18n: The margin on each line is defined as the quantity sold multiplied by the sales price for the
.. i18n: customer less the cost price of the products. By default, products are managed using standard price
.. i18n: in OpenERP (cost price fixed manually and reviewed once per year). You can change that to
.. i18n: ``Average Price``, meaning that the product cost fluctuates with purchases from
.. i18n: suppliers. After product receipt you can include fixed costs, such as delivery costs, in the cost of
.. i18n: each product.
..

The margin on each line is defined as the quantity sold multiplied by the sales price for the
customer less the cost price of the products. By default, products are managed using standard price
in OpenERP (cost price fixed manually and reviewed once per year). You can change that to
``Average Price``, meaning that the product cost fluctuates with purchases from
suppliers. After product receipt you can include fixed costs, such as delivery costs, in the cost of
each product.

.. i18n: .. index::
.. i18n:    single: module; product_extended
..

.. index::
   single: module; product_extended

.. i18n: OpenERP supports a third method of updating the cost price of products.
.. i18n: This is through the button :guilabel:`Update` on the product form which lets you
.. i18n: automatically recalculate the cost price for the selected product. 
.. i18n: The cost price is calculated from the raw materials and the operations carried out 
.. i18n: (if the products have been manufactured internally, so that you have set their costs).
..

OpenERP supports a third method of updating the cost price of products.
This is through the button :guilabel:`Update` on the product form which lets you
automatically recalculate the cost price for the selected product. 
The cost price is calculated from the raw materials and the operations carried out 
(if the products have been manufactured internally, so that you have set their costs).

.. i18n: Margins by Product
.. i18n: ------------------
..

Margins by Product
------------------

.. i18n: .. index::
.. i18n:    single: module; product_margin
..

.. index::
   single: module; product_margin

.. i18n: To track margins by product, install the module :mod:`product_margin`. Once the module
.. i18n: is installed you can see the margins by product by using the menu :menuselection:`Sales --> Products
.. i18n: --> Product Margins`.
..

To track margins by product, install the module :mod:`product_margin`. Once the module
is installed you can see the margins by product by using the menu :menuselection:`Sales --> Products
--> Product Margins`.

.. i18n: When you have clicked the menu option concerned, OpenERP asks for an analysis period and the state of invoices (draft, open, paid). If
.. i18n: no period is given, OpenERP will calculate margins on all of the operations without restriction. By
.. i18n: default, however, OpenERP proposes a period of the last 12 months for analysis.
..

When you have clicked the menu option concerned, OpenERP asks for an analysis period and the state of invoices (draft, open, paid). If
no period is given, OpenERP will calculate margins on all of the operations without restriction. By
default, however, OpenERP proposes a period of the last 12 months for analysis.

.. i18n: You can also filter the analysis on certain types of invoice:
..

You can also filter the analysis on certain types of invoice:

.. i18n: * All invoices, including unvalidated draft invoices,
.. i18n: 
.. i18n: * All open and/or paid invoices,
.. i18n: 
.. i18n: * Paid invoices only.
..

* All invoices, including unvalidated draft invoices,

* All open and/or paid invoices,

* Paid invoices only.

.. i18n: .. figure:: images/product_margin_tree.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Product Margins*
..

.. figure:: images/product_margin_tree.png
   :scale: 75
   :align: center

   *Product Margins*

.. i18n: You then get a margin analysis table. The following fields are displayed for the sales of each product:
..

You then get a margin analysis table. The following fields are displayed for the sales of each product:

.. i18n: * :guilabel:`Avg. Unit Price`: the average unit sales price,
.. i18n: 
.. i18n: * :guilabel:`Catalog Price`: the list price based on this product,
.. i18n: 
.. i18n: * :guilabel:`# Invoiced`: the number of sold products that have been invoiced,
.. i18n: 
.. i18n: * :guilabel:`Sales Gap`: the difference between the revenue calculated from list price and volume, and the actual sales,
.. i18n: 
.. i18n: * :guilabel:`Turnover`: the actual sales revenue for the product selected,
.. i18n: 
.. i18n: * :guilabel:`Expected Sale`: the number of products sold multiplied by the list price.
..

* :guilabel:`Avg. Unit Price`: the average unit sales price,

* :guilabel:`Catalog Price`: the list price based on this product,

* :guilabel:`# Invoiced`: the number of sold products that have been invoiced,

* :guilabel:`Sales Gap`: the difference between the revenue calculated from list price and volume, and the actual sales,

* :guilabel:`Turnover`: the actual sales revenue for the product selected,

* :guilabel:`Expected Sale`: the number of products sold multiplied by the list price.

.. i18n: .. figure:: images/product_margin_form.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Margin Details for a Given Product*
..

.. figure:: images/product_margin_form.png
   :scale: 75
   :align: center

   *Margin Details for a Given Product*

.. i18n: The following fields are given by product for purchases:
..

The following fields are given by product for purchases:

.. i18n: * :guilabel:`Avg. Unit price` : the average unit purchase price,
.. i18n: 
.. i18n: * :guilabel:`Standard price` : the standard cost price of the product for the company,
.. i18n: 
.. i18n: * :guilabel:`# Invoiced` : the number of purchased products,
.. i18n: 
.. i18n: * :guilabel:`Purchase Gap`: the difference between the total actual cost and the standard cost
.. i18n:   multiplied by the number of units purchased,
.. i18n: 
.. i18n: * :guilabel:`Total Cost`: the total cost of purchases for the product under consideration,
.. i18n: 
.. i18n: * :guilabel:`Normal Cost`: the number of products sold multiplied by the standard cost price.
..

* :guilabel:`Avg. Unit price` : the average unit purchase price,

* :guilabel:`Standard price` : the standard cost price of the product for the company,

* :guilabel:`# Invoiced` : the number of purchased products,

* :guilabel:`Purchase Gap`: the difference between the total actual cost and the standard cost
  multiplied by the number of units purchased,

* :guilabel:`Total Cost`: the total cost of purchases for the product under consideration,

* :guilabel:`Normal Cost`: the number of products sold multiplied by the standard cost price.

.. i18n: The following fields are given by product for margins:
..

The following fields are given by product for margins:

.. i18n: * :guilabel:`Total Margin`,
.. i18n: 
.. i18n: * :guilabel:`Expected Margin`,
.. i18n: 
.. i18n: * :guilabel:`Total Margin in percent`,
.. i18n: 
.. i18n: * :guilabel:`Expected Margin in percent`.
..

* :guilabel:`Total Margin`,

* :guilabel:`Expected Margin`,

* :guilabel:`Total Margin in percent`,

* :guilabel:`Expected Margin in percent`.

.. i18n: Margins by Project
.. i18n: ------------------
..

Margins by Project
------------------

.. i18n: To manage margins by project, you should install the analytical accounts with management by task. The use
.. i18n: of these accounts is described in :ref:`ch-accts`.
..

To manage margins by project, you should install the analytical accounts with management by task. The use
of these accounts is described in :ref:`ch-accts`.

.. i18n: .. index::
.. i18n:    single: module; account_analytic_analysis
..

.. index::
   single: module; account_analytic_analysis

.. i18n: Install the module :mod:`account_analytic_analysis` and all of its dependencies. 
.. i18n: This module adds a tab on the analytic account form to handle the different margins in an analytic account 
.. i18n: representing a project or a case, and several new reports on those accounts.
..

Install the module :mod:`account_analytic_analysis` and all of its dependencies. 
This module adds a tab on the analytic account form to handle the different margins in an analytic account 
representing a project or a case, and several new reports on those accounts.

.. i18n: .. figure:: images/account_analytic_analysis_form.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Detail of margins for a case*
..

.. figure:: images/account_analytic_analysis_form.png
   :scale: 75
   :align: center

   *Detail of margins for a case*

.. i18n: Start by opening a project's analytic account through
.. i18n: :menuselection:`Project --> Billing --> Overpassed Accounts`
.. i18n: and selecting one of them.
.. i18n: In the form's :guilabel:`Analysis summary` tab you will find the following information:
..

Start by opening a project's analytic account through
:menuselection:`Project --> Billing --> Overpassed Accounts`
and selecting one of them.
In the form's :guilabel:`Analysis summary` tab you will find the following information:

.. i18n: * The total costs for the analytic account,
.. i18n: 
.. i18n: * The total amount of invoiced sales,
.. i18n: 
.. i18n: * The number of hours worked,
.. i18n: 
.. i18n: * The number of hours remaining to be worked,
.. i18n: 
.. i18n: * The remaining income,
.. i18n: 
.. i18n: * The theoretical income (hours worked multiplied by their sale price),
.. i18n: 
.. i18n: * The number of hours invoiced,
.. i18n: 
.. i18n: * The real income per hour,
.. i18n: 
.. i18n: * The real margin,
.. i18n: 
.. i18n: * The theoretical margin taking into account everything yet to be invoiced,
.. i18n: 
.. i18n: * The real margin rate in percent,
.. i18n: 
.. i18n: * The last invoicing date,
.. i18n: 
.. i18n: * The last worked hours,
.. i18n: 
.. i18n: * The number of hours remaining to be invoiced,
.. i18n: 
.. i18n: * The amount remaining to be invoiced.
..

* The total costs for the analytic account,

* The total amount of invoiced sales,

* The number of hours worked,

* The number of hours remaining to be worked,

* The remaining income,

* The theoretical income (hours worked multiplied by their sale price),

* The number of hours invoiced,

* The real income per hour,

* The real margin,

* The theoretical margin taking into account everything yet to be invoiced,

* The real margin rate in percent,

* The last invoicing date,

* The last worked hours,

* The number of hours remaining to be invoiced,

* The amount remaining to be invoiced.

.. i18n: For detailed information on the analytic account you can use any of the several reports available in
.. i18n: the toolbar to the right.
..

For detailed information on the analytic account you can use any of the several reports available in
the toolbar to the right.

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
