Goal of Cube Designer
=====================

The goal is to develop a User Friendly Cube Designer for Open Object - BI that allows a user to define and / or modify an OLAP cube definition starting from any database. (Oracle, MySQL, PostgreSQL). This has to be user friendly so that a end-user can define his own cube on his own database without any development knowledge.

Basic features
--------------

The cube designer of the OpenObject – BI Solutions helps users create new cubes and modify existing ones. Once the user is connected to the database they can create cubes in two ways 
#Wizard Flow
#Generic Flow. 

Wizard Flow
+++++++++++

In the wizard flow a wizard guides the user through the entire process of cube creation. Navigation can be done through Next and Previous button.

.. note::
        Clicking on the “Save” button on every form causes the data to be written in the database and simultaneously the  “Next” button is activated and the user is navigated to the next form.
        Next button will not be activated until the data is “Saved”.

Generic Flow
++++++++++++

The cube can be modified / created by the user in a normal way.

:Modify / Create A Schema:

The user specifies the desired schema name.
They select the desired database or create it with the help of [new].
They specify the schema description.
They save the schema.

:Modify / Create A Fact Table:

User makes a particular Type for Fact table
They select the desired database or Schema for a particular Fact Table, or create one using the [new] button.
  
:Modify / Create A Database:

User specifies the “General Parameters”
He specifies the “Connection Parameters” that specify which database and port number will be used for the connection.
He tests the connection for error and the “Connection URL” is generated.
On connection string being correct the new database is created.

:Modify / Create A Cube:

The user provides desired cube name along with the fact tables and schema name.
The user can select previously created fact tables via a drop down box or can create a new fact table by clicking on [new].
Same goes for schema too.
The dimensions and measures will be empty as they have not yet been created.


:Modify / Create  A Dimension:

The user provides the dimension name. 
The given cube name will appear in the drop down box. They can select a cube name from the list or create a new cube by clicking on [new]. 
Hierarchies are absent.

:Modify / Create A Hierarchies:

The user provides the hierarchy name.
The dimension name will come in the dropdown box.
User can create a new dimension by clicking on [new]. 
User will provide the hierarchy field name, sequence, hierarchy type, all member and default member fields. 
User will give the fact table by selecting it from a drop down box or by creating a new fact table altogether by clicking on [new]

:Modify / Create A Levels:

The user has to specify the level name, column name, column id, level class, table name, sequence and hierarchy.
Hierarchy will appear in the drop down box. 
He can create a new hierarchy by clicking on [new]. 

.. note::
        Clicking on the "Save" button on every form causes the data to be written in the database.
        Double Click on row opens modification window of respective record.

:Modify / Create  A Measures:

The user provides the Measure name. 
The given cube name will appear in the drop down box. They can select a cube name from the list or create a new cube by clicking on the [new]. 
It defines the all calculation / aggregation with fact column name.
Here all calculation / aggregation are interdependent with the fields of fact column name, aggregator, data type and format of string.

