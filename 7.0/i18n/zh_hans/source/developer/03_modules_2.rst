
.. i18n: Objects, Fields and Methods
.. i18n: ===========================
..

Objects, Fields and Methods
===========================

.. i18n: OpenERP Objects
.. i18n: ---------------
..

OpenERP Objects
---------------

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

All the ERP's pieces of data are accessible through "objects". As an example, there is a res.partner object to access the data concerning the partners, an account.invoice object for the data concerning the invoices, etc...

.. i18n: Please note that there is an object for every type of resource, and not an
.. i18n: object per resource. We have thus a res.partner object to manage all the
.. i18n: partners and not a *res.partner* object per partner. If we talk in "object
.. i18n: oriented" terms, we could also say that there is an object per level.
..

Please note that there is an object for every type of resource, and not an
object per resource. We have thus a res.partner object to manage all the
partners and not a *res.partner* object per partner. If we talk in "object
oriented" terms, we could also say that there is an object per level.

.. i18n: The direct consequences is that all the methods of objects have a common parameter: the "ids" parameter. This specifies on which resources (for example, on which partner) the method must be applied. Precisely, this parameter contains a list of resource ids on which the method must be applied.
..

The direct consequences is that all the methods of objects have a common parameter: the "ids" parameter. This specifies on which resources (for example, on which partner) the method must be applied. Precisely, this parameter contains a list of resource ids on which the method must be applied.

.. i18n: For example, if we have two partners with the identifiers 1 and 5, and we want to call the res_partner method "send_email", we will write something like::
.. i18n: 
.. i18n:         res_partner.send_email(... , [1, 5], ...)
..

For example, if we have two partners with the identifiers 1 and 5, and we want to call the res_partner method "send_email", we will write something like::

        res_partner.send_email(... , [1, 5], ...)

.. i18n: We will see the exact syntax of object method calls further in this document.
..

We will see the exact syntax of object method calls further in this document.

.. i18n: In the following section, we will see how to define a new object. Then, we will check out the different methods of doing this.
..

In the following section, we will see how to define a new object. Then, we will check out the different methods of doing this.

.. i18n: For developers:
..

For developers:

.. i18n: * OpenERP "objects" are usually called classes in object oriented programming.
.. i18n: * A OpenERP "resource" is usually called an object in OO programming, instance of a class. 
..

* OpenERP "objects" are usually called classes in object oriented programming.
* A OpenERP "resource" is usually called an object in OO programming, instance of a class. 

.. i18n: It's a bit confusing when you try to program inside OpenERP, because the language used is Python, and Python is a fully object oriented language, and has objects and instances ...
..

It's a bit confusing when you try to program inside OpenERP, because the language used is Python, and Python is a fully object oriented language, and has objects and instances ...

.. i18n: Luckily, an OpenERP "resource" can be converted magically into a nice Python object using the "browse" class method (OpenERP object method).
..

Luckily, an OpenERP "resource" can be converted magically into a nice Python object using the "browse" class method (OpenERP object method).

.. i18n: The ORM - Object-relational mapping - Models
.. i18n: --------------------------------------------
..

The ORM - Object-relational mapping - Models
--------------------------------------------

.. i18n: The ORM, short for Object-Relational Mapping, is a central part of OpenERP.
..

The ORM, short for Object-Relational Mapping, is a central part of OpenERP.

.. i18n: In OpenERP, the data model is described and manipulated through Python classes
.. i18n: and objects. It is the ORM job to bridge the gap -- as transparently as
.. i18n: possible for the developer -- between Python and the underlying relational
.. i18n: database (PostgreSQL), which will provide the persistence we need for our
.. i18n: objects.
..

In OpenERP, the data model is described and manipulated through Python classes
and objects. It is the ORM job to bridge the gap -- as transparently as
possible for the developer -- between Python and the underlying relational
database (PostgreSQL), which will provide the persistence we need for our
objects.

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

To define a new object, you must define a new Python class then instantiate it. This class must inherit from the osv class in the osv module.

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

The first line of the object definition will always be of the form::

        class name_of_the_object(osv.osv):
                _name = 'name.of.the.object'
                _columns = { ... }
                ...
        name_of_the_object()

.. i18n: An object is defined by declaring some fields with predefined names in the
.. i18n: class. Two of them are required (_name and _columns), the rest are optional.
.. i18n: The predefined fields are:
..

An object is defined by declaring some fields with predefined names in the
class. Two of them are required (_name and _columns), the rest are optional.
The predefined fields are:

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
  Determines whether a corresponding PostgreSQL table must be generated
  automatically from the object. Setting _auto to False can be useful in case
  of OpenERP objects generated from PostgreSQL views. See the "Reporting From
  PostgreSQL Views" section for more details.

.. i18n: `_columns (required)`
.. i18n:   The object fields. See the :ref:`fields <fields-link>` section for further details.
..

`_columns (required)`
  The object fields. See the :ref:`fields <fields-link>` section for further details.

.. i18n: `_constraints`
.. i18n:   The constraints on the object. See the constraints section for details.
..

`_constraints`
  The constraints on the object. See the constraints section for details.

.. i18n: `_sql_constraints`
.. i18n:   The SQL Constraint on the object. See the SQL constraints section for further details.
..

`_sql_constraints`
  The SQL Constraint on the object. See the SQL constraints section for further details.

.. i18n: `_defaults`
.. i18n:   The default values for some of the object's fields. See the default value section for details.
..

`_defaults`
  The default values for some of the object's fields. See the default value section for details.

.. i18n: `_inherit`
.. i18n:   The name of the osv object which the current object inherits from. See the :ref:`object inheritance section<inherit-link>`
.. i18n:   (first form) for further details.
..

`_inherit`
  The name of the osv object which the current object inherits from. See the :ref:`object inheritance section<inherit-link>`
  (first form) for further details.

.. i18n: `_inherits`
.. i18n:   The list of osv objects the object inherits from. This list must be given in
.. i18n:   a python dictionary of the form: {'name_of_the_parent_object':
.. i18n:   'name_of_the_field', ...}. See the :ref:`object inheritance section<inherits-link>` 
.. i18n:   (second form) for further details. Default value: {}.
..

`_inherits`
  The list of osv objects the object inherits from. This list must be given in
  a python dictionary of the form: {'name_of_the_parent_object':
  'name_of_the_field', ...}. See the :ref:`object inheritance section<inherits-link>` 
  (second form) for further details. Default value: {}.

.. i18n: `_log_access`
.. i18n:   Determines whether or not the write access to the resource must be logged.
.. i18n:   If true, four fields will be created in the SQL table: create_uid,
.. i18n:   create_date, write_uid, write_date. Those fields represent respectively the
.. i18n:   id of the user who created the record, the creation date of record, the id
.. i18n:   of the user who last modified the record, and the date of that last
.. i18n:   modification. This data may be obtained by using the perm_read method.
..

`_log_access`
  Determines whether or not the write access to the resource must be logged.
  If true, four fields will be created in the SQL table: create_uid,
  create_date, write_uid, write_date. Those fields represent respectively the
  id of the user who created the record, the creation date of record, the id
  of the user who last modified the record, and the date of that last
  modification. This data may be obtained by using the perm_read method.

.. i18n: `_name (required)`
.. i18n:   Name of the object. Default value: None.
..

`_name (required)`
  Name of the object. Default value: None.

.. i18n: `_order`
.. i18n:   Name of the fields used to sort the results of the search and read methods.
..

`_order`
  Name of the fields used to sort the results of the search and read methods.

.. i18n:   Default value: 'id'.
..

  Default value: 'id'.

.. i18n:   Examples::
.. i18n: 
.. i18n:     _order = "name"  
.. i18n:     _order = "date_order desc"
..

  Examples::

    _order = "name"  
    _order = "date_order desc"

.. i18n: `_rec_name`
.. i18n:   Name of the field in which the name of every resource is stored. Default
.. i18n:   value: 'name'. Note: by default, the name_get method simply returns the
.. i18n:   content of this field.
..

`_rec_name`
  Name of the field in which the name of every resource is stored. Default
  value: 'name'. Note: by default, the name_get method simply returns the
  content of this field.

.. i18n: `_sequence`
.. i18n:   Name of the SQL sequence that manages the ids for this object. Default value: None.
..

`_sequence`
  Name of the SQL sequence that manages the ids for this object. Default value: None.

.. i18n: `_sql`
.. i18n:  SQL code executed upon creation of the object (only if _auto is True). It means this code gets executed after the table is created.
..

`_sql`
 SQL code executed upon creation of the object (only if _auto is True). It means this code gets executed after the table is created.

.. i18n: `_table`
.. i18n:   Name of the SQL table. Default value: the value of the _name field above
.. i18n:   with the dots ( . ) replaced by underscores ( _ ). 
..

`_table`
  Name of the SQL table. Default value: the value of the _name field above
  with the dots ( . ) replaced by underscores ( _ ). 

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

Objects may be inherited in some custom or specific modules. It is better to
inherit an object to add/modify some fields.

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

There are two possible ways to do this kind of inheritance. Both ways result in
a new class of data, which holds parent fields and behaviour as well as
additional fields and behaviour, but they differ in heavy programatical
consequences.

.. i18n: While Example 1 creates a new subclass "custom_material" that may be "seen" or
.. i18n: "used" by any view or tree which handles "network.material", this will not be
.. i18n: the case for Example 2.
..

While Example 1 creates a new subclass "custom_material" that may be "seen" or
"used" by any view or tree which handles "network.material", this will not be
the case for Example 2.

.. i18n: This is due to the table (other.material) the new subclass is operating on,
.. i18n: which will never be recognized by previous "network.material" views or trees.
..

This is due to the table (other.material) the new subclass is operating on,
which will never be recognized by previous "network.material" views or trees.

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

Example 1::

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

In this example, the 'custom_material' will add a new field 'manuf_warranty' to
the object 'network.material'. New instances of this class will be visible by
views or trees operating on the superclasses table 'network.material'.

.. i18n: This inheritancy is usually called "class inheritance" in Object oriented
.. i18n: design. The child inherits data (fields) and behavior (functions) of his
.. i18n: parent.
..

This inheritancy is usually called "class inheritance" in Object oriented
design. The child inherits data (fields) and behavior (functions) of his
parent.

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

Example 2::

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

In this example, the 'other_material' will hold all fields specified by
'network.material' and it will additionally hold a new field 'manuf_warranty'.
All those fields will be part of the table 'other.material'. New instances of
this class will therefore never been seen by views or trees operating on the
superclasses table 'network.material'.

.. i18n: This type of inheritancy is known as "inheritance by prototyping" (e.g.
.. i18n: Javascript), because the newly created subclass "copies" all fields from the
.. i18n: specified superclass (prototype). The child inherits data (fields) and behavior
.. i18n: (functions) of his parent.
..

This type of inheritancy is known as "inheritance by prototyping" (e.g.
Javascript), because the newly created subclass "copies" all fields from the
specified superclass (prototype). The child inherits data (fields) and behavior
(functions) of his parent.

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

The object 'tiny.object' inherits from all the columns and all the methods from
the n objects 'tiny.object_a', ..., 'tiny.object_n'.

.. i18n: To inherit from multiple tables, the technique consists in adding one column to
.. i18n: the table tiny_object per inherited object. This column will store a foreign
.. i18n: key (an id from another table). The values *'object_a_id' 'object_b_id' ...
.. i18n: 'object_n_id'* are of type string and determine the title of the columns in
.. i18n: which the foreign keys from 'tiny.object_a', ..., 'tiny.object_n' are stored.
..

To inherit from multiple tables, the technique consists in adding one column to
the table tiny_object per inherited object. This column will store a foreign
key (an id from another table). The values *'object_a_id' 'object_b_id' ...
'object_n_id'* are of type string and determine the title of the columns in
which the foreign keys from 'tiny.object_a', ..., 'tiny.object_n' are stored.

.. i18n: This inheritance mechanism is usually called " *instance inheritance* "  or  "
.. i18n: *value inheritance* ". A resource (instance) has the VALUES of its parents.
..

This inheritance mechanism is usually called " *instance inheritance* "  or  "
*value inheritance* ". A resource (instance) has the VALUES of its parents.

.. i18n: .. _fields-link:
.. i18n: 
.. i18n: Fields Introduction
.. i18n: -------------------
..

.. _fields-link:

Fields Introduction
-------------------

.. i18n: Objects may contain different types of fields. Those types can be divided into
.. i18n: three categories: simple types, relation types and functional fields. The
.. i18n: simple types are integers, floats, booleans, strings, etc ... ; the relation
.. i18n: types are used to represent relations between objects (one2one, one2many,
.. i18n: many2one). Functional fields are special fields because they are not stored in
.. i18n: the database but calculated in real time given other fields of the view.
..

Objects may contain different types of fields. Those types can be divided into
three categories: simple types, relation types and functional fields. The
simple types are integers, floats, booleans, strings, etc ... ; the relation
types are used to represent relations between objects (one2one, one2many,
many2one). Functional fields are special fields because they are not stored in
the database but calculated in real time given other fields of the view.

.. i18n: Here's the header of the initialization method of the class any field defined
.. i18n: in OpenERP inherits (as you can see in server/bin/osv/fields.py)::
.. i18n: 
.. i18n:     def __init__(self, string='unknown', required=False, readonly=False,
.. i18n:                  domain=None, context="", states=None, priority=0, change_default=False, size=None,
.. i18n:                  ondelete="set null", translate=False, select=False, **args) :
..

Here's the header of the initialization method of the class any field defined
in OpenERP inherits (as you can see in server/bin/osv/fields.py)::

    def __init__(self, string='unknown', required=False, readonly=False,
                 domain=None, context="", states=None, priority=0, change_default=False, size=None,
                 ondelete="set null", translate=False, select=False, **args) :

.. i18n: There are a common set of optional parameters that are available to most field
.. i18n: types:
..

There are a common set of optional parameters that are available to most field
types:

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

:change_default: 
	Whether or not the user can define default values on other fields depending 
	on the value of this field. Those default values need to be defined in
	the ir.values table.
:help: 
	A description of how the field should be used: longer and more descriptive
	than `string`. It will appear in a tooltip when the mouse hovers over the 
	field.
:ondelete: 
	How to handle deletions in a related record. Allowable values are: 
	'restrict', 'no action', 'cascade', 'set null', and 'set default'.
:priority: Not used?
:readonly: `True` if the user cannot edit this field, otherwise `False`.
:required:
	`True` if this field must have a value before the object can be saved, 
	otherwise `False`.
:size: The size of the field in the database: number characters or digits.
:states:
	Lets you override other parameters for specific states of this object. 
	Accepts a dictionary with the state names as keys and a list of name/value 
	tuples as the values. For example: `states={'posted':[('readonly',True)]}`
:string: 
	The field name as it should appear in a label or column header. Strings
	containing non-ASCII characters must use python unicode objects. 
	For example: `'tested': fields.boolean(u'Testé')` 
:translate:
	`True` if the *content* of this field should be translated, otherwise 
	`False`.

.. i18n: There are also some optional parameters that are specific to some field types:
..

There are also some optional parameters that are specific to some field types:

.. i18n: :context: 
.. i18n: 	Define a variable's value visible in the view's context or an on-change 
.. i18n: 	function. Used when searching child table of `one2many` relationship?
.. i18n: :domain: 
.. i18n:     Domain restriction on a relational field.
..

:context: 
	Define a variable's value visible in the view's context or an on-change 
	function. Used when searching child table of `one2many` relationship?
:domain: 
    Domain restriction on a relational field.

.. i18n:     Default value: []. 
..

    Default value: []. 

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

    Example: domain=[('field','=',value)])
:invisible: Hide the field's value in forms. For example, a password.
:on_change:
	Default value for the `on_change` attribute in the view. This will launch
	a function on the server when the field changes in the client. For example,
	`on_change="onchange_shop_id(shop_id)"`. 
:relation:
	Used when a field is an id reference to another table. This is the name of
	the table to look in. Most commonly used with related and function field
	types.
:select: 
	Default value for the `select` attribute in the view. 1 means basic search,
	and 2 means advanced search.

.. i18n: Type of Fields
.. i18n: --------------
..

Type of Fields
--------------

.. i18n: Basic Types
.. i18n: +++++++++++
..

Basic Types
+++++++++++

.. i18n: :boolean:
..

:boolean:

.. i18n: 	A boolean (true, false).
..

	A boolean (true, false).

.. i18n: 	Syntax::
.. i18n: 
.. i18n:                 fields.boolean('Field Name' [, Optional Parameters]),
..

	Syntax::

                fields.boolean('Field Name' [, Optional Parameters]),

.. i18n: :integer:
..

:integer:

.. i18n: 	An integer.
..

	An integer.

.. i18n: 	Syntax::
.. i18n: 
.. i18n:                 fields.integer('Field Name' [, Optional Parameters]),
..

	Syntax::

                fields.integer('Field Name' [, Optional Parameters]),

.. i18n: :float:
..

:float:

.. i18n:     A floating point number.
..

    A floating point number.

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

    Syntax::

                fields.float('Field Name' [, Optional Parameters]),

    .. note::

            The optional parameter digits defines the precision and scale of the
            number. The scale being the number of digits after the decimal point
            whereas the precision is the total number of significant digits in the
            number (before and after the decimal point). If the parameter digits is
            not present, the number will be a double precision floating point number.
            Warning: these floating-point numbers are inexact (not any value can be
            converted to its binary representation) and this can lead to rounding
            errors. You should always use the digits parameter for monetary amounts.

    Example::

        'rate': fields.float(
            'Relative Change rate',
            digits=(12,6) [,
            Optional Parameters]),

.. i18n: :char:
..

:char:

.. i18n:   A string of limited length. The required size parameter determines its size.
..

  A string of limited length. The required size parameter determines its size.

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

  Syntax::

  	fields.char(
  		'Field Name', 
  		size=n [, 
  		Optional Parameters]), # where ''n'' is an integer.

  Example::

        'city' : fields.char('City Name', size=30, required=True),

.. i18n: :text:
..

:text:

.. i18n:   A text field with no limit in length.
..

  A text field with no limit in length.

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

  A field which allows the user to make a selection between various predefined values.

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

  A one2one field expresses a one:to:one relation between two objects. It is
  deprecated. Use many2one instead.

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

  Associates this object to a parent object via this Field. For example
  Department an Employee belongs to would Many to one. i.e Many employees will
  belong to a Department

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

  Optional parameters:
  
    - ondelete: What should happen when the resource this field points to is deleted.
            + Predefined value: "cascade", "set null", "restrict", "no action", "set default"
            + Default value: "set null"
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

  Optional parameters:
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
                - other.object.name is the other object which belongs to the relation
                - relation object is the table that makes the link
                - actual.object.id and other.object.id are the fields' names used in the relation table

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

  Sometimes you need to refer to the relation of a relation. For example,
  supposing you have objects: City -> State -> Country, and you need to refer to
  the Country from a City, you can define a field as below in the City object::

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
  	- :guilabel:`type` is the type of that desired field.
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

A functional field is a field whose value is calculated by a function (rather
than being stored in the database).

.. i18n: **Parameters:** ::
.. i18n: 
.. i18n:     fnct, arg=None, fnct_inv=None, fnct_inv_arg=None, type="float",
.. i18n:         fnct_search=None, obj=None, method=False, store=False, multi=False
..

**Parameters:** ::

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

    * :guilabel:`fnct` is the function or method that will compute the field 
      value. It must have been declared before declaring the functional field.
    * :guilabel:`fnct_inv` is the function or method that will allow writing
      values in that field.
    * :guilabel:`type` is the field type name returned by the function. It can
      be any field type name except function.
    * :guilabel:`fnct_search` allows you to define the searching behaviour on
      that field.
    * :guilabel:`method` whether the field is computed by a method (of an
      object) or a global function
    * :guilabel:`store` If you want to store field in database or not. Default
      is False.
    * :guilabel:`multi` is a group name. All fields with the same `multi`
      parameter will be calculated in a single function call. 

.. i18n: fnct parameter
.. i18n: """"""""""""""
.. i18n: If *method* is True, the signature of the method must be::
.. i18n: 
.. i18n:     def fnct(self, cr, uid, ids, field_name, arg, context):
..

fnct parameter
""""""""""""""
If *method* is True, the signature of the method must be::

    def fnct(self, cr, uid, ids, field_name, arg, context):

.. i18n: otherwise (if it is a global function), its signature must be::
.. i18n: 
.. i18n:     def fnct(cr, table, ids, field_name, arg, context):
..

otherwise (if it is a global function), its signature must be::

    def fnct(cr, table, ids, field_name, arg, context):

.. i18n: Either way, it must return a dictionary of values of the form
.. i18n: **{id'_1_': value'_1_', id'_2_': value'_2_',...}.**
..

Either way, it must return a dictionary of values of the form
**{id'_1_': value'_1_', id'_2_': value'_2_',...}.**

.. i18n: The values of the returned dictionary must be of the type specified by the type 
.. i18n: argument in the field declaration.
..

The values of the returned dictionary must be of the type specified by the type 
argument in the field declaration.

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

If *multi* is set, then *field_name* is replaced by *field_names*: a list
of the field names that should be calculated. Each value in the returned 
dictionary is also a dictionary from field name to value. For example, if the
fields `'name'`, and `'age'` are both based on the `vital_statistics` function,
then the return value of `vital_statistics` might look like this when `ids` is
`[1, 2, 5]`::

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
If *method* is true, the signature of the method must be::

    def fnct(self, cr, uid, ids, field_name, field_value, arg, context):
    

.. i18n: otherwise (if it is a global function), it should be::
.. i18n: 
.. i18n:     def fnct(cr, table, ids, field_name, field_value, arg, context):
..

otherwise (if it is a global function), it should be::

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

The return value is a list containing 3-part tuples which are used in search function::

    return [('id','in',[1,3,5])]

.. i18n: *obj* is the same as *self*, and *name* receives the field name. *args* is a list
.. i18n: of 3-part tuples containing search criteria for this field, although the search
.. i18n: function may be called separately for each tuple.
..

*obj* is the same as *self*, and *name* receives the field name. *args* is a list
of 3-part tuples containing search criteria for this field, although the search
function may be called separately for each tuple.

.. i18n: Example
.. i18n: """""""
.. i18n: Suppose we create a contract object which is :
..

Example
"""""""
Suppose we create a contract object which is :

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

If we want to add a field that retrieves the function of an employee by looking its current contract, we use a functional field. The object hr_employee is inherited this way:

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

.. note:: three points

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

The id of the function is retrieved using a SQL query. Note that if the query 
returns no result, the value of sql_res['func_id'] will be None. We force the
False value in this case value because XML:RPC (communication between the server 
and the client) doesn't allow to transmit this value.

.. i18n: store Parameter
.. i18n: """""""""""""""
.. i18n: It will calculate the field and store the result in the table. The field will be
.. i18n: recalculated when certain fields are changed on other objects. It uses the
.. i18n: following syntax:
..

store Parameter
"""""""""""""""
It will calculate the field and store the result in the table. The field will be
recalculated when certain fields are changed on other objects. It uses the
following syntax:

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

It will call function function_name when any changes are written to fields in the
list ['field1','field2'] on object 'object_name'. The function should have the
following signature::

    def function_name(self, cr, uid, ids, context=None):

.. i18n: Where `ids` will be the ids of records in the other object's table that have
.. i18n: changed values in the watched fields. The function should return a list of ids
.. i18n: of records in its own table that should have the field recalculated. That list 
.. i18n: will be sent as a parameter for the main function of the field.
..

Where `ids` will be the ids of records in the other object's table that have
changed values in the watched fields. The function should return a list of ids
of records in its own table that should have the field recalculated. That list 
will be sent as a parameter for the main function of the field.

.. i18n: Here's an example from the membership module:
..

Here's an example from the membership module:

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

A property is a special field: fields.property.

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

Then you have to create the default value in a .XML file for this property:

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

To add properties in forms, just put the <properties/> tag in your form. This will automatically add all properties fields that are related to this object. The system will add properties depending on your rights. (some people will be able to change a specific property, others won't).

.. i18n: Properties are displayed by section, depending on the group_name attribute. (It is rendered in the client like a separator tag).
..

Properties are displayed by section, depending on the group_name attribute. (It is rendered in the client like a separator tag).

.. i18n: **How does this work ?**
..

**How does this work ?**

.. i18n: The fields.property class inherits from fields.function and overrides the read and write method. The type of this field is many2one, so in the form a property is represented like a many2one function.
..

The fields.property class inherits from fields.function and overrides the read and write method. The type of this field is many2one, so in the form a property is represented like a many2one function.

.. i18n: But the value of a property is stored in the ir.property class/table as a complete record. The stored value is a field of type reference (not many2one) because each property may point to a different object. If you edit properties values (from the administration menu), these are represented like a field of type reference.
..

But the value of a property is stored in the ir.property class/table as a complete record. The stored value is a field of type reference (not many2one) because each property may point to a different object. If you edit properties values (from the administration menu), these are represented like a field of type reference.

.. i18n: When you read a property, the program gives you the property attached to the instance of object you are reading. If this object has no value, the system will give you the default property.
..

When you read a property, the program gives you the property attached to the instance of object you are reading. If this object has no value, the system will give you the default property.

.. i18n: The definition of a property is stored in the ir.model.fields class like any other fields. In the definition of the property, you can add groups that are allowed to change to property.
..

The definition of a property is stored in the ir.model.fields class like any other fields. In the definition of the property, you can add groups that are allowed to change to property.

.. i18n: **Using properties or normal fields**
..

**Using properties or normal fields**

.. i18n: When you want to add a new feature, you will have to choose to implement it as a property or as normal field. Use a normal field when you inherit from an object and want to extend this object. Use a property when the new feature is not related to the object but to an external concept.
..

When you want to add a new feature, you will have to choose to implement it as a property or as normal field. Use a normal field when you inherit from an object and want to extend this object. Use a property when the new feature is not related to the object but to an external concept.

.. i18n: Here are a few tips to help you choose between a normal field or a property:
..

Here are a few tips to help you choose between a normal field or a property:

.. i18n: Normal fields extend the object, adding more features or data.
..

Normal fields extend the object, adding more features or data.

.. i18n: A property is a concept that is attached to an object and have special features:
..

A property is a concept that is attached to an object and have special features:

.. i18n: * Different value for the same property depending on the company
.. i18n: * Rights management per field
.. i18n: * It's a link between resources (many2one)
..

* Different value for the same property depending on the company
* Rights management per field
* It's a link between resources (many2one)

.. i18n: **Example 1: Account Receivable**
..

**Example 1: Account Receivable**

.. i18n: The default "Account Receivable" for a specific partner is implemented as a property because:
..

The default "Account Receivable" for a specific partner is implemented as a property because:

.. i18n:     * This is a concept related to the account chart and not to the partner, so it is an account property that is visible on a partner form. Rights have to be managed on this fields for accountants, these are not the same rights that are applied to partner objects. So you have specific rights just for this field of the partner form: only accountants may change the account receivable of a partner.
.. i18n: 
.. i18n:     * This is a multi-company field: the same partner may have different account receivable values depending on the company the user belongs to. In a multi-company system, there is one account chart per company. The account receivable of a partner depends on the company it placed the sale order.
.. i18n: 
.. i18n:     * The default account receivable is the same for all partners and is configured from the general property menu (in administration).
..

    * This is a concept related to the account chart and not to the partner, so it is an account property that is visible on a partner form. Rights have to be managed on this fields for accountants, these are not the same rights that are applied to partner objects. So you have specific rights just for this field of the partner form: only accountants may change the account receivable of a partner.

    * This is a multi-company field: the same partner may have different account receivable values depending on the company the user belongs to. In a multi-company system, there is one account chart per company. The account receivable of a partner depends on the company it placed the sale order.

    * The default account receivable is the same for all partners and is configured from the general property menu (in administration).

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

The product expiry module implements all delays related to products: removal date, product usetime, ... This module is very useful for food industries.

.. i18n: This module inherits from the product.product object and adds new fields to it:
..

This module inherits from the product.product object and adds new fields to it:

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

This module adds simple fields to the product.product object. We did not use properties because:

.. i18n:     * We extend a product, the life_time field is a concept related to a product, not to another object.
.. i18n:     * We do not need a right management per field, the different delays are managed by the same people that manage all products.
..

    * We extend a product, the life_time field is a concept related to a product, not to another object.
    * We do not need a right management per field, the different delays are managed by the same people that manage all products.

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

In OpenObject, the context holds very important data such as the language in
which a document must be written, whether function field needs updating or not,
etc.

.. i18n: When calling an ORM method, you will probably already have a context - for
.. i18n: example the framework will provide you with one as a parameter of almost 
.. i18n: every method.
.. i18n: If you do have a context, it is very important that you always pass it through
.. i18n: to every single method you call.
..

When calling an ORM method, you will probably already have a context - for
example the framework will provide you with one as a parameter of almost 
every method.
If you do have a context, it is very important that you always pass it through
to every single method you call.

.. i18n: This rule also applies to writing ORM methods. You should expect to receive a
.. i18n: context as parameter, and always pass it through to every other method you call.. 
..

This rule also applies to writing ORM methods. You should expect to receive a
context as parameter, and always pass it through to every other method you call.. 

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
