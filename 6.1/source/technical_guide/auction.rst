
.. module:: auction
    :synopsis: Auction module (Official, Quality Certified)
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/auction"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Auction module (*auction*)
==========================
:Module: auction
:Name: Auction module
:Version: 5.0.1.0
:Author: Tiny
:Directory: auction
:Web: 
:Official module: yes
:Quality certified: yes

Description
-----------

::

  This module provides functionality to 
       manage artists, articles, sellers, buyers and auction.
       Manage bids, track of sold, paid and unpaid objects.
       Delivery Management.

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/auction.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/auction.zip>`_


Dependencies
------------

 * :mod:`base`
 * :mod:`account`
 * :mod:`hr_attendance`

Reports
-------

 * Listing Huissiers

 * Artists Biography

 * Bids phones

 * Bids

 * Code barres du lot

 * Lots List - Landscape

 * Auction Totals with lists

 * Buyer Form

 * Deposits

 * Seller Form

 * Seller List

 * Buyer List

 * Bids per lot (phone)

 * Results with buyer

Menus
-------

 * Auction Management
 * Auction Management/Configuration
 * Auction Management/Configuration/Define Artists
 * Auction Management/Configuration/Object Categories
 * Auction Management/Auction Dates
 * Auction Management/Auction Dates/Next Auction Dates
 * Auction Management/Auction Dates/Old Auction Dates
 * Auction Management/Auction Dates/New Auction Dates
 * Auction Management/Objects
 * Auction Management/Objects/All objects
 * Auction Management/Objects/All objects/Sold Objects
 * Auction Management/Objects/All objects/Objects to sell
 * Auction Management/Objects/All objects/Unplanned objects
 * Auction Management/Objects/All objects/Unsold Objects
 * Auction Management/Objects/All objects/Unclassified objects
 * Auction Management/Sellers
 * Auction Management/Sellers/Deposit border
 * Auction Management/Buyers
 * Auction Management/Buyers/Bids
 * Auction Management/Buyers/Bids/Bids line
 * Auction Management/Reporting
 * Auction Management/Reporting/Auction
 * Auction Management/Reporting/Auction/Auction's Summary
 * Auction Management/Reporting/Auction/Auction's Revenues
 * Auction Management/Reporting/Sellers
 * Auction Management/Reporting/Sellers/Seller's Summary
 * Auction Management/Reporting/Sellers/Seller's Revenues
 * Auction Management/Reporting/Buyer
 * Auction Management/Reporting/Buyer/Buyer's Summary
 * Auction Management/Reporting/Buyer/Buyer's Revenues
 * Auction Management/Reporting/Employees
 * Auction Management/Reporting/Employees/Comparison of estimations
 * Auction Management/Reporting/Manager
 * Auction Management/Reporting/Manager/Comparison of estimations
 * Auction Management/Reporting/Employees/Attendance
 * Auction Management/Reporting/Manager/Attendance
 * Auction Management/Reporting/Employees/My Latest Deposits
 * Auction Management/Reporting/Manager/Latest Deposits
 * Auction Management/Reporting/Manager/Encoded Objects Per Day
 * Auction Management/Reporting/Employees/My Encoded Objects Per Day
 * Auction Management/Objects/Objects by Auction
 * Auction Management/Reporting/Manager/Adjudication by Auction
 * Auction Management/Reporting/Manager/Depositer's Statistics
 * Auction Management/Reporting/Employees/Depositer's Statistics
 * Auction Management/Tools Bar Codes
 * Auction Management/Tools Bar Codes/Deliveries Management

Views
-----

 * auction.artists.tree (tree)
 * auction.artists.form (form)
 * auction.lot.category.tree (tree)
 * auction.lot.category.form (form)
 * Auction dates (tree)
 * Auction dates (form)
 * Auction lots (tree)
 * Auction lots (form)
 * Auction lots (graph)
 * Auction lots (tree)
 * Auction lots (form)
 * auction.lots.form3 (form)
 * Auction.deposit.tree (tree)
 * auction.deposit.form (form)
 * Deposit border (tree)
 * auction.bid_line.tree1 (tree)
 * auction.bid_line.form1 (form)
 * auction.bid.form (form)
 * auction.bid.tree (tree)
 * auction.reports.tree (tree)
 * auction.reports.form (form)
 * auction.reports.tree2 (tree)
 * Auction report (form)
 * Seller's auction (form)
 * Seller's auction (tree)
 * Seller's auction (graph)
 * Seller's auction (form)
 * Seller's auction (tree)
 * Seller's auction (graph)
 * Buyer's auction (form)
 * Buyer's auction (tree)
 * Buyer's auction (form)
 * Buyer's auction (tree)
 * Unplanned objects (tree)
 * Unplanned objects (form)
 * report.auction.estimation.adj.category.form (form)
 * report.auction.estimation.adj.category.tree (tree)
 * report.auction.estimation.adj.category.graph (graph)
 * report attendance (tree)
 * Graph attendance (graph)
 * Objects by date (tree)
 * Object date (form)
 * report.auction.object.date.graph (graph)
 * report.auction.adjudication.tree (tree)
 * report.auction.adjudication.graph (graph)
 * Depositer's statistics (tree)
 * report.object.encoded.form (form)
 * report.object.encoded.tree (tree)
 * report.object.encoded.graph (graph)
 * report.object.encoded.tree (tree)
 * report.object.encoded.graph (graph)
 * report.unclassified.objects (tree)


Objects
-------

Object: auction.artists (auction.artists)
#########################################



:birth_death_dates: Birth / Death dates, char





:pseudo: Pseudo, char





:name: Artist/Author Name, char, required





:biography: Biography, text




Object: auction.dates (auction.dates)
#####################################



:journal_seller_id: Seller Journal, many2one, required





:expo1: First Exposition Day, date, required





:acc_expense: Expense Account, many2one, required





:expo2: Last Exposition Day, date, required





:acc_income: Income Account, many2one, required





:journal_id: Buyer Journal, many2one, required





:adj_total: Total Adjudication, float, readonly





:state: Status, selection, readonly





:auction1: First Auction Day, date, required





:buyer_costs: Buyer Costs, many2many





:auction2: Last Auction Day, date, required





:account_analytic_id: Analytic Account, many2one, required





:seller_costs: Seller Costs, many2many





:name: Auction date, char, required




Object: Deposit Border (auction.deposit)
########################################



:info: Description, char





:create_uid: Created by, many2one, readonly





:specific_cost_ids: Specific Costs, one2many





:name: Depositer Inventory, char, required





:date_dep: Deposit date, date, required





:transfer: Transfer, boolean





:partner_id: Seller, many2one, required





:lot_id: Objects, one2many





:total_neg: Allow Negative Amount, boolean





:method: Withdrawned method, selection, required





:tax_id: Expenses, many2one




Object: auction.deposit.cost (auction.deposit.cost)
###################################################



:deposit_id: Deposit, many2one





:account: Destination Account, many2one, required





:amount: Amount, float





:name: Cost Name, char, required




Object: auction.lot.category (auction.lot.category)
###################################################



:priority: Priority, float





:active: Active, boolean





:name: Category Name, char, required





:aie_categ: Aie Category, selection




Object: Object (auction.lots)
#############################



:is_ok: Buyer's payment, boolean





:vnd_lim: Seller limit, float





:statement_id: Payment, many2many





:net_margin: Net Margin (%), float, readonly





:image: Image, binary





:lot_num: List Number, integer, required





:ach_uid: Buyer, many2one





:sel_inv_id: Seller Invoice, many2one, readonly





:vnd_lim_net: Net limit ?, boolean, readonly





:bord_vnd_id: Depositer Inventory, many2one, required





:ach_emp: Taken Away, boolean





:ach_avance: Buyer Advance, float





:lot_local: Location, char





:net_revenue: Net revenue, float, readonly





:artist2_id: Artist/Author 2, many2one





:obj_comm: Commission, boolean





:paid_ach: Buyer invoice reconciled, boolean, readonly





:lot_type: Object category, selection





:state: Status, selection, required, readonly





:auction_id: Auction Date, many2one





:history_ids: Auction history, one2many





:artist_id: Artist/Author, many2one





:ach_login: Buyer Username, char





:gross_revenue: Gross revenue, float, readonly





:author_right: Author rights, many2one





:create_uid: Created by, many2one, readonly





:gross_margin: Gross Margin (%), float, readonly





:important: To be Emphasised, boolean





:bid_lines: Bids, one2many





:lot_est1: Minimum Estimation, float





:lot_est2: Maximum Estimation, float





:name: Short Description, char, required





:obj_num: Catalog Number, integer





:buyer_price: Buyer price, float, readonly





:ach_inv_id: Buyer Invoice, many2one, readonly





:obj_price: Adjudication price, float





:obj_ret: Price retired, float





:costs: Indirect costs, float, readonly





:name2: Short Description (2), char





:paid_vnd: Seller Paid, boolean





:product_id: Product, many2one, required





:obj_desc: Object Description, text





:seller_price: Seller price, float, readonly




Object: Bid auctions (auction.bid)
##################################



:bid_lines: Bid, one2many





:contact_tel: Contact, char





:auction_id: Auction Date, many2one, required





:partner_id: Buyer Name, many2one, required





:name: Bid ID, char, required




Object: Lot history (auction.lot.history)
#########################################



:lot_id: Object, many2one, required





:price: Withdrawn price, float





:auction_id: Auction date, many2one, required





:name: Date, date




Object: Bid (auction.bid_line)
##############################



:name: Bid date, char





:auction: Auction Name, char





:price: Maximum Price, float





:bid_id: Bid ID, many2one, required





:call: To be Called, boolean





:lot_id: Object, many2one, required




Object: Auction Reporting on buyer view (report.buyer.auction)
##############################################################



:total_price: Total Adj., float, readonly





:auction: Auction date, many2one, readonly





:object: No of objects, integer, readonly





:buyer: Buyer, many2one, readonly





:avg_price: Avg Adj., float, readonly





:date: Create Date, date





:buyer_login: Buyer Login, char, readonly




Object: Auction Reporting on buyer view (report.buyer.auction2)
###############################################################



:gross_revenue: Gross Revenue, float, readonly





:net_revenue: Net Revenue, float, readonly





:auction: Auction date, many2one, readonly





:net_margin: Net Margin, float, readonly





:buyer: Buyer, many2one, readonly





:sumadj: Sum of adjustication, float, readonly





:date: Create Date, date, required





:buyer_login: Buyer Login, char, readonly




Object: Auction Reporting on seller view (report.seller.auction)
################################################################



:total_price: Total adjudication, float, readonly





:auction: Auction date, many2one, readonly





:object_number: No of Objects, integer, readonly





:seller: Seller, many2one, readonly





:state: Status, selection, readonly





:avg_estimation: Avg estimation, float, readonly





:avg_price: Avg adjudication, float, readonly





:date: Create Date, date, required




Object: Auction Reporting on seller view2 (report.seller.auction2)
##################################################################



:gross_revenue: Gross revenue, float, readonly





:sum_adj: Sum Adjustication, float, readonly





:net_revenue: Net revenue, float, readonly





:auction: Auction date, many2one, readonly





:seller: Seller, many2one, readonly





:date: Auction date, date, required





:net_margin: Net margin, float, readonly




Object: Auction Reporting on  view2 (report.auction.view2)
##########################################################



:gross_revenue: Gross revenue, float, readonly





:obj_number: # of Objects, integer, readonly





:sum_adj: Sum of adjudication, float, readonly





:net_revenue: Net revenue, float, readonly





:auction: Auction date, many2one, readonly





:obj_margin_procent: Net margin (%), float, readonly





:obj_margin: Avg margin, float, readonly





:date: Auction date, date, required




Object: Auction Reporting on view1 (report.auction.view)
########################################################



:max_est: Maximum Estimation, float, readonly





:min_est: Minimum Estimation, float, readonly





:nseller: No of sellers, float, readonly





:nbuyer: No of buyers, float, readonly





:nobjects: No of objects, float, readonly





:obj_ret: # obj ret, integer, readonly





:auction_id: Auction date, many2one, readonly





:adj_price: Adjudication price, float, readonly




Object: Objects per day (report.auction.object.date)
####################################################



:month: Month, date





:user_id: User, many2one





:obj_num: # of Objects, integer





:name: Created date, date




Object: comparison estimate/adjudication  (report.auction.estimation.adj.category)
###################################################################################



:user_id: User, many2one





:lot_type: Object Type, selection





:adj_total: Total Adjudication, float





:date: Date, date, readonly





:lot_est1: Minimum Estimation, float





:lot_est2: Maximum Estimation, float




Object: report_auction_adjudication (report.auction.adjudication)
#################################################################



:date: Date, date, readonly





:adj_total: Total Adjudication, float





:state: Status, selection





:user_id: User, many2one





:name: Auction date, many2one, readonly




Object: Report Sign In/Out (report.attendance)
##############################################



:total_attendance: Total, float, readonly





:employee_id: Employee, many2one, readonly





:name: Date, date, readonly




Object: Report deposit border (report.deposit.border)
#####################################################



:total_marge: Total margin, float, readonly





:nb_obj: # of objects, float, readonly





:bord: Depositer Inventory, char, required





:moy_est: Avg. Est, float, readonly





:seller: Seller, many2one




Object: Object encoded (report.object.encoded)
##############################################



:user_id: User, many2one





:obj_num: # of Encoded obj., integer, readonly





:obj_ret: # obj ret, integer, readonly





:state: Status, selection, required





:date: Create Date, date, required





:estimation: Estimation, float




Object: Object encoded (report.object.encoded.manager)
######################################################



:gross_revenue: Gross revenue, float, readonly





:user_id: User, many2one





:obj_num: # of Encoded obj., integer, readonly





:net_revenue: Net revenue, float, readonly





:obj_ret: # obj ret, integer, readonly





:obj_margin: Net margin, float, readonly





:date: Create Date, date, required





:estimation: Estimation, float





:adj: Adj., integer, readonly




Object: Unclassified objects  (report.unclassified.objects)
###########################################################



:obj_num: Catalog Number, integer





:auction: Auction date, many2one, readonly





:obj_comm: Commission, boolean





:obj_price: Adjudication price, float





:name: Short Description, char, required





:lot_type: Object category, selection





:state: Status, selection, required, readonly





:lot_num: List Number, integer, required





:lot_est1: Minimum Estimation, float





:lot_est2: Maximum Estimation, float





:bord_vnd_id: Depositer Inventory, many2one, required





:ach_login: Buyer Username, char


