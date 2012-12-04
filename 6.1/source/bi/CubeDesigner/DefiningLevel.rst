
Defining Level
==============

:ref:`Level <level-link>` It specifies the actual data to be displayed. It
specifies the depth for the hierarchy. Now taking the same example for the
Products. We need it to be two level depth.

  #. Product Category
  #. Product Name

Lets start with making the levels. Details like hierarchy name, level name
filled by default according the schema we are in. We need to specify the column
to be used for filling the level. We open the column name and it will show all
the fields from tables defined in the hierarchy.  We select name from the
product category

.. image::  images/level1.png
   :scale: 65

We want more level for displaying the name of the products. In the column name
we will select the column name from the product_template. The main thing is to
change the sequence to 2. This will show the products category wise on the
browser.

.. image::  images/level1.png
   :scale: 65

