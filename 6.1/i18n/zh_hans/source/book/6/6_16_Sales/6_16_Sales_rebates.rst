.. i18n: Rebates at the End of a Campaign
.. i18n: ================================
..

活动结束后的回佣
================================

.. i18n: If you want to provide discounts on an order, you can use the pricelist system in OpenERP. But we would not be writing about end-of-campaign rebates if no other solution was available. You can also work with end-of-campaign rebates or year-end rebates. The customer pays a certain price during the whole of the campaign or the year, and he will receive a rebate at the end of the campaign according to the sales made throughout the year.
..

If you want to provide discounts on an order, you can use the pricelist system in OpenERP. But we would not be writing about end-of-campaign rebates if no other solution was available. You can also work with end-of-campaign rebates or year-end rebates. The customer pays a certain price during the whole of the campaign or the year, and he will receive a rebate at the end of the campaign according to the sales made throughout the year.

.. i18n: Take the case of contract negotiations with a wholesaler. To get the best selling price, the
.. i18n: wholesaler will ask you for a good deal and will sign up to a certain volume of orders over
.. i18n: the year.
..

Take the case of contract negotiations with a wholesaler. To get the best selling price, the
wholesaler will ask you for a good deal and will sign up to a certain volume of orders over
the year.

.. i18n: You can then propose a price based on the volume that the wholesaler agrees to sell. But then you
.. i18n: do not have any control over his orders. If at the end of the year the wholesaler has not taken the
.. i18n: agreed volumes, you can do nothing. At most you can review his terms for the following year.
..

You can then propose a price based on the volume that the wholesaler agrees to sell. But then you
do not have any control over his orders. If at the end of the year the wholesaler has not taken the
agreed volumes, you can do nothing. At most you can review his terms for the following year.

.. i18n: Rebates at the end of a campaign can help you avoid this sort of problem. You can propose a contract
.. i18n: where the price depends on the usual wholesaler's terms. You can propose a rebate grid which
.. i18n: will be assigned at the end of the year as a function of the actual sales made.
..

Rebates at the end of a campaign can help you avoid this sort of problem. You can propose a contract
where the price depends on the usual wholesaler's terms. You can propose a rebate grid which
will be assigned at the end of the year as a function of the actual sales made.

.. i18n: .. index::
.. i18n:    single: module; discount_campaign
..

.. index::
   single: module; discount_campaign

.. i18n: Install the :mod:`discount_campaign` module (in ``extra-addons`` at the time of writing)
.. i18n: to generate rebates at the end of the campaign. Once the modules have been installed, you can configure your campaign using the menu :menuselection:`Sales --> Configuration --> Sales --> Discount Campaigns`.
..

Install the :mod:`discount_campaign` module (in ``extra-addons`` at the time of writing)
to generate rebates at the end of the campaign. Once the modules have been installed, you can configure your campaign using the menu :menuselection:`Sales --> Configuration --> Sales --> Discount Campaigns`.

.. i18n: .. note:: Year-end Rebate
.. i18n: 
.. i18n:    Most companies use the term *year-end rebate*, where rebates are applied at the end of the year.
.. i18n:    But of course you can also define rebates for a campaign that lasts less than or more than one year.
..

.. note:: Year-end Rebate

   Most companies use the term *year-end rebate*, where rebates are applied at the end of the year.
   But of course you can also define rebates for a campaign that lasts less than or more than one year.

.. i18n: .. figure:: images/discount_campaign_RFA.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Configuring a Campaign Rebate*
..

.. figure:: images/discount_campaign_RFA.png
   :scale: 75
   :align: center

   *Configuring a Campaign Rebate*

.. i18n: A campaign should have a name, a refund journal (to create the credit notes at the end of the campaign), a start date, and an end date. After entering this information, you should describe the lines of the campaign. Each line can be applied to a product or a category of
.. i18n: products. Then set the quantity of products sold from which the discount is applied, and the amount
.. i18n: of the rebate as a percentage of the actual sales volume.
..

A campaign should have a name, a refund journal (to create the credit notes at the end of the campaign), a start date, and an end date. After entering this information, you should describe the lines of the campaign. Each line can be applied to a product or a category of
products. Then set the quantity of products sold from which the discount is applied, and the amount
of the rebate as a percentage of the actual sales volume.

.. i18n: When you have defined the campaign, you can activate it by clicking the :guilabel:`Open` button. The
.. i18n: figure :ref:`fig-discamp` shows a campaign with a rebate on computers which is between 10% and 20% depending on
.. i18n: the sales volume.
..

When you have defined the campaign, you can activate it by clicking the :guilabel:`Open` button. The
figure :ref:`fig-discamp` shows a campaign with a rebate on computers which is between 10% and 20% depending on
the sales volume.

.. i18n: .. _fig-discamp:
.. i18n: 
.. i18n: .. figure:: images/discount_campaign.png
.. i18n:    :scale: 75
.. i18n:    :align: center
.. i18n: 
.. i18n:    *Configuring a Discount Campaign for Computers*
..

.. _fig-discamp:

.. figure:: images/discount_campaign.png
   :scale: 75
   :align: center

   *Configuring a Discount Campaign for Computers*

.. i18n: Once the campaign has been defined and activated, you can assign it to various partners. To do that
.. i18n: set a :guilabel:`Discount Campaign` in the second tab :guilabel:`Sales & Purchases` of the partner form.
..

Once the campaign has been defined and activated, you can assign it to various partners. To do that
set a :guilabel:`Discount Campaign` in the second tab :guilabel:`Sales & Purchases` of the partner form.

.. i18n: Finally, at the end of the campaign, you should close it and OpenERP will automatically generate
.. i18n: invoices or credit notes for your partner associated with this campaign. OpenERP opens credit
.. i18n: notes in the ``Draft`` state so you can modify them before validation. To calculate the amount on the
.. i18n: credit note, OpenERP uses all of the invoices sent out during the period of the campaign as a
.. i18n: basis.
..

Finally, at the end of the campaign, you should close it and OpenERP will automatically generate
invoices or credit notes for your partner associated with this campaign. OpenERP opens credit
notes in the ``Draft`` state so you can modify them before validation. To calculate the amount on the
credit note, OpenERP uses all of the invoices sent out during the period of the campaign as a
basis.

.. i18n: You can also get an overview of all draft credit notes using the menu :menuselection:`Accounting
.. i18n: --> Customers --> Customer Refunds`.
..

You can also get an overview of all draft credit notes using the menu :menuselection:`Accounting
--> Customers --> Customer Refunds`.

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
