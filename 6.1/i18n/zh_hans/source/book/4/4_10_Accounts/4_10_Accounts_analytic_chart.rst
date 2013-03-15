.. i18n: .. index::
.. i18n:    pair: chart of accounts; analytic
..

.. index::
   pair: chart of accounts; analytic

.. i18n: To Each Enterprise its own Analytic Chart of Accounts
.. i18n: =====================================================
..

公司辅助核算科目表
=====================================================

.. i18n: To illustrate analytic accounts clearly, you will follow three use cases, each in one of three different types of company:
..

为了清楚地说明分析会计，将使用三个案例，分别应用在三个不同类型的公司：

.. i18n:         #. Industrial Manufacturing Enterprise,
.. i18n: 
.. i18n:         #. Law Firm,
.. i18n: 
.. i18n:         #. IT Services Company.
..

        #. 制造行业企业,

        #. 律师事务所,

        #. IT服务公司.

.. i18n: Case 1: Industrial Manufacturing Enterprise
.. i18n: -------------------------------------------
..

案例 1: 制造行业企业
-------------------------------------------

.. i18n: In industry, you will often find analytic charts of accounts structured into departments and products the company itself is built on.
..

在工业中，你会经常发现分析科目表建立在部门和产品上，这也是公司建立的基础。

.. i18n: So the objective is to examine the costs, sales and margins by department and by product. The first level of the structure comprises the different departments, and the lower levels represent the product ranges the company makes and sells.
..

因此，目标是研究部门和产品的成本，销售和利润。结构的第一级由不同的部门构成，下级代表公司制造和销售的产品系列。

.. i18n: .. note::  Analytic Chart of Accounts for an Industrial Manufacturing Company
.. i18n: 
.. i18n:                 #. Marketing Department
.. i18n: 
.. i18n:                 #. Commercial Department
.. i18n: 
.. i18n:                 #. Administration Department
.. i18n: 
.. i18n:                 #. Production
.. i18n: 
.. i18n:                         * Product Range 1
.. i18n: 
.. i18n:                         * Sub-groups
.. i18n: 
.. i18n:                         * Product Range 2
..

.. note:: 工业制造公司的分析科目表

                #. 市场部

                #. 商务部

                #. 行政部

                #. 生产部

                        * 产品系列 1

                        * 子产品系列

                        * 产品系列 2

.. i18n: .. index::
.. i18n:    pair: cost; allocation
..

.. index::
   pair: cost; allocation

.. i18n: In daily use, it is useful to mark the analytic account on each purchase invoice. The analytic account is the one to which the costs of that purchase should be allocated. When the invoice is approved, it will automatically generate the entries for both the general and the corresponding analytic accounts. So, for each entry on the general accounts, there is at least one analytic entry that allocates costs to the department which incurred them.
..

在日常使用中，将每次采购发票标注到相应的分析账户是非常有用的。分析账户是采购成本的分配。当发票被核准时，它会自动生成财务和相应的分析账户的分录。因此，在每个总账分录上至少有一个分析账户分录以分配发生成本的部门。

.. i18n: Here is a possible breakdown of some general accounting entries for the example above, allocated to various analytic accounts:
..

这里有上面的例子中的一些的会计分录，归集到多个分析账户：

.. i18n: .. csv-table::  Breakdown of general and analytic accounting entries (Case 1)
.. i18n:    :header: "General accounts","","","","","Analytic accounts",""
.. i18n:    :widths: 10,5,5,5,2,10,8
.. i18n: 
.. i18n:    "Title","Account","Debit","Credit","","Account","Value"
.. i18n:    "Purchase of Raw Material","600","1500","","","Production / Range 1","-1 500"
.. i18n:    "Subcontractors","602","450","","","Production / Range 2","-450"
.. i18n:    "Credit Note for defective materials","600","","200","","Production / Range 1","200"
.. i18n:    "Transport charges","613","450","","","Production / Range 1","-450"
.. i18n:    "Staff costs","6201","10000","","","Marketing","-2 000"
.. i18n:    "","","","","","Commercial","-3 000"
.. i18n:    "","","","","","Administrative","-1 000"
.. i18n:    "","","","","","Production / Range 1","-2 000"
.. i18n:    "","","","","","Production / Range 2","-2 000"
.. i18n:    "PR ","614","450","","","Marketing","-450 "
..

.. csv-table::  财务和分析会计分录明细（案例1）
   :header: "一般会计账户","","","","","分析账户",""
   :widths: 10,5,5,5,2,10,8

   "标题","账户","借","贷","","账户","金额"
   "购买原材料","600","1500","","","产品 / 系列 1","-1 500"
   "分包商","602","450","","","产品 / 系列 2","-450"
   "有缺陷的材料","600","","200","","产品 / 系列 1","200"
   "运输费用","613","450","","","产品 / 系列 1","-450"
   "员工成本","6201","10000","","","市场部","-2 000"
   "","","","","","商务部","-3 000"
   "","","","","","行政部","-1 000"
   "","","","","","产品 / 系列 1","-2 000"
   "","","","","","产品 / 系列 2","-2 000"
   "公关 ","614","450","","","市场部","-450 "

.. i18n: The analytic representation by department enables you to investigate the costs allocated to each department in the company.
..

按部门分析可以让您审查分配到公司各部门的成本。

.. i18n: So, the analytic chart of accounts shows the distribution of the company's costs using the example above:
..

因此，分析科目表显示上面的例子中的公司的成本分布：

.. i18n: .. csv-table::  Analytic chart of accounts (Case 1)
.. i18n:    :header: "Account","Total"
.. i18n:    :widths: 10, 5
.. i18n: 
.. i18n:    "Marketing Department","-2 450 "
.. i18n:    "Commercial Department","-3 000 "
.. i18n:    "Administration Department","-1 000 "
.. i18n:    "Production","-6 200 "
.. i18n:    "Product Range 1","-3 750"
.. i18n:    "Product Range 2","-2 450"
..

.. csv-table::  账目分析图表（案例1）
   :header: "账户","合计"
   :widths: 10, 5

   "市场部","-2 450 "
   "商务部","-3 000 "
   "行政部","-1 000 "
   "产品","-6 200 "
   "产品 系列 1","-3 750"
   "产品 系列 2","-2 450"

.. i18n: In this example of a hierarchical structure in OpenERP, you can analyse not only the costs of each product range, but also the costs of the whole production. The balance of a summary account (*Production*) is the sum of the balances of the child accounts.
..

在这个OpenERP分层结构的例子中，你不仅可以分析每个产品系列的成本，也可以分析整个产品的成本。汇总账户（产品）的余额是子账户余额的合计。

.. i18n: A report that relates both general accounts and analytic accounts enables you to get a breakdown of costs within a given department. An analysis of the Production / Product Range 1 department is shown in this table:
..

一份联系总账和分析账户的报告是你了解成本构成在一个被指定的部门。对产品/系列1的分析如下表中所示：

.. i18n: .. csv-table:: Report merging both general and analytic accounts for a department (Case 1)
.. i18n:    :header: "Production / Product Range 1",""
.. i18n:    :widths: 10,5
.. i18n: 
.. i18n:    "General Account","Amount"
.. i18n:    "600 – Raw Materials","- 1 300"
.. i18n:    "613 – Transport charges","- 450"
.. i18n:    "6201 – Staff costs","-2 000"
.. i18n:    "Total","-3 750"
..

.. csv-table:: 部门一般账户和分析账户的合并报告（案例1）
   :header: "产品 / 系列 1",""
   :widths: 10,5

   "一般账户","金额"
   "600 – 原材料","- 1 300"
   "613 – 运输费","- 450"
   "6201 – 员工成本","-2 000"
   "合计","-3 750"

.. i18n: The examples above are based on a breakdown of the costs of the company. Analytic allocations can be just as effective for sales. That gives you the profitability (sales - costs) of different departments.
..

上面的例子是基于一个公司的成本构成明细。成本分配的分析对销售一样有效。这提供了不同部门的盈利能力（销售-成本）。

.. i18n: .. note::  Representation by Unique Product Range
.. i18n: 
.. i18n:         This analytic representation by department and by product range is generally used by trading
.. i18n:         companies and industries.
.. i18n: 
.. i18n:         A variant of this, is not to break it down by sales and marketing departments, but to assign each
.. i18n:         cost to its corresponding product range.
.. i18n:         This will give you an analysis of the profitability of each product range.
.. i18n: 
.. i18n:         Choosing one over the other depends on how you look at your marketing effort.
.. i18n:         Is it a global cost allocated in some general way, or is each product range responsible
.. i18n:         for its own marketing costs?
..

.. note::  独特的产品系列的代表性

        这种按部门和产品系列的分析表示通常用于贸易公司和生产企业。

        这方面的一个变种是不区分销售和营销部门，而是将每项成本分配给其相应的产品系列。这样就能得到每个产品系列的盈利能力分析。

        选择其他方式，取决于你如何看待你的营销效能。它是总成本集中分配的一般方式还是每个产品系列都应分摊该产品自身营销成本？

.. i18n: Case 2:  Law Firm
.. i18n: -----------------
..

案例 2:  律师事务所
-------------------

.. i18n: Law firms generally adopt management by case, where each case represents a current client file. All of the expenses and products are then attached to a given file.
..

律师事务所普遍采取按案件管理，每个案件代表了相对应的一个当前客户的档案。所有的费用和产品，都归属到一个给定的档案。

.. i18n: A principal preoccupation of law firms is the invoicing of hours worked, and the profitability by case and by employee.
..

一个律师事务所主要关注的是每小时的收费以及每个案件和雇员的盈利能力。

.. i18n: Mechanisms used for encoding the hours worked will be covered in detail in `Human Resources`. Like most system processes, hours worked are integrated into the analytic accounting. Every time an employee enters a timesheet for a number of hours, that automatically generates analytic accounts corresponding to the cost of those hours in the case concerned. The hourly charge is a function of the employee's salary.
..

工时编制机制将在下一章《领导并激励你的员工》中详细地介绍。像大多数系统进程，工时都纳入分析账户。每次当一个雇员在时间表里填写小时数，这些小时数将自动生成分析账户将这些时间的成本对应到相关案件上。每小时收费是以员工的工资进行换算。

.. i18n: .. index::
.. i18n:    single: absences
..

.. index::
   single: absences

.. i18n: So a law firm will opt for an analytic representation which reflects the management of the time that employees work on the different client cases.
..

因此，律师事务将会选择一个能够反映每个员工在服务于不同客户案件的时间管理分析。

.. i18n: .. note::  *Example Representation of an Analytic Chart of Accounts for a Law Firm*
.. i18n: 
.. i18n:                 #. Absences
.. i18n: 
.. i18n:                         * Paid Absences
.. i18n: 
.. i18n:                         * Unpaid Absences
.. i18n: 
.. i18n:                 #. Internal Projects
.. i18n: 
.. i18n:                         * Administrative
.. i18n: 
.. i18n:                         * Others
.. i18n: 
.. i18n:                 #. Client Cases
.. i18n: 
.. i18n:                         * Client 1
.. i18n: 
.. i18n:                             * Case 1.1
.. i18n: 
.. i18n:                             * Case 1.2
.. i18n: 
.. i18n:                         * Client 2
.. i18n: 
.. i18n:                             * Case 2.1
..

.. note::  *针对一家律师事务所的账户分析表作案例演示*

                #. 缺勤

                        * 带薪缺勤

                        * 无薪缺勤

                #. 内部项目

                        * 行政管理

                        * 其他

                #. 客户案例

                        * 客户 1

                            * 案例 1.1

                            * 案例 1.2

                        * 客户 2

                            * 案例 2.1

.. i18n: All expenses and sales are then attached to a case. This gives the profitability of each case and, at a consolidated level, of each client.
..

所有费用和销售所得都关联到一个案例，这就能得到在每一个客户每个案例在综合水平下的盈利能力。

.. i18n: Billing for the different cases is a bit unusual. The cases do not match any entry in the general account nor do they come from purchase or sales invoices. They are represented by the various analytic operations and do not have exact counterparts in the general accounts. They are calculated on the basis of the hourly cost per employee. These entries are automatically created when billing worksheets.
..

不同案例帐单是有点不同。案例与普通帐的任何会计分录都不相符并且也不是来自采购发票或销售发票。它们由各种分析操作表示，在普通帐户中没有对应。它们都基于雇员工作的小时成本基础上计算。这些分录在计费工作表上自动创建。

.. i18n: At the end of the month when you pay salaries and benefits, you integrate them into the general accounts but not in the analytic accounts, because they have already been accounted for in billing each account. A report that relates data from the analytic and general accounts then lets you compare the totals, so you can readjust your estimates of hourly cost per employee depending on the time actually worked.
..

在月底支付工资和福利时，你将它们记入普通账户中，但不在分析账户中，因为他们已被占为每个账户的计费。你可以出一份报告，比较辅助核算项和普通账户数据的汇总，以便你可以调整员工实际工作的每小时成本。

.. i18n: The following table shows an example of different analytic entries that you can find for your analytic account:
..

下表给出了不同的辅助核算分录的例子：

.. i18n: .. csv-table:: Analytic Entries for the Account Chart (Case 2)
.. i18n:    :header: "Title","Account","Amount","","General Account","Debit","Credit"
.. i18n:    :widths: 15, 10, 8, 2, 15, 8, 8
.. i18n: 
.. i18n:    "Study the file (1 h)","Case 1.1","-15","","","",""
.. i18n:    "Search for information (3 h)","Case 1.1","-45","","","",""
.. i18n:    "Consultation (4 h)","Case 2.1","-60","","","",""
.. i18n:    "Service charges","Case 1.1","280","","705 – Billing services","","280"
.. i18n:    "Stationery purchase","Administrative","-42","","601 – Furniture purchase","42",""
.. i18n:    "Fuel Cost -Client trip","Case 1.1","-35","","613 – Transports","35",""
.. i18n:    "Staff salaries","","","","6201 – Salaries","","3 000"
..

.. csv-table:: 会计科目表的辅助核算分录（案例2）
   :header: "标题","账户","金额","","总账","借","贷"
   :widths: 15, 10, 8, 2, 15, 8, 8

   "研究案例（1小时）","案例 1.1","-15","","","",""
   "搜索信息（3小时）","案例 1.1","-45","","","",""
   "咨询服务（4小时）","案例 2.1","-60","","","",""
   "服务费","案例 1.1","280","","705 – 结算服务","","280"
   "购买文具","行政","-42","","601 – 购买家具","42",""
   "燃料成本-拜访客户","案例 1.1","-35","","613 – 运输","35",""
   "工作人员薪金","","","","6201 – 薪金","","3 000"

.. i18n: Such a structure allows you to make a detailed study of the profitability of various transactions. In this example, the cost of Case 1.1 is 95.00 (the sum of the analytic costs of studying the files, searching for information and fuel costs), but has been invoiced at 280.00, which gives you a gross profit of 185.00.
..

你会看到，它使您可以详细分析了解来自不同会计事项的盈利。在本例中的1.1案例的成本是95.00（分析费用的总和，包括研究分析案例文档、搜索信息和服务费），但开票是280.00，带来的利润总额是185.00。

.. i18n: But an interest in analytical accounts is not limited to a simple analysis of the profitability of different cases.
..

但在辅助核算项的重点不是仅限于简单的分析不同案例的盈利情况。

.. i18n: The same data can be used for automatic recharging of the services to the client at the end of the month. To invoice clients, just take the analytic costs in that month and apply a selling price factor to generate the invoice. Invoicing mechanisms for this are explained in greater detail in `Services & Project Management`. If the client requires details of the services used on the case, you can print the service entries in the analytic account for this case.
..

这些产生自客户服务的相同数据可在月末自动收取服务成本。给客户的发票只需要在本月的分析成本基础上再加上一个销售价格系数即可。开票机制对此能为提供优质的服务做出最详细的解释。假如客户要求列出在此案例中提供的具体服务，那么你可以把这个辅助核算项中的关于这个案例的服务分录打印出来。

.. i18n: .. tip:: Invoicing Analytic Costs
.. i18n: 
.. i18n:         Most software that manages billing enables you to recharge hours worked.
.. i18n:         In OpenERP, these services are automatically represented by analytic costs.
.. i18n:         But many other OpenERP documents can also generate analytic costs, such as credit notes and
.. i18n:         purchases of goods.
.. i18n: 
.. i18n:         So when you invoice the client at the end of the month, it is possible for you to include all the
.. i18n:         analytic costs, and not just the hours worked. So, for example, you can easily recharge the whole cost of your journeys
.. i18n:         to the client.
..

.. tip:: 结算分析成本

        大多数管理软件允许你收回花费的工时，在OpenERP里这些服务是通过成本的有效性分析来自动体现的，但是在很多其它的OpenERP 文档中也能生成分析成本，如信用票据和货物采购。

        所以，当你在月底开发票给你的客户时，它包括所有的分析成本，而不仅仅是投入的工时。例如，你可以轻易的收回你为你的客户在整个流程中垫付的整体成本。

.. i18n: Case 3: IT Services Company
.. i18n: ---------------------------
..

案例 3: IT服务行业
---------------------------

.. i18n: Most IT service companies face the following problems:
..

Most IT service companies face the following problems:

.. i18n: * project planning,
.. i18n: 
.. i18n: * invoicing, profitability and financial follow-up of projects,
.. i18n: 
.. i18n: * managing support contracts.
..

* project planning,

* invoicing, profitability and financial follow-up of projects,

* managing support contracts.

.. i18n: To deal with these problems, you would use an analytic chart of accounts structured by project and by contract. A representation of that is given in the following example:
..

To deal with these problems, you would use an analytic chart of accounts structured by project and by contract. A representation of that is given in the following example:

.. i18n: .. note::  *Example Analytic Representation of a Chart of Accounts for an IT Services Company*
.. i18n: 
.. i18n:                 #. Internal Projects
.. i18n: 
.. i18n:                         * Administrative and Commercial
.. i18n: 
.. i18n:                         * Research and Development
.. i18n: 
.. i18n:                 #. Client Projects
.. i18n: 
.. i18n:                         * Client 1
.. i18n: 
.. i18n:                             * Project 1.1
.. i18n: 
.. i18n:                             * Project 1.2
.. i18n: 
.. i18n:                         * Client 2
.. i18n: 
.. i18n:                             * Project 2.1
.. i18n: 
.. i18n:                             * Project 2.2
.. i18n: 
.. i18n:                 #. Support Contracts – 20h
.. i18n: 
.. i18n:                         * Customer X
.. i18n: 
.. i18n:                         * Customer Y
..

.. note::  *Example Analytic Representation of a Chart of Accounts for an IT Services Company*

                #. Internal Projects

                        * Administrative and Commercial

                        * Research and Development

                #. Client Projects

                        * Client 1

                            * Project 1.1

                            * Project 1.2

                        * Client 2

                            * Project 2.1

                            * Project 2.2

                #. Support Contracts – 20h

                        * Customer X

                        * Customer Y

.. i18n: The management of services, expenditures and sales is similar to that presented above for lawyers. Invoicing and the study of profitability are also similar.
..

The management of services, expenditures and sales is similar to that presented above for lawyers. Invoicing and the study of profitability are also similar.

.. i18n: But now look at support contracts. These contracts are usually limited to a prepaid number of hours. Each service posted in the analytic accounts shows the remaining hours of support. To manage support contracts, you would use the quantities and not the amounts in the analytic entries.
..

But now look at support contracts. These contracts are usually limited to a prepaid number of hours. Each service posted in the analytic accounts shows the remaining hours of support. To manage support contracts, you would use the quantities and not the amounts in the analytic entries.

.. i18n: In OpenERP, each analytic line lists the number of units sold or used, as well as what you would usually find there – the amount in currency units (USD or GBP, or whatever other choice you make). So you can sum the quantities sold and used on each analytic account to determine whether any hours of the support contract remain.
..

In OpenERP, each analytic line lists the number of units sold or used, as well as what you would usually find there – the amount in currency units (USD or GBP, or whatever other choice you make). So you can sum the quantities sold and used on each analytic account to determine whether any hours of the support contract remain.

.. i18n: .. index::
.. i18n:    pair: cost; allocation
..

.. index::
   pair: cost; allocation

.. i18n: To differentiate services from other costs in the analytic account, you use the concept of the analytic journal. Analytic entries are then allocated into the different journals:
..

To differentiate services from other costs in the analytic account, you use the concept of the analytic journal. Analytic entries are then allocated into the different journals:

.. i18n: * service journal,
.. i18n: 
.. i18n: * expense journal,
.. i18n: 
.. i18n: * sales journal,
.. i18n: 
.. i18n: * purchase journal.
..

* service journal,

* expense journal,

* sales journal,

* purchase journal.

.. i18n: To obtain the detailed breakdown of a support contract, you only have to look at the service journal for the analytic account corresponding to the contract in question.
..

To obtain the detailed breakdown of a support contract, you only have to look at the service journal for the analytic account corresponding to the contract in question.

.. i18n: Finally, the analytic account can be used to forecast future needs. For example, monthly planning of staff on different projects can be seen as an analytic budget limited to the service journal. Accounting entries are expressed in quantities (such as number of hours, and numbers of products), and in amounts in units of currency (USD or GBP for instance).
..

Finally, the analytic account can be used to forecast future needs. For example, monthly planning of staff on different projects can be seen as an analytic budget limited to the service journal. Accounting entries are expressed in quantities (such as number of hours, and numbers of products), and in amounts in units of currency (USD or GBP for instance).

.. i18n: So you can set up planning on just the basis of quantities. Analysing the analytic budget enables you to compare the budget (that is, your plan) to the services actually carried out by month end.
..

So you can set up planning on just the basis of quantities. Analysing the analytic budget enables you to compare the budget (that is, your plan) to the services actually carried out by month end.

.. i18n: .. tip:: Cash Budgets
.. i18n: 
.. i18n:         Problems of cash management are amongst the main difficulties encountered by small growing businesses.
.. i18n:         It is really difficult to predict the amount of cash that will be available when a company is young
.. i18n:         and rapidly growing.
.. i18n: 
.. i18n:         If the company adopts management by case, then staff planning can be represented in the analytic
.. i18n:         accounts report, as you have seen.
.. i18n: 
.. i18n:         But since you know your selling price for each of the different projects, you can see that it is easy to use the plan in the analytic accounts to more precisely forecast the amounts that you will invoice in the coming months.
..

.. tip:: Cash Budgets

        Problems of cash management are amongst the main difficulties encountered by small growing businesses.
        It is really difficult to predict the amount of cash that will be available when a company is young
        and rapidly growing.

        If the company adopts management by case, then staff planning can be represented in the analytic
        accounts report, as you have seen.

        But since you know your selling price for each of the different projects, you can see that it is easy to use the plan in the analytic accounts to more precisely forecast the amounts that you will invoice in the coming months.

.. i18n: .. Copyright © Open Object Press. All rights reserved.
..

.. Copyright © Open Object Press. All rights reserved.

.. i18n: .. You may take electronic copy of this publication and distribute it if you don't
.. i18n: .. change the content. You can also print a copy to be read by yourself only.
..

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. i18n: .. We have contracts with different publishers in different countries to sell and
.. i18n: .. distribute paper or electronic based versions of this book (translated or not)
.. i18n: .. in bookstores. This helps to distribute and promote the OpenERP product. It
.. i18n: .. also helps us to create incentives to pay contributors and authors using author
.. i18n: .. rights of these sales.
..

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the OpenERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. i18n: .. Due to this, grants to translate, modify or sell this book are strictly
.. i18n: .. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. i18n: .. written authorisation for this.
..

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. i18n: .. Many of the designations used by manufacturers and suppliers to distinguish their
.. i18n: .. products are claimed as trademarks. Where those designations appear in this book,
.. i18n: .. and Open Object Press was aware of a trademark claim, the designations have been
.. i18n: .. printed in initial capitals.
..

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. i18n: .. While every precaution has been taken in the preparation of this book, the publisher
.. i18n: .. and the authors assume no responsibility for errors or omissions, or for damages
.. i18n: .. resulting from the use of the information contained herein.
..

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. i18n: .. Published by Open Object Press, Grand Rosière, Belgium
..

.. Published by Open Object Press, Grand Rosière, Belgium
