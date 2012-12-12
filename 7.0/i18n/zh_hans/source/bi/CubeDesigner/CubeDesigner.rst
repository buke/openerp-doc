
.. i18n: Goal of Cube Designer
.. i18n: =====================
..

Goal of Cube Designer
=====================

.. i18n: The goal is to develop a User Friendly Cube Designer for Open Object - BI that allows a user to define and / or modify an OLAP cube definition starting from any database. (Oracle, MySQL, PostgreSQL). This has to be user friendly so that a end-user can define his own cube on his own database without any development knowledge.
..

The goal is to develop a User Friendly Cube Designer for Open Object - BI that allows a user to define and / or modify an OLAP cube definition starting from any database. (Oracle, MySQL, PostgreSQL). This has to be user friendly so that a end-user can define his own cube on his own database without any development knowledge.

.. i18n: Basic features
.. i18n: --------------
..

Basic features
--------------

.. i18n: The cube designer of the OpenObject – BI Solutions helps users create new cubes and modify existing ones. Once the user is connected to the database they can create cubes in two ways 
.. i18n: #Wizard Flow
.. i18n: #Generic Flow. 
..

The cube designer of the OpenObject – BI Solutions helps users create new cubes and modify existing ones. Once the user is connected to the database they can create cubes in two ways 
#Wizard Flow
#Generic Flow. 

.. i18n: Wizard Flow
.. i18n: +++++++++++
..

Wizard Flow
+++++++++++

.. i18n: In the wizard flow a wizard guides the user through the entire process of cube creation. Navigation can be done through Next and Previous button.
..

In the wizard flow a wizard guides the user through the entire process of cube creation. Navigation can be done through Next and Previous button.

.. i18n: .. note::
.. i18n:         Clicking on the “Save” button on every form causes the data to be written in the database and simultaneously the  “Next” button is activated and the user is navigated to the next form.
.. i18n:         Next button will not be activated until the data is “Saved”.
..

.. note::
        Clicking on the “Save” button on every form causes the data to be written in the database and simultaneously the  “Next” button is activated and the user is navigated to the next form.
        Next button will not be activated until the data is “Saved”.

.. i18n: Generic Flow
.. i18n: ++++++++++++
..

Generic Flow
++++++++++++

.. i18n: The cube can be modified / created by the user in a normal way.
..

The cube can be modified / created by the user in a normal way.

.. i18n: :Modify / Create A Schema:
..

:Modify / Create A Schema:

.. i18n: The user specifies the desired schema name.
.. i18n: They select the desired database or create it with the help of [new].
.. i18n: They specify the schema description.
.. i18n: They save the schema.
..

The user specifies the desired schema name.
They select the desired database or create it with the help of [new].
They specify the schema description.
They save the schema.

.. i18n: :Modify / Create A Fact Table:
..

:Modify / Create A Fact Table:

.. i18n: User makes a particular Type for Fact table
.. i18n: They select the desired database or Schema for a particular Fact Table, or create one using the [new] button.
.. i18n:   
.. i18n: :Modify / Create A Database:
..

User makes a particular Type for Fact table
They select the desired database or Schema for a particular Fact Table, or create one using the [new] button.
  
:Modify / Create A Database:

.. i18n: User specifies the “General Parameters”
.. i18n: He specifies the “Connection Parameters” that specify which database and port number will be used for the connection.
.. i18n: He tests the connection for error and the “Connection URL” is generated.
.. i18n: On connection string being correct the new database is created.
..

User specifies the “General Parameters”
He specifies the “Connection Parameters” that specify which database and port number will be used for the connection.
He tests the connection for error and the “Connection URL” is generated.
On connection string being correct the new database is created.

.. i18n: :Modify / Create A Cube:
..

:Modify / Create A Cube:

.. i18n: The user provides desired cube name along with the fact tables and schema name.
.. i18n: The user can select previously created fact tables via a drop down box or can create a new fact table by clicking on [new].
.. i18n: Same goes for schema too.
.. i18n: The dimensions and measures will be empty as they have not yet been created.
..

The user provides desired cube name along with the fact tables and schema name.
The user can select previously created fact tables via a drop down box or can create a new fact table by clicking on [new].
Same goes for schema too.
The dimensions and measures will be empty as they have not yet been created.

.. i18n: :Modify / Create  A Dimension:
..

:Modify / Create  A Dimension:

.. i18n: The user provides the dimension name. 
.. i18n: The given cube name will appear in the drop down box. They can select a cube name from the list or create a new cube by clicking on [new]. 
.. i18n: Hierarchies are absent.
..

The user provides the dimension name. 
The given cube name will appear in the drop down box. They can select a cube name from the list or create a new cube by clicking on [new]. 
Hierarchies are absent.

.. i18n: :Modify / Create A Hierarchies:
..

:Modify / Create A Hierarchies:

.. i18n: The user provides the hierarchy name.
.. i18n: The dimension name will come in the dropdown box.
.. i18n: User can create a new dimension by clicking on [new]. 
.. i18n: User will provide the hierarchy field name, sequence, hierarchy type, all member and default member fields. 
.. i18n: User will give the fact table by selecting it from a drop down box or by creating a new fact table altogether by clicking on [new]
..

The user provides the hierarchy name.
The dimension name will come in the dropdown box.
User can create a new dimension by clicking on [new]. 
User will provide the hierarchy field name, sequence, hierarchy type, all member and default member fields. 
User will give the fact table by selecting it from a drop down box or by creating a new fact table altogether by clicking on [new]

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
