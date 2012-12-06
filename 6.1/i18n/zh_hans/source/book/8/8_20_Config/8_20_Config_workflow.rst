.. i18n: .. index::
.. i18n:    single: workflow
.. i18n:    single: process
..

.. index::
   single: workflow
   single: process

.. i18n: Configuring Workflows and Processes
.. i18n: ===================================
..

设置工作流和流程
===================================

.. i18n: Workflows represent the company's different document flows. They are completely configurable and
.. i18n: define the path that any individual OpenERP object (such as an order) must follow, depending on the conditions
.. i18n: (for example, an order above a certain value must be approved by a sales director, otherwise by any
.. i18n: sales person, before the delivery can be triggered).
..

工作流代表了公司不同的文档流程。它们是完全可设置的，并且定义任何单个OpenERP对象（比如一个订单）依
据条件必须遵循的路径（例如一个订单在交付前，超过一定的金额必须由销售总监批准，其它情况任何销售人员就可以）。

.. i18n: The figure :ref:`fig-sflow` shows the standard workflow for an order. You can show it from the GTK client
.. i18n: starting with :menuselection:`Sales --> Sales --> Sales Orders`. Select an
.. i18n: order, then go to the top menu :menuselection:`Plugins --> Execute a plugin --> Print Workflow` to
.. i18n: show the workflow below.
..

下图  :ref:`fig-sflow` 展示了一个订单的标准工作流。你能从GTK客户端 用 :menuselection:`销售 --> 销售 --> 销售订单`  显示它，
选择一个 订单，然后进入顶部菜单    :menuselection:`插件 --> 执行一个插件 --> 打印工作流` 

.. i18n: In the web client, you can reach a workflow from the associated cross-company process
.. i18n: (the process itself is reached by going to the sales document and then clicking the 
.. i18n: :guilabel:`Corporate Intelligence` button above it). 
.. i18n: The chapter :ref:`ch-process` provides all of the information
.. i18n: needed to create and modify technical workflows and cross-company processes.
..

In the web client, you can reach a workflow from the associated cross-company process
(the process itself is reached by going to the sales document and then clicking the 
:guilabel:`Corporate Intelligence` button above it). 
The chapter :ref:`ch-process` provides all of the information
needed to create and modify technical workflows and cross-company processes.

  *译注：英文文档描述在6.1 已经不对应，下面根据实际情况重写*
在web客户端，首先要进入开发者模式（右上角 关于，然后 点击 激活开发者模式），在表单标
题（例如销售订单）右侧表单调试视图选择框中，点击“编辑工作流”。
然后在右侧的视图切换中点击 最右的按钮“图形”，即可进入工作流的可视化编辑状态。

.. i18n: .. _fig-sflow:
.. i18n: 
.. i18n: .. figure::  images/sales_workflow.png
.. i18n:    :scale: 65
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Workflow for order SO005*
..

.. _fig-sflow:

.. figure::  images/sales_workflow.png
   :scale: 65
   :align: center

   *订单 SO005 的工作流*

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
