.. i18n: Module development
.. i18n: ==================
..

模块开发
==================

.. i18n: Introduction
.. i18n: ------------
..

简介
------------

.. i18n: OpenERP uses a `three-tier architecture
.. i18n: <http://en.wikipedia.org/wiki/Multitier_architecture#Three-tier_architecture>`_.
.. i18n: The application tier itself is written as a core and multiple additional
.. i18n: modules that can be installed or not to create a particular configuration of
.. i18n: OpenERP.
..

OpenERP 采用 `三层架构
<http://en.wikipedia.org/wiki/Multitier_architecture#Three-tier_architecture>`_。
应用层本身被设计成核心和多个附加的模块，这些模块可以安装，不用OpenERP创建一个特殊的配置。

.. i18n: The core of OpenERP and its different modules are written in `Python
.. i18n: <http://python.org/>`_. The functionality of a module is exposed through
.. i18n: XML-RPC (and/or NET-RPC depending on the server's configuration). Modules also
.. i18n: typically make use of OpenERP ORM to persist their data in a relational
.. i18n: database (PostgreSQL). Modules can insert data in the database during
.. i18n: installation by providing XML (or CSV or YML) files.
..

OpenERP的核心和其他不同的模块都是用 `Python
<http://python.org/>`_写的。 模块的功能通过XML-RPC（或是NET-RPC，这取决于服务器端的配置）显示出来。模块也采用OpenERP ORM在关系型数据库（PostgreSQL）中来持久化数据。当模块安装好后通过提供XML文件就可以在数据库中插入数据。

.. i18n: Although  modules are a simple way to structure a complex application,
.. i18n: OpenERP modules also extend the system. Modules are
.. i18n: also called addons (they could also have been called plugins).
..

尽管使用模块是构建一个复杂应用的简单方式，在OpenERP中模块同样可以扩展系统。事实上，模块也被称为addons（它们有时也被称为plugins）。

.. i18n: In a typical configuration of OpenERP, the following modules can be found:
..

在OpenERP的典型配置中，以下模块是必须的：

.. i18n:     * base: the most basic module; it is always installed and can be thought
.. i18n:       as being part of the core of OpenERP. It defines ``ir.property``,
.. i18n:       ``res.company``, ``res.request``, ``res.currency``, ``res.users``,
.. i18n:       ``res.partner``, and so on.
.. i18n:     * crm: Customer & Supplier Relationship management.
.. i18n:     * sale: Sales management.
.. i18n:     * mrp: Manufacturing Resource Planning. 
..

    * base: 最基本的模块。它无论何种情况下都必须安装，被认为是OpenERP核心的一部分。定义了 ``ir.property``,
      ``res.company``, ``res.request``, ``res.currency``, ``res.users``,
      ``res.partner``, 等等。
    * crm: 客户关系管理和供应商关系管理。
    * sale: 销售管理。
    * mrp: 制造资源管理。 

.. i18n: By using Python, XML files, and relying on OpenERP's ORM and its extensibility
.. i18n: mechanisms, new modules can be written easily and quickly. OpenERP's open
.. i18n: source nature and its numerous modules also provide a lot of examples for any
.. i18n: new development.
..

通过使用Python, XML files，依赖OpenERP的ORM和它的延伸机制，新的模块可以很容易快速的写出。OpenERP的开源特性和它众多的模块也为新模块的开发提供很多的例子。

.. i18n: Module Structure
.. i18n: ----------------
..

模块结构
----------------

.. i18n: The Modules
.. i18n: +++++++++++
..

模块
+++++++++++

.. i18n:    #. Introduction
.. i18n:    #. Files & Directories
.. i18n:          #. __openerp__.py
.. i18n:          #. __init__.py
.. i18n:          #. XML Files
.. i18n:                #. Actions
.. i18n:                #. Menu Entries
.. i18n:                #. Reports
.. i18n:                #. Wizards
.. i18n:    #. Profiles
..

   #. 介绍
   #. 文件和文件夹结构
         #. __openerp__.py
         #. __init__.py
         #. XML 文件
               #. 操作
               #. 菜单
               #. 报表
               #. 向导
   #. 配置文件

.. i18n: Modules - Files and Directories
.. i18n: +++++++++++++++++++++++++++++++
..

模块 - 文件和文件夹结构
+++++++++++++++++++++++++++++++

.. i18n: All the modules are located in the server/addons directory.
..

所有模块都应放到 server/addons 文件夹下。

.. i18n: The following steps are necessary to create a new module:
..

按下面步骤创建新模块：

.. i18n:     * create a subdirectory in the server/addons directory
.. i18n:     * create a module description file: **__openerp__.py**
.. i18n:     * create the **Python** file containing the **objects**
.. i18n:     * create **.xml files** that download the data (views, menu entries, demo data, ...)
.. i18n:     * optionally create **reports**, **wizards** or **workflows**.
..

    * 在 server/addons 文件夹下面创建模块子文件夹
    * 创建模块定义文件: **__openerp__.py**
    * 创建定义 **objects** 的 **Python** 文件
    * 创建包括(初始数据, 视图, 菜单, 演示数据)的 **.xml 文件**
    * 创建包含 **reports**, **wizards** 及  **workflows** 的 xml文件(可选)

.. i18n: The Modules - Files And Directories - XML Files
.. i18n: """""""""""""""""""""""""""""""""""""""""""""""
..

模块 - 文件和目录 - XML 文件
"""""""""""""""""""""""""""""""""""""""""""""""

.. i18n: XML files located in the module directory are used to modify the structure of
.. i18n: the database. They are used for many purposes, among which we can cite :
..

模块目录里的XML文件用于修改数据库结构，他们有很多的用途，我们可以列出来：

.. i18n:     * initialization and demonstration data declaration,
.. i18n:     * views declaration,
.. i18n:     * reports declaration,
.. i18n:     * wizards declaration,
.. i18n:     * workflows declaration.
..

    * 初始化，实例化（demonstration）数据声明（declaration）
    * 视图声明
    * 报表声明
    * 向导声明
    * 工作流声明

.. i18n: General structure of OpenERP XML files is more detailed in the 
.. i18n: :ref:`xml-serialization` section. Look here if you are interested in learning 
.. i18n: more about *initialization* and *demonstration data declaration* XML files. The 
.. i18n: following section are only related to XML specific to *actions, menu entries, 
.. i18n: reports, wizards* and *workflows* declaration.
..

OpenERP XML文件主要结构的更多细节在
:ref:`xml-serialization` 部分，如果你想学习更多关于*初始化* 和 *示例数据* XML文件，可以查看这里。 下面的部分只是关于特定的XML文件，如
following section are only related to XML specific to *actions, menu entries, 
*操作、菜单、报表、向导* 和 *工作流* 定义。

.. i18n: Python Module Descriptor File __init__.py
.. i18n: """""""""""""""""""""""""""""""""""""""""
..

Python 模块描述文件 __init__.py
"""""""""""""""""""""""""""""""""""""""""

.. i18n: **The __init__.py file**
..

** __init__.py 文件**

.. i18n: The __init__.py file is, like any Python module, executed at the start of the program. It needs to import the Python files that need to be loaded.
..

The __init__.py file is, like any Python module, executed at the start of the program. It needs to import the Python files that need to be loaded.

.. i18n: So, if you create a "module.py" file, containing the description of your objects, you have to write one line in __init__.py::
.. i18n: 
.. i18n:     import module
..

So, if you create a "module.py" file, containing the description of your objects, you have to write one line in __init__.py::

    import module

.. i18n: OpenERP Module Descriptor File __openerp__.py
.. i18n: """""""""""""""""""""""""""""""""""""""""""""
..

OpenERP Module Descriptor File __openerp__.py
"""""""""""""""""""""""""""""""""""""""""""""

.. i18n: In the created module directory, you must add a **__openerp__.py** file. This file, which must be in Python format, is responsible to
..

In the created module directory, you must add a **__openerp__.py** file. This file, which must be in Python format, is responsible to

.. i18n:    1. determine the *XML files that will be parsed* during the initialization of the server, and also to
.. i18n:    2. determine the *dependencies* of the created module.
..

   1. determine the *XML files that will be parsed* during the initialization of the server, and also to
   2. determine the *dependencies* of the created module.

.. i18n: This file must contain a Python dictionary with the following values:
..

This file must contain a Python dictionary with the following values:

.. i18n: **name**
..

**name**

.. i18n:     The (Plain English) name of the module.
..

    The (Plain English) name of the module.

.. i18n: **version**
..

**version**

.. i18n:     The version of the module, on 2 digits (1.2 or 2.0).
..

    The version of the module, on 2 digits (1.2 or 2.0).

.. i18n: **description**
..

**description**

.. i18n:     The module description (text) including documentation on how to use your modules.
..

    The module description (text) including documentation on how to use your modules.

.. i18n: **author**
..

**author**

.. i18n:     The author of the module.
..

    The author of the module.

.. i18n: **website**
..

**website**

.. i18n:     The website of the module.
..

    The website of the module.

.. i18n: **license**
..

**license**

.. i18n:     The license of the module (default:GPL-2).
..

    The license of the module (default:GPL-2).

.. i18n: **depends**
..

**depends**

.. i18n:     List of modules on which this module depends. The base module must almost always be in the dependencies because some necessary data for the views, reports, ... are in the base module.
..

    List of modules on which this module depends. The base module must almost always be in the dependencies because some necessary data for the views, reports, ... are in the base module.

.. i18n: **init**
..

**init**

.. i18n:     List of .xml files to load when the server is launched with the "--init=module" argument. Filepaths must be relative to the directory where the module is. OpenERP XML File Format is detailed in this section.
..

    List of .xml files to load when the server is launched with the "--init=module" argument. Filepaths must be relative to the directory where the module is. OpenERP XML File Format is detailed in this section.

.. i18n: **data**
..

**data**

.. i18n:     List of .xml files to load when the server is launched with the "--update=module" launched. Filepaths must be relative to the directory where the module is. OpenERP XML File Format is detailed in this section.
..

    List of .xml files to load when the server is launched with the "--update=module" launched. Filepaths must be relative to the directory where the module is. OpenERP XML File Format is detailed in this section.

.. i18n: **demo**
..

**demo**

.. i18n:     List of .xml files to provide demo data. Filepaths must be relative to the directory where the module is. OpenERP XML File Format is detailed in this section.
..

    List of .xml files to provide demo data. Filepaths must be relative to the directory where the module is. OpenERP XML File Format is detailed in this section.

.. i18n: **installable**
..

**installable**

.. i18n:     True or False. Determines if the module is installable or not.
..

    True or False. Determines if the module is installable or not.

.. i18n: **images**
..

**images**

.. i18n:     List of .png files to provide screenshots, used on http://apps.openerp.com.
..

    List of .png files to provide screenshots, used on http://apps.openerp.com.

.. i18n: **active**
..

**active**

.. i18n:     True or False (default: False). Determines the modules that are installed on the database creation.
..

    True or False (default: False). Determines the modules that are installed on the database creation.

.. i18n: **test**
..

**test**

.. i18n:     List of .yml files to provide YAML tests.
..

    List of .yml files to provide YAML tests.

.. i18n: **Example**
..

**Example**

.. i18n: Here is an example of __openerp__.py file for the product module
..

Here is an example of __openerp__.py file for the product module

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     {
.. i18n:         "name" : "Products & Pricelists",
.. i18n:         "version" : "1.1",
.. i18n:         "author" : "Open",
.. i18n:         "category" : "Generic Modules/Inventory Control",
.. i18n:         "depends" : ["base", "account"],
.. i18n:         "init_xml" : [],
.. i18n:         "demo_xml" : ["product_demo.xml"],
.. i18n:         "update_xml" : ["product_data.xml", "product_report.xml", "product_wizard.xml",
.. i18n:                         "product_view.xml", "pricelist_view.xml"],
.. i18n:         "installable": True,
.. i18n:         "active": True
.. i18n:     }
..

.. code-block:: python

    {
        "name" : "Products & Pricelists",
        "version" : "1.1",
        "author" : "Open",
        "category" : "Generic Modules/Inventory Control",
        "depends" : ["base", "account"],
        "init_xml" : [],
        "demo_xml" : ["product_demo.xml"],
        "update_xml" : ["product_data.xml", "product_report.xml", "product_wizard.xml",
                        "product_view.xml", "pricelist_view.xml"],
        "installable": True,
        "active": True
    }

.. i18n: The files that must be placed in init_xml are the ones that relate to the workflow definition, data to load at the installation of the software and the data for the demonstrations.
..

The files that must be placed in init_xml are the ones that relate to the workflow definition, data to load at the installation of the software and the data for the demonstrations.

.. i18n: The files in **update_xml** concern: views, reports and wizards.
..

The files in **update_xml** concern: views, reports and wizards.

.. i18n: Objects
.. i18n: """""""
..

Objects
"""""""

.. i18n: All OpenERP resources are objects: menus, actions, reports, invoices, partners, ... OpenERP is based on an object relational mapping of a database to control the information. Object names are hierarchical, as in the following examples:
..

All OpenERP resources are objects: menus, actions, reports, invoices, partners, ... OpenERP is based on an object relational mapping of a database to control the information. Object names are hierarchical, as in the following examples:

.. i18n:     * account.transfer : a money transfer
.. i18n:     * account.invoice : an invoice
.. i18n:     * account.invoice.line : an invoice line
..

    * account.transfer : a money transfer
    * account.invoice : an invoice
    * account.invoice.line : an invoice line

.. i18n: Generally, the first word is the name of the module: account, stock, sale.
..

Generally, the first word is the name of the module: account, stock, sale.

.. i18n: Other advantages of an ORM;
..

Other advantages of an ORM;

.. i18n:     * simpler relations : invoice.partner.address[0].city
.. i18n:     * objects have properties and methods: invoice.pay(3400 EUR),
.. i18n:     * inheritance, high level constraints, ...
..

    * simpler relations : invoice.partner.address[0].city
    * objects have properties and methods: invoice.pay(3400 EUR),
    * inheritance, high level constraints, ...

.. i18n: It is easier to manipulate one object (example, a partner) than several tables (partner address, categories, events, ...)
..

It is easier to manipulate one object (example, a partner) than several tables (partner address, categories, events, ...)

.. i18n: .. figure::  images/pom_3_0_3.png
.. i18n:    :scale: 50
.. i18n:    :align: center
.. i18n: 
.. i18n:    *The Physical Objects Model of [OpenERP version 3.0.3]*
..

.. figure::  images/pom_3_0_3.png
   :scale: 50
   :align: center

   *The Physical Objects Model of [OpenERP version 3.0.3]*

.. i18n: PostgreSQL
.. i18n: //////////
..

PostgreSQL
//////////

.. i18n: The ORM of OpenERP is constructed over PostgreSQL. It is thus possible to
.. i18n: query the object used by OpenERP using the object interface or by directly
.. i18n: using SQL statements.
..

The ORM of OpenERP is constructed over PostgreSQL. It is thus possible to
query the object used by OpenERP using the object interface or by directly
using SQL statements.

.. i18n: But it is dangerous to write or read directly in the PostgreSQL database, as
.. i18n: you will shortcut important steps like constraints checking or workflow
.. i18n: modification.
..

But it is dangerous to write or read directly in the PostgreSQL database, as
you will shortcut important steps like constraints checking or workflow
modification.

.. i18n: .. note::
.. i18n: 
.. i18n:     The Physical Database Model of OpenERP
..

.. note::

    The Physical Database Model of OpenERP

.. i18n: Pre-Installed Data
.. i18n: """"""""""""""""""
..

Pre-Installed Data
""""""""""""""""""

.. i18n: Data can be inserted or updated into the PostgreSQL tables corresponding to the
.. i18n: OpenERP objects using XML files. The general structure of an OpenERP XML file
.. i18n: is as follows:
..

Data can be inserted or updated into the PostgreSQL tables corresponding to the
OpenERP objects using XML files. The general structure of an OpenERP XML file
is as follows:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:    <?xml version="1.0"?>
.. i18n:    <openerp>
.. i18n:      <data>
.. i18n:        <record model="model.name_1" id="id_name_1">
.. i18n:          <field name="field1">
.. i18n:            "field1 content"
.. i18n:          </field>
.. i18n:          <field name="field2">
.. i18n:            "field2 content"
.. i18n:          </field>
.. i18n:          (...)
.. i18n:        </record>
.. i18n:        <record model="model.name_2" id="id_name_2">
.. i18n:            (...)
.. i18n:        </record>
.. i18n:        (...)
.. i18n:      </data>
.. i18n:    </openerp>
..

.. code-block:: xml

   <?xml version="1.0"?>
   <openerp>
     <data>
       <record model="model.name_1" id="id_name_1">
         <field name="field1">
           "field1 content"
         </field>
         <field name="field2">
           "field2 content"
         </field>
         (...)
       </record>
       <record model="model.name_2" id="id_name_2">
           (...)
       </record>
       (...)
     </data>
   </openerp>

.. i18n: Fields content are strings that must be encoded as *UTF-8* in XML files.
..

Fields content are strings that must be encoded as *UTF-8* in XML files.

.. i18n: Let's review an example taken from the OpenERP source (base_demo.xml in the base module):
..

Let's review an example taken from the OpenERP source (base_demo.xml in the base module):

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:        <record model="res.company" id="main_company">
.. i18n:            <field name="name">Tiny sprl</field>
.. i18n:            <field name="partner_id" ref="main_partner"/>
.. i18n:            <field name="currency_id" ref="EUR"/>
.. i18n:        </record>
..

.. code-block:: xml

       <record model="res.company" id="main_company">
           <field name="name">Tiny sprl</field>
           <field name="partner_id" ref="main_partner"/>
           <field name="currency_id" ref="EUR"/>
       </record>

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:        <record model="res.users" id="user_admin">
.. i18n:            <field name="login">admin</field>
.. i18n:            <field name="password">admin</field>
.. i18n:            <field name="name">Administrator</field>
.. i18n:            <field name="signature">Administrator</field>
.. i18n:            <field name="action_id" ref="action_menu_admin"/>
.. i18n:            <field name="menu_id" ref="action_menu_admin"/>
.. i18n:            <field name="address_id" ref="main_address"/>
.. i18n:            <field name="groups_id" eval="[(6,0,[group_admin])]"/>
.. i18n:            <field name="company_id" ref="main_company"/>
.. i18n:        </record>
..

.. code-block:: xml

       <record model="res.users" id="user_admin">
           <field name="login">admin</field>
           <field name="password">admin</field>
           <field name="name">Administrator</field>
           <field name="signature">Administrator</field>
           <field name="action_id" ref="action_menu_admin"/>
           <field name="menu_id" ref="action_menu_admin"/>
           <field name="address_id" ref="main_address"/>
           <field name="groups_id" eval="[(6,0,[group_admin])]"/>
           <field name="company_id" ref="main_company"/>
       </record>

.. i18n: This last record defines the admin user :
..

This last record defines the admin user :

.. i18n:     * The fields login, password, etc are straightforward.
.. i18n:     * The ref attribute allows to fill relations between the records :
..

    * The fields login, password, etc are straightforward.
    * The ref attribute allows to fill relations between the records :

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:        <field name="company_id" ref="main_company"/>
..

.. code-block:: xml

       <field name="company_id" ref="main_company"/>

.. i18n: The field **company_id** is a many-to-one relation from the user object to the company object, and **main_company** is the id of to associate.
..

The field **company_id** is a many-to-one relation from the user object to the company object, and **main_company** is the id of to associate.

.. i18n:     * The **eval** attribute allows to put some python code in the xml: here the groups_id field is a many2many. For such a field, "[(6,0,[group_admin])]" means : Remove all the groups associated with the current user and use the list [group_admin] as the new associated groups (and group_admin is the id of another record).
.. i18n: 
.. i18n:     * The **search** attribute allows to find the record to associate when you do not know its xml id. You can thus specify a search criteria to find the wanted record. The criteria is a list of tuples of the same form than for the predefined search method. If there are several results, an arbitrary one will be chosen (the first one):
..

    * The **eval** attribute allows to put some python code in the xml: here the groups_id field is a many2many. For such a field, "[(6,0,[group_admin])]" means : Remove all the groups associated with the current user and use the list [group_admin] as the new associated groups (and group_admin is the id of another record).

    * The **search** attribute allows to find the record to associate when you do not know its xml id. You can thus specify a search criteria to find the wanted record. The criteria is a list of tuples of the same form than for the predefined search method. If there are several results, an arbitrary one will be chosen (the first one):

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:        <field name="partner_id" search="[]" model="res.partner"/>
..

.. code-block:: xml

       <field name="partner_id" search="[]" model="res.partner"/>

.. i18n: This is a classical example of the use of **search** in demo data: here we do not really care about which partner we want to use for the test, so we give an empty list. Notice the **model** attribute is currently mandatory.
..

This is a classical example of the use of **search** in demo data: here we do not really care about which partner we want to use for the test, so we give an empty list. Notice the **model** attribute is currently mandatory.

.. i18n: Record Tag
.. i18n: //////////
..

Record Tag
//////////

.. i18n: **Description**
..

**Description**

.. i18n: The addition of new data is made with the record tag. This one takes a mandatory attribute : model. Model is the object name where the insertion has to be done. The tag record can also take an optional attribute: id. If this attribute is given, a variable of this name can be used later on, in the same file, to make reference to the newly created resource ID.
..

The addition of new data is made with the record tag. This one takes a mandatory attribute : model. Model is the object name where the insertion has to be done. The tag record can also take an optional attribute: id. If this attribute is given, a variable of this name can be used later on, in the same file, to make reference to the newly created resource ID.

.. i18n: A record tag may contain field tags. They indicate the record's fields value. If a field is not specified the default value will be used.
..

A record tag may contain field tags. They indicate the record's fields value. If a field is not specified the default value will be used.

.. i18n: **Example**
..

**Example**

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <record model="ir.actions.report.xml" id="l0">
.. i18n:          <field name="model">account.invoice</field>
.. i18n:          <field name="name">Invoices List</field>
.. i18n:          <field name="report_name">account.invoice.list</field>
.. i18n:          <field name="report_xsl">account/report/invoice.xsl</field>
.. i18n:          <field name="report_xml">account/report/invoice.xml</field>
.. i18n:     </record>
..

.. code-block:: xml

    <record model="ir.actions.report.xml" id="l0">
         <field name="model">account.invoice</field>
         <field name="name">Invoices List</field>
         <field name="report_name">account.invoice.list</field>
         <field name="report_xsl">account/report/invoice.xsl</field>
         <field name="report_xml">account/report/invoice.xml</field>
    </record>

.. i18n: Field tag
.. i18n: /////////
..

Field tag
/////////

.. i18n: The attributes for the field tag are the following:
..

The attributes for the field tag are the following:

.. i18n: name : mandatory
.. i18n:   the field name
..

name : mandatory
  the field name

.. i18n: eval : optional
.. i18n:   python expression that indicating the value to add
.. i18n:   
.. i18n: ref
.. i18n:   reference to an id defined in this file
..

eval : optional
  python expression that indicating the value to add
  
ref
  reference to an id defined in this file

.. i18n: model
.. i18n:   model to be looked up in the search
..

model
  model to be looked up in the search

.. i18n: search
.. i18n:   a query
..

search
  a query

.. i18n: Function tag
.. i18n: ////////////
..

Function tag
////////////

.. i18n: A function tag can contain other function tags.
..

A function tag can contain other function tags.

.. i18n: model : mandatory
.. i18n:   The model to be used
..

model : mandatory
  The model to be used

.. i18n: name : mandatory
.. i18n:   the function given name
..

name : mandatory
  the function given name

.. i18n: eval
.. i18n:   should evaluate to the list of parameters of the method to be called, excluding cr and uid
..

eval
  should evaluate to the list of parameters of the method to be called, excluding cr and uid

.. i18n: **Example**
..

**Example**

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <function model="ir.ui.menu" name="search" eval="[[('name','=','Operations')]]"/>
..

.. code-block:: xml

    <function model="ir.ui.menu" name="search" eval="[[('name','=','Operations')]]"/>

.. i18n: Getitem tag
.. i18n: ///////////
..

Getitem tag
///////////

.. i18n: Takes a subset of the evaluation of the last child node of the tag.
..

Takes a subset of the evaluation of the last child node of the tag.

.. i18n: type : mandatory
.. i18n:   int or list
..

type : mandatory
  int or list

.. i18n: index : mandatory
.. i18n:   int or string (a key of a dictionary)
..

index : mandatory
  int or string (a key of a dictionary)

.. i18n: **Example**
..

**Example**

.. i18n: Evaluates to the first element of the list of ids returned by the function node
..

Evaluates to the first element of the list of ids returned by the function node

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <getitem index="0" type="list">
.. i18n:         <function model="ir.ui.menu" name="search" eval="[[('name','=','Operations')]]"/>
.. i18n:     </getitem>
..

.. code-block:: xml

    <getitem index="0" type="list">
        <function model="ir.ui.menu" name="search" eval="[[('name','=','Operations')]]"/>
    </getitem>

.. i18n: i18n
.. i18n: """"
..

i18n
""""

.. i18n: Improving Translations
.. i18n: //////////////////////
..

Improving Translations
//////////////////////

.. i18n: .. describe:: Translating in launchpad
..

.. describe:: Translating in launchpad

.. i18n: Translations are managed by
.. i18n: the `Launchpad Web interface <https://translations.launchpad.net/openobject>`_. Here, you'll
.. i18n: find the list of translatable projects.
..

Translations are managed by
the `Launchpad Web interface <https://translations.launchpad.net/openobject>`_. Here, you'll
find the list of translatable projects.

.. i18n: Please read the `FAQ <https://answers.launchpad.net/rosetta/+faqs>`_ before asking questions.
..

Please read the `FAQ <https://answers.launchpad.net/rosetta/+faqs>`_ before asking questions.

.. i18n: .. describe:: Translating your own module
..

.. describe:: Translating your own module

.. i18n: .. versionchanged:: 5.0
..

.. versionchanged:: 5.0

.. i18n: Contrary to the 4.2.x version, the translations are now done by module. So,
.. i18n: instead of an unique ``i18n`` folder for the whole application, each module has
.. i18n: its own ``i18n`` folder. In addition, OpenERP can now deal with ``.po`` [#f_po]_
.. i18n: files as import/export format. The translation files of the installed languages
.. i18n: are automatically loaded when installing or updating a module. OpenERP can also
.. i18n: generate a .tgz archive containing well organised ``.po`` files for each selected
.. i18n: module.
..

Contrary to the 4.2.x version, the translations are now done by module. So,
instead of an unique ``i18n`` folder for the whole application, each module has
its own ``i18n`` folder. In addition, OpenERP can now deal with ``.po`` [#f_po]_
files as import/export format. The translation files of the installed languages
are automatically loaded when installing or updating a module. OpenERP can also
generate a .tgz archive containing well organised ``.po`` files for each selected
module.

.. i18n: .. [#f_po] http://www.gnu.org/software/autoconf/manual/gettext/PO-Files.html#PO-Files
..

.. [#f_po] http://www.gnu.org/software/autoconf/manual/gettext/PO-Files.html#PO-Files

.. i18n: Process
.. i18n: """""""
..

Process
"""""""

.. i18n: Defining the process
.. i18n: ////////////////////
..

Defining the process
////////////////////

.. i18n: Through the interface and module recorder.
.. i18n: Then, put the generated XML in your own module.
..

Through the interface and module recorder.
Then, put the generated XML in your own module.

.. i18n: Views
.. i18n: """""
..

Views
"""""

.. i18n: Technical Specifications - Architecture - Views
.. i18n: ///////////////////////////////////////////////
..

Technical Specifications - Architecture - Views
///////////////////////////////////////////////

.. i18n: Views are a way to represent the objects on the client side. They indicate to the client how to lay out the data coming from the objects on the screen.
..

Views are a way to represent the objects on the client side. They indicate to the client how to lay out the data coming from the objects on the screen.

.. i18n: There are two types of views:
..

There are two types of views:

.. i18n:     * form views
.. i18n:     * tree views
..

    * form views
    * tree views

.. i18n: Lists are simply a particular case of tree views.
..

Lists are simply a particular case of tree views.

.. i18n: A same object may have several views: the first defined view of a kind (*tree, form*, ...) will be used as the default view for this kind. That way you can have a default tree view (that will act as the view of a one2many) and a specialized view with more or less information that will appear when one double-clicks on a menu item. For example, the products have several views according to the product variants.
..

A same object may have several views: the first defined view of a kind (*tree, form*, ...) will be used as the default view for this kind. That way you can have a default tree view (that will act as the view of a one2many) and a specialized view with more or less information that will appear when one double-clicks on a menu item. For example, the products have several views according to the product variants.

.. i18n: Views are described in XML.
..

Views are described in XML.

.. i18n: If no view has been defined for an object, the object is able to generate a view to represent itself. This can limit the developer's work but results in less ergonomic views.
..

If no view has been defined for an object, the object is able to generate a view to represent itself. This can limit the developer's work but results in less ergonomic views.

.. i18n: Usage example
.. i18n: /////////////
..

Usage example
/////////////

.. i18n: When you open an invoice, here is the chain of operations followed by the client:
..

When you open an invoice, here is the chain of operations followed by the client:

.. i18n:     * An action asks to open the invoice (it gives the object's data (account.invoice), the view, the domain (e.g. only unpaid invoices) ).
.. i18n:     * The client asks (with XML-RPC) to the server what views are defined for the invoice object and what are the data it must show.
.. i18n:     * The client displays the form according to the view
..

    * An action asks to open the invoice (it gives the object's data (account.invoice), the view, the domain (e.g. only unpaid invoices) ).
    * The client asks (with XML-RPC) to the server what views are defined for the invoice object and what are the data it must show.
    * The client displays the form according to the view

.. i18n: .. figure::  images/arch_view_use.png
.. i18n:    :scale: 50
.. i18n:    :align: center
..

.. figure::  images/arch_view_use.png
   :scale: 50
   :align: center

.. i18n: To develop new objects
.. i18n: //////////////////////
..

To develop new objects
//////////////////////

.. i18n: The design of new objects is restricted to the minimum: create the objects and optionally create the views to represent them. The PostgreSQL tables do not have to be written by hand because the objects are able to automatically create them (or adapt them in case they already exist).
..

The design of new objects is restricted to the minimum: create the objects and optionally create the views to represent them. The PostgreSQL tables do not have to be written by hand because the objects are able to automatically create them (or adapt them in case they already exist).

.. i18n: Reports
.. i18n: """""""
..

Reports
"""""""

.. i18n: OpenERP uses a flexible and powerful reporting system. Reports are generated either in PDF or in HTML. Reports are designed on the principle of separation between the data layer and the presentation layer.
..

OpenERP uses a flexible and powerful reporting system. Reports are generated either in PDF or in HTML. Reports are designed on the principle of separation between the data layer and the presentation layer.

.. i18n: Reports are described more in details in the `Reporting <http://openobject.com/wiki/index.php/Developers:Developper%27s_Book/Reports>`_ chapter.
..

Reports are described more in details in the `Reporting <http://openobject.com/wiki/index.php/Developers:Developper%27s_Book/Reports>`_ chapter.

.. i18n: Wizards
.. i18n: """""""
..

Wizards
"""""""

.. i18n: Here's an example of a .XML file that declares a wizard.
..

Here's an example of a .XML file that declares a wizard.

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <?xml version="1.0"?>
.. i18n:     <openerp>
.. i18n:         <data>
.. i18n:          <wizard string="Employee Info"
.. i18n:                  model="hr.employee"
.. i18n:                  name="employee.info.wizard"
.. i18n:                  id="wizard_employee_info"/>
.. i18n:         </data>
.. i18n:     </openerp>
..

.. code-block:: xml

    <?xml version="1.0"?>
    <openerp>
        <data>
         <wizard string="Employee Info"
                 model="hr.employee"
                 name="employee.info.wizard"
                 id="wizard_employee_info"/>
        </data>
    </openerp>

.. i18n: A wizard is declared using a wizard tag. See "Add A New Wizard" for more information about wizard XML.
..

A wizard is declared using a wizard tag. See "Add A New Wizard" for more information about wizard XML.

.. i18n: also you can add wizard in menu using following xml entry
..

also you can add wizard in menu using following xml entry

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <?xml version="1.0"?>
.. i18n:     </openerp>
.. i18n:          <data>
.. i18n:          <wizard string="Employee Info"
.. i18n:                  model="hr.employee"
.. i18n:                  name="employee.info.wizard"
.. i18n:                  id="wizard_employee_info"/>
.. i18n:          <menuitem
.. i18n:                  name="Human Resource/Employee Info"
.. i18n:                  action="wizard_employee_info"
.. i18n:                  type="wizard"
.. i18n:                  id="menu_wizard_employee_info"/>
.. i18n:          </data>
.. i18n:     </openerp>
..

.. code-block:: xml

    <?xml version="1.0"?>
    </openerp>
         <data>
         <wizard string="Employee Info"
                 model="hr.employee"
                 name="employee.info.wizard"
                 id="wizard_employee_info"/>
         <menuitem
                 name="Human Resource/Employee Info"
                 action="wizard_employee_info"
                 type="wizard"
                 id="menu_wizard_employee_info"/>
         </data>
    </openerp>

.. i18n: Workflow
.. i18n: """"""""
..

Workflow
""""""""

.. i18n: The objects and the views allow you to define new forms very simply, lists/trees and interactions between them. But that is not enough, you must define the dynamics of these objects.
..

The objects and the views allow you to define new forms very simply, lists/trees and interactions between them. But that is not enough, you must define the dynamics of these objects.

.. i18n: A few examples:
..

A few examples:

.. i18n:     * a confirmed sale order must generate an invoice, according to certain conditions
.. i18n:     * a paid invoice must, only under certain conditions, start the shipping order
..

    * a confirmed sale order must generate an invoice, according to certain conditions
    * a paid invoice must, only under certain conditions, start the shipping order

.. i18n: The workflows describe these interactions with graphs. One or several workflows may be associated to the objects. Workflows are not mandatory; some objects don't have workflows.
..

The workflows describe these interactions with graphs. One or several workflows may be associated to the objects. Workflows are not mandatory; some objects don't have workflows.

.. i18n: Below is an example workflow used for sale orders. It must generate invoices and shipments according to certain conditions.
..

Below is an example workflow used for sale orders. It must generate invoices and shipments according to certain conditions.

.. i18n: .. figure::  images/arch_workflow_sale.png
.. i18n:    :scale: 85
.. i18n:    :align: center
..

.. figure::  images/arch_workflow_sale.png
   :scale: 85
   :align: center

.. i18n: In this graph, the nodes represent the actions to be done:
..

In this graph, the nodes represent the actions to be done:

.. i18n:     * create an invoice,
.. i18n:     * cancel the sale order,
.. i18n:     * generate the shipping order, ...
..

    * create an invoice,
    * cancel the sale order,
    * generate the shipping order, ...

.. i18n: The arrows are the conditions;
..

The arrows are the conditions;

.. i18n:     * waiting for the order validation,
.. i18n:     * invoice paid,
.. i18n:     * click on the cancel button, ...
..

    * waiting for the order validation,
    * invoice paid,
    * click on the cancel button, ...

.. i18n: The squared nodes represent other Workflows;
..

The squared nodes represent other Workflows;

.. i18n:     * the invoice
.. i18n:     * the shipping
..

    * the invoice
    * the shipping

.. i18n: OpenERP Module Descriptor File : __openerp__.py
.. i18n: -----------------------------------------------
..

OpenERP Module Descriptor File : __openerp__.py
-----------------------------------------------

.. i18n: Normal Module
.. i18n: +++++++++++++
..

Normal Module
+++++++++++++

.. i18n: In the created module directory, you must add a **__openerp__.py** file. This file, which must be in Python format, is responsible to
..

In the created module directory, you must add a **__openerp__.py** file. This file, which must be in Python format, is responsible to

.. i18n:    1. determine the XML files that will be parsed during the initialization of the server, and also to
.. i18n:    2. determine the dependencies of the created module.
..

   1. determine the XML files that will be parsed during the initialization of the server, and also to
   2. determine the dependencies of the created module.

.. i18n: This file must contain a Python dictionary with the following values:
..

This file must contain a Python dictionary with the following values:

.. i18n: **name**
..

**name**

.. i18n:     The (Plain English) name of the module.
..

    The (Plain English) name of the module.

.. i18n: **version**
..

**version**

.. i18n:     The version of the module.
..

    The version of the module.

.. i18n: **description**
..

**description**

.. i18n:     The module description (text).
..

    The module description (text).

.. i18n: **author**
..

**author**

.. i18n:     The author of the module.
..

    The author of the module.

.. i18n: **website**
..

**website**

.. i18n:     The website of the module.
..

    The website of the module.

.. i18n: **license**
..

**license**

.. i18n:     The license of the module (default:GPL-2).
..

    The license of the module (default:GPL-2).

.. i18n: **depends**
..

**depends**

.. i18n:     List of modules on which this module depends. The base module must almost always be in the dependencies because some necessary data for the views, reports, ... are in the base module.
..

    List of modules on which this module depends. The base module must almost always be in the dependencies because some necessary data for the views, reports, ... are in the base module.

.. i18n: **init_xml**
..

**init_xml**

.. i18n:     List of .xml files to load when the server is launched with the "--init=module" argument. Filepaths must be relative to the directory where the module is. OpenERP XML File Format is detailed in this section.
..

    List of .xml files to load when the server is launched with the "--init=module" argument. Filepaths must be relative to the directory where the module is. OpenERP XML File Format is detailed in this section.

.. i18n: **update_xml**
..

**update_xml**

.. i18n:     List of .xml files to load when the server is launched with the "--update=module" launched. Filepaths must be relative to the directory where the module is. OpenERP XML File Format is detailed in this section.
..

    List of .xml files to load when the server is launched with the "--update=module" launched. Filepaths must be relative to the directory where the module is. OpenERP XML File Format is detailed in this section.

.. i18n: **installable**
..

**installable**

.. i18n:     True or False. Determines if the module is installable or not.
..

    True or False. Determines if the module is installable or not.

.. i18n: **active**
..

**active**

.. i18n:     True or False (default: False). Determines the modules that are installed on the database creation.
..

    True or False (default: False). Determines the modules that are installed on the database creation.

.. i18n: Example
.. i18n: """""""
..

Example
"""""""

.. i18n: Here is an example of __openerp__.py file for the *product* module:
..

Here is an example of __openerp__.py file for the *product* module:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     {
.. i18n:         "name" : "Products & Pricelists",
.. i18n:         "version" : "1.1",
.. i18n:         "author" : "Open",
.. i18n:         "category" : "Generic Modules/Inventory Control",
.. i18n:         "depends" : ["base", "account"],
.. i18n:         "init_xml" : [],
.. i18n:         "demo_xml" : ["product_demo.xml"],
.. i18n:         "update_xml" : ["product_data.xml","product_report.xml", "product_wizard.xml","product_view.xml", "pricelist_view.xml"],
.. i18n:         "installable": True,
.. i18n:         "active": True
.. i18n:     }
..

.. code-block:: python

    {
        "name" : "Products & Pricelists",
        "version" : "1.1",
        "author" : "Open",
        "category" : "Generic Modules/Inventory Control",
        "depends" : ["base", "account"],
        "init_xml" : [],
        "demo_xml" : ["product_demo.xml"],
        "update_xml" : ["product_data.xml","product_report.xml", "product_wizard.xml","product_view.xml", "pricelist_view.xml"],
        "installable": True,
        "active": True
    }

.. i18n: The files that must be placed in init_xml are the ones that relate to the workflow definition, data to load at the installation of the software and the data for the demonstrations.
..

The files that must be placed in init_xml are the ones that relate to the workflow definition, data to load at the installation of the software and the data for the demonstrations.

.. i18n: The files in **update_xml** concern: views, reports and wizards.
..

The files in **update_xml** concern: views, reports and wizards.

.. i18n: Profile Module
.. i18n: ++++++++++++++
..

Profile Module
++++++++++++++

.. i18n: The purpose of a profile is to initialize OpenERP with a set of modules directly after the database has been created. A profile is a special kind of module that contains no code, only *dependencies on other modules*.
..

The purpose of a profile is to initialize OpenERP with a set of modules directly after the database has been created. A profile is a special kind of module that contains no code, only *dependencies on other modules*.

.. i18n: In order to create a profile, you only have to create a new directory in server/addons (you *should* call this folder profile_modulename), in which you put an *empty* __init__.py file (as every directory Python imports must contain an __init__.py file), and a __openerp__.py whose structure is as follows :
..

In order to create a profile, you only have to create a new directory in server/addons (you *should* call this folder profile_modulename), in which you put an *empty* __init__.py file (as every directory Python imports must contain an __init__.py file), and a __openerp__.py whose structure is as follows :

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     {
.. i18n:          "name":"''Name of the Profile'',
.. i18n:          "version":"''Version String''",
.. i18n:          "author":"''Author Name''",
.. i18n:          "category":"Profile",
.. i18n:          "depends":[''List of the modules to install with the profile''],
.. i18n:          "demo_xml":[],
.. i18n:          "update_xml":[],
.. i18n:          "active":False,
.. i18n:          "installable":True,
.. i18n:     }
..

.. code-block:: python

    {
         "name":"''Name of the Profile'',
         "version":"''Version String''",
         "author":"''Author Name''",
         "category":"Profile",
         "depends":[''List of the modules to install with the profile''],
         "demo_xml":[],
         "update_xml":[],
         "active":False,
         "installable":True,
    }

.. i18n: Example
.. i18n: """""""
..

Example
"""""""

.. i18n: Here's the code of the file
.. i18n: server/bin/addons/profile_manufacturing/__openerp__.py, which corresponds to the
.. i18n: manufacturing industry profile in OpenERP.
..

Here's the code of the file
server/bin/addons/profile_manufacturing/__openerp__.py, which corresponds to the
manufacturing industry profile in OpenERP.

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     {
.. i18n:          "name":"Manufacturing industry profile",
.. i18n:          "version":"1.1",
.. i18n:          "author":"Open",
.. i18n:          "category":"Profile",
.. i18n:          "depends":["mrp", "crm", "sale", "delivery"],
.. i18n:          "demo_xml":[],
.. i18n:          "update_xml":[],
.. i18n:          "active":False,
.. i18n:          "installable":True,
.. i18n:     }
..

.. code-block:: python

    {
         "name":"Manufacturing industry profile",
         "version":"1.1",
         "author":"Open",
         "category":"Profile",
         "depends":["mrp", "crm", "sale", "delivery"],
         "demo_xml":[],
         "update_xml":[],
         "active":False,
         "installable":True,
    }

.. i18n: Module creation
.. i18n: ---------------
..

Module creation
---------------

.. i18n: Getting the skeleton directory
.. i18n: ++++++++++++++++++++++++++++++
..

Getting the skeleton directory
++++++++++++++++++++++++++++++

.. i18n: You can copy __openerp__.py and __init__.py from any other module to create a new module into a new directory.
..

You can copy __openerp__.py and __init__.py from any other module to create a new module into a new directory.

.. i18n: As an example on Ubuntu:
.. i18n: ::
.. i18n: 
.. i18n: 	$ cd ~/workspace/stable/stable_addons_5.0/
.. i18n: 	$ mkdir travel
.. i18n: 	$ sudo cp ~/workspace/stable/stable_addons_5.0/hr/__openerp__.py ~/workspace/stable/stable_addons_5.0/travel
.. i18n: 	sudo cp ~/workspace/stable/stable_addons_5.0/hr/__init__.py ~/workspace/stable/stable_addons_5.0/travel
..

As an example on Ubuntu:
::

	$ cd ~/workspace/stable/stable_addons_5.0/
	$ mkdir travel
	$ sudo cp ~/workspace/stable/stable_addons_5.0/hr/__openerp__.py ~/workspace/stable/stable_addons_5.0/travel
	sudo cp ~/workspace/stable/stable_addons_5.0/hr/__init__.py ~/workspace/stable/stable_addons_5.0/travel

.. i18n: You will need to give yourself permissions over that new directory if you want
.. i18n: to be able to modify it: ::
.. i18n: 
.. i18n:     $ sudo chown -R `whoami` travel
..

You will need to give yourself permissions over that new directory if you want
to be able to modify it: ::

    $ sudo chown -R `whoami` travel

.. i18n: You got yourself the directory for a new module there, and a skeleton
.. i18n: structure, but you still need to change a few things inside the module's
.. i18n: definition...
..

You got yourself the directory for a new module there, and a skeleton
structure, but you still need to change a few things inside the module's
definition...

.. i18n: Changing the default definition
.. i18n: +++++++++++++++++++++++++++++++
..

Changing the default definition
+++++++++++++++++++++++++++++++

.. i18n: To change the default settings of the "travel" module,
.. i18n: get yourself into the "travel" directory and edit *__openerp__.py* (with *gedit*,
.. i18n: for example, a simple text editor. Feel free to use another one) ::
.. i18n: 
.. i18n:     $ cd travel
.. i18n:     $ gedit __openerp__.py
..

To change the default settings of the "travel" module,
get yourself into the "travel" directory and edit *__openerp__.py* (with *gedit*,
for example, a simple text editor. Feel free to use another one) ::

    $ cd travel
    $ gedit __openerp__.py

.. i18n: The file looks like this:
..

The file looks like this:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     {
.. i18n:       "name" : "Human Resources",
.. i18n:       "version" : "1.1",
.. i18n:       "author" : "Tiny",
.. i18n:       "category" : "Generic Modules/Human Resources",
.. i18n:       "website" : "http://www.openerp.com",
.. i18n:       "description": """
.. i18n:       Module for human resource management. You can manage:
.. i18n:       * Employees and hierarchies
.. i18n:       * Work hours sheets
.. i18n:       * Attendances and sign in/out system
.. i18n: 
.. i18n:       Different reports are also provided, mainly for attendance statistics.
.. i18n:       """,
.. i18n:       'author': 'Tiny',
.. i18n:       'website': 'http://www.openerp.com',
.. i18n:       'depends': ['base', 'process'],
.. i18n:       'init_xml': [],
.. i18n:       'update_xml': [
.. i18n:           'security/hr_security.xml',
.. i18n:           'security/ir.model.access.csv',
.. i18n:           'hr_view.xml',
.. i18n:           'hr_department_view.xml',
.. i18n:           'process/hr_process.xml'
.. i18n:       ],
.. i18n:       'demo_xml': ['hr_demo.xml', 'hr_department_demo.xml'],
.. i18n:       'installable': True,
.. i18n:       'active': False,
.. i18n:       'certificate': '0086710558965',
.. i18n:     }
..

.. code-block:: python

    {
      "name" : "Human Resources",
      "version" : "1.1",
      "author" : "Tiny",
      "category" : "Generic Modules/Human Resources",
      "website" : "http://www.openerp.com",
      "description": """
      Module for human resource management. You can manage:
      * Employees and hierarchies
      * Work hours sheets
      * Attendances and sign in/out system

      Different reports are also provided, mainly for attendance statistics.
      """,
      'author': 'Tiny',
      'website': 'http://www.openerp.com',
      'depends': ['base', 'process'],
      'init_xml': [],
      'update_xml': [
          'security/hr_security.xml',
          'security/ir.model.access.csv',
          'hr_view.xml',
          'hr_department_view.xml',
          'process/hr_process.xml'
      ],
      'demo_xml': ['hr_demo.xml', 'hr_department_demo.xml'],
      'installable': True,
      'active': False,
      'certificate': '0086710558965',
    }

.. i18n: You will want to change whichever settings you feel right and get something like this:
..

You will want to change whichever settings you feel right and get something like this:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     {
.. i18n:         "name" : "Travel agency module",
.. i18n:         "version" : "1.1",
.. i18n:         "author" : "Tiny",
.. i18n:         "category" : "Generic Modules/Others",
.. i18n:         "website" : "http://www.openerp.com",
.. i18n:         "description": "A module to manage hotel bookings and a few other useful features.",
.. i18n:         "depends" : ["base"],
.. i18n:         "init_xml" : [],
.. i18n:         "update_xml" : ["travel_view.xml"],
.. i18n:         "active": True,
.. i18n:         "installable": True
.. i18n:     }
..

.. code-block:: python

    {
        "name" : "Travel agency module",
        "version" : "1.1",
        "author" : "Tiny",
        "category" : "Generic Modules/Others",
        "website" : "http://www.openerp.com",
        "description": "A module to manage hotel bookings and a few other useful features.",
        "depends" : ["base"],
        "init_xml" : [],
        "update_xml" : ["travel_view.xml"],
        "active": True,
        "installable": True
    }

.. i18n: Note the "active" field becomes true.
..

Note the "active" field becomes true.

.. i18n: Changing the main module file
.. i18n: +++++++++++++++++++++++++++++
..

Changing the main module file
+++++++++++++++++++++++++++++

.. i18n: Now you need to update the travel.py script to suit the needs of your module.
.. i18n: We suggest you follow the Flash tutorial for this or download the travel agency
.. i18n: module from the 20 minutes tutorial page.  ::
.. i18n: 
.. i18n:     The documentation below is overlapping the two next step in this wiki tutorial,
.. i18n:     so just consider them as a help and head towards the next two pages first...
..

Now you need to update the travel.py script to suit the needs of your module.
We suggest you follow the Flash tutorial for this or download the travel agency
module from the 20 minutes tutorial page.  ::

    The documentation below is overlapping the two next step in this wiki tutorial,
    so just consider them as a help and head towards the next two pages first...

.. i18n: The travel.py file should initially look like this:
..

The travel.py file should initially look like this:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     from osv import osv, fields
.. i18n: 
.. i18n:     class travel_hostel(osv.osv):
.. i18n:            _name = 'travel.hostel'
.. i18n:            _inherit = 'res.partner'
.. i18n:            _columns = {
.. i18n:            'rooms_id': fields.one2many('travel.room', 'hostel_id', 'Rooms'),
.. i18n:            'quality': fields.char('Quality', size=16),
.. i18n:            }
.. i18n:            _defaults = {
.. i18n:            }
.. i18n:     travel_hostel()
..

.. code-block:: python

    from osv import osv, fields

    class travel_hostel(osv.osv):
           _name = 'travel.hostel'
           _inherit = 'res.partner'
           _columns = {
           'rooms_id': fields.one2many('travel.room', 'hostel_id', 'Rooms'),
           'quality': fields.char('Quality', size=16),
           }
           _defaults = {
           }
    travel_hostel()

.. i18n: Ideally, you would copy that bunch of code several times to create all the
.. i18n: entities you need (travel_airport, travel_room, travel_flight). This is what
.. i18n: will hold the database structure of your objects, but you don't really need to
.. i18n: worry too much about the database side. Just filling this file will create the
.. i18n: system structure for you when you install the module.
..

Ideally, you would copy that bunch of code several times to create all the
entities you need (travel_airport, travel_room, travel_flight). This is what
will hold the database structure of your objects, but you don't really need to
worry too much about the database side. Just filling this file will create the
system structure for you when you install the module.

.. i18n: Customizing the view
.. i18n: ++++++++++++++++++++
..

Customizing the view
++++++++++++++++++++

.. i18n: You can now move on to editing the views. To do this, edit the custom_view.xml file. It should first look like this:
..

You can now move on to editing the views. To do this, edit the custom_view.xml file. It should first look like this:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <openerp>
.. i18n:     <data>
.. i18n:         <record model="res.groups" id="group_compta_user">
.. i18n:                 <field name="name">grcompta</field>
.. i18n:         </record>
.. i18n:         <record model="res.groups" id="group_compta_admin">
.. i18n:                 <field name="name">grcomptaadmin</field>
.. i18n:         </record>
.. i18n:         <menuitem name="Administration" groups="admin,grcomptaadmin"
.. i18n: 		        icon="terp-stock" id="menu_admin_compta"/>
.. i18n:     </data>
.. i18n:     </openerp>
..

.. code-block:: xml

    <openerp>
    <data>
        <record model="res.groups" id="group_compta_user">
                <field name="name">grcompta</field>
        </record>
        <record model="res.groups" id="group_compta_admin">
                <field name="name">grcomptaadmin</field>
        </record>
        <menuitem name="Administration" groups="admin,grcomptaadmin"
		        icon="terp-stock" id="menu_admin_compta"/>
    </data>
    </openerp>

.. i18n: This is, as you can see, an example taken from an accounting system (French
.. i18n: people call accounting "comptabilité", which explains the compta bit).
..

This is, as you can see, an example taken from an accounting system (French
people call accounting "comptabilité", which explains the compta bit).

.. i18n: Defining a view is defining the interfaces the user will get when accessing
.. i18n: your module. Just defining a bunch of fields here should already get you
.. i18n: started on a complete interface. However, due to the complexity of doing it
.. i18n: right, we recommend, once again, that download the travel agency module example from this link http://www.openerp.com/download/modules/5.0/.
..

Defining a view is defining the interfaces the user will get when accessing
your module. Just defining a bunch of fields here should already get you
started on a complete interface. However, due to the complexity of doing it
right, we recommend, once again, that download the travel agency module example from this link http://www.openerp.com/download/modules/5.0/.

.. i18n: Next you should be able to create different views using other files to separate
.. i18n: them from your basic/admin view.
..

Next you should be able to create different views using other files to separate
them from your basic/admin view.

.. i18n: Action creation
.. i18n: ---------------
.. i18n:   
.. i18n: Linking events to action
.. i18n: ++++++++++++++++++++++++
..

Action creation
---------------
  
Linking events to action
++++++++++++++++++++++++

.. i18n: The available type of events are:
..

The available type of events are:

.. i18n:     * **client_print_multi** (print from a list or form)
.. i18n:     * **client_action_multi** (action from a list or form)
.. i18n:     * **tree_but_open** (double click on the item of a tree, like the menu)
.. i18n:     * **tree_but_action** (action on the items of a tree) 
..

    * **client_print_multi** (print from a list or form)
    * **client_action_multi** (action from a list or form)
    * **tree_but_open** (double click on the item of a tree, like the menu)
    * **tree_but_action** (action on the items of a tree) 

.. i18n: To map an events to an action:
..

To map an events to an action:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <record model="ir.values" id="ir_open_journal_period">
.. i18n:         <field name="key2">tree_but_open</field>
.. i18n:         <field name="model">account.journal.period</field>
.. i18n:         <field name="name">Open Journal</field>
.. i18n:         <field name="value" eval="'ir.actions.wizard,%d'%action_move_journal_line_form_select"/>
.. i18n:         <field name="object" eval="True"/>
.. i18n:     </record>
..

.. code-block:: xml

    <record model="ir.values" id="ir_open_journal_period">
        <field name="key2">tree_but_open</field>
        <field name="model">account.journal.period</field>
        <field name="name">Open Journal</field>
        <field name="value" eval="'ir.actions.wizard,%d'%action_move_journal_line_form_select"/>
        <field name="object" eval="True"/>
    </record>

.. i18n: If you double click on a journal/period (object: account.journal.period), this will open the selected wizard. (id="action_move_journal_line_form_select").
..

If you double click on a journal/period (object: account.journal.period), this will open the selected wizard. (id="action_move_journal_line_form_select").

.. i18n: You can use a res_id field to allow this action only if the user click on a specific object.
..

You can use a res_id field to allow this action only if the user click on a specific object.

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <record model="ir.values" id="ir_open_journal_period">
.. i18n:         <field name="key2">tree_but_open</field>
.. i18n:         <field name="model">account.journal.period</field>
.. i18n:         <field name="name">Open Journal</field>
.. i18n:         <field name="value" eval="'ir.actions.wizard,%d'%action_move_journal_line_form_select"/>
.. i18n:         <field name="res_id" eval="3"/>
.. i18n:         <field name="object" eval="True"/>
.. i18n:     </record>
..

.. code-block:: xml

    <record model="ir.values" id="ir_open_journal_period">
        <field name="key2">tree_but_open</field>
        <field name="model">account.journal.period</field>
        <field name="name">Open Journal</field>
        <field name="value" eval="'ir.actions.wizard,%d'%action_move_journal_line_form_select"/>
        <field name="res_id" eval="3"/>
        <field name="object" eval="True"/>
    </record>

.. i18n: The action will be triggered if the user clicks on the account.journal.period n°3.
..

The action will be triggered if the user clicks on the account.journal.period n°3.

.. i18n: When you declare wizard, report or menus, the ir.values creation is automatically made with these tags:
..

When you declare wizard, report or menus, the ir.values creation is automatically made with these tags:

.. i18n:   * <wizard... />
.. i18n:   * <menuitem... />
.. i18n:   * <report... /> 
..

  * <wizard... />
  * <menuitem... />
  * <report... /> 

.. i18n: So you usually do not need to add the mapping by yourself.
..

So you usually do not need to add the mapping by yourself.
