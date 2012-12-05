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
:menuselection:`设置 --> 自定义 --> 用户界面 --> 菜单项` “设置→自定义→用户界面→菜单项”,来变更菜单的显
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

   *Selecting a new welcome page*

.. i18n: The :guilabel:`Home Action` is the menu item that is automatically opened when you first sign on,
.. i18n: and is also reached when you click the :guilabel:`Home` link in the top right toolbar of the web
.. i18n: client. There you can choose any page that you would reach through any menu – one of the dashboards
.. i18n: could be most useful. The :guilabel:`Menu Action` is the one you reach through the menu
.. i18n: :menuselection:`Form --> Menu` in the GTK client. You can choose the
.. i18n: main menu and the dashboards there.
..

The :guilabel:`Home Action` is the menu item that is automatically opened when you first sign on,
and is also reached when you click the :guilabel:`Home` link in the top right toolbar of the web
client. There you can choose any page that you would reach through any menu – one of the dashboards
could be most useful.


The :guilabel:`Menu Action` is the one you reach through the menu
:menuselection:`Form --> Menu` in the GTK client. You can choose the
main menu and the dashboards there.


:guilabel:`主页动作`  是当你第一次登陆是自动打开的菜单项目。当你在在WEB客户端的右上角工具条的 :guilabel:`Home` 链接上面点击时，
也能到达。你这里能选择能通过菜单到达的任意页面 – 一个控制台是最有用的。
在GTK 客户端，通过菜单 :menuselection:`表单 --> 菜单` ， :guilabel:`菜单动作` 可以是你能通过菜单到达的任意一个。


.. i18n: .. tip:: Actions on the Administrator's Menu
.. i18n: 
.. i18n: 	It is very easy to change the welcome page and the menu of the different users.
.. i18n: 	However, you should not change the main administrator's menu because you could make certain menus
.. i18n: 	completely inaccessible by mistake.
..

.. tip:: Actions on the Administrator's Menu

	It is very easy to change the welcome page and the menu of the different users.
	However, you should not change the main administrator's menu because you could make certain menus
	completely inaccessible by mistake.

.. i18n: .. index:: 
.. i18n:    single: field; default value
.. i18n:    
.. i18n: Assigning Default Values to Fields
.. i18n: ----------------------------------
..

.. index:: 
   single: field; default value
   
Assigning Default Values to Fields
----------------------------------

.. i18n: You can quite easily configure the system to put default values in various fields as you open new
.. i18n: forms. This enables you to pre-complete the fields with default data to simplify your users' work in
.. i18n: entering new documents. Let us use the Customer form to demonstrate this feature. Create a new customer
.. i18n: with :guilabel:`Country` set as :guilabel:`New Zealand`
..

You can quite easily configure the system to put default values in various fields as you open new
forms. This enables you to pre-complete the fields with default data to simplify your users' work in
entering new documents. Let us use the Customer form to demonstrate this feature. Create a new customer
with :guilabel:`Country` set as :guilabel:`New Zealand`

.. i18n: * If you are using the web client, click the small button at the right of the :guilabel:`Country`
.. i18n:   field.
.. i18n: 
.. i18n: * If you are using the GTK client, you just need to right-click the mouse while the pointer is in the
.. i18n:   field.
.. i18n:   
.. i18n: Select \ ``Set as default`` \ from the pop-up menu.
.. i18n: An administrator has the choice of making the default work just for that user, or for all users of the database.
..

* If you are using the web client, click the small button at the right of the :guilabel:`Country`
  field.

* If you are using the GTK client, you just need to right-click the mouse while the pointer is in the
  field.
  
Select \ ``Set as default`` \ from the pop-up menu.
An administrator has the choice of making the default work just for that user, or for all users of the database.

.. i18n: .. figure::  images/set_default.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Inserting a new default value*
..

.. figure::  images/set_default.png
   :scale: 75
   :align: center

   *Inserting a new default value*

.. i18n: To check this new configuration, open a new partner form: the field :guilabel:`Country` should now
.. i18n: contain the entry \ ``New Zealand``\  .
..

To check this new configuration, open a new partner form: the field :guilabel:`Country` should now
contain the entry \ ``New Zealand``\  .

.. i18n: This is a very powerful feature! An administrator can use this functionality to redefine the
.. i18n: behavior of your whole system. You can test that in database \ ``openerp_ch13`` \ by opening up a
.. i18n: new :guilabel:`Purchase Order` form, clicking the second tab :guilabel:`Delivery & Invoicing`,
.. i18n: selecting \ ``From Picking`` \ in the :guilabel:`Invoicing Control` field and then making that the
.. i18n: default.
..

This is a very powerful feature! An administrator can use this functionality to redefine the
behavior of your whole system. You can test that in database \ ``openerp_ch13`` \ by opening up a
new :guilabel:`Purchase Order` form, clicking the second tab :guilabel:`Delivery & Invoicing`,
selecting \ ``From Picking`` \ in the :guilabel:`Invoicing Control` field and then making that the
default.

.. i18n: From that moment on, you would automatically create draft purchase invoices only when goods are
.. i18n: received, so you could very easily restrict your accountants from paying any invoices that turn up
.. i18n: until you were sure you had received the goods. It would not stop anyone from selecting another
.. i18n: method of invoice control, but they would start with the default definition.
..

From that moment on, you would automatically create draft purchase invoices only when goods are
received, so you could very easily restrict your accountants from paying any invoices that turn up
until you were sure you had received the goods. It would not stop anyone from selecting another
method of invoice control, but they would start with the default definition.

.. i18n: Changing the Terminology
.. i18n: ------------------------
..

Changing the Terminology
------------------------

.. i18n: You can use OpenERP's language translation functionality to substitute its standard terminology
.. i18n: with terminology that fits your company better. It is quite straightforward to adapt the software
.. i18n: with different terms specific to your industry. Moreover, this can strengthen acceptance of your new
.. i18n: OpenERP system, because everybody will be able to retain their usual vocabulary.
..

You can use OpenERP's language translation functionality to substitute its standard terminology
with terminology that fits your company better. It is quite straightforward to adapt the software
with different terms specific to your industry. Moreover, this can strengthen acceptance of your new
OpenERP system, because everybody will be able to retain their usual vocabulary.

.. i18n: You can do this one of two ways:
..

You can do this one of two ways:

.. i18n: * translate them in a CSV file, which gives you a global overview of all of the system terms so that
.. i18n:   you can search and replace specific occurrences everywhere,
.. i18n: 
.. i18n: * translate the phrases directly in the client, which means that you can change them in their
.. i18n:   context, and that can be helpful to you while you are translating.
..

* translate them in a CSV file, which gives you a global overview of all of the system terms so that
  you can search and replace specific occurrences everywhere,

* translate the phrases directly in the client, which means that you can change them in their
  context, and that can be helpful to you while you are translating.

.. i18n: The same approach is used to translate terms that have not been created yet. This can be useful, for
.. i18n: example, with modules that have not yet been translated into English or any other language that you
.. i18n: want.
..

The same approach is used to translate terms that have not been created yet. This can be useful, for
example, with modules that have not yet been translated into English or any other language that you
want.

.. i18n: .. index::
.. i18n:    single: translation
..

.. index::
   single: translation

.. i18n: Translation through a CSV File
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
..

Translation through a CSV File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: To translate or modify all of the system's phrases, you first have to export a translation file in
.. i18n: CSV form. And to do that, you have to install a language into OpenERP. To load a translation
.. i18n: that already exists in OpenERP, use
.. i18n: :menuselection:`Administration --> Translations --> Load an Official Translation`,
.. i18n: choose a language and then click :guilabel:`Load`.
..

To translate or modify all of the system's phrases, you first have to export a translation file in
CSV form. And to do that, you have to install a language into OpenERP. To load a translation
that already exists in OpenERP, use
:menuselection:`Administration --> Translations --> Load an Official Translation`,
choose a language and then click :guilabel:`Load`.

.. i18n: Then export it using 
.. i18n: :menuselection:`Administration --> Translations --> Import/Export --> Export Translation`. 
.. i18n: Select the language, then the :guilabel:`CSV File` format, then one or more (or all) modules.
.. i18n: Click :guilabel:`Export` to start the export process, then click the small 
.. i18n: :guilabel:`Save As` icon to save the file somewhere.
..

Then export it using 
:menuselection:`Administration --> Translations --> Import/Export --> Export Translation`. 
Select the language, then the :guilabel:`CSV File` format, then one or more (or all) modules.
Click :guilabel:`Export` to start the export process, then click the small 
:guilabel:`Save As` icon to save the file somewhere.

.. i18n: .. note:: UTF-8 Format
.. i18n: 
.. i18n: 	The CSV file is encoded in the UTF-8 format.
.. i18n: 	Make sure that you retain this format when you open the file in a spreadsheet program, because
.. i18n: 	if you **do not** retain it, you risk seeing strange character strings in place of accented
.. i18n: 	characters.
..

.. note:: UTF-8 Format

	The CSV file is encoded in the UTF-8 format.
	Make sure that you retain this format when you open the file in a spreadsheet program, because
	if you **do not** retain it, you risk seeing strange character strings in place of accented
	characters.

.. i18n: .. figure::  images/csv_transl.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *CSV translation file with a translation in view*
..

.. figure::  images/csv_transl.png
   :scale: 75
   :align: center

   *CSV translation file with a translation in view*

.. i18n: The file contains six columns: :guilabel:`module` , 
.. i18n: :guilabel:`type` , :guilabel:`name`, :guilabel:`res_id`,
.. i18n: :guilabel:`src`, and :guilabel:`value`. You have to ensure that the first line, which specifies
.. i18n: these column names, remains untouched. 
..

The file contains six columns: :guilabel:`module` , 
:guilabel:`type` , :guilabel:`name`, :guilabel:`res_id`,
:guilabel:`src`, and :guilabel:`value`. You have to ensure that the first line, which specifies
these column names, remains untouched. 

.. i18n: The :guilabel:`src` field contains the base text in English,
.. i18n: and the :guilabel:`value` field contains a translation into another conventional language or into a
.. i18n: specialist technical phrase. If there is nothing at all in the :guilabel:`value` field then the
.. i18n: English translation will automatically be used on the form you see.
..

The :guilabel:`src` field contains the base text in English,
and the :guilabel:`value` field contains a translation into another conventional language or into a
specialist technical phrase. If there is nothing at all in the :guilabel:`value` field then the
English translation will automatically be used on the form you see.

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

.. tip:: Where Should you Modify the Text?

   Most of the time, you will find the text that you want to modify in several lines of the CSV
   file.
   Which line should you modify?
   Refer to the two columns :guilabel:`type` (in column B) and :guilabel:`name` (in column C).
   Some lines have the name :guilabel:`ir.ui.menu` in the :guilabel:`name` column, which shows that this is a menu entry.
   Others have :guilabel:`selection` in the :guilabel:`type` column, which indicates that you would
   see this entry in a drop-down menu.

.. i18n: You should then load the new file into your OpenERP system using the menu
.. i18n: :menuselection:`Administration --> Translations --> Import/Export --> Import Translation`. 
.. i18n: You have then got two ways forward:
..

You should then load the new file into your OpenERP system using the menu
:menuselection:`Administration --> Translations --> Import/Export --> Import Translation`. 
You have then got two ways forward:

.. i18n: * you can overwrite the previous translation by using the same name as before (so you could have a
.. i18n:   special 'standard French' translation by reusing the :guilabel:`Name` \ ``Français``\   and
.. i18n:   :guilabel:`Code` \ ``fr_FR``\  ),
.. i18n: 
.. i18n: * you could create a new translation file which users can select in their :guilabel:`Preferences`.
..

* you can overwrite the previous translation by using the same name as before (so you could have a
  special 'standard French' translation by reusing the :guilabel:`Name` \ ``Français``\   and
  :guilabel:`Code` \ ``fr_FR``\  ),

* you could create a new translation file which users can select in their :guilabel:`Preferences`.

.. i18n: If you are not connected to the translated language, click :guilabel:`Edit Preferences`, select the
.. i18n: language in :guilabel:`Language` from the :guilabel:`Preferences` tab, and finally click :guilabel:`Save`
.. i18n: to load the new language with its new terminology.
..

If you are not connected to the translated language, click :guilabel:`Edit Preferences`, select the
language in :guilabel:`Language` from the :guilabel:`Preferences` tab, and finally click :guilabel:`Save`
to load the new language with its new terminology.

.. i18n: .. tip:: Partial Translations
.. i18n: 
.. i18n:    You can load a selection of the lines in a translation file by deleting most of the lines in the
.. i18n:    file and then loading back only the changed ones. OpenERP then changes only the uploaded lines
.. i18n:    and leaves the original ones alone.
..

.. tip:: Partial Translations

   You can load a selection of the lines in a translation file by deleting most of the lines in the
   file and then loading back only the changed ones. OpenERP then changes only the uploaded lines
   and leaves the original ones alone.

.. i18n: Changes through the Client Interface
.. i18n: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
..

Changes through the Client Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. i18n: You can also change labels and other screen items on screen in the web client. 
.. i18n: To do that, open the form that you want to translate, then click the 
.. i18n: :guilabel:`Translate` icon to its bottom right. 
.. i18n: You then have the choice of translating:
..

You can also change labels and other screen items on screen in the web client. 
To do that, open the form that you want to translate, then click the 
:guilabel:`Translate` icon to its bottom right. 
You then have the choice of translating:

.. i18n: * the data in the system (contained in the :guilabel:`Fields`),
.. i18n: 
.. i18n: * the field titles (the :guilabel:`Labels`),
.. i18n: 
.. i18n: * all of the :guilabel:`Action` buttons to the right of the form (the :guilabel:`Relates` option),
.. i18n: 
.. i18n: * the terms used in the form :guilabel:`View`.
..

* the data in the system (contained in the :guilabel:`Fields`),

* the field titles (the :guilabel:`Labels`),

* all of the :guilabel:`Action` buttons to the right of the form (the :guilabel:`Relates` option),

* the terms used in the form :guilabel:`View`.

.. i18n: You can modify any of these.
..

You can modify any of these.

.. i18n: The procedure is slightly different using the GTK client. In this you just right-click on a label or button
.. i18n: with the mouse. You can choose to translate the item itself or the whole view.
..

The procedure is slightly different using the GTK client. In this you just right-click on a label or button
with the mouse. You can choose to translate the item itself or the whole view.

.. i18n: This method is simple and quick when you only have a few entries to modify, but it can become
.. i18n: tiresome and you can lose a lot of time if you have got to change some terms across the whole system.
..

This method is simple and quick when you only have a few entries to modify, but it can become
tiresome and you can lose a lot of time if you have got to change some terms across the whole system.

.. i18n: In that case it would be better to use the translation method that employs a CSV file.
..

In that case it would be better to use the translation method that employs a CSV file.

.. i18n: .. tip:: Taking account of Translations
.. i18n: 
.. i18n:    In the GTK client, the modified terms are not updated immediately.
.. i18n:    To see the effects of the modifications, you must close the current window and then reopen the
.. i18n:    form.
..

.. tip:: Taking account of Translations

   In the GTK client, the modified terms are not updated immediately.
   To see the effects of the modifications, you must close the current window and then reopen the
   form.

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
