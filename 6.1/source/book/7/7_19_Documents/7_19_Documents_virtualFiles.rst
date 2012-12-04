
.. index::
   single: virtual; file

Virtual Files
=============

The most well-organized companies keep track of all the documents they have sent to customers in their
document management system. It is very useful to be able to retrieve every document about a customer
or a project. But the work of storing these documents can itself often take up quite a bit of time
for staff. Each report must be saved in the document management system as well as be sent
by email to the customer.

That is not the case in OpenERP. To automatically make OpenERP reports available in the FTP server,
OpenERP automatically uses *virtual files*. You can put virtual files into directories
that have the special type of *linked resource* and link the virtual files to OpenERP's reports.

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

The screen :ref:`fig-docvirt` shows the parameters of the virtual files in All Sales Order. You define the virtual files
using the name ORDERNUM_print.pdf, where ORDERNUM represents the reference to the order. To do
this, you must check the option :guilabel:`Include Record Name` of the file for a directory. 
You can then find a virtual file for each report associated with an order.

.. _fig-docvirt:

.. figure::  images/document_virtual_form.png
   :scale: 75
   :align: center

   *Virtual files for Sales Orders in OpenERP*

To see the effect of this configuration, connect to the FTP server and go into a directory for an
order such as :menuselection:`Documents --> Sales Order --> All Sales Order --> SO003`. You
can then just click the file :guilabel:`SO003_print.pdf` to get a printout of Order SO003.
You can attach it to an email or put it on your desktop.

.. figure::  images/document_virtual_ftp.png
   :scale: 75
   :align: center

   *Virtual files for Sales Orders through FTP*

This system of virtual files is very useful in a lot of situations. For example, if you must quickly
re-send a quotation to a customer, you do not have to open OpenERP, you can just attach the relevant
virtual file to your email.

Importantly, once files have been read or copied, they become real files, taking up real space, rather than
just virtual. This means that you can keep a legal record of all documents that have been created and sent
to customers and suppliers.


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
