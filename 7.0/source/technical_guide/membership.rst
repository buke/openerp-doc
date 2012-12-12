
.. module:: membership
    :synopsis: Membership (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/membership"></div>
    <script src="http://js-kit.com/ratings.js"></script>

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

Description
-----------

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

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/membership.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/membership.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/membership.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`product`
 * :mod:`account`
 * :mod:`process`

Reports
-------

None


Menus
-------

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

Views
-----

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


Objects
-------

Object: Member line (membership.membership_line)
################################################



:date_from: From, date





:state: State, selection, readonly





:account_invoice_line: Account Invoice line, many2one





:date_to: To, date





:partner: Partner, many2one





:date_cancel: Cancel date, date




Object: Membership by Years (report.partner_member.year)
########################################################



:waiting_number: Waiting, integer, readonly





:paid_amount: Paid, float, readonly





:invoiced_amount: Invoiced, float, readonly





:paid_number: Paid, integer, readonly





:canceled_number: Cancelled, integer, readonly





:currency: Currency, many2one, readonly





:invoiced_number: Invoiced, integer, readonly





:year: Year, char, readonly





:waiting_amount: Waiting, float, readonly





:canceled_amount: Cancelled, float, readonly




Object: New Membership by Years (report.partner_member.year_new)
################################################################



:waiting_number: Waiting, integer, readonly





:paid_amount: Paid, float, readonly





:invoiced_amount: Invoiced, float, readonly





:paid_number: Paid, integer, readonly





:canceled_number: Cancelled, integer, readonly





:currency: Currency, many2one, readonly





:invoiced_number: Invoiced, integer, readonly





:year: Year, char, readonly





:waiting_amount: Waiting, float, readonly





:canceled_amount: Cancelled, float, readonly


