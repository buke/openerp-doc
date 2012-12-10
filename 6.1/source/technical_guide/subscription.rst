
.. i18n: .. module:: subscription
.. i18n:     :synopsis: Subscription and recurring operations (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: subscription
    :synopsis: Subscription and recurring operations (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/subscription"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/subscription"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Subscription and recurring operations (*subscription*)
.. i18n: ======================================================
.. i18n: :Module: subscription
.. i18n: :Name: Subscription and recurring operations
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: subscription
.. i18n: :Web: 
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

Subscription and recurring operations (*subscription*)
======================================================
:Module: subscription
:Name: Subscription and recurring operations
:Version: 5.0.1.0
:Author: Tiny
:Directory: subscription
:Web: 
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Module allows to create new documents and add subscription on that document.
..

::

  Module allows to create new documents and add subscription on that document.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/subscription.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/subscription.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/subscription.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/subscription.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/subscription.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/subscription.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
..

 * :mod:`base`

.. i18n: Reports
.. i18n: -------
..

Reports
-------

.. i18n: None
..

None

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Tools
.. i18n:  * Tools/Subscriptions
.. i18n:  * Tools/Subscriptions/Configuration
.. i18n:  * Tools/Subscriptions/All Subscriptions
.. i18n:  * Tools/Subscriptions/Configuration/Document Types
..

 * Tools
 * Tools/Subscriptions
 * Tools/Subscriptions/Configuration
 * Tools/Subscriptions/All Subscriptions
 * Tools/Subscriptions/Configuration/Document Types

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * subscription.subscription.form (form)
.. i18n:  * subscription.subscription.tree (tree)
.. i18n:  * subscription.subscription.history.tree (tree)
.. i18n:  * subscription.subscription.history.form (form)
.. i18n:  * subscription.document.form (form)
.. i18n:  * subscription.document.tree (tree)
.. i18n:  * subscription.document.fields.form (form)
.. i18n:  * subscription.document.fields.tree (tree)
..

 * subscription.subscription.form (form)
 * subscription.subscription.tree (tree)
 * subscription.subscription.history.tree (tree)
 * subscription.subscription.history.form (form)
 * subscription.document.form (form)
 * subscription.document.tree (tree)
 * subscription.document.fields.form (form)
 * subscription.document.fields.tree (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Subscription document (subscription.document)
.. i18n: #####################################################
..

Object: Subscription document (subscription.document)
#####################################################

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :model: Object, many2one, required
..

:model: Object, many2one, required

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :field_ids: Fields, one2many
..

:field_ids: Fields, one2many

.. i18n: Object: Subscription document fields (subscription.document.fields)
.. i18n: ###################################################################
..

Object: Subscription document fields (subscription.document.fields)
###################################################################

.. i18n: :field: Field, many2one, required
..

:field: Field, many2one, required

.. i18n: :document_id: Subscription Document, many2one
..

:document_id: Subscription Document, many2one

.. i18n: :value: Default Value, selection
..

:value: Default Value, selection

.. i18n: Object: Subscription (subscription.subscription)
.. i18n: ################################################
..

Object: Subscription (subscription.subscription)
################################################

.. i18n: :cron_id: Cron Job, many2one
..

:cron_id: Cron Job, many2one

.. i18n: :user_id: User, many2one, required
..

:user_id: User, many2one, required

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :partner_id: Partner, many2one
..

:partner_id: Partner, many2one

.. i18n: :notes: Notes, text
..

:notes: Notes, text

.. i18n: :interval_type: Interval Unit, selection
..

:interval_type: Interval Unit, selection

.. i18n: :exec_init: Number of documents, integer
..

:exec_init: Number of documents, integer

.. i18n: :state: Status, selection
..

:state: Status, selection

.. i18n: :doc_lines: Documents created, one2many, readonly
..

:doc_lines: Documents created, one2many, readonly

.. i18n: :doc_source: Source Document, reference, required
..

:doc_source: Source Document, reference, required

.. i18n: :interval_number: Interval Qty, integer
..

:interval_number: Interval Qty, integer

.. i18n: :date_init: First Date, datetime
..

:date_init: First Date, datetime

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: Object: Subscription history (subscription.subscription.history)
.. i18n: ################################################################
..

Object: Subscription history (subscription.subscription.history)
################################################################

.. i18n: :date: Date, datetime
..

:date: Date, datetime

.. i18n: :subscription_id: Subscription, many2one
..

:subscription_id: Subscription, many2one

.. i18n: :document_id: Source Document, reference, required
..

:document_id: Source Document, reference, required
