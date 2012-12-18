.. i18n: =======================
.. i18n: Menu Organization Rules
.. i18n: =======================
..

=======================
菜单组织规则
=======================

.. i18n: Menu organization
.. i18n: +++++++++++++++++
..

菜单组织
+++++++++++++++++

.. i18n: * The first items of the main menu (application management) must be the most useful documents of the application. There are 2 reasons for this: 
.. i18n: 
.. i18n:   * users must have direct and easy access to their documents, usually, most important features which correspond to daily operations.
.. i18n:   * In web client, this first menu is unfolded by default
..

* 应用套件的第一个菜单往往是最主要的功能。理由如下： 
  * 用户可以方便直接读取他们的文档，通常来说，是和日常工作对应的主要功能
  * 在Web客户端，第一个菜单默认情况下是打开的


.. i18n:     .. figure:: Pictures/webmenu.png
.. i18n:        :align: center
..

    .. figure:: Pictures/webmenu.png
       :align: center

.. i18n: * If the application contains the object “res.partner” it is always after the main menu. Because, it is important to have easy access to the suppliers in “purchases” or the customers in “sales”. 
.. i18n: * “Configuration” is always the last menu item in an application. By default, only “admin / configuration” has access to this menu. 
.. i18n: * “Reporting” is always before “Configuration”. For managers it is the last item.
.. i18n: * If the application contains the object “res.product”, it is always before “Reporting” (from user side, it is the last item)
.. i18n: * the invoice object; if there is one in the application, it must be before “Products)
.. i18n: * All other menus are organized in a logical order. For example, in “Human Resources”, user have generally more often the need for “Time Tracking” than “Expenses”. So “Time Tracking” is placed before “Expenses”
..

* 如果应用套件包含 “res.partner” 对象，往往是放在主菜单之后。无论是在销售中的“客户”或采购当中的“供应商”，都是非常重要的。
* “设置” 菜单往往放在主菜单的最后一项。只有“admin / configuration” 组的用户才有权限操作。
* “报表” 菜单往往是在 “设置” 菜单之前。对于经理来说是最后一项菜单。
* 如果应用套件包含 “res.product” 对象，往往是放在 “报表” 项之前（对普通用来来说，这是最后一项菜单）。
* 如果应用套件有“invoice（发票）” 对象，那必须放在 “产品” 菜单之前。
* 其他菜单就按照一定的逻辑顺序排列。例如，在 “人力资源” 中，时间追踪要比费用更常用，因此时间追踪会放在费用之前。

.. i18n: To summarize menus have to look like :
..

总结下菜单的样子：

.. i18n: * Main application 
.. i18n: * (Address book)
.. i18n: * …
.. i18n: * (Billings)
.. i18n: * (Product)
.. i18n: * Reporting
.. i18n: * Configuration
..

* 应用的主菜单 
* (地址薄)
* …
* (费用)
* (产品)
* 报表
* 设置

.. i18n: Menu terminology
.. i18n: ++++++++++++++++
..

菜单用词
++++++++++++++++

.. i18n: The name must be short and explicit. Firstly, it must be short because in web client, main menus are organized on the top, in a horizontal bar. So it cannot take too much space. For instance we use “Purchases”, not “Purchases Management”, to minimise the space taken in the menu. 
..

菜单名称必须言简意赅。首先，在 Web 客户端主菜单是位于页面上部的水平栏里，因此不能占用太多地方。所以，我们用 “采购” 而不是 “采购管理”，这样可以缩短单词长度。

.. i18n: .. figure:: Pictures/menubar.png
.. i18n:    :align: center
..

.. figure:: Pictures/menubar.png
   :align: center

.. i18n: Secondly, used terminology must be linked to the application and explicit to it. For example, res.partner object is named “Customer” in “sales” and “Supplier” in “Purchase”.
..

其次，菜单名称必须符合应用的上下文。比如，res.partner 对象在 “销售” 中是 “客户”，而在 “采购” 中是 “供应商”。
