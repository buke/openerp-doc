.. i18n: Objects, Fields and Methods
.. i18n: ===========================
..

Objects, Fields and Methods
===========================

.. i18n: OpenERP Objects
.. i18n: ---------------
..

OpenERP 对象
------------

.. i18n: .. This chapter is dedicated to detailed objects definition:
.. i18n:     all fields
.. i18n:     all objects
.. i18n:     inheritancies
..

.. This chapter is dedicated to detailed objects definition:
    all fields
    all objects
    inheritancies

.. i18n: All the ERP's pieces of data are accessible through "objects". As an example, there is a res.partner object to access the data concerning the partners, an account.invoice object for the data concerning the invoices, etc...
..

我们可以通过 `对象` 访问所有ERP的数据。举个例子，可以通过 `res.partner` 对象访问 `合作伙伴` 相关的数据，通过 `account.invoice` 对象访问 `发票` 相关的数据。

.. i18n: Please note that there is an object for every type of resource, and not an
.. i18n: object per resource. We have thus a res.partner object to manage all the
.. i18n: partners and not a *res.partner* object per partner. If we talk in "object
.. i18n: oriented" terms, we could also say that there is an object per level.
..

请注意的是，每种类型的资源是一个对象，而不是每个资源是一个对象。我们可以使用res.partner对象来管理所有的partners，而不是每个partner用一个res.partner对象来表示。当我们说“object oriented”术语时，其实说的是每级有个对象（an object per level）。

.. i18n: The direct consequences is that all the methods of objects have a common parameter: the "ids" parameter. This specifies on which resources (for example, on which partner) the method must be applied. Precisely, this parameter contains a list of resource ids on which the method must be applied.
..

直接的后果是，对象的所有方法都有一个共同的参数：参数“ids”。这个资源特别指定的方法必须被使用。准确的是，必须使用的这个方法的参数包括着资源ids的列表。

.. i18n: For example, if we have two partners with the identifiers 1 and 5, and we want to call the res_partner method "send_email", we will write something like::
.. i18n: 
.. i18n:         res_partner.send_email(... , [1, 5], ...)
..

例如，我们有两个标识为1和5的合作伙伴，当我们想要调用res_partner的方法“send_email”时，我们应该这样写：::

        res_partner.send_email(... , [1, 5], ...)

.. i18n: We will see the exact syntax of object method calls further in this document.
..

我们在这份文档中将会看到更多具体的对象方法调用的语法。

.. i18n: In the following section, we will see how to define a new object. Then, we will check out the different methods of doing this.
..

在下面的章节中，我们将会看到如何定义一个新对象。然后，我们会检验定义新对象所使用的不同方法。

.. i18n: For developers:
..

对于开发者来说：

.. i18n: * OpenERP "objects" are usually called classes in object oriented programming.
.. i18n: * A OpenERP "resource" is usually called an object in OO programming, instance of a class. 
..

* OpenERP “object”在面向对象编程中经常被成为类（class）。
* 一个OpenERP “resource”在面向对象编程中经常被称为一个对象，一个类的实例。

.. i18n: It's a bit confusing when you try to program inside OpenERP, because the language used is Python, and Python is a fully object oriented language, and has objects and instances ...
..

当你试图在OpenERP中编程时会有些困惑，因为使用的是Python语言，而Python语言是一种完全的面向对象语言。它有对象和实例…

.. i18n: Luckily, an OpenERP "resource" can be converted magically into a nice Python object using the "browse" class method (OpenERP object method).
..

我们感到幸运的是，OpenERP“resource”当使用“browse”类方法（OpenERP object method）时，可以神奇的转变成一个Python对象。

.. i18n: The ORM - Object-relational mapping - Models
.. i18n: --------------------------------------------
..

The ORM - Object-relational mapping - Models
--------------------------------------------

.. i18n: The ORM, short for Object-Relational Mapping, is a central part of OpenERP.
..

ORM是Object-Relational Mapping（对象关系映射）的简称，是OpenERP的中心部分。

.. i18n: In OpenERP, the data model is described and manipulated through Python classes
.. i18n: and objects. It is the ORM job to bridge the gap -- as transparently as
.. i18n: possible for the developer -- between Python and the underlying relational
.. i18n: database (PostgreSQL), which will provide the persistence we need for our
.. i18n: objects.
..

在OpenERP中，数据模型的描述和操纵都是通过Python的类和对象。ORM的作用是为python文件和底层的关系型数据库（PostgreSQL）消除隔阂（bridge the gap）（尽可能的透明的为开发人员），为对象提供持久性。

.. i18n: OpenERP Object Attributes
.. i18n: -------------------------
..

OpenERP Object Attributes
-------------------------

.. i18n: Objects Introduction
.. i18n: ++++++++++++++++++++
..

Objects Introduction
++++++++++++++++++++

.. i18n: To define a new object, you must define a new Python class then instantiate it. This class must inherit from the osv class in the osv module.
..

想要定义一个新对象，你就要先定义一个新的Python类，然后实例化它。这个类必须继承自osv模块的osv类。

.. i18n: Object definition
.. i18n: +++++++++++++++++
..

Object definition
+++++++++++++++++

.. i18n: The first line of the object definition will always be of the form::
.. i18n: 
.. i18n:         class name_of_the_object(osv.osv):
.. i18n:                 _name = 'name.of.the.object'
.. i18n:                 _columns = { ... }
.. i18n:                 ...
.. i18n:         name_of_the_object()
..

对象定义的前几行如下：::

        class name_of_the_object(osv.osv):
                _name = 'name.of.the.object'
                _columns = { ... }
                ...
        name_of_the_object()

.. i18n: An object is defined by declaring some fields with predefined names in the
.. i18n: class. Two of them are required (_name and _columns), the rest are optional.
.. i18n: The predefined fields are:
..

一个对象可以通过一些字段来定义，而这些字段在类中已经预定义了名称。其中有两个是必须的（_name和_columns），其他都是可选的。预定义的字段是：

.. i18n: Predefined fields
.. i18n: +++++++++++++++++
..

Predefined fields
+++++++++++++++++

.. i18n: `_auto`
.. i18n:   Determines whether a corresponding PostgreSQL table must be generated
.. i18n:   automatically from the object. Setting _auto to False can be useful in case
.. i18n:   of OpenERP objects generated from PostgreSQL views. See the "Reporting From
.. i18n:   PostgreSQL Views" section for more details.
..

`_auto`
  是否自动创建对象对应的Table，如果OpenERP的对象从PostgreSQL views中产生时，将_auto设为False比较好。想要知道更多的细节可以查看“Reporting From PostgreSQL Views”。

.. i18n: `_columns (required)`
.. i18n:   The object fields. See the :ref:`fields <fields-link>` section for further details.
..

`_columns (required)`
  对象字段，可在field章节了解更多。

.. i18n: `_constraints`
.. i18n:   The constraints on the object. See the constraints section for details.
..

`_constraints`
  定义对象上的约束，可在“constraints”章节了解更多。

.. i18n: `_sql_constraints`
.. i18n:   The SQL Constraint on the object. See the SQL constraints section for further details.
..

`_sql_constraints`
   定义对象中SQL约束，可在“SQL constraints”章节了解更多。

.. i18n: `_defaults`
.. i18n:   The default values for some of the object's fields. See the default value section for details.
..

`_defaults`
  定义一些字段的缺省值，可在“default value”章节了解更多。

.. i18n: `_inherit`
.. i18n:   The name of the osv object which the current object inherits from. See the :ref:`object inheritance section<inherit-link>`
.. i18n:   (first form) for further details.
..

`_inherit`
  当前对象继承自哪里，可在 :ref:`object inheritance section<inherit-link>`
  (first form) 了解更多。

.. i18n: `_inherits`
.. i18n:   The list of osv objects the object inherits from. This list must be given in
.. i18n:   a python dictionary of the form: {'name_of_the_parent_object':
.. i18n:   'name_of_the_field', ...}. See the :ref:`object inheritance section<inherits-link>` 
.. i18n:   (second form) for further details. Default value: {}.
..

`_inherits`
  
  当前对象继承的对象列表，这个列表必须是下面的形式：{‘name_of_the_parent_object’: ‘name_of_the_field’, ...}。可在“object inheritance section”了解更多。缺省值是：{}

.. i18n: `_log_access`
.. i18n:   Determines whether or not the write access to the resource must be logged.
.. i18n:   If true, four fields will be created in the SQL table: create_uid,
.. i18n:   create_date, write_uid, write_date. Those fields represent respectively the
.. i18n:   id of the user who created the record, the creation date of record, the id
.. i18n:   of the user who last modified the record, and the date of that last
.. i18n:   modification. This data may be obtained by using the perm_read method.
..

`_log_access`
  定义对资源的写访问是否应写入日志，如果是true，那将自动在对应的数据表中增加create_uid, create_date, write_uid, write_date四个字段，缺省值为True，即字段增加。这四个字段分布记录record的创建人，创建日期，修改人，修改日期。这四个字段值可以用对象的方法（perm_read）读取。

.. i18n: `_name (required)`
.. i18n:   Name of the object. Default value: None.
..

`_name (required)`
  定义对象的名称，缺省值为None。

.. i18n: `_order`
.. i18n:   Name of the fields used to sort the results of the search and read methods.
..

`_order`
  定义search和read方法的结果记录排序规则。

.. i18n:   Default value: 'id'.
..

  缺省值：“id”

.. i18n:   Examples::
.. i18n: 
.. i18n:     _order = "name"  
.. i18n:     _order = "date_order desc"
..

  例如::

    _order = "name"  
    _order = "date_order desc"

.. i18n: `_rec_name`
.. i18n:   Name of the field in which the name of every resource is stored. Default
.. i18n:   value: 'name'. Note: by default, the name_get method simply returns the
.. i18n:   content of this field.
..

`_rec_name`
  标识每个已被存储的资源的名称字段。缺省值是：“name”，缺省情况（name_get没被重载的话）方法name_get()返回本字段值。

.. i18n: `_sequence`
.. i18n:   Name of the SQL sequence that manages the ids for this object. Default value: None.
..

`_sequence`
  数据库表的id字段的序列采集器，缺省值为: None。

.. i18n: `_sql`
.. i18n:  SQL code executed upon creation of the object (only if _auto is True). It means this code gets executed after the table is created.
..

`_sql`
 SQL代码执行在对象的创建之上，意思就是说在表格创建后代码执行。

.. i18n: `_table`
.. i18n:   Name of the SQL table. Default value: the value of the _name field above
.. i18n:   with the dots ( . ) replaced by underscores ( _ ). 
..

`_table`
   数据库表名，缺省值是和_name一样，只是将"."替换成"_"。

.. i18n: .. _inherit-link:
.. i18n: 
.. i18n: Object Inheritance - _inherit
.. i18n: -----------------------------
..

.. _inherit-link:

Object Inheritance - _inherit
-----------------------------

.. i18n: Introduction
.. i18n: ++++++++++++
..

Introduction
++++++++++++

.. i18n: Objects may be inherited in some custom or specific modules. It is better to
.. i18n: inherit an object to add/modify some fields.
..

对象可能继承于很多定制的或是特定的模块。这比继承一个对象增加或修改某方面更好。

.. i18n: It is done with::
.. i18n: 
.. i18n:     _inherit='object.name'
..

It is done with::

    _inherit='object.name'

.. i18n: Extension of an object
.. i18n: ++++++++++++++++++++++
..

Extension of an object
++++++++++++++++++++++

.. i18n: There are two possible ways to do this kind of inheritance. Both ways result in
.. i18n: a new class of data, which holds parent fields and behaviour as well as
.. i18n: additional fields and behaviour, but they differ in heavy programatical
.. i18n: consequences.
..

这里继承有两种方式：他们都产生一个新的数据类，它将父类的字段和行为做为自己额外的字段和行为，但是他们在heavy programatical consequences上不同。

.. i18n: While Example 1 creates a new subclass "custom_material" that may be "seen" or
.. i18n: "used" by any view or tree which handles "network.material", this will not be
.. i18n: the case for Example 2.
..

例子1中产生一个新的子类叫“custom_material”，当操作network.material的视图或是列表时可以看到或是使用它。这和例子2不同。

.. i18n: This is due to the table (other.material) the new subclass is operating on,
.. i18n: which will never be recognized by previous "network.material" views or trees.
..

这是由于这个新类操作的表格（other.material）是不能被之前的对象“network.material”的视图或列表所识别的。

.. i18n: Example 1::
.. i18n: 
.. i18n:     class custom_material(osv.osv):
.. i18n:         _name = 'network.material'
.. i18n:         _inherit = 'network.material'
.. i18n:         _columns = {
.. i18n:             'manuf_warranty': fields.boolean('Manufacturer warranty?'),
.. i18n:         }
.. i18n:         _defaults = {
.. i18n:             'manuf_warranty': lambda *a: False,
.. i18n:         }
.. i18n:         custom_material()
..

例子1::

    class custom_material(osv.osv):
        _name = 'network.material'
        _inherit = 'network.material'
        _columns = {
            'manuf_warranty': fields.boolean('Manufacturer warranty?'),
        }
        _defaults = {
            'manuf_warranty': lambda *a: False,
        }
        custom_material()

.. i18n: .. tip:: Notice
.. i18n: 
.. i18n:     _name == _inherit
..

.. tip:: Notice

    _name == _inherit

.. i18n: In this example, the 'custom_material' will add a new field 'manuf_warranty' to
.. i18n: the object 'network.material'. New instances of this class will be visible by
.. i18n: views or trees operating on the superclasses table 'network.material'.
..

这个例子，“custom_material”增加了一个新的字段“manuf_warranty”到对象“network.material”中。这个类的新的实例对运行在父类“network.material”上的视图或列表是可见的。

.. i18n: This inheritancy is usually called "class inheritance" in Object oriented
.. i18n: design. The child inherits data (fields) and behavior (functions) of his
.. i18n: parent.
..

在面向对象的设计中，这种继承通常称为“类继承（class inheritance）”。子类继承父类的字段和函数。

.. i18n: Example 2::
.. i18n: 
.. i18n:     class other_material(osv.osv):
.. i18n:         _name = 'other.material'
.. i18n:         _inherit = 'network.material'
.. i18n:         _columns = {
.. i18n:             'manuf_warranty': fields.boolean('Manufacturer warranty?'),
.. i18n:         }
.. i18n:         _defaults = {
.. i18n:             'manuf_warranty': lambda *a: False,
.. i18n:         }
.. i18n:         other_material()
..

例子2::

    class other_material(osv.osv):
        _name = 'other.material'
        _inherit = 'network.material'
        _columns = {
            'manuf_warranty': fields.boolean('Manufacturer warranty?'),
        }
        _defaults = {
            'manuf_warranty': lambda *a: False,
        }
        other_material()

.. i18n: .. tip:: Notice
.. i18n: 
.. i18n:     _name != _inherit
..

.. tip:: Notice

    _name != _inherit

.. i18n: In this example, the 'other_material' will hold all fields specified by
.. i18n: 'network.material' and it will additionally hold a new field 'manuf_warranty'.
.. i18n: All those fields will be part of the table 'other.material'. New instances of
.. i18n: this class will therefore never been seen by views or trees operating on the
.. i18n: superclasses table 'network.material'.
..

在这个例子中，“other_material”会继承“network.material”的所有字段，它另外会加入一个新的字段“manuf_warranty”。所有这些字段都在表格“other.material”中。这个类的新的实例对运行在父类“network.material”上的视图或列表是不可见的。

.. i18n: This type of inheritancy is known as "inheritance by prototyping" (e.g.
.. i18n: Javascript), because the newly created subclass "copies" all fields from the
.. i18n: specified superclass (prototype). The child inherits data (fields) and behavior
.. i18n: (functions) of his parent.
..

这种类型的继承被称为“原型继承（inheritance by prototyping）”。因为新创建的子类拷贝了父类的所有字段。子类继承父类的字段和方法。

.. i18n: .. _inherits-link:
.. i18n: 
.. i18n: Inheritance by Delegation - _inherits
.. i18n: -------------------------------------
..

.. _inherits-link:

Inheritance by Delegation - _inherits
-------------------------------------

.. i18n:  **Syntax :**::
.. i18n: 
.. i18n:     class tiny_object(osv.osv)
.. i18n:         _name = 'tiny.object'
.. i18n:         _table = 'tiny_object'
.. i18n:         _inherits = {
.. i18n:             'tiny.object_a': 'object_a_id',
.. i18n:             'tiny.object_b': 'object_b_id',
.. i18n:             ... ,
.. i18n:             'tiny.object_n': 'object_n_id'
.. i18n:         }
.. i18n:         (...)
..

 **Syntax :**::

    class tiny_object(osv.osv)
        _name = 'tiny.object'
        _table = 'tiny_object'
        _inherits = {
            'tiny.object_a': 'object_a_id',
            'tiny.object_b': 'object_b_id',
            ... ,
            'tiny.object_n': 'object_n_id'
        }
        (...)

.. i18n: The object 'tiny.object' inherits from all the columns and all the methods from
.. i18n: the n objects 'tiny.object_a', ..., 'tiny.object_n'.
..

对象“tiny.object”继承n个对象“tiny.object_a, ...,tiny.object_n”的所有的字段和方法。

.. i18n: To inherit from multiple tables, the technique consists in adding one column to
.. i18n: the table tiny_object per inherited object. This column will store a foreign
.. i18n: key (an id from another table). The values *'object_a_id' 'object_b_id' ...
.. i18n: 'object_n_id'* are of type string and determine the title of the columns in
.. i18n: which the foreign keys from 'tiny.object_a', ..., 'tiny.object_n' are stored.
..

为了继承多种表格，每继承一个对象就加一列到表格中。这个列存储继承表格的外键。值‘object_a_id’ ‘object_b_id’ ... ‘object_n_id’ 是字符串类型，定义列头，它里面放着存储对象‘tiny.object_a’, ..., ‘tiny.object_n’的外键。

.. i18n: This inheritance mechanism is usually called " *instance inheritance* "  or  "
.. i18n: *value inheritance* ". A resource (instance) has the VALUES of its parents.
..

这种继承称为“对象继承（instance inheritance）”或是“值继承（value inheritance）”。对象有它父类的值（values）。

.. i18n: .. _fields-link:
.. i18n: 
.. i18n: Fields Introduction
.. i18n: -------------------
..

.. _fields-link:

字段(Fields) 简介
-----------------

.. i18n: Objects may contain different types of fields. Those types can be divided into
.. i18n: three categories: simple types, relation types and functional fields. The
.. i18n: simple types are integers, floats, booleans, strings, etc ... ; the relation
.. i18n: types are used to represent relations between objects (one2one, one2many,
.. i18n: many2one). Functional fields are special fields because they are not stored in
.. i18n: the database but calculated in real time given other fields of the view.
..

对象包括不同类型的字段，分为三类：simple types，relation types，functional fields。simple types是integers, floats, booleans, strings, etc ...；relation types是表示对象间的关系（one2one, one2many, many2one）。Functional fields是特殊的字段，因为它们不是存储在数据库中，而是实时计算视图给定的其他字段。

.. i18n: Here's the header of the initialization method of the class any field defined
.. i18n: in OpenERP inherits (as you can see in server/bin/osv/fields.py)::
.. i18n: 
.. i18n:     def __init__(self, string='unknown', required=False, readonly=False,
.. i18n:                  domain=None, context="", states=None, priority=0, change_default=False, size=None,
.. i18n:                  ondelete="set null", translate=False, select=False, **args) :
..

这是OpenERP继承类方法初始化的头文件。（Here’s the header of the initialization method of the class any field defined in OpenERP inherits）。::

    def __init__(self, string='unknown', required=False, readonly=False,
                 domain=None, context="", states=None, priority=0, change_default=False, size=None,
                 ondelete="set null", translate=False, select=False, **args) :

.. i18n: There are a common set of optional parameters that are available to most field
.. i18n: types:
..

这里有一套通用的可选参数，它对大多数的字段类型是可用的：

.. i18n: :change_default: 
.. i18n: 	Whether or not the user can define default values on other fields depending 
.. i18n: 	on the value of this field. Those default values need to be defined in
.. i18n: 	the ir.values table.
.. i18n: :help: 
.. i18n: 	A description of how the field should be used: longer and more descriptive
.. i18n: 	than `string`. It will appear in a tooltip when the mouse hovers over the 
.. i18n: 	field.
.. i18n: :ondelete: 
.. i18n: 	How to handle deletions in a related record. Allowable values are: 
.. i18n: 	'restrict', 'no action', 'cascade', 'set null', and 'set default'.
.. i18n: :priority: Not used?
.. i18n: :readonly: `True` if the user cannot edit this field, otherwise `False`.
.. i18n: :required:
.. i18n: 	`True` if this field must have a value before the object can be saved, 
.. i18n: 	otherwise `False`.
.. i18n: :size: The size of the field in the database: number characters or digits.
.. i18n: :states:
.. i18n: 	Lets you override other parameters for specific states of this object. 
.. i18n: 	Accepts a dictionary with the state names as keys and a list of name/value 
.. i18n: 	tuples as the values. For example: `states={'posted':[('readonly',True)]}`
.. i18n: :string: 
.. i18n: 	The field name as it should appear in a label or column header. Strings
.. i18n: 	containing non-ASCII characters must use python unicode objects. 
.. i18n: 	For example: `'tested': fields.boolean(u'Testé')` 
.. i18n: :translate:
.. i18n: 	`True` if the *content* of this field should be translated, otherwise 
.. i18n: 	`False`.
..

change_default：别的字段的缺省值是否可依赖于本字段。这些缺省值定义在ir.values表格中。
help：用于描述这个字段如何使用：更长的描述文字。当鼠标滑过该字段时将会显示在一个提示框中。
ondelete：如何处理相关记录的删除。允许的值有：‘restrict’, ‘no action’, ‘cascade’, ‘set null’, and ‘set default’。
priority：Not used？
readonly：当值为True时，该字段只读不可修改，缺省值：False
required：当值为True时，在对象存储前，该字段必须有个值，缺省值：False
size：数据库中该字段的size：number characters or digits.
states：让我们为这个对象特定的states重写其他参数，Accepts a dictionary with the state names as keys and a list of name/value tuples as the values. For example: states={‘posted’:[(‘readonly’,True)]} 
string：The field name as it should appear in a label or column header. Strings containing non-ASCII characters must use python unicode objects. For example: ‘tested’: fields.boolean(u’Testé’)
translate：值为True的话应该翻译这个字段的content，为False的话就不翻。

.. i18n: There are also some optional parameters that are specific to some field types:
..

对于一些字段类型，下面也是可选的参数：

.. i18n: :context: 
.. i18n: 	Define a variable's value visible in the view's context or an on-change 
.. i18n: 	function. Used when searching child table of `one2many` relationship?
.. i18n: :domain: 
.. i18n:     Domain restriction on a relational field.
..

context: Define a variable’s value visible in the view’s context or an on-change function. Used when searching child table of one2many relationship?
domain: 相关字段的Domain restriction

.. i18n:     Default value: []. 
..

    缺省值: []. 

.. i18n:     Example: domain=[('field','=',value)])
.. i18n: :invisible: Hide the field's value in forms. For example, a password.
.. i18n: :on_change:
.. i18n: 	Default value for the `on_change` attribute in the view. This will launch
.. i18n: 	a function on the server when the field changes in the client. For example,
.. i18n: 	`on_change="onchange_shop_id(shop_id)"`. 
.. i18n: :relation:
.. i18n: 	Used when a field is an id reference to another table. This is the name of
.. i18n: 	the table to look in. Most commonly used with related and function field
.. i18n: 	types.
.. i18n: :select: 
.. i18n: 	Default value for the `select` attribute in the view. 1 means basic search,
.. i18n: 	and 2 means advanced search.
..

示例: domain=[('field','=',value)])
:invisible: 在表单中隐藏该字段的值，例如输入密码区
:on_change: Default value for the on_change attribute in the view. This will launch a function on the server when the field changes in the client. For example, on_change=”onchange_shop_id(shop_id)”.
:relation: 当某个字段是另张表的id reference时就使用它。This is the name of the table to look in. Most commonly used with related and function field types.
:select: 视图中select 属性的默认值，1指basic search，2指advanced search.

.. i18n: Type of Fields
.. i18n: --------------
..

字段类型
--------

.. i18n: Basic Types
.. i18n: +++++++++++
..

基础类型
++++++++

.. i18n: :boolean:
..

:boolean:

.. i18n: 	A boolean (true, false).
..

	布尔型(boolean) (true, false).

.. i18n: 	Syntax::
.. i18n: 
.. i18n:                 fields.boolean('Field Name' [, Optional Parameters]),
..

	语法::

                fields.boolean('字段名称' [, 可选参数]),

.. i18n: :integer:
..

:integer:

.. i18n: 	An integer.
..

	整型(integer).

.. i18n: 	Syntax::
.. i18n: 
.. i18n:                 fields.integer('Field Name' [, Optional Parameters]),
..

	语法::

                fields.integer('字段名称' [, 可选参数]),

.. i18n: :float:
..

:float:

.. i18n:     A floating point number.
..

    浮点型(float).

.. i18n:     Syntax::
.. i18n: 
.. i18n:                 fields.float('Field Name' [, Optional Parameters]),
.. i18n: 
.. i18n:     .. note::
.. i18n: 
.. i18n:             The optional parameter digits defines the precision and scale of the
.. i18n:             number. The scale being the number of digits after the decimal point
.. i18n:             whereas the precision is the total number of significant digits in the
.. i18n:             number (before and after the decimal point). If the parameter digits is
.. i18n:             not present, the number will be a double precision floating point number.
.. i18n:             Warning: these floating-point numbers are inexact (not any value can be
.. i18n:             converted to its binary representation) and this can lead to rounding
.. i18n:             errors. You should always use the digits parameter for monetary amounts.
.. i18n: 
.. i18n:     Example::
.. i18n: 
.. i18n:         'rate': fields.float(
.. i18n:             'Relative Change rate',
.. i18n:             digits=(12,6) [,
.. i18n:             Optional Parameters]),
..

    语法::

                fields.float('字段名称' [, 可选参数]),

    .. note::

            digits定义整数部分和小数部分的位数。 The scale being the number of digits after the decimal point
            whereas the precision is the total number of significant digits in the
            number (before and after the decimal point). If the parameter digits is
            not present, the number will be a double precision floating point number.
            Warning: these floating-point numbers are inexact (not any value can be
            converted to its binary representation) and this can lead to rounding
            errors. You should always use the digits parameter for monetary amounts.

    例子::

        'rate': fields.float(
            'Relative Change rate',
            digits=(12,6) [,
            Optional Parameters]),

.. i18n: :char:
..

:char:

.. i18n:   A string of limited length. The required size parameter determines its size.
..

  字符串(char):
  限定长度的字符串，size属性定义字符串长度。

.. i18n:   Syntax::
.. i18n: 
.. i18n:   	fields.char(
.. i18n:   		'Field Name', 
.. i18n:   		size=n [, 
.. i18n:   		Optional Parameters]), # where ''n'' is an integer.
.. i18n: 
.. i18n:   Example::
.. i18n: 
.. i18n:         'city' : fields.char('City Name', size=30, required=True),
..

  语法::

  	fields.char(
  		'字段名称', 
  		size=n [, 
  		可选参数]), # 参数 ''n'' 指明了字符串字段的长度.

  Example::

        'city' : fields.char('City Name', size=30, required=True),

.. i18n: :text:
..

:text:

.. i18n:   A text field with no limit in length.
..

  没有长度限制的text field

.. i18n:   Syntax::
.. i18n: 
.. i18n:                 fields.text('Field Name' [, Optional Parameters]),
..

  Syntax::

                fields.text('Field Name' [, Optional Parameters]),

.. i18n: :date:
..

:date:

.. i18n:   A date.
..

  A date.

.. i18n:   Syntax::
.. i18n: 
.. i18n:                 fields.date('Field Name' [, Optional Parameters]),
..

  Syntax::

                fields.date('Field Name' [, Optional Parameters]),

.. i18n: :datetime:
..

:datetime:

.. i18n:   Allows to store a date and the time of day in the same field.
..

  Allows to store a date and the time of day in the same field.

.. i18n:   Syntax::
.. i18n: 
.. i18n:                 fields.datetime('Field Name' [, Optional Parameters]),
..

  Syntax::

                fields.datetime('Field Name' [, Optional Parameters]),

.. i18n: :binary:
..

:binary:

.. i18n:   A binary chain
..

  A binary chain

.. i18n: :selection:
..

:selection:

.. i18n:   A field which allows the user to make a selection between various predefined values.
..

  这个字段让用户对之前定义的值进行选择

.. i18n:   Syntax::
.. i18n: 
.. i18n:                 fields.selection((('n','Unconfirmed'), ('c','Confirmed')),
.. i18n:                                    'Field Name' [, Optional Parameters]),
.. i18n: 
.. i18n:   .. note::
.. i18n: 
.. i18n:              Format of the selection parameter: tuple of tuples of strings of the form::
.. i18n: 
.. i18n:                 (('key_or_value', 'string_to_display'), ... )
.. i18n:                 
.. i18n:   .. note::
.. i18n:              You can specify a function that will return the tuple. Example ::
.. i18n:              
.. i18n:                  def _get_selection(self, cursor, user_id, context=None):
.. i18n:                      return (
.. i18n:                      	('choice1', 'This is the choice 1'), 
.. i18n:                      	('choice2', 'This is the choice 2'))
.. i18n:                      
.. i18n:                  _columns = {
.. i18n:                     'sel' : fields.selection(
.. i18n:                     	_get_selection, 
.. i18n:                     	'What do you want ?')
.. i18n:                  }
.. i18n: 
.. i18n:   *Example*
.. i18n: 
.. i18n:   Using relation fields **many2one** with **selection**. In fields definitions add::
.. i18n: 
.. i18n:         ...,
.. i18n:         'my_field': fields.many2one(
.. i18n:         	'mymodule.relation.model', 
.. i18n:         	'Title', 
.. i18n:         	selection=_sel_func),
.. i18n:         ...,
.. i18n: 
.. i18n:   And then define the _sel_func like this (but before the fields definitions)::
.. i18n: 
.. i18n:         def _sel_func(self, cr, uid, context=None):
.. i18n:             obj = self.pool.get('mymodule.relation.model')
.. i18n:             ids = obj.search(cr, uid, [])
.. i18n:             res = obj.read(cr, uid, ids, ['name', 'id'], context)
.. i18n:             res = [(r['id'], r['name']) for r in res]
.. i18n:             return res
..

  Syntax::

                fields.selection((('n','Unconfirmed'), ('c','Confirmed')),
                                   'Field Name' [, Optional Parameters]),

  .. note::

             Format of the selection parameter: tuple of tuples of strings of the form::

                (('key_or_value', 'string_to_display'), ... )
                
  .. note::
             You can specify a function that will return the tuple. Example ::
             
                 def _get_selection(self, cursor, user_id, context=None):
                     return (
                     	('choice1', 'This is the choice 1'), 
                     	('choice2', 'This is the choice 2'))
                     
                 _columns = {
                    'sel' : fields.selection(
                    	_get_selection, 
                    	'What do you want ?')
                 }

  *Example*

  Using relation fields **many2one** with **selection**. In fields definitions add::

        ...,
        'my_field': fields.many2one(
        	'mymodule.relation.model', 
        	'Title', 
        	selection=_sel_func),
        ...,

  And then define the _sel_func like this (but before the fields definitions)::

        def _sel_func(self, cr, uid, context=None):
            obj = self.pool.get('mymodule.relation.model')
            ids = obj.search(cr, uid, [])
            res = obj.read(cr, uid, ids, ['name', 'id'], context)
            res = [(r['id'], r['name']) for r in res]
            return res

.. i18n: Relational Types
.. i18n: ++++++++++++++++
..

Relational Types
++++++++++++++++

.. i18n: :one2one:
..

:one2one:

.. i18n:   A one2one field expresses a one:to:one relation between two objects. It is
.. i18n:   deprecated. Use many2one instead.
..

  表示有两个对象是一对一的关系。现在用many2one来代替。

.. i18n:   Syntax::
.. i18n: 
.. i18n:                 fields.one2one('other.object.name', 'Field Name')
..

  Syntax::

                fields.one2one('other.object.name', 'Field Name')

.. i18n: :many2one:
..

:many2one:

.. i18n:   Associates this object to a parent object via this Field. For example
.. i18n:   Department an Employee belongs to would Many to one. i.e Many employees will
.. i18n:   belong to a Department
..

  通过这个字段一个对象与它的父对象关联。例如，员工和部门的关系就是多对一的关系。

.. i18n:   Syntax::
.. i18n: 
.. i18n: 		fields.many2one(
.. i18n: 			'other.object.name', 
.. i18n: 			'Field Name', 
.. i18n: 			optional parameters)
.. i18n: 
.. i18n:   Optional parameters:
.. i18n:   
.. i18n:     - ondelete: What should happen when the resource this field points to is deleted.
.. i18n:             + Predefined value: "cascade", "set null", "restrict", "no action", "set default"
.. i18n:             + Default value: "set null"
.. i18n:     - required: True
.. i18n:     - readonly: True
.. i18n:     - select: True - (creates an index on the Foreign Key field)
.. i18n: 
.. i18n:   *Example* ::
.. i18n: 
.. i18n:                 'commercial': fields.many2one(
.. i18n:                 	'res.users', 
.. i18n:                 	'Commercial', 
.. i18n:                 	ondelete='cascade'),
..

  Syntax::

		fields.many2one(
			'other.object.name', 
			'Field Name', 
			optional parameters)

  可选的参数:
  
    - ondelete: 当该字段指示的资源被删除时会发生些什么
            + 预先定义的值: "cascade", "set null", "restrict", "no action", "set default"
            + 缺省值: "set null"
    - required: True
    - readonly: True
    - select: True - (creates an index on the Foreign Key field)

  *Example* ::

                'commercial': fields.many2one(
                	'res.users', 
                	'Commercial', 
                	ondelete='cascade'),

.. i18n: :one2many:
..

:one2many:

.. i18n:   TODO
..

  TODO

.. i18n:   Syntax::
.. i18n: 
.. i18n:                 fields.one2many(
.. i18n:                 	'other.object.name', 
.. i18n:                 	'Field relation id', 
.. i18n:                 	'Fieldname', 
.. i18n:                 	optional parameter)
.. i18n: 
.. i18n:   Optional parameters:
.. i18n:                 - invisible: True/False
.. i18n:                 - states: ?
.. i18n:                 - readonly: True/False
.. i18n: 
.. i18n:   *Example* ::
.. i18n: 
.. i18n:                 'address': fields.one2many(
.. i18n:                 	'res.partner.address', 
.. i18n:                 	'partner_id', 
.. i18n:                 	'Contacts'),
..

  Syntax::

                fields.one2many(
                	'other.object.name', 
                	'Field relation id', 
                	'Fieldname', 
                	optional parameter)

  可选的参数：
                - invisible: True/False
                - states: ?
                - readonly: True/False

  *Example* ::

                'address': fields.one2many(
                	'res.partner.address', 
                	'partner_id', 
                	'Contacts'),

.. i18n: :many2many:
..

:many2many:

.. i18n:         TODO
..

        TODO

.. i18n:         Syntax::
.. i18n: 
.. i18n:                 fields.many2many('other.object.name',
.. i18n:                                  'relation object',
.. i18n:                                  'actual.object.id',
.. i18n:                                  'other.object.id',                                 
.. i18n:                                  'Field Name')
.. i18n: 
.. i18n:         Where:
.. i18n:                 - other.object.name is the other object which belongs to the relation
.. i18n:                 - relation object is the table that makes the link
.. i18n:                 - actual.object.id and other.object.id are the fields' names used in the relation table
.. i18n: 
.. i18n:         Example::
.. i18n: 
.. i18n:                 'category_ids':
.. i18n:                    fields.many2many(
.. i18n:                     'res.partner.category',
.. i18n:                     'res_partner_category_rel',
.. i18n:                     'partner_id',
.. i18n:                     'category_id',
.. i18n:                     'Categories'),
.. i18n: 
.. i18n:         To make it bidirectional (= create a field in the other object)::
.. i18n: 
.. i18n:                 class other_object_name2(osv.osv):
.. i18n:                     _inherit = 'other.object.name'
.. i18n:                     _columns = {
.. i18n:                         'other_fields': fields.many2many(
.. i18n:                             'actual.object.name', 
.. i18n:                             'relation object', 
.. i18n:                             'actual.object.id', 
.. i18n:                             'other.object.id', 
.. i18n:                             'Other Field Name'),
.. i18n:                     }
.. i18n:                 other_object_name2()
.. i18n: 
.. i18n:         Example::
.. i18n: 
.. i18n:                 class res_partner_category2(osv.osv):
.. i18n:                     _inherit = 'res.partner.category'
.. i18n:                     _columns = {
.. i18n:                         'partner_ids': fields.many2many(
.. i18n:                             'res.partner', 
.. i18n:                             'res_partner_category_rel', 
.. i18n:                             'category_id', 
.. i18n:                             'partner_id', 
.. i18n:                             'Partners'),
.. i18n:                     }
.. i18n:                 res_partner_category2()
..

        Syntax::

                fields.many2many('other.object.name',
                                 'relation object',
                                 'actual.object.id',
                                 'other.object.id',                                 
                                 'Field Name')

        Where:
                - other.object.name是属于这个关系的其他对象。
                - relation object做该关系链接的表格
                - actual.object.id和other.object.id是用于关系表格的字段名称。

        Example::

                'category_ids':
                   fields.many2many(
                    'res.partner.category',
                    'res_partner_category_rel',
                    'partner_id',
                    'category_id',
                    'Categories'),

        To make it bidirectional (= create a field in the other object)::

                class other_object_name2(osv.osv):
                    _inherit = 'other.object.name'
                    _columns = {
                        'other_fields': fields.many2many(
                            'actual.object.name', 
                            'relation object', 
                            'actual.object.id', 
                            'other.object.id', 
                            'Other Field Name'),
                    }
                other_object_name2()

        Example::

                class res_partner_category2(osv.osv):
                    _inherit = 'res.partner.category'
                    _columns = {
                        'partner_ids': fields.many2many(
                            'res.partner', 
                            'res_partner_category_rel', 
                            'category_id', 
                            'partner_id', 
                            'Partners'),
                    }
                res_partner_category2()

.. i18n: :related:
..

:related:

.. i18n:   Sometimes you need to refer to the relation of a relation. For example,
.. i18n:   supposing you have objects: City -> State -> Country, and you need to refer to
.. i18n:   the Country from a City, you can define a field as below in the City object::
.. i18n: 
.. i18n:         'country_id': fields.related(
.. i18n:             'state_id', 
.. i18n:             'country_id', 
.. i18n:             type="many2one",
.. i18n:             relation="res.country",
.. i18n:             string="Country", 
.. i18n:             store=False)
.. i18n: 
.. i18n:   Where:
.. i18n:   	- The first set of parameters are the chain of reference fields to
.. i18n:   	  follow, with the desired field at the end.
.. i18n:   	- :guilabel:`type` is the type of that desired field.
.. i18n:   	- Use :guilabel:`relation` if the desired field is still some kind of
.. i18n:   	  reference. :guilabel:`relation` is the table to look up that
.. i18n:   	  reference in.
..

  有时候你需要考虑关联中的关联。例如，假设你有这样的对象：City -> State -> Country，你需要从一个城市名得到一个国家名，你可以在City对象中定义::

        'country_id': fields.related(
            'state_id', 
            'country_id', 
            type="many2one",
            relation="res.country",
            string="Country", 
            store=False)

  Where:
  	- The first set of parameters are the chain of reference fields to
  	  follow, with the desired field at the end.
  	- :guilabel:type是期望字段的类型。
  	- Use :guilabel:`relation` if the desired field is still some kind of
  	  reference. :guilabel:`relation` is the table to look up that
  	  reference in.

.. i18n: Functional Fields
.. i18n: +++++++++++++++++
..

Functional Fields
+++++++++++++++++

.. i18n: A functional field is a field whose value is calculated by a function (rather
.. i18n: than being stored in the database).
..

函数字段是通过函数计算了值的字段。 (而不是存储在数据库中).

.. i18n: **Parameters:** ::
.. i18n: 
.. i18n:     fnct, arg=None, fnct_inv=None, fnct_inv_arg=None, type="float",
.. i18n:         fnct_search=None, obj=None, method=False, store=False, multi=False
..

**参数:** ::

    fnct, arg=None, fnct_inv=None, fnct_inv_arg=None, type="float",
        fnct_search=None, obj=None, method=False, store=False, multi=False

.. i18n: where
..

where

.. i18n:     * :guilabel:`fnct` is the function or method that will compute the field 
.. i18n:       value. It must have been declared before declaring the functional field.
.. i18n:     * :guilabel:`fnct_inv` is the function or method that will allow writing
.. i18n:       values in that field.
.. i18n:     * :guilabel:`type` is the field type name returned by the function. It can
.. i18n:       be any field type name except function.
.. i18n:     * :guilabel:`fnct_search` allows you to define the searching behaviour on
.. i18n:       that field.
.. i18n:     * :guilabel:`method` whether the field is computed by a method (of an
.. i18n:       object) or a global function
.. i18n:     * :guilabel:`store` If you want to store field in database or not. Default
.. i18n:       is False.
.. i18n:     * :guilabel:`multi` is a group name. All fields with the same `multi`
.. i18n:       parameter will be calculated in a single function call. 
..

    * :guilabel:`fnct` 是计算字段值的函数或者方法。它必须在声明该函数字段前定义。
    * :guilabel:`fnct_inv` 用来为改制段写入值的函数或者方法.
    * :guilabel:`type` 由函数返回的字段类型名称. 可以是函数以外的任何字段类型名称.
    * :guilabel:`fnct_search` 允许你在该字段上面定义搜索行为.
    * :guilabel:`method` 指明了该字段是由一个方法（属于对象）或者一个全局函数计算的。
    * :guilabel:`store` 是否要储存该字段在数据库中。默认是 False.
    * :guilabel:`multi` 是一个组名. 所有具有相同 `multi` 参数的字段将被在单次函数调用中计算。 

.. i18n: fnct parameter
.. i18n: """"""""""""""
.. i18n: If *method* is True, the signature of the method must be::
.. i18n: 
.. i18n:     def fnct(self, cr, uid, ids, field_name, arg, context):
..

fnct 参数
""""""""""""""
如果 *method* 是 True, 那么方法的声明必须是这样的::

    def fnct(self, cr, uid, ids, field_name, arg, context):

.. i18n: otherwise (if it is a global function), its signature must be::
.. i18n: 
.. i18n:     def fnct(cr, table, ids, field_name, arg, context):
..

否则(如果是个全局函数), 它的声明必须是这样::

    def fnct(cr, table, ids, field_name, arg, context):

.. i18n: Either way, it must return a dictionary of values of the form
.. i18n: **{id'_1_': value'_1_', id'_2_': value'_2_',...}.**
..

不管哪种形式，它的返回值形式是：
**{id'_1_': value'_1_', id'_2_': value'_2_',...}.**

.. i18n: The values of the returned dictionary must be of the type specified by the type 
.. i18n: argument in the field declaration.
..

返回值必须是之前定义的类型。

.. i18n: If *multi* is set, then *field_name* is replaced by *field_names*: a list
.. i18n: of the field names that should be calculated. Each value in the returned 
.. i18n: dictionary is also a dictionary from field name to value. For example, if the
.. i18n: fields `'name'`, and `'age'` are both based on the `vital_statistics` function,
.. i18n: then the return value of `vital_statistics` might look like this when `ids` is
.. i18n: `[1, 2, 5]`::
.. i18n: 
.. i18n:     {
.. i18n:         1: {'name': 'Bob', 'age': 23}, 
.. i18n:         2: {'name': 'Sally', 'age', 19}, 
.. i18n:         5: {'name': 'Ed', 'age': 62}
.. i18n:     }
..

如果multi是set，则field_name将会被field_names代替：a list of the field names会被计算。Each value in the returned dictionary is also a dictionary from field name to value.例如，如果字段’name’和’age’都基于函数vital_statistics，那么该函数的返回值应该是这样（当ids是[1,2,5]）：::

    {
        1: {'name': 'Bob', 'age': 23}, 
        2: {'name': 'Sally', 'age', 19}, 
        5: {'name': 'Ed', 'age': 62}
    }

.. i18n: fnct_inv parameter
.. i18n: """"""""""""""""""
.. i18n: If *method* is true, the signature of the method must be::
.. i18n: 
.. i18n:     def fnct(self, cr, uid, ids, field_name, field_value, arg, context):
.. i18n:     
..

fnct_inv parameter
""""""""""""""""""
如果method是True，那么method声明是：::

    def fnct(self, cr, uid, ids, field_name, field_value, arg, context):
    

.. i18n: otherwise (if it is a global function), it should be::
.. i18n: 
.. i18n:     def fnct(cr, table, ids, field_name, field_value, arg, context):
..

不然（如果是全局函数），声明是::

    def fnct(cr, table, ids, field_name, field_value, arg, context):

.. i18n: fnct_search parameter
.. i18n: """""""""""""""""""""
.. i18n: If method is true, the signature of the method must be::
.. i18n: 
.. i18n:     def fnct(self, cr, uid, obj, name, args, context):
..

fnct_search parameter
"""""""""""""""""""""
If method is true, the signature of the method must be::

    def fnct(self, cr, uid, obj, name, args, context):

.. i18n: otherwise (if it is a global function), it should be::
.. i18n: 
.. i18n:     def fnct(cr, uid, obj, name, args, context):
..

otherwise (if it is a global function), it should be::

    def fnct(cr, uid, obj, name, args, context):

.. i18n: The return value is a list containing 3-part tuples which are used in search function::
.. i18n: 
.. i18n:     return [('id','in',[1,3,5])]
..

在查找函数中，返回值是三元祖的列表。

    return [('id','in',[1,3,5])]

.. i18n: *obj* is the same as *self*, and *name* receives the field name. *args* is a list
.. i18n: of 3-part tuples containing search criteria for this field, although the search
.. i18n: function may be called separately for each tuple.
..

obj和self相同，name接受字段名。args是三元祖的列表，包含这个字段的查询规范，即使每个元祖分别调用该查询函数。

.. i18n: Example
.. i18n: """""""
.. i18n: Suppose we create a contract object which is :
..

例子
"""""""
我们创建这样一个contract对象：

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     class hr_contract(osv.osv):
.. i18n:         _name = 'hr.contract'
.. i18n:         _description = 'Contract'
.. i18n:         _columns = {
.. i18n:             'name' : fields.char('Contract Name', size=30, required=True),
.. i18n:             'employee_id' : fields.many2one('hr.employee', 'Employee', required=True),
.. i18n:             'function' : fields.many2one('res.partner.function', 'Function'),
.. i18n:         }
.. i18n:     hr_contract()
..

.. code-block:: python

    class hr_contract(osv.osv):
        _name = 'hr.contract'
        _description = 'Contract'
        _columns = {
            'name' : fields.char('Contract Name', size=30, required=True),
            'employee_id' : fields.many2one('hr.employee', 'Employee', required=True),
            'function' : fields.many2one('res.partner.function', 'Function'),
        }
    hr_contract()

.. i18n: If we want to add a field that retrieves the function of an employee by looking its current contract, we use a functional field. The object hr_employee is inherited this way:
..

如果添加一个字段要通过看它的current contract来检索员工，我们使用functional field。对象hr_employee这样继承：

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     class hr_employee(osv.osv):
.. i18n:         _name = "hr.employee"
.. i18n:         _description = "Employee"
.. i18n:         _inherit = "hr.employee"
.. i18n:         _columns = {
.. i18n:             'contract_ids' : fields.one2many('hr.contract', 'employee_id', 'Contracts'),
.. i18n:             'function' : fields.function(
.. i18n:                 _get_cur_function_id, 
.. i18n:                 type='many2one', 
.. i18n:                 obj="res.partner.function",
.. i18n:                 method=True, 
.. i18n:                 string='Contract Function'),
.. i18n:         }
.. i18n:     hr_employee()
..

.. code-block:: python

    class hr_employee(osv.osv):
        _name = "hr.employee"
        _description = "Employee"
        _inherit = "hr.employee"
        _columns = {
            'contract_ids' : fields.one2many('hr.contract', 'employee_id', 'Contracts'),
            'function' : fields.function(
                _get_cur_function_id, 
                type='many2one', 
                obj="res.partner.function",
                method=True, 
                string='Contract Function'),
        }
    hr_employee()

.. i18n: .. note:: three points
.. i18n: 
.. i18n:         * :guilabel:`type` ='many2one' is because the function field must create
.. i18n:           a many2one field; function is declared as a many2one in hr_contract also.
.. i18n:         * :guilabel:`obj` ="res.partner.function" is used to specify that the
.. i18n:           object to use for the many2one field is res.partner.function.
.. i18n:         * We called our method :guilabel:`_get_cur_function_id` because its role
.. i18n:           is to return a dictionary whose keys are ids of employees, and whose
.. i18n:           corresponding values are ids of the function of those employees. The 
.. i18n:           code of this method is:
..

.. 注意有三点：

        * :guilabel:`type` ='many2one' is because the function field must create
          a many2one field; function is declared as a many2one in hr_contract also.
        * :guilabel:`obj` ="res.partner.function" is used to specify that the
          object to use for the many2one field is res.partner.function.
        * We called our method :guilabel:`_get_cur_function_id` because its role
          is to return a dictionary whose keys are ids of employees, and whose
          corresponding values are ids of the function of those employees. The 
          code of this method is:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     def _get_cur_function_id(self, cr, uid, ids, field_name, arg, context):
.. i18n:         for i in ids:
.. i18n:             #get the id of the current function of the employee of identifier "i"
.. i18n:             sql_req= """
.. i18n:             SELECT f.id AS func_id
.. i18n:             FROM hr_contract c
.. i18n:               LEFT JOIN res_partner_function f ON (f.id = c.function)
.. i18n:             WHERE
.. i18n:               (c.employee_id = %d)
.. i18n:             """ % (i,)
.. i18n:     
.. i18n:             cr.execute(sql_req)
.. i18n:             sql_res = cr.dictfetchone()
.. i18n:     
.. i18n:             if sql_res: #The employee has one associated contract
.. i18n:                 res[i] = sql_res['func_id']
.. i18n:             else:
.. i18n:                 #res[i] must be set to False and not to None because of XML:RPC
.. i18n:                 # "cannot marshal None unless allow_none is enabled"
.. i18n:                 res[i] = False
.. i18n:         return res
..

.. code-block:: python

    def _get_cur_function_id(self, cr, uid, ids, field_name, arg, context):
        for i in ids:
            #get the id of the current function of the employee of identifier "i"
            sql_req= """
            SELECT f.id AS func_id
            FROM hr_contract c
              LEFT JOIN res_partner_function f ON (f.id = c.function)
            WHERE
              (c.employee_id = %d)
            """ % (i,)
    
            cr.execute(sql_req)
            sql_res = cr.dictfetchone()
    
            if sql_res: #The employee has one associated contract
                res[i] = sql_res['func_id']
            else:
                #res[i] must be set to False and not to None because of XML:RPC
                # "cannot marshal None unless allow_none is enabled"
                res[i] = False
        return res

.. i18n: The id of the function is retrieved using a SQL query. Note that if the query 
.. i18n: returns no result, the value of sql_res['func_id'] will be None. We force the
.. i18n: False value in this case value because XML:RPC (communication between the server 
.. i18n: and the client) doesn't allow to transmit this value.
..

在SQL query中使用函数的id来检索。如果这个查询没有结果返回，那么sql_res[‘func_id’]的值为None。我们必须将值设为False，因为XML:RPC不允许传送该值。

.. i18n: store Parameter
.. i18n: """""""""""""""
.. i18n: It will calculate the field and store the result in the table. The field will be
.. i18n: recalculated when certain fields are changed on other objects. It uses the
.. i18n: following syntax:
..

store Parameter
"""""""""""""""
它会计算该字段的值，并且将结果存储在表中。当其他对象中相应该字段的值发生变化时会重新计算它。它使用一下句法：

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     store = {
.. i18n:         'object_name': (
.. i18n:         	function_name, 
.. i18n:         	['field_name1', 'field_name2'],
.. i18n:         	priority)
.. i18n:     }
..

.. code-block:: python

    store = {
        'object_name': (
        	function_name, 
        	['field_name1', 'field_name2'],
        	priority)
    }

.. i18n: It will call function function_name when any changes are written to fields in the
.. i18n: list ['field1','field2'] on object 'object_name'. The function should have the
.. i18n: following signature::
.. i18n: 
.. i18n:     def function_name(self, cr, uid, ids, context=None):
..

当对象object_name中列表['field1','field2']中的字段发生变化时，会调用函数function_name。函数声明如下：

    def function_name(self, cr, uid, ids, context=None):

.. i18n: Where `ids` will be the ids of records in the other object's table that have
.. i18n: changed values in the watched fields. The function should return a list of ids
.. i18n: of records in its own table that should have the field recalculated. That list 
.. i18n: will be sent as a parameter for the main function of the field.
..

ids是其他对象表中记录的ids，这些对象有些字段值已被更改。这个函数在自己表中返回a list of ids of records 并且有些值已被更改。这个list作为main函数的参数字段。

.. i18n: Here's an example from the membership module:
..

下面是一个membership模块的例子：

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     'membership_state':
.. i18n:         fields.function(
.. i18n:             _membership_state,
.. i18n:             method=True, 
.. i18n:             string='Current membership state',
.. i18n:             type='selection', 
.. i18n:             selection=STATE,
.. i18n:             store={
.. i18n:                 'account.invoice': (_get_invoice_partner, ['state'], 10),
.. i18n:                 'membership.membership_line': (_get_partner_id,['state'], 10),
.. i18n:                 'res.partner': (
.. i18n:                     lambda self, cr, uid, ids, c={}: ids, 
.. i18n:                     ['free_member'], 
.. i18n:                     10)
.. i18n:             }),
..

.. code-block:: python

    'membership_state':
        fields.function(
            _membership_state,
            method=True, 
            string='Current membership state',
            type='selection', 
            selection=STATE,
            store={
                'account.invoice': (_get_invoice_partner, ['state'], 10),
                'membership.membership_line': (_get_partner_id,['state'], 10),
                'res.partner': (
                    lambda self, cr, uid, ids, c={}: ids, 
                    ['free_member'], 
                    10)
            }),

.. i18n: Property Fields
.. i18n: +++++++++++++++
..

Property Fields
+++++++++++++++

.. i18n: .. describe:: Declaring a property
..

.. describe:: Declaring a property

.. i18n: A property is a special field: fields.property.
..

property是一个特定的字段：fields.property

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         class res_partner(osv.osv):
.. i18n:             _name = "res.partner"
.. i18n:             _inherit = "res.partner"
.. i18n:             _columns = {
.. i18n:                         'property_product_pricelist':
.. i18n: 						    fields.property(
.. i18n:                         		'product.pricelist',
.. i18n:                                 type='many2one',
.. i18n:                                 relation='product.pricelist',
.. i18n:                                 string="Sale Pricelist",
.. i18n:                         		method=True,
.. i18n:                         		view_load=True,
.. i18n:                         		group_name="Pricelists Properties"),
.. i18n:             }
..

.. code-block:: python

        class res_partner(osv.osv):
            _name = "res.partner"
            _inherit = "res.partner"
            _columns = {
                        'property_product_pricelist':
						    fields.property(
                        		'product.pricelist',
                                type='many2one',
                                relation='product.pricelist',
                                string="Sale Pricelist",
                        		method=True,
                        		view_load=True,
                        		group_name="Pricelists Properties"),
            }

.. i18n: Then you have to create the default value in a .XML file for this property:
..

你要在.xml文件中为这个property创建一个默认值：

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:         <record model="ir.property" id="property_product_pricelist">
.. i18n:             <field name="name">property_product_pricelist</field>
.. i18n:             <field name="fields_id" search="[('model','=','res.partner'),
.. i18n:               ('name','=','property_product_pricelist')]"/>
.. i18n:             <field name="value" eval="'product.pricelist,'+str(list0)"/>
.. i18n:         </record>
..

.. code-block:: xml

        <record model="ir.property" id="property_product_pricelist">
            <field name="name">property_product_pricelist</field>
            <field name="fields_id" search="[('model','=','res.partner'),
              ('name','=','property_product_pricelist')]"/>
            <field name="value" eval="'product.pricelist,'+str(list0)"/>
        </record>

.. i18n: ..
..

..

.. i18n: .. tip::
.. i18n: 
.. i18n:         if the default value points to a resource from another module, you can use the ref function like this:
.. i18n: 
.. i18n:         <field name="value" eval="'product.pricelist,'+str(ref('module.data_id'))"/>
..

.. tip::

        if the default value points to a resource from another module, you can use the ref function like this:

        <field name="value" eval="'product.pricelist,'+str(ref('module.data_id'))"/>

.. i18n: **Putting properties in forms**
..

**Putting properties in forms**

.. i18n: To add properties in forms, just put the <properties/> tag in your form. This will automatically add all properties fields that are related to this object. The system will add properties depending on your rights. (some people will be able to change a specific property, others won't).
..

想要在表单中添加属性，就要放<properties/>标签在表单中。这会自动添加与该对象相关的所有属性字段。你有权添加想要的属性。

.. i18n: Properties are displayed by section, depending on the group_name attribute. (It is rendered in the client like a separator tag).
..

属性值以部分的形式显示，依赖于group_name属性（这个在客户端像分隔符标签的样子渲染）。

.. i18n: **How does this work ?**
..

**How does this work ?**

.. i18n: The fields.property class inherits from fields.function and overrides the read and write method. The type of this field is many2one, so in the form a property is represented like a many2one function.
..

fields.property类继承自fields.function，重写了读写方法。这个字段的type是many2one，所以在表单中，property像many2one方法那样显示。

.. i18n: But the value of a property is stored in the ir.property class/table as a complete record. The stored value is a field of type reference (not many2one) because each property may point to a different object. If you edit properties values (from the administration menu), these are represented like a field of type reference.
..

但是property的值作为一个完全的记录存储在ir.property class/table中。已存储的值是一个字段类型参考（不是many2one），因为每个property指向一个不同的对象。如果你要编辑properties values（从administration menu），这些代表着字段类型参考。

.. i18n: When you read a property, the program gives you the property attached to the instance of object you are reading. If this object has no value, the system will give you the default property.
..

当你读取一个property时，程序会给你链接该property附属的对象实例。如果该对象没有值，系统会给你缺省值。

.. i18n: The definition of a property is stored in the ir.model.fields class like any other fields. In the definition of the property, you can add groups that are allowed to change to property.
..

property的定义像其他字段一样存储在ir.model.fields类中。在property的定义中，你可以添加groups来更改property。

.. i18n: **Using properties or normal fields**
..

**Using properties or normal fields**

.. i18n: When you want to add a new feature, you will have to choose to implement it as a property or as normal field. Use a normal field when you inherit from an object and want to extend this object. Use a property when the new feature is not related to the object but to an external concept.
..

当你想要添加一个新feature，你会选择是作为property还是normal field来实现它。当你继承自对象并想要扩展它时，应该选择作为normal field。当新feature和对象不相关，只是一个外部概念时，应该选择作为property。

.. i18n: Here are a few tips to help you choose between a normal field or a property:
..

下面有些技巧来帮助你在normal field和property之间做选择：

.. i18n: Normal fields extend the object, adding more features or data.
..

Normal field扩展对象，增加很多features或是数据。

.. i18n: A property is a concept that is attached to an object and have special features:
..

A property是附属于对象的概念，有着特定的属性：

.. i18n: * Different value for the same property depending on the company
.. i18n: * Rights management per field
.. i18n: * It's a link between resources (many2one)
..

* 由公司决定相同的property有不同的值。
* 每个字段权限管理
* 资源之间的链接 (many2one)

.. i18n: **Example 1: Account Receivable**
..

**Example 1: Account Receivable**

.. i18n: The default "Account Receivable" for a specific partner is implemented as a property because:
..

对于一个特定partner的默认“Account Receivable”作为property执行是因为：

.. i18n:     * This is a concept related to the account chart and not to the partner, so it is an account property that is visible on a partner form. Rights have to be managed on this fields for accountants, these are not the same rights that are applied to partner objects. So you have specific rights just for this field of the partner form: only accountants may change the account receivable of a partner.
.. i18n: 
.. i18n:     * This is a multi-company field: the same partner may have different account receivable values depending on the company the user belongs to. In a multi-company system, there is one account chart per company. The account receivable of a partner depends on the company it placed the sale order.
.. i18n: 
.. i18n:     * The default account receivable is the same for all partners and is configured from the general property menu (in administration).
..

    * 这是个关系到account chart而不是partner的概念，所以account property在合作伙伴表单上是可见。会计人员有权管理这个字段。这不是相同的权限应用于partner对象。所以你对于partner表单的这个字段有特定的权限：只有会计人员可以更改the account receivable of a partner。

    * 1．这是个多公司字段：相同的partner有不同的account receivable values取决于这个用户属于哪个公司。在多公司系统中，每个公司有一个account chart。一个合作伙伴的account receivable取决于该公司的销售订单。

    * 1．对于所有合作伙伴的默认account receivable是相同的，由（administration中）主要property menu来配置。

.. i18n: .. note::
.. i18n:         One interesting thing is that properties avoid "spaghetti" code. The account module depends on the partner (base) module. But you can install the partner (base) module without the accounting module. If you add a field that points to an account in the partner object, both objects will depend on each other. It's much more difficult to maintain and code (for instance, try to remove a table when both tables are pointing to each others.)
..

.. note::
        One interesting thing is that properties avoid "spaghetti" code. The account module depends on the partner (base) module. But you can install the partner (base) module without the accounting module. If you add a field that points to an account in the partner object, both objects will depend on each other. It's much more difficult to maintain and code (for instance, try to remove a table when both tables are pointing to each others.)

.. i18n: **Example 2: Product Times**
..

**Example 2: Product Times**

.. i18n: The product expiry module implements all delays related to products: removal date, product usetime, ... This module is very useful for food industries.
..

生产到期模块实现所有相关产品的逾期：搬运日期，生产所用时间…这个模块对于食品生产非常有用。

.. i18n: This module inherits from the product.product object and adds new fields to it:
..

这个模块继承自product.product，并且添加新字段到其中：

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         class product_product(osv.osv):
.. i18n: 
.. i18n:             _inherit = 'product.product'
.. i18n:             _name = 'product.product'
.. i18n:             _columns = {
.. i18n: 
.. i18n:                 'life_time': fields.integer('Product lifetime'),
.. i18n:                 'use_time': fields.integer('Product usetime'),
.. i18n:                 'removal_time': fields.integer('Product removal time'),
.. i18n:                 'alert_time': fields.integer('Product alert time'),
.. i18n:                 }
.. i18n: 
.. i18n:         product_product()
..

.. code-block:: python

        class product_product(osv.osv):

            _inherit = 'product.product'
            _name = 'product.product'
            _columns = {

                'life_time': fields.integer('Product lifetime'),
                'use_time': fields.integer('Product usetime'),
                'removal_time': fields.integer('Product removal time'),
                'alert_time': fields.integer('Product alert time'),
                }

        product_product()

.. i18n: ..
..

..

.. i18n: This module adds simple fields to the product.product object. We did not use properties because:
..

这个模块添加简单的字段到product.product对象中。我们不使用properties的原因是：

.. i18n:     * We extend a product, the life_time field is a concept related to a product, not to another object.
.. i18n:     * We do not need a right management per field, the different delays are managed by the same people that manage all products.
..

    * 我们扩展一个product，life_time字段是相关到product而不是另一个对象的概念
    * 我们不需要一个字段有个权限管理，不同的延迟被管理所有产品的人管理着。

.. i18n: ORM methods
.. i18n: -----------
..

ORM methods
-----------

.. i18n: Keeping the context in ORM methods
.. i18n: ++++++++++++++++++++++++++++++++++
..

Keeping the context in ORM methods
++++++++++++++++++++++++++++++++++

.. i18n: In OpenObject, the context holds very important data such as the language in
.. i18n: which a document must be written, whether function field needs updating or not,
.. i18n: etc.
..

在OpenObject中，上下文保留重要数据类似文档必须被写入的语言等，无论function field是否需要更新等。

.. i18n: When calling an ORM method, you will probably already have a context - for
.. i18n: example the framework will provide you with one as a parameter of almost 
.. i18n: every method.
.. i18n: If you do have a context, it is very important that you always pass it through
.. i18n: to every single method you call.
..

当调用ORM方法时，你已经拥有一个上下文，例如，框架提供给你一个几乎每个方法的参数。如果你有一个上下文，那么你一直带它通过你调用的每个单独的方法是很重要的。


.. i18n: This rule also applies to writing ORM methods. You should expect to receive a
.. i18n: context as parameter, and always pass it through to every other method you call.. 
..

这个规则适用于写ORM方法。你应该希望接受一个上下文作为参数，让它一直通过你调用的其他方法。 

.. i18n: ORM methods
.. i18n: +++++++++++
..

ORM methods
+++++++++++

.. i18n: .. automodule:: openerp.osv.orm
.. i18n:    :members:
.. i18n:    :show-inheritance:
..

.. automodule:: openerp.osv.orm
   :members:
   :show-inheritance:
