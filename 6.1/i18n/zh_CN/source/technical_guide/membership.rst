
.. i18n: .. module:: membership
.. i18n:     :synopsis: Membership (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: membership
    :synopsis: Membership (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/membership"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/membership"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Membership (*membership*)
.. i18n: =========================
.. i18n: :Module: membership
.. i18n: :Name: Membership
.. i18n: :Version: 5.0.0.1
.. i18n: :Author: Tiny
.. i18n: :Directory: membership
.. i18n: :Web: 
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

Membership (*membership*)
=========================
:Module: membership
:Name: Membership
:Version: 5.0.0.1
:Author: Tiny
:Directory: membership
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
.. i18n:   This module allows you to manage all operations for managing memberships.
.. i18n:   It supports different kind of members:
.. i18n:   * Free member
.. i18n:   * Associated member (ex: a group subscribe for a membership for all
.. i18n:     subsidiaries)
.. i18n:   * Paid members,
.. i18n:   * Special member prices, ...
.. i18n:   
.. i18n:   It is integrated with sales and accounting to allow you to automatically
.. i18n:   invoice and send propositions for membership renewal.
..

::

  This module allows you to manage all operations for managing memberships.
  It supports different kind of members:
  * Free member
  * Associated member (ex: a group subscribe for a membership for all
    subsidiaries)
  * Paid members,
  * Special member prices, ...
  
  It is integrated with sales and accounting to allow you to automatically
  invoice and send propositions for membership renewal.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/membership.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/membership.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/membership.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/membership.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/membership.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/membership.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
.. i18n:  * :mod:`product`
.. i18n:  * :mod:`account`
.. i18n:  * :mod:`process`
..

 * :mod:`base`
 * :mod:`product`
 * :mod:`account`
 * :mod:`process`

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

.. i18n:  * Membership
.. i18n:  * Membership/Configuration
.. i18n:  * Membership/Configuration/Membership products
.. i18n:  * Membership/Current members
.. i18n:  * Membership/Current members/Paid members
.. i18n:  * Membership/Current members/Free members
.. i18n:  * Membership/Current members/Associated members
.. i18n:  * Membership/Current members/Invoiced members
.. i18n:  * Membership/Future members (invoice not confirmed)
.. i18n:  * Membership/Old members
.. i18n:  * Membership/Reporting
.. i18n:  * Membership/Reporting/Membership by Years
.. i18n:  * Membership/Reporting/New Membership by Years
..

 * Membership
 * Membership/Configuration
 * Membership/Configuration/Membership products
 * Membership/Current members
 * Membership/Current members/Paid members
 * Membership/Current members/Free members
 * Membership/Current members/Associated members
 * Membership/Current members/Invoiced members
 * Membership/Future members (invoice not confirmed)
 * Membership/Old members
 * Membership/Reporting
 * Membership/Reporting/Membership by Years
 * Membership/Reporting/New Membership by Years

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * Membership products (tree)
.. i18n:  * Membership products (form)
.. i18n:  * \* INHERIT Membership product (form)
.. i18n:  * Current members (tree)
.. i18n:  * associate members (tree)
.. i18n:  * \* INHERIT res.partner.tree.form.inherit (form)
.. i18n:  * \* INHERIT res.partner.form.inherit (form)
.. i18n:  * report.partner_member.year.tree (tree)
.. i18n:  * report.partner_member.year.tree (tree)
.. i18n:  * report.partner_member.year.graph1 (graph)
.. i18n:  * report.partner_member.year.graph2 (graph)
.. i18n:  * report.partner_member.year_new.tree (tree)
.. i18n:  * report.partner_member.year_new.tree (tree)
.. i18n:  * report.partner_member.year_new.graph1 (graph)
.. i18n:  * report.partner_member.year_new.graph2 (graph)
.. i18n:  * \* INHERIT product.normal.form (form)
..

 * Membership products (tree)
 * Membership products (form)
 * \* INHERIT Membership product (form)
 * Current members (tree)
 * associate members (tree)
 * \* INHERIT res.partner.tree.form.inherit (form)
 * \* INHERIT res.partner.form.inherit (form)
 * report.partner_member.year.tree (tree)
 * report.partner_member.year.tree (tree)
 * report.partner_member.year.graph1 (graph)
 * report.partner_member.year.graph2 (graph)
 * report.partner_member.year_new.tree (tree)
 * report.partner_member.year_new.tree (tree)
 * report.partner_member.year_new.graph1 (graph)
 * report.partner_member.year_new.graph2 (graph)
 * \* INHERIT product.normal.form (form)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Member line (membership.membership_line)
.. i18n: ################################################
..

Object: Member line (membership.membership_line)
################################################

.. i18n: :date_from: From, date
..

:date_from: From, date

.. i18n: :state: State, selection, readonly
..

:state: State, selection, readonly

.. i18n: :account_invoice_line: Account Invoice line, many2one
..

:account_invoice_line: Account Invoice line, many2one

.. i18n: :date_to: To, date
..

:date_to: To, date

.. i18n: :partner: Partner, many2one
..

:partner: Partner, many2one

.. i18n: :date_cancel: Cancel date, date
..

:date_cancel: Cancel date, date

.. i18n: Object: Membership by Years (report.partner_member.year)
.. i18n: ########################################################
..

Object: Membership by Years (report.partner_member.year)
########################################################

.. i18n: :waiting_number: Waiting, integer, readonly
..

:waiting_number: Waiting, integer, readonly

.. i18n: :paid_amount: Paid, float, readonly
..

:paid_amount: Paid, float, readonly

.. i18n: :invoiced_amount: Invoiced, float, readonly
..

:invoiced_amount: Invoiced, float, readonly

.. i18n: :paid_number: Paid, integer, readonly
..

:paid_number: Paid, integer, readonly

.. i18n: :canceled_number: Cancelled, integer, readonly
..

:canceled_number: Cancelled, integer, readonly

.. i18n: :currency: Currency, many2one, readonly
..

:currency: Currency, many2one, readonly

.. i18n: :invoiced_number: Invoiced, integer, readonly
..

:invoiced_number: Invoiced, integer, readonly

.. i18n: :year: Year, char, readonly
..

:year: Year, char, readonly

.. i18n: :waiting_amount: Waiting, float, readonly
..

:waiting_amount: Waiting, float, readonly

.. i18n: :canceled_amount: Cancelled, float, readonly
..

:canceled_amount: Cancelled, float, readonly

.. i18n: Object: New Membership by Years (report.partner_member.year_new)
.. i18n: ################################################################
..

Object: New Membership by Years (report.partner_member.year_new)
################################################################

.. i18n: :waiting_number: Waiting, integer, readonly
..

:waiting_number: Waiting, integer, readonly

.. i18n: :paid_amount: Paid, float, readonly
..

:paid_amount: Paid, float, readonly

.. i18n: :invoiced_amount: Invoiced, float, readonly
..

:invoiced_amount: Invoiced, float, readonly

.. i18n: :paid_number: Paid, integer, readonly
..

:paid_number: Paid, integer, readonly

.. i18n: :canceled_number: Cancelled, integer, readonly
..

:canceled_number: Cancelled, integer, readonly

.. i18n: :currency: Currency, many2one, readonly
..

:currency: Currency, many2one, readonly

.. i18n: :invoiced_number: Invoiced, integer, readonly
..

:invoiced_number: Invoiced, integer, readonly

.. i18n: :year: Year, char, readonly
..

:year: Year, char, readonly

.. i18n: :waiting_amount: Waiting, float, readonly
..

:waiting_amount: Waiting, float, readonly

.. i18n: :canceled_amount: Cancelled, float, readonly
..

:canceled_amount: Cancelled, float, readonly
