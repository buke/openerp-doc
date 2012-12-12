Creating your Products
----------------------

The :menuselection:`Sales --> Products` menu gives you access to the definition of products.
In OpenERP, `product` is used to define a raw material, a stockable product, a consumable or a service.

.. index::
   single: Product; Consumable

.. tip::  Consumables

	In OpenERP, a consumable is a physical product which is treated like a stockable product, with the exception
	that stock management is not taken into account by the system. You could buy it, deliver it or
	produce it, but OpenERP will always assume that there is enough of it in stock. Examples: nails, labels.

Open a product form to see its specific information. 

Price lists (:menuselection:`Sales --> Configuration --> Pricelists`) determine the purchase and selling prices and
adjustments derived from the use of different currencies. The :menuselection:`Default Purchase
Pricelist` uses the product's :guilabel:`Cost Price` field for the Purchase price to be calculated. The
:menuselection:`Public Pricelist` uses the product's :guilabel:`Sale Price` field to calculate the Sales price in quotations.

Price lists are extremely flexible and enable you to put a complete price management policy in place.
They are composed of simple rules that enable you to build up a rule set for most complex situations:
multiple discounts, selling prices based on purchase prices, price reductions, promotions on product ranges and so on.

To start, define the following product:

.. table:: Product Definition

   ==================== ======================
   Field                Value
   ==================== ======================
   Name                 Central Heating Type 1
   Reference            CCT1
   Product Type         Stockable Product
   Supply Method        Buy
   ==================== ======================

From the menu :menuselection:`Sales --> Product --> Products`, click :guilabel:`New` to define a new product.

.. figure:: images/stock_product.png
   :scale: 75
   :align: center

   *Defining a New Product*

Three fields are important when you are configuring a new product:

* :guilabel:`Product Type`,

* :guilabel:`Procurement Method`,

* :guilabel:`Supply Method`.

Using the Correct Product Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The product type indicates whether the product is handled in stock management and if OpenERP manages its
procurement. The three distinct product types are:

* :guilabel:`Stockable Product`: this product is used in stock management and its replenishment is
  more or less automated as defined by the rules established in the system. For these products, we have to know
  how many pieces we have in stock. Examples: a bicycle, a computer or a central heating system.

* :guilabel:`Consumable`: This product is handled in stock management, you can receive it, deliver it and produce it.
  However, its stock level is not managed by the system. OpenERP assumes that you have got sufficient levels
  in stock at all times, so it does not restock it automatically. Example: nails, labels.

* :guilabel:`Service`: It does not appear in the various stock operations. Example: a consulting
  service.

Procurement Methods – Make to Stock and Make to Order
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The procurement method determines how the product will be replenished:

* :guilabel:`Make to Stock`: your customers are supplied from available stock. If the quantities in stock are
  too low to fulfil the order, a Purchase Order (according the minimum stock rules) will be generated in order 
  to get the products required. Example: a classic distributor.

* :guilabel:`Make to Order`: when a customer order is confirmed, you procure or manufacture
  the products for this order. A customer order 'Make to Order' will not modify stock in the medium term
  because you restock with the exact amount that was ordered. Example: computers from a large supplier
  assembled on demand.

You find a mix of these two modes used for the different final and intermediate products in most
industries. The procurement method shown on the product form is a default value for the order,
enabling the salesperson to choose the best mode for fulfilling a particular order by varying the
sales order parameters as needed.

The figures :ref:`fig-stfrst` and :ref:`fig-stfrord` show the change of stock levels for one product
managed as `Make to Order` and another managed as `Make to Stock`. The two figures are taken from OpenERP's 
:guilabel:`Stock Level Forecast` report, available from the product form.

.. _fig-stfrst:

.. figure:: images/stock_from_stock.png
   :scale: 65
   :align: center

   *Change in Stock for a  Make to Stock Product*

.. _fig-stfrord:

.. figure:: images/stock_from_order.png
   :scale: 65
   :align: center

   *Change in Stock for a Make to Order Product*

.. note:: Logistical Methods

   The :guilabel:`Make to Stock` logistical approach is usually used for high volumes and when the
   demand is seasonal or otherwise easy to forecast.
   The :guilabel:`Make to Order` approach is used for products that are measured, or very expensive to
   stock or have a short restocking time.

Choosing Supply Methods
^^^^^^^^^^^^^^^^^^^^^^^

OpenERP supports two supply methods:

* Produce: when the product is manufactured or the service is supplied from internal resources.

* Buy: when the product is bought from a supplier.

These are just the default settings used by the system during automated replenishment. The same
product can be either manufactured internally or bought from a supplier.

These three fields (:guilabel:`Supply Method`, :guilabel:`Procurement Method`, :guilabel:`Product
Type`) determine the system's behaviour when a product is required. The system will generate
different documents depending on the configuration of these three fields.

Figure :ref:`fig-stflow` illustrates different cases for automatic procurement.

.. _fig-stflow:

.. figure:: images/stock_flow.png
   :scale: 80
   :align: center

   *Workflow for Automatic Procurement, depending on the Product Configuration*

.. index::
   single: unit of measure
   single: UoM

Understanding Units of Measure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

OpenERP supports several units of measure. Quantities of the same product can be expressed in
several units of measure at once. For example, you can buy grain by the tonne and resell it by kg.
You just have to make sure that all the units of measure used for a product are in the same units of
measure category.

.. note:: Categories of Units of Measure

   All units of measure in the same category are convertible from one unit to another.

The table below shows some examples of units of measure and their category. The factor is used to
convert from one unit of measure to another as long as they are in the same category.

.. table:: Example Units of Measure

   ========= ============ ====== =========
   UoM       Category     Ratio  UoM Type
   ========= ============ ====== =========
   Kg        Weight            1 Reference       
   Gram      Weight         1000   Smaller
   Tonne     Weight         1000    Bigger
   Hour      Working time      8   Smaller
   Day       Working time      1 Reference
   Half-day  Working time      4   Smaller
   Item      Unit              1
   100 Items Unit           0.01
   ========= ============ ====== =========

Depending on the table above, you have 1Kg = 1000g = 0.001 Tonnes. A product in the ``Weight``
category could be expressed in Kg, Tonnes or Grammes. You cannot express it in hours or pieces, for example.

Use the menu :menuselection:`Sales --> Configuration --> Products -->  Units of Measure --> Units of Measure`
to define a new unit of measure.

In the definition of a Unit of Measure, you have a :guilabel:`Rounding precision` factor which shows how
amounts are rounded after the conversion. A value of 1 gives rounding to the level of one unit. 0.01
gives rounding to one hundredth.

.. note::  Secondary Units

   OpenERP supports double units of measure.
   Notice however that the default unit of measure and the purchase unit of measure have to be in the same category.
   Only the sales unit of measure may be in a different category.

   This is very useful in the agro-food industry, for example: you sell ham by the piece but invoice
   by the Kg.
   A weighing operation is needed before invoicing the customer.

To activate the management options for double units of measure, assign the group :guilabel:`Useability /
Product UoS View` to your user.

In this case, the same product can be expressed in two units of measure belonging to different
categories for sales and stock/purchase. You can then distinguish between the unit of stock management (the piece) and the unit
of invoicing or sales (kg).

In the product form you can then set one unit of measure for sales and stock management, and one
unit of measure for purchases.

For each operation on a product, you can use another unit of
measure, as long as it can be found in the same category as the two units already defined. If you
use another unit of measure, OpenERP automatically handles the conversion of prices and quantities.

So if you have 430 Kg of carrots at 5.30 EUR/Kg, OpenERP will automatically make the conversion if
you want to sell in tonnes – 0.43 tonnes at 5300 EUR / tonne. If you had set a rounding factor of
0.1 for the :guilabel:`tonne` unit of measure, OpenERP will tell you that you have only 0.4 tonnes
available.

The :menuselection:`Sales --> Products` menu allows you to create new products and update existing products.

Categorizing your Products
^^^^^^^^^^^^^^^^^^^^^^^^^^

Unlike partner categories (as explained in chapter :ref:`partner-categ`) and their assigned partners, product categories do have an effect on the products assigned to them - and a product may only belong to one category. Product categories are linked to accounting and they determine the default income / expense account when invoicing. For a CRM point of view, categories will be very useful to group your sales information in a different way.

Suppose you would like to have product categories that correspond to your product lines (or your lines of business). With such a category tree structure, you can easily track your opportunities and forecast per product line. Go to the `Reporting` menu, and open the `Sales Analysis` screen to group your quotations and sales orders by category of products.

You can define new product categories from the :menuselection:`Sales --> Sales --> Configuration --> Product --> Products Categories`, and also directly from the `Product` form.

From the :menuselection:`Sales --> Product --> Products by Category` menu, you get an overview of all product categories according to their tree structure. To see the products linked to a particular category, simply unfold and/or click the product concerned. All products from that category will be displayed. 

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

