
.. index:: payment terms

Payment Terms
=============

You can define whatever payment terms you need in OpenERP. Payment terms determine the due dates
for paying an invoice.

To define new payment terms, use the menu :menuselection:`Accounting -->
Configuration --> Miscellaneous --> Payment Terms` and then click :guilabel:`New`.

The figure below represents the following payment term: 5000 within 5 days, 50% payment at the last day of current month,
Remaining on 15th of next month.

.. figure::  images/account_payment_term.png
   :scale: 75
   :align: center

   *Configuring payment terms*

To configure new conditions, start by giving a name to the :guilabel:`Payment Term` field. Text that
you put in the field :guilabel:`Description on invoices`, is used on invoices, so enter a clear description of
the payment terms there.

Then create individual lines for calculating the terms in the section :guilabel:`Payment Term`. You
must give each line a name (:guilabel:`Line Name`). These give an informative title and do not affect
the actual calculation of terms. The :guilabel:`Sequence` field lets you define the order in which
the rules are evaluated.

The :guilabel:`Valuation` field enables you to calculate the amount to pay for each line:

* ``Percent`` : the line corresponds to a percentage of the total amount, the factor being
  given in :guilabel:`Value Amount`. The number indicated in :guilabel:`Value Amount` must take a value between 0 and 1.

* ``Fixed Amount`` : this is a fixed value given by the :guilabel:`Value Amount` box.

* ``Balance`` : indicates the balance remaining after accounting for the other lines.

Think carefully about setting the last line of the calculation to \ ``Balance`` \, to avoid rounding
errors. The highest sequence number is evaluated last.

The two last fields, :guilabel:`Number of Days` and :guilabel:`Day of the Month`, enable the calculation of
the delay in payment for each line. The delay :guilabel:`Day of the Month` can be set to \ ``-1`` \, \ ``0`` \
or any positive number. For example, if today is 20th December 2010, and if you want to set payment terms like this:

* :guilabel:`5000 within 5 days`: set `Valuation` ``Fixed Amount``, `Number of Days` ``5`` and `Day of the Month` ``0``. That creates journal entry for date 25th December 2010.
* :guilabel:`50% payment at the last day of current month`: set `Valuation` ``Percent``, `Number of Days` ``0`` and  `Day of the Month` ``-1``. That creates journal entry for date 31st December 2010.
* :guilabel:`Remaining on 15th of next month`: set `Valuation` ``Balance``, `Number of Days` ``0`` and  `Day of the Month` ``15``. That creates journal entry for date 15th January 2011.

You can then add payment terms to a Partner through the tab :guilabel:`Accounting` on the partner form.

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
