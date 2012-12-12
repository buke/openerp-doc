
.. module:: cci_partner
    :synopsis: CCI Partner 
    :noindex:
.. 

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. tip:: This module is part of the OpenERP software, the leading Open Source 
  enterprise management system. If you want to discover OpenERP, check our 
  `screencasts <http://openerp.tv>`_ or download 
  `OpenERP <http://openerp.com>`_ directly.

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/cci_partner"></div>
    <script src="http://js-kit.com/ratings.js"></script>

CCI Partner (*cci_partner*)
===========================
:Module: cci_partner
:Name: CCI Partner
:Version: 5.0.1.0
:Author: Tiny
:Directory: cci_partner
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  Specific module for cci project which will inherit partner module

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/cci_partner.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/cci_partner.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`base_vat`
 * :mod:`cci_base_contact`
 * :mod:`account_l10nbe_domiciliation`
 * :mod:`cci_country`

Reports
-------

 * Count invoices

Menus
-------

 * Partners/Configuration/States
 * Partners/Configuration/States/Activity State
 * Partners/Configuration/States/Customer State
 * Partners/Configuration/Partner Activity
 * Partners/Configuration/Partner Activity/Activity
 * Partners/Configuration/Partner Activity/Activity Relation
 * Partners/Configuration/Partner Activity/Activity List
 * Partners/Configuration/Zip
 * Partners/Configuration/Zip/Zip
 * Partners/Configuration/Zip/Zip Group
 * Partners/Configuration/Zip/Group Type
 * Partners/Configuration/Article
 * Partners/Configuration/Article/Article
 * Partners/Configuration/Article/Article Keyword
 * Partners/Configuration/Article/Article Reviews
 * Partners/Configuration/Link Type/Partner Link Type

Views
-----

 * \* INHERIT res.company.form (form)
 * res.partner.state.form (form)
 * res.partner.state2.form (form)
 * res.partner.activity.form (form)
 * res.partner.activity.tree (tree)
 * res.partner.activity.relation.form (form)
 * res.partner.activity.relation.tree (tree)
 * res.partner.activity.list.form (form)
 * res.partner.activity.list.tree (tree)
 * res.partner.zip.form (form)
 * res.partner.zip.tree (tree)
 * res.partner.zip.group.form (form)
 * res.partner.zip.group.tree (tree)
 * res.partner.zip.group.type.form (form)
 * res.partner.zip.group.type.tree (tree)
 * res.partner.article.form (form)
 * res.partner.article.tree (tree)
 * res.partner.article.keywords.form (form)
 * res.partner.article.keywords.tree (tree)
 * res.partner.article.review.form (form)
 * res.partner.article.review.tree (tree)
 * res.partner.relation.type.form (form)
 * res.partner.relation.tree (tree)
 * res.partner.relation.form (form)
 * \* INHERIT res.partner.contact.form (form)
 * \* INHERIT res.partner.contact.form (form)
 * \* INHERIT res.partner.contact.form (form)
 * \* INHERIT res.partner.job.form.inherit1 (form)
 * \* INHERIT Partner addresses inherited (form)
 * \* INHERIT res.partner.form (form)
 * \* INHERIT res.partner.form (form)
 * \* INHERIT res.partner.form (form)
 * \* INHERIT res.partner.form (form)
 * \* INHERIT res.partner.form (form)
 * \* INHERIT res.partner.form (form)
 * \* INHERIT Partner form inherited (form)


Objects
-------

Object: res.partner.state (res.partner.state)
#############################################



:name: Partner Status, char, required




Object: res.partner.state2 (res.partner.state2)
###############################################



:name: Customer Status, char, required




Object: res.partner.article.review (res.partner.article.review)
###############################################################



:date: Date, date, required





:article_ids: Articles, one2many





:name: Name, char, required




Object: res.partner.article (res.partner.article)
#################################################



:picture: Picture, boolean





:subtitle: Subtitle, text





:review_id: Review, many2one





:canal_id: Reference, char

    *A text with or without a link incorporated*



:press_review: In the next press review, boolean

    *Must be inserted on the next press review*



:data: Data, boolean





:title: Title, char, required





:summary: Summary, text





:source_id: Source, char





:contact_ids: Contacts, many2many





:keywords_ids: Keywords, many2many





:graph: Graph, boolean





:date: Date, date, required





:partner_ids: Partners, many2many





:article_length: Length, float





:article_id: Article, char





:page: Page, integer




Object: res.partner.article.keywords (res.partner.article.keywords)
###################################################################



:article_ids: Articles, many2many





:name: Name, char, required




Object: res.partner.zip.group.type (res.partner.zip.group.type)
###############################################################



:name: Name, char, required




Object: res.partner.zip.group (res.partner.zip.group)
#####################################################



:name: Name, char, required





:type_id: Type, many2one




Object: res.partner.zip (res.partner.zip)
#########################################



:post_center_id: Post Center, char





:city: City, char





:user_id: Salesman Responsible, many2one





:name: Zip Code, char, required





:groups_id: Areas, many2many





:post_center_special: Post Center Special, boolean





:partner_id: Master Cci, many2one





:distance: Distance, integer

    *Distance (km) between zip location and the cci.*


Object: res.partner.activity.list (res.partner.activity.list)
#############################################################



:abbreviation: Abbreviation, char





:name: Code list, char, required




Object: res.partner.activity (res.partner.activity)
###################################################



:code_relations: Related codes, many2many





:code: Code, char, required





:list_id: List, many2one, required





:description: Description, text





:label: Label, char, required




Object: res.partner.activity.relation (res.partner.activity.relation)
#####################################################################



:importance: Importance, selection, required





:activity_id: Activity, many2one





:partner_id: Partner, many2one




Object: res.partner.relation.type (res.partner.relation.type)
#############################################################



:name: Contact, char, required




Object: res.partner.relation (res.partner.relation)
###################################################



:percent: Ownership, float





:current_partner_id: Partner, many2one, required





:partner_id: Partner, many2one, required





:description: Description, text





:type_id: Type, many2one, required




Object: res.partner.country.relation (res.partner.country.relation)
###################################################################



:country_id: Country, many2one





:frequency: Frequency, selection





:partner_id: Partner, many2one





:type: Types, selection


