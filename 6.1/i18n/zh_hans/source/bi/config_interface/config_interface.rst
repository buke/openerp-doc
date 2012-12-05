
.. i18n: Configuration Interface
.. i18n: =======================
..

Configuration Interface
=======================

.. i18n: The main goal of any user connecting to OpenObject BI is to fetch the data from database using the powerful MDX queries.
..

The main goal of any user connecting to OpenObject BI is to fetch the data from database using the powerful MDX queries.

.. i18n: To run any MDX Query there is a need to make a cube and the user can define / configure their own custom cube using two interface : 
..

To run any MDX Query there is a need to make a cube and the user can define / configure their own custom cube using two interface : 

.. i18n: .. _schema_configuration-link:
.. i18n: 
.. i18n: Introduction
.. i18n: ----------------------------------
..

.. _schema_configuration-link:

Introduction
----------------------------------

.. i18n: By default the Cube Designer displays all schema in the tree form and provide options to add new schema:
..

By default the Cube Designer displays all schema in the tree form and provide options to add new schema:

.. i18n: .. image::  images/1.png
.. i18n:    :scale: 65
..

.. image::  images/1.png
   :scale: 65

.. i18n: --------
..

--------

.. i18n: Creating the Schema : Schema defines the database from where the data is to be fetched. It gives a meaningful name to the database connection:
..

Creating the Schema : Schema defines the database from where the data is to be fetched. It gives a meaningful name to the database connection:

.. i18n: .. image::  images/2.png
.. i18n:    :scale: 65
.. i18n:     
.. i18n: --------
.. i18n: 
.. i18n:     
.. i18n: Database Connection specifies the parameters for connecting to the database. It generally includes type of the database (postgres, oracle, mysql), username, password, database to use:
..

.. image::  images/2.png
   :scale: 65
    
--------

    
Database Connection specifies the parameters for connecting to the database. It generally includes type of the database (postgres, oracle, mysql), username, password, database to use:

.. i18n: .. image::  images/3.png
.. i18n:    :scale: 65
.. i18n:         
.. i18n: --------
..

.. image::  images/3.png
   :scale: 65
        
--------

.. i18n: Once we configure the database connection the next step is to load the database using introspection. This will load the structure of the database. By structure we mean tables, columns and the relations. This will help in defining cube easily. As the structure is loaded there will be no query to the database again and again:
..

Once we configure the database connection the next step is to load the database using introspection. This will load the structure of the database. By structure we mean tables, columns and the relations. This will help in defining cube easily. As the structure is loaded there will be no query to the database again and again:

.. i18n: .. image::  images/4.png
.. i18n:    :scale: 65
.. i18n:         
.. i18n: --------
..

.. image::  images/4.png
   :scale: 65
        
--------

.. i18n: The next step is to configure the loaded database. This is useful to hide unnecessary table and columns. If database is from OpenERP it can be auto-configured:
..

The next step is to configure the loaded database. This is useful to hide unnecessary table and columns. If database is from OpenERP it can be auto-configured:

.. i18n: .. image::  images/4a.png
.. i18n:    :scale: 65
.. i18n:        
.. i18n: --------
.. i18n: 
.. i18n:  
.. i18n: Once the cube schema is created we can start creating the cube:
..

.. image::  images/4a.png
   :scale: 65
       
--------

 
Once the cube schema is created we can start creating the cube:

.. i18n: .. image::  images/5.png
.. i18n:    :scale: 65
.. i18n:       
.. i18n: --------
.. i18n: 
.. i18n:   
.. i18n: Cube is the structure that is based on the schema (database), it will configure how to retrieve the data:
..

.. image::  images/5.png
   :scale: 65
      
--------

  
Cube is the structure that is based on the schema (database), it will configure how to retrieve the data:

.. i18n: .. image::  images/6.png
.. i18n:    :scale: 65
.. i18n:         
.. i18n: --------
..

.. image::  images/6.png
   :scale: 65
        
--------

.. i18n: Cube requires the fact table to be defined. Fact tables are the key tables in which measures are stored and we can branch to other tables for other parameters. For example for sales we can define sale_order as our fact table as it will give the details of the sales. Fact table can be join of tables.
.. i18n: The fact table is given a meaningful name:
..

Cube requires the fact table to be defined. Fact tables are the key tables in which measures are stored and we can branch to other tables for other parameters. For example for sales we can define sale_order as our fact table as it will give the details of the sales. Fact table can be join of tables.
The fact table is given a meaningful name:

.. i18n: .. image::  images/7.png
.. i18n:    :scale: 65
.. i18n:        
.. i18n: --------
.. i18n: 
.. i18n:  
.. i18n: And the cube screen will be
..

.. image::  images/7.png
   :scale: 65
       
--------

 
And the cube screen will be

.. i18n: .. image::  images/8.png
.. i18n:    :scale: 65
.. i18n:         
.. i18n: --------
..

.. image::  images/8.png
   :scale: 65
        
--------

.. i18n: After cube we can decide upon the dimensions to be used for the cube. For example we want to look on products sold, Dates, City etc. to analyse the sales accordingly.
.. i18n: We decide the measures to be used, for example items sold. So we can decide the dimension and measures:
..

After cube we can decide upon the dimensions to be used for the cube. For example we want to look on products sold, Dates, City etc. to analyse the sales accordingly.
We decide the measures to be used, for example items sold. So we can decide the dimension and measures:

.. i18n: .. image::  images/9.png
.. i18n:    :scale: 65
.. i18n:         
.. i18n: --------
..

.. image::  images/9.png
   :scale: 65
        
--------

.. i18n: Adding the dimension Products. So we will be able to see product wise item sold:
..

Adding the dimension Products. So we will be able to see product wise item sold:

.. i18n: .. image::  images/10.png
.. i18n:    :scale: 65
..

.. image::  images/10.png
   :scale: 65

.. i18n: After dimension we explain how to get the products details in the hierarchy. That requires configuring the fact table:
..

After dimension we explain how to get the products details in the hierarchy. That requires configuring the fact table:

.. i18n: .. image::  images/12.png
.. i18n:    :scale: 65
.. i18n:         
.. i18n: --------
..

.. image::  images/12.png
   :scale: 65
        
--------

.. i18n: After adding the hierarchy  we decide from which field the product name will come:
..

After adding the hierarchy  we decide from which field the product name will come:

.. i18n: .. image::  images/14.png
.. i18n:    :scale: 65
.. i18n:         
.. i18n: --------
..

.. image::  images/14.png
   :scale: 65
        
--------

.. i18n: The fully configured cube tree will look like:
..

The fully configured cube tree will look like:

.. i18n: .. image::  images/15.png
.. i18n:    :scale: 65
..

.. image::  images/15.png
   :scale: 65

.. i18n: Connecting to an Existing Database
.. i18n: ----------------------------------
..

Connecting to an Existing Database
----------------------------------

.. i18n: One can very easily connect to an existing database. The details required are 
..

One can very easily connect to an existing database. The details required are 

.. i18n: #. Fact Name : Logical Name of the database
.. i18n: 
.. i18n: #. Database Name: Physical Database name to be used
.. i18n: 
.. i18n: #. Database type : Type of the database it can be PostgreSQL, MySQL, Oracle etc.
.. i18n: 
.. i18n: #. Connection type : Port or Socket
.. i18n: 
.. i18n: #. Database Host : Server name like localhost
.. i18n: 
.. i18n: #. Database Port : Port to be used for making connection to the database
.. i18n: 
.. i18n: #. Database Login: Login name for accessing a database
.. i18n: 
.. i18n: #. Database Password:Password for the user in login
..

#. Fact Name : Logical Name of the database

#. Database Name: Physical Database name to be used

#. Database type : Type of the database it can be PostgreSQL, MySQL, Oracle etc.

#. Connection type : Port or Socket

#. Database Host : Server name like localhost

#. Database Port : Port to be used for making connection to the database

#. Database Login: Login name for accessing a database

#. Database Password:Password for the user in login

.. i18n: ------
..

------

.. i18n: Giving this detail will generate a string like ''postgres://postgres:postgres@localhost:5432/terp''
..

Giving this detail will generate a string like ''postgres://postgres:postgres@localhost:5432/terp''

.. i18n: ------
..

------

.. i18n: Strings so generated is a connection string for making connection to the database.
..

Strings so generated is a connection string for making connection to the database.

.. i18n: Writing a Schema
.. i18n: ----------------
..

Writing a Schema
----------------

.. i18n: .. describe::  What is Schema ?
..

.. describe::  What is Schema ?

.. i18n: Schema means shape or, more generally, plan. In the context of OpenObject BI it defines the logical model, consisting of cubes, hierarchies, and members, and a mapping of this model onto a physical model.
..

Schema means shape or, more generally, plan. In the context of OpenObject BI it defines the logical model, consisting of cubes, hierarchies, and members, and a mapping of this model onto a physical model.

.. i18n: The logical model consists of the constructs used to write queries in MDX language: cubes, dimensions, hierarchies, levels, and members.
..

The logical model consists of the constructs used to write queries in MDX language: cubes, dimensions, hierarchies, levels, and members.

.. i18n: The physical model is the source of the data which is presented through the logical model. It is typically a star schema, which is a set of tables in a relational database; later, we shall see examples of other kinds of mappings.
..

The physical model is the source of the data which is presented through the logical model. It is typically a star schema, which is a set of tables in a relational database; later, we shall see examples of other kinds of mappings.

.. i18n: Making Schema
.. i18n: +++++++++++++
..

Making Schema
+++++++++++++

.. i18n: In OpenObject BI schemas are represented in a XML file. It can be designed in the way OpenERP does. The details of XML file can be seen at *Creating XML*
..

In OpenObject BI schemas are represented in a XML file. It can be designed in the way OpenERP does. The details of XML file can be seen at *Creating XML*

.. i18n:         
..

        
