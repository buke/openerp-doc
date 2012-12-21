.. i18n: Configuration Interface
.. i18n: =======================
..

 配置接口
=======================

.. i18n: The main goal of any user connecting to OpenObject BI is to fetch the data from database using the powerful MDX queries.
..

主要目标的任何用户连接到OpenObject BI是获取数据从数据库使用强大的MDX查询。

.. i18n: To run any MDX Query there is a need to make a cube and the user can define / configure their own custom cube using two interface : 
..

运行任何MDX查询需要作出一个立方体,用户可以定义/配置他们自己的自定义多维数据集使用两个接口:

.. i18n: .. _schema_configuration-link:
.. i18n: 
.. i18n: Introduction
.. i18n: ----------------------------------
..

.. _schema_configuration-link:

介绍
----------------------------------

.. i18n: By default the Cube Designer displays all schema in the tree form and provide options to add new schema:
..

默认情况下,立方体设计师显示所有模式在树形式和提供选项来添加新模式

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

创建模式:模式定义了数据库的数据被取出。它给了一个有意义的名称到数据库的连接:

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

    
数据库连接参数指定用于连接到数据库。它通常包含类型的数据库(postgres、oracle、mysql)、用户名、密码、数据库使用:

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

一旦我们配置数据库连接下一步是加载数据库使用内省。这将加载数据库的结构。通过结构我们意味着表、列和关系。这将帮助定义多维数据集很容易。随着结构被加载将没有对数据库的查询一次又一次的:

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

下一步是配置加载数据库。这是有用的隐藏不必要的表和列。如果数据库是OpenERP它可以自动配置:

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

 
一旦创建多维数据集模式是我们可以开始创建多维数据集:

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

  
立方体是结构,基于模式(数据库),它将配置如何检索数据:

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



多维数据集需要事实表定义。事实表是关键的表中存储,我们可以措施部门其他表的其他参数。例如,我们可以定义销售订单销售作为我们的事实表,因为它会给销售的细节。事实表的表可以加入。
事实表是给出一个有意义的名字:


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

 
这个立方体屏幕将会是:

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


我们可以决定在多维数据集的维度用于多维数据集。例如我们要看产品销售、日期、城市等方法分析了相应的销售。
我们决定要使用的措施,例如项目出售。所以我们可以决定维度和措施:


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

添加维度的产品。所以我们将能够看到产品明智的项目出售:

.. i18n: .. image::  images/10.png
.. i18n:    :scale: 65
..

.. image::  images/10.png
   :scale: 65

.. i18n: After dimension we explain how to get the products details in the hierarchy. That requires configuring the fact table:
..

我们将解释如何在维度获取产品详细信息的层次结构。这需要配置事实表:

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

在添加层次我们决定从哪个字段产品名称将:

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

完全配置多维数据集的树将看起来像:

.. i18n: .. image::  images/15.png
.. i18n:    :scale: 65
..

.. image::  images/15.png
   :scale: 65

.. i18n: Connecting to an Existing Database
.. i18n: ----------------------------------
..

连接至现有数据库
----------------------------------

.. i18n: One can very easily connect to an existing database. The details required are 
..

一个可以很容易地连接到一个现有的数据库。要求的细节是

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

生成的字符串,是一个连接字符串让连接到数据库。

.. i18n: Writing a Schema
.. i18n: ----------------
..

写作模式
----------------

.. i18n: .. describe::  What is Schema ?
..

.. describe::  What is Schema ?

.. i18n: Schema means shape or, more generally, plan. In the context of OpenObject BI it defines the logical model, consisting of cubes, hierarchies, and members, and a mapping of this model onto a physical model.
..

模式意味着形状,或更普遍而言,计划。上下文中的OpenObject BI它定义了逻辑模型,由立方体、层次结构和成员,和一个映射到该模型的物理模型。

.. i18n: The logical model consists of the constructs used to write queries in MDX language: cubes, dimensions, hierarchies, levels, and members.
..

逻辑模型包括构造用于编写查询MDX语言:立方体、维度、层次结构的水平,和成员。

.. i18n: The physical model is the source of the data which is presented through the logical model. It is typically a star schema, which is a set of tables in a relational database; later, we shall see examples of other kinds of mappings.
..

物理模型数据的来源,提出了逻辑模型。这通常是一个星型模式,这是一组关系数据库表中;之后,我们将看到其他类型的映射的例子。

.. i18n: Making Schema
.. i18n: +++++++++++++
..

制造模式
+++++++++++++

.. i18n: In OpenObject BI schemas are represented in a XML file. It can be designed in the way OpenERP does. The details of XML file can be seen at *Creating XML*
..

在OpenObject BI架构在一个XML文件表示。它可以被设计OpenERP的方式做。XML文件的细节可以看到在* *创建XML

.. i18n:         
..

        
