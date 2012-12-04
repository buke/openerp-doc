
Alerts
======

.. index:: 
   single: warning
   single: alerts
   single: module; warning

To manage alerts on products or partners, you can install the :mod:`warning` module. Once that is
installed, you will be able to configure a series of alerts on the partners or products by
setting parameters in the new :guilabel:`Warnings` tab on each of the forms.

You can select any of the following types of warnings and create different warnings for purchases and for sales:

* :guilabel:`No Message`: This option will not display a message.

* :guilabel:`Warning`: This option will show the user the message entered.

* :guilabel:`Blocking Message`: The message displayed will cause an exception and block the workflow.

You can activate alerts for a series of events. For each alert, you should enter a message that will
be displayed when the event concerned is started.

.. figure:: images/warning_partner.png
   :scale: 75
   :align: center

   *Management of alerts on partners*

The available warnings in the partner form are:

* Create a warning for a sales order,

* Create a warning for a purchase order,

* Create a warning for a delivery to a partner (or receiving an item),

* Create a warning when invoicing a partner.

For example, if you enter an alert for the invoicing of a customer, for an accountant entering an
invoice for that customer, the alert message will be attached as shown in the figure :ref:`fig-warnsmp`.

.. _fig-warnsmp:

.. figure:: images/warning_sample.png
   :scale: 75
   :align: center

   *Alert from Invoicing a Customer*

.. figure:: images/warning_product.png
   :scale: 75
   :align: center

   *Management of Alerts on Products*

The alerts that can be configured on a product form are related to:

* The sales of that product,

* The purchase of that product.

A practical example:

Now when could you use such an alert? Suppose that your customer asks you to never make any deliveries on Tuesday morning, because the street is blocked due to a weekly market. You surely would like your transporter to be aware of this, so it could be useful to have a kind of message printed by default on each delivery order for this customer.
To do this, you could create a Warning on the Picking in the **Customer** form of the partner concerned, saying that no deliveries are allowed on Tuesday morning.

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
