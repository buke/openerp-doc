Creating your report with drag and drop
=======================================

Cube Browser uses basic drag-and-drop operations to add data to a report.
Measures represent categories of stored values; Dimensions represent categories of OLAP information

All UI controls update their contents automatically, and the resulting query is displayed on the OLAP Grid.

Queries can be created by Dragging a member on the on the Droppable Area marked with the box for the drop zone.

Lets drop the All Product Category on the drop zone referred as grid afterward.
As soon as the member is dropped the resultant query is formed and can be viewed using the toolbar.
Query is then executed giving the first output on the grid. The first drop is always on the rows. 

.. image::  images/d_browsr4.png
   :scale: 65

The second axis can be added by dropping a member on blue zone. The output can be seen immediately. Each user action changes and executes the query and then shows the result. The cross or delete button beside each item in grid deletes the elements from the query and the resultant grid. On top we can see if any filters are applied on the query or not.

.. image::  images/d_browsr5.png
   :scale: 65


We can see the query by selecting the MDX button on the toolbar. This will open the pop up to show the mdx query for the current grid.

.. image::  images/data_browser11.png
   :scale: 65
