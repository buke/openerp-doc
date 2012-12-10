
.. i18n: .. _olap-link:
.. i18n: 
.. i18n: OLAP
.. i18n: ====
..

.. _olap-link:

OLAP
====

.. i18n: Online Analytical Processing (OLAP) means analysing large quantities of data in real-time. Unlike Online Transaction Processing (OLTP), where typical operations read and modify individual and small numbers of records, OLAP deals with data in bulk, and operations are generally read-only. The term 'online' implies that even though huge quantities of data are involved — typically many millions of records, occupying several gigabytes — the system must respond to queries fast enough to allow an interactive exploration of the data. As we shall see, that presents considerable technical challenges.
..

Online Analytical Processing (OLAP) means analysing large quantities of data in real-time. Unlike Online Transaction Processing (OLTP), where typical operations read and modify individual and small numbers of records, OLAP deals with data in bulk, and operations are generally read-only. The term 'online' implies that even though huge quantities of data are involved — typically many millions of records, occupying several gigabytes — the system must respond to queries fast enough to allow an interactive exploration of the data. As we shall see, that presents considerable technical challenges.

.. i18n: OLAP performs multidimensional analysis of business data and provides the capability for complex calculations, trend analysis, and sophisticated data modeling. Whereas a relational database stores all data in the form of rows and columns, a multidimensional dataset consists of axes and cells.
.. i18n: Consider the dataset
..

OLAP performs multidimensional analysis of business data and provides the capability for complex calculations, trend analysis, and sophisticated data modeling. Whereas a relational database stores all data in the form of rows and columns, a multidimensional dataset consists of axes and cells.
Consider the dataset

.. i18n: .. csv-table:: 
.. i18n:    :header: "Year",2000,,2001,,"Growth",
.. i18n:    
.. i18n:    "Product","Dollar sales","Unit sales","Dollar sales","Unit sales","Dollar sales","Unit sales"
.. i18n:    "Total","$7,073.00",2693,"$7,636.00",3008,8.00%,12.00%
.. i18n:    "Books","$2,753.00",824,"$3,331.00",966,21.00%,17.00%
.. i18n:    "Fiction","$1,341.00",424,"$1,202.00",380,-10.00%,-10.00%
.. i18n:    "Non-fiction","$1,412.00",400,"$2,129.00",586,51.00%,47.00%
.. i18n:    "Magazines","$2,753.00",824,"$2,426.00",766,-12.00%,-7.00%
.. i18n:    "Greetings cards","$1,567.00",1045,"$1,879.00",1276,20.00%,22.00%
..

.. csv-table:: 
   :header: "Year",2000,,2001,,"Growth",
   
   "Product","Dollar sales","Unit sales","Dollar sales","Unit sales","Dollar sales","Unit sales"
   "Total","$7,073.00",2693,"$7,636.00",3008,8.00%,12.00%
   "Books","$2,753.00",824,"$3,331.00",966,21.00%,17.00%
   "Fiction","$1,341.00",424,"$1,202.00",380,-10.00%,-10.00%
   "Non-fiction","$1,412.00",400,"$2,129.00",586,51.00%,47.00%
   "Magazines","$2,753.00",824,"$2,426.00",766,-12.00%,-7.00%
   "Greetings cards","$1,567.00",1045,"$1,879.00",1276,20.00%,22.00%

.. i18n: The rows axis consists of the members 'All products', 'Books', 'Fiction', and so forth, and the columns axis consists of the cartesian product of the years '2000' and '2001', and the calculation 'Growth', and the measures 'Unit sales' and 'Dollar sales'. Each cell represents the sales of a product category in a particular year; for example, the dollar sales of Magazines in 2001 were $2,426.
..

The rows axis consists of the members 'All products', 'Books', 'Fiction', and so forth, and the columns axis consists of the cartesian product of the years '2000' and '2001', and the calculation 'Growth', and the measures 'Unit sales' and 'Dollar sales'. Each cell represents the sales of a product category in a particular year; for example, the dollar sales of Magazines in 2001 were $2,426.

.. i18n: This is a richer view of the data than would be presented by a relational database. The members of a multidimensional dataset are not always values from a relational column. 'Total', 'Books' and 'Fiction' are members at successive levels in a hierarchy, each of which is rolled up to the next. And even though it is alongside the years '2000' and '2001', 'Growth' is a calculated member, which introduces a formula for computing cells from other cells.
..

This is a richer view of the data than would be presented by a relational database. The members of a multidimensional dataset are not always values from a relational column. 'Total', 'Books' and 'Fiction' are members at successive levels in a hierarchy, each of which is rolled up to the next. And even though it is alongside the years '2000' and '2001', 'Growth' is a calculated member, which introduces a formula for computing cells from other cells.

.. i18n: The dimensions used here — products, time, and measures — are just three of many dimensions by which the dataset can be categorized and filtered. The collection of dimensions, hierarchies and measures is called a cube.
..

The dimensions used here — products, time, and measures — are just three of many dimensions by which the dataset can be categorized and filtered. The collection of dimensions, hierarchies and measures is called a cube.

.. i18n: The above simple example or outlook shows how one can get the smallest details from the data stored for years in the database in form of relation. It helps in managing resources, forming policies , budgeting , Business Process Management, designing strategic marketing policies, forecasting and many more. The options are endless.
..

The above simple example or outlook shows how one can get the smallest details from the data stored for years in the database in form of relation. It helps in managing resources, forming policies , budgeting , Business Process Management, designing strategic marketing policies, forecasting and many more. The options are endless.

.. i18n: The multidimensional is above all a way of presenting data. Although some multidimensional databases store the data in multidimensional format, I shall argue that it is simpler to store the data in relational format and manipulate it using OLAP.
..

The multidimensional is above all a way of presenting data. Although some multidimensional databases store the data in multidimensional format, I shall argue that it is simpler to store the data in relational format and manipulate it using OLAP.

.. i18n: Who uses OLAP and Why?
.. i18n: ----------------------
..

Who uses OLAP and Why?
----------------------

.. i18n: OLAP applications span a variety of organizational functions. Finance departments use OLAP for applications such as budgeting, activity-based costing (allocations), financial performance analysis, and financial modeling. Sales analysis and forecasting are two of the OLAP applications found in sales departments. Among other applications, marketing departments use OLAP for market research analysis, sales forecasting, promotions analysis, customer analysis, and market/customer segmentation. Typical manufacturing OLAP applications include production planning and defect analysis.
..

OLAP applications span a variety of organizational functions. Finance departments use OLAP for applications such as budgeting, activity-based costing (allocations), financial performance analysis, and financial modeling. Sales analysis and forecasting are two of the OLAP applications found in sales departments. Among other applications, marketing departments use OLAP for market research analysis, sales forecasting, promotions analysis, customer analysis, and market/customer segmentation. Typical manufacturing OLAP applications include production planning and defect analysis.

.. i18n: Important to all of the above applications is the ability to provide managers with the information they need to make effective decisions about an organisation's strategic directions. The key indicator of a successful OLAP application is its ability to provide information as needed, i.e., its ability to provide "just-in-time" information for effective decision-making. This requires more than a base level of detailed data. 
..

Important to all of the above applications is the ability to provide managers with the information they need to make effective decisions about an organisation's strategic directions. The key indicator of a successful OLAP application is its ability to provide information as needed, i.e., its ability to provide "just-in-time" information for effective decision-making. This requires more than a base level of detailed data. 

.. i18n: Just-in-time information is computed data that usually reflects complex relationships and is often calculated on the fly. Analyzing and modeling complex relationships are practical only if response times are consistently short. In addition, because the nature of data relationships may not be known in advance, the data model must be flexible. A truly flexible data model ensures that OLAP systems can respond to changing business requirements as needed for effective decision making. Although OLAP applications are found in widely divergent functional areas, they all require the following key features:
..

Just-in-time information is computed data that usually reflects complex relationships and is often calculated on the fly. Analyzing and modeling complex relationships are practical only if response times are consistently short. In addition, because the nature of data relationships may not be known in advance, the data model must be flexible. A truly flexible data model ensures that OLAP systems can respond to changing business requirements as needed for effective decision making. Although OLAP applications are found in widely divergent functional areas, they all require the following key features:

.. i18n: #. Multidimensional views of data
.. i18n: 
.. i18n: #. Calculation-intensive capabilities
.. i18n: 
.. i18n: #. Time intelligence
..

#. Multidimensional views of data

#. Calculation-intensive capabilities

#. Time intelligence

.. i18n: Multidimensional views of data
.. i18n: ++++++++++++++++++++++++++++++
..

Multidimensional views of data
++++++++++++++++++++++++++++++

.. i18n: Multidimensional views are inherently representative of an actual business model. Rarely is a business model limited to fewer than three dimensions. Managers typically look at financial data by scenario (for example, actual vs. budget), organization, line items and at sales data by product, geography, channel, and time.
..

Multidimensional views are inherently representative of an actual business model. Rarely is a business model limited to fewer than three dimensions. Managers typically look at financial data by scenario (for example, actual vs. budget), organization, line items and at sales data by product, geography, channel, and time.

.. i18n: A multidimensional view of data provides more than the ability to "slice and dice"; it provides the foundation for analytical processing through flexible access to information. Database design should not prejudice which operations can be performed on a dimension or how rapidly those operations are performed. Managers must be able to analyze data across any dimension, at any level of aggregation, with equal functionality and ease. OLAP software should support these views of data in a natural and responsive fashion, insulating users of the information from complex query syntax. After all, managers should not have to understand complex table layouts, elaborate table joins, and summary tables.
..

A multidimensional view of data provides more than the ability to "slice and dice"; it provides the foundation for analytical processing through flexible access to information. Database design should not prejudice which operations can be performed on a dimension or how rapidly those operations are performed. Managers must be able to analyze data across any dimension, at any level of aggregation, with equal functionality and ease. OLAP software should support these views of data in a natural and responsive fashion, insulating users of the information from complex query syntax. After all, managers should not have to understand complex table layouts, elaborate table joins, and summary tables.

.. i18n: Whether a request is for the weekly sales of a product across all geographical areas or the year-to-date sales in a city across all products, an OLAP system must have consistent response times. Basic aggregation is performed on some of the dimensions (product, customer, and channel). More complex calculations are performed on other dimensions. The measure dimension computes ratios and averages. Variances are computed along the scenario dimension. A complex model based on historical performance is used to compute the forecast scenario. Consistently quick response times to these kinds of queries are key to establishing a server's ability to provide multidimensional views of information.
..

Whether a request is for the weekly sales of a product across all geographical areas or the year-to-date sales in a city across all products, an OLAP system must have consistent response times. Basic aggregation is performed on some of the dimensions (product, customer, and channel). More complex calculations are performed on other dimensions. The measure dimension computes ratios and averages. Variances are computed along the scenario dimension. A complex model based on historical performance is used to compute the forecast scenario. Consistently quick response times to these kinds of queries are key to establishing a server's ability to provide multidimensional views of information.

.. i18n: Calculation-intensive capabilities
.. i18n: ++++++++++++++++++++++++++++++++++
..

Calculation-intensive capabilities
++++++++++++++++++++++++++++++++++

.. i18n: The real test of an OLAP database is its ability to perform complex calculations. OLAP databases must be able to do more than simple aggregation. While aggregation along a hierarchy is important, there is more to analysis than simple data roll-ups. Examples of more complex calculations include share calculations (percentage of total) and allocations (which use hierarchies from a top-down perspective).
..

The real test of an OLAP database is its ability to perform complex calculations. OLAP databases must be able to do more than simple aggregation. While aggregation along a hierarchy is important, there is more to analysis than simple data roll-ups. Examples of more complex calculations include share calculations (percentage of total) and allocations (which use hierarchies from a top-down perspective).

.. i18n: Key performance indicators often require involved algebraic equations. Sales forecasting uses trend algorithms such as moving averages and percentage growth. Analyzing the sales and promotions of a given company and its competitors requires modeling complex relationships among the players. The real world is complicated -- the ability to model complex relationships is key in analytical processing applications.
..

Key performance indicators often require involved algebraic equations. Sales forecasting uses trend algorithms such as moving averages and percentage growth. Analyzing the sales and promotions of a given company and its competitors requires modeling complex relationships among the players. The real world is complicated -- the ability to model complex relationships is key in analytical processing applications.

.. i18n: Whereas transaction processing systems are judged on their ability to collect and manage data, analytical processing systems are judged on their ability to create information from data.
..

Whereas transaction processing systems are judged on their ability to collect and manage data, analytical processing systems are judged on their ability to create information from data.

.. i18n: Time intelligence
.. i18n: +++++++++++++++++
..

Time intelligence
+++++++++++++++++

.. i18n: Time is an integral component of almost any analytical application. Time is a unique dimension because it is sequential in character (January always comes before February). True OLAP systems understand the sequential nature of time. Business performance is almost always judged over time, for example, this month vs. last month, this month vs. the same month last year.  The time hierarchy is not always used in the same manner as other hierarchies. For example, a manager might ask to see the sales for May or the sales for the first five months of 1995. The same manager might also ask to see the sales for blue shirts but   would never ask to see the sales for the first five shirts. Concepts such as year-to-date and period over period comparisons must be easily defined in an OLAP system.
..

Time is an integral component of almost any analytical application. Time is a unique dimension because it is sequential in character (January always comes before February). True OLAP systems understand the sequential nature of time. Business performance is almost always judged over time, for example, this month vs. last month, this month vs. the same month last year.  The time hierarchy is not always used in the same manner as other hierarchies. For example, a manager might ask to see the sales for May or the sales for the first five months of 1995. The same manager might also ask to see the sales for blue shirts but   would never ask to see the sales for the first five shirts. Concepts such as year-to-date and period over period comparisons must be easily defined in an OLAP system.

.. i18n: In addition, OLAP systems must understand the concept of balances over time. For example, if a company sold 10 shirts in January, five shirts in February, and 10 shirts in March, then the total balance sold for the quarter would be 25 shirts. If, on the other hand, a company had a head count of 10 employees in January, only five employees in February, and 10 employees again in March, what was the company's employee head count for the quarter? Most companies would use an average balance. In the case of cash,    most companies use an ending balance.
..

In addition, OLAP systems must understand the concept of balances over time. For example, if a company sold 10 shirts in January, five shirts in February, and 10 shirts in March, then the total balance sold for the quarter would be 25 shirts. If, on the other hand, a company had a head count of 10 employees in January, only five employees in February, and 10 employees again in March, what was the company's employee head count for the quarter? Most companies would use an average balance. In the case of cash,    most companies use an ending balance.
