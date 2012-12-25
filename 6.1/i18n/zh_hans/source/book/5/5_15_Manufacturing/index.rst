.. i18n: .. index::
.. i18n:    single: Manufacturing
.. i18n:    single: production; management
..

.. index::
   single: Manufacturing
   single: production; management

.. i18n: .. _part3-man-manuf:
.. i18n: 
.. i18n: *************************
.. i18n: Defining your Master Data
.. i18n: *************************
..

.. _part3-man-manuf:

*************************
定义主数据
*************************

.. i18n:  *The management of manufacturing described in this chapter covers
.. i18n:  planning, ordering, stocks and the manufacturing or assembly of products from raw materials and
.. i18n:  components.
.. i18n:  It also discusses consumption and production of products, as well as the necessary operations on
.. i18n:  machinery, tools or human resources.*
..

 *不要忘记在第二个选项卡其他信息中设置正确的参数选择一个好的物流和包装策略。在这里，
 我们选择的Invoiche的生产管理本章中介绍的涵盖计划，订货，库存和产品从原材料和零部件的制造
 或组装的。
 此外，还讨论消费和生产的产品，以及必要的操作机器，工具或人力资源.*

.. i18n: Manufacturing management in OpenERP is based on its stock management and equally very
.. i18n: flexible in both its operations and its financial control. It particularly benefits from the use of
.. i18n: double-entry stock management for production orders.
..

OpenERP的生产管理其存货管理的基础上，同样非常
灵活，其业务及财务控制。它特别受益于使用
双项库存管理生产订单.

.. i18n: .. index::
.. i18n:    single: module; mrp
..

.. index::
   single: module; mrp

.. i18n: Manufacturing management is implemented by the :mod:`mrp` module. It is used to transform all
.. i18n: kinds of products:
..

生产管理通过:mod:`mrp` 模块实现. 他用来计算所有种类的产品:

.. i18n: * Assemblies of parts: composite products, soldered or welded products, assemblies, packs,
.. i18n: 
.. i18n: * Machined parts: machining, cutting, planing,
.. i18n: 
.. i18n: * Foundries: clamping, heating,
.. i18n: 
.. i18n: * Mixtures: mixing, chemical processes, distillation.
..

* Assemblies of parts: composite products, soldered or welded products, assemblies, packs,

* Machined parts: machining, cutting, planing,

* Foundries: clamping, heating,

* Mixtures: mixing, chemical processes, distillation.

.. i18n: You will work in two areas: with products in the first part of this chapter, and with operations in the
.. i18n: second part. The management of products depends on the concept of classifications while operations management is related to routing and workcenters.
..

You will work in two areas: with products in the first part of this chapter, and with operations in the
second part. The management of products depends on the concept of classifications while operations management is related to routing and workcenters.

.. i18n: .. index::
.. i18n:    single: bill of materials
..

.. index::
   single: bill of materials

.. i18n: .. note:: Bills of Materials
.. i18n: 
.. i18n:     Bills of Materials, or manufacturing specifications, go by different names depending on their
.. i18n:     application area, for example:
.. i18n: 
.. i18n:     * Food: Recipes,
.. i18n: 
.. i18n:     * Chemicals: Equations,
.. i18n: 
.. i18n:     * Building: Plans.
..

.. note:: Bills of Materials

    Bills of Materials, or manufacturing specifications, go by different names depending on their
    application area, for example:

    * Food: Recipes,

    * Chemicals: Equations,

    * Building: Plans.

.. i18n: For this chapter you should start with a fresh database that includes demo data,
.. i18n: with :mod:`mrp` (``Manufacturing``) and its dependencies installed and a generic chart of accounts configured.
.. i18n: As you will notice, when you select ``Manufacturing`` to be installed, OpenERP will install the linked applications automatically.
..

For this chapter you should start with a fresh database that includes demo data,
with :mod:`mrp` (``Manufacturing``) and its dependencies installed and a generic chart of accounts configured.
As you will notice, when you select ``Manufacturing`` to be installed, OpenERP will install the linked applications automatically.

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <div class="all-toctree">
..

.. raw:: html

    <div class="all-toctree">

.. i18n: .. toctree::
.. i18n: 
.. i18n:    5_15_Master_data
.. i18n:    5_15_Manufacturing
.. i18n:    5_15_Manufacturing_logistic
.. i18n:    5_15_Manufacturing_forecasting
..

.. toctree::

   5_15_Master_data
   5_15_Manufacturing
   5_15_Manufacturing_logistic
   5_15_Manufacturing_forecasting

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     </div>
..

.. raw:: html

    </div>

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
