.. i18n: .. index::
.. i18n:    pair: configuring; module
..

.. index::
   pair: configuring; module

.. i18n: Creating a Configuration Module
.. i18n: ===============================
..

创建一个设置模块
===============================

.. i18n: It is very helpful to be able to backup your specific configuration settings in an OpenERP module
.. i18n: dedicated just to that. This enables you to:
..

备份你刚刚做的Openerp模块设置，对你来说非常有用的,它使您能够:

.. i18n: * automatically duplicate the configuration settings by installing the module in another database,
.. i18n: 
.. i18n: * reinstall a clean database with your own configuration, in case you have problems with the initial
.. i18n:   configuration,
.. i18n: 
.. i18n: * simplify migrations. If you have modified some elements of the basic configuration, there is a risk
.. i18n:   in returning them to their original state after the migration, unless you have saved the modifications
.. i18n:   in a module.
..

* 可通过其它数据库的设置信息自动安装模块

* 假如你自己的设置有问题，可用初始设置重新安装一个干净的数据库。

* 简化升级, 如果你修改了一些基本设置元素,这会对你还原初始状态造成风险, 但是如果你备份了修改信息将会有效避免风险.


.. i18n: .. index::
.. i18n:    single: module; base_module_record
..

.. index::
   single: module; base_module_record

.. i18n: Start by installing the module :mod:`base_module_record` in the usual way from
.. i18n: :menuselection:`Administration --> Modules --> Modules`. Manually make all your
.. i18n: configuration changes through the user
.. i18n: interface as you would normally do (such as menu management, dashboard assignments, screen
.. i18n: configuration, new reports, and access rights management – details of some of these possibilities
.. i18n: are described later in this chapter).
..

用通常的方式开始安装模块 :mod:`base_module_record` ，从菜单 :menuselection:`设置(Administration) --> 模块(Modules) --> 模块(Modules)`. 
通过用户界面像往常一样手工使您的所有设置变化（例如：菜单管理，仪表台控制，屏幕设置，新报表和访问权限管理 – 一些细节将在本章后面说明）。

.. i18n: Then start recording
.. i18n: your data using the menu :menuselection:`Administration --> Customization --> Module Creation -->
.. i18n: Export Customizations As a Module`. This opens a wizard through which you may select the date to record
.. i18n: from, choose records that have been \ ``Created`` \, \ ``Modified`` \ or both \ ``Created & Modified`` \.
.. i18n: You have to select the objects for recording and then start recording by clicking :guilabel:`Record`.
.. i18n: After the recording operation is complete, a dialog box appears giving you the opportunity to save
.. i18n: the recorded module at a desired location.
..

开始记录你的数据使用菜单 :menuselection:`设置(Administration) --> 自定义(Customization) --> 模块创建(Module Creation) -->导出自定义模块(Export Customizations As a Module)` 。
打开向导,选择要记录的数据，你可以选择录制日期,记录类型可以选择\ ``创建`` \, \ ``修改`` \或者\ ``创建和修改`` \.
你必须选择记录对象,然后点击 :guilabel:`记录` 开始录制。录制操作完成后,你需要在弹出对话框中选择保存位置.


.. i18n: OpenERP then creates a ZIP file for you containing all of the modifications you made while you
.. i18n: were carrying out your configuration work. You could reinstall this module on other databases.
.. i18n: This could turn out to be useful if you want to install a
.. i18n: test server for your company's users and give them the same configuration as the production server.
..

OpenERP会记录所有的设置工作并保存成为ZIP文件,你可以在其它数据库中重新安装.这对你安装测试
服务器,并保留所有用户的设置信息到生成服务器中,非常有用.

.. i18n: To install a new module saved in ZIP file form, use the menu :menuselection:`Administration -->
.. i18n: Modules --> Import Module`.
..

要安装一个保存在zip文件格式的模块，使用菜单  :menuselection:`设置(Administration) --> 模块(Modules) --> 导入模块(Import Module)`.

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
