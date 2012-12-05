.. index::
   single: Configuration
   single: Administration

.. _ch-config:

******************************
配置和系统管理
******************************

 *本章的对象为OpenERP系统管理员.
 你将学会如何配置, 使它适应公司及所有用户的需求.*

OpenERP通过用户界面提供极大灵活性来配置系统,可以定义界面外观,以
普通操作模式或多种查询功能友好的满足用户操作习惯.

每个用户可以自行安排他们的欢迎页面和他们自己的菜单，（OpenERP的
主菜单可以完全重组）。你还可以通过在欢迎页面为每个用户指定他们自己的控制台来实现个性的OpenERP，提供他们最新的信息。每次登录，他们马上就可以看到最相关的信息。

访问权限的管理让您指定某些功能给特定的系统用户。你也可以把用
户加入到组中，通过管理组，可以更方便的管理多个权限相同的用户。
你也能指派组给用户，让他们能切换系统单据的状态 (比如
用来批准员工的报销请求)。

.. index::
   single: configuration
   single: configuration; parametrization
   single: configuration; personalization
   single: configuration; customization
   single: configuration; setup
..

.. note:: 设置，参数化，个性化，自定义

	词语*个性化*有时被用来在这本书里你希望找到*配置*或*自定义*的地方。.

	*自定义*一般是指一些需要相当多的技术工作的事情（如建立专门的代码模块）和创建一个非标准的系统。

	*配置*是不太激进的 - 这是设置该软件的所有参数来适合你的系统需求的一
        般流程（通常被称为*参数化*或*设置*）。按照惯例，配置也是OpenERP的每个
        顶层菜单下面的子菜单的名称，只有该部分的管理员用户能够访问。

	*个性化*只是 为个人或公司的具体运作和/或 格式上的愿望 形成系统的配置设置选项的子集。.

使用*OpenOffice Report Designer* 模块(:mod:`base_report_designer`),，你可以改变由系统产生的任何报告的任何部分。系统管理设置员可以配置设置每个报告，修改它的布局和风格，甚至包括系统提供的数据。

.. note::  The OpenOffice Report Designer


         OpenOffice的在报表设计器插件，使你不仅仅配置设置OpenERP的基本产品的报告，也能建
         立全新的报表模板。当用户使用OpenERP的客户界面，OpenOffice可以创建一个报表模板来访
         问OpenERP文档类型的所有可用的数据。

         你可以轻松地创建传真文件、报价单，或任何其他的商业文件。此功能对于需要发送很多
         提案给客户的销售人员非常有用，它可大大提高你的销售人员的工作效率。

最后，你将看到如何自动导入你的数据到OpenERP，只通过很简单的步骤。

在本章你将一个包含演示数据的全新的数据库开始，这个数据库已安装了销售 :mod:`sale` 和它依赖的模块，另外还没有进行特别的账户配置设置。


.. raw:: html

    <div class="all-toctree">

.. toctree::

    8_20_Config_module
    8_20_Config_menu
    8_20_Config_accessRights
    8_20_Config_workflow
    8_20_Config_reports
    8_20_Config_import_export

.. raw:: html

    </div>
    
.. Copyright © Open Object Press. All rights reserved.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the OpenERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. Published by Open Object Press, Grand Rosière, Belgium

