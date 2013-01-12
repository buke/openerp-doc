.. i18n: .. _part-5-migration-upgrading-testing:
.. i18n: 
.. i18n: ======================================
.. i18n: Serialization, Migration and Upgrading
.. i18n: ======================================
..

.. _part-5-migration-upgrading-testing:

======================================
持久化，迁移和升级
======================================

.. i18n: .. _data-serialization:
.. i18n: 
.. i18n: Data Serialization
.. i18n: ==================
..

.. _data-serialization:

数据序列化
==================

.. i18n: During OpenERP installation, two steps are necessary to create and feed the database:
..

在 OpenERP 安装的时候, 创建和填充数据库是必须的两个步骤:

.. i18n:    1. Create the SQL tables
.. i18n:    2. Insert the different data into the tables
..

   1. 创建 SQL 表
   2. 插入不同的数据到表中

.. i18n: The creation (or modification in the case of an upgrade) of SQL tables is automated thanks to the description of objects in the server.
..

由于服务器中的对象描述，SQL表的创建和修改时自动的.

.. i18n: With OpenERP, everything except the business logic of objects is stored in the database. 
.. i18n: We find for example:
..

使用 OpenERP, 除了对象的业务逻辑以外，其它都存在数据库中. 
例如(不存入数据库):

.. i18n:     * the definitions of the reports,
.. i18n:     * the default values for fields,
.. i18n:     * the definition of client interfaces for each document (views),
.. i18n:     * the relationships between menus, buttons and actions
.. i18n:     * etc.
..

    * reports的定义,
    * fields的默认值,
    * 每个文档(views)的用户接口的定义 ,
    * 菜单，按钮和动作的关系
    * 等等其他.

.. i18n: There must be a mechanism to describe, modify and reload these different kinds of data. 
.. i18n: OpenERP data may be specified in CSV, XML or YAML serialization files provided by 
.. i18n: modules, and loaded during module installation/upgrade in order to fill or update the
.. i18n: database tables.
..

必须有一个机制去描述, 修改和装载这些不同的数据. 
OpenERP 的数据可以以模块提供的 CSV, XML or YAML 的序列化文件的形式指定模块 
modules, 并在模块安装和升级时装载以便填充和升级数据库表.

.. i18n: .. _xml-serialization:
.. i18n: 
.. i18n: XML Data Serialization
.. i18n: ----------------------
..

.. _xml-serialization:

XML 数据序列化
----------------------

.. i18n: Since version 4.2, OpenERP provides an XML-based data serialization format.
..

4.2版本之后, OpenERP 提供基于XML的数据序列化格式.

.. i18n: The basic format of an OpenERP XML file is as follows:
..

基本的 OpenERP XML 文件格式如下:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:      <?xml version="1.0"?>
.. i18n:      <openerp>
.. i18n:          <data>
.. i18n:          <record model="model.name_1" id="id_name_1">
.. i18n:              <field name="field1">
.. i18n:                  field1 content
.. i18n:              </field>
.. i18n:              <field name="field2">
.. i18n:                  field2 content
.. i18n:              </field>
.. i18n:              (...)
.. i18n:          </record>
.. i18n:          <record model="model.name_2" id="id_name_2">
.. i18n:              (...)
.. i18n:          </record>
.. i18n:          (...)
.. i18n:          </data>
.. i18n:      </openerp>
..

.. code-block:: xml

     <?xml version="1.0"?>
     <openerp>
         <data>
         <record model="model.name_1" id="id_name_1">
             <field name="field1">
                 field1 content
             </field>
             <field name="field2">
                 field2 content
             </field>
             (...)
         </record>
         <record model="model.name_2" id="id_name_2">
             (...)
         </record>
         (...)
         </data>
     </openerp>

.. i18n: Fields contents are strings that must be encoded as UTF-8 in XML files.
..

Fields 内容是 strings 类型,保存在以 UTF-8 编码的 XML 格式的文件中.

.. i18n: Let's review an example taken from the OpenERP source (base_demo.xml in the base module):
..

下面是一个来自 OpenERP 的源码的例子 (base_demo.xml 在 base 模块中):

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:        <record model="res.company" id="main_company">
.. i18n:            <field name="name">OpenERP SA</field>
.. i18n:            <field name="partner_id" ref="main_partner"/>
.. i18n:            <field name="currency_id" ref="EUR"/>
.. i18n:        </record>
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

       <record model="res.company" id="main_company">
           <field name="name">OpenERP SA</field>
           <field name="partner_id" ref="main_partner"/>
           <field name="currency_id" ref="EUR"/>
       </record>

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

最后的字段定义的 admin user :

.. i18n:     * The fields login, password, etc are straightforward.
.. i18n:     * The **ref** attribute allows to fill relations between the records :
..

    * 登录，密码等字段比较直接.
    * **ref** 属性用于填充两个记录之间的关系 :

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <field name="company_id" ref="main_company"/>
..

.. code-block:: xml

    <field name="company_id" ref="main_company"/>

.. i18n: The``company_id`` field is a many-to-one relation from the user object to the company object, and **main_company** is the id of to associate.
..

``company_id`` 字段是一个多对一(many2one) 从USER对象到 COMPANY 对象, **main_company** 是关系的 id.

.. i18n:     * The **eval** attribute allows to put some python code in the xml: here the groups_id field is a many2many. For such a field, "[(6,0,[group_admin])]" means : Remove all the groups associated with the current user and use the list [group_admin] as the new associated groups (and group_admin is the id of another record).
.. i18n: 
.. i18n:     * The **search** attribute allows to find the record to associate when you do not know its xml id. You can thus specify a search criteria to find the wanted record. The criteria is a list of tuples of the same form than for the predefined search method. If there are several results, an arbitrary one will be chosen (the first one):
..

    * **eval** 属性允许将一些 python 代码放进 xml 中: 这里 groups_id 字段是一个多对多(many2many)的关系. 对于这样一个字段, "[(6,0,[group_admin])]" 的意思为 : 删除所有与当前用户相关的组，并使用 [group_admin] 作为新的关联组 (and group_admin 是另一个记录的 id ).

    * **search** 属性允许你在不指定 xml id 的情况下. 查找相关的记录. 你可以指定一个搜索条目来寻找想要查询的字段. 条目是一个 tuple 的 lists 用于预定义的搜索方法, 如果有多个结果， 通常选中(第一个):

.. i18n:     <field name="partner_id" search="[]" model="res.partner"/>
..

    <field name="partner_id" search="[]" model="res.partner"/>

.. i18n: This is a classical example of the use of ``search`` in demo data: here we do not really care about which partner we want to use for the test, so we give an empty list. Notice the **model** attribute is currently mandatory.
..

只是 ``search`` 在演示数据的一个经典的例子：这里我们并不关心用哪一个 partner 来进行测试，所以我们给出一个空的 list . 注意 **model** 属性是必须的.

.. i18n: Some typical XML elements are described below.
..

一些典型的 XML 元素描述如下.

.. i18n: Record Tag
.. i18n: ++++++++++
..

记录标签
++++++++++

.. i18n: The addition of new data is made with the **record** tag. This one takes a mandatory attribute : **model**. Model is the object name where the insertion has to be done. The tag record can also take an optional attribute: **id**. If this attribute is given, a variable of this name can be used later on, in the same file, to make reference to the newly created resource ID.
..

通过 **record** 标签来实现新数据的添加. 这里 : **model** 属性是必须的. Model 是插入数据的对象名. 它还有一个可选的属性: **id**. 如果给出该属性, 在同一个文件中, 这个名字对应的变量将在以后使用, 以便生成新产生资源 ID 的引用.

.. i18n: A **record** tag may contain field tags. They indicate the record's **fields** value. If a field is not specified the default value will be used.
..

一个 **record** 标签可以包含多个 field 标签. 他们指定了记录的 **fields** 值. 如果不指定一个 field 默认值将会被使用.

.. i18n: Example
.. i18n: """""""
..

例子
"""""""

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

.. i18n: field tag
.. i18n: +++++++++
..

field tag
+++++++++

.. i18n: The attributes for the field tag are the following:
..

对应的属性如下:

.. i18n:     * **name**
.. i18n:           o mandatory attribute indicating the field name
.. i18n:     * **eval**
.. i18n:           o python expression that indicating the value to add
.. i18n:     * **ref**
.. i18n:           o reference to an id defined in this file
..

    * **name**
          o 必须的属性，用于指定字段名称
    * **eval**
          o 用于指定添加值的 python 语句
    * **ref**
          o 定义在此文件中的 id 的引用

.. i18n: function tag
.. i18n: ++++++++++++
..

function tag
++++++++++++

.. i18n:     * model:
.. i18n:     * name:
.. i18n:     * eval
.. i18n:           o should evaluate to the list of parameters of the method to be called, excluding cr and uid
..

    * model:
    * name:
    * eval
          o 用于评价将被调用的方法的属性列表，包括 cr 和 uid 

.. i18n: Example
.. i18n: """""""
..

例子
"""""""

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <function 
.. i18n:     	model="ir.ui.menu" 
.. i18n:     	name="search" 
.. i18n:     	eval="[[('name','=','Operations')]]"/>
..

.. code-block:: xml

    <function 
    	model="ir.ui.menu" 
    	name="search" 
    	eval="[[('name','=','Operations')]]"/>

.. i18n: getitem tag
.. i18n: +++++++++++
..

getitem tag
+++++++++++

.. i18n: Takes a subset of the evaluation of the last child node of the tag.
..

采用标签最后一个子节点的子集.

.. i18n:     * type
.. i18n:           - int or list
.. i18n:     * index
.. i18n:     * int or string (a key of a dictionary)
..

    * type
          - int or list
    * index
    * int or string (a key of a dictionary)

.. i18n: Example
.. i18n: """""""
..

例子
"""""""

.. i18n: Evaluates to the first element of the list of ids returned by the function node:
..

节点返回的一个 ids 的列表的第一个元素:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <getitem index="0" type="list">
.. i18n:         <function 
.. i18n:         	model="ir.ui.menu" 
.. i18n:         	name="search" 
.. i18n:         	eval="[[('name','=','Operations')]]"/>
.. i18n:     </getitem>
..

.. code-block:: xml

    <getitem index="0" type="list">
        <function 
        	model="ir.ui.menu" 
        	name="search" 
        	eval="[[('name','=','Operations')]]"/>
    </getitem>

.. i18n: .. _yaml-serialization:
.. i18n: 
.. i18n: YAML Data Serialization
.. i18n: -----------------------
..

.. _yaml-serialization:

YAML 数据序列化
-----------------------

.. i18n: YAML is a **human-readable** data serialization format that takes concepts from
.. i18n: programming languages such as C, Perl, and **Python**, and ideas from **XML**
.. i18n: and the data format of electronic mail.
.. i18n: YAML stands for *YAML Ain't Markup Language* (yes, that's a recursive acronym).
.. i18n: YAML is available as a format for OpenERP data **as of OpenERP 6.0**, featuring
.. i18n: the following advantages:
..

YAML 是 **human-readable** 可读的数据序列化格式 概念源于 C, Perl, **Python**, 主意来自 **XML**
和电子邮件的数据格式.
YAML stands for *YAML Ain't Markup Language* (yes, that's a recursive acronym).
YAML 用于 OpenERP 数据格式 **as of OpenERP 6.0**, 有以下优点:

.. i18n:     * User friendly format as an alternative to our current XML data format.
.. i18n:     * Same system to load data or tests, integrated in modules.
.. i18n:     * Built in OpenERP so that you can develop complex Python tests.
.. i18n:     * Simpler for non developers to write functional tests.
..

    * 作为当前的 XML 格式的一个用户友善的备选格式.
    * 在相同的系统模块中进行数据的装载，测试集成.
    * 内建与 OpenERP 以便开发复杂的 Python 测试.
    * 方便非开发人员写功能测试.

.. i18n: The following section compares an XML record with an equivalent YAML record.
..

下面是一个 XML 记录和 YAML 记录的比较.

.. i18n: First the XML Record using the current XML serialization format
.. i18n: (see :ref:`previous section <xml-serialization>`)
..

首先，XML 记录使用当前的 XML 序列化格式：
(see :ref:`previous section <xml-serialization>`)

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:   <!--
.. i18n:       Resource: sale.order
.. i18n:   -->
.. i18n: 
.. i18n:   <record id="order" model="sale.order">
.. i18n:     <field name="shop_id" ref="shop"/>
.. i18n:     <field model="product.pricelist" name="pricelist_id" search="[]"/>
.. i18n:     <field name="user_id" ref="base.user_root"/>
.. i18n:     <field model="res.partner" name="partner_id" search="[]"/>
.. i18n:     <field model="res.partner.address" name="partner_invoice_id search="[]"/>
.. i18n:     <field model="res.partner.address" name="partner_shipping_id" search="[]"/>
.. i18n:     <field model="res.partner.address" name="partner_order_id" search="[]"/>
.. i18n:   </record>
.. i18n: 
.. i18n:   <!--
.. i18n:         Resource: sale.order.line
.. i18n:   -->
.. i18n: 
.. i18n:   <record id="line" model="sale.order.line">
.. i18n:     <field name="order_id" ref="order"/>
.. i18n:     <field name="name">New server config + material</field>
.. i18n:     <field name="price_unit">123</field>
.. i18n:   </record>
.. i18n: 
.. i18n:   <record id="line1" model="sale.order.line">
.. i18n:     <field name="order_id" ref="order"/>
.. i18n:     <field name="name">[PC1] Basic PC</field>
.. i18n:     <field name="price_unit">450</field>
.. i18n:   </record>
..

.. code-block:: xml

  <!--
      Resource: sale.order
  -->

  <record id="order" model="sale.order">
    <field name="shop_id" ref="shop"/>
    <field model="product.pricelist" name="pricelist_id" search="[]"/>
    <field name="user_id" ref="base.user_root"/>
    <field model="res.partner" name="partner_id" search="[]"/>
    <field model="res.partner.address" name="partner_invoice_id search="[]"/>
    <field model="res.partner.address" name="partner_shipping_id" search="[]"/>
    <field model="res.partner.address" name="partner_order_id" search="[]"/>
  </record>

  <!--
        Resource: sale.order.line
  -->

  <record id="line" model="sale.order.line">
    <field name="order_id" ref="order"/>
    <field name="name">New server config + material</field>
    <field name="price_unit">123</field>
  </record>

  <record id="line1" model="sale.order.line">
    <field name="order_id" ref="order"/>
    <field name="name">[PC1] Basic PC</field>
    <field name="price_unit">450</field>
  </record>

.. i18n: YAML Record
.. i18n: +++++++++++
.. i18n: ::
.. i18n: 
.. i18n:     #<!--
.. i18n:     #       Resource: sale.order
.. i18n:     #   -->
.. i18n: 
.. i18n:     -
.. i18n:      !record {model: sale.order, id: sale_order_so4}:
.. i18n:        amount_total: 3263.0
.. i18n:        amount_untaxed: 3263.0
.. i18n:        create_date: '2010-04-06 10:45:14'
.. i18n:        date_order: '2010-04-06'
.. i18n:        invoice_quantity: order
.. i18n:        name: SO001
.. i18n:        order_line:
.. i18n:          - company_id: base.main_company
.. i18n:            name: New server config + material
.. i18n:            order_id: sale_order_so4
.. i18n:            price_unit: 123.0
.. i18n:          - company_id: base.main_company
.. i18n:            name: '[PC1] Basic PC'
.. i18n:            order_id: sale_order_so4
.. i18n:            price_unit: 450.0
.. i18n:        order_policy: manual
.. i18n:        partner_id: base.res_partner_agrolait
.. i18n:        partner_invoice_id: base.main_address
.. i18n:        partner_order_id: base.main_address
.. i18n:        partner_shipping_id: base.main_address
.. i18n:        picking_policy: direct
.. i18n:        pricelist_id: product.list0
.. i18n:        shop_id: sale.shop
..

YAML 记录
+++++++++++
::

    #<!--
    #       Resource: sale.order
    #   -->

    -
     !record {model: sale.order, id: sale_order_so4}:
       amount_total: 3263.0
       amount_untaxed: 3263.0
       create_date: '2010-04-06 10:45:14'
       date_order: '2010-04-06'
       invoice_quantity: order
       name: SO001
       order_line:
         - company_id: base.main_company
           name: New server config + material
           order_id: sale_order_so4
           price_unit: 123.0
         - company_id: base.main_company
           name: '[PC1] Basic PC'
           order_id: sale_order_so4
           price_unit: 450.0
       order_policy: manual
       partner_id: base.res_partner_agrolait
       partner_invoice_id: base.main_address
       partner_order_id: base.main_address
       partner_shipping_id: base.main_address
       picking_policy: direct
       pricelist_id: product.list0
       shop_id: sale.shop

.. i18n: YAML Tags
.. i18n: +++++++++
.. i18n: data
.. i18n: """"
.. i18n: * **Tag**: data
..

YAML Tags
+++++++++
data
""""
* **Tag**: data

.. i18n: * **Compulsory attributes**: None
.. i18n: 
.. i18n: * **Optional attributes**: noupdate \: 0 | 1
.. i18n: 
.. i18n: * **Child_tags**:
.. i18n: 
.. i18n:   - menuitem
.. i18n: 
.. i18n:   - record
.. i18n: 
.. i18n:   - workflow
.. i18n: 
.. i18n:   - delete
.. i18n: 
.. i18n:   - act_window
.. i18n: 
.. i18n:   - assert
.. i18n: 
.. i18n:   - report
.. i18n: 
.. i18n:   - function
.. i18n: 
.. i18n:   - ir_set
.. i18n: 
.. i18n: * **Example**:
.. i18n:   ::
.. i18n: 
.. i18n:     -
.. i18n:       !context
.. i18n:        noupdate: 0
..

* **Compulsory attributes**: None

* **Optional attributes**: noupdate \: 0 | 1

* **Child_tags**:

  - menuitem

  - record

  - workflow

  - delete

  - act_window

  - assert

  - report

  - function

  - ir_set

* **Example**:
  ::

    -
      !context
       noupdate: 0

.. i18n: record
.. i18n: """"""
.. i18n: * **Tag**: record
..

record
""""""
* **Tag**: record

.. i18n: * **Compulsory attributes**:
.. i18n:                 - model
.. i18n: 
.. i18n: * **Optional attributes**: noupdate \: 0 | 1
.. i18n: 
.. i18n: * **Child_tags**:
.. i18n:             - field
.. i18n: 
.. i18n: * **Optional attributes**:
.. i18n:                       - id
.. i18n: 
.. i18n:                       - forcreate
.. i18n: 
.. i18n:                       - context
.. i18n: 
.. i18n: * **Example**:
.. i18n:   ::
.. i18n: 
.. i18n:     -
.. i18n:       !record {model: sale.order, id: order}:
.. i18n:          name: "[PC1] Basic PC"
.. i18n:          amount_total: 3263.0
.. i18n:          type_ids:
.. i18n:            - project_tt_specification
.. i18n:            - project_tt_development
.. i18n:            - project_tt_testing
.. i18n:          order_line:
.. i18n:              - name: New server config
.. i18n:                 order_id: sale_order_so4
.. i18n:              - name: '[PC1] Basic PC'
.. i18n:                 order_id: sale_order_so4
..

* **Compulsory attributes**:
                - model

* **Optional attributes**: noupdate \: 0 | 1

* **Child_tags**:
            - field

* **Optional attributes**:
                      - id

                      - forcreate

                      - context

* **Example**:
  ::

    -
      !record {model: sale.order, id: order}:
         name: "[PC1] Basic PC"
         amount_total: 3263.0
         type_ids:
           - project_tt_specification
           - project_tt_development
           - project_tt_testing
         order_line:
             - name: New server config
                order_id: sale_order_so4
             - name: '[PC1] Basic PC'
                order_id: sale_order_so4

.. i18n: field
.. i18n: """""
..

field
"""""

.. i18n: * **Tag**: field
.. i18n: 
.. i18n: * **Compulsory attributes**:
.. i18n:                 - name
.. i18n: 
.. i18n: * **Optional attributes**:
.. i18n:                       - type
.. i18n: 
.. i18n:                       - ref
.. i18n: 
.. i18n:                       - eval
.. i18n: 
.. i18n:                       - domain
.. i18n: 
.. i18n:                       - search
.. i18n: 
.. i18n:                       - model
.. i18n: 
.. i18n:                       - use
.. i18n: * **Child_tags**:
.. i18n:             - text node
.. i18n: 
.. i18n: * **Example**:
.. i18n:   ::
.. i18n: 
.. i18n:     -price_unit: 450
.. i18n:     -product_id: product.product_product_pc1
..

* **Tag**: field

* **Compulsory attributes**:
                - name

* **Optional attributes**:
                      - type

                      - ref

                      - eval

                      - domain

                      - search

                      - model

                      - use
* **Child_tags**:
            - text node

* **Example**:
  ::

    -price_unit: 450
    -product_id: product.product_product_pc1

.. i18n: workflow
.. i18n: """"""""
.. i18n: * **Tag**: workflow
..

workflow
""""""""
* **Tag**: workflow

.. i18n: * **Compulsory attributes**:
.. i18n:                 - model
.. i18n: 
.. i18n:                 - action
.. i18n: 
.. i18n: * **Optional attributes**:
.. i18n:                  - uid
.. i18n: 
.. i18n:                  - ref
.. i18n: 
.. i18n: * **Child_tags**:
.. i18n:             - value
.. i18n: 
.. i18n: * **Example**:
.. i18n:   ::
.. i18n: 
.. i18n:    -
.. i18n:     !workflow {action: invoice_open, model: account.invoice}:
.. i18n:      - eval: "obj(ref('test_order_1')).invoice_ids[0].id"
.. i18n:        model: sale.order
.. i18n:      - model: account.account
.. i18n:        search: [('type', '=', 'cash')]
..

* **Compulsory attributes**:
                - model

                - action

* **Optional attributes**:
                 - uid

                 - ref

* **Child_tags**:
            - value

* **Example**:
  ::

   -
    !workflow {action: invoice_open, model: account.invoice}:
     - eval: "obj(ref('test_order_1')).invoice_ids[0].id"
       model: sale.order
     - model: account.account
       search: [('type', '=', 'cash')]

.. i18n: function
.. i18n: """"""""
.. i18n: * **Tag**: function
..

function
""""""""
* **Tag**: function

.. i18n: * **Compulsory attributes**:
.. i18n:                 - model
.. i18n: 
.. i18n:                 - name
.. i18n: 
.. i18n: * **Optional attributes**:
.. i18n:                  - id
.. i18n: 
.. i18n:                  - eval
.. i18n: 
.. i18n: * **Child_tags**:
.. i18n:             - value
.. i18n: 
.. i18n:             - function
.. i18n: 
.. i18n: * **Example**:
.. i18n:   ::
.. i18n: 
.. i18n:    -
.. i18n:     !function {model: account.invoice, name: pay_and_reconcile}:
.. i18n:      -eval: "[obj(ref('test_order_1')).id]"
.. i18n:       model: sale.order
..

* **Compulsory attributes**:
                - model

                - name

* **Optional attributes**:
                 - id

                 - eval

* **Child_tags**:
            - value

            - function

* **Example**:
  ::

   -
    !function {model: account.invoice, name: pay_and_reconcile}:
     -eval: "[obj(ref('test_order_1')).id]"
      model: sale.order

.. i18n: value
.. i18n: """"""
.. i18n: * **Tag**: value
..

value
""""""
* **Tag**: value

.. i18n: * **Compulsory attributes**: None
.. i18n: 
.. i18n: * **Optional attributes**:
.. i18n:                  - model
.. i18n: 
.. i18n:                  - search
.. i18n: 
.. i18n:                  - eval
.. i18n: 
.. i18n: * **Child_tags**: None
.. i18n: 
.. i18n: * **Example**:
.. i18n:   ::
.. i18n: 
.. i18n:      -eval: "[obj(ref('test_order_1')).id]"
.. i18n:       model: sale.order
..

* **Compulsory attributes**: None

* **Optional attributes**:
                 - model

                 - search

                 - eval

* **Child_tags**: None

* **Example**:
  ::

     -eval: "[obj(ref('test_order_1')).id]"
      model: sale.order

.. i18n: menuitem
.. i18n: """"""""
.. i18n: * **Tag**: menuitem
..

menuitem
""""""""
* **Tag**: menuitem

.. i18n: * **Compulsory attributes**: None
.. i18n: 
.. i18n: * **Optional attributes**:
.. i18n:                  - id
.. i18n: 
.. i18n:                  - name
.. i18n: 
.. i18n:                  - parent
.. i18n: 
.. i18n:                  - icon
.. i18n: 
.. i18n:                  - action
.. i18n: 
.. i18n:                  - string
.. i18n: 
.. i18n:                  - sequence
.. i18n: 
.. i18n:                  - groups
.. i18n: 
.. i18n:                  - type
.. i18n: 
.. i18n:                  - menu
.. i18n: 
.. i18n: * **Child_tags**: None
.. i18n: 
.. i18n: * **Example**:
.. i18n:   ::
.. i18n: 
.. i18n:      -
.. i18n:       !menuitem {sequence: 20, id: menu_administration,
.. i18n:        name: Administration,
.. i18n:        icon: terp-administration}
..

* **Compulsory attributes**: None

* **Optional attributes**:
                 - id

                 - name

                 - parent

                 - icon

                 - action

                 - string

                 - sequence

                 - groups

                 - type

                 - menu

* **Child_tags**: None

* **Example**:
  ::

     -
      !menuitem {sequence: 20, id: menu_administration,
       name: Administration,
       icon: terp-administration}

.. i18n: act_window
.. i18n: """"""""""
.. i18n: * **Tag**: act_window
..

act_window
""""""""""
* **Tag**: act_window

.. i18n: * **Compulsory attributes**:
.. i18n:                 - id
.. i18n: 
.. i18n:                 - name
.. i18n: 
.. i18n:                 - res_model
.. i18n: 
.. i18n: * **Optional attributes**:
.. i18n: 
.. i18n:                 - domain
.. i18n: 
.. i18n:                 - src_model
.. i18n: 
.. i18n:                 - context
.. i18n: 
.. i18n:                 - view
.. i18n: 
.. i18n:                 - view_id
.. i18n: 
.. i18n:                 - view_type
.. i18n: 
.. i18n:                 - view_mode
.. i18n: 
.. i18n:                 - multi
.. i18n: 
.. i18n:                 - target
.. i18n: 
.. i18n:                 - key2
.. i18n: 
.. i18n:                 - groups
.. i18n: 
.. i18n: * **Child_tags**: None
.. i18n: 
.. i18n: * **Example**:
.. i18n:   ::
.. i18n: 
.. i18n:      -
.. i18n:        !act_window {target: new,
.. i18n:        res_model: wizard.ir.model.menu.create,
.. i18n:        id:act_menu_create, name: Create Menu}
..

* **Compulsory attributes**:
                - id

                - name

                - res_model

* **Optional attributes**:

                - domain

                - src_model

                - context

                - view

                - view_id

                - view_type

                - view_mode

                - multi

                - target

                - key2

                - groups

* **Child_tags**: None

* **Example**:
  ::

     -
       !act_window {target: new,
       res_model: wizard.ir.model.menu.create,
       id:act_menu_create, name: Create Menu}

.. i18n: report
.. i18n: """"""
.. i18n: * **Tag**: report
..

report
""""""
* **Tag**: report

.. i18n: * **Compulsory attributes**:
.. i18n:                 - string
.. i18n: 
.. i18n:                 - model
.. i18n: 
.. i18n:                 - name
.. i18n: 
.. i18n: * **Optional attributes**:
.. i18n: 
.. i18n:                 - id
.. i18n: 
.. i18n:                 - report
.. i18n: 
.. i18n:                 - multi
.. i18n: 
.. i18n:                 - menu
.. i18n: 
.. i18n:                 - keyword
.. i18n: 
.. i18n:                 - rml
.. i18n: 
.. i18n:                 - sxw
.. i18n: 
.. i18n:                 - xml
.. i18n: 
.. i18n:                 - xsl
.. i18n: 
.. i18n:                 - auto
.. i18n: 
.. i18n:                 - header
.. i18n: 
.. i18n:                 - attachment
.. i18n: 
.. i18n:                 - attachment_use
.. i18n: 
.. i18n:                 - groups
.. i18n: 
.. i18n: * **Child_tags**: None
.. i18n: 
.. i18n: * **Example**:
.. i18n:   ::
.. i18n: 
.. i18n:      -
.. i18n:        !report {string: Technical guide,
.. i18n:         auto: False, model: ir.module.module,
.. i18n:         id: ir_module_reference_print,
.. i18n:         rml: base/module/report/ir_module_reference.rml,
.. i18n:         name: ir.module.reference}
..

* **Compulsory attributes**:
                - string

                - model

                - name

* **Optional attributes**:

                - id

                - report

                - multi

                - menu

                - keyword

                - rml

                - sxw

                - xml

                - xsl

                - auto

                - header

                - attachment

                - attachment_use

                - groups

* **Child_tags**: None

* **Example**:
  ::

     -
       !report {string: Technical guide,
        auto: False, model: ir.module.module,
        id: ir_module_reference_print,
        rml: base/module/report/ir_module_reference.rml,
        name: ir.module.reference}

.. i18n: ir_set
.. i18n: """"""
.. i18n: * **Tag**: ir_set
..

ir_set
""""""
* **Tag**: ir_set

.. i18n: * **Compulsory attributes**: None
.. i18n: 
.. i18n: * **Optional attributes**: None
.. i18n: 
.. i18n: * **Child_tags**:
.. i18n:             - field
.. i18n: 
.. i18n: * **Example**:
.. i18n:   ::
.. i18n: 
.. i18n:    -
.. i18n:     !ir_set:
.. i18n:     args: "[]"
.. i18n:     name: account.seller.costs
.. i18n:     value: tax_seller
..

* **Compulsory attributes**: None

* **Optional attributes**: None

* **Child_tags**:
            - field

* **Example**:
  ::

   -
    !ir_set:
    args: "[]"
    name: account.seller.costs
    value: tax_seller

.. i18n: python
.. i18n: """"""
.. i18n: * **Tag**: Python
..

python
""""""
* **Tag**: Python

.. i18n: * **Compulsory attributes**:
.. i18n:             - model
.. i18n: 
.. i18n: * **Optional attributes**: None
.. i18n: 
.. i18n: * **Child_tags**: None
.. i18n: 
.. i18n: * **Example**:
.. i18n:   ::
.. i18n: 
.. i18n:    Python code
..

* **Compulsory attributes**:
            - model

* **Optional attributes**: None

* **Child_tags**: None

* **Example**:
  ::

   Python code

.. i18n: delete
.. i18n: """"""
.. i18n: * **Tag**: delete
..

delete
""""""
* **Tag**: delete

.. i18n: * **Compulsory attributes**:
.. i18n:             - model
.. i18n: 
.. i18n: * **Optional attributes**:
.. i18n:                 - id
.. i18n: 
.. i18n:                 - search
.. i18n: 
.. i18n: * **Child_tags**: None
.. i18n: 
.. i18n: * **Example**:
.. i18n:   ::
.. i18n: 
.. i18n:    -
.. i18n:      !delete {model: ir.actions, search: "[(model,like,auction.)]"}
..

* **Compulsory attributes**:
            - model

* **Optional attributes**:
                - id

                - search

* **Child_tags**: None

* **Example**:
  ::

   -
     !delete {model: ir.actions, search: "[(model,like,auction.)]"}

.. i18n: assert
.. i18n: """"""
.. i18n: * **Tag**: assert
..

assert
""""""
* **Tag**: assert

.. i18n: * **Compulsory attributes**:
.. i18n:             - model
.. i18n: 
.. i18n: * **Optional attributes**:
.. i18n:                 - id
.. i18n: 
.. i18n:                 - search
.. i18n: 
.. i18n:                 - string
.. i18n: 
.. i18n: * **Child_tags**:
.. i18n:         - test
.. i18n: 
.. i18n: * **Example**:
.. i18n:   ::
.. i18n: 
.. i18n:    -
.. i18n:      !assert {model: sale.order,
.. i18n:       id: test_order, string: order in progress}:
.. i18n:         - state == "progress"
..

* **Compulsory attributes**:
            - model

* **Optional attributes**:
                - id

                - search

                - string

* **Child_tags**:
        - test

* **Example**:
  ::

   -
     !assert {model: sale.order,
      id: test_order, string: order in progress}:
        - state == "progress"

.. i18n: test
.. i18n: """"
.. i18n: * **Tag**: test
..

test
""""
* **Tag**: test

.. i18n: * **Compulsory attributes**:
.. i18n:             - expr
.. i18n: 
.. i18n: * **Optional attributes**: None
.. i18n: 
.. i18n: * **Child_tags**:
.. i18n:         - text node
.. i18n: 
.. i18n: * **Example**::
.. i18n: 
.. i18n:     - picking_ids[0].state == "done"
..

* **Compulsory attributes**:
            - expr

* **Optional attributes**: None

* **Child_tags**:
        - text node

* **Example**::

    - picking_ids[0].state == "done"

.. i18n: url
.. i18n: """"
.. i18n: * **Tag**: url
..

url
""""
* **Tag**: url

.. i18n: * **Compulsory attributes**: -
.. i18n: 
.. i18n: * **Optional attributes**: -
.. i18n: 
.. i18n: * **Child_tags**: -
.. i18n: 
.. i18n: * **Example**: -
..

* **Compulsory attributes**: -

* **Optional attributes**: -

* **Child_tags**: -

* **Example**: -

.. i18n: Writing YAML Tests
.. i18n: ------------------
..

写一个 YAML 测试
------------------

.. i18n: .. note::
.. i18n: 
.. i18n:     Please see also section :ref:`yaml-testing-guidelines`
..

.. note::

    参考第三部分 :ref:`yaml-testing-guidelines` 自动化YAML测试指南

.. i18n: **Write manually**
.. i18n:     * Record CRUD
.. i18n:     * Workflow transition
.. i18n:     * Assertions (one expression like in XML)
.. i18n:     * Pure Python code
..

**手工写**
    * 记录的 CRUD
    * 工作流过渡
    * 段言 (像在 XML 中的语句)
    * 纯 Python 代码

.. i18n: **Use base_module_record(er)**
..

**使用 base_module_record(er)**

.. i18n:     * Generate YAML file with record and workflow
..

    * 生成带有 record 和 workflow 的 YAML 文件

.. i18n:     .. figure::  images/record_object.png
.. i18n:        :align: center
.. i18n: 
.. i18n:     * Update this YAML with assertions / Python code
..

    .. figure::  images/record_object.png
       :align: center

    * 用 assertions / Python 代码更新这个 YAML 

.. i18n: .. warning:: Important
.. i18n: 
.. i18n:    As yaml is structured with indentation(like Python), each child tag(sub-tag) must be indented as compared to its parent tag.
..

.. warning:: 重要

   yaml 的结构采用(像 Python)缩进, 每一个 child 标签(sub-tag) 相对于父标签进行缩进.

.. i18n: Field Tag
.. i18n: +++++++++
..

Field Tag
+++++++++

.. i18n: * text
.. i18n:     + text with special characters at beginning or at end must be enclosed with double quotes.
.. i18n:         **Ex: name: "[PC1] Basic PC"**
.. i18n: 
.. i18n: * integer and float
.. i18n:     **Ex: price_unit: 450**
.. i18n:     **Ex: amount_total: 3263.0**
.. i18n: 
.. i18n: * boolean
.. i18n:     **active: 1**
.. i18n: 
.. i18n: * datetime
.. i18n:     **date_start: str(time.localtime()[0] - 1) + -08-07**
.. i18n: 
.. i18n: * selection
.. i18n:     + give the shortcut
.. i18n:         **Ex: title: M.**
.. i18n: 
.. i18n: * many2one
.. i18n:     + if its a reference to res_id, specify the res_id
.. i18n:         **Ex: user_id: base.user_root**
..

* text
    + 用双引号在前面或后面包含输入的文字.
        **Ex: name: "[PC1] Basic PC"**

* integer and float
    **Ex: price_unit: 450**
    **Ex: amount_total: 3263.0**

* boolean
    **active: 1**

* datetime
    **date_start: str(time.localtime()[0] - 1) + -08-07**

* selection
    + 给出一个缩写
        **Ex: title: M.**

* many2one
    + 如果它是 res_id 的引用, 指向 res_id
        **Ex: user_id: base.user_root**

.. i18n:     + if its value is based on search criteria specify the model to search on and the criteria
.. i18n:         **Ex: object_id: !ref {model: ir.model, search: "[('model','=','crm.claim')]”}**
..

    + 如果它的值是基于搜索条目，那么指定 model 到搜索条目
        **Ex: object_id: !ref {model: ir.model, search: "[('model','=','crm.claim')]”}**

.. i18n: * one2many
.. i18n:     + start each record in one2many field on a new line with a space and a hyphen
.. i18n:         **Ex: order_line:**
.. i18n:         **name: New server config**
.. i18n:         **order_id: sale_order_so4**
.. i18n:         **......**
..

* one2many
    + start each record in one2many field on a new line with a space and a hyphen
        **Ex: order_line:**
        **name: New server config**
        **order_id: sale_order_so4**
        **......**

.. i18n:         **name: '[PC1] Basic PC'**
.. i18n:         **order_id: sale_order_so4**
.. i18n:         **......**
..

        **name: '[PC1] Basic PC'**
        **order_id: sale_order_so4**
        **......**

.. i18n: * many2many
.. i18n:     + start each record in many2many field with a space and a hyphen
.. i18n:         **Ex: type_ids:**
.. i18n:         **- project_tt_specification **
.. i18n:         **- project_tt_development**
.. i18n:         **- project_tt_testing**
..

* many2many
    + 用每一个 many2many 字段，以空格和连字符开始
        **Ex: type_ids:**
        **- project_tt_specification **
        **- project_tt_development**
        **- project_tt_testing**

.. i18n: Value tag
.. i18n: +++++++++
.. i18n: * if the value can be evaluated(like res_id is available), we write value tag as follows:
.. i18n:     **-**
.. i18n:     **!function {model: account.invoice, name: pay_and_reconcile}:**
.. i18n:     **- eval: "obj(ref('test_order_1')).amount_total"**
.. i18n:     **model: sale.order**
..

Value tag
+++++++++
* 如果Tag能被评估(like res_id is available), 像下面一样写 value tag :
    **-**
    **!function {model: account.invoice, name: pay_and_reconcile}:**
    **- eval: "obj(ref('test_order_1')).amount_total"**
    **model: sale.order**

.. i18n:     This will fetch the 'amount_total' value of a 'sale.order' record with res_id 'test_order_1'
..

    这会捕获一个 'sale.order' 记录的 'amount_total' 值伴随 res_id 'test_order_1'

.. i18n: * If the value is to be searched on some model based on a criteria, we write value tag as follows:
.. i18n:     **-**
.. i18n:     **!function {model: account.invoice, name: pay_and_reconcile}:**
.. i18n:     **- model: account.account**
.. i18n:     **search: "[('type', '=', 'cash')]"**
.. i18n:     This will fetch all those account.account records whose type is equal to 'cash'
..

* 如果值是在一些基于条目的模块上被搜索, 那么就像下面一样写 value tag :
    **-**
    **!function {model: account.invoice, name: pay_and_reconcile}:**
    **- model: account.account**
    **search: "[('type', '=', 'cash')]"**
    这将抓取所有 account.account 记录类型等于 'cash'

.. i18n: Test Tag
.. i18n: ++++++++
..

Test Tag
++++++++

.. i18n: * specify the test directly
.. i18n:     **Ex:  - picking_ids[0].state == "done"**
.. i18n:     **- state == "manual"**
..

* 直接指定测试
    **Ex:  - picking_ids[0].state == "done"**
    **- state == "manual"**

.. i18n: comment
.. i18n: +++++++
..

comment
+++++++

.. i18n: **#<!-- Resource: sale.order -->**
..

**#<!-- Resource: sale.order -->**

.. i18n: Asserts and Python code
.. i18n: +++++++++++++++++++++++
.. i18n: To create an invoice, python code could be written as:
..

Asserts and Python code
+++++++++++++++++++++++
为了创建一个发票，python 代码应该这样写:

.. i18n: **-**
.. i18n:   **!python {model: account.invoice}: |**
.. i18n:      **self.action_move_create(cr, uid, [ref("invoice1")])**
..

**-**
  **!python {model: account.invoice}: |**
     **self.action_move_create(cr, uid, [ref("invoice1")])**

.. i18n: The invoice must be in draft state:
..

发票必须在 draft 状态:

.. i18n: **-**
.. i18n:   **!assert {model: account.invoice , id: invoice1, string: "the invoice is now in Draft state"}:**
.. i18n:      **- state == "draft"**
..

**-**
  **!assert {model: account.invoice , id: invoice1, string: "the invoice is now in Draft state"}:**
     **- state == "draft"**

.. i18n: To test that all account are in a tree data structure, we write the below python code:
..

测试所有在树形数据结构的账户, 我们写下面的 python 代码:

.. i18n: **-**
.. i18n:   **!python {model: account.account}:**
.. i18n:     **ids = self.search(cr, uid, [])**
..

**-**
  **!python {model: account.account}:**
    **ids = self.search(cr, uid, [])**

.. i18n:     **accounts_list = self.read(cr, uid, ids['parent_id','parent_left','parent_right'])**
..

    **accounts_list = self.read(cr, uid, ids['parent_id','parent_left','parent_right'])**

.. i18n:     **accounts = dict((x['id'], x) for x in accounts_list)**
..

    **accounts = dict((x['id'], x) for x in accounts_list)**

.. i18n:     **log("Testing parent structure for %d accounts", len(accounts_list))**
..

    **log("Testing parent structure for %d accounts", len(accounts_list))**

.. i18n:     **for a in accounts_list:**
.. i18n:         **if a['parent_id']:**
.. i18n:             **assert a['parent_left']>accounts[a['parent_id'][0]]['parent_left']**
..

    **for a in accounts_list:**
        **if a['parent_id']:**
            **assert a['parent_left']>accounts[a['parent_id'][0]]['parent_left']**

.. i18n:             **assert a['parent_right']<accounts[a['parent_id'][0]]['parent_right']**
..

            **assert a['parent_right']<accounts[a['parent_id'][0]]['parent_right']**

.. i18n:         **assert a['parent_left']<a['parent_right']**
..

        **assert a['parent_left']<a['parent_right']**

.. i18n:     **for a2 in accounts_list:**
..

    **for a2 in accounts_list:**

.. i18n:         **assert not ((a2['parent_right']>a['parent_left'])and**
.. i18n:             **(a2['parent_left']<a['parent_left'])and**
..

        **assert not ((a2['parent_right']>a['parent_left'])and**
            **(a2['parent_left']<a['parent_left'])and**

.. i18n:             **(a2['parent_right']<a['parent_right']))**
..

            **(a2['parent_right']<a['parent_right']))**

.. i18n:             **if a2['parent_id']==a['id']:**
.. i18n:                 **assert(a2['parent_left']>a['parent_left'])and(a2['parent_right']<a['parent_right'])**
..

            **if a2['parent_id']==a['id']:**
                **assert(a2['parent_left']>a['parent_left'])and(a2['parent_right']<a['parent_right'])**

.. i18n: Running tests
.. i18n: +++++++++++++
.. i18n:     * Save the file with '.yml' extension
.. i18n:     * Add the yaml file under 'demo_xml' in terp file
.. i18n:     * Run the server with '--log-level=test' option
..

运行测试
+++++++++++++
    * 以扩展名 '.yml' 保存文件
    * 添加 yaml 文件到 'demo_xml' 下
    * 以参数 '--log-level=test' 运行服务器

.. i18n: .. _csv_serialization:
.. i18n: 
.. i18n: CSV Data Serialization
.. i18n: ----------------------
..

.. _csv_serialization:

CSV Data Serialization
----------------------

.. i18n: Since version 4.2, OpenERP provides a Comma-Separated-Values (CSV),
.. i18n: spreadsheet-compatible data serialization format.
..

Since version 4.2, OpenERP provides a Comma-Separated-Values (CSV),
spreadsheet-compatible data serialization format.

.. i18n: The basic format of an OpenERP CSV file is as follows::
.. i18n: 
.. i18n:     "id","name","model_id:id","group_id:id","perm_read","perm_write","perm_create","perm_unlink"
.. i18n:     "access_product_uom_categ_manager","product.uom.categ manager","model_product_uom_categ","product.group_product_manager",1,1,1,1
.. i18n:     "access_product_uom_manager","product.uom manager","model_product_uom","product.group_product_manager",1,1,1,1
.. i18n:     "access_product_ul_manager","product.ul manager","model_product_ul","product.group_product_manager",1,1,1,1
.. i18n:     "access_product_category_manager","product.category manager","model_product_category","product.group_product_manager",1,1,1,1
.. i18n:     "access_product_template_manager","product.template manager","model_product_template","product.group_product_manager",1,1,1,1
.. i18n:     "access_product_product_manager","product.product manager","model_product_product","product.group_product_manager",1,1,1,1
.. i18n:     "access_product_packaging_manager","product.packaging manager","model_product_packaging","product.group_product_manager",1,1,1,1
.. i18n:     "access_product_uom_categ_user","product.uom.categ.user","model_product_uom_categ","base.group_user",1,0,0,0
.. i18n:     "access_product_uom_user","product.uom.user","model_product_uom","base.group_user",1,0,0,0
.. i18n:     "access_product_ul_user","product.ul.user","model_product_ul","base.group_user",1,0,0,0
.. i18n:     "access_product_category_user","product.category.user","model_product_category","base.group_user",1,0,0,0
.. i18n:     "access_product_template_user","product.template.user","model_product_template","base.group_user",1,0,0,0
.. i18n:     "access_product_product_user","product.product.user","model_product_product","base.group_user",1,0,0,0
.. i18n:     "access_product_packaging_user","product.packaging.user","model_product_packaging","base.group_user",1,0,0,0
..

The basic format of an OpenERP CSV file is as follows::

    "id","name","model_id:id","group_id:id","perm_read","perm_write","perm_create","perm_unlink"
    "access_product_uom_categ_manager","product.uom.categ manager","model_product_uom_categ","product.group_product_manager",1,1,1,1
    "access_product_uom_manager","product.uom manager","model_product_uom","product.group_product_manager",1,1,1,1
    "access_product_ul_manager","product.ul manager","model_product_ul","product.group_product_manager",1,1,1,1
    "access_product_category_manager","product.category manager","model_product_category","product.group_product_manager",1,1,1,1
    "access_product_template_manager","product.template manager","model_product_template","product.group_product_manager",1,1,1,1
    "access_product_product_manager","product.product manager","model_product_product","product.group_product_manager",1,1,1,1
    "access_product_packaging_manager","product.packaging manager","model_product_packaging","product.group_product_manager",1,1,1,1
    "access_product_uom_categ_user","product.uom.categ.user","model_product_uom_categ","base.group_user",1,0,0,0
    "access_product_uom_user","product.uom.user","model_product_uom","base.group_user",1,0,0,0
    "access_product_ul_user","product.ul.user","model_product_ul","base.group_user",1,0,0,0
    "access_product_category_user","product.category.user","model_product_category","base.group_user",1,0,0,0
    "access_product_template_user","product.template.user","model_product_template","base.group_user",1,0,0,0
    "access_product_product_user","product.product.user","model_product_product","base.group_user",1,0,0,0
    "access_product_packaging_user","product.packaging.user","model_product_packaging","base.group_user",1,0,0,0

.. i18n: Importing from a CSV
.. i18n: ++++++++++++++++++++
..

Importing from a CSV
++++++++++++++++++++

.. i18n: Instead of using .XML file, you can import .CSV files. It is simpler but the migration system does not migrate the data imported from the .CSV files. It's like the noupdate attribute in .XML files.
.. i18n: It's also more difficult to keep track of relations between resources and it is slower at the installation of the server.
..

Instead of using .XML file, you can import .CSV files. It is simpler but the migration system does not migrate the data imported from the .CSV files. It's like the noupdate attribute in .XML files.
It's also more difficult to keep track of relations between resources and it is slower at the installation of the server.

.. i18n: Use this only for [demo] data that will never been upgraded from one version of OpenERP to another.
..

Use this only for [demo] data that will never been upgraded from one version of OpenERP to another.

.. i18n: The name of the object is the name of the CSV file before the first '-'.
.. i18n: You must use one file per object to import. For example, to import a file with partners (including their
.. i18n: multiple contacts and events), the file must be named like one of the following example:
..

The name of the object is the name of the CSV file before the first '-'.
You must use one file per object to import. For example, to import a file with partners (including their
multiple contacts and events), the file must be named like one of the following example:

.. i18n:     * res.partner.csv
.. i18n:     * res.partner-tiny_demo.csv
.. i18n:     * res.partner-tiny.demo.csv
..

    * res.partner.csv
    * res.partner-tiny_demo.csv
    * res.partner-tiny.demo.csv

.. i18n: Structure of the CSV file
.. i18n: +++++++++++++++++++++++++
..

Structure of the CSV file
+++++++++++++++++++++++++

.. i18n:     * Separator to use: ``,``
.. i18n:     * Quote character for strings: ``"`` (optional if no separator is found in field values)
.. i18n:     * Encoding to use: ``UTF-8``
.. i18n:     * No whitespace allowed around separators if not using quote characters
.. i18n:     * Be sure to configure your CSV export software (e.g. spreadsheet editor) with the above parameters
..

    * Separator to use: ``,``
    * Quote character for strings: ``"`` (optional if no separator is found in field values)
    * Encoding to use: ``UTF-8``
    * No whitespace allowed around separators if not using quote characters
    * Be sure to configure your CSV export software (e.g. spreadsheet editor) with the above parameters

.. i18n: Exporting demo data and import it from a module
.. i18n: +++++++++++++++++++++++++++++++++++++++++++++++
..

Exporting demo data and import it from a module
+++++++++++++++++++++++++++++++++++++++++++++++

.. i18n: You can import .CSV file that have been exported from the OpenERP client.
.. i18n: This is interesting to create your own demo module. But both formats are not exactly the same,
.. i18n: mainly due to the conversion: Structured Data -> Flat Data -> Structured Data.
..

You can import .CSV file that have been exported from the OpenERP client.
This is interesting to create your own demo module. But both formats are not exactly the same,
mainly due to the conversion: Structured Data -> Flat Data -> Structured Data.

.. i18n:     *  .. compound::
.. i18n: 
.. i18n:           The name of the column (first line of the .CSV file) use the end user term in his own language when
.. i18n:           you export from the client. If you want to import from a module, you must convert the first column
.. i18n:           using the fields names. 
.. i18n:           Example, from the partner form::
.. i18n: 
.. i18n:               Name,Code,Contacts/Contact Name,Contacts/Street,Contacts/Zip
.. i18n: 
.. i18n:           becomes::
.. i18n: 
.. i18n:               name,ref,address/name,address/street,address/zip
.. i18n: 
.. i18n:     * When you export from the OpenERP client, you can select any many2one fields and their child's relation.
.. i18n:       When you import from a module, OpenERP tries to recreate the relations between the two resources.
.. i18n:       For example, do not export something like this from a sale order form - otherwise OpenERP will not be
.. i18n:       able to import your file::
.. i18n: 
.. i18n:           Order Description,Partner/Name,Partner/Payable,Partner/Address/Name
.. i18n: 
.. i18n:     * To find the link for a many2one or many2many field, the server uses the name_search function when importing.
.. i18n:       So, for a many2one field, it is better to export the field 'name' or 'code' of the related resource only.
.. i18n:       Use the more unique one. Be sure that the field you export is searchable by the name_search function.
.. i18n:       (the 'name' column is always searchable)::
.. i18n: 
.. i18n:           Order Description,Partner/Code
.. i18n: 
.. i18n:     * Change the title of the column for all many2many or many2one fields. It's because you export the related
.. i18n:       resource and you import a link on the resource.
.. i18n:       Example from a sale order: Partner/Code should become partner_id and not partner_id/code.
.. i18n:       If you kept the ``/code``, OpenERP will try to create those entries in the database instead of finding
.. i18n:       references to existing ones.
.. i18n: 
.. i18n:     * .. compound::
.. i18n: 
.. i18n:           Many2many fields. If all the exported data contains 0 or 1 relation on each many2many fields, there will
.. i18n:           be no problem. Otherwise, the export will result in one line per many2many. The import function expects
.. i18n:           to get all many2many relations in one column, separated by a comma.
.. i18n: 
.. i18n:           So, you have to make the transformation. For example, if the categories "Customer" and "Supplier"
.. i18n:           already exists::
.. i18n: 
.. i18n:               name,category_id
.. i18n:               Smith, "Customer, Supplier"
.. i18n: 
.. i18n:           If you want to create these two categories you can try ::
.. i18n: 
.. i18n:               name,category_id/name
.. i18n:               Smith, "Customer, Supplier"
.. i18n: 
.. i18n:           But this does not work as expected: a category "Customer, Supplier" is created.
.. i18n:           The solution is to create an empty line with only the second category::
.. i18n: 
.. i18n:               name,category_id/name
.. i18n:               Smith, Customer
.. i18n:               ,Supplier
.. i18n: 
.. i18n:           Note the comma before "Supplier"!
.. i18n: 
.. i18n:     * Read only fields. Do not try to import read only fields like the amount receivable or payable for a partner.
.. i18n:       Otherwise, OpenERP will not accept to import your file.
.. i18n: 
.. i18n:     * Exporting trees. You can export and import tree structures using the parent field.
.. i18n:       You just have to take care of the import order. The parent have to be created before his child's.
..

    *  .. compound::

          The name of the column (first line of the .CSV file) use the end user term in his own language when
          you export from the client. If you want to import from a module, you must convert the first column
          using the fields names. 
          Example, from the partner form::

              Name,Code,Contacts/Contact Name,Contacts/Street,Contacts/Zip

          becomes::

              name,ref,address/name,address/street,address/zip

    * When you export from the OpenERP client, you can select any many2one fields and their child's relation.
      When you import from a module, OpenERP tries to recreate the relations between the two resources.
      For example, do not export something like this from a sale order form - otherwise OpenERP will not be
      able to import your file::

          Order Description,Partner/Name,Partner/Payable,Partner/Address/Name

    * To find the link for a many2one or many2many field, the server uses the name_search function when importing.
      So, for a many2one field, it is better to export the field 'name' or 'code' of the related resource only.
      Use the more unique one. Be sure that the field you export is searchable by the name_search function.
      (the 'name' column is always searchable)::

          Order Description,Partner/Code

    * Change the title of the column for all many2many or many2one fields. It's because you export the related
      resource and you import a link on the resource.
      Example from a sale order: Partner/Code should become partner_id and not partner_id/code.
      If you kept the ``/code``, OpenERP will try to create those entries in the database instead of finding
      references to existing ones.

    * .. compound::

          Many2many fields. If all the exported data contains 0 or 1 relation on each many2many fields, there will
          be no problem. Otherwise, the export will result in one line per many2many. The import function expects
          to get all many2many relations in one column, separated by a comma.

          So, you have to make the transformation. For example, if the categories "Customer" and "Supplier"
          already exists::

              name,category_id
              Smith, "Customer, Supplier"

          If you want to create these two categories you can try ::

              name,category_id/name
              Smith, "Customer, Supplier"

          But this does not work as expected: a category "Customer, Supplier" is created.
          The solution is to create an empty line with only the second category::

              name,category_id/name
              Smith, Customer
              ,Supplier

          Note the comma before "Supplier"!

    * Read only fields. Do not try to import read only fields like the amount receivable or payable for a partner.
      Otherwise, OpenERP will not accept to import your file.

    * Exporting trees. You can export and import tree structures using the parent field.
      You just have to take care of the import order. The parent have to be created before his child's.

.. i18n: Use record id like in xml file
.. i18n: ++++++++++++++++++++++++++++++
..

Use record id like in xml file
++++++++++++++++++++++++++++++

.. i18n: It's possible to define an id for each line of the csv file. This allow to define references between records:
..

It's possible to define an id for each line of the csv file. This allow to define references between records:

.. i18n:     id, name, parent_id:id
.. i18n:     record_one, Father,
.. i18n:     record_two, Child, record_one
..

    id, name, parent_id:id
    record_one, Father,
    record_two, Child, record_one

.. i18n: If you do this, the line with the parent data must be before the child lines in the file.
..

If you do this, the line with the parent data must be before the child lines in the file.

.. i18n: Multiple CSV Files
.. i18n: ------------------
..

Multiple CSV Files
------------------

.. i18n: Importing from multiple CSV a full group of linked data
.. i18n: +++++++++++++++++++++++++++++++++++++++++++++++++++++++
..

Importing from multiple CSV a full group of linked data
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. i18n: It's possible to import a lot of data, with multiple CSV files imported as a single operation. Assume we have a database with books and authors with a relation many2many between book and author.
..

It's possible to import a lot of data, with multiple CSV files imported as a single operation. Assume we have a database with books and authors with a relation many2many between book and author.

.. i18n: And that you already have a file with a lot of books (like a library) and an other file with a lot of authors and a third file with the links between them.
..

And that you already have a file with a lot of books (like a library) and an other file with a lot of authors and a third file with the links between them.

.. i18n: How to import that easily in openERP ?
..

How to import that easily in openERP ?

.. i18n: Definition of an import module
.. i18n: ++++++++++++++++++++++++++++++
..

Definition of an import module
++++++++++++++++++++++++++++++

.. i18n: You can do this in the module you have defined to manage yours books and authors. but Sometimes, the tables to import can also be in several modules.
..

You can do this in the module you have defined to manage yours books and authors. but Sometimes, the tables to import can also be in several modules.

.. i18n: For this example, let's say that 'book' object is defined in a module called 'library_management' and that 'Author' object in a module called 'contact_name'.
..

For this example, let's say that 'book' object is defined in a module called 'library_management' and that 'Author' object in a module called 'contact_name'.

.. i18n: In this case, you can create a 'fake' module, just to import the data for all these multiples modules. Call this importation module : 'import_my_books'.
..

In this case, you can create a 'fake' module, just to import the data for all these multiples modules. Call this importation module : 'import_my_books'.

.. i18n: You create this module as others modules of OpenObject :
..

You create this module as others modules of OpenObject :

.. i18n:    1. create a folder 'import_my_books'
.. i18n:    2. inside, create a '__init__.py' file with only one line : import import_my_books
.. i18n:    3. again, in the same folder, create a '__openerp__.py' file and in this file, write the following code :
..

   1. create a folder 'import_my_books'
   2. inside, create a '__init__.py' file with only one line : import import_my_books
   3. again, in the same folder, create a '__openerp__.py' file and in this file, write the following code :

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:      # -*- encoding: utf-8 -*-
.. i18n:      {
.. i18n:        'name': 'My Book Import',
.. i18n:        'category': 'Data Module 1',
.. i18n:        'init_xml':[],
.. i18n:        'author': 'mySelf & I',
.. i18n:        'depends': ['base','library_management','contact_name'],
.. i18n:        'version': '1.0',
.. i18n:        'active': False,
.. i18n:        'demo_xml': [],
.. i18n:        'update_xml':['contact_name.author.csv','library.book.csv'],
.. i18n:        'installable': True
.. i18n:      }
..

.. code-block:: python

     # -*- encoding: utf-8 -*-
     {
       'name': 'My Book Import',
       'category': 'Data Module 1',
       'init_xml':[],
       'author': 'mySelf & I',
       'depends': ['base','library_management','contact_name'],
       'version': '1.0',
       'active': False,
       'demo_xml': [],
       'update_xml':['contact_name.author.csv','library.book.csv'],
       'installable': True
     }

.. i18n: Creation of CSV files
.. i18n: +++++++++++++++++++++
..

Creation of CSV files
+++++++++++++++++++++

.. i18n: For the CSV files, you'll import one after the other.
..

For the CSV files, you'll import one after the other.

.. i18n: So you have to choose in which way you'll treat the many2many relation.
.. i18n: For our example, we've choose to import all the authors, then all the books with the links to the authors.
..

So you have to choose in which way you'll treat the many2many relation.
For our example, we've choose to import all the authors, then all the books with the links to the authors.

.. i18n:    1. authors CSV file
..

   1. authors CSV file

.. i18n: You have to put your data in a CSV file without any link to books (because the book ids will be known only AFTERWARDS...) For example : ("contact_name.author.csv")
..

You have to put your data in a CSV file without any link to books (because the book ids will be known only AFTERWARDS...) For example : ("contact_name.author.csv")

.. i18n: ::
.. i18n: 
.. i18n:      id,last_name,first_name,type
.. i18n:      author_1,Bradley,Marion Zimmer,Book writer
.. i18n:      author_2,"Szu T'su",,Chinese philosopher
.. i18n:      author_3,Zelazny,Roger,Book writer
.. i18n:      author_4,Arleston,Scotch,Screen Writer
.. i18n:      author_5,Magnin,Florence,Comics Drawer
.. i18n:      ...
.. i18n: 
.. i18n:    1. Books CSV file
..

::

     id,last_name,first_name,type
     author_1,Bradley,Marion Zimmer,Book writer
     author_2,"Szu T'su",,Chinese philosopher
     author_3,Zelazny,Roger,Book writer
     author_4,Arleston,Scotch,Screen Writer
     author_5,Magnin,Florence,Comics Drawer
     ...

   1. Books CSV file

.. i18n: Here, you can put the data about your books, but also, the links to the authors, using the same id as the column 'id' of the author CSV file. For example : ("library.book.csv" )
..

Here, you can put the data about your books, but also, the links to the authors, using the same id as the column 'id' of the author CSV file. For example : ("library.book.csv" )

.. i18n: ::
.. i18n: 
.. i18n:      id,title,isbn,pages,date,author_ids:id
.. i18n:      book_a,Les Cours du Chaos,1234567890123,268,1975-12-25,"author_3"
.. i18n:      book_b,"L'art de la Guerre, en 219 volumes",1234567890124,1978-01-01,"author_2"
.. i18n:      book_c,"new marvellous comics",1587459248579,2009-01-01,"author_5,author_4"
.. i18n:      ...
..

::

     id,title,isbn,pages,date,author_ids:id
     book_a,Les Cours du Chaos,1234567890123,268,1975-12-25,"author_3"
     book_b,"L'art de la Guerre, en 219 volumes",1234567890124,1978-01-01,"author_2"
     book_c,"new marvellous comics",1587459248579,2009-01-01,"author_5,author_4"
     ...

.. i18n: Five remarks :
..

Five remarks :

.. i18n:    1. the field content must be enclosed in double quotes (") if there is a double quote or a comma in the field.
.. i18n:    2. the dates are in the format YYYY-MM-DD
.. i18n:    3. if you have many ids in the same column, you must separate them with a comma, and, by the way, you must enclosed the content of the column between double quotes...
.. i18n:    4. the name of the field is the same as the name of the field in the class definition AND must be followed by ':id' if the content is an ID that must be interpreted by the import module. In fact, "author_4" will be transformed by the import module in an integer id for the database module and this numerical id will be put also in the table between author and book, not the literal ID (author_4).
.. i18n:    5. the encoding to be used by the CSV file is the 'UTF-8' encoding
..

   1. the field content must be enclosed in double quotes (") if there is a double quote or a comma in the field.
   2. the dates are in the format YYYY-MM-DD
   3. if you have many ids in the same column, you must separate them with a comma, and, by the way, you must enclosed the content of the column between double quotes...
   4. the name of the field is the same as the name of the field in the class definition AND must be followed by ':id' if the content is an ID that must be interpreted by the import module. In fact, "author_4" will be transformed by the import module in an integer id for the database module and this numerical id will be put also in the table between author and book, not the literal ID (author_4).
   5. the encoding to be used by the CSV file is the 'UTF-8' encoding

.. i18n: Data Migration - Import / Export
.. i18n: ================================
..

Data Migration - Import / Export
================================

.. i18n: Data Importation
.. i18n: ----------------
..

Data Importation
----------------

.. i18n: Introduction
.. i18n: ++++++++++++
..

Introduction
++++++++++++

.. i18n: There are different methods to import your data into OpenERP:
..

There are different methods to import your data into OpenERP:

.. i18n:  * Through the web-service interface
.. i18n:  * Using CSV files through the client interface
.. i18n:  * Building a module with .XML or .CSV files with the content
.. i18n:  * Directly into the SQL database, using an ETL
..

 * Through the web-service interface
 * Using CSV files through the client interface
 * Building a module with .XML or .CSV files with the content
 * Directly into the SQL database, using an ETL

.. i18n: Importing data through a module
.. i18n: +++++++++++++++++++++++++++++++
..

Importing data through a module
+++++++++++++++++++++++++++++++

.. i18n: The best way to import data in OpenERP is to build a module that
.. i18n: integrates all the data you want to import. So, when you want to
.. i18n: import all the data, you just have to install the module and OpenERP
.. i18n: manages the different creation operations. When you have lots of different
.. i18n: data to import, we sometimes create different modules.
..

The best way to import data in OpenERP is to build a module that
integrates all the data you want to import. So, when you want to
import all the data, you just have to install the module and OpenERP
manages the different creation operations. When you have lots of different
data to import, we sometimes create different modules.

.. i18n: So, let's create a new module where we will store all our data. To do
.. i18n: this, from the addons directory, create a new module called data_yourcompany.
..

So, let's create a new module where we will store all our data. To do
this, from the addons directory, create a new module called data_yourcompany.

.. i18n: * mkdir data_yourcompany
.. i18n: * cd data_yourcompany
.. i18n: * touch __init__.py
..

* mkdir data_yourcompany
* cd data_yourcompany
* touch __init__.py

.. i18n: You must also create a file called __openerp__.py in this new module.
.. i18n: Write the following content in this module file description.
..

You must also create a file called __openerp__.py in this new module.
Write the following content in this module file description.

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:   {
.. i18n:     'name': 'Module for Data Importation',
.. i18n:     'version': '1.0',
.. i18n:     'category': 'Generic Modules/Others',
.. i18n:     'description': "Sample module for data importation.",
.. i18n:     'author': 'Tiny',
.. i18n:     'website': 'http://www.openerp.com',
.. i18n:     'depends': ['base'],
.. i18n:     'init_xml': [
.. i18n:         'res.partner.csv',
.. i18n:         'res.partner.address.csv'
.. i18n:     ],
.. i18n:     'update_xml': [],
.. i18n:     'installable': True,
.. i18n:     'active': False,
.. i18n:   }
..

.. code-block:: python

  {
    'name': 'Module for Data Importation',
    'version': '1.0',
    'category': 'Generic Modules/Others',
    'description': "Sample module for data importation.",
    'author': 'Tiny',
    'website': 'http://www.openerp.com',
    'depends': ['base'],
    'init_xml': [
        'res.partner.csv',
        'res.partner.address.csv'
    ],
    'update_xml': [],
    'installable': True,
    'active': False,
  }

.. i18n: The following module will import two different files:
..

The following module will import two different files:

.. i18n: * res.partner.csv : a CSV file containing records of the res.partner object
.. i18n: * res.partner.address.csv : a CSV file containing records of the res.partner.address object
..

* res.partner.csv : a CSV file containing records of the res.partner object
* res.partner.address.csv : a CSV file containing records of the res.partner.address object

.. i18n: Once this module is created, you must load data from your old application to
.. i18n: .CSV file that will be loaded in OpenERP. OpenERP has a builtin system to
.. i18n: manage identifications columns of the original software.
..

Once this module is created, you must load data from your old application to
.CSV file that will be loaded in OpenERP. OpenERP has a builtin system to
manage identifications columns of the original software.

.. i18n: For this exercise, we will load data from another OpenERP database called old.
.. i18n: As this database is in SQL, it's quite easy to export the data using the command
.. i18n: line postgresql client: psql. As to get a result that looks like a .CSV file,
.. i18n: we will use the following arguments of psql:
..

For this exercise, we will load data from another OpenERP database called old.
As this database is in SQL, it's quite easy to export the data using the command
line postgresql client: psql. As to get a result that looks like a .CSV file,
we will use the following arguments of psql:

.. i18n: * -A : display records without space for the row separators
.. i18n: * -F , : set the separator character as ','
.. i18n: * --pset footer : don't write the latest line that looks like "(21 rows)"
..

* -A : display records without space for the row separators
* -F , : set the separator character as ','
* --pset footer : don't write the latest line that looks like "(21 rows)"

.. i18n: When you import a .CSV file in OpenERP, you can provide a 'id' column that
.. i18n: contains a uniq identification number or string for the record. We will use
.. i18n: this 'id' column to refer to the ID of the record in the original application.
.. i18n: As to refer to this record from a many2one field, you can use 'FIELD_NAME:id'.
.. i18n: OpenERP will re-create the relationship between the record using this uniq
.. i18n: ID.
..

When you import a .CSV file in OpenERP, you can provide a 'id' column that
contains a uniq identification number or string for the record. We will use
this 'id' column to refer to the ID of the record in the original application.
As to refer to this record from a many2one field, you can use 'FIELD_NAME:id'.
OpenERP will re-create the relationship between the record using this uniq
ID.

.. i18n: So let's start to export the partners from our database using psql: ::
.. i18n: ::
.. i18n: 
.. i18n: 	  psql trunk -c "select 'partner_'||id as id,name from res_partner" 
.. i18n: 	             -A -F , --pset footer > res.partner.csv
..

So let's start to export the partners from our database using psql: ::
::

	  psql trunk -c "select 'partner_'||id as id,name from res_partner" 
	             -A -F , --pset footer > res.partner.csv

.. i18n: This creates a res.partner.csv file containing a structure that looks like this:
..

This creates a res.partner.csv file containing a structure that looks like this:

.. i18n: ::
.. i18n: 
.. i18n: 	  id,name
.. i18n: 	  partner_2,ASUStek
.. i18n: 	  partner_3,Agrolait
.. i18n: 	  partner_4,Camptocamp
.. i18n: 	  partner_5,Syleam
..

::

	  id,name
	  partner_2,ASUStek
	  partner_3,Agrolait
	  partner_4,Camptocamp
	  partner_5,Syleam

.. i18n: By doing this, we generated data from the res.partner object, by creating a uniq
.. i18n: identification string for each record, which is related to the old application's
.. i18n: ID.
..

By doing this, we generated data from the res.partner object, by creating a uniq
identification string for each record, which is related to the old application's
ID.

.. i18n: Now, we will export the table with addresses (or contacts) that are linked to
.. i18n: partners through the relation field: partner_id. We will proceed in the same
.. i18n: way to export the data and put them into our module:
..

Now, we will export the table with addresses (or contacts) that are linked to
partners through the relation field: partner_id. We will proceed in the same
way to export the data and put them into our module:

.. i18n: ::
.. i18n: 
.. i18n:   psql trunk -c "select 'partner_address'||id as id,name,'partner_'||
.. i18n:                 partner_id as \"partner_id:id\" from res_partner_address" 
.. i18n:                 -A -F , --pset footer > res.partner.address.csv
..

::

  psql trunk -c "select 'partner_address'||id as id,name,'partner_'||
                partner_id as \"partner_id:id\" from res_partner_address" 
                -A -F , --pset footer > res.partner.address.csv

.. i18n: This should create a file called res.partner.address with the following data:
..

This should create a file called res.partner.address with the following data:

.. i18n: ::
.. i18n: 
.. i18n:   id,name,partner_id:id
.. i18n:   partner_address2,Benoit Mortier,partner_2
.. i18n:   partner_address3,Laurent Jacot,partner_3
.. i18n:   partner_address4,Laith Jubair,partner_4
.. i18n:   partner_address5,Fabien Pinckaers,partner_4
..

::

  id,name,partner_id:id
  partner_address2,Benoit Mortier,partner_2
  partner_address3,Laurent Jacot,partner_3
  partner_address4,Laith Jubair,partner_4
  partner_address5,Fabien Pinckaers,partner_4

.. i18n: When you will install this module, OpenERP will automatically import the partners
.. i18n: and then the address and recreate efficiently the link between the two records.
.. i18n: When installing a module, OpenERP will test and apply the constraints for consistency
.. i18n: of the data. So, when you install this module, it may crash, for example, because
.. i18n: you may have different partners with the same name in the system. (due to the uniq
.. i18n: constraint on the name of a partner). So, you have to clean your data before importing
.. i18n: them.
..

When you will install this module, OpenERP will automatically import the partners
and then the address and recreate efficiently the link between the two records.
When installing a module, OpenERP will test and apply the constraints for consistency
of the data. So, when you install this module, it may crash, for example, because
you may have different partners with the same name in the system. (due to the uniq
constraint on the name of a partner). So, you have to clean your data before importing
them.

.. i18n: If you plan to upload thousands of records through this technique, you should consider
.. i18n: using the argument '-P' when running the server.
..

If you plan to upload thousands of records through this technique, you should consider
using the argument '-P' when running the server.

.. i18n: ::
.. i18n: 
.. i18n:   openerp_server.py -P status.pickle --init=data_yourcompany
..

::

  openerp_server.py -P status.pickle --init=data_yourcompany

.. i18n: This method provides a faster importation of the data and, if it crashes in the middle
.. i18n: of the import, it will continue at the same line after rerunning the server. This may
.. i18n: preserves hours of testing when importing big files.
..

This method provides a faster importation of the data and, if it crashes in the middle
of the import, it will continue at the same line after rerunning the server. This may
preserves hours of testing when importing big files.

.. i18n: Using OpenERP's ETL
.. i18n: +++++++++++++++++++
..

Using OpenERP's ETL
+++++++++++++++++++

.. i18n: The next version of OpenERP will include an ETL module to allow you
.. i18n: to easily manages complex import jobs. If you are interested in this
.. i18n: system, you can check the complete specifications and the available
.. i18n: prototype at this location:
..

The next version of OpenERP will include an ETL module to allow you
to easily manages complex import jobs. If you are interested in this
system, you can check the complete specifications and the available
prototype at this location:

.. i18n:   bzr branch lp:~openerp-commiter/openobject-addons/trunk-extra-addons/etl
..

  bzr branch lp:~openerp-commiter/openobject-addons/trunk-extra-addons/etl

.. i18n: ... to be continued ...
..

... to be continued ...

.. i18n: Data Loading
.. i18n: ------------
..

Data Loading
------------

.. i18n: During OpenERP installation, two steps are necessary to create and feed the database:
..

During OpenERP installation, two steps are necessary to create and feed the database:

.. i18n:    1. Create the SQL tables
.. i18n:    2. Insert the different data into the tables 
..

   1. Create the SQL tables
   2. Insert the different data into the tables 

.. i18n: The creation (or modification in the case of an upgrade) of SQL tables is automated thanks to the description of objects in the server.
..

The creation (or modification in the case of an upgrade) of SQL tables is automated thanks to the description of objects in the server.

.. i18n: Into OpenERP, all the logic of the application is stored in the database. We find for example:
..

Into OpenERP, all the logic of the application is stored in the database. We find for example:

.. i18n:     * the definitions of the reports,
.. i18n:     * the object default values,
.. i18n:     * the form description of the interface client,
.. i18n:     * the relations between the menu and the client buttons, ... 
..

    * the definitions of the reports,
    * the object default values,
    * the form description of the interface client,
    * the relations between the menu and the client buttons, ... 

.. i18n: There must be a mechanism to describe, modify and reload the different data. These data are represented into a set of XML files that can possibly be loaded during start of the program in order to fill in the tables. 
..

There must be a mechanism to describe, modify and reload the different data. These data are represented into a set of XML files that can possibly be loaded during start of the program in order to fill in the tables. 

.. i18n: Upgrading
.. i18n: =========
..

Upgrading
=========

.. i18n: .. warning:: This section needs to be rewritten or improved. If you think you
.. i18n:              can contribute to this effort, and are already familiar with Launchpad 
.. i18n:              and OpenERP's source control system, Bazaar, please have a look at:
.. i18n: 
.. i18n:                  * the section explaining how you can download and build the
.. i18n:                    current documentation on your system: :ref:`building_documentation`
.. i18n:                  * an RST primer such as `this one <http://sphinx.pocoo.org/rest.html>`_ to learn 
.. i18n:                    how you can start modifying the documentation content
..

.. warning:: This section needs to be rewritten or improved. If you think you
             can contribute to this effort, and are already familiar with Launchpad 
             and OpenERP's source control system, Bazaar, please have a look at:

                 * the section explaining how you can download and build the
                   current documentation on your system: :ref:`building_documentation`
                 * an RST primer such as `this one <http://sphinx.pocoo.org/rest.html>`_ to learn 
                   how you can start modifying the documentation content

.. i18n: .. _technical_update_procedure:
.. i18n: 
.. i18n: Upgrading Server, Modules 
.. i18n: -------------------------
..

.. _technical_update_procedure:

Upgrading Server, Modules 
-------------------------

.. i18n: The upgrade from version to version is automatic and doesn't need any special
.. i18n: scripting on the user's part. In fact, the server is able to automatically
.. i18n: rebuild the database and the data from a previously installed version.
..

The upgrade from version to version is automatic and doesn't need any special
scripting on the user's part. In fact, the server is able to automatically
rebuild the database and the data from a previously installed version.

.. i18n: The tables are rebuilt from the current module definitions. To rebuild the
.. i18n: tables, the server uses the definition of the objects and adds / modifies
.. i18n: database fields as necessary.
..

The tables are rebuilt from the current module definitions. To rebuild the
tables, the server uses the definition of the objects and adds / modifies
database fields as necessary.

.. i18n: To invoke a database upgrade after installing a new version, you need to start
.. i18n: the server with the **--update=all** argument :
..

To invoke a database upgrade after installing a new version, you need to start
the server with the **--update=all** argument :

.. i18n: ::
.. i18n: 
.. i18n: 	openerp-server.py --update=all
..

::

	openerp-server.py --update=all

.. i18n: You can also only upgrade specific modules, for example:
..

You can also only upgrade specific modules, for example:

.. i18n: ::
.. i18n: 
.. i18n: 	openerp-server.py --update=account,base
..

::

	openerp-server.py --update=account,base

.. i18n: The database is rebuilt according to information provided in XML files and
.. i18n: Python Classes.
.. i18n: You can also execute the server with **--init=all**. The server will then
.. i18n: rebuild the database according to the existing XML files on the system, delete
.. i18n: all existing data and return OpenERP to its basic configuration.
..

The database is rebuilt according to information provided in XML files and
Python Classes.
You can also execute the server with **--init=all**. The server will then
rebuild the database according to the existing XML files on the system, delete
all existing data and return OpenERP to its basic configuration.

.. i18n: Detailed update operations
.. i18n: ++++++++++++++++++++++++++
..

Detailed update operations
++++++++++++++++++++++++++

.. i18n: OpenERP has a built-in migration and upgrade system which allows updates to be nearly (or often) automatic.
.. i18n: This system also allows to easily include custom modules.
..

OpenERP has a built-in migration and upgrade system which allows updates to be nearly (or often) automatic.
This system also allows to easily include custom modules.

.. i18n: Table/Object structure
.. i18n: """"""""""""""""""""""
..

Table/Object structure
""""""""""""""""""""""

.. i18n: When you run openerp-server with option ``--init`` or ``--update``, the table 
.. i18n: structure is updated to match the new description that is in Python code. Fields 
.. i18n: that are removed from Python code are not removed from the postgresql database 
.. i18n: to avoid losing data.
..

When you run openerp-server with option ``--init`` or ``--update``, the table 
structure is updated to match the new description that is in Python code. Fields 
that are removed from Python code are not removed from the postgresql database 
to avoid losing data.

.. i18n: So, simply running with ``--update`` or ``--init``, will upgrade your table structure.
..

So, simply running with ``--update`` or ``--init``, will upgrade your table structure.

.. i18n: It's important to run ``--init=module`` the first time you install the module. 
.. i18n: Next time, you must use the ``--update=module`` argument instead of the init 
.. i18n: one. This is because ``--init`` loads resources that are loaded only once and 
.. i18n: never upgraded (i.e., resources with no ``id=""`` attribute or within a 
.. i18n: ``<data noupdate="1">`` tag). Resources with the ``noupdate`` attribute will still
.. i18n: be created if they do not exist at upgrade time. This can be overridden by marking
.. i18n: a record with ``forcecreate="False"``.
..

It's important to run ``--init=module`` the first time you install the module. 
Next time, you must use the ``--update=module`` argument instead of the init 
one. This is because ``--init`` loads resources that are loaded only once and 
never upgraded (i.e., resources with no ``id=""`` attribute or within a 
``<data noupdate="1">`` tag). Resources with the ``noupdate`` attribute will still
be created if they do not exist at upgrade time. This can be overridden by marking
a record with ``forcecreate="False"``.

.. i18n: Data
.. i18n: """"
.. i18n: Some data is automatically loaded at the installation of OpenERP:
..

Data
""""
Some data is automatically loaded at the installation of OpenERP:

.. i18n:     * views, actions, menus,
.. i18n:     * workflows,
.. i18n:     * demo data
..

    * views, actions, menus,
    * workflows,
    * demo data

.. i18n: This data is also migrated to a new version if you run --update or --init.
..

This data is also migrated to a new version if you run --update or --init.

.. i18n: Workflows
.. i18n: """"""""""
..

Workflows
""""""""""

.. i18n: Workflows are also upgraded automatically. If some activities are removed, the documents states evolves automatically to the preceding activities. That ensure that all documents are always in valid states.
..

Workflows are also upgraded automatically. If some activities are removed, the documents states evolves automatically to the preceding activities. That ensure that all documents are always in valid states.

.. i18n: You can freely remove activities in your XML files. If workitems are in this activity, they will evolve to the preceding unlinked activity. And after the activity will be removed.
..

You can freely remove activities in your XML files. If workitems are in this activity, they will evolve to the preceding unlinked activity. And after the activity will be removed.

.. i18n: Things to care about during development
.. i18n: """""""""""""""""""""""""""""""""""""""
..

Things to care about during development
"""""""""""""""""""""""""""""""""""""""

.. i18n: Since version 3.0.2 of OpenERP, you can not use twice the same 'id="..."' during resource creation in your XML files, unless they are in two different modules.
..

Since version 3.0.2 of OpenERP, you can not use twice the same 'id="..."' during resource creation in your XML files, unless they are in two different modules.

.. i18n: Resources which don't contain an id are created (and updated) only once; at the installation of the module or when you use the --init argument.
..

Resources which don't contain an id are created (and updated) only once; at the installation of the module or when you use the --init argument.

.. i18n: If a resource has an id and this resource is not present anymore in the next version of the XML file, OpenERP will automatically remove it from the database. If this resource is still present, OpenERP will update the modifications to this resource.
..

If a resource has an id and this resource is not present anymore in the next version of the XML file, OpenERP will automatically remove it from the database. If this resource is still present, OpenERP will update the modifications to this resource.

.. i18n: If you use a new id, the resource will be automatically created at the next update of this module.
..

If you use a new id, the resource will be automatically created at the next update of this module.

.. i18n: **Use explicit id declaration !**, Example:
..

**Use explicit id declaration !**, Example:

.. i18n:     * view_invoice_form,
.. i18n:     * view_move_line_tree,
.. i18n:     * action_invoice_form_open, ...
..

    * view_invoice_form,
    * view_move_line_tree,
    * action_invoice_form_open, ...

.. i18n: It is important to put id="...." to all record that are important for the next version migrations. For example, do not forget to put some id="..." on all workflows transitions. This will allows OpenERP to know which transition has been removed and which transition is new or updated.
..

It is important to put id="...." to all record that are important for the next version migrations. For example, do not forget to put some id="..." on all workflows transitions. This will allows OpenERP to know which transition has been removed and which transition is new or updated.

.. i18n: Custom modules
.. i18n: """"""""""""""
..

Custom modules
""""""""""""""

.. i18n: For example, if you want to override the view of an object named 'invoice_form' in your xml file (id="invoice_form"). All you have to do is redefine this view in your custom module with the same id. You can prefix ids with the name of the module to reference an id defined in another module.
..

For example, if you want to override the view of an object named 'invoice_form' in your xml file (id="invoice_form"). All you have to do is redefine this view in your custom module with the same id. You can prefix ids with the name of the module to reference an id defined in another module.

.. i18n: Example:
..

Example:

.. i18n:     <record model="ir.ui.view" id="account.invoice_form">
.. i18n:     ...
.. i18n:     <record>
..

    <record model="ir.ui.view" id="account.invoice_form">
    ...
    <record>

.. i18n: This will override the invoice form view. You do not have to delete the old view, like in 3.0 versions of OpenERP.
..

This will override the invoice form view. You do not have to delete the old view, like in 3.0 versions of OpenERP.

.. i18n: Note that it is often better to use view inheritance instead of overwriting views.
..

Note that it is often better to use view inheritance instead of overwriting views.

.. i18n: In this migration system, you do not have to delete any resource. The migration system will detect if it is an update or a delete using id="..." attributes. This is important to preserve references during migrations.
..

In this migration system, you do not have to delete any resource. The migration system will detect if it is an update or a delete using id="..." attributes. This is important to preserve references during migrations.

.. i18n: Demo data
.. i18n: """""""""
..

Demo data
"""""""""

.. i18n: Demo data does not have to be upgraded; because it was probably modified or 
.. i18n: deleted by users. To avoid demo data being upgraded you can put a 
.. i18n: ``noupdate="1"`` attribute in the ``<data>`` tag of your .xml data files.
..

Demo data does not have to be upgraded; because it was probably modified or 
deleted by users. To avoid demo data being upgraded you can put a 
``noupdate="1"`` attribute in the ``<data>`` tag of your .xml data files.

.. i18n: Summary of update and init process
.. i18n: ++++++++++++++++++++++++++++++++++
..

Summary of update and init process
++++++++++++++++++++++++++++++++++

.. i18n: init:
..

init:

.. i18n:     modify/add/delete demo data and built-in data
..

    modify/add/delete demo data and built-in data

.. i18n: update:
..

update:

.. i18n:     modify/add/delete non demo data
..

    modify/add/delete non demo data

.. i18n: Examples of built-in (non demo) data:
..

Examples of built-in (non demo) data:

.. i18n:     * Menu structure,
.. i18n:     * View definition,
.. i18n:     * Workflow description, ...
.. i18n:     * Everything that has an `id` attribute in the XML data declaration (if no attr noupdate="1" in the header)
..

    * Menu structure,
    * View definition,
    * Workflow description, ...
    * Everything that has an `id` attribute in the XML data declaration (if no attr noupdate="1" in the header)

.. i18n: What's going on during the update process:
..

What's going on during the update process:

.. i18n:    1. If you manually added data within the client:
.. i18n:           * the update process will not change them
.. i18n:    2. If you dropped data:
.. i18n:           * if it was demo data, the update process will do nothing
.. i18n:           * if it was built-in data (like a view), the update process will recreate it
.. i18n:    3. If you modified data (either in the .XML or the client):
.. i18n:           * if it's demo data: nothing
.. i18n:           * if it's built-in data, data are updated
.. i18n:    4. If built-in data have been deleted in the .XML file:
.. i18n:           * this data will be deleted in the database.
..

   1. If you manually added data within the client:
          * the update process will not change them
   2. If you dropped data:
          * if it was demo data, the update process will do nothing
          * if it was built-in data (like a view), the update process will recreate it
   3. If you modified data (either in the .XML or the client):
          * if it's demo data: nothing
          * if it's built-in data, data are updated
   4. If built-in data have been deleted in the .XML file:
          * this data will be deleted in the database.
