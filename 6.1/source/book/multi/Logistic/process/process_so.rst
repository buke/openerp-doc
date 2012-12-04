Sales Order
-----------

At this point, you have to login as a user of OpenERP France to make a Sales Order coming from a customer 
of this company.

.. figure:: images/sales_order_1tab.png
   :scale: 75
   :align: center
   
   *Defining a Sales Order*

You should not forget to set the correct parameters in the second tab `Other Information` to select the good shipping 
and picking policies. Here we select the `Invoice From the Picking` as ``Shipping Policy``. 

Confirm the Sales Order, then run the `Scheduler` (:menuselection:`Warehouses --> Schedulers --> Compute 
Schedulers`) and run the Procurement from each company (OpenERP France, OpenERP and OpenERP Belgium).

At this time, a `Purchase Order` and a `Delivery Order` have been generated. The Purchase Order is in the ``Request For 
Quotation`` state and you have to convert it into a Purchase Order to confirm the purchase. The Delivery Order is in ``Not Available`` state because you have to buy the products before delivery.

.. figure:: images/request_quotation.png
   :scale: 75
   :align: center
   
   *Purchase Order*

Once the purchase order has been confirmed and the reception is completed, we can process the delivery order.

Delivery Order
^^^^^^^^^^^^^^
Once the delivery order is processed, the products are sent to the customer and we can invoice the order from OpenERP 
France on the delivered quantities.

The delivery order will be processed from OpenERP Belgium. OpenERP Belgium is the company that manages the stock of products. 
This company is responsible for the delivery of the products to the final customers. However, the invoicing process will be 
handled by OpenERP France, because it is the company that received the order from the customer.

.. figure:: images/delivery_order.png
   :scale: 75
   :align: center
   
   *Deliver the Products*
   
From the user of OpenERP France, we can create the invoice for the order (:menuselection:`Sales --> Invoicing --> Lines 
to Invoice`), then pass the invoice from the Draft state to the Open state. To finalize the invoicing process, you have to 
go to :menuselection:`Accounting --> Customers --> Customers Invoices` to execute the payment process.

.. figure:: images/delivery_order_fr.png
   :scale: 75
   :align: center
   
   *Create the Invoice*
   
.. figure:: images/customer_invoice.png
   :scale: 75
   :align: center
   
   *Validate the Invoice*



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


