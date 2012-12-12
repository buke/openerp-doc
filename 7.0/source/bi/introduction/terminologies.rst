
.. _terminologies-link:

Terminologies
=============

This page defines all terminologies. Objects in the OLAP cube use this convention. 

.. _schema-link:

.. topic:: Schema

   A schema is a collection of N dimensions. It's the meta description
   of cubes..

.. _hierarchy-link:

.. topic:: Hierarchy

   A schema is divided in hierarchy, which are divided in dimensions.
   The main use of hierarchy is to check that different axis can not
   use dimensions of the same hierarchy.

.. _dimension-link:

.. topic:: Dimension

   A dimension is an attribute, or set of attributes, by which you can
   divide measures into sub-categories. It's a tree structure that
   define the axis of the cube. They can be explicitly defined:
   partner_id.country_id.state_ids or recursive 'parent_id'.
   A dimension is divided in levels.

.. _level-link:

.. topic:: Level

   One level of sub-categories defined by dimensions.

.. _measure-link:

.. topic:: Measure

   Meta data of the quantity your are measuring. (value)
   A measure may be complex, ex: the tuple (quantity,uom)
   Attributes which are also objects:

	Agregator: an SQL function that define how we aggregate measures
	"sum", "count", "min", "max", "avg", and "distinct-count"
	FormatString
	DataType (the measure/value datatype)

.. _cube-link:

.. topic:: Cube

   A cube is a collection of N axis. A cube is an instance of a schema.
   A cube is mapped to a 'SQL' query through the use of his axis. (or several)

.. topic:: Member

   A member is a point within a dimension determined by a particular set of
   attribute values. (instances) A member is able to compute a part of the
   SQL query.

.. topic:: Axis

   An axis is composed by one or a set of members. In others terms, the axis is
   defined by the part of the query preceding the "on rows", "on columns",
   "on pages"... The MDX result is also a cube composed of axis.

.. topic:: Value

   A value is an instance of a measure. (one particular case of the cube).

