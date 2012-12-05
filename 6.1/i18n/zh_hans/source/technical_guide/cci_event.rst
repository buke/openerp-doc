
.. i18n: .. module:: cci_event
.. i18n:     :synopsis: CCI EVENT 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: cci_event
    :synopsis: CCI EVENT 
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/cci_event"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/cci_event"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: CCI EVENT (*cci_event*)
.. i18n: =======================
.. i18n: :Module: cci_event
.. i18n: :Name: CCI EVENT
.. i18n: :Version: 5.0.1.0
.. i18n: :Author: Tiny
.. i18n: :Directory: cci_event
.. i18n: :Web: http://www.openerp.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

CCI EVENT (*cci_event*)
=======================
:Module: cci_event
:Name: CCI EVENT
:Version: 5.0.1.0
:Author: Tiny
:Directory: cci_event
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
.. i18n:   specific module for cci project which will use Event module.
..

::

  specific module for cci project which will use Event module.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/cci_event.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/cci_event.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/cci_event.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/cci_event.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`event_project`
.. i18n:  * :mod:`account_payment`
.. i18n:  * :mod:`membership`
.. i18n:  * :mod:`cci_account`
.. i18n:  * :mod:`cci_partner`
..

 * :mod:`event_project`
 * :mod:`account_payment`
 * :mod:`membership`
 * :mod:`cci_account`
 * :mod:`cci_partner`

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

.. i18n:  * Events Organisation/Configuration/Groups
.. i18n:  * Events Organisation/Configuration/Groups/Event Group
.. i18n:  * Events Organisation/Event Check
.. i18n:  * Events Organisation/Configuration/Event Check
.. i18n:  * Events Organisation/Configuration/Event Check/Check Type
.. i18n:  * Events Organisation/Event Meeting
.. i18n:  * Events Organisation/Reporting/Registrations with Missing Checks
..

 * Events Organisation/Configuration/Groups
 * Events Organisation/Configuration/Groups/Event Group
 * Events Organisation/Event Check
 * Events Organisation/Configuration/Event Check
 * Events Organisation/Configuration/Event Check/Check Type
 * Events Organisation/Event Meeting
 * Events Organisation/Reporting/Registrations with Missing Checks

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * \* INHERIT event.event.form.cci (form)
.. i18n:  * \* INHERIT event.event.form (form)
.. i18n:  * \* INHERIT event.event.form (form)
.. i18n:  * \* INHERIT event.event.form (form)
.. i18n:  * \* INHERIT event.event.form (form)
.. i18n:  * \* INHERIT event.event.form (form)
.. i18n:  * \* INHERIT event.event.form (form)
.. i18n:  * event.event.tree (tree)
.. i18n:  * \* INHERIT Event type (form)
.. i18n:  * \* INHERIT Event type (tree)
.. i18n:  * event.group.form (form)
.. i18n:  * event.group.tree (tree)
.. i18n:  * event.check.form (form)
.. i18n:  * event.check.tree (tree)
.. i18n:  * event.check.type.form (form)
.. i18n:  * event.check.type.tree (tree)
.. i18n:  * \* INHERIT event.registration.form (form)
.. i18n:  * \* INHERIT event.registration.form (form)
.. i18n:  * \* INHERIT event.registration.form (form)
.. i18n:  * \* INHERIT event.registration.form (form)
.. i18n:  * \* INHERIT event.registration.form.cci (form)
.. i18n:  * \* INHERIT event.registration.form (form)
.. i18n:  * \* INHERIT event.registration.form (form)
.. i18n:  * \* INHERIT event.registration.form (form)
.. i18n:  * \* INHERIT event.registration.form (form)
.. i18n:  * event.meeting.table.form (form)
.. i18n:  * event.meeting.table.tree (tree)
.. i18n:  * \* INHERIT account.move.line.form (form)
..

 * \* INHERIT event.event.form.cci (form)
 * \* INHERIT event.event.form (form)
 * \* INHERIT event.event.form (form)
 * \* INHERIT event.event.form (form)
 * \* INHERIT event.event.form (form)
 * \* INHERIT event.event.form (form)
 * \* INHERIT event.event.form (form)
 * event.event.tree (tree)
 * \* INHERIT Event type (form)
 * \* INHERIT Event type (tree)
 * event.group.form (form)
 * event.group.tree (tree)
 * event.check.form (form)
 * event.check.tree (tree)
 * event.check.type.form (form)
 * event.check.type.tree (tree)
 * \* INHERIT event.registration.form (form)
 * \* INHERIT event.registration.form (form)
 * \* INHERIT event.registration.form (form)
 * \* INHERIT event.registration.form (form)
 * \* INHERIT event.registration.form.cci (form)
 * \* INHERIT event.registration.form (form)
 * \* INHERIT event.registration.form (form)
 * \* INHERIT event.registration.form (form)
 * \* INHERIT event.registration.form (form)
 * event.meeting.table.form (form)
 * event.meeting.table.tree (tree)
 * \* INHERIT account.move.line.form (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: event.meeting.table (event.meeting.table)
.. i18n: #################################################
..

Object: event.meeting.table (event.meeting.table)
#################################################

.. i18n: :service: Service, integer, required
..

:service: Service, integer, required

.. i18n: :event_id: Related Event, many2one, required
..

:event_id: Related Event, many2one, required

.. i18n: :contact_id2: Second Contact, many2one, required
..

:contact_id2: Second Contact, many2one, required

.. i18n: :contact_id1: First Contact, many2one, required
..

:contact_id1: First Contact, many2one, required

.. i18n: :partner_id1: First Partner, many2one, required
..

:partner_id1: First Partner, many2one, required

.. i18n: :table: Table, char, required
..

:table: Table, char, required

.. i18n: :partner_id2: Second Partner, many2one, required
..

:partner_id2: Second Partner, many2one, required

.. i18n: Object: event.check.type (event.check.type)
.. i18n: ###########################################
..

Object: event.check.type (event.check.type)
###########################################

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: Object: event.check (event.check)
.. i18n: #################################
..

Object: event.check (event.check)
#################################

.. i18n: :date_reception: Reception Date, date
..

:date_reception: Reception Date, date

.. i18n: :code: Code, char
..

:code: Code, char

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :type_id: Type, many2one
..

:type_id: Type, many2one

.. i18n: :date_submission: Submission Date, date
..

:date_submission: Submission Date, date

.. i18n: :date_limit: Limit Date, date
..

:date_limit: Limit Date, date

.. i18n: :reg_id: Inscriptions, many2one, required
..

:reg_id: Inscriptions, many2one, required

.. i18n: :state: State, selection, readonly
..

:state: State, selection, readonly

.. i18n: :unit_nbr: Value, float
..

:unit_nbr: Value, float

.. i18n: Object: event.group (event.group)
.. i18n: #################################
..

Object: event.group (event.group)
#################################

.. i18n: :picture: Picture, binary
..

:picture: Picture, binary

.. i18n: :type: Type, selection, required
..

:type: Type, selection, required

.. i18n: :name: Group Name, char, required
..

:name: Group Name, char, required

.. i18n: :bookmark_name: Value, char
..

:bookmark_name: Value, char
