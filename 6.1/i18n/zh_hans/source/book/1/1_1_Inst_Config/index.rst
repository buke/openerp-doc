.. i18n: .. index::
.. i18n:    single: Installation
.. i18n:    single: Initial Setup
.. i18n:    pair: configuration; setup
..

.. index::
   single: Installation
   single: Initial Setup
   pair: configuration; setup

.. i18n: .. _ch-inst:
.. i18n: 
.. i18n: ******************************
.. i18n: Installation and Initial Setup
.. i18n: ******************************
..

.. _ch-inst:

******************************
安装与初始配置
******************************

.. i18n:  *Installing OpenERP under Windows or Linux to get familiar with the software should take you only half an
.. i18n:  hour or so and needs only a couple of operations.*
.. i18n:  
.. i18n:  *The first operation is to install the application and database server on a server PC (that is
.. i18n:  a Windows or Linux or Macintosh computer).*
..

 *要熟悉OpenERP,可以自己在Windows或Linux下安装OpenERP，安装过程大概只需要半个小时左右。*
 
 *第一步是在一台服务器PC（即Windows或Linux或Macintosh电脑）上安装OpenERP和数据库服务器（即PostgreSQL）。*

.. i18n:  *You have a choice of approaches for the second operation:
.. i18n:  either use standard web
.. i18n:  clients that can be found on anybody's PC, or install application clients on each intended user's PC.*
.. i18n:  
.. i18n: When you first install OpenERP, you will set up a database containing a little functionality and
.. i18n: some demonstration data to test the installation.
.. i18n:  
.. i18n: .. index::
.. i18n:    single: Tiny ERP
..

 *第二步你可以选择使用网页浏览器或在用户的电脑上安装OpenERP客户端软件来访问OpenERP服务器*
 
当你安装完OpenERP后，接下来就要创建一个包含一些演示数据的数据库，以便测试安装是否成功。
 
.. index::
   single: Tiny ERP

.. i18n: .. note:: Renaming from Tiny ERP to OpenERP
.. i18n: 
.. i18n:    Tiny ERP was renamed to OpenERP early in 2008, so anyone who has used Tiny ERP should be
.. i18n:    equally at home with OpenERP. Both names refer to the same software, so there is no
.. i18n:    functional difference between versions 4.2.X of OpenERP and 4.2.X of Tiny ERP. This book
.. i18n:    applies to versions of OpenERP from 6.1.0 onwards, with references to earlier versions from
.. i18n:    time to time.
..

.. note:: Tiny ERP 更名为 OpenERP

   早在2008年，Tiny ERP更名为OpenERP，所有使用过Tiny ERP的用户应该同样熟悉OpenERP。两个名字所指的是同一个软件，
   因此OpenERP的4.2.X版本和Tiny ERP的4.2.X版本在功能上没有差别。本书适用于OpenERP 6.1.0以及之后的版本，但也会
   时常参考到6.1之前的版本。

.. i18n: .. index::
.. i18n:    single:SaaS
..

.. index::
   single:SaaS

.. i18n: .. note:: The SaaS, or “on-demand”, offer
.. i18n: 
.. i18n:    SaaS (Software as a Service) is delivered by a hosting supplier and paid in the form of a monthly
.. i18n:    subscription that
.. i18n:    includes hardware (servers), system maintenance, provision of hosting services, and support.
.. i18n: 
.. i18n:    You can get a month's free trial on OpenERP's http://www.openerp.com/online, which enables you to get
.. i18n:    started quickly
.. i18n:    without incurring costs for integration or for buying computer systems.
.. i18n:    Many of OpenERP's partner companies will access this, and some may offer their own similar service.
.. i18n: 
.. i18n:    This service should be particularly useful to small companies that just want to get going quickly
.. i18n:    and at low cost.
.. i18n:    It gives you immediate access to an integrated management system that has been built on the type
.. i18n:    of enterprise architecture
.. i18n:    used in banks and other large organizations.
.. i18n:    OpenERP is that system, and is described in detail throughout this book.
..

.. note:: SaaS或按需提供

   SaaS (软件即服务 ) 由托管服务商提供服务，客户按月缴纳服务费的形式使用。包括硬件（服务器），系统维护，提供托管服务和支持。

   在你这里你可以获得OpenERP一个月的免费试用 http://www.openerp.com/online，它可以让你在不增加系统费用投入的情况下快速的开始试用。
   很多OpenERP的合作伙伴都是用它，其中有一些还提供类似的服务。

   这项服务对于小公司特别有用，他们往往希望用尽量少的花费，最快的将系统运行起来。
   
   It gives you immediate access to an integrated management system that has been built on the type
   of enterprise architecture
   used in banks and other large organizations.
   OpenERP is that system, and is described in detail throughout this book.

.. i18n: Whether you want to test OpenERP or to put it into full production, you have at least three starting
.. i18n: points:
..

无论你是想测试OpenERP还是想把它投入正式生产，至少需要三starting点：


.. i18n: * no need to install OpenERP, you can test it through http://demo.openerp.com,
.. i18n: 
.. i18n: * evaluate it on line at http://www.openerp.com and ask OpenERP for a SaaS trial hosted at
.. i18n:   http://ondemand.openerp.com, or the equivalent service at any of OpenERP's partner companies,
.. i18n: 
.. i18n: * install it on your own computers to test it in your company's system environment.
..

* 无需安装，可通过这里进行测试 http://demo.openerp.com,

* 在线评估地址 http://www.openerp.com OpenERP SaaS 测试地址 http://ondemand.openerp.com，
  或者在OpenERP合作伙伴处体验这些内容，
 

* 在你自己的电脑上安装测试。

.. i18n: There are some differences between installing OpenERP on Windows and on Linux systems, but once
.. i18n: installed, both systems offer the same functionality so you will not generally be able to tell which type
.. i18n: of server you are using.
..

在Windows上安装OpenERP和在Linux上安装略有不同，但是一旦安装上，系统提供的功能都是一样的，所以你不必在意你用的是那种服务器。


.. i18n: .. note:: Linux, Windows, Mac
.. i18n: 
.. i18n:    Although this book deals only with installation on Windows and Linux systems, the same versions
.. i18n:    are also available for Macintosh on the official website of OpenERP.
..

.. note:: Linux, Windows, Mac

   虽然这本书只涉及在Windows和Linux系统上安装，但是OpenERP的官方网站上相同的版本也可用于Macintosh。

.. i18n: .. note:: Websites for OpenERP
.. i18n: 
.. i18n:    * Main Site: http://www.openerp.com,
.. i18n: 
.. i18n:    * SaaS or OpenERP OnLine Site: http://www.openerp.com/online,
.. i18n: 
.. i18n:    * Documentation Site: http://doc.openerp.com/,
.. i18n: 
.. i18n:    * Community discussion forum where you can often receive informed assistance:
.. i18n:      http://www.openobject.com/forum.
..

.. note:: OpenERP的网站

   * 主站: http://www.openerp.com,

   * SaaS 或 OpenERP在线: http://www.openerp.com/online,

   * 文档站: http://doc.openerp.com/,

   * 社区论坛，在那里你可以经常得到其他人的帮助:
     http://www.openobject.com/forum.

.. i18n: .. tip:: Current documentation
.. i18n: 
.. i18n:    The procedure for installing OpenERP will change and improve with
.. i18n:    each new version, so you should always check each release's documentation – both packaged with
.. i18n:    the release and on the website – for exact installation procedures.
..

.. tip:: 当前文档

   The procedure for installing OpenERP will change and improve with
   each new version, so you should always check each release's documentation – both packaged with
   the release and on the website – for exact installation procedures.

.. i18n: Once you have completed this installation, create and set up a database to confirm that your
.. i18n: OpenERP installation is working. You can follow earlier chapters in this part of the book to achieve this.
..

一旦你已经安装完成，就可以创建数据库了，并确认您的OpenERP的进程在运行。您可以按照本书前面的章节来实现。

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <div class="all-toctree">
..

.. raw:: html

    <div class="all-toctree">

.. i18n: .. toctree::
.. i18n: 
.. i18n:    1_1_Inst_Config_architecture
.. i18n:    1_1_Inst_Config_install
.. i18n:    1_1_Inst_Config_db_create
..

.. toctree::

   1_1_Inst_Config_architecture
   1_1_Inst_Config_install
   1_1_Inst_Config_db_create

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
