
.. _part-multicompany:

#########################
Multi-Company Environment
#########################

This part of the book concentrates on the multi-company environment of OpenERP. From version 6.0 of OpenERP, you do not have to
install any additional modules to enable the multi-company environment. All components are included in the base modules. All you have to do to work in a multi-company environment, is add the Useability/Multi-Companies group to your user.

The multi-company environment allows you to manage operations from different companies with different warehouses, customers and suppliers, products, ...

In the following chapters, we will perform a complete order flow made by a customer in France that does not 
handle the stock, but delegates it to another company located in Belgium that will deliver the product to the customer.

In order to achieve this, we will follow the schema defined below.

.. figure:: Logistic/images/schema.png
   :scale: 100
   :align: center
   
   *Flow Schema*

To be able to manage the process, please install the following modules:
	* :mod:`sale`
	* :mod:`purchase`
	* :mod:`stock`
	* :mod:`stock_location`, *Reconfigure* wizard --> *Advanced route* (in order to be able to define pull & push flows)

.. toctree::
    :maxdepth: 2

    Logistic/index

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


