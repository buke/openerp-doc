
.. i18n: Creating Cube Definition using XML file
.. i18n: =======================================
..

Creating Cube Definition using XML file
=======================================

.. i18n: .. describe:: Things to know
..

.. describe:: Things to know

.. i18n: Before going through XML details it is good to have an idea of all :ref:`Terminologies <terminologies-link>`  of OLAP.
..

Before going through XML details it is good to have an idea of all :ref:`Terminologies <terminologies-link>`  of OLAP.

.. i18n: **Lets understand XML file in detail**
..

**Lets understand XML file in detail**

.. i18n: **Step: 1. The first step is to specify the database to use with parameters such as name, database name , database login and database password**
..

**Step: 1. The first step is to specify the database to use with parameters such as name, database name , database login and database password**

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:    <record model="olap.fact.database" id="fact_databases_BI">
.. i18n:   	<field name="name">Tiny ERP databases</field>
.. i18n:   	<field name="db_name">Sales</field>
.. i18n:   	<field name="db_login">postgres</field>
.. i18n:   	<field name="db_password">postgres</field>
.. i18n:    </record>
..

.. code-block:: xml

   <record model="olap.fact.database" id="fact_databases_BI">
  	<field name="name">Tiny ERP databases</field>
  	<field name="db_name">Sales</field>
  	<field name="db_login">postgres</field>
  	<field name="db_password">postgres</field>
   </record>

.. i18n: * This will create the parameters needed to connect to the database.
..

* This will create the parameters needed to connect to the database.

.. i18n: **Step: 2. Defining Schema**
..

**Step: 2. Defining Schema**

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:    <record model="olap.schema" id="schema_main_sales">
.. i18n:   	<field name="name">tinysales</field>
.. i18n:   	<field name="state">none</field>
.. i18n:   	<field name="database_id" ref="fact_databases_BI"/>
.. i18n:    </record>
..

.. code-block:: xml

   <record model="olap.schema" id="schema_main_sales">
  	<field name="name">tinysales</field>
  	<field name="state">none</field>
  	<field name="database_id" ref="fact_databases_BI"/>
   </record>

.. i18n: * This will create schema name tinysales for fact_database_BI made in step 1
..

* This will create schema name tinysales for fact_database_BI made in step 1

.. i18n: **Step: 3. Defining fact table to be used (In this case, sale_order_line)**
..

**Step: 3. Defining fact table to be used (In this case, sale_order_line)**

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:    <record model="olap.cube.table" id="table_sales_order_line">
.. i18n:   	<field name="name">sale_order_line</field>
.. i18n:         	<field name='schema_id' ref='schema_main_sales'/>
.. i18n:    </record>
..

.. code-block:: xml

   <record model="olap.cube.table" id="table_sales_order_line">
  	<field name="name">sale_order_line</field>
        	<field name='schema_id' ref='schema_main_sales'/>
   </record>

.. i18n: **Step: 4. Making Cube on fact_table**
..

**Step: 4. Making Cube on fact_table**

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:    <record model="olap.cube" id="cube_sales_order_line">
.. i18n:   	<field name="name">sale_order_line</field>
.. i18n:   	<field name="table_id" ref="table_sales_order_line"/>
.. i18n:   	<field name="schema_id" ref="schema_main_sales"/>
.. i18n:    </record>
..

.. code-block:: xml

   <record model="olap.cube" id="cube_sales_order_line">
  	<field name="name">sale_order_line</field>
  	<field name="table_id" ref="table_sales_order_line"/>
  	<field name="schema_id" ref="schema_main_sales"/>
   </record>

.. i18n: * This will create the cube named sale_order_line 
..

* This will create the cube named sale_order_line 

.. i18n: **Step: 5. Creating Dimension product**
..

**Step: 5. Creating Dimension product**

.. i18n: * This will be used to fetch and make MDX Query on all the product 
..

* This will be used to fetch and make MDX Query on all the product 

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:    <record model="olap.dimension" id="dimension_product_template">
.. i18n: 	<field name="name">Products</field>
.. i18n: 	<field name="cube_id" ref="cube_sales_order_line"/>
.. i18n:   </record>
.. i18n: 
.. i18n:    <record model="olap.cube.table" id="table_product_template">
.. i18n:   	<field name="name">product_product</field>
.. i18n:    </record>
..

.. code-block:: xml

   <record model="olap.dimension" id="dimension_product_template">
	<field name="name">Products</field>
	<field name="cube_id" ref="cube_sales_order_line"/>
  </record>

   <record model="olap.cube.table" id="table_product_template">
  	<field name="name">product_product</field>
   </record>

.. i18n: **Step: 5a. Creating Hierarchy for the Dimension Product**
..

**Step: 5a. Creating Hierarchy for the Dimension Product**

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:    <record model="olap.hierarchy" id="hierarchy_product_template">
.. i18n: 	<field name="name">All Products</field>
.. i18n: 	<field name="dimension_id" ref="dimension_product_template"/>
.. i18n: 	<field name="primary_key_table">product_product</field>
.. i18n: 	<field name="table_id" ref="table_product_template"/>
.. i18n:   </record>
..

.. code-block:: xml

   <record model="olap.hierarchy" id="hierarchy_product_template">
	<field name="name">All Products</field>
	<field name="dimension_id" ref="dimension_product_template"/>
	<field name="primary_key_table">product_product</field>
	<field name="table_id" ref="table_product_template"/>
  </record>

.. i18n: **Step: 5b  Creating Level for the Dimension Product**
..

**Step: 5b  Creating Level for the Dimension Product**

.. i18n: First, we create column.
..

First, we create column.

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n: 	<record model="olap.database.columns" id="columns_product_product_default_code">
.. i18n: 		<field name="name">default_code</field>
.. i18n: 		<field name="column_db_name">default_code</field>
.. i18n: 		<field name="type">varchar</field>
.. i18n: 		<field name="table_id" ref="table_product_template>
.. i18n: 		<field name="active">True</field>
.. i18n: 	</record>
..

.. code-block:: xml

	<record model="olap.database.columns" id="columns_product_product_default_code">
		<field name="name">default_code</field>
		<field name="column_db_name">default_code</field>
		<field name="type">varchar</field>
		<field name="table_id" ref="table_product_template>
		<field name="active">True</field>
	</record>

.. i18n: Now, level.
..

Now, level.

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <record model="olap.level" id="level_product_template">
.. i18n: 	<field name="name">default_code</field>
.. i18n: 	<field name="column_name" ref="columns_product_product_default_code"></field>
.. i18n: 	<field name="hierarchy_id" ref="hierarchy_product_template"/>
.. i18n: 	<field name="table_name">res_partner</field>
.. i18n: 	<field name="column_id_name">name</field>
.. i18n:    </record>
..

.. code-block:: xml

    <record model="olap.level" id="level_product_template">
	<field name="name">default_code</field>
	<field name="column_name" ref="columns_product_product_default_code"></field>
	<field name="hierarchy_id" ref="hierarchy_product_template"/>
	<field name="table_name">res_partner</field>
	<field name="column_id_name">name</field>
   </record>

.. i18n: **Step: 6  Creating Dimension date_order up to the quarters**
..

**Step: 6  Creating Dimension date_order up to the quarters**

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <record model="olap.dimension" id="dimension_sales_order">
.. i18n:   	<field name="name">Order Date</field>
.. i18n:   	<field name="cube_id" ref="cube_sales_order_line"/>
.. i18n:      </record>
.. i18n:      
.. i18n:      <record model="olap.cube.table" id="table_sales_order">
.. i18n:   	<field name="name">sale_order</field>
.. i18n:      </record>
.. i18n:      
.. i18n:      <record model="olap.hierarchy" id="hierarchy_sales_order">
.. i18n:   	<field name="name">Order Date</field>
.. i18n:   	<field name="dimension_id" ref="dimension_sales_order"/>
.. i18n:   	<field name="primary_key_table">sale_order</field>
.. i18n:   	<field name="table_id" ref="table_sales_order"/>
.. i18n:      </record>
.. i18n:      
.. i18n:      <record model="olap.database.columns" id="columns_sale_order_date_order">
.. i18n: 	<field name="name">date_order</field>
.. i18n: 	<field name="column_db_name">date_order</field>
.. i18n: 	<field name="type">date</field>
.. i18n: 	<field name="table_id" ref="table_sale_order"/>
.. i18n: 	<field name="active">True</field>
.. i18n:       </record>
..

.. code-block:: xml

    <record model="olap.dimension" id="dimension_sales_order">
  	<field name="name">Order Date</field>
  	<field name="cube_id" ref="cube_sales_order_line"/>
     </record>
     
     <record model="olap.cube.table" id="table_sales_order">
  	<field name="name">sale_order</field>
     </record>
     
     <record model="olap.hierarchy" id="hierarchy_sales_order">
  	<field name="name">Order Date</field>
  	<field name="dimension_id" ref="dimension_sales_order"/>
  	<field name="primary_key_table">sale_order</field>
  	<field name="table_id" ref="table_sales_order"/>
     </record>
     
     <record model="olap.database.columns" id="columns_sale_order_date_order">
	<field name="name">date_order</field>
	<field name="column_db_name">date_order</field>
	<field name="type">date</field>
	<field name="table_id" ref="table_sale_order"/>
	<field name="active">True</field>
      </record>

.. i18n: Making levels in Order Date so to get details as per year, quarters and months. 
..

Making levels in Order Date so to get details as per year, quarters and months. 

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:      <record model="olap.level" id="level_sales_order">
.. i18n:   	<field name="name">date_order</field>
.. i18n:   	<field name="column_name" ref="columns_sale_order_date_order"></field>
.. i18n:   	<field name="column_id_name">date_order</field>
.. i18n:   	<field name="type">date_year</field>
.. i18n:   	<field name="sequence">1</field>
.. i18n:   	<field name="table_name">sale_order</field>
.. i18n:   	<field name="hierarchy_id" ref="hierarchy_sales_order"/>
.. i18n:      </record>
.. i18n: 
.. i18n:      <record model="olap.level" id="level_sales_order_q">
.. i18n:   	<field name="name">date_order</field>
.. i18n:   	<field name="column_name" ref="columns_sale_order_date_order"></field>
.. i18n:   	<field name="column_id_name">date_order</field>
.. i18n:   	<field name="type">date_quarter</field>
.. i18n:   	<field name="sequence">2</field>
.. i18n:   	<field name="table_name">sale_order</field>
.. i18n:   	<field name="hierarchy_id" ref="hierarchy_sales_order"/>
.. i18n:      </record>
.. i18n:      <record model="olap.level" id="level_sales_order_m">
.. i18n:   	<field name="name">date_order</field>
.. i18n:   	<field name="column_name" ref="columns_sale_order_date_order"></field>
.. i18n:   	<field name="column_id_name">date_order</field>
.. i18n:   	<field name="type">date_month</field>
.. i18n:   	<field name="sequence">3</field>
.. i18n:   	<field name="table_name">sale_order</field>
.. i18n:   	<field name="hierarchy_id" ref="hierarchy_sales_order"/>
.. i18n:      </record>
..

.. code-block:: xml

     <record model="olap.level" id="level_sales_order">
  	<field name="name">date_order</field>
  	<field name="column_name" ref="columns_sale_order_date_order"></field>
  	<field name="column_id_name">date_order</field>
  	<field name="type">date_year</field>
  	<field name="sequence">1</field>
  	<field name="table_name">sale_order</field>
  	<field name="hierarchy_id" ref="hierarchy_sales_order"/>
     </record>

     <record model="olap.level" id="level_sales_order_q">
  	<field name="name">date_order</field>
  	<field name="column_name" ref="columns_sale_order_date_order"></field>
  	<field name="column_id_name">date_order</field>
  	<field name="type">date_quarter</field>
  	<field name="sequence">2</field>
  	<field name="table_name">sale_order</field>
  	<field name="hierarchy_id" ref="hierarchy_sales_order"/>
     </record>
     <record model="olap.level" id="level_sales_order_m">
  	<field name="name">date_order</field>
  	<field name="column_name" ref="columns_sale_order_date_order"></field>
  	<field name="column_id_name">date_order</field>
  	<field name="type">date_month</field>
  	<field name="sequence">3</field>
  	<field name="table_name">sale_order</field>
  	<field name="hierarchy_id" ref="hierarchy_sales_order"/>
     </record>

.. i18n: **Step: 7  Creating Dimension res_country**
..

**Step: 7  Creating Dimension res_country**

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:       <record model="olap.cube.table" id="table_sale_order">
.. i18n: 	<field name="name">sale_order</field>
.. i18n:         	<field name='schema_id' ref='schema_main_sales'/>
.. i18n:      </record>
.. i18n:      
.. i18n:      <record model="olap.cube.table" id="table_partner_address_0">
.. i18n:   	<field name="name">res_partner_address</field>
.. i18n:   	<field name='schema_id' ref='schema_main_sales'/>
.. i18n:      </record>
.. i18n:      <record model="olap.cube.table" id="table_partner_address_1">
.. i18n:   	<field name="name">res_country</field>
.. i18n:   	<field name='schema_id' ref='schema_main_sales'/>
.. i18n:      </record>
.. i18n: 
.. i18n:      <record model="olap.cube.table" id="table_partner_address">
.. i18n:   	<field name="name">res_partner_address</field>
.. i18n:   	<field name='schema_id' ref='schema_main_sales'/>
.. i18n:      </record>
.. i18n: 
.. i18n:      <record model="olap.cube.table" id="table_partner_country">
.. i18n:   	<field name="name">sale_order_country</field>
.. i18n:   	<field name='schema_id' ref='schema_main_sales'/>
.. i18n:      </record>
.. i18n: 
.. i18n:      <record model="olap.dimension" id="dimension_partner_country">
.. i18n:   	<field name="name">Sales From Partners</field>
.. i18n:   	<field name="cube_id" ref="cube_sales_order_line"/>
.. i18n:      </record>
.. i18n: 
.. i18n:      <record model="olap.hierarchy" id="hierarchy_partner_country">
.. i18n:   	<field name="name">partner_country</field>
.. i18n:   	<field name="dimension_id" ref="dimension_partner_country"/>
.. i18n:   	<field name="primary_key_table">sale_order</field>
.. i18n:   	<field name="table_id" ref="table_partner_country"/>
.. i18n:      </record>
.. i18n: 
.. i18n:      <record model="olap.level" id="level_partner_country">
.. i18n:   	<field name="name">country_id</field>
.. i18n:   	<field name="column_name" ref="columns_sale_order_date_order"></field>
.. i18n:   	<field name="column_id_name">name</field>
.. i18n:   	<field name="table_name">res_country</field>
.. i18n:   	<field name="hierarchy_id" ref="hierarchy_partner_country"/>
.. i18n:      </record>
..

.. code-block:: xml

      <record model="olap.cube.table" id="table_sale_order">
	<field name="name">sale_order</field>
        	<field name='schema_id' ref='schema_main_sales'/>
     </record>
     
     <record model="olap.cube.table" id="table_partner_address_0">
  	<field name="name">res_partner_address</field>
  	<field name='schema_id' ref='schema_main_sales'/>
     </record>
     <record model="olap.cube.table" id="table_partner_address_1">
  	<field name="name">res_country</field>
  	<field name='schema_id' ref='schema_main_sales'/>
     </record>

     <record model="olap.cube.table" id="table_partner_address">
  	<field name="name">res_partner_address</field>
  	<field name='schema_id' ref='schema_main_sales'/>
     </record>

     <record model="olap.cube.table" id="table_partner_country">
  	<field name="name">sale_order_country</field>
  	<field name='schema_id' ref='schema_main_sales'/>
     </record>

     <record model="olap.dimension" id="dimension_partner_country">
  	<field name="name">Sales From Partners</field>
  	<field name="cube_id" ref="cube_sales_order_line"/>
     </record>

     <record model="olap.hierarchy" id="hierarchy_partner_country">
  	<field name="name">partner_country</field>
  	<field name="dimension_id" ref="dimension_partner_country"/>
  	<field name="primary_key_table">sale_order</field>
  	<field name="table_id" ref="table_partner_country"/>
     </record>

     <record model="olap.level" id="level_partner_country">
  	<field name="name">country_id</field>
  	<field name="column_name" ref="columns_sale_order_date_order"></field>
  	<field name="column_id_name">name</field>
  	<field name="table_name">res_country</field>
  	<field name="hierarchy_id" ref="hierarchy_partner_country"/>
     </record>

.. i18n: **Step: 8  Creating Dimension res_partner_address**
..

**Step: 8  Creating Dimension res_partner_address**

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:       <record model="olap.database.columns" id="columns_res_partner_address">
.. i18n: 		<field name="name">name</field>
.. i18n: 		<field name="column_db_name">name</field>
.. i18n: 		<field name="type">varchar</field>
.. i18n: 		<field name="table_id" ref="table_sales_order"/>
.. i18n: 		<field name="active">True</field>
.. i18n:     </record>
.. i18n:      <record model="olap.cube.table" id="table_address">
.. i18n:   	<field name="name">res_partner_address</field>
.. i18n:   	<field name='schema_id' ref='schema_main_sales'/>
.. i18n:      </record>
.. i18n: 
.. i18n:      <record model="olap.cube.table" id="table_address_country">
.. i18n:   	<field name="name">sale_order_country</field>
.. i18n:   	<field name='schema_id' ref='schema_main_sales'/>
.. i18n:      </record>
.. i18n: 
.. i18n:      <record model="olap.dimension" id="dimension_partner_address_country">
.. i18n:   	<field name="name">Sales by Order Address</field>
.. i18n:   	<field name="cube_id" ref="cube_sales_order_line"/>
.. i18n:      </record>
.. i18n: 
.. i18n:      <record model="olap.hierarchy" id="hierarchy_partner_address_country">
.. i18n:   	<field name="name">address_country</field>
.. i18n:   	<field name="dimension_id" ref="dimension_partner_address_country"/>
.. i18n:   	<field name="primary_key_table">sale_order</field>
.. i18n:   	<field name="table_id" ref="table_address_country"/>
.. i18n:      </record>
.. i18n: 
.. i18n:      <record model="olap.level" id="level_address_country">
.. i18n:   	<field name="name">country_id</field>
.. i18n:   	<field name="sequence">1</field>
.. i18n:   	<field name="column_name" ref="columns_res_partner_address"></field>
.. i18n:   	<field name="column_id_name">country_id</field>
.. i18n:   	<field name="table_name">res_partner_address</field>
.. i18n:   	<field name="hierarchy_id" ref="hierarchy_partner_address_country"/>
.. i18n:      </record>
.. i18n: 
.. i18n:      <record model="olap.level" id="level_address_partner">
.. i18n:   	<field name="name">partner_id</field>
.. i18n:   	<field name="sequence">2</field>
.. i18n:   	<field name="column_name" ref="columns_res_partner_address"></field>
.. i18n:   	<field name="column_id_name">partner_id</field>
.. i18n:   	<field name="table_name">res_partner_address</field>
.. i18n:   	<field name="hierarchy_id" ref="hierarchy_partner_address_country"/>
.. i18n:       </record>
..

.. code-block:: xml

      <record model="olap.database.columns" id="columns_res_partner_address">
		<field name="name">name</field>
		<field name="column_db_name">name</field>
		<field name="type">varchar</field>
		<field name="table_id" ref="table_sales_order"/>
		<field name="active">True</field>
    </record>
     <record model="olap.cube.table" id="table_address">
  	<field name="name">res_partner_address</field>
  	<field name='schema_id' ref='schema_main_sales'/>
     </record>

     <record model="olap.cube.table" id="table_address_country">
  	<field name="name">sale_order_country</field>
  	<field name='schema_id' ref='schema_main_sales'/>
     </record>

     <record model="olap.dimension" id="dimension_partner_address_country">
  	<field name="name">Sales by Order Address</field>
  	<field name="cube_id" ref="cube_sales_order_line"/>
     </record>

     <record model="olap.hierarchy" id="hierarchy_partner_address_country">
  	<field name="name">address_country</field>
  	<field name="dimension_id" ref="dimension_partner_address_country"/>
  	<field name="primary_key_table">sale_order</field>
  	<field name="table_id" ref="table_address_country"/>
     </record>

     <record model="olap.level" id="level_address_country">
  	<field name="name">country_id</field>
  	<field name="sequence">1</field>
  	<field name="column_name" ref="columns_res_partner_address"></field>
  	<field name="column_id_name">country_id</field>
  	<field name="table_name">res_partner_address</field>
  	<field name="hierarchy_id" ref="hierarchy_partner_address_country"/>
     </record>

     <record model="olap.level" id="level_address_partner">
  	<field name="name">partner_id</field>
  	<field name="sequence">2</field>
  	<field name="column_name" ref="columns_res_partner_address"></field>
  	<field name="column_id_name">partner_id</field>
  	<field name="table_name">res_partner_address</field>
  	<field name="hierarchy_id" ref="hierarchy_partner_address_country"/>
      </record>

.. i18n: **Step: 9  Creating Dimension res_user**
..

**Step: 9  Creating Dimension res_user**

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:       <record model="olap.database.columns" id="columns_res_user_name">
.. i18n: 	<field name="name">name</field>
.. i18n: 	<field name="column_db_name">name</field>
.. i18n: 	<field name="type">varchar</field>
.. i18n: 	<field name="table_id" ref="table_sales_order"/>
.. i18n: 	<field name="active">True</field>
.. i18n:      </record>
.. i18n:      
.. i18n:      <record model="olap.dimension" id="dimension_sales_user">
.. i18n:   	<field name="name">user</field>
.. i18n:   	<field name="cube_id" ref="cube_sales_order_line"/>
.. i18n:      </record>
.. i18n:      
.. i18n:      <record model="olap.cube.table" id="table_sales_res_users">
.. i18n:   	<field name="name">res_users</field>
.. i18n:      </record>
.. i18n:      
.. i18n:      <record model="olap.hierarchy" id="hierarchy_sales_user">
.. i18n:   	<field name="name">user</field>
.. i18n:   	<field name="dimension_id" ref="dimension_sales_user"/>
.. i18n:   	<field name="primary_key_table">res_users</field>
.. i18n:   	<field name="table_id" ref="table_sales_res_users"/>
.. i18n:      </record>
.. i18n:      
.. i18n:      <record model="olap.level" id="hierarchy_sales_user_level">
.. i18n:   	<field name="name">name</field>
.. i18n:   	<field name="column_name" ref="columns_res_user_name""></field>
.. i18n:   	<field name="hierarchy_id" ref="hierarchy_sales_user"/>
.. i18n:      </record>
..

.. code-block:: xml

      <record model="olap.database.columns" id="columns_res_user_name">
	<field name="name">name</field>
	<field name="column_db_name">name</field>
	<field name="type">varchar</field>
	<field name="table_id" ref="table_sales_order"/>
	<field name="active">True</field>
     </record>
     
     <record model="olap.dimension" id="dimension_sales_user">
  	<field name="name">user</field>
  	<field name="cube_id" ref="cube_sales_order_line"/>
     </record>
     
     <record model="olap.cube.table" id="table_sales_res_users">
  	<field name="name">res_users</field>
     </record>
     
     <record model="olap.hierarchy" id="hierarchy_sales_user">
  	<field name="name">user</field>
  	<field name="dimension_id" ref="dimension_sales_user"/>
  	<field name="primary_key_table">res_users</field>
  	<field name="table_id" ref="table_sales_res_users"/>
     </record>
     
     <record model="olap.level" id="hierarchy_sales_user_level">
  	<field name="name">name</field>
  	<field name="column_name" ref="columns_res_user_name""></field>
  	<field name="hierarchy_id" ref="hierarchy_sales_user"/>
     </record>

.. i18n: **Step: 10  Creating Measures Item Sold and Total Sold**
..

**Step: 10  Creating Measures Item Sold and Total Sold**

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <record model="olap.database.columns" id="columns_sale_order_line_product_uom_qty">
.. i18n: 		<field name="name">product_uom_qty</field>
.. i18n: 		<field name="column_db_name">product_uom_qty</field>
.. i18n: 		<field name="type">numeric</field>
.. i18n: 		<field name="table_id" ref="table_sale_order_line"/>
.. i18n: 		<field name="active">True</field>
.. i18n:     </record>
.. i18n: 	
.. i18n:    <record model="olap.measure" id="measure_item_sold">
.. i18n:   	<field name="name">Items Sold</field>
.. i18n:   	<field name="cube_id" ref="cube_sales_order_line"/>
.. i18n:   	<field name="value_column" ref="columns_sale_order_line_product_uom_qty"></field>
.. i18n:   	<field name="value_column_id_name">product_uom_qty</field>
.. i18n: 	<field name="table_name">sale_order_line</field>
.. i18n: 	<field name="agregator">sum</field>
.. i18n:    </record>
.. i18n:    <record model="olap.measure" id="measure_total_sales">
.. i18n: 	<field name="name">Total Sold</field>
.. i18n: 	<field name="cube_id" ref="cube_sales_order_line"/>
.. i18n: 	<field name="value_column" ref="columns_sale_order_line_price_unit"></field>
.. i18n: 	<field name="value_column_id_name">price_unit</field>
.. i18n: 	<field name="table_name">sale_order_line</field>
.. i18n: 	<field name="agregator">sum</field>
.. i18n:   </record>
..

.. code-block:: xml

    <record model="olap.database.columns" id="columns_sale_order_line_product_uom_qty">
		<field name="name">product_uom_qty</field>
		<field name="column_db_name">product_uom_qty</field>
		<field name="type">numeric</field>
		<field name="table_id" ref="table_sale_order_line"/>
		<field name="active">True</field>
    </record>
	
   <record model="olap.measure" id="measure_item_sold">
  	<field name="name">Items Sold</field>
  	<field name="cube_id" ref="cube_sales_order_line"/>
  	<field name="value_column" ref="columns_sale_order_line_product_uom_qty"></field>
  	<field name="value_column_id_name">product_uom_qty</field>
	<field name="table_name">sale_order_line</field>
	<field name="agregator">sum</field>
   </record>
   <record model="olap.measure" id="measure_total_sales">
	<field name="name">Total Sold</field>
	<field name="cube_id" ref="cube_sales_order_line"/>
	<field name="value_column" ref="columns_sale_order_line_price_unit"></field>
	<field name="value_column_id_name">price_unit</field>
	<field name="table_name">sale_order_line</field>
	<field name="agregator">sum</field>
  </record>
