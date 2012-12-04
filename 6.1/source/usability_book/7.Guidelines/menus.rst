
=======================
Menu Organization Rules
=======================

Menu organization
+++++++++++++++++

* The first items of the main menu (application management) must be the most useful documents of the application. There are 2 reasons for this: 

  * users must have direct and easy access to their documents, usually, most important features which correspond to daily operations.
  * In web client, this first menu is unfolded by default

    .. figure:: Pictures/webmenu.png
       :align: center

* If the application contains the object “res.partner” it is always after the main menu. Because, it is important to have easy access to the suppliers in “purchases” or the customers in “sales”. 
* “Configuration” is always the last menu item in an application. By default, only “admin / configuration” has access to this menu. 
* “Reporting” is always before “Configuration”. For managers it is the last item.
* If the application contains the object “res.product”, it is always before “Reporting” (from user side, it is the last item)
* the invoice object; if there is one in the application, it must be before “Products)
* All other menus are organized in a logical order. For example, in “Human Resources”, user have generally more often the need for “Time Tracking” than “Expenses”. So “Time Tracking” is placed before “Expenses”

To summarize menus have to look like :

* Main application 
* (Address book)
* …
* (Billings)
* (Product)
* Reporting
* Configuration

Menu terminology
++++++++++++++++

The name must be short and explicit. Firstly, it must be short because in web client, main menus are organized on the top, in a horizontal bar. So it cannot take too much space. For instance we use “Purchases”, not “Purchases Management”, to minimise the space taken in the menu. 

.. figure:: Pictures/menubar.png
   :align: center

Secondly, used terminology must be linked to the application and explicit to it. For example, res.partner object is named “Customer” in “sales” and “Supplier” in “Purchase”.
