.. i18n: Goal of Cube Designer
.. i18n: =====================
..

Goal of Cube Designer
=====================

.. i18n: The goal is to develop a User Friendly Cube Designer for Open Object - BI that allows a user to define and / or modify an OLAP cube definition starting from any database. (Oracle, MySQL, PostgreSQL). This has to be user friendly so that a end-user can define his own cube on his own database without any development knowledge.
..

目标是开发一个用户友好的立方体设计师为开放对象- BI,用户可以通过定义和/或修改一个OLAP多维数据集定义从任何数据库。(Oracle、MySQL、PostgreSQL)。这是用户友好的,这样一个终端用户可以定义自己的多维数据集在他自己的数据库没有任何发展知识。
.. i18n: Basic features
.. i18n: --------------
..

Basic features
--------------

.. i18n: The cube designer of the OpenObject – BI Solutions helps users create new cubes and modify existing ones. Once the user is connected to the database they can create cubes in two ways 
.. i18n: #Wizard Flow
.. i18n: #Generic Flow. 
..

这个立方体的设计师OpenObject - BI解决方案可以帮助用户创建新的多维数据集和修改现有的。一旦用户连接到数据库,他们可以以两种方式创建多维数据集
#Wizard Flow
#Generic Flow. 

.. i18n: Wizard Flow
.. i18n: +++++++++++
..

向导流
+++++++++++

.. i18n: In the wizard flow a wizard guides the user through the entire process of cube creation. Navigation can be done through Next and Previous button.
..

在向导中流动向导指导用户通过多维数据集创建的整个过程。导航可以通过一个和下一个按钮。

.. i18n: .. note::
.. i18n:         Clicking on the “Save” button on every form causes the data to be written in the database and simultaneously the  “Next” button is activated and the user is navigated to the next form.
.. i18n:         Next button will not be activated until the data is “Saved”.
..

.. note::
       点击“保存”按钮在每个表单使数据被写入数据库,同时“下一步”按钮被激活和用户导航到接下来的形式。Next按钮不会被激活,直到数据是“保存”。

.. i18n: Generic Flow
.. i18n: ++++++++++++
..

Generic Flow
++++++++++++

.. i18n: The cube can be modified / created by the user in a normal way.
..

多维数据集可以修改/用户创建的以正常方式。

.. i18n: :Modify / Create A Schema:
..

:Modify / Create A Schema:

.. i18n: The user specifies the desired schema name.
.. i18n: They select the desired database or create it with the help of [new].
.. i18n: They specify the schema description.
.. i18n: They save the schema.
..

用户指定所需的模式名称。
他们选择所需的数据库或创建的帮助[新]。
他们指定schema描述。
他们保存模式。


.. i18n: :Modify / Create A Fact Table:
..

:Modify / Create A Fact Table:

.. i18n: User makes a particular Type for Fact table
.. i18n: They select the desired database or Schema for a particular Fact Table, or create one using the [new] button.
.. i18n:   
.. i18n: :Modify / Create A Database:
..

用户做了一个特定类型的事实表
他们选择所需的数据库或模式为一个特定的事实表,或创建一个使用[new]按钮。
  
:Modify / Create A Database:

.. i18n: User specifies the “General Parameters”
.. i18n: He specifies the “Connection Parameters” that specify which database and port number will be used for the connection.
.. i18n: He tests the connection for error and the “Connection URL” is generated.
.. i18n: On connection string being correct the new database is created.
..


用户指定的“通用参数”
他指定了“连接参数”,指定哪个数据库和端口号将用于连接。
他测试连接错误和“连接URL”是生成的。
在连接字符串被正确创建新的数据库。


.. i18n: :Modify / Create A Cube:
..

:Modify / Create A Cube:

.. i18n: The user provides desired cube name along with the fact tables and schema name.
.. i18n: The user can select previously created fact tables via a drop down box or can create a new fact table by clicking on [new].
.. i18n: Same goes for schema too.
.. i18n: The dimensions and measures will be empty as they have not yet been created.
..



用户提供所需的多维数据集名称以及事实表和模式名称。
用户可以选择先前创建的事实表通过一个下拉框或创建一个新的事实表可以通过点击[new]。同样的模式太。

将维度和测度将是空的,因为他们没有被建立出来

.. i18n: :Modify / Create  A Dimension:
..

:Modify / Create  A Dimension:

.. i18n: The user provides the dimension name. 
.. i18n: The given cube name will appear in the drop down box. They can select a cube name from the list or create a new cube by clicking on [new]. 
.. i18n: Hierarchies are absent.
..

用户提供的维度名称。


给定的多维数据集的名字将出现在这个下拉框。他们可以选择一个多维数据集的名字从名单中或创建一个新的多维数据集通过点击[new]。
层次缺席
.

.. i18n: :Modify / Create A Hierarchies:
..

:Modify / Create A Hierarchies:

.. i18n: The user provides the hierarchy name.
.. i18n: The dimension name will come in the dropdown box.
.. i18n: User can create a new dimension by clicking on [new]. 
.. i18n: User will provide the hierarchy field name, sequence, hierarchy type, all member and default member fields. 
.. i18n: User will give the fact table by selecting it from a drop down box or by creating a new fact table altogether by clicking on [new]
..

用户提供的层次结构的名字
维度的名字将出现在这个下拉框。
用户可以创建一个新维度通过点击 [new]. 
用户将提供层次字段名、序列、层次结构类型,所有成员和默认成员字段. 
用户会给事实表中选择它从一个下拉框或通过创建一个新的事实表完全被点击 [new]

.. i18n: :Modify / Create A Levels:
..

:Modify / Create A Levels:

.. i18n: The user has to specify the level name, column name, column id, level class, table name, sequence and hierarchy.
.. i18n: Hierarchy will appear in the drop down box. 
.. i18n: He can create a new hierarchy by clicking on [new]. 
..

The user has to specify the level name, column name, column id, level class, table name, sequence and hierarchy.
Hierarchy will appear in the drop down box. 
He can create a new hierarchy by clicking on [new]. 

.. i18n: .. note::
.. i18n:         Clicking on the "Save" button on every form causes the data to be written in the database.
.. i18n:         Double Click on row opens modification window of respective record.
..

.. note::
        Clicking on the "Save" button on every form causes the data to be written in the database.
        Double Click on row opens modification window of respective record.

.. i18n: :Modify / Create  A Measures:
..

:Modify / Create  A Measures:

.. i18n: The user provides the Measure name. 
.. i18n: The given cube name will appear in the drop down box. They can select a cube name from the list or create a new cube by clicking on the [new]. 
.. i18n: It defines the all calculation / aggregation with fact column name.
.. i18n: Here all calculation / aggregation are interdependent with the fields of fact column name, aggregator, data type and format of string.
..

The user provides the Measure name. 
The given cube name will appear in the drop down box. They can select a cube name from the list or create a new cube by clicking on the [new]. 
It defines the all calculation / aggregation with fact column name.
Here all calculation / aggregation are interdependent with the fields of fact column name, aggregator, data type and format of string.
