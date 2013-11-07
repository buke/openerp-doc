.. i18n: .. _terminologies-link:
.. i18n: 
.. i18n: Terminologies
.. i18n: =============
..

.. _terminologies-link:

术语
=============

.. i18n: This page defines all terminologies. Objects in the OLAP cube use this convention. 
..

本页对所有术语进行定义。 在OLAP多维数据集的对象使用本约定。

.. i18n: .. _schema-link:
.. i18n: 
.. i18n: .. topic:: Schema
.. i18n: 
.. i18n:    A schema is a collection of N dimensions. It's the meta description
.. i18n:    of cubes..
..

.. _schema-link:

.. topic:: Schema

   A schema is a collection of N dimensions. It's the meta description
   of cubes..

.. i18n: .. _hierarchy-link:
.. i18n: 
.. i18n: .. topic:: Hierarchy
.. i18n: 
.. i18n:    A schema is divided in hierarchy, which are divided in dimensions.
.. i18n:    The main use of hierarchy is to check that different axis can not
.. i18n:    use dimensions of the same hierarchy.
..

.. _hierarchy-link:

.. topic:: Hierarchy

   A schema is divided in hierarchy, which are divided in dimensions.
   The main use of hierarchy is to check that different axis can not
   use dimensions of the same hierarchy.

.. i18n: .. _dimension-link:
.. i18n: 
.. i18n: .. topic:: Dimension
.. i18n: 
.. i18n:    A dimension is an attribute, or set of attributes, by which you can
.. i18n:    divide measures into sub-categories. It's a tree structure that
.. i18n:    define the axis of the cube. They can be explicitly defined:
.. i18n:    partner_id.country_id.state_ids or recursive 'parent_id'.
.. i18n:    A dimension is divided in levels.
..

.. _dimension-link:

.. topic:: Dimension

   A dimension is an attribute, or set of attributes, by which you can
   divide measures into sub-categories. It's a tree structure that
   define the axis of the cube. They can be explicitly defined:
   partner_id.country_id.state_ids or recursive 'parent_id'.
   A dimension is divided in levels.

.. i18n: .. _level-link:
.. i18n: 
.. i18n: .. topic:: Level
.. i18n: 
.. i18n:    One level of sub-categories defined by dimensions.
..

.. _level-link:

.. topic:: Level

   One level of sub-categories defined by dimensions.

.. i18n: .. _measure-link:
.. i18n: 
.. i18n: .. topic:: Measure
.. i18n: 
.. i18n:    Meta data of the quantity your are measuring. (value)
.. i18n:    A measure may be complex, ex: the tuple (quantity,uom)
.. i18n:    Attributes which are also objects:
.. i18n: 
.. i18n: 	Agregator: an SQL function that define how we aggregate measures
.. i18n: 	"sum", "count", "min", "max", "avg", and "distinct-count"
.. i18n: 	FormatString
.. i18n: 	DataType (the measure/value datatype)
..

.. _measure-link:

.. topic:: Measure

   Meta data of the quantity your are measuring. (value)
   A measure may be complex, ex: the tuple (quantity,uom)
   Attributes which are also objects:

	Agregator: an SQL function that define how we aggregate measures
	"sum", "count", "min", "max", "avg", and "distinct-count"
	FormatString
	DataType (the measure/value datatype)

.. i18n: .. _cube-link:
.. i18n: 
.. i18n: .. topic:: Cube
.. i18n: 
.. i18n:    A cube is a collection of N axis. A cube is an instance of a schema.
.. i18n:    A cube is mapped to a 'SQL' query through the use of his axis. (or several)
..

.. _cube-link:

.. topic:: Cube

   A cube is a collection of N axis. A cube is an instance of a schema.
   A cube is mapped to a 'SQL' query through the use of his axis. (or several)

.. i18n: .. topic:: Member
.. i18n: 
.. i18n:    A member is a point within a dimension determined by a particular set of
.. i18n:    attribute values. (instances) A member is able to compute a part of the
.. i18n:    SQL query.
..

.. topic:: Member

   A member is a point within a dimension determined by a particular set of
   attribute values. (instances) A member is able to compute a part of the
   SQL query.

.. i18n: .. topic:: Axis
.. i18n: 
.. i18n:    An axis is composed by one or a set of members. In others terms, the axis is
.. i18n:    defined by the part of the query preceding the "on rows", "on columns",
.. i18n:    "on pages"... The MDX result is also a cube composed of axis.
..

.. topic:: Axis

   An axis is composed by one or a set of members. In others terms, the axis is
   defined by the part of the query preceding the "on rows", "on columns",
   "on pages"... The MDX result is also a cube composed of axis.

.. i18n: .. topic:: Value
.. i18n: 
.. i18n:    A value is an instance of a measure. (one particular case of the cube).
..

.. topic:: Value

   A value is an instance of a measure. (one particular case of the cube).
