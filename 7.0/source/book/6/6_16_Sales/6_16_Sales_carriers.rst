
Management of Carriers
======================

.. index::
   single: delivery grid
   single: carriers
   single: module; delivery
   single: module; profile_manufacturing

To manage deliveries in OpenERP, you can install the :mod:`delivery` module.
To do that, use the :guilabel:`Reconfigure` wizard and select :guilabel:`Delivery Costs` under the :guilabel:`Sales Application Configuration` section for installation.

This module enables you to manage:

* the different carriers with whom you work,

* the different transport methods,

* cost calculation and invoicing of each delivery,

* the transport methods and their tariffs.

Once the :mod:`delivery` module has been installed, the first thing to do is to configure the different
modes of delivery accepted by your company. Go to the menu :menuselection:`Warehouse
--> Configuration --> Delivery --> Delivery Method` to create your company's delivery modes.

For each delivery mode, you should define the following elements:

* Name of the delivery mode,

* The partner associated with the transport (which can be your own company),

* The associated product.

Let's give you an example:

.. table:: Example Delivery Modes

   ================    ===============   ==========================
   Carrier             Carrier Partner   Delivery Product
   ================    ===============   ==========================
   Express Track       Mail Office       Express Track Delivery
   Priority Courier    Mail Office       Courier Express Delivery
   EFG Standard        EFG Inc           Delivery EFG
   EFG Express         EFG Inc           Delivery EFG Express
   ================    ===============   ==========================

Information about the invoicing of transport (such as accounts, applicable taxes) is entered in the
product linked to the delivery mode. Ideally the product should be configured with 
:guilabel:`Product Type` ``Service`` and :guilabel:`Procurement Method` ``Make to Stock``.

You can use the same product for several delivery modes. This simplifies the
configuration, but it has the disadvantage that you will not be able to separate your sales figures by delivery mode.

Tariff Grids
------------

Unlike ordinary products, delivery prices are not proposed through pricelists but through delivery grids,
designed specifically for this purpose. For each delivery mode, you enter one or several tariff grids.
Each grid is used for a given region/destination.

For example, for the postal tariffs for Priority Courier, you generally define the three tariff grids
for Mail Office:

* National Courier,

* Courier in Europe,

* Courier Outside Europe.

To define a new delivery grid, use the menu :menuselection:`Warehouse --> Configuration -->
Delivery --> Delivery Pricelist`. Give a name to your delivery grid and define the
region for which the tariffs in the grid will apply in the second tab
:guilabel:`Destination`. There you can set:

* A list of countries (for UK or Europe, for example),

* A list of states,

* A range of postal codes (for Paris you might have 75000 – 75900).

Then you have to set the rules for calculating the transport price in the first tab :guilabel:`Grid definition`.
First of all, give the rule a name. Then set the condition for which this rule is applicable, for
example ``Weight < 0.5kg``.

.. note:: Weights

   Weights are always expressed in kilograms. You can define a number with a decimal point or comma, so
   to set 500g you would put 0.5 in the weight rule.

Next you can set the sales price and the cost price. Prices can be expressed in various ways:

* a fixed price,

* a variable price, as a function of weight, volume, weight x volume or price.

For example, mailing within France using current tariffs would be defined as shown in the table below:

.. table:: Example Tariff Rules

   ==========  =============  =====   =============
   Name        Condition      Price   Price Type
   ==========  =============  =====   =============
   S           Weight < 3 kg  6.90    Fixed
   M           Weight < 5 kg  7.82    Fixed
   L           Weight < 6 kg  8.53    Fixed
   XL          Weight < 7 kg  9.87    Fixed
   ==========  =============  =====   =============

You can also define rules that depend on the total amount on the order. For example to offer fixed price
delivery if the total order amount is greater than 150 USD, add the following rule:

.. table:: Additional Tariff Rule

   ================= ===============  ======   =============
   Name              Condition        Price    Price Type
   ================= ===============  ======   =============
   Franked > 150 USD Price > 150 USD  10       Fixed
   ================= ===============  ======   =============

Delivery Modes
--------------

Once the delivery modes and their corresponding tariffs have been defined, you can use them in a Sales Order. 
There are two methods for doing that in OpenERP.

* Delivery based on Ordered Quantities,

* Delivery based on Shipped Quantities.

Delivery based on Ordered Quantities
------------------------------------

To add the delivery charges (or transport costs) to the quotation, use the button :guilabel:`Delivery Costs` available on the `Sales Order` tab of the form. A dialog box opens, asking you to select a delivery mode from the list available.

.. figure:: images/sale_delivery.png
   :scale: 75
   :align: center

   *Adding Transport Costs to an Order*

Once the delivery mode has been selected, OpenERP automatically adds a line to the quotation with
the amount calculated by the delivery function. This technique enables you to calculate the
delivery charge based on the order and then, separately, how the products will really be delivered
to the customer.

If you want to calculate the exact delivery charges depending on the actual deliveries, you must use
invoicing based on deliveries.

Delivery based on Shipped Quantities
------------------------------------

To invoice the delivery according to the items shipped, you set the delivery mode in the
:guilabel:`Delivery Method` field on the second tab of the order, :guilabel:`Other Information`, to :guilabel:`Invoice from Delivery`. 

You can then confirm the order, and when the goods are available you can also validate the delivery order.

The transport costs will not be added to the sales order, but only to the invoice.
When the manager has generated the invoices corresponding to the deliveries carried out,
OpenERP automatically adds a line on each invoice corresponding to the delivery charge, calculated
on the basis of the items actually sent.


.. Copyright © Open Object Press. All rights reserved.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the OpenERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. Published by Open Object Press, Grand Rosière, Belgium
