.. i18n: .. _part2-crm-channel:
.. i18n: 
.. i18n: Managing your Indirect Sales
.. i18n: ============================
..

.. _part2-crm-channel:

管理你的间接的销售
============================

.. i18n: .. index::
.. i18n:    single: module; crm_partner_assign
..

.. index::
   single: module; crm_partner_assign

.. i18n: OpenERP will help you to manage your Channel Partners. You can geolocalize your opportunities by going to :menuselection:`Administration --> Modules --> Modules` and then typing :mod:`crm_partner_assign` in the ``Name`` field. Check the module and click the button at the end of the line (after the ``State`` field) to plan the module for installation. Notice that the ``State`` will change to 'To be installed'. In the Actions at the right, click `Apply Scheduled Upgrades`. The module will be installed and the menus :menuselection:`Sales --> Configuration --> Leads & Opportunities --> Partner Grade` and :menuselection:`Sales --> Reporting --> Opportunity Assignment Analysis` will be added.
..

OpenERP 将帮助你管理你的渠道业务伙伴. 可以将商机进行区域化，只需要在 :menuselection:`管理 --> 模块 --> 模块` 在Modules的 ``Name`` 字段中输入: `crm_partner_assign` . 进行检索再点击最后一行的按钮 (在 ``State`` 字段后) 进行模块的安装. 注意 ``State`` 会转变为'将要安装的模块'. 点击执行左侧的动作`执行已安排的升级`. 模块将被安装，并且增加以下菜单:`销售 --> 设置 --> 线索 & 商机 --> 业务伙伴级别` 与 `销售 --> 报告 --> 商机指定分析`.

.. i18n: .. note:: CRM Configuration Wizard
.. i18n: 
.. i18n:         When you click `Apply Scheduled Upgrades`, the Configuration Wizard will be displayed. You can cancel it if you need no other CRM modules to be installed.
..

注意:: CRM 配置向导

        当你点击`执行已安排的升级`, 配置向导将会显示. 如果不需要安装其他CRM模块，可以点击取消配置向导.

.. i18n: Forwarding Opportunities to Channel Partners
.. i18n: --------------------------------------------
..

转发商机给渠道业务伙伴
--------------------------------------------

.. i18n: You can use geolocalization to assign and forward opportunities to channel partners.
..

可以使用地域化功能，把商机指派和转交给渠道业务伙伴.

.. i18n: Through :menuselection:`Sales --> Configuration --> Leads & Opportunities --> Partner Grade`, you can create partner grades to classify your partners, such as Gold Partner, Silver Partner, Ready Partner. These grades will be used to determine who gets assigned which kind of opportunities.
..

通过菜单项:`销售 --> 设置 --> 线索 & 商机 --> 业务伙伴级别`, 可以创建业务伙伴级别对业务伙伴进行分类, 例如金牌业务伙伴, 银牌业务伙伴, 准业务伙伴. 这些级别将会被用来确定谁可以得到哪些商机.

.. i18n: Assign the grades to the partners on the `Geo Localization` tab of the Customer form. Also assign a `Weight` to determine the probability of assigning opportunities to a partner. The weight might for instance be how much the partner pays for their channel partner contract.
..

在客户视图中的 `Geo Localization 定位` 分页中指定业务伙伴的级别. 同时可指定 `重要性` 用于指定商机分配给业务伙伴的概率(0表示不分配). 这个`重要性`,举例来说,可以是业务伙伴所能支付的业务合同的最大金额.

.. i18n: How can you tell OpenERP to geolocalize an opportunity?
.. i18n:  
.. i18n: Either you convert a promising lead to an opportunity, or you go directly to the opportunity you wish to assign to the channel partner.
.. i18n: Go to the `Assignation` tab of the **Opportunities** form, and click the `Geo Assign` button. The location of the partner in the opportunity will be matched with the geolatitude and the weight of the channel partners. The most appropriate channel partner will be assigned.
..

How can you tell OpenERP to geolocalize an opportunity?
 
Either you convert a promising lead to an opportunity, or you go directly to the opportunity you wish to assign to the channel partner.
Go to the `Assignation` tab of the **Opportunities** form, and click the `Geo Assign` button. The location of the partner in the opportunity will be matched with the geolatitude and the weight of the channel partners. The most appropriate channel partner will be assigned.

.. i18n: .. note:: GPS
.. i18n: 
.. i18n:        You can also use the geolocalisation without GPS coordinates.
..

.. note:: GPS

       You can also use the geolocalisation without GPS coordinates.

.. i18n: Now you can decide whether this is the correct channel partner for this opportunity. If you feel that another channel partner would be better to follow up this opportunity because he , you can change the assigned channel partner.
..

Now you can decide whether this is the correct channel partner for this opportunity. If you feel that another channel partner would be better to follow up this opportunity because he , you can change the assigned channel partner.

.. i18n: To automatically inform the channel partner of the new opportunity, proceed as follows.
..

To automatically inform the channel partner of the new opportunity, proceed as follows.

.. i18n: Click the ``Forward`` button to automatically send an email to the assigned partner with all the details of the opportunity and the prospect.
.. i18n: When forwarding an opportunity to a partner, you can select which information you want to send: Latest email, Whole Story or Case Information. You can add a cc and add attachments to the mail.
.. i18n: You can send the mail to the partner (any contact person you want), to an OpenERP user or to an email address you specify.
..

Click the ``Forward`` button to automatically send an email to the assigned partner with all the details of the opportunity and the prospect.
When forwarding an opportunity to a partner, you can select which information you want to send: Latest email, Whole Story or Case Information. You can add a cc and add attachments to the mail.
You can send the mail to the partner (any contact person you want), to an OpenERP user or to an email address you specify.

.. i18n: To allow your salespeople to keep a view on forwarded opportunities, the assigned opportunity will be displayed for the selected channel partner on the `Geo Localization` tab of the **Customer** form.
..

To allow your salespeople to keep a view on forwarded opportunities, the assigned opportunity will be displayed for the selected channel partner on the `Geo Localization` tab of the **Customer** form.

.. i18n: Use the **Opportunity Assignment Analysis** for your reporting.
..

Use the **Opportunity Assignment Analysis** for your reporting.

.. i18n: .. todo:: test screen
..

.. todo:: test screen

.. i18n: .. tip:: Google Maps
.. i18n: 
.. i18n:        Use the geolocalization together with the google_map module. This adds a Map button to your **Partner** form. Click this button to open a browser with the partner's location displayed in Google Maps.
..

.. tip:: Google Maps

       Use the geolocalization together with the google_map module. This adds a Map button to your **Partner** form. Click this button to open a browser with the partner's location displayed in Google Maps.

.. i18n: Geolocalization of a Partner
.. i18n: ----------------------------
..

Partner的地理定位
----------------------------

.. i18n: To determine the geographic location of your partners, you do not have to enter the GPS coordinates yourself. OpenERP can do this for you. All you have to do is click the ``Geo Localize`` button in the **Customer** form. The GPS coordinates will now be filled according to the address of the partner.
..

To determine the geographic location of your partners, you do not have to enter the GPS coordinates yourself. OpenERP can do this for you. All you have to do is click the ``Geo Localize`` button in the **Customer** form. The GPS coordinates will now be filled according to the address of the partner.

.. i18n: In the partner form, the `Geo Localization` tab gives you the information you need.
..

In the partner form, the `Geo Localization` tab gives you the information you need.

.. i18n: .. figure:: images/crm_partner_geolocalize.png
.. i18n:    :scale: 80
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Geolocalizing a Partner*
..

.. figure:: images/crm_partner_geolocalize.png
   :scale: 80
   :align: center

   *Geolocalizing a Partner*

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
