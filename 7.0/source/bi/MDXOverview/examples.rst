A look at few examples to write MDX Queries
-------------------------------------------

Writing a simple MDX on a SALES Schema::

    select 
      {[partner_country].[all]} on rows,
      {[measures].[Items Sold]} on columns
    from sale_order_line

Gives results as,

===================== ============
 /                     Items Sold
===================== ============
 All partner_country     [43.0]
===================== ============


Expanding the partner country to its children, we change the MDX as.::

    select 
       {[partner_country].[all],[partner_country].children} on rows, 
       {[measures].[Items Sold]} on columns 
    from sale_order_line

Gives result as,

===================== ============
 /                     Items Sold
===================== ============
 All partner_country   [43.0]
 Belgium               [30.0]
 China                 [4.0]
 France                [9.0]
===================== ============

One more example bit complex with slicer::

    select 
      {[date_order].children,[date_order].[2008].children,[date_order].[2008].[Q2].children},
      {[measures].[Items Sold]} 
    from sale_order_line 
    where ([date_order].[2008])

Gives results as:

===================== ============
 /                     Items Sold
===================== ============
 2008.0                  [43.0]
 Q1                      [43.0]
===================== ============


