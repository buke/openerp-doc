
.. i18n: A look at few examples to write MDX Queries
.. i18n: -------------------------------------------
..

A look at few examples to write MDX Queries
-------------------------------------------

.. i18n: Writing a simple MDX on a SALES Schema::
.. i18n: 
.. i18n:     select 
.. i18n:       {[partner_country].[all]} on rows,
.. i18n:       {[measures].[Items Sold]} on columns
.. i18n:     from sale_order_line
..

Writing a simple MDX on a SALES Schema::

    select 
      {[partner_country].[all]} on rows,
      {[measures].[Items Sold]} on columns
    from sale_order_line

.. i18n: Gives results as,
..

Gives results as,

.. i18n: ===================== ============
.. i18n:  /                     Items Sold
.. i18n: ===================== ============
.. i18n:  All partner_country     [43.0]
.. i18n: ===================== ============
..

===================== ============
 /                     Items Sold
===================== ============
 All partner_country     [43.0]
===================== ============

.. i18n: Expanding the partner country to its children, we change the MDX as.::
.. i18n: 
.. i18n:     select 
.. i18n:        {[partner_country].[all],[partner_country].children} on rows, 
.. i18n:        {[measures].[Items Sold]} on columns 
.. i18n:     from sale_order_line
..

Expanding the partner country to its children, we change the MDX as.::

    select 
       {[partner_country].[all],[partner_country].children} on rows, 
       {[measures].[Items Sold]} on columns 
    from sale_order_line

.. i18n: Gives result as,
..

Gives result as,

.. i18n: ===================== ============
.. i18n:  /                     Items Sold
.. i18n: ===================== ============
.. i18n:  All partner_country   [43.0]
.. i18n:  Belgium               [30.0]
.. i18n:  China                 [4.0]
.. i18n:  France                [9.0]
.. i18n: ===================== ============
..

===================== ============
 /                     Items Sold
===================== ============
 All partner_country   [43.0]
 Belgium               [30.0]
 China                 [4.0]
 France                [9.0]
===================== ============

.. i18n: One more example bit complex with slicer::
.. i18n: 
.. i18n:     select 
.. i18n:       {[date_order].children,[date_order].[2008].children,[date_order].[2008].[Q2].children},
.. i18n:       {[measures].[Items Sold]} 
.. i18n:     from sale_order_line 
.. i18n:     where ([date_order].[2008])
..

One more example bit complex with slicer::

    select 
      {[date_order].children,[date_order].[2008].children,[date_order].[2008].[Q2].children},
      {[measures].[Items Sold]} 
    from sale_order_line 
    where ([date_order].[2008])

.. i18n: Gives results as:
..

Gives results as:

.. i18n: ===================== ============
.. i18n:  /                     Items Sold
.. i18n: ===================== ============
.. i18n:  2008.0                  [43.0]
.. i18n:  Q1                      [43.0]
.. i18n: ===================== ============
..

===================== ============
 /                     Items Sold
===================== ============
 2008.0                  [43.0]
 Q1                      [43.0]
===================== ============
