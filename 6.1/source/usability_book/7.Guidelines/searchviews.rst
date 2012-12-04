============
Search Views
============

How organize a search view
++++++++++++++++++++++++++

.. figure:: Pictures/3.5.search_view.png
   :align: center


Filtering buttons and main filter fields must be the first elements on top of the view, and on the same line. Below this main filter option,  you must place extended filters and group by one above the other. Each field group must be placed in a new line. Finally, the search bar must be below the view as displayed in the picture above. 


Use a business oriented terminology
+++++++++++++++++++++++++++++++++++

As previously mentioned, the used terminology must be adapted to the application. An example of this would be, in sale order the search field “partner_id” is named “Customer” and in purchase application, the same search field is named “Supplier”. In the same way, the “user_id” field in sales is named “Salesman” and in project management, it is named “Project Manager”. 


Filter Button Details 
+++++++++++++++++++++

* These kinds of buttons are on the top left of the screen. 
* Filtering buttons are grouped by context (more often States and Dates).
* Inside a single group, button behavior is exclusive. 
* Each context is separated by a vertical separator. 
* The first group is always related to states (Current, Pending or Open).

Then there are other buttons in one or more groups, it depends on the context. These are specific to the current view. For instance, in sale orders, we have “to invoice”. Finally, if there are buttons related to the date such as, “This Month” or “Today”, it has to be last group on the right. 

.. note::

   In statistic reports search views, filter buttons related to dates are first on the left. Because user date is important, statistics is often computed on a given time. A sales manager wants to see statistics of the month or of the year. 

* If there is a current button, it is generally selected by default. This button filters all draft and open documents. This is  usually selected by default to avoid seeing cancelled and closed documents.

Main Filter Options reflects columns of the list view
+++++++++++++++++++++++++++++++++++++++++++++++++++++

* Default search fields might reflect the available columns in the list view. In other words, each field must have a related column in the list view and is placed in the same position as the column.
* Near fields like “user_id” or “section_id”, following the current view context, we can find some buttons

   - near “user_id” field we can find the following buttons :
 
      + this filters all documents of the current user and is named “My..”
      + this filters all unassigned documents. This button is used in views where documents are self generated such as leads. 

   - Near “section_id” we can find buttons generally used in views related to sale's applications. This button shows documents linked with current user's department(sales/marketing/HR,etc.). 


Group by : organization
+++++++++++++++++++++++

* like buttons, “group by” are organized in context. 
* The first group is related to human resources, the second group is related to the state of the document. The third group is related to a place, and finally the last group is related to dates. 
* A separator is defined between each group. For example : Salesman Partner | Stage State | Shop Company | Day Month Year
* Use appropriate icons as defined in :ref:`button-icon-list-link`.
* In all search views, except for report's search view, groups by must be folded. The goal is to have simple view by default. 

Use of Extended Filters
+++++++++++++++++++++++

* There are extended filters only in extended interface because it complicates the views. In the simplified interface, the user can use optional filters.
* By default, extended filters are folded.
* Generally, the user can find important fields in extended filters, but it is possible that no column is linked to the field. 
* Extended filters also give you the possibility to add columns that users might need. 

.. figure:: Pictures/3.7.extended_filter_button.png
   :align: center
