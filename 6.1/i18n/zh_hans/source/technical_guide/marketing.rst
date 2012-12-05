
.. i18n: .. module:: marketing
.. i18n:     :synopsis: Marketing Campaigns 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: marketing
    :synopsis: Marketing Campaigns 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/marketing"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/marketing"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Marketing Campaigns (*marketing*)
.. i18n: =================================
.. i18n: :Module: marketing
.. i18n: :Name: Marketing Campaigns
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: marketing
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

Marketing Campaigns (*marketing*)
=================================
:Module: marketing
:Name: Marketing Campaigns
:Version: 5.0.1.0
:Author: Tiny
:Directory: marketing
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   Marketing management module
..

::

  Marketing management module

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/marketing.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/marketing.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/marketing.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/marketing.zip>`_

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

.. i18n:  * Marketing Operations
.. i18n:  * Marketing Operations/Campaigns
.. i18n:  * Marketing Operations/Configuration
.. i18n:  * Marketing Operations/Configuration/Campaign Definition
..

 * Marketing Operations
 * Marketing Operations/Campaigns
 * Marketing Operations/Configuration
 * Marketing Operations/Configuration/Campaign Definition

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * campaign.campaign.view (tree)
.. i18n:  * campaign.campaign.view (form)
.. i18n:  * campaign.step.tree (tree)
.. i18n:  * campaign.step.form (form)
.. i18n:  * campaign.partner.tree (tree)
.. i18n:  * campaign.partner.form (form)
.. i18n:  * campaign.partner.history.form (form)
.. i18n:  * campaign.partner.history.tree (tree)
..

 * campaign.campaign.view (tree)
 * campaign.campaign.view (form)
 * campaign.step.tree (tree)
 * campaign.step.form (form)
 * campaign.partner.tree (tree)
 * campaign.partner.form (form)
 * campaign.partner.history.form (form)
 * campaign.partner.history.tree (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: campaign.campaign (campaign.campaign)
.. i18n: #############################################
..

Object: campaign.campaign (campaign.campaign)
#############################################

.. i18n: :info: Description, text
..

:info: Description, text

.. i18n: :date_stop: Stop Date, date
..

:date_stop: Stop Date, date

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :date_start: Start Date, date
..

:date_start: Start Date, date

.. i18n: :planned_costs: Planned Costs, float
..

:planned_costs: Planned Costs, float

.. i18n: :costs: Initial Costs, float
..

:costs: Initial Costs, float

.. i18n: :step_id: Campaign Steps, one2many
..

:step_id: Campaign Steps, one2many

.. i18n: :planned_revenue: Planned Revenue, float
..

:planned_revenue: Planned Revenue, float

.. i18n: Object: campaign.step (campaign.step)
.. i18n: #####################################
..

Object: campaign.step (campaign.step)
#####################################

.. i18n: :info: Description, text
..

:info: Description, text

.. i18n: :name: Step Name, char, required
..

:name: Step Name, char, required

.. i18n: :procent: Success Rate (0<x<1), float
..

:procent: Success Rate (0<x<1), float

.. i18n: :stop_date: Stop Date, date
..

:stop_date: Stop Date, date

.. i18n: :campaign_id: Campaign, many2one
..

:campaign_id: Campaign, many2one

.. i18n: :priority: Sequence, integer, required
..

:priority: Sequence, integer, required

.. i18n: :costs: Step Costs, float
..

:costs: Step Costs, float

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :max_try: Max Attempts, integer
..

:max_try: Max Attempts, integer

.. i18n: :start_date: Start Date, date
..

:start_date: Start Date, date

.. i18n: Object: campaign.partner (campaign.partner)
.. i18n: ###########################################
..

Object: campaign.partner (campaign.partner)
###########################################

.. i18n: :part_adr_id: Partner Address, many2one, required
..

:part_adr_id: Partner Address, many2one, required

.. i18n: :info: Comments, text
..

:info: Comments, text

.. i18n: :state: State, selection, readonly
..

:state: State, selection, readonly

.. i18n: :user_id: Salesman, many2one
..

:user_id: Salesman, many2one

.. i18n: :name: Name / Reference, char, required
..

:name: Name / Reference, char, required

.. i18n: :date_recall: Call again on, datetime
..

:date_recall: Call again on, datetime

.. i18n: :notes: Prospect Notes, text
..

:notes: Prospect Notes, text

.. i18n: :campaign_id: Campaign, many2one
..

:campaign_id: Campaign, many2one

.. i18n: :priority: Priority, selection, required
..

:priority: Priority, selection, required

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :step: Step, many2one, required
..

:step: Step, many2one, required

.. i18n: :contact: Partner Contact, char
..

:contact: Partner Contact, char

.. i18n: :history_ids: History, one2many
..

:history_ids: History, one2many

.. i18n: :partner_id: Partner, many2one, required
..

:partner_id: Partner, many2one, required

.. i18n: Object: campaign.partner.history (campaign.partner.history)
.. i18n: ###########################################################
..

Object: campaign.partner.history (campaign.partner.history)
###########################################################

.. i18n: :info: Comments, text
..

:info: Comments, text

.. i18n: :name: History, char, required
..

:name: History, char, required

.. i18n: :camp_partner_id: Prospect, many2one, readonly
..

:camp_partner_id: Prospect, many2one, readonly

.. i18n: :step_attempt: Attempt, integer, readonly
..

:step_attempt: Attempt, integer, readonly

.. i18n: :date: Date, datetime, readonly
..

:date: Date, datetime, readonly

.. i18n: :step_id: Step, many2one, readonly
..

:step_id: Step, many2one, readonly
