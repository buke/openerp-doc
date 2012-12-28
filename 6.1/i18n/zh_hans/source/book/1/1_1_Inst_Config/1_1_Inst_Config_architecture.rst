.. i18n: .. index::
.. i18n:    single: architecture; OpenERP
..

.. index::
   single: architecture; OpenERP

.. i18n: The Architecture of OpenERP
.. i18n: ===========================
..

OpenERP 架构
===========================

.. i18n: To access OpenERP you can:
..

要使用 OpenERP ，你可以:

.. i18n: * use a web browser pointed at the OpenERP server, or
.. i18n: 
.. i18n: * use an application client (the GTK client) installed on each computer.
..

* 使用浏览器指向 OpenERP 服务器，或是

* 使用在电脑上安装的应用程序客户端(GTK)。

.. i18n: Both access methods give similar facilities, and you can use both on
.. i18n: the same server at the same time. It is best to use the web browser if the
.. i18n: OpenERP server is some distance away (such as on another continent) because
.. i18n: it is more tolerant of time delays between the two than the GTK client is. The
.. i18n: web client is also easier to maintain, because it is generally already installed
.. i18n: on users' computers.
..

两种使用方法提供了类似的使用界面和功能，而且你可以同时用两种方法连上同一台服务器使用。
如果 OpenERP 服务器离使用者有段距离(例如服务器在另一洲)，最好是使用浏览器，因为浏览器对时间延迟的容忍度
比 GTK 客户端要好。网页客户端也比较容易维护，因为通常使用者的电脑上已经安装了浏览器。

.. i18n: Conversely you would be better off with the application client (called the GTK
.. i18n: client because of the technology it is built with) if you are using a local
.. i18n: server (such as in the same building). In this case the GTK client will be more
.. i18n: responsive, so more satisfying to use.
..

相反地如果你是使用本地的服务器(例如在同一栋建筑内)，应用程序的客户端(被称为 GTK 客户端，因为内建 GTK 的技术)会较佳)。这种状况下 GTK 客户端响应速度较快，使用满意度也会较高。

.. i18n: .. index::
.. i18n:    single: client; web (thin) and GTK (thick)
.. i18n:    single: client; caching
..

.. 索引::
   single: client; web (thin) and GTK (thick)
   single: client; caching

.. i18n: .. note::   Web Client and GTK Client
.. i18n: 
.. i18n:     There is little functional difference between the two OpenERP clients - the 
.. i18n:     web client and the GTK client at present. 
.. i18n:     The web client offers more functionality, for instance, the Corporate Intelligence feature, and the Gantt view.
.. i18n:     
.. i18n:     The OpenERP company will continue to support two clients for the foreseeable
.. i18n:     future, so you can use whichever client you prefer.
..

.. 备注::   网页客户端和 GTK 客户端

    网页客户端和 GTK 客户端，这两种 OpenERP 客户端有一点点功能上的不同。 
    网页客户端提供较多功能，例如，企业情报 的功能和 甘特图。
    
    OpenERP 公司将会在可见的未来里继续支持这两种客户端，所以这两种客户端，你可以爱用哪种就用哪种。

.. i18n: An OpenERP system is formed from two components:
..

OpenERP 系统是由2部分组成:

.. i18n: * the PostgreSQL database server, which contains all of the databases, each of which contains all
.. i18n:   data and most elements of the OpenERP system configuration,
.. i18n: 
.. i18n: * the OpenERP application server, which contains all of the enterprise logic and ensures that
.. i18n:   OpenERP runs optimally.  It also contains the web server.
..

* PostgreSQL 数据库服务器，包含了所有数据库，其中每个数据库都包含了所有数据以及OpenERP系统组态大部分的要素。

* OpenERP 应用程序服务器，包含了所有企业的工作逻辑，服务器同时也确保 OpenERP 在最佳状态运行。这其中也包含了网页服务器。

.. i18n: .. figure:: images/terp_arch_1.png
.. i18n:    :align: center
.. i18n:    :scale: 90
.. i18n:    
.. i18n:    *The architecture of OpenERP*
..

.. figure:: images/terp_arch_1.png
   :align: center
   :scale: 90
   
   *OpenERP 的架构*

.. i18n: .. index::
.. i18n:    single: PostgreSQL
..

.. index::
   single: PostgreSQL

.. i18n: .. note::   PostgreSQL, the relational and object database management system.
.. i18n: 
.. i18n:     It is a free and open-source high-performance system that compares well with other database
.. i18n:     management systems such as MySQL and FirebirdSQL (both free), Sybase, DB2
.. i18n:     and Microsoft SQL Server (all proprietary). It runs on all types of
.. i18n:     Operating System, from Unix/Linux to the various releases of Windows, via
.. i18n:     Mac OS X, Solaris, SunOS and BSD.
..

.. 备注::   PostgreSQL 是一种关系型，也是物件型的数据库管理系统。

    这是一种免费，开源，高效能的系统，与其他数据库管理系统比起来毫不逊色，例如
    MySQL，FirebirdSQL (都是免费系统)， Sybase， DB2，微软 SQL Server (都是有版权的)。
     这个系统在各种作业系统上都可以运行，从 Unix/Linux 到许多不同版本的 Windows，也包含了
    Mac OS X， Solaris， SunOS 和 BSD.

.. i18n: Both components can be installed on the same server or
.. i18n: distributed onto separate computer servers, if performance considerations
.. i18n: require it.
..

这两部分可以安装在同一个服务器上，如果有考虑运作的效能需要，也可以分布在不同的电脑服务器上。

.. i18n: .. Copyright © Open Object Press. All rights reserved.
..

..  © Open Object Press. 版权所有，保留所有权利。

.. i18n: .. You may take electronic copy of this publication and distribute it if you don't
.. i18n: .. change the content. You can also print a copy to be read by yourself only.
..

.. 你可以拿这份刊物的电子档打印出来供自己阅读使用，或是如果你不修改任何内容，你也可以转发给其他人。

.. i18n: .. We have contracts with different publishers in different countries to sell and
.. i18n: .. distribute paper or electronic based versions of this book (translated or not)
.. i18n: .. in bookstores. This helps to distribute and promote the OpenERP product. It
.. i18n: .. also helps us to create incentives to pay contributors and authors using author
.. i18n: .. rights of these sales.
..

.. 我们有与许多不同国家的不同出版社签约，来发行及销售这本书的纸本或电子版本，包含原文版和翻译文的版本。
.. 这对传播和推广 OpenERP 产品有很大帮助，同时我们会用这些销售产生的版税收入，作为支付给作者及贡献者的奖励。

.. i18n: .. Due to this, grants to translate, modify or sell this book are strictly
.. i18n: .. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. i18n: .. written authorisation for this.
..

.. 因此，除非获得 Tiny SPRL (代表开源物件出版社，Open Object Press) 的书面授权，翻译补助金，修改或是贩卖这本书是被严格禁止的。

.. i18n: .. Many of the designations used by manufacturers and suppliers to distinguish their
.. i18n: .. products are claimed as trademarks. Where those designations appear in this book,
.. i18n: .. and Open Object Press was aware of a trademark claim, the designations have been
.. i18n: .. printed in initial capitals.
..

.. 许多制造商或供应商用于辨识他们产品的代号被称为 注册商标。在本书里出现的这些代号，如果开源物件出版社知道是注册商标的，会使用大写字母开头。

.. i18n: .. While every precaution has been taken in the preparation of this book, the publisher
.. i18n: .. and the authors assume no responsibility for errors or omissions, or for damages
.. i18n: .. resulting from the use of the information contained herein.
..

.. 出版商及作者已经尽最大努力准备这本书，所以不对内容的错误和疏漏承担责任；出版商及作者也不对采用书中讯息造成的损害承担任何责任。

.. i18n: .. Published by Open Object Press, Grand Rosière, Belgium
..

.. 开源物件出版社，于比利时 Grand Rosière
