.. i18n: Views and Events
.. i18n: ================
..

视图和事件
================

.. i18n: Introduction to Views
.. i18n: ---------------------
..

介绍视图
---------------------

.. i18n: As all program data is stored in objects, as explained in the Objects section, how are these objects exposed to the user ? We will try to answer this question in this section.
..

因为程序中所有数据存储在对象中，这个在对象的部分已经解释过了，这些对象如何显示给用户的呢？我们将在这个部分解释这个问题。

.. i18n: First of all, let's note that every resource type uses its own interface. For example, the screen to modify a partner's data is not the same as the one to modify an invoice.
..

首先注意每个资源类型有自己的界面。例如，修改一个合作伙伴数据的显示不同于修改invoice。

.. i18n: Then, you should know that the OpenERP user interface is dynamic, which means it is not described "statically" by some code, but is dynamically built from XML descriptions of the client screens.
..

然后，你应该知道Openerp用户界面是动态变化的，这意味着它不是有“静态”代码来描述，而是由XML动态描述用户界面。

.. i18n: From now on, we will call these screen descriptions views.
..

从现在起，我们称这些为screen descriptions views。

.. i18n: A notable characteristic of these views is that they can be edited at any time (even during program execution). After modifying a displayed view you simply need to close the tab corresponding to that 'view' and re-open it for the changes to appear. 
..

这些视图的显著特征是可以在任何时刻被修改（即使是在程序执行时刻）。如果对一个已经显示的视图进行修改后，你只需要关闭这个视图的标签，并且再打开，修改后的视图就会显示。

.. i18n: Views principles
.. i18n: ++++++++++++++++
..

视图原理
++++++++++++++++

.. i18n: Views describe how each object (type of resource) is displayed. More precisely, for each object, we can define one (or several) view(s) to describe which fields should be drawn and how.
..

视图描述了每个对象是如何显示的。更准确的说，对每个对象，我们可以定义一个或几个视图来描述哪个字段要显示和如何显示。

.. i18n: There are two types of views:
..

视图有两种:

.. i18n:    #. form views
.. i18n:    #. tree views 
..

   #. form views
   #. tree views 

.. i18n: .. note:: Since OpenERP 4.1, form views can also contain graphs. 
..

.. note:: Since OpenERP 4.1, form views can also contain graphs. 

.. i18n: Form views
.. i18n: ----------
..

Form 视图
----------

.. i18n: The field disposition in a form view always follows the same principle. Fields are distributed on the screen following the rules below:
..

在表单视图中，字段配置一致遵守相同的准则。显示的字段遵守以下的准则：

.. i18n:     * By default, each field is preceded by a label, with its name.
.. i18n:     * Fields are placed on the screen from left to right, and from top to bottom, according to the order in which they are declared in the view.
.. i18n:     * Every screen is divided into 4 columns, each column being able to contain either a label, or an "edition" field. As every edition field is preceded (by default) by a label with its name, there will be two fields (and their respective labels) on each line of the screen. The green and red zones on the screen-shot below illustrate those 4 columns. They designate respectively the labels and their corresponding fields. 
..

    * 默认情况下，每个字段由label开始，以字段名称代表该字段。
    * 字段在屏幕上按照从左到右，从上到下的顺序显示，是依照他们在视图中的显示顺序。
    * 每个屏幕分成4列，每一列要么是一个label，要么是“edition”字段。每个edition字段由label开始（默认情况下），以字段名称代表该字段，在屏幕的每一行将有两个字段。下面的截图中，绿色和红色的区域正好举例说明了这4列，他们分别代表着labels和他们相关的字段。

.. i18n: .. figure::  images/sale_order.png
.. i18n:    :scale: 50
.. i18n:    :align: center
..

.. figure::  images/sale_order.png
   :scale: 50
   :align: center

.. i18n: Views also support more advanced placement options:
..

视图支持更多的高级选项：

.. i18n:     * A view field can use several columns. For example, on the screen-shot below, the zone in the blue frame is, in fact, the only field of a "one to many". We will come back later on this note, but let's note that it uses the whole width of the screen and not only one column. 
..

    * 一个视图字段可以有多列。例如，下面的截图中，蓝框的区域事实上是一个“one to many”的字段。我们注意到该字段是整个屏幕的宽度，而不是一列。

.. i18n:       .. figure::  images/sale_order_sale_order_lines.png
.. i18n:         :scale: 50
.. i18n:         :align: center
.. i18n: 
.. i18n:     * We can also make the opposite operation: take a columns group and divide it in as many columns as desired. The surrounded green zones of the screen above are good examples. Precisely, the green framework up and on the right side takes the place of two columns, but contains 4 columns. 
..

      .. figure::  images/sale_order_sale_order_lines.png
        :scale: 50
        :align: center

    * 我们同样可以做相反的操作：将一列分成任意的多列。上图中的绿框区域正好就说明这个情况。更准确的说，绿框看着是两列，其实包括着4列。

.. i18n: As we can see below in the purple zone of the screen, there is also a way to distribute the fields of an object on different tabs.
..

下面截图中蓝色的区域，是将对象的字段分成不同的标签。

.. i18n: .. figure::  images/sale_order_notebook.png
.. i18n:    :scale: 50
.. i18n:    :align: center
..

.. figure::  images/sale_order_notebook.png
   :scale: 50
   :align: center

.. i18n: Tree views
.. i18n: -----------
..

Tree 视图
-----------

.. i18n: These views are used when we work in list mode (in order to visualise several resources at once) and in the search screen. These views are simpler than the form views and thus have less options.
..

当我们工作在一个list样式下（想要同时看到很多资源）和查询界面时，这些视图就会用到。这些视图比form views简单，有较少的选项。

.. i18n: .. figure::  images/tree_view.png
.. i18n:    :scale: 50
.. i18n:    :align: center
..

.. figure::  images/tree_view.png
   :scale: 50
   :align: center

.. i18n: Graph views
.. i18n: --------------
..

Graph 视图
--------------

.. i18n: A graph is a new mode of view for all views of type form. If, for example, a sale order line must be visible as list or as graph, define it like this in the action that opens this sale order line. Do not set the view mode as "tree,form,graph" or "form,graph" - it must be "graph,tree" to show the graph first or "tree,graph" to show the list first. (This view mode is extra to your "form,tree" view and should have a separate menu item):
..

graph对所有的表单视图来说是一种新形式的视图。例如，如果一个销售订单线作为list或graph必须是可见的，将它定义为打开这个销售订单线的动作。不要将视图形式设置为“tree，form，graph”或“form，graph”，必须设置为“graph，tree”来首先显示graph或者设置为“tree，graph”来首先显示list。（这个视图形式是你的“form，tree”视图的额外形式并且应该有个分开的菜单选项）。

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n: 	 <field name="view_type">form</field>
.. i18n: 	 <field name="view_mode">tree,graph</field>
..

.. code-block:: xml

	 <field name="view_type">form</field>
	 <field name="view_mode">tree,graph</field>

.. i18n: view_type::
.. i18n: 
.. i18n:         tree = (tree with shortcuts at the left), form = (switchable view form/list) 
..

view_type::

        tree = (tree with shortcuts at the left), form = (switchable view form/list) 

.. i18n: view_mode::
.. i18n: 
.. i18n:         tree,graph : sequences of the views when switching 
..

view_mode::

        tree,graph : sequences of the views when switching 

.. i18n: Then, the user will be able to switch from one view to the other. Unlike forms and trees, OpenERP is not able to automatically create a view on demand for the graph type. So, you must define a view for this graph:
..

接下来，用户可以从一个视图转换到另一个视图。不像表单和列表视图一样，OpenERP不能自动按需创建graph视图，所以你必须自己定义graph视图：

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n: 	<record model="ir.ui.view" id="view_order_line_graph">
.. i18n: 	   <field name="name">sale.order.line.graph</field>
.. i18n: 	   <field name="model">sale.order.line</field>
.. i18n: 	   <field name="type">graph</field>
.. i18n: 	   <field name="arch" type="xml">
.. i18n: 		 <graph string="Sales Order Lines">
.. i18n: 		      <field name="product_id" group="True"/>
.. i18n: 		      <field name="price_unit" operator="*"/>
.. i18n: 		</graph>
.. i18n: 	    </field>
.. i18n: 	</record>
..

.. code-block:: xml

	<record model="ir.ui.view" id="view_order_line_graph">
	   <field name="name">sale.order.line.graph</field>
	   <field name="model">sale.order.line</field>
	   <field name="type">graph</field>
	   <field name="arch" type="xml">
		 <graph string="Sales Order Lines">
		      <field name="product_id" group="True"/>
		      <field name="price_unit" operator="*"/>
		</graph>
	    </field>
	</record>

.. i18n: The graph view
..

graph 视图

.. i18n: A view of type graph is just a list of fields for the graph.
..

graph类型的视图只是graph的字段列表。

.. i18n: Graph tag
.. i18n: ++++++++++
..

Graph tag
++++++++++

.. i18n: The default type of the graph is a pie chart - to change it to a barchart change **<graph string="Sales Order Lines">** to **<graph string="Sales Order Lines" type="bar">** You also may change the orientation.
..

graph的默认类型是圆形分格统计图表（pie chart），要将它转换成条形图（barchart），就需要将<graph string=”Sales Order Lines”> 转换成 <graph string=”Sales Order Lines” type=”bar”>，你也可以改变方向。

.. i18n: :Example : 
..

:例如 : 

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n: 	<graph string="Sales Order Lines" orientation="horizontal" type="bar">
..

.. code-block:: xml

	<graph string="Sales Order Lines" orientation="horizontal" type="bar">

.. i18n: Field tag
.. i18n: +++++++++
..

Field tag
+++++++++

.. i18n: The first field is the X axis. The second one is the Y axis and the optional third one is the Z axis for 3 dimensional graphs. You can apply a few attributes to each field/axis:
..

第一个字段是x轴，第二个是y轴，第三个是z轴，这个是可选择的三维图字段。你可以运用一些属性到每个field/axis。

.. i18n:     * **group**: if set to true, the client will group all item of the same value for this field. For every other field, it will apply an operator
.. i18n:     * **operator**: the operator to apply if another field is grouped. By default it is '+'. Allowed values are:
..

    * **group**: 如果设置为true，客户端会组合这个字段相同值的所有项。对于相互的字段，它会应用operator。
    * **operator**: operator的应用是由另一个字段决定的，默认是“+”，允许的值是：

.. i18n:           + +: addition
.. i18n:           + \*: multiply
.. i18n:           + \**: exponent
.. i18n:           + min: minimum of the list
.. i18n:           + max: maximum of the list 
..

          + +: addition
          + \*: multiply
          + \**: exponent
          + min: minimum of the list
          + max: maximum of the list 

.. i18n: :Defining real statistics on objects:
..

:Defining real statistics on objects:

.. i18n: The easiest method to compute real statistics on objects is:
..

定义真正的对象数据统计：

.. i18n:    1. Define a statistic object which is a postgresql view
.. i18n:    2. Create a tree view and a graph view on this object 
..

   1. 定义一个统计对象，它是PostgreSQL视图
   2. 在这个对象上创建一个tree view和graph view

.. i18n: You can get an example in all modules of the form: report\_.... Example: report_crm. 
..

You can get an example in all modules of the form: report\_.... Example: report_crm. 

.. i18n: Search views
.. i18n: --------------
..

Search views
--------------

.. i18n: Search views are a new feature of OpenERP supported as of version 6.0.
.. i18n: It creates a customized search panel, and is declared quite similarly to a form view,
.. i18n: except that the view type and root element change to ``search`` instead of ``form``.
..

search views是Openerp 6.0版本支持的一个新特性。它创建一个自定义的查找面板，它的显示和表单视图非常相似，除了将视图的类型和根元素由form改为search。

.. i18n: .. image:: images/search.png
.. i18n:    :scale: 50
.. i18n:    :align: center
..

.. image:: images/search.png
   :scale: 50
   :align: center

.. i18n: Following is the list of new elements and features supported in search views.
..

下面是search视图中要用到的新的元素和特性列表。

.. i18n: Group tag
.. i18n: +++++++++
..

Group tag
+++++++++

.. i18n: Unlike form group elements, search view groups support unlimited number of widgets (fields or filters)
.. i18n: in a row (no automatic line wrapping), and only use the following attributes:
..

不像表单元素组，search view groups支持一行中不限数量的widget（fields或filters），并且只是使用下面的属性：

.. i18n:     + ``expand``: turns on the expander icon on the group (1 for expanded by default, 0 for collapsed)
.. i18n:     + ``string``: label for the group
..

    + ``expand``: turns on the expander icon on the group (1 for expanded by default, 0 for collapsed)
    + ``string``: label for the group

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <group expand="1" string="Group By...">
.. i18n:        <filter string="Users" icon="terp-project" domain="[]" context="{'group_by':'user_id'}"/>
.. i18n:        <filter string="Project" icon="terp-project" domain="[]" context="{'group_by':'project_id'}"/>
.. i18n:        <separator orientation="vertical"/>
.. i18n:        <filter string="Deadline" icon="terp-project" domain="[]" context="{'group_by':'date_deadline'}"/>
.. i18n:     </group>
..

.. code-block:: xml

    <group expand="1" string="Group By...">
       <filter string="Users" icon="terp-project" domain="[]" context="{'group_by':'user_id'}"/>
       <filter string="Project" icon="terp-project" domain="[]" context="{'group_by':'project_id'}"/>
       <separator orientation="vertical"/>
       <filter string="Deadline" icon="terp-project" domain="[]" context="{'group_by':'date_deadline'}"/>
    </group>

.. i18n: In the screenshot above the green area is an expandable group.
..

以上的截图是个扩展group。

.. i18n: Filter tag
.. i18n: +++++++++++
.. i18n: Filters are displayed as a toggle button on search panel 
.. i18n: Filter elements can add new values in the current domain or context of the search view.
.. i18n: Filters can be added as a child element of field too, to indicate that they apply specifically
.. i18n: to that field (in this case the button's icon will smaller)
..

Filter tag
+++++++++++
Filters在查找面板作为一个触发按钮方式显示，可以添加新的过滤元素在当前域或是查询视图的上下文。Filters可以作为一个字段子元素添加进去，来表示他们专门用于该字段（这种情况下button按钮会变小些）。

.. i18n: In the picture above the red area contains filters at the top of the form while
.. i18n: the blue area highlights a field and its child filter.
..

在图中表单上部红色区域包含着filters，而蓝色区域是一个字段，并且是child filter。

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <filter string="Current" domain="[('state','in',('open','draft'))]" help="Draft, Open and Pending Tasks" icon="terp-project"/>
.. i18n:     <field name="project_id" select="1" widget="selection">
.. i18n:         <filter domain="[('project_id.user_id','=',uid)]" help="My Projects" icon="terp-project"/>
.. i18n:     </field>
..

.. code-block:: xml

    <filter string="Current" domain="[('state','in',('open','draft'))]" help="Draft, Open and Pending Tasks" icon="terp-project"/>
    <field name="project_id" select="1" widget="selection">
        <filter domain="[('project_id.user_id','=',uid)]" help="My Projects" icon="terp-project"/>
    </field>

.. i18n: Group By
.. i18n: ++++++++
..

Group By
++++++++

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <filter string="Project" icon="terp-project" domain="[]" context="{'group_by':'project_id'}"/>
..

.. code-block:: xml

    <filter string="Project" icon="terp-project" domain="[]" context="{'group_by':'project_id'}"/>

.. i18n: Above filters groups records sharing the same ``project_id`` value. Groups are loaded
.. i18n: lazily, so the inner records are only loaded when the group is expanded.
.. i18n: The group header lines contain the common values for all records in that group, and all numeric
.. i18n: fields currently displayed in the view are replaced by the sum of the values in that group.
..

以上的filters groups records都用相同的project_id值。groups懒加载，所以，inner records只在group扩展时加载。group header lines包含这个group中所有记录的共同值，并且所有数字型的字段一般先是在视图中，来代替值的和。

.. i18n: It is also possible to group on multiple values by specifying a list of fields instead of a single string.
.. i18n: In this case nested groups will be displayed::
.. i18n: 
.. i18n:     <filter string="Project" icon="terp-project" domain="[]" context="{'group_by': ['project_id', 'user_id'] }"/>
..

将指定的a list of fields的很多值分组来代替a single string是可能的。这种情况下，嵌套分组就会显示出来::

    <filter string="Project" icon="terp-project" domain="[]" context="{'group_by': ['project_id', 'user_id'] }"/>

.. i18n: Fields
.. i18n: ++++++
..

Fields
++++++

.. i18n: Field elements in search views are used to get user-provided values
.. i18n: for searches. As a result, as for group elements, they are quite
.. i18n: different than form view's fields:
..

search view里面的字段元素用来为搜索得到user-provided值。其结果是，对于组元素（group elements），它们和表单视图的字段大不相同：

.. i18n: * a search field can contain filters, which generally indicate that
.. i18n:   both field and filter manage the same field and are related.
..

* 一个搜索字段可以包含过滤（filters），通常表明字段和过滤管理相同的字段并且二者相关。

.. i18n:   Those inner filters are rendered as smaller buttons, right next to
.. i18n:   the field, and *must not* have a ``string`` attribute.
..

  那些内部的过滤器渲染为小buttons，紧挨着字段，肯定没有string属性。

.. i18n: * a search field really builds a domain composed of ``[(field_name,
.. i18n:   operator, field_value)]``. This domain can be overridden in two
.. i18n:   ways:
.. i18n: 
.. i18n:   * ``@operator`` replaces the default operator for the field (which
.. i18n:     depends on its type)
.. i18n: 
.. i18n:   * ``@filter_domain`` lets you provide a fully custom domain, which
.. i18n:     will replace the default domain creation
.. i18n: 
.. i18n: * a search field does not create a context by default, but you can
.. i18n:   provide an ``@context`` which will be evaluated and merged into the
.. i18n:   wider context (as with a ``filter`` element).
..

  * 一个search字段确实构造了一个由[(field_name, operator, field_value)]构成的domain。这个domain在两种情况下无效：

  * ``@operator`` replaces the default operator for the field (which
    depends on its type)

  * ``@filter_domain`` lets you provide a fully custom domain, which
    will replace the default domain creation

* 一个search字段不能默认创建上下文，但是你可以提供一个context，来评估和合并进wider context。

.. i18n: To get the value of the field in your ``@context`` or
.. i18n: ``@filter_domain``, you can use the variable ``self``:
..

为了在你的context或filter_domain中获得字段值，你可以使用可变的self：

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <field name="location_id" string="Location"
.. i18n:            filter_domain="['|',('location_id','ilike',self),('location_dest_id','ilike',self)]"/>
..

.. code-block:: xml

    <field name="location_id" string="Location"
           filter_domain="['|',('location_id','ilike',self),('location_dest_id','ilike',self)]"/>

.. i18n: or
..

or

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <field name="journal_id" widget="selection"
.. i18n:            context="{'journal_id':self, 'visible_id':self, 'normal_view':False}"/>
..

.. code-block:: xml

    <field name="journal_id" widget="selection"
           context="{'journal_id':self, 'visible_id':self, 'normal_view':False}"/>

.. i18n: Range fields (date, datetime, time)
.. i18n: """""""""""""""""""""""""""""""""""
..

Range fields (date, datetime, time)
"""""""""""""""""""""""""""""""""""

.. i18n: The range fields are composed of two input widgets (from and to)
.. i18n: instead of just one.
..

range字段由两个input widgets组成，而不是之前的一个。

.. i18n: This leads to peculiarities (compared to non-range search fields):
..

这导致了它的特殊性（相比于non-range search fields来说）：

.. i18n: * It is not possible to override the operator of a range field via
.. i18n:   ``@operator``, as the domain is built of two sections and each
.. i18n:   section uses a different operator.
.. i18n: 
.. i18n: * Instead of being a simple value (integer, string, float) ``self``
.. i18n:   for use in ``@filter_domain`` and ``@context`` is a ``dict``.
..

* 由于domain由两个section构成，每个section使用不同的operator，但通过@operator重写range field是不可能的。

* Instead of being a simple value (integer, string, float) ``self``
  for use in ``@filter_domain`` and ``@context`` is a ``dict``.

.. i18n:   Because each input widget of a range field can be empty (and the
.. i18n:   field itself will still be valid), care must be taken when using
.. i18n:   ``self``: it has two string keys ``"from"`` and ``"to"``, but any of
.. i18n:   these keys can be either missing entirely or set to the value
.. i18n:   ``False``.
..

  因为range field的每个input widget可以为空（并且字段本身始终有效），必须谨慎使用self：它有两个string keys“from”和“to”，这些keys任意一个可以不使用或设置其值为False。

.. i18n: Actions for Search view
.. i18n: +++++++++++++++++++++++
..

Actions for Search view
+++++++++++++++++++++++

.. i18n: After declaring a search view, it will be used automatically for all tree views on the same model.
.. i18n: If several search views exist for a single model, the one with the highest priority (lowest sequence) will
.. i18n: be used. Another option is to explicitly select the search view you want to use, by setting the
.. i18n: ``search_view_id`` field of the action.
..

在声明一个search view后，它会被自动用在相同model的所有tree view中。如果一个model有几个search view，那它会使用拥有最高优先级的那个。另一个选择就是通过设置action中的search_view_id字段来明确选择想要使用的search view。

.. i18n: In addition to being able to pass default form values in the context of the action, OpenERP 6.0 now
.. i18n: supports passing initial values for search views too, via the context. The context keys need to match the
.. i18n: ``search_default_XXX`` format. ``XXX`` may refer to the ``name`` of a ``<field>`` or ``<filter>``
.. i18n: in the search view (as the ``name`` attribute is not required on filters, this only works for filters that have
.. i18n: an explicit ``name`` set). The value should be either the initial value for search fields, or
.. i18n: simply a boolean value for filters, to toggle them 
..

除了能够传递在action上下文中的默认表单值外，OpenERP 6.0现在支持通过上下文来传递search views的初始值。这个上下文keys需要匹配search_default_XXX格式。在search view中XXX是指<field>或<filter>的名字（其实对于filters，name属性并不是必须的，当它必须要有个明确的name值时才起作用）。这个值要么是search fields的初始值，要么是filter的布尔值，现在来切换它们：

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <record id="action_view_task" model="ir.actions.act_window">
.. i18n:         <field name="name">Tasks</field>
.. i18n:         <field name="res_model">project.task</field>
.. i18n:         <field name="view_type">form</field>
.. i18n:         <field name="view_mode">tree,form,calendar,gantt,graph</field>
.. i18n:         <field eval="False" name="filter"/>
.. i18n:         <field name="view_id" ref="view_task_tree2"/>
.. i18n:         <field name="context">{"search_default_current":1,"search_default_user_id":uid}</field>
.. i18n:         <field name="search_view_id" ref="view_task_search_form"/>
.. i18n:     </record>
..

.. code-block:: xml

    <record id="action_view_task" model="ir.actions.act_window">
        <field name="name">Tasks</field>
        <field name="res_model">project.task</field>
        <field name="view_type">form</field>
        <field name="view_mode">tree,form,calendar,gantt,graph</field>
        <field eval="False" name="filter"/>
        <field name="view_id" ref="view_task_tree2"/>
        <field name="context">{"search_default_current":1,"search_default_user_id":uid}</field>
        <field name="search_view_id" ref="view_task_search_form"/>
    </record>

.. i18n: Custom Filters
.. i18n: ++++++++++++++
..

Custom Filters
++++++++++++++

.. i18n: As of v6.0, all search views feature custom search filters, as shown below.
.. i18n: Users can define their own custom filters using any of the fields available on the current model,
.. i18n: combining them with AND/OR operators. It is also possible to save any search context (the combination
.. i18n: of all currently applied domain and context values) as a personal filter, which can be recalled
.. i18n: at any time. Filters can also be turned into Shortcuts directly available in the User's homepage.
..

对于V6.0，search view都可以进行自定义search filters，向下面显示的那样。用户可以使用当前模块的任意字段来定义自己的filters，并且用AND/OR operator来合并他们。将任何的search context作为个人过滤器都是可以的，还可以在任何时候重新调用。过滤器可以在用户主页直接转换成快捷键。

.. i18n: .. image:: images/filter.png
.. i18n:    :scale: 50
.. i18n:    :align: center
..

.. image:: images/filter.png
   :scale: 50
   :align: center

.. i18n: In above screenshot we filter Partner where Salesman = Demo user and Country = Belgium,
.. i18n: We can save this search criteria as a Shortcut or save as Filter.
..

在以上的截图中，我们过滤Partner用Salesman = Demo user 和Country = Belgium，我们将这个搜索标准作为快捷键或是保存为过滤器。

.. i18n: Filters are user specific and can be modified via the Manage Filters option in the filters drop-down.
..

过滤器是用户特定的，可以通过在filters 下拉菜单中管理过滤器选项来进行修改。

.. i18n: Calendar Views
.. i18n: --------------
..

Calendar Views
--------------

.. i18n: Calendar view provides timeline/schedule view for the data.
..

Calendar 视图为数据提供时间线（timeline）/日程表（schedule）视图。

.. i18n: View Specification
.. i18n: ++++++++++++++++++
..

View Specification
++++++++++++++++++

.. i18n: Here is an example view:
..

这有一个视图例子：

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <calendar color="user_id" date_delay="planned_hours" date_start="date_start" string="Tasks">
.. i18n:         <field name="name"/>
.. i18n:         <field name="project_id"/>
.. i18n:     </calendar>
..

.. code-block:: xml

    <calendar color="user_id" date_delay="planned_hours" date_start="date_start" string="Tasks">
        <field name="name"/>
        <field name="project_id"/>
    </calendar>

.. i18n: Here is the list of supported attributes for ``calendar`` tag:
..

下面是该视图标签的属性:

.. i18n:     ``string``
.. i18n:         The title string for the view.
..

    ``string``
        该视图的标题

.. i18n:     ``date_start``
.. i18n:         A ``datetime`` field to specify the starting date for the calendar item. This 
.. i18n:         attribute is required.
.. i18n:         
.. i18n:     ``date_stop``
.. i18n:         A ``datetime`` field to specify the end date. Ignored if ``date_delay`` 
.. i18n:         attribute is specified.
.. i18n:         
.. i18n:     ``date_delay``
.. i18n:         A ``numeric`` field to specify time in hours for a record. This attribute
.. i18n:         will get preference over ``date_stop`` and ``date_stop`` will be ignored.
.. i18n:         
.. i18n:     ``day_length``
.. i18n:         An ``integer`` value to specify working day length. Default is ``8`` hours.
.. i18n:         
.. i18n:     ``color``
.. i18n:         A field, generally ``many2one``, to colourise calendar/gantt items.
.. i18n:         
.. i18n:     ``mode``
.. i18n:         A string value to set default view/zoom mode. For ``calendar`` view, this can be
.. i18n:         one of following (default is ``month``):
.. i18n:         
.. i18n:         * ``day``
.. i18n:         * ``week``
.. i18n:         * ``month``
.. i18n:    
.. i18n: Screenshots
.. i18n: +++++++++++
..

date_start  ：表示开始时间的属性，该字段是必须的。
date_stop  ：表示结束时间的属性，如果指定了date_delay属性就可以忽视该属性。
date_delay  ：A numeric field to specify time in hours for a record. This attribute will get preference over date_stop and date_stop will be ignored.
day_length  ：显示工作时间长度的数字值，默认为8小时
color  ：A field, generally many2one, to colorize calendar/gantt items.        
mode  ：A string value to set default view/zoom mode. For calendar view, this can be one of following (default is month):
        
        * ``day``
        * ``week``
        * ``month``
   
Screenshots
+++++++++++

.. i18n: Month Calendar:
..

Month Calendar:

.. i18n: .. figure::  images/calendar_month.png
.. i18n:     :scale: 50%
.. i18n:     :align: center
..

.. figure::  images/calendar_month.png
    :scale: 50%
    :align: center

.. i18n: Week Calendar:
.. i18n:     
.. i18n: .. figure::  images/calendar_week.png
.. i18n:     :scale: 50%
.. i18n:     :align: center
..

Week Calendar:
    
.. figure::  images/calendar_week.png
    :scale: 50%
    :align: center

.. i18n: Gantt Views
.. i18n: -----------
..

Gantt Views
-----------

.. i18n: Gantt view provides timeline view for the data. Generally, it can be used to display
.. i18n: project tasks and resource allocation.
..

Gantt view为数据提供时间线视图，总体来说，它用于显示项目任务和资源分配。

.. i18n: A Gantt chart is a graphical display of all the tasks that a project is composed of.
.. i18n: Each bar on the chart is a graphical representation of the length of time the task is
.. i18n: planned to take.
..

甘特图是这个项目所有任务的图形显示。图的每一条显示该任务花费时间的长度。

.. i18n: A resource allocation summary bar is shown on top of all the grouped tasks,
.. i18n: representing how effectively the resources are allocated among the tasks.
..

资源分配总条在图中所有任务的上面显示，代表着任务中资源的有效利用情况。

.. i18n: Color coding of the summary bar is as follows:
..

颜色使用情况是：

.. i18n:     * `Gray` shows that the resource is not allocated to any task at that time    	
.. i18n:     * `Blue` shows that the resource is fully allocated at that time.
.. i18n:     * `Red` shows that the resource is overallocated
..

    * `Gray` 显示是指这个时候资源没有分配给任何任务。
    * `Blue` 显示是指这个时候资源完全分配了。
    * `Red` 显示是指这个时候资源overallocated。

.. i18n: View Specification
.. i18n: ++++++++++++++++++
..

View Specification
++++++++++++++++++

.. i18n: Here is an example view:
..

Here is an example view:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <gantt color="user_id" date_delay="planned_hours" date_start="date_start" string="Tasks">
.. i18n:         <level object="project.project" link="project_id" domain="[]">
.. i18n:             <field name="name"/>
.. i18n:         </level>
.. i18n:     </gantt>
..

.. code-block:: xml

    <gantt color="user_id" date_delay="planned_hours" date_start="date_start" string="Tasks">
        <level object="project.project" link="project_id" domain="[]">
            <field name="name"/>
        </level>
    </gantt>

.. i18n: The ``attributes`` accepted by the ``gantt`` tag are similar to ``calendar`` view tag. The
.. i18n: ``level`` tag is used to group the records by some ``many2one`` field. Currently, only
.. i18n: one level is supported.
..

甘特图标签的属性和calendar图标签的属性类似。level标签用于将一些many2one字段的记录分组。目前仅支持one level。

.. i18n: Here is the list of supported attributes for ``gantt`` tag:
..

下面是gantt标签的属性：

.. i18n:     ``string``
.. i18n:         The title string for the view.
..

    ``string``
        The title string for the view.

.. i18n:     ``date_start``
.. i18n:         A ``datetime`` field to specify the starting date for the gantt item. This 
.. i18n:         attribute is required.
.. i18n:         
.. i18n:     ``date_stop``
.. i18n:         A ``datetime`` field to specify the end date. Ignored if ``date_delay`` 
.. i18n:         attribute is specified.
.. i18n:         
.. i18n:     ``date_delay``
.. i18n:         A ``numeric`` field to specify time in hours for a record. This attribute
.. i18n:         will get preference over ``date_stop`` and ``date_stop`` will be ignored.
.. i18n:         
.. i18n:     ``day_length``
.. i18n:         An ``integer`` value to specify working day length. Default is ``8`` hours.
.. i18n:         
.. i18n:     ``color``
.. i18n:         A field, generally ``many2one``, to colorize calendar/gantt items.
.. i18n:         
.. i18n:     ``mode``
.. i18n:         A string value to set default view/zoom mode. For ``gantt`` view, this can be
.. i18n:         one of following (default is ``month``):
.. i18n:         
.. i18n:         * ``day``
.. i18n:         * ``3days``
.. i18n:         * ``week``
.. i18n:         * ``3weeks``
.. i18n:         * ``month``
.. i18n:         * ``3months``
.. i18n:         * ``year``
.. i18n:         * ``3years``
.. i18n:         * ``5years``
..

    ``date_start``
        A ``datetime`` field to specify the starting date for the gantt item. This 
        attribute is required.
        
    ``date_stop``
        A ``datetime`` field to specify the end date. Ignored if ``date_delay`` 
        attribute is specified.
        
    ``date_delay``
        A ``numeric`` field to specify time in hours for a record. This attribute
        will get preference over ``date_stop`` and ``date_stop`` will be ignored.
        
    ``day_length``
        An ``integer`` value to specify working day length. Default is ``8`` hours.
        
    ``color``
        A field, generally ``many2one``, to colorize calendar/gantt items.
        
    ``mode``
        A string value to set default view/zoom mode. For ``gantt`` view, this can be
        one of following (default is ``month``):
        
        * ``day``
        * ``3days``
        * ``week``
        * ``3weeks``
        * ``month``
        * ``3months``
        * ``year``
        * ``3years``
        * ``5years``

.. i18n: The ``level`` tag supports following attributes:
..

The ``level`` tag supports following attributes:

.. i18n:     ``object``
.. i18n:         An openerp object having many2one relationship with view object.
..

    ``object``
        一个openerp对象和视图object有many2one的关系。

.. i18n:     ``link``
.. i18n:         The field name in current object that links to the given ``object``.
..

    ``link``
        链接到给定对象的当前对象的字段名

.. i18n:     ``domain``
.. i18n:         The domain to be used to filter the given ``object`` records.
..

    ``domain``
        这个domain用于过滤给定的对象记录。

.. i18n: Drag and Drop
.. i18n: +++++++++++++
..

Drag and Drop
+++++++++++++

.. i18n: The left side pane displays list of the tasks grouped by the given ``level`` field.
.. i18n: You can reorder or change the group of any records by dragging them.
..

左边的窗格显示由level分组的任务列表。你可以重新排序或是通过拖动他们来更改记录的分组。

.. i18n: The main content pane displays horizontal bars plotted on a timeline grid. A group
.. i18n: of bars are summarised with a top summary bar displaying resource allocation of all
.. i18n: the underlying tasks.
..

主要内容窗格显示在时间格中绘制的水平条。一组水平条概要汇总了所有任务资源分配条。

.. i18n: You can change the task start time by dragging the tasks horizontally. While
.. i18n: end time can be changed by dragging right end of a bar.
..

你可以通过水平拖动任务来更改任务开始时间，当然也可以通过拖动右侧条来更改结束时间。

.. i18n: .. note::
.. i18n: 
.. i18n:     The time is calculated considering ``day_length`` so a bar will span more
.. i18n:     then one day if total time for a task is greater then ``day_length`` value.
.. i18n:     
.. i18n: Screenshots
.. i18n: +++++++++++
.. i18n:     
.. i18n: .. figure::  images/gantt.png
.. i18n:     :scale: 50%
.. i18n:     :align: center
..

.. note::

    The time is calculated considering ``day_length`` so a bar will span more
    then one day if total time for a task is greater then ``day_length`` value.
    
Screenshots
+++++++++++
    
.. figure::  images/gantt.png
    :scale: 50%
    :align: center

.. i18n: Design Elements
.. i18n: ---------------
..

Design Elements
---------------

.. i18n: The files describing the views are of the form:
..

文件中的视图描述形式如下：

.. i18n: :Example:
..

:Example:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <?xml version="1.0"?>
.. i18n:     <openerp>
.. i18n:        <data>
.. i18n:            [view definitions]
.. i18n:        </data>
.. i18n:     </openerp>
..

.. code-block:: xml

    <?xml version="1.0"?>
    <openerp>
       <data>
           [view definitions]
       </data>
    </openerp>

.. i18n: The view definitions contain mainly three types of tags:
..

视图定义包含了以下三种类型的标签：

.. i18n:     * **<record>** tags with the attribute model="ir.ui.view", which contain the view definitions themselves
.. i18n:     * **<record>** tags with the attribute model="ir.actions.act_window", which link actions to these views
.. i18n:     * **<menuitem>** tags, which create entries in the menu, and link them with actions
..

    * **<record>** 标签有属性model=“ir.ui.view”，它包含本身的视图定义
    * **<record>** 标签有属性model=“ir.actions.act_window”，它将动作和这些视图链接起来。
    * **<menuitem>** 标签，在菜单中创建记录，将他们和动作链接起来。

.. i18n: New : You can specify groups for whom the menu is accessible using the groups 
.. i18n: attribute in the `menuitem` tag.
..

New：你可以指定组，菜单在menuitem标签中用组属性来访问这些组。

.. i18n: New : You can now add shortcut using the `shortcut` tag.
..

New：你可以使用shortcut标签来加快捷键。

.. i18n: :Example:
..

:Example:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <shortcut 
.. i18n:     	name="Draft Purchase Order (Proposals)" 
.. i18n:     	model="purchase.order" 
.. i18n:     	logins="demo" 
.. i18n:     	menu="m"/>
..

.. code-block:: xml

    <shortcut 
    	name="Draft Purchase Order (Proposals)" 
    	model="purchase.order" 
    	logins="demo" 
    	menu="m"/>

.. i18n: Note that you should add an id attribute on the `menuitem` which is referred by 
.. i18n: menu attribute.
..

你应该加一个id属性在menuitem上

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <record model="ir.ui.view" id="v">
.. i18n:         <field name="name">sale.order.form</field>
.. i18n:         <field name="model">sale.order</field>
.. i18n:         <field name="priority" eval="2"/>
.. i18n:         <field name="arch" type="xml">
.. i18n: 	        <form string="Sale Order">
.. i18n: 	            .........
.. i18n: 	        </form>
.. i18n:         </field>
.. i18n:     </record>
..

.. code-block:: xml

    <record model="ir.ui.view" id="v">
        <field name="name">sale.order.form</field>
        <field name="model">sale.order</field>
        <field name="priority" eval="2"/>
        <field name="arch" type="xml">
	        <form string="Sale Order">
	            .........
	        </form>
        </field>
    </record>

.. i18n: Default value for the priority field : 16. When not specified the system will use the view with the lower priority.
..

priority字段的默认值为16，在没有特别规定的前提下，系统的视图都是最低优先级。

.. i18n: View Types
.. i18n: ++++++++++
..

View Types
++++++++++

.. i18n: Tree View
.. i18n: """""""""
.. i18n: You can specify the columns to include in the list, along with some details of
.. i18n: the list's appearance. The search fields aren't specified here, they're 
.. i18n: specified by the `select` attribute in the form view fields.
..

Tree View
"""""""""
你可以指定列表中包含的列元素和一些细节在列的显示中。search字段不能在这指定，他们显示在form视图中。

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:         <record id="view_location_tree2" model="ir.ui.view">
.. i18n:             <field name="name">stock.location.tree</field>
.. i18n:             <field name="model">stock.location</field>
.. i18n:             <field name="type">tree</field>
.. i18n:             <field name="priority" eval="2"/>
.. i18n:             <field name="arch" type="xml">
.. i18n:                 <tree 
.. i18n:                 	colors="blue:usage=='view';darkred:usage=='internal'">
.. i18n:                 	
.. i18n:                     <field name="complete_name"/>
.. i18n:                     <field name="usage"/>
.. i18n:                     <field 
.. i18n:                     	name="stock_real" 
.. i18n:                     	invisible="'product_id' not in context"/>
.. i18n:                     <field 
.. i18n:                     	name="stock_virtual" 
.. i18n:                     	invisible="'product_id' not in context"/>
.. i18n:                 </tree>
.. i18n:             </field>
.. i18n:         </record>
..

.. code-block:: xml

        <record id="view_location_tree2" model="ir.ui.view">
            <field name="name">stock.location.tree</field>
            <field name="model">stock.location</field>
            <field name="type">tree</field>
            <field name="priority" eval="2"/>
            <field name="arch" type="xml">
                <tree 
                	colors="blue:usage=='view';darkred:usage=='internal'">
                	
                    <field name="complete_name"/>
                    <field name="usage"/>
                    <field 
                    	name="stock_real" 
                    	invisible="'product_id' not in context"/>
                    <field 
                    	name="stock_virtual" 
                    	invisible="'product_id' not in context"/>
                </tree>
            </field>
        </record>

.. i18n: That example is just a flat list, but you can also display a real tree structure
.. i18n: by specifying a `field_parent`. The name is a bit misleading, though; the field
.. i18n: you specify must contain a list of all **child** entries.
..

这个例子是一个二维列表，但是你可以通过指点field_parent来显示树结构。这个名字尽管有些误导人，但是该字段必须包含一列所有的child记录。

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:         <record id="view_location_tree" model="ir.ui.view">
.. i18n:             <field name="name">stock.location.tree</field>
.. i18n:             <field name="model">stock.location</field>
.. i18n:             <field name="type">tree</field>
.. i18n:             <field name="field_parent">child_ids</field>
.. i18n:             <field name="arch" type="xml">
.. i18n:                 <tree toolbar="1">
.. i18n:                     <field icon="icon" name="name"/>
.. i18n:                 </tree>
.. i18n:             </field>
.. i18n:         </record>
..

.. code-block:: xml

        <record id="view_location_tree" model="ir.ui.view">
            <field name="name">stock.location.tree</field>
            <field name="model">stock.location</field>
            <field name="type">tree</field>
            <field name="field_parent">child_ids</field>
            <field name="arch" type="xml">
                <tree toolbar="1">
                    <field icon="icon" name="name"/>
                </tree>
            </field>
        </record>

.. i18n: On the `tree` element, the following attributes are supported:
..

在tree元素中包含下面的属性：

.. i18n: colors
.. i18n: 	Conditions for applying different colours to items in the list. The default
.. i18n: 	is black.
.. i18n: toolbar
.. i18n: 	Set this to 1 if you want a tree structure to list the top level entries
.. i18n: 	in a separate toolbar area. When you click on an entry in the toolbar, all
.. i18n: 	its descendants will be displayed in the main tree. The value is ignored
.. i18n: 	for flat lists.
..

colors：在列表中根据不同情况不同的颜色来记录，默认为黑。
toolbar：如果你想要一个树结构在单独工具栏区域列出上层的记录，那就把给属性值设为1。当你点击工具栏上的一个记录时，它的所有的后代都会显示在main tree中。二维列表中该值可以忽略

.. i18n: Grouping Elements
.. i18n: +++++++++++++++++
..

Grouping Elements
+++++++++++++++++

.. i18n: Separator
.. i18n: """""""""
..

Separator
"""""""""

.. i18n: Adds a separator line
..

加个分隔线

.. i18n: :Example:
..

:Example:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <separator string="Links" colspan="4"/>
..

.. code-block:: xml

    <separator string="Links" colspan="4"/>

.. i18n: The string attribute defines its label and the colspan attribute defines his horizontal size (in number of columns).
..

string属性定义了它的标签，colspan属性定义了他的水平大小（列的个数）。

.. i18n: Notebook
.. i18n: """"""""
..

Notebook
""""""""

.. i18n: <notebook>: With notebooks you can distribute the view fields on different tabs (each one defined by a page tag). You can use the tabpos properties to set tab at: up, down, left, right.
..

<notebook>: 用notebooks你可以分配视图字段在不同的标签上（每个由page tag定义）。你可以使用tabpos属性来设置tab：up，down，left，right。

.. i18n: :Example:
..

:Example:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <notebook colspan="4">....</notebook>
..

.. code-block:: xml

    <notebook colspan="4">....</notebook>

.. i18n: Group
.. i18n: """""
..

Group
"""""

.. i18n: <group>: groups several columns and split the group in as many columns as desired.
..

<group>: 对几个列进行分组。

.. i18n:     * **colspan**: the number of columns to use
.. i18n:     * **rowspan**: the number of rows to use
.. i18n:     * **expand**: if we should expand the group or not
.. i18n:     * **col**: the number of columns to provide (to its children)
.. i18n:     * **string**: (optional) If set, a frame will be drawn around the group of fields, with a label containing the string. Otherwise, the frame will be invisible.
..

    * **colspan**: 被使用的列数
    * **rowspan**: 被使用的行数
    * **expand**: 是否扩展该分组
    * **col**:被提供的列数 (给他的下级)
    * **string**: (可选) 如果设置了，将在字段组周围绘制一个框架, 包括这个string作为标签. 否则，这个框架是不可见的.

.. i18n: :Example:
..

:Example:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <group col="3" colspan="2">
.. i18n:         <field name="invoiced" select="2"/>
.. i18n:         <button colspan="1" name="make_invoice" states="confirmed" string="Make Invoice"
.. i18n:             type="object"/>
.. i18n:     </group>
..

.. code-block:: xml

    <group col="3" colspan="2">
        <field name="invoiced" select="2"/>
        <button colspan="1" name="make_invoice" states="confirmed" string="Make Invoice"
            type="object"/>
    </group>

.. i18n: Page
.. i18n: """"
..

Page
""""

.. i18n: Defines a new notebook page for the view.
..

为视图定义新的notebook

.. i18n: :Example:
..

:Example:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <page string="Order Line"> ... </page>:
..

.. code-block:: xml

    <page string="Order Line"> ... </page>:

.. i18n: * **string**: defines the name of the page.
..

* **string**: 定义page的名称

.. i18n: Data Elements
.. i18n: +++++++++++++
..

数据元素
+++++++++++++

.. i18n: Field
.. i18n: """""
..

Field
"""""

.. i18n: :guilabel:`attributes for the "field" tag`
..

:guilabel:`"field" tag的属性`

.. i18n:     * ``select="1"``: mark this field as being one of the search criteria for 
.. i18n:         this resource's search view. A value of 1 means that the field is
.. i18n:         included in the basic search, and a value of 2 means that it is in
.. i18n:         the advanced search.
.. i18n: 
.. i18n:     * ``colspan="4"``: the number of columns on which a field must extend.
.. i18n: 
.. i18n:     * ``readonly="1"``: set the widget as read only
.. i18n: 
.. i18n:     * ``required="1"``: the field is marked as required. If a field is marked as required, a user has to fill it the system won't save the resource if the field is not filled. This attribute supersede the required field value defined in the object.
.. i18n: 
.. i18n:     * ``nolabel="1"``: hides the label of the field (but the field is not hidden in the search view).
.. i18n: 
.. i18n:     * ``invisible="True"``: hides both the label and the field.
.. i18n: 
.. i18n:     * ``password="True"``: replace field values by asterisks, "*".
.. i18n: 
.. i18n:     * ``string=""``: change the field label. Note that this label is also used in the search view: see select attribute above).
.. i18n: 
.. i18n:     * ``domain``: can restrict the domain.
.. i18n:           + Example: domain="[('partner_id','=',partner_id)]"
.. i18n: 
.. i18n:     * ``widget``: can change the widget.
.. i18n:           + Example: widget="one2many_list"
.. i18n:                 - one2one_list
.. i18n:                 - one2many_list
.. i18n:                 - many2one_list
.. i18n:                 - many2many
.. i18n:                 - url
.. i18n:                 - email
.. i18n:                 - image
.. i18n:                 - float_time
.. i18n:                 - reference
.. i18n: 
.. i18n:     * ``mode``: sequences of the views when switching.            
.. i18n:         + Example: mode="tree,graph"
.. i18n: 
.. i18n:     * ``on_change``: define a function that is called when the content of the field changes.
.. i18n:           + Example: on_change="onchange_partner(type,partner_id)"
.. i18n:           + See the :ref:`on change event <onchange-event-link>` for details.
.. i18n: 
.. i18n:     * ``attrs``: Permits to define attributes of a field depends on other fields of the same window. (It can be use on     page, group, button and notebook tag also)
.. i18n:           + Format: "{'attribute':[('field_name','operator','value'),('field_name','operator','value')],'attribute2':[('field_name','operator','value'),]}"
.. i18n:           + where attribute will be readonly, invisible, required
.. i18n:           + Default value: {}.
.. i18n:           + Example: (in product.product)
..

    * ``select="1"``: 标记这个是search 视图的搜索条件之一 。
        数值1 意思是这个字段被被包括在基本搜索里
        数值2 意思是这个字段在高级搜索中.

    * ``colspan="4"``: 字段被扩展开的列数.

    * ``readonly="1"``: 设置位置 只读

    * ``required="1"``: 该字段被标记为 必须. 如果字段被标记为必须,用户必须填写它，如果字段不填，系统不会保存资源。这个属性将取代 对象中的定义的required 字段值.

    * ``nolabel="1"``: 隐藏字段的便签(但是这个字段在 search 视图不会被隐藏).

    * ``invisible="True"``: 隐藏标签和字段.

    * ``password="True"``: 用 星号替换字段值, "*".

    * ``string=""``: 改变字段的标签. 注意，这个标签也会用在search视图: 看上面的 select 属性).

    * ``domain``: 约束条件.
          + Example: domain="[('partner_id','=',partner_id)]"

    * ``widget``: 可改变 widget.
          + Example: widget="one2many_list"
                - one2one_list
                - one2many_list
                - many2one_list
                - many2many
                - url
                - email
                - image
                - float_time
                - reference

    * ``mode``: 视图切换时的顺序.
        + Example: mode="tree,graph"

    * ``on_change``: 定义一个 函数，当字段内容被改变时调用.
          + Example: on_change="onchange_partner(type,partner_id)"
          + 要更详细的内容，查看 :ref:`on change event <onchange-event-link>` .

    * ``attrs``: 允许定义一个字段的取决于同一窗口其它字段 的属性 . (也可用在 page, group, button and notebook 标签中o)
          + 格式: "{'attribute':[('field_name','operator','value'),('field_name','operator','value')],'attribute2':[('field_name','operator','value'),]}"
          + 这里的 attribute 是 readonly, invisible, required
          + 默认值: {}.
          + 例子在: (in product.product)

.. i18n:         .. code-block:: xml
.. i18n: 
.. i18n:             <field digits="(14, 3)" name="volume" attrs="{'readonly':[('type','=','service')]}"/>
.. i18n: 
.. i18n:     * ``eval``: evaluate the attribute content as if it was Python code (see :ref:`below <eval-attribute-link>` for example)
.. i18n: 
.. i18n:     * ``default_focus``: set to ``1`` to put the focus (cursor position) on this field when the form is first opened.
.. i18n:       There can only be one field within a view having this attribute set to ``1`` **(new as of 5.2)**
.. i18n: 
.. i18n:         .. code-block:: xml
.. i18n: 
.. i18n:             <field name="name" default_focus=”1”/> 
..

        .. code-block:: xml

            <field digits="(14, 3)" name="volume" attrs="{'readonly':[('type','=','service')]}"/>

    * ``eval``: evaluate the attribute content as if it was Python code (see :ref:`below <eval-attribute-link>` for example)

    * ``default_focus``: set to ``1`` to put the focus (cursor position) on this field when the form is first opened.
      There can only be one field within a view having this attribute set to ``1`` **(new as of 5.2)**

        .. code-block:: xml

            <field name="name" default_focus=”1”/> 

.. i18n: Example
..

Example

.. i18n: Here's the source code of the view of a sale order object. This is the object shown on the screen shots of the presentation.
..

这有销售订单对象视图的源代码。这是相同对象作为对象在截图中的显示。

.. i18n: :Example:
..

:Example:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <?xml version="1.0"?>
.. i18n:     <openerp>
.. i18n:         <data>
.. i18n:         <record id="view_partner_form" model="ir.ui.view">
.. i18n:                 <field name="name">res.partner.form</field>
.. i18n:                 <field name="model">res.partner</field>
.. i18n:                 <field name="type">form</field>
.. i18n:                 <field name="arch" type="xml">
.. i18n:                 <form string="Partners">
.. i18n:                     <group colspan="4" col="6">
.. i18n:                         <field name="name" select="1"/>
.. i18n:                         <field name="ref" select="1"/>
.. i18n:                         <field name="customer" select="1"/>
.. i18n:                         <field domain="[('domain', '=', 'partner')]" name="title"/>
.. i18n:                         <field name="lang" select="2"/>
.. i18n:                         <field name="supplier" select="2"/>
.. i18n:                     </group>
.. i18n:                     <notebook colspan="4">
.. i18n:                         <page string="General">
.. i18n:                             <field colspan="4" mode="form,tree" name="address"
.. i18n:                              nolabel="1" select="1">
.. i18n:                                 <form string="Partner Contacts">
.. i18n:                                     <field name="name" select="2"/>
.. i18n:                                     <field domain="[('domain', '=', 'contact')]" name="title"/>
.. i18n:                                     <field name="function"/>
.. i18n:                                     <field name="type" select="2"/>
.. i18n:                                     <field name="street" select="2"/>
.. i18n:                                     <field name="street2"/>
.. i18n:                                     <newline/>
.. i18n:                                     <field name="zip" select="2"/>
.. i18n:                                     <field name="city" select="2"/>
.. i18n:                                     <newline/>
.. i18n:                                     <field completion="1" name="country_id" select="2"/>
.. i18n:                                     <field name="state_id" select="2"/>
.. i18n:                                     <newline/>
.. i18n:                                     <field name="phone"/>
.. i18n:                                     <field name="fax"/>
.. i18n:                                     <newline/>
.. i18n:                                     <field name="mobile"/>
.. i18n:                                     <field name="email" select="2" widget="email"/>
.. i18n:                                 </form>
.. i18n:                                 <tree string="Partner Contacts">
.. i18n:                                     <field name="name"/>
.. i18n:                                     <field name="zip"/>
.. i18n:                                     <field name="city"/>
.. i18n:                                     <field name="country_id"/>
.. i18n:                                     <field name="phone"/>
.. i18n:                                     <field name="email"/>
.. i18n:                                 </tree>
.. i18n:                             </field>
.. i18n:                             <separator colspan="4" string="Categories"/>
.. i18n:                             <field colspan="4" name="category_id" nolabel="1" select="2"/>
.. i18n:                         </page>
.. i18n:                         <page string="Sales &amp; Purchases">
.. i18n:                             <separator string="General Information" colspan="4"/>
.. i18n:                             <field name="user_id" select="2"/>
.. i18n:                             <field name="active" select="2"/>
.. i18n:                             <field name="website" widget="url"/>
.. i18n:                             <field name="date" select="2"/>
.. i18n:                             <field name="parent_id"/>
.. i18n:                             <newline/>
.. i18n:                         </page>
.. i18n:                         <page string="History">
.. i18n:                             <field colspan="4" name="events" nolabel="1" widget="one2many_list"/>
.. i18n:                         </page>
.. i18n:                         <page string="Notes">
.. i18n:                             <field colspan="4" name="comment" nolabel="1"/>
.. i18n:                         </page>
.. i18n:                     </notebook>
.. i18n:                 </form>
.. i18n:                 </field>
.. i18n:             </record>
.. i18n:         <menuitem
.. i18n:                 action="action_partner_form"
.. i18n:                 id="menu_partner_form"
.. i18n:                 parent="base.menu_base_partner"
.. i18n:                 sequence="2"/>
.. i18n:         </data>
.. i18n:      </openerp>
..

.. code-block:: xml

    <?xml version="1.0"?>
    <openerp>
        <data>
        <record id="view_partner_form" model="ir.ui.view">
                <field name="name">res.partner.form</field>
                <field name="model">res.partner</field>
                <field name="type">form</field>
                <field name="arch" type="xml">
                <form string="Partners">
                    <group colspan="4" col="6">
                        <field name="name" select="1"/>
                        <field name="ref" select="1"/>
                        <field name="customer" select="1"/>
                        <field domain="[('domain', '=', 'partner')]" name="title"/>
                        <field name="lang" select="2"/>
                        <field name="supplier" select="2"/>
                    </group>
                    <notebook colspan="4">
                        <page string="General">
                            <field colspan="4" mode="form,tree" name="address"
                             nolabel="1" select="1">
                                <form string="Partner Contacts">
                                    <field name="name" select="2"/>
                                    <field domain="[('domain', '=', 'contact')]" name="title"/>
                                    <field name="function"/>
                                    <field name="type" select="2"/>
                                    <field name="street" select="2"/>
                                    <field name="street2"/>
                                    <newline/>
                                    <field name="zip" select="2"/>
                                    <field name="city" select="2"/>
                                    <newline/>
                                    <field completion="1" name="country_id" select="2"/>
                                    <field name="state_id" select="2"/>
                                    <newline/>
                                    <field name="phone"/>
                                    <field name="fax"/>
                                    <newline/>
                                    <field name="mobile"/>
                                    <field name="email" select="2" widget="email"/>
                                </form>
                                <tree string="Partner Contacts">
                                    <field name="name"/>
                                    <field name="zip"/>
                                    <field name="city"/>
                                    <field name="country_id"/>
                                    <field name="phone"/>
                                    <field name="email"/>
                                </tree>
                            </field>
                            <separator colspan="4" string="Categories"/>
                            <field colspan="4" name="category_id" nolabel="1" select="2"/>
                        </page>
                        <page string="Sales &amp; Purchases">
                            <separator string="General Information" colspan="4"/>
                            <field name="user_id" select="2"/>
                            <field name="active" select="2"/>
                            <field name="website" widget="url"/>
                            <field name="date" select="2"/>
                            <field name="parent_id"/>
                            <newline/>
                        </page>
                        <page string="History">
                            <field colspan="4" name="events" nolabel="1" widget="one2many_list"/>
                        </page>
                        <page string="Notes">
                            <field colspan="4" name="comment" nolabel="1"/>
                        </page>
                    </notebook>
                </form>
                </field>
            </record>
        <menuitem
                action="action_partner_form"
                id="menu_partner_form"
                parent="base.menu_base_partner"
                sequence="2"/>
        </data>
     </openerp>

.. i18n: .. _eval-attribute-link:
.. i18n: 
.. i18n: The eval attribute
.. i18n: //////////////////
..

.. _eval-attribute-link:

The eval attribute
//////////////////

.. i18n: The **eval** attribute evaluates its content as if it was Python code. This
.. i18n: allows you to define values that are not strings.
..

eval属性评估它的内容像Python代码似地。这就允许你定义不是字符串的值。

.. i18n: Normally, content inside *<field>* tags are always evaluated as strings.
..

一般情况下，内容中<field>标签一直作为字符串来计算。

.. i18n: .. describe:: Example 1:
..

.. describe:: Example 1:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <field name="value">2.3</field>
..

.. code-block:: xml

    <field name="value">2.3</field>

.. i18n: This will evaluate to the string ``'2.3'`` and not the float ``2.3``
..

2.3不是float 2.3而是字符串2.3

.. i18n: .. describe:: Example 2:
..

.. describe:: Example 2:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <field name="value">False</field>
..

.. code-block:: xml

    <field name="value">False</field>

.. i18n: This will evaluate to the string ``'False'`` and not the boolean
.. i18n: ``False``. This is especially tricky because Python's conversion rules
.. i18n: consider any non-empty string to be ``True``, so the above code will
.. i18n: end up storing the opposite of what is desired. 
..

False不是布尔值False，而是字符串’False’。 This is especially tricky because Python's conversion rules
consider any non-empty string to be ``True``, so the above code will
end up storing the opposite of what is desired. 

.. i18n: If you want to evaluate the value to a float, a boolean or another
.. i18n: type, except string, you need to use the **eval** attribute:
..

如果你想要计算float，boolean或是其他类型，除了string，可以使用eval属性：

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <field name="value" eval="2.3" />
.. i18n:     <field name="value" eval="False" />
..

.. code-block:: xml

    <field name="value" eval="2.3" />
    <field name="value" eval="False" />

.. i18n: Button
.. i18n: """"""
..

Button
""""""

.. i18n: Adds a button to the current view. Allows the user to perform various
.. i18n: actions on the current record.
..

加button到当前视图中。允许用户在当前记录上执行各种动作。

.. i18n: After a button has been clicked, the record should always be reloaded.
..

点击button按钮后，记录会重新装载。

.. i18n: Buttons have the following attributes:
..

Buttons有以下的属性：

.. i18n: ``@type``
.. i18n:   Defines the type of action performed when the button is activated:
..

``@type``
  定义button按钮激活后action执行类型。

.. i18n:   ``workflow`` (default)
.. i18n:     The button will send a workflow signal [#]_ on the current model
.. i18n:     using the ``@name`` of the button as workflow signal name and
.. i18n:     providing the record id as parameter (in a list).
..

  ``workflow`` (default)
    button会在当前model上发送workflow signal，使用button的name作为workflow signal name并且提供记录id作为参数（in a list）。

.. i18n:     The workflow signal may return an :ref:`action descriptor <window-action>`,
.. i18n:     which should be executed. Otherwise it will return ``False``.
..

   workflow signal会返回一个动作描述符，已执行的。否则会返回False。

.. i18n:   ``object``
.. i18n:     The button will execute the method of name ``@name`` on the
.. i18n:     current model, providing the record id as parameter (in a
.. i18n:     list). This call may return an :ref:`action descriptor <window-action>`,
.. i18n:     which should be executed. Otherwise it will return ``False``.
..

  ``object``
    button会在当前model上执行@name的方法，提供一个记录id作为参数（in a list）。该调用会返回一个动作描述符来执行。

.. i18n:   ``action``
.. i18n:     The button will trigger the execution of an action
.. i18n:     (``ir.actions.actions``). The ``id`` of this action is the
.. i18n:     ``@name`` of the button.
..

  ``action``
    button会触发action（ir.actions.actions）来执行。这个动作的id是button的@name。

.. i18n:     From there, follows the normal action-execution workflow. One extra action
.. i18n:     type is to just close the window.
..

    From there, follows the normal action-execution workflow. One extra action
    type is to just close the window.

.. i18n: 	.. code-block:: python
.. i18n: 	
.. i18n: 		return {'type': 'ir.actions.act_window_close'}
..

	.. code-block:: python
	
		return {'type': 'ir.actions.act_window_close'}

.. i18n: ``@special``
.. i18n:   Only has one possible value currently: ``cancel``, which indicates
.. i18n:   that the popup should be closed without performing any RPC call or
.. i18n:   action resolution.
..

``@special``
  当前仅有一个可能值：cancel，popup在没有RPC调用或是action执行时就会关闭。

.. i18n:   .. note::
.. i18n:      Only meaningful within a popup-type window (e.g. a
.. i18n:      wizard). Otherwise, is a noop.
.. i18n: 
.. i18n:   .. warning::
.. i18n: 
.. i18n:      ``@special`` and ``@type`` are incompatible.
..

  .. note::
     Only meaningful within a popup-type window (e.g. a
     wizard). Otherwise, is a noop.

  .. warning::

     ``@special`` and ``@type`` are incompatible.

.. i18n: ``@name``
.. i18n:   The button's identifier, used to indicate which method should be
.. i18n:   called, which signal sent or which action executed.
..

``@name``
  button的标识符，用于指出调用哪个方法，发送哪个signal，执行哪个动作。

.. i18n: ``@confirm``
.. i18n:   A confirmation popup to display before executing the button's
.. i18n:   task. If the confirmation is dismissed the button's task *must not*
.. i18n:   be executed.
..

``@confirm``
  当执行button的任务前，确认对话框会显示。当确认取消后，button的任务不会执行。

.. i18n: ``@string``
.. i18n:   The label which should be displayed on the button [#]_.
..

``@string``
  button上会显示的标签。 [#]_.

.. i18n: ``@icon``
.. i18n:   Display an icon on the button, if absent the button is text-only
.. i18n:   [#]_.
..

``@icon``
  显示button图表，如果没有这个button就是text-only
  [#]_.

.. i18n: ``@states``, ``@attrs``, ``@invisible``
.. i18n:   Standard OpenERP meaning for those view attributes
..

``@states``, ``@attrs``, ``@invisible``
  OpenERP这些视图属性的标准含义。

.. i18n: ``@default_focus``
.. i18n:   If set to a truthy value (``1``), automatically selects that button
.. i18n:   so it is used if ``RETURN`` is pressed while on the form.
..

``@default_focus``
  如果设置为确认值（1）时，当点击RETURN时就会自动搜索按钮。

.. i18n:   May be ignored by the client.
..

  client端会忽视这个属性。

.. i18n:   .. versionadded:: 6.0
..

  .. versionadded:: 6.0

.. i18n: :Example:
..

:Example:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <button name="order_confirm" states="draft" string="Confirm Order" icon="gtk-execute"/>
.. i18n:     <button name="_action_open_window" string="Open Margins" type="object" default_focus=”1”/>
..

.. code-block:: xml

    <button name="order_confirm" states="draft" string="Confirm Order" icon="gtk-execute"/>
    <button name="_action_open_window" string="Open Margins" type="object" default_focus=”1”/>

.. i18n: Label
.. i18n: """""
..

Label
"""""

.. i18n: Adds a simple label using the string attribute as caption.
..

用label来加个标题。

.. i18n: :Example:
..

:Example:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <label string="Test"/>
..

.. code-block:: xml

    <label string="Test"/>

.. i18n: New Line
.. i18n: """"""""
..

New Line
""""""""

.. i18n: Force a return to the line even if all the columns of the view are not filled in.
..

如果视图的所有列不能全部放进一行是强制换行。

.. i18n: :Example:
..

:Example:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <newline/>
..

.. code-block:: xml

    <newline/>

.. i18n: .. [#] via ``exec_workflow`` on the ``object`` rpc endpoint
..

.. [#] via ``exec_workflow`` on the ``object`` rpc endpoint

.. i18n: .. [#] in form view, in list view buttons have no label
..

.. [#] in form view, in list view buttons have no label

.. i18n: .. [#] behavior in list view is undefined, as list view buttons don't
.. i18n:        have labels.
..

.. [#] behavior in list view is undefined, as list view buttons don't
       have labels.

.. i18n: Inheritance in Views 
.. i18n: --------------------
..

Inheritance in Views 
--------------------

.. i18n: When you create and inherit objects in some custom or specific modules, it is better to inherit (than to replace) from an existing view to add/modify/delete some fields and preserve the others.
..

当你要在一些自定义或是特定的模块上创建和继承对象时，在已经存在的视图上通过继承来添加/修改/删除一些字段相比于替换更好些。

.. i18n: :Example:
..

:Example:

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n: 	<record model="ir.ui.view" id="view_partner_form">
.. i18n: 	    <field name="name">res.partner.form.inherit</field>
.. i18n: 	    <field name="model">res.partner</field>
.. i18n: 	    <field name="inherit_id" ref="base.view_partner_form"/>
.. i18n: 	    <field name="arch" type="xml">
.. i18n: 	        <notebook position="inside">
.. i18n: 	            <page string="Relations">
.. i18n: 	                <field name="relation_ids" colspan="4" nolabel="1"/>
.. i18n: 	            </page>
.. i18n: 	        </notebook>
.. i18n: 	    </field>
.. i18n: 	</record>
..

.. code-block:: xml

	<record model="ir.ui.view" id="view_partner_form">
	    <field name="name">res.partner.form.inherit</field>
	    <field name="model">res.partner</field>
	    <field name="inherit_id" ref="base.view_partner_form"/>
	    <field name="arch" type="xml">
	        <notebook position="inside">
	            <page string="Relations">
	                <field name="relation_ids" colspan="4" nolabel="1"/>
	            </page>
	        </notebook>
	    </field>
	</record>

.. i18n: This will add a page to the notebook of the ``res.partner.form`` view in the 
.. i18n: base module.
..

这是要在base模块上给res.partner.form的notebook里面加一个page。

.. i18n: The inheritance engine will parse the existing view and search for the root nodes of
..

继承engine会分析已存在的视图并且搜索的根节点。

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n: 	<field name="arch" type="xml">
..

.. code-block:: xml

	<field name="arch" type="xml">

.. i18n: It will append or edit the content of this tag. If this tag has some attributes, 
.. i18n: it will look in the parent view for a node with matching attributes (except 
.. i18n: position).
..

它会添加或是修改这个标签的内容。如果这个标签有很多属性，它会查找父类视图来匹配这些属性。

.. i18n: You can use these values in the position attribute:
..

在位置属性上你可以使用以下的值：

.. i18n:     * inside (default): your values will be appended inside the tag
.. i18n:     * after: add the content after the tag
.. i18n:     * before: add the content before the tag
.. i18n:     * replace: replace the content of the tag. 
..

    * inside (default): your values will be appended inside the tag
    * after: add the content after the tag
    * before: add the content before the tag
    * replace: replace the content of the tag. 

.. i18n: Replacing Content
.. i18n: +++++++++++++++++
..

Replacing Content
+++++++++++++++++

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n: 	<record model="ir.ui.view" id="view_partner_form1">
.. i18n: 	    <field name="name">res.partner.form.inherit1</field>
.. i18n: 	    <field name="model">res.partner</field>
.. i18n: 	    <field name="inherit_id" ref="base.view_partner_form"/>
.. i18n: 	    <field name="arch" type="xml">
.. i18n: 	        <page string="Extra Info" position="replace">
.. i18n: 	            <field name="relation_ids" colspan="4" nolabel="1"/>
.. i18n: 	        </page>
.. i18n: 	    </field>
.. i18n: 	</record>
..

.. code-block:: xml

	<record model="ir.ui.view" id="view_partner_form1">
	    <field name="name">res.partner.form.inherit1</field>
	    <field name="model">res.partner</field>
	    <field name="inherit_id" ref="base.view_partner_form"/>
	    <field name="arch" type="xml">
	        <page string="Extra Info" position="replace">
	            <field name="relation_ids" colspan="4" nolabel="1"/>
	        </page>
	    </field>
	</record>

.. i18n: Will replace the content of the Extra Info tab of the notebook with the ``relation_ids`` field.
..

可用relation_ids字段来替换notebook的额外信息标签的内容。

.. i18n: The parent and the inherited views are correctly updated with ``--update=all`` argument like any other views.
..

父类和子类的视图可像其他视图一样通过—update=all来进行更新。

.. i18n: Deleting Content
.. i18n: ++++++++++++++++
..

Deleting Content
++++++++++++++++

.. i18n: To delete a field from a form, an empty element with ``position="replace"`` attribute is used. Example:
..

想要删除表单视图中的一个字段，可使用position="replace"属性。

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n: 	<record model="ir.ui.view" id="view_partner_form2">
.. i18n: 	    <field name="name">res.partner.form.inherit2</field>
.. i18n: 	    <field name="model">res.partner</field>
.. i18n: 	    <field name="inherit_id" ref="base.view_partner_form"/>
.. i18n: 	    <field name="arch" type="xml">
.. i18n: 	        <field name="lang" position="replace"/>
.. i18n: 	    </field>
.. i18n: 	</record>
..

.. code-block:: xml

	<record model="ir.ui.view" id="view_partner_form2">
	    <field name="name">res.partner.form.inherit2</field>
	    <field name="model">res.partner</field>
	    <field name="inherit_id" ref="base.view_partner_form"/>
	    <field name="arch" type="xml">
	        <field name="lang" position="replace"/>
	    </field>
	</record>

.. i18n: Inserting Content
.. i18n: +++++++++++++++++
..

Inserting Content
+++++++++++++++++

.. i18n: To add a field into a form before the specified tag use ``position="before"`` attribute. 
..

想要加一个字段到form中在特定标签前的话，使用position=’before’属性。

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n: 	<record model="ir.ui.view" id="view_partner_form3">
.. i18n: 	    <field name="name">res.partner.form.inherit3</field>
.. i18n: 	    <field name="model">res.partner</field>
.. i18n: 	    <field name="inherit_id" ref="base.view_partner_form"/>
.. i18n: 	    <field name="arch" type="xml">
.. i18n: 	        <field name="lang" position="before">
.. i18n: 	            <field name="relation_ids"/>
.. i18n: 	        </field>
.. i18n: 	    </field>
.. i18n: 	</record>
.. i18n: 	
.. i18n: Will add ``relation_ids`` field before the ``lang`` field.	
..

.. code-block:: xml

	<record model="ir.ui.view" id="view_partner_form3">
	    <field name="name">res.partner.form.inherit3</field>
	    <field name="model">res.partner</field>
	    <field name="inherit_id" ref="base.view_partner_form"/>
	    <field name="arch" type="xml">
	        <field name="lang" position="before">
	            <field name="relation_ids"/>
	        </field>
	    </field>
	</record>
	
在lang字段前加relation_ids字段。	

.. i18n: To add a field into a form after the specified tag use ``position="after"`` attribute. 
..

想要加一个字段到form中在指定标签后的话，使用position=’before’属性。

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n: 	<record model="ir.ui.view" id="view_partner_form4">
.. i18n: 	    <field name="name">res.partner.form.inherit4</field>
.. i18n: 	    <field name="model">res.partner</field>
.. i18n: 	    <field name="inherit_id" ref="base.view_partner_form"/>
.. i18n: 	    <field name="arch" type="xml">
.. i18n: 	        <field name="lang" position="after">
.. i18n: 	            <field name="relation_ids"/>
.. i18n: 	        </field>
.. i18n: 	    </field>
.. i18n: 	</record>
.. i18n: 	
.. i18n: Will add ``relation_ids`` field after the ``lang`` field.
..

.. code-block:: xml

	<record model="ir.ui.view" id="view_partner_form4">
	    <field name="name">res.partner.form.inherit4</field>
	    <field name="model">res.partner</field>
	    <field name="inherit_id" ref="base.view_partner_form"/>
	    <field name="arch" type="xml">
	        <field name="lang" position="after">
	            <field name="relation_ids"/>
	        </field>
	    </field>
	</record>
	
在lang字段后加relation_ids字段。

.. i18n: Multiple Changes
.. i18n: ++++++++++++++++
..

Multiple Changes
++++++++++++++++

.. i18n: To make changes in more than one location, wrap the fields in a data element.
..

想要在多个位置进行更改，在数据元素中包裹多个字段。

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <record model="ir.ui.view" id="view_partner_form5">
.. i18n:         <field name="name">res.partner.form.inherit5</field>
.. i18n:         <field name="model">res.partner</field>
.. i18n:         <field name="inherit_id" ref="base.view_partner_form"/>
.. i18n:         <field name="arch" type="xml">
.. i18n:             <data>
.. i18n:                 <field name="lang" position="replace"/>
.. i18n:                 <field name="website" position="after">
.. i18n:                     <field name="lang"/>
.. i18n:                 </field>
.. i18n:             </data>
.. i18n:         </field>
.. i18n:     </record>
..

.. code-block:: xml

    <record model="ir.ui.view" id="view_partner_form5">
        <field name="name">res.partner.form.inherit5</field>
        <field name="model">res.partner</field>
        <field name="inherit_id" ref="base.view_partner_form"/>
        <field name="arch" type="xml">
            <data>
                <field name="lang" position="replace"/>
                <field name="website" position="after">
                    <field name="lang"/>
                </field>
            </data>
        </field>
    </record>

.. i18n: Will delete the ``lang`` field from its usual location, and display it after
.. i18n: the ``website`` field.
..

在平常位置删除lang字段，在website后显示它。

.. i18n: .. _xpath-element-inheritance:
.. i18n: 
.. i18n: XPath Element
.. i18n: +++++++++++++
..

.. _xpath-element-inheritance:

XPath Element
+++++++++++++

.. i18n: Sometimes a view is too complicated to let you simply identify a target field
.. i18n: by name. For example, the field might appear in two places. When that happens,
.. i18n: you can use an ``xpath`` element to describe where your changes should be 
.. i18n: placed. 
..

有时视图因为太复杂了而不能让你简单的通过name找到字段。例如，字段显示在两个地方。在这种情况下，你可以使用xpath元素来描述想要进行更改的位置。

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <record model="ir.ui.view" id="view_partner_form6">
.. i18n:         <field name="name">res.partner.form.inherit6</field>
.. i18n:         <field name="model">res.partner</field>
.. i18n:         <field name="inherit_id" ref="base.view_partner_form"/>
.. i18n:         <field name="arch" type="xml">
.. i18n:             <data>
.. i18n:                 <xpath 
.. i18n:                     expr="//field[@name='address']/form/field[@name='email']"
.. i18n:                     position="after">
.. i18n:                     <field name="age"/>
.. i18n:                 </xpath>
.. i18n:                 <xpath 
.. i18n:                     expr="//field[@name='address']/tree/field[@name='email']"
.. i18n:                     position="after">
.. i18n:                     <field name="age"/>
.. i18n:                 </xpath>
.. i18n:             </data>
.. i18n:         </field>
.. i18n:     </record>
.. i18n:     
.. i18n: Will add the ``age`` field after the ``email`` field in both the form and tree 
.. i18n: view of the address list.       
..

.. code-block:: xml

    <record model="ir.ui.view" id="view_partner_form6">
        <field name="name">res.partner.form.inherit6</field>
        <field name="model">res.partner</field>
        <field name="inherit_id" ref="base.view_partner_form"/>
        <field name="arch" type="xml">
            <data>
                <xpath 
                    expr="//field[@name='address']/form/field[@name='email']"
                    position="after">
                    <field name="age"/>
                </xpath>
                <xpath 
                    expr="//field[@name='address']/tree/field[@name='email']"
                    position="after">
                    <field name="age"/>
                </xpath>
            </data>
        </field>
    </record>
    
在表单视图和列表视图中添加age字段在email字段后。      

.. i18n: Replacing Attributes
.. i18n: ++++++++++++++++++++
..

Replacing Attributes
++++++++++++++++++++

.. i18n: The ``attributes`` position lets you change an element's attributes without 
.. i18n: completely replacing it and its children. A common example is changing the
.. i18n: colours in a tree view.
..

The ``attributes`` position lets you change an element's attributes without 
completely replacing it and its children. A common example is changing the
colours in a tree view.

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <record id="mrp_production_tree_view" model="ir.ui.view">
.. i18n:       <field name="name">mrp.production.mycompany.tree.view</field>
.. i18n:       <field name="model">mrp.production</field>
.. i18n:       <field name="type">tree</field>
.. i18n:       <field name="inherit_id" ref="mrp.mrp_production_tree_view"/>
.. i18n:       <field name="arch" type="xml">
.. i18n:         <xpath expr="//tree" position="attributes">
.. i18n:           <attribute name="colors">blue:state=='draft'</attribute>
.. i18n:         </xpath>
.. i18n:       </field>
.. i18n:     </record>
..

.. code-block:: xml

    <record id="mrp_production_tree_view" model="ir.ui.view">
      <field name="name">mrp.production.mycompany.tree.view</field>
      <field name="model">mrp.production</field>
      <field name="type">tree</field>
      <field name="inherit_id" ref="mrp.mrp_production_tree_view"/>
      <field name="arch" type="xml">
        <xpath expr="//tree" position="attributes">
          <attribute name="colors">blue:state=='draft'</attribute>
        </xpath>
      </field>
    </record>

.. i18n: Specify the views you want to use
.. i18n: ---------------------------------
..

指定你要使用的视图
---------------------------------

.. i18n: There are some cases where you would like to specify a view other than the default:
..

在几种情况下你相比于默认的视图更想用指定的视图：

.. i18n: - If there are several form or tree views for an object.
.. i18n: - If you want to change the form or tree view used by a relational field 
.. i18n:   (one2many for example).
..

- 如果一个对象有好几种表单或是列表视图。
- 如果你想要通过使用关系字段（如one2many）来更改表单或是列表视图。

.. i18n: Using the priority field
.. i18n: ++++++++++++++++++++++++
..

Using the priority field
++++++++++++++++++++++++

.. i18n: This field is available in the view definition, and is 16 by default. By 
.. i18n: default, OpenERP will display a model using the view with the highest priority
.. i18n: (the smallest number). For example, imagine we have two views for a simple model.
.. i18n: The model *client* with two fields : **firstname** and **lastname**. We will define
.. i18n: two views, one which shows the firstname first, and the other one which shows 
.. i18n: the lastname first.
..

这个字段在视图定义中是可用的，默认为16。在默认情况下，OpenERP用最高优先级（更小的值）的视图来显示model。比如，想象我们的一个model有两个视图。model client有两个字段：firstname和lastname。我们将会定义两个视图，一个用于首先显示firstname，另一个用于首先显示lastname。

.. i18n: .. code-block:: xml
.. i18n:     :linenos:
.. i18n: 
.. i18n:     <!--
.. i18n:         Here is the first view for the model 'client'.
.. i18n:         We don't specify a priority field, which means 
.. i18n:         by default 16.
.. i18n:     -->
.. i18n:     <record model="ir.ui.view" id="client_form_view_1">
.. i18n:         <field name="name">client.form.view1</field>
.. i18n:         <field name="model">client</field>
.. i18n:         <field name="type">form</fiel>
.. i18n:         <field name="arch" type="xml">
.. i18n:             <field name="firstname"/>
.. i18n:             <field name="lastname"/>
.. i18n:         </field>
.. i18n:     </record>
.. i18n: 
.. i18n:     <!--
.. i18n:         A second view, which show fields in an other order.
.. i18n:         We specify a priority of 15.
.. i18n:     -->
.. i18n:     <record model="ir.ui.view" id="client_form_view_2">
.. i18n:         <field name="name">client.form.view2</field>
.. i18n:         <field name="model">client</field>
.. i18n:         <field name="priority" eval="15"/>
.. i18n:         <field name="type">form</fiel>
.. i18n:         <field name="arch" type="xml">
.. i18n:             <field name="lastname"/>
.. i18n:             <field name="firstname"/>
.. i18n:         </field>
.. i18n:     </record>
..

.. code-block:: xml
    :linenos:

    <!--
        Here is the first view for the model 'client'.
        We don't specify a priority field, which means 
        by default 16.
    -->
    <record model="ir.ui.view" id="client_form_view_1">
        <field name="name">client.form.view1</field>
        <field name="model">client</field>
        <field name="type">form</fiel>
        <field name="arch" type="xml">
            <field name="firstname"/>
            <field name="lastname"/>
        </field>
    </record>

    <!--
        A second view, which show fields in an other order.
        We specify a priority of 15.
    -->
    <record model="ir.ui.view" id="client_form_view_2">
        <field name="name">client.form.view2</field>
        <field name="model">client</field>
        <field name="priority" eval="15"/>
        <field name="type">form</fiel>
        <field name="arch" type="xml">
            <field name="lastname"/>
            <field name="firstname"/>
        </field>
    </record>

.. i18n: Now, each time OpenERP will have to show a form view for our object *client*, it will have the choice between two views.
.. i18n: **It will always use the second one, because it has a higher priority !** Unless you tell it to use the first one !
..

现在，OpenERP每次为对象client显示表单视图，它都有两个视图选择。它一直选择的是第二个，因为这个有高优先级。除非你告诉它选择第一个。

.. i18n: Specify per-action view
.. i18n: +++++++++++++++++++++++
..

Specify per-action view
+++++++++++++++++++++++

.. i18n: To illustrate this point, we will create 2 menus which show a form view for this *client* object :
..

为了说明这一点，我们将会创建2个菜单来为client对象显示表单视图。

.. i18n: .. code-block:: xml
.. i18n:     :linenos:
.. i18n: 
.. i18n:     <!--
.. i18n:         This action open the default view (in our case,
.. i18n:         the view with the highest priority, the second one)
.. i18n:     -->
.. i18n:     <record 
.. i18n:     	model="ir.actions.act_window" 
.. i18n:     	id="client_form_action">
.. i18n:         <field name="name">client.form.action</field>
.. i18n:         <field name="res_model">client</field>
.. i18n:         <field name="view_type">form</field>
.. i18n:         <field name="view_mode">form</field>
.. i18n:     </record>
.. i18n: 
.. i18n:     <!--
.. i18n:         This action open the view we specify.
.. i18n:     -->
.. i18n:     <record 
.. i18n:     	model="ir.actions.act_window" 
.. i18n:     	id="client_form_action1">
.. i18n:         <field name="name">client.form.action1</field>
.. i18n:         <field name="res_model">client</field>
.. i18n:         <field name="view_type">form</field>
.. i18n:         <field name="view_mode">form</field>
.. i18n:         <field name="view_id" ref="client_form_view_1"/>
.. i18n:     </record>
.. i18n: 
.. i18n:     <menuitem id="menu_id" name="Client main menu"/>
.. i18n:     <menuitem 
.. i18n:     	id="menu_id_1" 
.. i18n:     	name="Here we don't specify the view"
.. i18n:         action="client_form_action" parent="menu_id"/>
.. i18n:     <menuitem 
.. i18n:     	id="menu_id_1" 
.. i18n:     	name="Here we specify the view"
.. i18n:         action="client_form_action1" parent="menu_id"/>
..

.. code-block:: xml
    :linenos:

    <!--
        This action open the default view (in our case,
        the view with the highest priority, the second one)
    -->
    <record 
    	model="ir.actions.act_window" 
    	id="client_form_action">
        <field name="name">client.form.action</field>
        <field name="res_model">client</field>
        <field name="view_type">form</field>
        <field name="view_mode">form</field>
    </record>

    <!--
        This action open the view we specify.
    -->
    <record 
    	model="ir.actions.act_window" 
    	id="client_form_action1">
        <field name="name">client.form.action1</field>
        <field name="res_model">client</field>
        <field name="view_type">form</field>
        <field name="view_mode">form</field>
        <field name="view_id" ref="client_form_view_1"/>
    </record>

    <menuitem id="menu_id" name="Client main menu"/>
    <menuitem 
    	id="menu_id_1" 
    	name="Here we don't specify the view"
        action="client_form_action" parent="menu_id"/>
    <menuitem 
    	id="menu_id_1" 
    	name="Here we specify the view"
        action="client_form_action1" parent="menu_id"/>

.. i18n: As you can see on line *19*, we can specify a view. That means that when we open 
.. i18n: the second menu, OpenERP will use the form view *client_form_view_1*, regardless
.. i18n: of its priority.
..

你可以看到第19行，我们特定了一个视图。这意味着当我们打开第二个菜单时，OpenERP将会使用视图client_form_view_1，而不管它的优先级。

.. i18n: .. note::
.. i18n: 
.. i18n:     Remember to use the module name (*module.view_id*) in the *ref* attribute if 
.. i18n:     you are referring to a view defined in another module.
..

.. note::

    Remember to use the module name (*module.view_id*) in the *ref* attribute if 
    you are referring to a view defined in another module.

.. i18n: Specify views for related fields
.. i18n: ++++++++++++++++++++++++++++++++
..

Specify views for related fields
++++++++++++++++++++++++++++++++

.. i18n: Using the context
.. i18n: """""""""""""""""
..

Using the context
"""""""""""""""""

.. i18n: The *view_id* method works very well for menus/actions, but how can you specify the view to use for a one2many
.. i18n: field, for example? When you have a one2many field, two views are used, a tree view (**in blue**), and a form view when
.. i18n: you click on the add button (**in red**).
..

view_id方法对于menus/actions效果很好，但是你如何为one2many字段特定视图呢？当你有一个one2many字段时，将会使用两个视图，一个列表视图（蓝色的），和一个表单视图（红色的，当你点击添加按钮时就会显示出）。

.. i18n: .. figure::  images/one2many_views.png
.. i18n:     :scale: 70%
.. i18n:     :align: center
..

.. figure::  images/one2many_views.png
    :scale: 70%
    :align: center

.. i18n: When you add a one2many field in a form view, you do something like this :
..

当你添加一个one2many字段在表单视图中时，你会这么做：

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <field name="order_line" colspan="4" nolabel="1"/>
..

.. code-block:: xml

    <field name="order_line" colspan="4" nolabel="1"/>

.. i18n: If you want to specify the views to use, you can add a *context* attribute, and
.. i18n: specify a view id for each type of view supported, exactly like the action's 
.. i18n: *view_id* attribute:
..

当你想要使用指定的视图时，你可以添加一个context属性，并且为每个支持的视图类型指定一个view id，就像action的view_id属性：

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <field name="order_line" colspan="4" nolabel="1"
.. i18n:            context="{'form_view_ref' : 'module.view_id', 'tree_view_ref' : 'module.view_id'}"/>
..

.. code-block:: xml

    <field name="order_line" colspan="4" nolabel="1"
           context="{'form_view_ref' : 'module.view_id', 'tree_view_ref' : 'module.view_id'}"/>

.. i18n: If you don't specify the views, OpenERP will choose one in this order :
..

如果你不想指定视图，OpenERP将会在以下的order中选择一个：

.. i18n: 1. It will use the <form> or <tree> view defined **inside** the field (see below)
.. i18n: 2. Else, it will use the views with the highest priority for this object.
.. i18n: 3. Finally, it will generate default empty views, with all fields.
..

1．它会使用定义了inside字段的<form>和<tree>视图。
2．不然，它会使用这个对象最高优先级的视图。
3．最后，它会产生拥有所有字段的默认空视图。

.. i18n: .. note::
.. i18n: 
.. i18n:     The context keys are named <view_type>_view_ref.
..

.. note::

    The context keys are named <view_type>_view_ref.

.. i18n: .. note::
.. i18n: 
.. i18n:     By default, OpenERP will never use a view that is not defined for your object. If you have two models, with the
.. i18n:     same fields, but a different model name, OpenERP will never use the view of one for the other,
.. i18n:     even if one model inherit an other.
.. i18n: 
.. i18n:     You can force this by manually specifying the view, either in the action or in the context.
..

.. note::

  默认情况下，OpenERP不会使用不是为自己对象定义的视图。如果你有两个model，有相同的字段，但是不同的model名称，OpenERP不会混乱使用，即使一个model继承自另一个。你可以更改这个通过手动指定视图，在动作中或是上下文中。

.. i18n: Using subviews
.. i18n: """"""""""""""
..

Using subviews
""""""""""""""

.. i18n: In the case of relational fields, you can create a view directly inside a field :
..

对于相关的字段，你可以直接在一个字段中创建一个视图：

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <record model="ir.ui.view" id="some_view">
.. i18n:         <field name="name">some.view</field>
.. i18n:         <field name="type">form</field>
.. i18n:         <field name="model">some.model.with.one2many</field>
.. i18n:         <field name="arch" type="xml">
.. i18n:             <field name="..."/>
.. i18n:             
.. i18n:             <!-- <=== order_line is a one2many field -->
.. i18n:             <field name="order_line" colspan="4" nolabel="1">
.. i18n:                 <form>
.. i18n:                     <field name="qty"/>
.. i18n:                     ...
.. i18n:                 </form>
.. i18n:                 <tree>
.. i18n:                     <field name="qty"/>
.. i18n:                     ...
.. i18n:                 </tree>
.. i18n:             </field>
.. i18n:     </field>
..

.. code-block:: xml

    <record model="ir.ui.view" id="some_view">
        <field name="name">some.view</field>
        <field name="type">form</field>
        <field name="model">some.model.with.one2many</field>
        <field name="arch" type="xml">
            <field name="..."/>
            
            <!-- <=== order_line is a one2many field -->
            <field name="order_line" colspan="4" nolabel="1">
                <form>
                    <field name="qty"/>
                    ...
                </form>
                <tree>
                    <field name="qty"/>
                    ...
                </tree>
            </field>
    </field>

.. i18n: If you or another developer want to inherit from this view in another module,
.. i18n: you need to inherit from the parent view and then modify the child fields.
.. i18n: With child views, you'll often need to use an :ref:`xpath-element-inheritance`
.. i18n: to describe exactly where to place your new fields.
..

如果你或是其他的开发人员想要在其他的module中继承这个视图，你需要继承父类视图并且修改子类字段。对于子类视图，你需要使用XPath Element来直接描述想要在哪里存放你的新字段。

.. i18n: .. code-block:: xml
.. i18n: 
.. i18n:     <record model="ir.ui.view" id="some_inherited_view">
.. i18n:         <field name="name">some.inherited.view</field>
.. i18n:         <field name="type">form</field>
.. i18n:         <field name="model">some.model.with.one2many</field>
.. i18n:         <field name="inherit_id" ref="core_module.some_view"/>
.. i18n:         <field name="arch" type="xml">
.. i18n:             <data>
.. i18n:                 <xpath 
.. i18n:                    expr="//field[@name='order_line']/form/field[@name='qty']"
.. i18n:                    position="after">
.. i18n:                    <field name="size"/>
.. i18n:                 </xpath>
.. i18n:                 <xpath 
.. i18n:                    expr="//field[@name='order_line']/tree/field[@name='qty']"
.. i18n:                    position="after">
.. i18n:                    <field name="size"/>
.. i18n:                 </xpath>
.. i18n:             </data>
.. i18n:     </field>
..

.. code-block:: xml

    <record model="ir.ui.view" id="some_inherited_view">
        <field name="name">some.inherited.view</field>
        <field name="type">form</field>
        <field name="model">some.model.with.one2many</field>
        <field name="inherit_id" ref="core_module.some_view"/>
        <field name="arch" type="xml">
            <data>
                <xpath 
                   expr="//field[@name='order_line']/form/field[@name='qty']"
                   position="after">
                   <field name="size"/>
                </xpath>
                <xpath 
                   expr="//field[@name='order_line']/tree/field[@name='qty']"
                   position="after">
                   <field name="size"/>
                </xpath>
            </data>
    </field>

.. i18n: One down side of defining a subview like this is that it can't be inherited on
.. i18n: its own, it can only be inherited with the parent view. Your views will be more
.. i18n: flexible if you define the child views separately and then specify which child
.. i18n: view to use as part of the one2many field.
..

像这样定义一个subview的副作用是，它不能继承自它自己，它只能继承自父类视图。如果你单独定义了子类视图并且指定哪个子类视图来作为one2many字段的一部分使用，这样你的视图将会非常灵活。

.. i18n: Events
.. i18n: ------
..

Events
------

.. i18n: .. _onchange-event-link:
.. i18n: 
.. i18n: On Change
.. i18n: +++++++++
..

.. _onchange-event-link:

On Change
+++++++++

.. i18n: The on_change attribute defines a method that is called when the content of a view field has changed.
..

当一个字段的内容发生改变时，on_change属性定义个方法就会被调用。

.. i18n: This method takes at least arguments: cr, uid, ids, which are the three classical arguments and also the context dictionary. You can add parameters to the method. They must correspond to other fields defined in the view, and must also be defined in the XML with fields defined this way::
.. i18n: 
.. i18n:         <field 
.. i18n:             name="name_of_field" 
.. i18n:             on_change="name_of_method(other_field_1, ..., other_field_n)"/> 
..

这个方法至少有几个参数：cr，uid，ids，这是三个传统的参数并且也在上下文字典中。你需要给方法添加参数。他们必须符合在视图中定义的其他字段，并且必须在XML中以以下的方式定义：::

        <field 
            name="name_of_field" 
            on_change="name_of_method(other_field_1, ..., other_field_n)"/> 

.. i18n: The example below is from the sale order view.
..

下面的是来自销售订单视图中的例子。

.. i18n: You can use the 'context' keyword to access data in the context that can be used as params of the function.::
.. i18n: 
.. i18n:         <field name="shop_id" on_change="onchange_shop_id(shop_id)"/>
..

你可以使用‘context’关键字来访问上下文中的数据，这个上下文可以被用作函数中的参数：::

        <field name="shop_id" on_change="onchange_shop_id(shop_id)"/>

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:         def onchange_shop_id(self, cr, uid, ids, shop_id):
.. i18n: 
.. i18n:             v={} 
.. i18n:             if shop_id:
.. i18n: 
.. i18n:                 shop=self.pool.get('sale.shop').browse(cr,uid,shop_id) 
.. i18n:                 v['project_id']=shop.project_id.id 
.. i18n:                 if shop.pricelist_id.id:
.. i18n: 
.. i18n:                     v['pricelist_id']=shop.pricelist_id.id 
.. i18n: 
.. i18n:                 v['payment_default_id']=shop.payment_default_id.id 
.. i18n: 
.. i18n:             return {'value':v} 
..

.. code-block:: python

        def onchange_shop_id(self, cr, uid, ids, shop_id):

            v={} 
            if shop_id:

                shop=self.pool.get('sale.shop').browse(cr,uid,shop_id) 
                v['project_id']=shop.project_id.id 
                if shop.pricelist_id.id:

                    v['pricelist_id']=shop.pricelist_id.id 

                v['payment_default_id']=shop.payment_default_id.id 

            return {'value':v} 

.. i18n: When editing the shop_id form field, the onchange_shop_id method of the sale_order object is called and returns a dictionary where the 'value' key contains a dictionary of the new value to use in the 'project_id', 'pricelist_id' and 'payment_default_id' fields.
..

当编辑shop_id表单字段时，sale_order对象的onchange_shop_id方法会被调用，并且返回一个字典，其中‘value’关键字包含在’project_id’, ‘pricelist_id’, ‘payment_default_id’字段中新值来使用的字典。

.. i18n: Note that it is possible to change more than just the values of
.. i18n: fields. For example, it is possible to change the value of some fields
.. i18n: and the domain of other fields by returning a value of the form:
.. i18n: return {'domain': d, 'value': value}
..

我们注意到除了字段值，更改更多的东西是可能的。例如，可以更改字段值和其他字段的domain，这个更改通过表单的返回值：return {‘domain’: d, ‘value’: value}

.. i18n: :returns: a dictionary with any mix of the following keys:
..

:returns: 一个字典有以下关键字任意的混合：

.. i18n:     ``domain``
.. i18n:       A mapping of ``{field: domain}``.
..

    ``domain``
      {field: domain}的一个映射

.. i18n:       The returned domains should be set on the fields instead of the
.. i18n:       default ones.
..

      这个返回的domains在字段上设置，而不是之前默认的。

.. i18n:     ``value``
.. i18n:       A mapping of ``{field: value}}``, the values will be set on the
.. i18n:       corresponding fields and may trigger new onchanges or attrs
.. i18n:       changes
..

    ``value``
      field: value}的映射，这个值将会在相对应的字段上设置，可能触发新的改变或是属性的改变。

.. i18n:     ``warning`` A dict with the keys ``title`` and ``message``. Both
.. i18n:       are mandatory. Indicate that an error message should be
.. i18n:       displayed to the user.
..

    ``warning`` 有关键字title和message（两个是必须的）的字典。指出显示给用户的错误信息。
