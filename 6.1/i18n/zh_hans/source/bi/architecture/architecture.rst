.. i18n: Schema
.. i18n: ======
..

架构
======

.. i18n: .. image::  images/Bi_arch.png
..

.. image::  images/Bi_arch.png

.. i18n: Components
.. i18n: ==========
..

组件
==========

.. i18n: The Cube
.. i18n: --------
..

The Cube
--------

.. i18n: The cube is based of the following component:
..

cube 基于以下组件:

.. i18n: * A MDX parser that will transform an MDX expression to RDBMs queries:
.. i18n:         - Computed using a mix of:
.. i18n:                 + Using star flow snake as in mondrian (based on joins)
.. i18n:                 + Using space hierarchy cutting like in cubulus
.. i18n: * A memory cache system
.. i18n:         - On space hierarchies (dimensions with space cutting)
.. i18n: * An aggregation system
.. i18n:         - Ability to create aggregated table to speed up all queries (automatic or user-defined)
.. i18n:         - Queries will be computed on fact tables or aggregated tables
.. i18n: * A MDX Output (or several) to output the result
..

* MDX解析器将把MDX表达式转换为RDBMs查询:
        - 使用交叉混合计算:
                + 使用星型/雪花模式，在mondrian里 (基于joins)
                + 使用空间层次切割，比如在cubulus里
* 内存缓存系统
        - 空间层次 (空间纬度切割)
* 聚合系统
        - 能够创建汇总表，以加快查询速度 (自动的或者用户定义的)
        - 查询将计算事实数据表或汇总表
* 一条（或几条）MDX 输出结果

.. i18n: The cube will use:
..

cube将使用:

.. i18n: * SQLAlchemy for all database communications
.. i18n: 
.. i18n: * XML-RPC for his external interfaces
.. i18n: 
.. i18n: * PyParser for MDX parsing
..

* 所有数据库通信：SQLAlchemy 

* 扩展接口：XML-RPC

* MDX解析：PyParser

.. i18n: The CLI interface
.. i18n: -----------------
..

CLI 接口 
-----------------

.. i18n: Allows user to test MDX queries in this CLI command line interface. Simple script in python
.. i18n: that will send XML-RPC queries and print the result.
..

CLI命令行接口允许用户测试MDX查询. 简单的python脚本
将发送XML -RPC查询并显示出结果.

.. i18n: The Cube Definition
.. i18n: -------------------
..

Cube 定义
-------------------

.. i18n: The meta data of the cube definition will be stored in the OpenERP database. The user interface
.. i18n: to edit cubes is in OpenERP. We will use the same concept of the one defined in the ... XML standard. So that we will be able, in a future phase, to import such files.
..

定义Cube的元数据将被保存在OpenERP的数据库里.在OpenERP里通过用户界面去编辑Cube. 我们将使用一个相同的概念定义在标准的XML文件里. 因此，我们将能够在将来某阶段，导入这种文件.

.. i18n: This must not depend on any module of OpenERP so that if you want to use the BI library independently, you may not use OpenERP if cubes are defined. If cubes are not defined, you just install the minimal version of OpenERP that includes: the olap module, user management, workflow managements, access rights management, ... (the base module)
..

这必须不依赖OpenERP的任何模块，所以，假如Cubes已经定义，如果你想独立使用BI库，您可能无法使用OpenERP，假如Cubes还没有定义,你只需要最小安装OpenERP其中包括：olap 模块、用户管理、工作流管理、,账户权限管理, ... (这些基本模块)

.. i18n: The goal is that the user never have to create the cubes himself. We will create a wizard that 
.. i18n: will compute cubes based on introspection on the RDBM's. The steps of this wizard:
..

我们的目标是用户没有自己建立cubes. 我们将创建一个来计算基于RDBM's的cubes向导反思. 步骤向导:

.. i18n: * Selection of the database (type of db, then selection box like in the login of OpenERP)
.. i18n: 
.. i18n: * Selection of the factable (selection box)
.. i18n: 
.. i18n: * Selection of the measures and their attributes (selection box, aggregation func)
.. i18n: 
.. i18n: * Selection of the dimensions (click on a tree structure)
..

* 选择数据库 (数据库类型, 像OpenERP的登录选择框)

* 选择事实表 (选择框)

* 选择度量和他们的属性 (选择框, 聚合功能)

* 选举纬度 (点击树状结构)

.. i18n: Then it's done, the cube is computed. The aggregated table may be also automatically computed by OpenERP.
..

然后便已完成, cube 已经被计算. 聚合表也已经被 OpenERP自动计算完成.

.. i18n: The goal is to create new cube on the fly from the OpenERP client on every object, on user demand. This will also server the online demo server.
..

我们的目标是当用户需要从OpenERP的任意对象建立一个新的cube，也将作为在线演示服务器服务.

.. i18n: The cube creation can be stored in the server of kept in memory for one time usage.
..

创建的Cube可以被存储在服务器内存一段时间.

.. i18n: The Web Client
.. i18n: --------------
..

Web 客户端
--------------

.. i18n: The web client is a web-server that display cubes and provide tools to browse them, it must provide at least these operations:
..

Web客户端是一个Web服务，显示浏览cubes和提供浏览工具，它必须至少提供以下操作:

.. i18n: * switch view
.. i18n: 
.. i18n: * different type of charts
.. i18n: 
.. i18n: * drill up/down
.. i18n: 
.. i18n: * slice
.. i18n: 
.. i18n: * dice
..

* 切换视图

* 不同类型的图表

* 乡下钻取

* 切片

* 切块

.. i18n: The OpenOffice plugin
.. i18n: ---------------------
..

OpenOffice 插件
---------------------

.. i18n: Similar to Palo but all operation of construction and manipulation of cubes remains in OpenERP to limit development on OOo. The development on OOo just contains functions to:
..

Similar to Palo but all operation of construction and manipulation of cubes remains in OpenERP to limit development on OOo. The development on OOo just contains functions to:

.. i18n: * Insert new data (based on selection of dimensions and filters)
.. i18n: 
.. i18n: * Drill up/down functions
.. i18n: 
.. i18n: * Slice function
..

* Insert new data (based on selection of dimensions and filters)

* Drill up/down functions

* Slice function

.. i18n: The OpenERP interface
.. i18n: -----------------------
..

OpenERP 接口
-----------------------

.. i18n: From OpenERP, you should be able to right click/drag and drop any field to trigger the cube definition wizard to create your own cube on demand. For this, we will use the web client of the bi system.
..

From OpenERP, you should be able to right click/drag and drop any field to trigger the cube definition wizard to create your own cube on demand. For this, we will use the web client of the bi system.

.. i18n: We will integrate this on the gtk and web clients of OpenERP. The GTK client will open the browser to browse the cube.
..

We will integrate this on the gtk and web clients of OpenERP. The GTK client will open the browser to browse the cube.

.. i18n: Extra libraries
.. i18n: ===============
..

额外的库 
===============

.. i18n: Libraries we will use:
..

我们将使用以下库:

.. i18n: * Turbogears for the web client to browse cube
.. i18n: 
.. i18n: * Mathplotlib for rendering graphs
.. i18n: 
.. i18n: * PyParsing to parse MDX Expressions
.. i18n: 
.. i18n: * SQLAlchemy to construct SQL queries and RDBMS connections
.. i18n: 
.. i18n: * XMLRPC lib for communication with the cube server
.. i18n: 
.. i18n: * PÿUNO for the OOo integration
..

* Cube浏览Web客户端：Turbogears

* 图形渲染：Mathplotlib

* MDX表达式解析：PyParsing

* SQL 查询创建和RDBMS 连接：SQLAlchemy 

* Cube服务器通信：XMLRPC

* OOo整合：PÿUNO 

.. i18n: We will use an object relational mapping system on all objects: dimensions, ...
..

我们将在所有的对象上使用对象关系映射系统: 纬度, ...
