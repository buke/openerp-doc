Defining Hierarchy
==================

:ref:`Hierarchy <hierarchy-link>` is the arrangements of objects, peoples etc .. in a ranked or some series. The hierarchy are the way of arranging the dimensions. 

It need the fact table. 

Lets take the Example of Products. 

We want our sales cube to work on the products - we want to see the products sold. We have divided the products into categories. So we will make the Product Hierarchy display products by category.

Lets see the new hierarchy. Some values, such as hierarchy name and dimension, may be set by default.

.. image::  images/hier1.png
   :scale: 65

We now define the fact table for the hierarchy. Relational column will show the all fields of the sale_order_line and sale_order as these are the fact tables for the cube. We select product_id from sale_order_line which is related to product_product

.. image::  images/hier2.png
   :scale: 65

We want to get both product name and category. We know the product_category will give category and product_template will give the name. 
Now the list is filtered accordingly for adding the join tables

.. image::  images/hier3.png
   :scale: 65

After selecting the product_tmpl_id we select the category table.

.. image::  images/hier4.png
   :scale: 65

So final fact table for the Product Category will be
 
.. image::  images/hier5.png
   :scale: 65
