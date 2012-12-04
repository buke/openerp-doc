
.. module:: crm_bayes
    :synopsis: crm_bayes 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/crm_bayes"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Bayesian Filter (*crm_bayes*)
=============================

:Module: crm_bayes
:Name: Bayesian Filter
:Version: 1.0
:Author: Tiny
:Directory: crm_bayes
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

This module allows automated actions to be performed on customers request, based on bayes. First we need to train some email contents in bayes to related category then after guess the email content using bayes and then send an email template to the customer. If you try to categorise without training no result is produced and the system cannot send an email template to the responsible customer to correct category.
For example, suppose you receive French, English and Spanish emails into one account. First we must train some content into each category. Any new emails will then filter correctly and send an email template to the correct category and responsible person.
Suppose a received email is in French, then it will automatically send email template in French.

Required Package:-     -> python-reverend

Download links
--------------

You can download this module as a zip file in the following version:

  * `trunk <http://www.openerp.com/download/modules/trunk/crm_bayes.zip>`_ 


Dependencies
------------

  * :mod:`crm_configuration`
  * :mod:`base`


Reports
-------
None

Menus
-------

None

Views
-----

  * crm_bayes_group (form)
  * crm_bayes_group (tree)
  * crm_bayes_categories (form)
  * crm_bayes_categories (tree)
  * \* INHERIT crm_case_rule (form)
  * \* INHERIT crm_case_bayes_form_oppor (form)
  * \* INHERIT crm_case_bayes_form_leads (form)
  * \* INHERIT crm_case_bayes_form_claims (form)
  * \* INHERIT crm_case_bayes_form_support (form)
  * report.crm.bayes.statistic.tree (tree)
  * report.crm.bayes.statistic.form (form)
  * report.crm.bayes.statistic.graph (graph)


Objects
-------

  * crm.bayes.group
  * crm.bayes.categories
  * crm.bayes.test.guess
  * crm.bayes.test.train
  * crm.bayes.train.message
  * report.crm.bayes.statistic



