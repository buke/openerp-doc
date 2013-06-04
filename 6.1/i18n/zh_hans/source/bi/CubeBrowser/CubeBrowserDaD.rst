.. i18n: Creating your report with drag and drop
.. i18n: =======================================
..

拖放方式创建你的报表
=======================================

.. i18n: Cube Browser uses basic drag-and-drop operations to add data to a report.
.. i18n: Measures represent categories of stored values; Dimensions represent categories of OLAP information
..

Cube Browser 使用基本的拖放操作添加数据到一个报表.
Measures 代表储存类别的值; Dimensions 代表OLAP类别的信息

.. i18n: All UI controls update their contents automatically, and the resulting query is displayed on the OLAP Grid.
..

所有的UI控件自动更新其内容,查询结果显示在OLAP表格里.

.. i18n: Queries can be created by Dragging a member on the on the Droppable Area marked with the box for the drop zone.
..

在标记有可以拖拉区域的下拉框里，你可以通过拖动一个选项来新建一个查询。

.. i18n: Lets drop the All Product Category on the drop zone referred as grid afterward.
.. i18n: As soon as the member is dropped the resultant query is formed and can be viewed using the toolbar.
.. i18n: Query is then executed giving the first output on the grid. The first drop is always on the rows. 
..
让我们在表格后面可拖动区域中移动所有的产品种类，
一个类别被拖动后马上就会建立新的查询结果，就可以利用工具条来查……
查询结果生成之后马上就会用表格显示出来，第一个被拖动的总是出现在行中。

.. i18n: .. image::  images/d_browsr4.png
.. i18n:    :scale: 65
..

.. image::  images/d_browsr4.png
   :scale: 65

.. i18n: The second axis can be added by dropping a member on blue zone. The output can be seen immediately. Each user action changes and executes the query and then shows the result. The cross or delete button beside each item in grid deletes the elements from the query and the resultant grid. On top we can see if any filters are applied on the query or not.
..

 当拖动一个选项到蓝色区域时将会添加第二个主干，马上就会看到结果的变化。每个用户改变动作或者执行查询后马上就会显示出结果。在项目表格旁边都有方向与删除键，我们可以从查询汇总表格中删除一个因素。在最上面我们还可以看到是否应用到哪些过滤条件。


.. i18n: .. image::  images/d_browsr5.png
.. i18n:    :scale: 65
..

.. image::  images/d_browsr5.png
   :scale: 65

.. i18n: We can see the query by selecting the MDX button on the toolbar. This will open the pop up to show the mdx query for the current grid.
..

我们可以通过点选工具栏上的MDX按扭来查询，就会在当前表格中弹出显示MDX查询结果。

.. i18n: .. image::  images/data_browser11.png
.. i18n:    :scale: 65
..

.. image::  images/data_browser11.png
   :scale: 65
