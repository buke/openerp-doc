
.. i18n: .. module:: crm_bayes
.. i18n:     :synopsis: crm_bayes 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: crm_bayes
    :synopsis: crm_bayes 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:       <br />
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />
..

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: .. tip:: This module is part of the OpenERP software, the leading Open Source 
.. i18n:   enterprise management system. If you want to discover OpenERP, check our 
.. i18n:   `screencasts <http://openerp.tv>`_ or download 
.. i18n:   `OpenERP <http://openerp.com>`_ directly.
..

.. tip:: This module is part of the OpenERP software, the leading Open Source 
  enterprise management system. If you want to discover OpenERP, check our 
  `screencasts <http://openerp.tv>`_ or download 
  `OpenERP <http://openerp.com>`_ directly.

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/crm_bayes"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/crm_bayes"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Bayesian Filter (*crm_bayes*)
.. i18n: =============================
..

Bayesian Filter (*crm_bayes*)
=============================

.. i18n: :Module: crm_bayes
.. i18n: :Name: Bayesian Filter
.. i18n: :Version: 1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: crm_bayes
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

:Module: crm_bayes
:Name: Bayesian Filter
:Version: 1.0
:Author: Tiny
:Directory: crm_bayes
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: This module allows automated actions to be performed on customers request, based on bayes. First we need to train some email contents in bayes to related category then after guess the email content using bayes and then send an email template to the customer. If you try to categorise without training no result is produced and the system cannot send an email template to the responsible customer to correct category.
.. i18n: For example, suppose you receive French, English and Spanish emails into one account. First we must train some content into each category. Any new emails will then filter correctly and send an email template to the correct category and responsible person.
.. i18n: Suppose a received email is in French, then it will automatically send email template in French.
..

This module allows automated actions to be performed on customers request, based on bayes. First we need to train some email contents in bayes to related category then after guess the email content using bayes and then send an email template to the customer. If you try to categorise without training no result is produced and the system cannot send an email template to the responsible customer to correct category.
For example, suppose you receive French, English and Spanish emails into one account. First we must train some content into each category. Any new emails will then filter correctly and send an email template to the correct category and responsible person.
Suppose a received email is in French, then it will automatically send email template in French.

.. i18n: Required Package:-     -> python-reverend
..

Required Package:-     -> python-reverend

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/crm_bayes.zip>`_ 
..

  * `trunk <http://www.openerp.com/download/modules/trunk/crm_bayes.zip>`_ 

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:   * :mod:`crm_configuration`
.. i18n:   * :mod:`base`
..

  * :mod:`crm_configuration`
  * :mod:`base`

.. i18n: Reports
.. i18n: -------
.. i18n: None
..

Reports
-------
None

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n: None
..

None

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:   * crm_bayes_group (form)
.. i18n:   * crm_bayes_group (tree)
.. i18n:   * crm_bayes_categories (form)
.. i18n:   * crm_bayes_categories (tree)
.. i18n:   * \* INHERIT crm_case_rule (form)
.. i18n:   * \* INHERIT crm_case_bayes_form_oppor (form)
.. i18n:   * \* INHERIT crm_case_bayes_form_leads (form)
.. i18n:   * \* INHERIT crm_case_bayes_form_claims (form)
.. i18n:   * \* INHERIT crm_case_bayes_form_support (form)
.. i18n:   * report.crm.bayes.statistic.tree (tree)
.. i18n:   * report.crm.bayes.statistic.form (form)
.. i18n:   * report.crm.bayes.statistic.graph (graph)
..

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

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n:   * crm.bayes.group
.. i18n:   * crm.bayes.categories
.. i18n:   * crm.bayes.test.guess
.. i18n:   * crm.bayes.test.train
.. i18n:   * crm.bayes.train.message
.. i18n:   * report.crm.bayes.statistic
..

  * crm.bayes.group
  * crm.bayes.categories
  * crm.bayes.test.guess
  * crm.bayes.test.train
  * crm.bayes.train.message
  * report.crm.bayes.statistic
