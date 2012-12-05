
.. i18n: Defining Cube
.. i18n: =============
..

Defining Cube
=============

.. i18n: Cube as we discussed in :ref:`The Cube <cube-link>` 
..

Cube as we discussed in :ref:`The Cube <cube-link>` 

.. i18n: For making the cube we need
..

For making the cube we need

.. i18n: #. Cube Name : Meaningful name for the cube 
.. i18n: #. :ref:`Schema <schema-link>`: :ref:`Configuring Schema <schema_configuration-link>`
.. i18n: #. Query Logging : It will decides whether the query will be logged or not.
.. i18n: #. Fact Table : A table that contains the facts (measures) and the link to the other tables that in turn qualifies for the dimensions. The fact table can be a join of two or more tables.
..

#. Cube Name : Meaningful name for the cube 
#. :ref:`Schema <schema-link>`: :ref:`Configuring Schema <schema_configuration-link>`
#. Query Logging : It will decides whether the query will be logged or not.
#. Fact Table : A table that contains the facts (measures) and the link to the other tables that in turn qualifies for the dimensions. The fact table can be a join of two or more tables.

.. i18n: For example : 
.. i18n: To analyse the sales data we will take join of sale_order and sale_order_line as a fact table.
..

For example : 
To analyse the sales data we will take join of sale_order and sale_order_line as a fact table.

.. i18n: So we start making the cube. The screen shows the new cube window. The schema name will be filled by default depending on the schema we are browsing in the tree. The initial window will show the relational column for fact table which will open the search box of all the fact  table created so far.
..

So we start making the cube. The screen shows the new cube window. The schema name will be filled by default depending on the schema we are browsing in the tree. The initial window will show the relational column for fact table which will open the search box of all the fact  table created so far.

.. i18n: .. image::  images/cube1.png
.. i18n:    :scale: 65
..

.. image::  images/cube1.png
   :scale: 65

.. i18n: We create the new fact table. In the relational column it will show all the primary keys for all tables loaded in the introspection. 
.. i18n: We select sale_order_line table with primary key id. Once we are done with the selection we will join the table.
..

We create the new fact table. In the relational column it will show all the primary keys for all tables loaded in the introspection. 
We select sale_order_line table with primary key id. Once we are done with the selection we will join the table.

.. i18n: .. image::  images/cube2.png
.. i18n:    :scale: 65
..

.. image::  images/cube2.png
   :scale: 65

.. i18n: Join Table will open all the tables that are referenced from the sale_order_line, according to the table name from the relational column. We select order_id as it is the field related to the sale_order. Hence, we made the join of the sale_order_line and sale_order
..

Join Table will open all the tables that are referenced from the sale_order_line, according to the table name from the relational column. We select order_id as it is the field related to the sale_order. Hence, we made the join of the sale_order_line and sale_order

.. i18n: .. image::  images/cube3.png
.. i18n:    :scale: 65
..

.. image::  images/cube3.png
   :scale: 65

.. i18n: If we want more tables to be joined we can do that by adding more on Join Tables. Now the search will be on all the reference from sale_order and sale_order_line
..

If we want more tables to be joined we can do that by adding more on Join Tables. Now the search will be on all the reference from sale_order and sale_order_line

.. i18n: .. image::  images/cube4.png
.. i18n:    :scale: 65
..

.. image::  images/cube4.png
   :scale: 65

.. i18n: Finally the cube page will look like 
..

Finally the cube page will look like 

.. i18n: .. image::  images/cube5.png
.. i18n:    :scale: 65
..

.. image::  images/cube5.png
   :scale: 65
