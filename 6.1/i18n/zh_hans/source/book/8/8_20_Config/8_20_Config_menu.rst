.. i18n: .. index:: 
.. i18n:    single: menu; configuring
..

.. index:: 
   single: menu; configuring

.. i18n: Configuring the Menu
.. i18n: ====================
..

设置菜单
====================

.. i18n: OpenERP's menu organization is not subject to any restriction, so you can modify the whole
.. i18n: structure, the terminology and all access rights to it to meet your specific needs in the best
.. i18n: possible way. However, before you do all that and just as you would for any other customizable
.. i18n: software, you should balance both the benefits you see in such changes and the costs, such as the
.. i18n: need to train users, to maintain new documentation and to continue the alterations through
.. i18n: subsequent versions of the software.
..

OpenERP的菜单组织不受任何限制，所以你可以修改整体结构、术语和所有访问权限，它尽最大可能满足您的特定需求。
然而，你做这一切之前，就像任何其他的可自定义的软件，你应该平衡考虑这种变化的好处和成本，比如需要培训用户，
要维护新的文件，以及继续修改这个软件的后续版本。

.. i18n: This section describes how to proceed to change the structure of the menu and the welcome page, to
.. i18n: configure the terminology of the menus and forms in the user interface, and for managing users'
.. i18n: access rights to the menus and the various underlying business objects.
..

本节介绍如何更改菜单结构和欢迎页面，设置在用户界面中菜单和表单的术语，管理用户的菜单访问权限的以及各项
基础业务对象。

.. i18n: .. index::
.. i18n:    single: menu; duplicating
..

.. index::
   single: menu; duplicating

.. i18n: Changing the Menu
.. i18n: -----------------
..

修改菜单
-----------------

.. i18n: You can change the way menu items appear and the actions they trigger by using the menu
.. i18n: :menuselection:`Administration --> Customization --> User Interface --> Menu Items`. This
.. i18n: opens a search view where you may locate the menu item to be edited by entering its entire
.. i18n: name (specified as menu hierarchy) in the :guilabel:`Menu` field or specifying its immediate
.. i18n: parent menu name in :guilabel:`Parent Menu`.
..


你可以改变菜单项出现的方式和他们触发的动作，使用菜单
:menuselection:`设置 --> 自定义 --> 用户界面 --> 菜单项` ,来变更菜单的显
示方式及触发动作。
在搜索视图中, 在:guilabel:`菜单` 字段输入整个名称找到你要编辑的菜单项目（如菜单层次结构中
指定），或在 :guilabel:`上级菜单` 指定上级菜单名称.



.. i18n: As an example, locate the menu item \ ``Administration/Translations/Import / Export/Export Translation`` \
.. i18n: and click on this entry to open its corresponding form.
.. i18n: You could now edit this form (**but do not do that, read the next paragraph first!**) – change 
.. i18n: its :guilabel:`Parent Menu`, which moves the entry to a
.. i18n: different part of the menu system; edit its :guilabel:`Menu` name to change how it appears in the
.. i18n: menu tree, or give it a new :guilabel:`Icon`. Or you could give it a new :guilabel:`Action` entirely
.. i18n: (but this would lose the point of this particular exercise).
..


例如: 找到菜单项  \ ``设置/翻译/导入/导出 翻译`` \ 
点击该项打开响应的表单,你能编辑这个表单 (**请先不要这样操作,请先阅读下
一段**), 改变它的 :guilabel:`上级菜单` ，并移动至菜单系统任何一个位置; 编辑 :guilabel:`菜单`  可以改变
菜单树显示的内容，或者给一个新的 :guilabel:`图标` 。或者你能给一个全新的 :guilabel:`动作` (但会导致错误的操作)



.. i18n: Instead of editing this form, which is the original menu entry, duplicate it. With the web
.. i18n: client you must first make the form read-only by clicking the :guilabel:`Cancel` button, then you
.. i18n: click the :guilabel:`Duplicate` button that appears (in the GTK client, click :menuselection:`Form
.. i18n: --> Duplicate`  from the top menu). The form that remains is now the duplicate entry, not the
.. i18n: original.
..

在编辑原始表单内容前,请先复制。在WEB客户端,你点击:guilabel:`取消` 按钮使得表单只读,然后点击”复制”按钮
（在GTK客户端，单击从顶部的菜单 :menuselection:`表单
--> 复制` ）.你看到是复制后的,而不是原来的菜单内容.


.. i18n: To move this duplicate entry, change the :guilabel:`Parent Menu` field by deleting what is there and
.. i18n: replacing it with another menu that everyone can see, such as :guilabel:`Tools` or :guilabel:`Human
.. i18n: Resources`, and make sure that the entry moves to the end of the menu list by replacing the
.. i18n: :guilabel:`Sequence` with \ ``99``\  . You can experiment with icons if you like. Save the form and
.. i18n: then reload the page to see the results.
..

为了移动复制项, 通过删除或者用其它每人能看到的菜单（比如 :guilabel:`工具` 或者   :guilabel:`人力资源`）
替换的方式改变 :guilabel:`上级菜单` 字段 。
并确保该项目移动到菜单的尾部,用 \ ``99``\   替换 :guilabel:`序列`  字段。你
可尝试修改你喜欢的图标并保存,并刷新页面查看结果.


.. i18n: .. tip:: Duplicating the Menu
.. i18n: 
.. i18n:    If you are planning to modify a menu, you should duplicate it first.
.. i18n:    In this way you will always keep a link to the original menu that works if you need it to.
..

.. tip:: 复制菜单

   如果你打算修改菜单,请先复制. 这可以保证你找回原始的菜单信息.

.. i18n: .. index:: 
.. i18n:    single: welcome page
.. i18n:    
.. i18n: Personalizing the Welcome Page for Each User
.. i18n: --------------------------------------------
..

.. index:: 
   single: welcome page
   
为每个用户个性化欢迎页面
--------------------------------------------

.. i18n: The administrator can change both the welcome page and the main menu page individually for each user
.. i18n: of the system, and can adapt OpenERP to each role in the company to best fit the needs of everyone.
..

管理员能为每个用户设置欢迎页面和主菜单,以满足不同角色的需求.

.. i18n: To make modifications for a particular user, edit the user configuration again in
.. i18n: :menuselection:`Administration --> Users --> Users`. Open the form for a particular user, and select
.. i18n: different menu entries for the two fields :guilabel:`Home Action` and :guilabel:`Menu Action`.
..

使用 :menuselection:`设置 --> 用户 --> 用户`  为特定用户修改设置.打开特定用户的表单,
为 :guilabel:`主页动作` 和 :guilabel:`菜单动作` 字段选择不同的菜单项目。

.. i18n: .. figure::  images/new_home.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Selecting a new welcome page*
..

.. figure::  images/new_home.png
   :scale: 75
   :align: center

   *选择一个新的欢迎页*

.. i18n: The :guilabel:`Home Action` is the menu item that is automatically opened when you first sign on,
.. i18n: and is also reached when you click the :guilabel:`Home` link in the top right toolbar of the web
.. i18n: client. There you can choose any page that you would reach through any menu – one of the dashboards
.. i18n: could be most useful. The :guilabel:`Menu Action` is the one you reach through the menu
.. i18n: :menuselection:`Form --> Menu` in the GTK client. You can choose the
.. i18n: main menu and the dashboards there.
..

:guilabel:`主页动作`  是当你第一次登陆是自动打开的菜单项目。当你在在WEB客户端的右上角工具条的 :guilabel:`Home` 链接上面点击时，
也能到达。你这里能选择能通过菜单到达的任意页面 – 一个控制台是最有用的。
在GTK 客户端，通过菜单 :menuselection:`表单 --> 菜单` ， :guilabel:`菜单动作` 可以是你能通过菜单到达的任意一个。


.. i18n: .. tip:: Actions on the Administrator's Menu
.. i18n: 
.. i18n: 	It is very easy to change the welcome page and the menu of the different users.
.. i18n: 	However, you should not change the main administrator's menu because you could make certain menus
.. i18n: 	completely inaccessible by mistake.
..

.. tip:: 管理员菜单的动作

	非常容易改变不同用户的欢迎页面和菜单。然而，你不能改变管理员的菜单，因为你可以错误地使某些菜单完全无法访问

.. i18n: .. index:: 
.. i18n:    single: field; default value
.. i18n:    
.. i18n: Assigning Default Values to Fields
.. i18n: ----------------------------------
..

.. index:: 
   single: field; default value
   
为字段指定默认值
----------------------------------

.. i18n: You can quite easily configure the system to put default values in various fields as you open new
.. i18n: forms. This enables you to pre-complete the fields with default data to simplify your users' work in
.. i18n: entering new documents. Let us use the Customer form to demonstrate this feature. Create a new customer
.. i18n: with :guilabel:`Country` set as :guilabel:`New Zealand`
..

你能很容易地设置系统在打开新表单时的各个字段的默认值。用默认数据预先完成这些字段，可简
化用户在输入新单据的工作。

让我们用“客户”表单来演示这个特性。创建一个新客户时 将:guilabel:`国家` 字段设置为  :guilabel:`新西兰` 

.. i18n: * If you are using the web client, click the small button at the right of the :guilabel:`Country`
.. i18n:   field.
.. i18n: 
.. i18n: * If you are using the GTK client, you just need to right-click the mouse while the pointer is in the
.. i18n:   field.
.. i18n:   
.. i18n: Select \ ``Set as default`` \ from the pop-up menu.
.. i18n: An administrator has the choice of making the default work just for that user, or for all users of the database.
..

* 如果你使用web 客户端。单击 :guilabel:`国家` 字段右边的小按钮。

* 如果你使用 GTK 客户端，鼠标右击字段。
  
从弹出菜单选择 \ ``设置默认值`` \ 。
管理能选择默认值是对指定用户有效还是对数据库中的所有用户有效.

.. i18n: .. figure::  images/set_default.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Inserting a new default value*
..

.. figure::  images/set_default.png
   :scale: 75
   :align: center

   *插入一个新的默认值*

.. i18n: To check this new configuration, open a new partner form: the field :guilabel:`Country` should now
.. i18n: contain the entry \ ``New Zealand``\  .
..

要测试这个新的配置，打开一个合作伙伴表单，在字段 :guilabel:`国家` 现在有了\ ``新西兰``\ 


.. i18n: This is a very powerful feature! An administrator can use this functionality to redefine the
.. i18n: behavior of your whole system. You can test that in database \ ``openerp_ch13`` \ by opening up a
.. i18n: new :guilabel:`Purchase Order` form, clicking the second tab :guilabel:`Delivery & Invoicing`,
.. i18n: selecting \ ``From Picking`` \ in the :guilabel:`Invoicing Control` field and then making that the
.. i18n: default.
..

这是一个非常强大的特性，管理员能用这个功能重新定义整个系统的行为。你能在数据库  \ ``openerp_ch13`` \  
测试这个，通过打开一
个新的:guilabel:`采购订单` ，点击第二个选项卡  :guilabel:`交付和开发票` ， 在  \ ``开票方式`` \  
字段选择  \ ``从收货`` \ 为默认值。


.. i18n: From that moment on, you would automatically create draft purchase invoices only when goods are
.. i18n: received, so you could very easily restrict your accountants from paying any invoices that turn up
.. i18n: until you were sure you had received the goods. It would not stop anyone from selecting another
.. i18n: method of invoice control, but they would start with the default definition.
..

从这一刻起，只有当货物被收到时，你将自动创建采购发票草稿，所以你可以很容易地限制你的会计师支付任何发票，
直到你确信你已经收到货物。他不会阻止选择其它的发票控制方法，但他们将从定义的默认值开始

   *（译注：测试中发现开票方式字段 并不能设置默认值，该字段右边没有小按钮）*

.. i18n: Changing the Terminology
.. i18n: ------------------------
..

更改术语
------------------------

.. i18n: You can use OpenERP's language translation functionality to substitute its standard terminology
.. i18n: with terminology that fits your company better. It is quite straightforward to adapt the software
.. i18n: with different terms specific to your industry. Moreover, this can strengthen acceptance of your new
.. i18n: OpenERP system, because everybody will be able to retain their usual vocabulary.
..

你可以使用OpenERP的语言翻译功能，用更好适合你的公司的术语来取代标准术语。这是很简单的，软件以适应不同的条款
针对具体的行业。此外，这可以增强新的OpenERP系统的接受程度，因为每个人都将能够保持其一贯的词汇。

.. i18n: You can do this one of two ways:
..

你有两条途径做这些：:

.. i18n: * translate them in a CSV file, which gives you a global overview of all of the system terms so that
.. i18n:   you can search and replace specific occurrences everywhere,
.. i18n: 
.. i18n: * translate the phrases directly in the client, which means that you can change them in their
.. i18n:   context, and that can be helpful to you while you are translating.
..

* 在CSV文件里翻译他们，他给你一个全局的概况，这样你能搜索和替换各处的特定术语。
* 直接在客户端翻译短语，意味你能在上下文里修改他们，当你翻译的时候给你很好的帮助。


.. i18n: The same approach is used to translate terms that have not been created yet. This can be useful, for
.. i18n: example, with modules that have not yet been translated into English or any other language that you
.. i18n: want.
..

同样的方法用来翻译那些尚未创建的术语。这是有用的，例如，那些模块还没有被翻译为英语或者其它任何你要的语言

.. i18n: .. index::
.. i18n:    single: translation
..

.. index::
   single: translation

.. i18n: Translation through a CSV File
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
..

通过CSV文件翻译
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: To translate or modify all of the system's phrases, you first have to export a translation file in
.. i18n: CSV form. And to do that, you have to install a language into OpenERP. To load a translation
.. i18n: that already exists in OpenERP, use
.. i18n: :menuselection:`Administration --> Translations --> Load an Official Translation`,
.. i18n: choose a language and then click :guilabel:`Load`.
..


要翻译或者修改所有系统短语，你首先要导出一个翻译文件到CSV表单。要做这些，你需要安装
一个语言进入OpenERP。要装入一个OpenERP已存在的翻译，
使用 :menuselection:`设置 --> 翻译 --> 装入一个官方翻译` ，选择语言，然后点击  :guilabel:`装入`。

.. i18n: Then export it using 
.. i18n: :menuselection:`Administration --> Translations --> Import/Export --> Export Translation`. 
.. i18n: Select the language, then the :guilabel:`CSV File` format, then one or more (or all) modules.
.. i18n: Click :guilabel:`Export` to start the export process, then click the small 
.. i18n: :guilabel:`Save As` icon to save the file somewhere.
..

然后导出它，使用 :menuselection:`设置 --> 翻译 --> 导入/导出--> 导出 翻译` ，选择语言，CSV 文件格式，
然后选择 一个或多个（或全部）模块。点击:guilabel:`导出` 开始导出过程，
然后点击 小的 :guilabel:`保存为` ，保存文件到某个地方。


.. i18n: .. note:: UTF-8 Format
.. i18n: 
.. i18n: 	The CSV file is encoded in the UTF-8 format.
.. i18n: 	Make sure that you retain this format when you open the file in a spreadsheet program, because
.. i18n: 	if you **do not** retain it, you risk seeing strange character strings in place of accented
.. i18n: 	characters.
..

.. note:: UTF-8 格式

	这个CSV文件用UTF-8格式编码。要确保你在电子表格程序中打开这个文件是保留这个格式，因为你如果**不保留**，
        你可能会看到奇怪的乱码（重音符）

.. i18n: .. figure::  images/csv_transl.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *CSV translation file with a translation in view*
..

.. figure::  images/csv_transl.png
   :scale: 75
   :align: center

   *在CSV文件的翻译视图*

.. i18n: The file contains six columns: :guilabel:`module` , 
.. i18n: :guilabel:`type` , :guilabel:`name`, :guilabel:`res_id`,
.. i18n: :guilabel:`src`, and :guilabel:`value`. You have to ensure that the first line, which specifies
.. i18n: these column names, remains untouched. 
..

这个文件包含了6列：: :guilabel:`module` , 
:guilabel:`type` , :guilabel:`name`, :guilabel:`res_id`,
:guilabel:`src`, and :guilabel:`value`. 你必须确保第一行包含了这些列名，保持不变。

.. i18n: The :guilabel:`src` field contains the base text in English,
.. i18n: and the :guilabel:`value` field contains a translation into another conventional language or into a
.. i18n: specialist technical phrase. If there is nothing at all in the :guilabel:`value` field then the
.. i18n: English translation will automatically be used on the form you see.
..

:guilabel:`src`  字段包含了英语的基础文本，:guilabel:`value`  字段包含了翻译成另一个传统的语言或专业技术短语。
如果 :guilabel:`value`  字段没有内容,英语基础文本将会做为默认显示。

.. i18n: .. tip:: Where Should you Modify the Text?
.. i18n: 
.. i18n:    Most of the time, you will find the text that you want to modify in several lines of the CSV
.. i18n:    file.
.. i18n:    Which line should you modify?
.. i18n:    Refer to the two columns :guilabel:`type` (in column B) and :guilabel:`name` (in column C).
.. i18n:    Some lines have the name :guilabel:`ir.ui.menu` in the :guilabel:`name` column, which shows that this is a menu entry.
.. i18n:    Others have :guilabel:`selection` in the :guilabel:`type` column, which indicates that you would
.. i18n:    see this entry in a drop-down menu.
..

.. tip:: 你应该在哪里修改文本？?

   大部分时间，你会发现要修改的文字在CSV文件中的好几行。
   你应该修改哪一行？
   参考这两列：:guilabel:`type`（B列）
   和:guilabel:`name` （C列）。有些行在 :guilabel:`name` 列有名称 :guilabel:`ir.ui.menu`，表明这是
   一个菜单项的名。
   另外在:guilabel:`type`列有:guilabel:`selection` ，这表明，你会在一个下拉菜单项看到这个项目。



.. i18n: You should then load the new file into your OpenERP system using the menu
.. i18n: :menuselection:`Administration --> Translations --> Import/Export --> Import Translation`. 
.. i18n: You have then got two ways forward:
..
  

然后你要装入这个新文件到你的OpenERP系统中，使用菜单 :menuselection:`设置 --> 翻译 --> 导入/导出 --> 导入翻译`
。之后你有两种方法：


.. i18n: * you can overwrite the previous translation by using the same name as before (so you could have a
.. i18n:   special 'standard French' translation by reusing the :guilabel:`Name` \ ``Français``\   and
.. i18n:   :guilabel:`Code` \ ``fr_FR``\  ),
.. i18n: 
.. i18n: * you could create a new translation file which users can select in their :guilabel:`Preferences`.
..


* 你能使用相同的名称覆盖以前的翻译（所以，重新使用名称 :guilabel:`Name` \ ``Français``\  和代码 :guilabel:`Code` \ ``fr_FR``\  ，你能有一个特殊的‘standard French’翻译）

* 你能创建一个新的翻译文件，用户可以在“用户喜好”中选择。

.. i18n: If you are not connected to the translated language, click :guilabel:`Edit Preferences`, select the
.. i18n: language in :guilabel:`Language` from the :guilabel:`Preferences` tab, and finally click :guilabel:`Save`
.. i18n: to load the new language with its new terminology.
..

如果您没有连接到翻译的语言，单击  :guilabel:`编辑首选项` “”，从 :guilabel:`Preferences` 标签的 :guilabel:`语言` 字段选择语言，最后点击:guilabel:`保存` ，装入新的语言，用新的术语。


.. i18n: .. tip:: Partial Translations
.. i18n: 
.. i18n:    You can load a selection of the lines in a translation file by deleting most of the lines in the
.. i18n:    file and then loading back only the changed ones. OpenERP then changes only the uploaded lines
.. i18n:    and leaves the original ones alone.
..

.. tip:: 部分翻译

   你可以选择翻译部分行，删去文件中的大部分行，然后只装入改变后的行。OpenERP只修改上传的行，其它的保留原样。

.. i18n: Changes through the Client Interface
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
..

通过客户端界面修改
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: You can also change labels and other screen items on screen in the web client. 
.. i18n: To do that, open the form that you want to translate, then click the 
.. i18n: :guilabel:`Translate` icon to its bottom right. 
.. i18n: You then have the choice of translating:
..

你还能通过客户端界面在WEB客户端改变标签和其它屏幕上的项目。要做到这一点，打开你要翻译的表单，然后点击其右下角的
:guilabel:`翻译`  图标。
然后，你有的翻译选择：

.. i18n: * the data in the system (contained in the :guilabel:`Fields`),
.. i18n: 
.. i18n: * the field titles (the :guilabel:`Labels`),
.. i18n: 
.. i18n: * all of the :guilabel:`Action` buttons to the right of the form (the :guilabel:`Relates` option),
.. i18n: 
.. i18n: * the terms used in the form :guilabel:`View`.
..

* 系统中的数据(包含在:guilabel:`字段`里) 

* 字段标题 ( :guilabel:`标签`),

* 表单右侧所有的:guilabel:`动作`按钮（:guilabel:`关联`的选项）

* 在表单 :guilabel:`视图` 中的术语。

.. i18n: You can modify any of these.
..

你能修改这些中任意一项。

.. i18n: The procedure is slightly different using the GTK client. In this you just right-click on a label or button
.. i18n: with the mouse. You can choose to translate the item itself or the whole view.
..

使用GTK的客户端的过程略有不同。在此，你只是一个选项卡或按钮，用鼠标右键单击。你可以选择翻译项目本身或整个视图。

.. i18n: This method is simple and quick when you only have a few entries to modify, but it can become
.. i18n: tiresome and you can lose a lot of time if you have got to change some terms across the whole system.
..

当你只有几个项目要修改，这个方法是简单和快速的。但是如果要修改贯穿于整个系统中的术语，这将变得厌烦，要花费很多时间。

.. i18n: In that case it would be better to use the translation method that employs a CSV file.
..

这种情况下，更好的方法就是采用CSV文件的翻译方法。

.. i18n: .. tip:: Taking account of Translations
.. i18n: 
.. i18n:    In the GTK client, the modified terms are not updated immediately.
.. i18n:    To see the effects of the modifications, you must close the current window and then reopen the
.. i18n:    form.
..

.. tip:: 译文的考虑

   在 GTK 客户端，修改的属于并不会立即生效,
   要看到修改的效果，必须关掉当前的窗口，并且再次打开表单。

.. i18n: .. Copyright © Open Object Press. All rights reserved.
..

.. Copyright © Open Object Press. All rights reserved.

.. i18n: .. You may take electronic copy of this publication and distribute it if you don't
.. i18n: .. change the content. You can also print a copy to be read by yourself only.
..

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. i18n: .. We have contracts with different publishers in different countries to sell and
.. i18n: .. distribute paper or electronic based versions of this book (translated or not)
.. i18n: .. in bookstores. This helps to distribute and promote the OpenERP product. It
.. i18n: .. also helps us to create incentives to pay contributors and authors using author
.. i18n: .. rights of these sales.
..

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the OpenERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. i18n: .. Due to this, grants to translate, modify or sell this book are strictly
.. i18n: .. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. i18n: .. written authorisation for this.
..

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. i18n: .. Many of the designations used by manufacturers and suppliers to distinguish their
.. i18n: .. products are claimed as trademarks. Where those designations appear in this book,
.. i18n: .. and Open Object Press was aware of a trademark claim, the designations have been
.. i18n: .. printed in initial capitals.
..

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. i18n: .. While every precaution has been taken in the preparation of this book, the publisher
.. i18n: .. and the authors assume no responsibility for errors or omissions, or for damages
.. i18n: .. resulting from the use of the information contained herein.
..

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. i18n: .. Published by Open Object Press, Grand Rosière, Belgium
..

.. Published by Open Object Press, Grand Rosière, Belgium
