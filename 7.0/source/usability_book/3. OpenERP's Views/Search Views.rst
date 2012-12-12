
============
Search Views
============

Introduction
------------

As previously  mentioned, OpenERP is developing within a business framework and vision. When using OpenERP, users can find business applications, in these applications, they can surf on some of the business oriented views. In this search view they will also find that it facilitates the work and the search of the user. 

Search views in OpenERP allow the responsible user to search in only one view. Indeed, a Sales Responsible user, can see, in the same view, his created documents (sale orders) and, if he is allowed, the one created by his colleagues. So, in Sales Order menuitem, he can see all quotations, current sales and sales to invoice. 

.. note::

   search views are present in some of the types of views. There is a search part in calendar view, in list view and  in statistic reports. 

The terminology used to qualify each element of the search view are related to the application and also to the business context of use. For example, in sale order, there are buttons to filter different states. Instead of using a state label “Draft”, we use a label more explicit for the sales context which is “Quotations”. 

Components of search views
--------------------------

Many options are given to users to optimize their searches. Buttons are used to quickly filter groups of important documents. Usually, a button is chosen following the importance of the document's type. We can take a look at an example, in sale order, it is important that the user can quickly see only the quotations that he needs. 

In all search views there are also some selected search fields. These fields are usually chosen regarding the importance of the object (related to column of list view). An example of this would be, in sale order search view, the salesman should be able to see current sales regarding only one customer. 

.. figure:: Pictures/3.1.main_fields.png
   :align: center


Some buttons allow users to group by elements, for example, salesman can group by customer and see, for each customer, all the sale orders they have made. 

.. figure:: Pictures/3.2group_by.png
   :align: center


Finally, OpenERP allows users to search following most of the elements we can find in form view with personal filter. Thanks to these filters, we can lighten and clear the view. If users want see all leads that come from one state in the United-States, they can add a filter easily and then save it as a preference, this is especially useful if they have to use it often. 

.. figure:: Pictures/3.3.other_fields.png
   :align: center


.. note::

	In extended view, in some search views, there are extended filters. These are used to allow user filtering on important elements but are not specific to a 		list view. For example, in Leads, there is not the Lead's country in the Lead list view, but, it regularly happens that Salesman want to filter all Leads 		by a specific country. It also allows you to modify columns of the list view by adding one. This kind of field is only on the extended interface and not in all 		search views. Our goal is to simplify, so if it is not necessary, there are no extended filters. A user can always use a personal filter.  

.. figure:: Pictures/3.4.extended_filters.png
   :align: center
       


