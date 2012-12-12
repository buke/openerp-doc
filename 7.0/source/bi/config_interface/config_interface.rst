Configuration Interface
=======================


The main goal of any user connecting to OpenObject BI is to fetch the data from database using the powerful MDX queries.

To run any MDX Query there is a need to make a cube and the user can define / configure their own custom cube using two interface : 

.. _schema_configuration-link:

Introduction
----------------------------------

By default the Cube Designer displays all schema in the tree form and provide options to add new schema:

.. image::  images/1.png
   :scale: 65

--------


Creating the Schema : Schema defines the database from where the data is to be fetched. It gives a meaningful name to the database connection:

.. image::  images/2.png
   :scale: 65
    
--------

    
Database Connection specifies the parameters for connecting to the database. It generally includes type of the database (postgres, oracle, mysql), username, password, database to use:

.. image::  images/3.png
   :scale: 65
        
--------


Once we configure the database connection the next step is to load the database using introspection. This will load the structure of the database. By structure we mean tables, columns and the relations. This will help in defining cube easily. As the structure is loaded there will be no query to the database again and again:

.. image::  images/4.png
   :scale: 65
        
--------


The next step is to configure the loaded database. This is useful to hide unnecessary table and columns. If database is from OpenERP it can be auto-configured:

.. image::  images/4a.png
   :scale: 65
       
--------

 
Once the cube schema is created we can start creating the cube:

.. image::  images/5.png
   :scale: 65
      
--------

  
Cube is the structure that is based on the schema (database), it will configure how to retrieve the data:

.. image::  images/6.png
   :scale: 65
        
--------


Cube requires the fact table to be defined. Fact tables are the key tables in which measures are stored and we can branch to other tables for other parameters. For example for sales we can define sale_order as our fact table as it will give the details of the sales. Fact table can be join of tables.
The fact table is given a meaningful name:

.. image::  images/7.png
   :scale: 65
       
--------

 
And the cube screen will be

.. image::  images/8.png
   :scale: 65
        
--------


After cube we can decide upon the dimensions to be used for the cube. For example we want to look on products sold, Dates, City etc. to analyse the sales accordingly.
We decide the measures to be used, for example items sold. So we can decide the dimension and measures:

.. image::  images/9.png
   :scale: 65
        
--------


Adding the dimension Products. So we will be able to see product wise item sold:

.. image::  images/10.png
   :scale: 65


After dimension we explain how to get the products details in the hierarchy. That requires configuring the fact table:

.. image::  images/12.png
   :scale: 65
        
--------


After adding the hierarchy  we decide from which field the product name will come:

.. image::  images/14.png
   :scale: 65
        
--------


The fully configured cube tree will look like:

.. image::  images/15.png
   :scale: 65

Connecting to an Existing Database
----------------------------------

One can very easily connect to an existing database. The details required are 


#. Fact Name : Logical Name of the database

#. Database Name: Physical Database name to be used

#. Database type : Type of the database it can be PostgreSQL, MySQL, Oracle etc.

#. Connection type : Port or Socket

#. Database Host : Server name like localhost

#. Database Port : Port to be used for making connection to the database

#. Database Login: Login name for accessing a database

#. Database Password:Password for the user in login

------

Giving this detail will generate a string like ''postgres://postgres:postgres@localhost:5432/terp''

------

Strings so generated is a connection string for making connection to the database.


Writing a Schema
----------------

.. describe::  What is Schema ?

Schema means shape or, more generally, plan. In the context of OpenObject BI it defines the logical model, consisting of cubes, hierarchies, and members, and a mapping of this model onto a physical model.

The logical model consists of the constructs used to write queries in MDX language: cubes, dimensions, hierarchies, levels, and members.

The physical model is the source of the data which is presented through the logical model. It is typically a star schema, which is a set of tables in a relational database; later, we shall see examples of other kinds of mappings.

Making Schema
+++++++++++++

In OpenObject BI schemas are represented in a XML file. It can be designed in the way OpenERP does. The details of XML file can be seen at *Creating XML*

        

