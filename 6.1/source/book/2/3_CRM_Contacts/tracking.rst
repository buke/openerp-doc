
.. _part2-crm-tracking:
 
####################################
Keeping Track of your Communications
####################################


Tracking your Customer's History
--------------------------------

Information related to leads & opportunities, meetings, phone calls,  marketing campaigns and emails will be tracked in OpenERP. 
The activities are automatically reported in the partner form of the associated customer. To have a complete overview of the activities for a customer, all you have to do is open the **Customer** form and click the `History` tab. As you will notice in the screenshot below, this is not merely a report. From this tab, you can also plan new activities for the customer or change existing activities!

.. figure:: images/crm_partner_event.png
   :scale: 80
   :align: center

   *History of Activities in a Customer Form*

Tracking Sales Orders
---------------------

After intensive opportunity qualification, your customer asks you to make a quotation. You can easily do this from the corresponding opportunity! Just click the ``Convert to Quote`` button and OpenERP will create a sales quotation ready for you to be edited. A sales quotation is an unconfirmed sales order. On the quotation, the Source document it was created from (in this case the opportunity) is displayed, to allow you to keep track of which opportunity is linked to which sales quotation / order.

To review the quotation later, you can access it from the :menuselection:`Sales --> Sales --> Sales Orders` menu. On the `Extra Info` tab of the sales quotation, you can find the reference to the related sales quotation / order that has been created from the opportunity concerned.

For more information about sales orders, please refer to the chapter :ref:`part4-crm-sales`.

.. index:: attachments

Storing Attached Documents
--------------------------

For any object in OpenERP, for instance a lead, opportunity, customer, you can attach external documents. Suppose you send a product folder to one of your customers, and to make sure you know exactly which version of the document he received, you can keep it as an attachment in OpenERP.

To attach whatever type of document to the customer, you just have to go to the :menuselection:`Sales --> Address Book --> Customers` menu.

Open the Customer form of the selected partner, and click the `Add` button in the Action bar, just below `Attachments`. Then click the `Browse...` button and navigate to the location where the product folder is stored, just like you would do in your file explorer. Click the product folder, and then confirm.

The product folder is now stored in OpenERP as an attachment for the customer. You can open it by clicking the document in Attachments.

OpenERP allows you to add as many attachments as needed. Combined with the `Knowledge` application, OpenERP will index documents of the type .doc, .pdf, .sxw and .odt, so that you can effortlessly search through their content.
 
.. note::  File Storage

   If you do not install the Document Management system (`Knowledge` application) then the attachments in OpenERP are stored
   directly in the database.
   Once the document management system has been installed,
   the contents of the files are no longer stored in the database, but on the OpenERP
   server file system.

   You can then read and add attachments to OpenERP quite independently of the OpenERP
   interface or the FTP server using simple drag and drop.

For more information about the Knowledge and Document Management System, please refer to the online documentation.


.. Copyright © Open Object Press. All rights reserved.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the OpenERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. Published by Open Object Press, Grand Rosière, Belgium


.. Copyright © Open Object Press. All rights reserved.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the OpenERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. Published by Open Object Press, Grand Rosière, Belgium

