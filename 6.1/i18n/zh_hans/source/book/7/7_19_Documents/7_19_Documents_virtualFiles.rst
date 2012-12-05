
.. i18n: .. index::
.. i18n:    single: virtual; file
..

.. index::
   single: virtual; file

.. i18n: Virtual Files
.. i18n: =============
..

Virtual Files
=============

.. i18n: The most well-organized companies keep track of all the documents they have sent to customers in their
.. i18n: document management system. It is very useful to be able to retrieve every document about a customer
.. i18n: or a project. But the work of storing these documents can itself often take up quite a bit of time
.. i18n: for staff. Each report must be saved in the document management system as well as be sent
.. i18n: by email to the customer.
..

The most well-organized companies keep track of all the documents they have sent to customers in their
document management system. It is very useful to be able to retrieve every document about a customer
or a project. But the work of storing these documents can itself often take up quite a bit of time
for staff. Each report must be saved in the document management system as well as be sent
by email to the customer.

.. i18n: That is not the case in OpenERP. To automatically make OpenERP reports available in the FTP server,
.. i18n: OpenERP automatically uses *virtual files*. You can put virtual files into directories
.. i18n: that have the special type of *linked resource* and link the virtual files to OpenERP's reports.
..

That is not the case in OpenERP. To automatically make OpenERP reports available in the FTP server,
OpenERP automatically uses *virtual files*. You can put virtual files into directories
that have the special type of *linked resource* and link the virtual files to OpenERP's reports.

.. i18n: .. note:: Virtual Files
.. i18n: 
.. i18n:     Virtual files do not actually exist in OpenERP but are made visible with a size of 0 in the FTP
.. i18n:     server.
.. i18n:     Once these files have been read by the client software, OpenERP prints the document related to
.. i18n:     this file and
.. i18n:     returns a PDF document linked to the resource.
.. i18n: 
.. i18n:     When you copy or open a virtual file you print the selected resource.
.. i18n:     You do not then have to go and print a document through OpenERP –
.. i18n:     you just open the file containing that document in the document management system.
.. i18n:     The PDF file is then created in real time by OpenERP by reading the relevant data.
..

.. note:: Virtual Files

    Virtual files do not actually exist in OpenERP but are made visible with a size of 0 in the FTP
    server.
    Once these files have been read by the client software, OpenERP prints the document related to
    this file and
    returns a PDF document linked to the resource.

    When you copy or open a virtual file you print the selected resource.
    You do not then have to go and print a document through OpenERP –
    you just open the file containing that document in the document management system.
    The PDF file is then created in real time by OpenERP by reading the relevant data.

.. i18n: The screen :ref:`fig-docvirt` shows the parameters of the virtual files in All Sales Order. You define the virtual files
.. i18n: using the name ORDERNUM_print.pdf, where ORDERNUM represents the reference to the order. To do
.. i18n: this, you must check the option :guilabel:`Include Record Name` of the file for a directory. 
.. i18n: You can then find a virtual file for each report associated with an order.
..

The screen :ref:`fig-docvirt` shows the parameters of the virtual files in All Sales Order. You define the virtual files
using the name ORDERNUM_print.pdf, where ORDERNUM represents the reference to the order. To do
this, you must check the option :guilabel:`Include Record Name` of the file for a directory. 
You can then find a virtual file for each report associated with an order.

.. i18n: .. _fig-docvirt:
.. i18n: 
.. i18n: .. figure::  images/document_virtual_form.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Virtual files for Sales Orders in OpenERP*
..

.. _fig-docvirt:

.. figure::  images/document_virtual_form.png
   :scale: 75
   :align: center

   *Virtual files for Sales Orders in OpenERP*

.. i18n: To see the effect of this configuration, connect to the FTP server and go into a directory for an
.. i18n: order such as :menuselection:`Documents --> Sales Order --> All Sales Order --> SO003`. You
.. i18n: can then just click the file :guilabel:`SO003_print.pdf` to get a printout of Order SO003.
.. i18n: You can attach it to an email or put it on your desktop.
..

To see the effect of this configuration, connect to the FTP server and go into a directory for an
order such as :menuselection:`Documents --> Sales Order --> All Sales Order --> SO003`. You
can then just click the file :guilabel:`SO003_print.pdf` to get a printout of Order SO003.
You can attach it to an email or put it on your desktop.

.. i18n: .. figure::  images/document_virtual_ftp.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Virtual files for Sales Orders through FTP*
..

.. figure::  images/document_virtual_ftp.png
   :scale: 75
   :align: center

   *Virtual files for Sales Orders through FTP*

.. i18n: This system of virtual files is very useful in a lot of situations. For example, if you must quickly
.. i18n: re-send a quotation to a customer, you do not have to open OpenERP, you can just attach the relevant
.. i18n: virtual file to your email.
..

This system of virtual files is very useful in a lot of situations. For example, if you must quickly
re-send a quotation to a customer, you do not have to open OpenERP, you can just attach the relevant
virtual file to your email.

.. i18n: Importantly, once files have been read or copied, they become real files, taking up real space, rather than
.. i18n: just virtual. This means that you can keep a legal record of all documents that have been created and sent
.. i18n: to customers and suppliers.
..

Importantly, once files have been read or copied, they become real files, taking up real space, rather than
just virtual. This means that you can keep a legal record of all documents that have been created and sent
to customers and suppliers.

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
