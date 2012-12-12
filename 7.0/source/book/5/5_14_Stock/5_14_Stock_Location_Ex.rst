Stock Location Example
++++++++++++++++++++++

In this section, we will develop a more detailed example that includes different concepts seen
in the previous sections. 

The following example will use the *Stock Location types*, the *Logistic Flows* and the *Bill Of
Materials*.

We have two companies: OpenERP SA and OpenERP US.

We have three products: Product A, Product B and Product C. For each product, we will have to define
the Stock Location to determine where to take these products.

To make one unit of Product A, we need the Product B and the Product C. So we will have to define a 
*Bill of Material*.


.. table:: Bill of Materials

   =========== ==========
   Field       Value
   =========== ==========
   Product     Product A
   Product Qty 1
   Name        Product A
   BoM Type    Normal
   Company     OpenERP US
   =========== ==========

The different components to produce one unit of Product A are one unit of Product B
and one unit of Product C.

.. table:: Companies and Products
   
   ========== =====================
   Company    What
   ========== =====================
   OpenERP SA Sell the Product A
   OpenERP SA Store the Product C
   OpenERP US Produce the Product A
   OpenERP US Store the Product B
   ========== =====================
              
.. table:: Logistics Flows

   ======================== ==== ========= ======================================================
   Name                     Type Product   Goal of the flow
   ======================== ==== ========= ======================================================
   Ask for Production       Pull Product A OpenERP SA asks OpenERP US to produce the Product A
   Launch Production        Pull Product A OpenERP US launches the production of the Product A
   Send Product to Transit  Pull Product C OpenERP US asks for the Product C to OpenERP SA
   Get Product from Transit Pull Product C OpenERP US receives the Product C
   ======================== ==== ========= ======================================================
   
Here are the details of the different flows:

.. figure:: images/ask_production.png
	:scale: 75
	:align: center
	
	*Ask for Production*
	
.. figure:: images/launch_production.png
	:scale: 75
	:align: center
	
	*Launch Production*	
	
.. figure:: images/send_transit.png
	:scale: 75
	:align: center
	
	*Send Product to Transit*	

.. figure:: images/get_transit.png
	:scale: 75
	:align: center
	
	*Get Product from Transit*

With this configuration, when a Sales Order for 3 units of Product A is confirmed and the scheduler has been launched,
you will have the following procurements:

.. figure:: images/procurement.png
	:scale: 90
	:align: center
	
	*Procurements View*
	
And the following stock moves have been generated:

.. figure:: images/stock_moves_ex.png
	:scale: 90
	:align: center
	
	*Stock Moves*

Because we are working in two different companies, different stock moves have been generated. The products have to move 
from OpenERP SA to OpenERP US for the products C. After the manufacturing process, the products A have to move from
OpenERP US to OpenERP SA to be sold to the customer.

Once you have confirmed the different moves for the products B and C, the Manufacturing Order is in `ready to produce`
status. So you can run the production of the three units of Product A.

.. figure:: images/start_production.png
	:scale: 75
	:align: center
	
	*Launch the Production*

Once again due to the use of two companies, you have to confirm different deliveries. One to deliver the product 
from OpenERP US to OpenERP SA and another to deliver the product from OpenERP SA to the customer.
Now you have to confirm the delivery of the three units from OpenERP US to OpenERP SA, then to confirm the 
reception of the products in OpenERP SA and finally, deliver the products to you final customer.	

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
