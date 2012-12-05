
.. i18n: ============
.. i18n: Search Views
.. i18n: ============
..

============
Search Views
============

.. i18n: How organize a search view
.. i18n: ++++++++++++++++++++++++++
..

How organize a search view
++++++++++++++++++++++++++

.. i18n: .. figure:: Pictures/3.5.search_view.png
.. i18n:    :align: center
..

.. figure:: Pictures/3.5.search_view.png
   :align: center

.. i18n: Filtering buttons and main filter fields must be the first elements on top of the view, and on the same line. Below this main filter option,  you must place extended filters and group by one above the other. Each field group must be placed in a new line. Finally, the search bar must be below the view as displayed in the picture above. 
..

Filtering buttons and main filter fields must be the first elements on top of the view, and on the same line. Below this main filter option,  you must place extended filters and group by one above the other. Each field group must be placed in a new line. Finally, the search bar must be below the view as displayed in the picture above. 

.. i18n: Use a business oriented terminology
.. i18n: +++++++++++++++++++++++++++++++++++
..

Use a business oriented terminology
+++++++++++++++++++++++++++++++++++

.. i18n: As previously mentioned, the used terminology must be adapted to the application. An example of this would be, in sale order the search field “partner_id” is named “Customer” and in purchase application, the same search field is named “Supplier”. In the same way, the “user_id” field in sales is named “Salesman” and in project management, it is named “Project Manager”. 
..

As previously mentioned, the used terminology must be adapted to the application. An example of this would be, in sale order the search field “partner_id” is named “Customer” and in purchase application, the same search field is named “Supplier”. In the same way, the “user_id” field in sales is named “Salesman” and in project management, it is named “Project Manager”. 

.. i18n: Filter Button Details 
.. i18n: +++++++++++++++++++++
..

Filter Button Details 
+++++++++++++++++++++

.. i18n: * These kinds of buttons are on the top left of the screen. 
.. i18n: * Filtering buttons are grouped by context (more often States and Dates).
.. i18n: * Inside a single group, button behavior is exclusive. 
.. i18n: * Each context is separated by a vertical separator. 
.. i18n: * The first group is always related to states (Current, Pending or Open).
..

* These kinds of buttons are on the top left of the screen. 
* Filtering buttons are grouped by context (more often States and Dates).
* Inside a single group, button behavior is exclusive. 
* Each context is separated by a vertical separator. 
* The first group is always related to states (Current, Pending or Open).

.. i18n: Then there are other buttons in one or more groups, it depends on the context. These are specific to the current view. For instance, in sale orders, we have “to invoice”. Finally, if there are buttons related to the date such as, “This Month” or “Today”, it has to be last group on the right. 
..

Then there are other buttons in one or more groups, it depends on the context. These are specific to the current view. For instance, in sale orders, we have “to invoice”. Finally, if there are buttons related to the date such as, “This Month” or “Today”, it has to be last group on the right. 

.. i18n: .. note::
.. i18n: 
.. i18n:    In statistic reports search views, filter buttons related to dates are first on the left. Because user date is important, statistics is often computed on a given time. A sales manager wants to see statistics of the month or of the year. 
..

.. note::

   In statistic reports search views, filter buttons related to dates are first on the left. Because user date is important, statistics is often computed on a given time. A sales manager wants to see statistics of the month or of the year. 

.. i18n: * If there is a current button, it is generally selected by default. This button filters all draft and open documents. This is  usually selected by default to avoid seeing cancelled and closed documents.
..

* If there is a current button, it is generally selected by default. This button filters all draft and open documents. This is  usually selected by default to avoid seeing cancelled and closed documents.

.. i18n: Main Filter Options reflects columns of the list view
.. i18n: +++++++++++++++++++++++++++++++++++++++++++++++++++++
..

Main Filter Options reflects columns of the list view
+++++++++++++++++++++++++++++++++++++++++++++++++++++

.. i18n: * Default search fields might reflect the available columns in the list view. In other words, each field must have a related column in the list view and is placed in the same position as the column.
.. i18n: * Near fields like “user_id” or “section_id”, following the current view context, we can find some buttons
.. i18n: 
.. i18n:    - near “user_id” field we can find the following buttons :
.. i18n:  
.. i18n:       + this filters all documents of the current user and is named “My..”
.. i18n:       + this filters all unassigned documents. This button is used in views where documents are self generated such as leads. 
.. i18n: 
.. i18n:    - Near “section_id” we can find buttons generally used in views related to sale's applications. This button shows documents linked with current user's department(sales/marketing/HR,etc.). 
..

* Default search fields might reflect the available columns in the list view. In other words, each field must have a related column in the list view and is placed in the same position as the column.
* Near fields like “user_id” or “section_id”, following the current view context, we can find some buttons

   - near “user_id” field we can find the following buttons :
 
      + this filters all documents of the current user and is named “My..”
      + this filters all unassigned documents. This button is used in views where documents are self generated such as leads. 

   - Near “section_id” we can find buttons generally used in views related to sale's applications. This button shows documents linked with current user's department(sales/marketing/HR,etc.). 

.. i18n: Group by : organization
.. i18n: +++++++++++++++++++++++
..

Group by : organization
+++++++++++++++++++++++

.. i18n: * like buttons, “group by” are organized in context. 
.. i18n: * The first group is related to human resources, the second group is related to the state of the document. The third group is related to a place, and finally the last group is related to dates. 
.. i18n: * A separator is defined between each group. For example : Salesman Partner | Stage State | Shop Company | Day Month Year
.. i18n: * Use appropriate icons as defined in :ref:`button-icon-list-link`.
.. i18n: * In all search views, except for report's search view, groups by must be folded. The goal is to have simple view by default. 
..

* like buttons, “group by” are organized in context. 
* The first group is related to human resources, the second group is related to the state of the document. The third group is related to a place, and finally the last group is related to dates. 
* A separator is defined between each group. For example : Salesman Partner | Stage State | Shop Company | Day Month Year
* Use appropriate icons as defined in :ref:`button-icon-list-link`.
* In all search views, except for report's search view, groups by must be folded. The goal is to have simple view by default. 

.. i18n: Use of Extended Filters
.. i18n: +++++++++++++++++++++++
..

Use of Extended Filters
+++++++++++++++++++++++

.. i18n: * There are extended filters only in extended interface because it complicates the views. In the simplified interface, the user can use optional filters.
.. i18n: * By default, extended filters are folded.
.. i18n: * Generally, the user can find important fields in extended filters, but it is possible that no column is linked to the field. 
.. i18n: * Extended filters also give you the possibility to add columns that users might need. 
..

* There are extended filters only in extended interface because it complicates the views. In the simplified interface, the user can use optional filters.
* By default, extended filters are folded.
* Generally, the user can find important fields in extended filters, but it is possible that no column is linked to the field. 
* Extended filters also give you the possibility to add columns that users might need. 

.. i18n: .. figure:: Pictures/3.7.extended_filter_button.png
.. i18n:    :align: center
..

.. figure:: Pictures/3.7.extended_filter_button.png
   :align: center
