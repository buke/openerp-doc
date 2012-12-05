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

这个文件就像任何的Python模块中一样，在程序的开始运行。它负责导入程序所需的Python文件。

.. i18n: So, if you create a "module.py" file, containing the description of your objects, you have to write one line in __init__.py::
.. i18n: 
.. i18n:     import module
..

所以，如果你想创建一个“module.py”文件，它包括你的对象的描述，在这种情况下，你需要在__init__.py文件中写一行：
    import module

.. i18n: OpenERP Module Descriptor File __openerp__.py
.. i18n: """""""""""""""""""""""""""""""""""""""""""""
..

OpenERP 模块描述文件 __openerp__.py
"""""""""""""""""""""""""""""""""""""""""""""

.. i18n: In the created module directory, you must add a **__openerp__.py** file. This file, which must be in Python format, is responsible to
..

在已经创建的模块目录中，我们需要添加这样一个文件__openerp__.py。这个文件必须是Python的格式书写，用于：

.. i18n:    1. determine the *XML files that will be parsed* during the initialization of the server, and also to
.. i18n:    2. determine the *dependencies* of the created module.
..

    1.确定所需的XML文件，server在进行初始化时将从语法上分析这些文件。
    2.确定该创建模块的依赖模块。

.. i18n: This file must contain a Python dictionary with the following values:
..

这个文件包括下面的值：

.. i18n: **name**
..

**name**

.. i18n:     The (Plain English) name of the module.
..

    (英文) 模块名称。

.. i18n: **version**
..

**version**

.. i18n:     The version of the module, on 2 digits (1.2 or 2.0).
..

    模块版本号， 2 位 (1.2 或 2.0).

.. i18n: **description**
..

**description**

.. i18n:     The module description (text) including documentation on how to use your modules.
..

    模块的描述，包含模块的使用文档。

.. i18n: **author**
..

**author**

.. i18n:     The author of the module.
..

    模块编者

.. i18n: **website**
..

**website**

.. i18n:     The website of the module.
..

    模块的网址

.. i18n: **license**
..

**license**

.. i18n:     The license of the module (default:GPL-2).
..

    模块的许可证（默认是GPL）

.. i18n: **depends**
..

**depends**

.. i18n:     List of modules on which this module depends. The base module must almost always be in the dependencies because some necessary data for the views, reports, ... are in the base module.
..
    列出该模块所依赖的其他模块，因为base模块包括模块必须的视图，报表等数据，所以base模块应该在其他所有模块的依赖中。

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

    True或是False，决定这个模块是否可安装。

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

    True或是False（默认是False），决定这个模块在数据库创建时是否安装。

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

以product模块中的__openerp__.py为例：

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

放置在init_xml中的文件必须要么是和工作流定义相关，要么是安装软件时装载数据相关，或是和示例数据相关。

.. i18n: The files in **update_xml** concern: views, reports and wizards.
..

update_xml中的文件涉及到视图，报表和向导。

.. i18n: Objects
.. i18n: """""""
..

对象
"""""""

.. i18n: All OpenERP resources are objects: menus, actions, reports, invoices, partners, ... OpenERP is based on an object relational mapping of a database to control the information. Object names are hierarchical, as in the following examples:
..

所有OpenERP的资源都是对象，如menus，actions，reports，invoices，partners... OpenERP通过数据库的对象关系映射(ORM,object relational mapping of a database)来控制信息存储。OpenERP的对象名是层次结构的，例如：

.. i18n:     * account.transfer : a money transfer
.. i18n:     * account.invoice : an invoice
.. i18n:     * account.invoice.line : an invoice line
..

    * account.transfer : a money transfer
    * account.invoice : an invoice
    * account.invoice.line : an invoice line

.. i18n: Generally, the first word is the name of the module: account, stock, sale.
..

总之，第一个单词是模块的名字：account，stock，sale

.. i18n: Other advantages of an ORM;
..

ORM的其他优点有：

.. i18n:     * simpler relations : invoice.partner.address[0].city
.. i18n:     * objects have properties and methods: invoice.pay(3400 EUR),
.. i18n:     * inheritance, high level constraints, ...
..

    * simpler relations : invoice.partner.address[0].city
    * objects have properties and methods: invoice.pay(3400 EUR),
    * inheritance, high level constraints, ...

.. i18n: It is easier to manipulate one object (example, a partner) than several tables (partner address, categories, events, ...)
..

操作一个对象比很多表要容易些。

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

OpenERP的ORM是在PostgreSQL上构造的。在OpenERP上通过对象接口或是直接使用SQL语句查询一个对象是可行的。

.. i18n: But it is dangerous to write or read directly in the PostgreSQL database, as
.. i18n: you will shortcut important steps like constraints checking or workflow
.. i18n: modification.
..

在PostgreSQL数据库中直接进行读写是非常危险的，因为可能会漏掉重要的步骤如约束检查或是工作流的修改。

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

PostgreSQL表中的数据可以使用XML文件来进行插入或更新，使得于OpenERP对象数据一致。OpenERP XML文件的主要结构是：

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

让我们回顾一下另一个例子（base模块中的base_demo.xml）：

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

上面的这个record定义了admin user：

.. i18n:     * The fields login, password, etc are straightforward.
.. i18n:     * The ref attribute allows to fill relations between the records :
..

    * 	明确定义了login，password等
	*   ref属性用于在records之间建立关系

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:        <field name="company_id" ref="main_company"/>
..

.. code-block:: xml

       <field name="company_id" ref="main_company"/>

.. i18n: The field **company_id** is a many-to-one relation from the user object to the company object, and **main_company** is the id of to associate.
..

字段company_id是一个从user object到company object的many-to-one的关系，main_company是相关联的id。

.. i18n:     * The **eval** attribute allows to put some python code in the xml: here the groups_id field is a many2many. For such a field, "[(6,0,[group_admin])]" means : Remove all the groups associated with the current user and use the list [group_admin] as the new associated groups (and group_admin is the id of another record).
.. i18n: 
.. i18n:     * The **search** attribute allows to find the record to associate when you do not know its xml id. You can thus specify a search criteria to find the wanted record. The criteria is a list of tuples of the same form than for the predefined search method. If there are several results, an arbitrary one will be chosen (the first one):
..

    * eval字段使得XML中有很多python代码：这里的groups_id字段是many2many的。“[(6,0,[group_admin])]”的意思是：移除与当前用户相关的所有groups，使用list[group_admin]作为新的相关groups（并且group_admin is the id of another record）。

    * Search字段是当你不知道它的XML id时，用来查找相关记录（record）。当你查找所需记录时可以特别指定一个查找标准。这个标准相对于预定义的查找方法最好是一个相同形式元祖的列表（The criteria is a list of tuples of the same form than for the predefined search method.）。如果有很多查找记录，程序自动选择任意一个（第一个）：

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:        <field name="partner_id" search="[]" model="res.partner"/>
..

.. code-block:: xml

       <field name="partner_id" search="[]" model="res.partner"/>

.. i18n: This is a classical example of the use of **search** in demo data: here we do not really care about which partner we want to use for the test, so we give an empty list. Notice the **model** attribute is currently mandatory.
..

这是个在demo数据中使用search的典型例子。在这里我们并不是真正想知道是哪个partner，所以我们给出了一个空的list。注意model属性是在一般情况下必须要写的。

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

T新数据的添加是通过record标签实现的。它利用一个必备的属性：model。Model是一个对象名称，可以用来实现插入数据。record标签内还有一个可选择的属性：id。如果使用了这个属性，那么在相同文件中，这个名字可以代替新创建的资源ID。

.. i18n: A record tag may contain field tags. They indicate the record's fields value. If a field is not specified the default value will be used.
..

record标签中包含field标签。他们指出record的字段值（record’s fields value）。如果这个field没有详细说明，那么它会使用默认值。

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

field标签包含的属性如下所示：

.. i18n: name : mandatory
.. i18n:   the field name
..

name : （必须有的）field name

.. i18n: eval : optional
.. i18n:   python expression that indicating the value to add
.. i18n:   
.. i18n: ref
.. i18n:   reference to an id defined in this file
..

eval : （可选）将指定值进行添加的python表达式
  
ref  :  这个文件中涉及到已定义的id

.. i18n: model
.. i18n:   model to be looked up in the search
..

model ：用于查找的model

.. i18n: search
.. i18n:   a query
..

search ：查询

.. i18n: Function tag
.. i18n: ////////////
..

Function tag
////////////

.. i18n: A function tag can contain other function tags.
..

一个功能标签包含其他的功能标签。

.. i18n: model : mandatory
.. i18n:   The model to be used
..


model ：（必须有的）要调用的model

.. i18n: name : mandatory
.. i18n:   the function given name
..

name ：（必需）function的名称

.. i18n: eval
.. i18n:   should evaluate to the list of parameters of the method to be called, excluding cr and uid
..

eval
  eval ：估值（evaluate）要调用的方法的参数列表，不计cr和uid

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

得到该标签最近子节点估值的子集

.. i18n: type : mandatory
.. i18n:   int or list
..

type ：（必需）int 或 list

.. i18n: index : mandatory
.. i18n:   int or string (a key of a dictionary)
..


index ：（必需）int or string

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

改进翻译
//////////////////////

.. i18n: .. describe:: Translating in launchpad
..

.. describe:: Translating in launchpad

.. i18n: Translations are managed by
.. i18n: the `Launchpad Web interface <https://translations.launchpad.net/openobject>`_. Here, you'll
.. i18n: find the list of translatable projects.
..

翻译由“Launchpad Web interface”管理。在这里你会找到可译项目的清单。

.. i18n: Please read the `FAQ <https://answers.launchpad.net/rosetta/+faqs>`_ before asking questions.
..

请在问问题前阅读 `FAQ <https://answers.launchpad.net/rosetta/+faqs>`_

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

和之前4.2.x的版本不同，现在翻译都是通过模块来做。所以和之前整个系统中有一个特殊i18n文件夹不同的是，现在每一个模块都有自己的i18n文件夹。此外，OpenERP可以处理.po文件作为导入导出格式。当我们安装或是更新一个模块时，安装语言的翻译文件可以自动装入系统中。OpenERP也可以产生一个.tgz文件归档，里面包括为每个选中模块组织很好的.po文件。

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

通过界面（interface）或是模块recorder来定义进程。然后放置生成的XML文件在自己的模块中。

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

视图是一种在客户端显示对象的方式。他们指示客户端如何在屏幕上显示对象数据。

.. i18n: There are two types of views:
..

视图有两种表现形式：

.. i18n:     * form views
.. i18n:     * tree views
..

    * 表单视图
    * 列表视图

.. i18n: Lists are simply a particular case of tree views.
..

Lists是tree views中的特殊情形。

.. i18n: A same object may have several views: the first defined view of a kind (*tree, form*, ...) will be used as the default view for this kind. That way you can have a default tree view (that will act as the view of a one2many) and a specialized view with more or less information that will appear when one double-clicks on a menu item. For example, the products have several views according to the product variants.
..

同一个对象有几种视图：首先定义的视图样式（tree，form，…）将会做为它默认的样式。那样的话，当你双击一个菜单项时，就有一个默认的tree view和一个特定的view显示差不多的信息。例如，products针对product变量有几种视图。

.. i18n: Views are described in XML.
..

视图都是在XML文件中进行描述的。

.. i18n: If no view has been defined for an object, the object is able to generate a view to represent itself. This can limit the developer's work but results in less ergonomic views.
..

如果一个对象没有定义视图，那么这个对象可以自己产生一个视图来显示它自己。这会限制开发者的工作，但是会导致较少的人们自己的视图设计（ergonomic views）。

.. i18n: Usage example
.. i18n: /////////////
..

Usage example
/////////////

.. i18n: When you open an invoice, here is the chain of operations followed by the client:
..

当我们打开一张发票时，接下来是在客户端上的操作：

.. i18n:     * An action asks to open the invoice (it gives the object's data (account.invoice), the view, the domain (e.g. only unpaid invoices) ).
.. i18n:     * The client asks (with XML-RPC) to the server what views are defined for the invoice object and what are the data it must show.
.. i18n:     * The client displays the form according to the view
..

    *   一个动作请求打开发票（它给出了一个对象的数据（account.invoice）,视图，域（例如仅仅是还未付款的发票））
    * 客户端请求server，什么样的视图由发票对象定义，哪些数据要显示。
    * 客户端通过视图显示表单

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

对新对象的设计限制到最低限度：创建对象并且有选择的创建视图来显示他们。PostgreSQL的table数据不用手写，因为对象会自动创建它们（除非它们已经存在）。

.. i18n: Reports
.. i18n: """""""
..

Reports
"""""""

.. i18n: OpenERP uses a flexible and powerful reporting system. Reports are generated either in PDF or in HTML. Reports are designed on the principle of separation between the data layer and the presentation layer.
..

OpenERP使用一个非常灵活和强大的报表系统。报表以PDF或是HTML的形式生成。报表是以数据层和表现层分开的原理进行设计的。

.. i18n: Reports are described more in details in the `Reporting <http://openobject.com/wiki/index.php/Developers:Developper%27s_Book/Reports>`_ chapter.
..

关于报表更多的细节在 `Reporting <http://openobject.com/wiki/index.php/Developers:Developper%27s_Book/Reports>`_ 章节。

.. i18n: Wizards
.. i18n: """""""
..

Wizards
"""""""

.. i18n: Here's an example of a .XML file that declares a wizard.
..

这里有个描述向导的.xml文件的例子：

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

向导的声明是通过使用wizard标签。想要知道更多关于向导XML文件的信息可以查看“Add A New Wizard”部分。

.. i18n: also you can add wizard in menu using following xml entry
..

或者你可以在菜单中通过使用下面的XML entry添加向导。

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

通过对象和视图，我们可以很简单的定义新的表单，lists/trees和它们间的交互。但是这还不够：你还得定义这些对象间的动态关系。
.. i18n: A few examples:
..

举个例子：

.. i18n:     * a confirmed sale order must generate an invoice, according to certain conditions
.. i18n:     * a paid invoice must, only under certain conditions, start the shipping order
..

    * 在一般的情况下，一个已确定的销售订单必须生成一张发货单。
    * 只是在确认发货单已付款的前提下，才会开出运送清单。

.. i18n: The workflows describe these interactions with graphs. One or several workflows may be associated to the objects. Workflows are not mandatory; some objects don't have workflows.
..

工作流使用图表描述这些交互，一个或几个工作流相关到对象。工作流是非必须的；一些对象就没有工作流。

.. i18n: Below is an example workflow used for sale orders. It must generate invoices and shipments according to certain conditions.
..

下面的工作流用于销售订单的例子。在一定的条件下，它必须产生发货单和出货。

.. i18n: .. figure::  images/arch_workflow_sale.png
.. i18n:    :scale: 85
.. i18n:    :align: center
..

.. figure::  images/arch_workflow_sale.png
   :scale: 85
   :align: center

.. i18n: In this graph, the nodes represent the actions to be done:
..

在这张图表中节点代表着要做的动作。

.. i18n:     * create an invoice,
.. i18n:     * cancel the sale order,
.. i18n:     * generate the shipping order, ...
..

    * 创建发票
    * 取消销售订单
    * 生成装货单, ...

.. i18n: The arrows are the conditions;
..

上面的箭头代表条件：

.. i18n:     * waiting for the order validation,
.. i18n:     * invoice paid,
.. i18n:     * click on the cancel button, ...
..

     1.等待订单获得批准
     2.发票支付
     3.点击取消按钮，。。。

.. i18n: The squared nodes represent other Workflows;
..

方格样式的节点代表其他的工作流：

.. i18n:     * the invoice
.. i18n:     * the shipping
..

    * 发票
    * 发货

.. i18n: OpenERP Module Descriptor File : __openerp__.py
.. i18n: -----------------------------------------------
..

OpenERP 模块描述文件 : __openerp__.py
-----------------------------------------------

.. i18n: Normal Module
.. i18n: +++++++++++++
..

一般模块
+++++++++++++

.. i18n: In the created module directory, you must add a **__openerp__.py** file. This file, which must be in Python format, is responsible to
..

在已创建模块的目录下，你必须添加一个__openerp__.py文件。这个文件必须在Python的格式下，负责：

.. i18n:    1. determine the XML files that will be parsed during the initialization of the server, and also to
.. i18n:    2. determine the dependencies of the created module.
..

   1. 确定所需的XML文件，server在进行初始化时将从语法上分析这些文件。
   2. 1.确定已创建模块的依赖。

.. i18n: This file must contain a Python dictionary with the following values:
..

这个文件包括下面的值：

.. i18n: **name**
..

**name**

.. i18n:     The (Plain English) name of the module.
..

    (英文)名称.

.. i18n: **version**
..

**version**

.. i18n:     The version of the module.
..

    版本

.. i18n: **description**
..

**description**

.. i18n:     The module description (text).
..

    描述

.. i18n: **author**
..

**author**

.. i18n:     The author of the module.
..

    模块的作者
	
.. i18n: **website**
..

**website**

.. i18n:     The website of the module.
..

    模块的网站

.. i18n: **license**
..

**license**

.. i18n:     The license of the module (default:GPL-2).
..

    模块的授权协议(默认AGPL).

.. i18n: **depends**
..

**depends**

.. i18n:     List of modules on which this module depends. The base module must almost always be in the dependencies because some necessary data for the views, reports, ... are in the base module.
..

    列出该模块所依赖的其他模块，因为base模块包括模块必须的视图，报表等数据，所以base模块应该在其他所有模块的依赖中。

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

    True或是False，决定这个模块是否可安装。

.. i18n: **active**
..

**active**

.. i18n:     True or False (default: False). Determines the modules that are installed on the database creation.
..

    True或是False（默认是False），决定这个模块在数据库创建时是否安装。

.. i18n: Example
.. i18n: """""""
..

示例
"""""""

.. i18n: Here is an example of __openerp__.py file for the *product* module:
..

以product模块中的__openerp__.py为例：

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

放置在init_xml中的文件必须要么是和工作流相关，要么是安装软件时装载数据相关，或是和示例数据相关。

.. i18n: The files in **update_xml** concern: views, reports and wizards.
..

update_xml中的文件涉及到视图，报表和向导。

.. i18n: Profile Module
.. i18n: ++++++++++++++
..

Profile 模块
++++++++++++++

.. i18n: The purpose of a profile is to initialize OpenERP with a set of modules directly after the database has been created. A profile is a special kind of module that contains no code, only *dependencies on other modules*.
..

一个profile的目的是在数据库创建后直接使用一组模块来初始化OpenERP。这个profile是一种特殊的模块，它不包含代码，只是 *依赖于其他的模块* 。

.. i18n: In order to create a profile, you only have to create a new directory in server/addons (you *should* call this folder profile_modulename), in which you put an *empty* __init__.py file (as every directory Python imports must contain an __init__.py file), and a __openerp__.py whose structure is as follows :
..

为了创建一个新的profile，你需要在server/addons里建一个新目录（可以给它取名为profile_modulename）。在新目录里放一个空的__init__.py文件和__openerp__.py。这个文件的结构是：

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

示例
"""""""

.. i18n: Here's the code of the file
.. i18n: server/bin/addons/profile_manufacturing/__openerp__.py, which corresponds to the
.. i18n: manufacturing industry profile in OpenERP.
..

我们以文件server/bin/addons/profile_manufacturing/__openerp__.py中的代码为例，它对应着OpenERP中的manufacturing industry profile。

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

创建模块
---------------

.. i18n: Getting the skeleton directory
.. i18n: ++++++++++++++++++++++++++++++
..

Getting the skeleton directory
++++++++++++++++++++++++++++++

.. i18n: You can copy __openerp__.py and __init__.py from any other module to create a new module into a new directory.
..

你可以从其他任意模块中复制文件__openerp__.py和__init__.py到一个新目录来创建一个新模块。

.. i18n: As an example on Ubuntu:
.. i18n: ::
.. i18n: 
.. i18n: 	$ cd ~/workspace/stable/stable_addons_5.0/
.. i18n: 	$ mkdir travel
.. i18n: 	$ sudo cp ~/workspace/stable/stable_addons_5.0/hr/__openerp__.py ~/workspace/stable/stable_addons_5.0/travel
.. i18n: 	sudo cp ~/workspace/stable/stable_addons_5.0/hr/__init__.py ~/workspace/stable/stable_addons_5.0/travel
..

Ubuntu中一个例子：
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

你如果想修改这个目录，你需要设置自己的权限在这个目录上: ::

    $ sudo chown -R `whoami` travel

.. i18n: You got yourself the directory for a new module there, and a skeleton
.. i18n: structure, but you still need to change a few things inside the module's
.. i18n: definition...
..

进入新模块的目录，里面有个框架结构，你仍需要去更改模块定义里面的东西。

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

为了更改模块“travel”里面的默认设置，我们需要进入“travel”目录，编辑__openerp__.py文件。 ::

    $ cd travel
    $ gedit __openerp__.py

.. i18n: The file looks like this:
..

文件里面类似下面：

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

你可能会更改任意你觉得正确的东西，像下面这样：

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

注意“active”字段变成了true。

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

现在你需要更新travel.py脚本以满足你自己的模块的需要。我们建议你遵循Flash教程，或是从20minutes教程页面来下载travel agent模块。  ::

    The documentation below is overlapping the two next step in this wiki tutorial,
    so just consider them as a help and head towards the next two pages first...

.. i18n: The travel.py file should initially look like this:
..

travel.py文件应该看起来是这样：

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

理想情况下，你会拷贝那些代码几次来创建你所需要的实体（travel_airport, travel_room, travel_flight）。这就是你的对象的数据库结构，但是你真的不需要担心数据库端。当你安装模块时，这个文件会为你创建系统架构。

.. i18n: Customizing the view
.. i18n: ++++++++++++++++++++
..

Customizing the view
++++++++++++++++++++

.. i18n: You can now move on to editing the views. To do this, edit the custom_view.xml file. It should first look like this:
..

接下来你可以编辑视图。编辑custom_view.xml文件，像这样：

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

就像你看到的，这是个accounting系统的例子。

.. i18n: Defining a view is defining the interfaces the user will get when accessing
.. i18n: your module. Just defining a bunch of fields here should already get you
.. i18n: started on a complete interface. However, due to the complexity of doing it
.. i18n: right, we recommend, once again, that download the travel agency module example from this link http://www.openerp.com/download/modules/5.0/.
..

定义视图就是定义访问你的模块时的用户界面。这里定义的这些字段已经是一个完整的界面。然而，由于做这个的复杂性，我们建议，再一次，从链接http://www.openerp.com/download/modules/5.0/下载travel agent模块。

.. i18n: Next you should be able to create different views using other files to separate
.. i18n: them from your basic/admin view.
..

下次你可以使用其他的文件来定义不同的视图，并且在你的basic/admin视图中分开它们。

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

可用类型的事件是：

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

从事件到动作的映射是：

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

如果你双击journal/period (object: account.journal.period),将会打开一个选中的向导(id=”action_move_journal_line_form_select”).

.. i18n: You can use a res_id field to allow this action only if the user click on a specific object.
..

只是当用户点击特定的对象时，你可以使用res_id字段来允许这个动作。

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

当用户点击account.journal.period n°3时，这个动作将会触发。

.. i18n: When you declare wizard, report or menus, the ir.values creation is automatically made with these tags:
..

当你声明向导，报表或是菜单时，ir.values的创建会自动由下面的标签完成：

.. i18n:   * <wizard... />
.. i18n:   * <menuitem... />
.. i18n:   * <report... /> 
..

  * <wizard... />
  * <menuitem... />
  * <report... /> 

.. i18n: So you usually do not need to add the mapping by yourself.
..

所以一般不需要自己加映射。
