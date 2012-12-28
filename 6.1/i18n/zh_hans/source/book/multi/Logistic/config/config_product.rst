.. i18n: Product
.. i18n: -------
..

产品
-------

.. i18n: Definition
.. i18n: ^^^^^^^^^^
..

基础数据
^^^^^^^^^^

.. i18n: Now that we have defined the different actors, we can define our product that will be stored in Belgium and proposed to sell in
.. i18n: France. Go to :menuselection:`Sales --> Products --> Products` and create a new product with the following specifications:
..

目前我们可以定义不同的角色，可以将计划在法国销售的产品存储在比利时，进入菜单选项，选择销售->产品-> 然后根据下列的详细参数创建一个新产品

.. i18n: .. figure:: images/product.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n:    
.. i18n:    *Defining Products*
.. i18n:    
.. i18n: In the ``Suppliers`` tab, you can select the supplier defined above. In the tab ``Logistical Flows``, we will define 
.. i18n: the different flows in order to share the different objects between the companies. To order the product in Belgium from a sales order made in France, we will define a `Pull flow`.
..

.. figure:: images/product.png
   :scale: 75
   :align: center
   
   *Defining Products*
   
In the ``Suppliers`` tab, you can select the supplier defined above. In the tab ``Logistical Flows``, we will define 
the different flows in order to share the different objects between the companies. To order the product in Belgium from a sales order made in France, we will define a `Pull flow`.

.. i18n: Flows
.. i18n: ^^^^^
..

Flows
^^^^^

.. i18n: In our process, we have to create a pull flow, because the process begins with a need from OpenERP France. OpenERP France needs some 
.. i18n: products ordered by the customers.
..

In our process, we have to create a pull flow, because the process begins with a need from OpenERP France. OpenERP France needs some 
products ordered by the customers.

.. i18n: The flow will go through our two child companies. The starting point is OpenERP Belgium that will supply OpenERP France that will 
.. i18n: supply the goods to the customer.
..

The flow will go through our two child companies. The starting point is OpenERP Belgium that will supply OpenERP France that will 
supply the goods to the customer.

.. i18n: We can draw the process like this: Customer <-- [OpenERP France] <-- [OpenERP Belgium] <-- Supplier
..

We can draw the process like this: Customer <-- [OpenERP France] <-- [OpenERP Belgium] <-- Supplier

.. i18n: .. figure:: images/pull_flow_def.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n:    
.. i18n:    *Pull Flow Definition*
..

.. figure:: images/pull_flow_def.png
   :scale: 75
   :align: center
   
   *Pull Flow Definition*

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
