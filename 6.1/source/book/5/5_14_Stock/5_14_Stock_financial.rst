Financial Inventory Management
==============================

Manual and Real-time Stock Valuation
------------------------------------
If you have experience of managing with traditional software, you will know the problem of getting useful 
indicators. If you ask your accountant for a stock valuation or the value added by production, he will give you 
a figure.

If you ask for the same figure from your stores manager, you will get an entirely different amount. You have no
idea who is right!

In OpenERP, stock management is completely integrated with the accounts, to give strong coherence between 
the two systems. The double-entry structure of locations enables a very precise correspondence between
stocks and accounts.

Each stock movement also generates a corresponding accounting entry in an accounting journal to ensure that the
two systems can stay in permanent synchronization.

To do that, set up a general account for each location that should be valued in your accounts. If a product goes
to one location or another and the accounts are different in the two locations, OpenERP automatically generates 
the corresponding accounting entries in the accounts, in the stock journal.

If a stock move will go from a location without an account to a location where an account has been assigned (for
example goods receipt from a supplier order), OpenERP generates an accounting entry using the properties defined
in the product form for the counterpart. You can use different accounts per location or link several locations 
to the same account, depending on the level of analysis needed.

You use this system for managing consigned stocks:

* a supplier location that is valued in your own accounts or,
* a location in your own company that is not valued in your accounts.

*How to Configure Accounting Valuation?*

In the Product form, go to the ``Accounting`` tab and select the ``Real Time`` (automated) option for Inventory Valuation,

To define your accounts, you have two options. Set them on the product category, or on the product.

1. From the ``Accounting Stock Properties`` section, for the Product Category, set the ``Stock Input Account``, the ``Stock Output Account`` and the ``Stock Variation Account``,

2. From the ``Accounting`` tab, for the Product, set the ``Stock Input Account`` and the ``Stock Output Account``.

You can also overwrite the accounts from the Product or the Product Category by defining Stock Input Account
and Stock Output Account for a Location.

.. note:: account_anglo_saxon 
	
	You can also install the account_anglo_saxon module (Reconfigure wizard, Anglo-Saxon Accounting) to value
	your stock according to Anglo-saxon principles.
    
The figure below shows the various accounts that can be used, with and without the account_anglo_saxon
module installed.

.. figure:: images/account_anglo_saxon.png
	:scale: 80
	:align: center
	
	*Setting up Stock Valuation Accounts*
    
Managing Transportation Costs
-----------------------------

In OpenERP, you can handle the delivery methods when installing the :mod:`delivery` module.

This module will allow you:

* To select the delivery company

.. figure:: images/delivery_method_form.png
	:scale: 75
	:align: center
	
	*Define the Delivery Method*
	
* To define the delivery pricelist according to the price, the weight or the volume.

.. figure:: images/grid_lines.png
	:scale: 75
	:align: center
	
	*Define the Delivery Costs*

Now, in each :guilabel:`Delivery Order`, two new fields are available to enter the right 
value to deliver the products to the customer. You can also find a new field in the :guilabel:`Sales Order`
form that enables you to select a delivery method.

.. figure:: images/delivery_order_delivcost.png
	:scale: 75
	:align: center
	
	*Delivery Cost in the Delivery Orders*

.. figure:: images/sale_order_delivcost.png	
	:scale: 75
	:align: center
	
	*Delivery Method in the Sales Orders*

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

