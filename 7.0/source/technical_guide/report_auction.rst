
.. module:: report_auction
    :synopsis: Auction Management - Reporting 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/report_auction"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Auction Management - Reporting (*report_auction*)
=================================================
:Module: report_auction
:Name: Auction Management - Reporting
:Version: 5.0.1.0
:Author: Tiny
:Directory: report_auction
:Web: http://www.openerp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  A module that adds new reports based on Auction.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/report_auction.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/report_auction.zip>`_


Dependencies
------------

 * :mod:`auction`
 * :mod:`hr_timesheet_sheet`

Reports
-------

None


Menus
-------

 * Auction Management/Reporting/Manager
 * Auction Management/Reporting/Manager/Auction Adjudication
 * Auction Management/Reporting/Member
 * Auction Management/Reporting/Member/Auction Adjudication
 * Auction Management/Reporting/Member/Auction Adjudication
 * Auction Management/Reporting/Manager/Customer Per Seller
 * Auction Management/Reporting/Member/My Latest 10 Deposit
 * Auction Management/Reporting/Member/My Latest 10 Objects
 * Auction Management/Reporting/Member/Object Per Day
 * Auction Management/Reporting/Manager/Object Per Day
 * Auction Management/Reporting/Member/This Month
 * Auction Management/Reporting/Member/This Month/Estimation
 * Auction Management/Reporting/Member/This Month/Estimation/Adjudication
 * Auction Management/Reporting/Manager/This Month
 * Auction Management/Reporting/Manager/This Month/Estimation
 * Auction Management/Reporting/Manager/This Month/Estimation/Adjudication
 * Auction Management/Reporting/Member/Summary of Sign_in Sign_out
 * Auction Management/Reporting/Manager/Summary of Sign_in Sign_out

Views
-----

 * Auction adjudication (tree)
 * Auction adjudication (form)
 * report.auction.adjudication.graph1 (graph)
 * report.per.seller.customer.tree (tree)
 * Seller/customer (form)
 * report.per.seller.customer.graph (graph)
 * Latest deposit  (form)
 * Latest deposit (tree)
 * report.latest.objects.tree (tree)
 * Latest objects (form)
 * Object date (tree)
 * Object date (form)
 * report.auction.object.date.graph1 (graph)
 * report.auction.estimation.adj.category.tree1 (tree)
 * report.auction.estimation.adj.category.graph1 (graph)
 * report.auction.user.pointing.tree (tree)
 * report.auction.user.pointing.graph (graph)


Objects
-------

Object: report_auction_adjudication (report.auction.adjudication1)
##################################################################



:name: Auction date, char, required





:adj_total: Total Adjudication, float





:auction1: First Auction Day, date, required





:buyer_costs: Buyer Costs, many2many





:auction2: Last Auction Day, date, required





:seller_costs: Seller Costs, many2many




Object: Customer per seller (report.per.seller.customer)
########################################################



:partner_id: Partner, many2one





:no_of_buyer: Buyer, integer





:name: Seller, char, required




Object: Latest 10 Deposits (report.latest.deposit)
##################################################



:info: Description, char





:specific_cost_ids: Specific Costs, one2many





:user_id: User, many2one





:name: Depositer Inventory, char, required





:date_dep: Deposit date, date, required





:total_neg: Allow Negative Amount, boolean





:lot_id: Objects, one2many





:partner_id: Seller, many2one, required





:method: Withdrawned method, selection, required





:tax_id: Expenses, many2one




Object: Latest 10 Objects (report.latest.objects)
#################################################



:user_id: User, many2one





:obj_num: Catalog Number, integer





:obj_comm: Commission, boolean





:obj_price: Adjudication price, float





:bord_vnd_id: Depositer Inventory, many2one, required





:obj_ret: Price retired, float





:auction_id: Auction Date, many2one





:partner_id: Seller, many2one, required





:obj_desc: Object Description, text




Object: Objects per day (report.auction.object.date1)
#####################################################



:obj_ret: Price retired, float





:obj_num: Catalog Number, integer





:obj_comm: Commission, boolean





:obj_price: Adjudication price, float





:bord_vnd_id: Depositer Inventory, many2one, required





:lot_type: Object Type, selection





:state: State, selection, required





:auction_id: Auction Date, many2one





:lot_num: Quantity, integer, required





:date: Name, char, required





:obj_desc: Object Description, text





:name: Short Description, char, required




Object: comparison estimate/adjudication  (report.auction.estimation.adj.category1)
###################################################################################



:obj_ret: Price retired, float





:name: Short Description, char, required





:obj_comm: Commission, boolean





:obj_price: Adjudication price, float





:obj_desc: Object Description, text





:lot_type: Object Type, selection





:adj_total: Total Adjudication, float





:state: State, selection, required





:auction_id: Auction Date, many2one





:lot_num: Quantity, integer, required





:date: Name, char, required





:lot_est1: Minimum Estimation, float





:lot_est2: Maximum Estimation, float





:bord_vnd_id: Depositer Inventory, many2one, required





:obj_num: Catalog Number, integer




Object: user pointing  (report.auction.user.pointing1)
######################################################



:total_timesheet: Project Timesheet, float





:sheet_id: Sheet, many2one





:user_id: User, char, required





:name: Date, date


