
Packaging
=========

Products can be managed in several packaged forms. For example, if you sell
batteries you can define the following packages for a given battery product:

* Piece: a battery,

* Blister Pack: a pack of 4 batteries,

* Pack of 100 blisters: 400 batteries,

* Palette: 40 packs for a total of 16,000 batteries.

OpenERP's package management enables you to sell the same product in several different forms. The
salesperson could sell separately, one battery or a palette of batteries. In the order, you can
select the default packaging type as a function of the quantities ordered.

For example, if the customer wants to buy 30,000 batteries, the salesperson can select the ``palette`` package. OpenERP will then propose to sell 32,000 batteries, which corresponds to two palettes. Or the salesperson can select 75 packs.

The available packages are defined in the product form, in the :guilabel:`Packaging` tab. The first item on the
list is the one that will be used by default.

Once a package has been defined on the order, OpenERP will throw up an alert if the ordered
quantities do not correspond to the proposed packages. The quantity must be a multiple of the field
:guilabel:`Quantity by Package` defined on the packaging form.

.. figure:: images/sale_warning_packaging.png
   :scale: 75
   :align: center

   *Alert on the Quantities sold compared to the Packaging*

Do not confuse the management of packaging with the management of multiple units of measure. The
Unit of Measure is used to manage the stock differently according to the various units. 
With packages, the stock is always managed by individual items, but information about the package to use is supplied
to the storesperson along with that item.

Even if the effects are the same, the printed documents will be different. The two following
operations have the same effect on stock movement levels, but will be printed differently
on the sales order and the packing order as where quantities are concerned:

* 32,000 batteries, delivered on two palettes,

* 2 palettes of batteries, with no information about packaging.

If the customer wants to order a palette and 10 packs, the salesperson can put two order
lines on the sales order using the same product with different units of measure.

It is sometimes more useful to define different products than to define several possible packages for
the same product. A case of beer in a supermarket is a good example. A case holds 24 bottles, plus
the empty case itself. The customer can buy bottles by the piece or a case of 24 bottles at one go.

You could define two packages for the ``Bottle of beer`` : ``PCE`` and ``case`` . But this
representation does not let you manage the stock and price of empty cases. So you might instead
prefer a Bill of Materials, defining and using three different products:

* the empty case for the beer,

* the bottle of beer,

* the case of 24 bottles of beer.

You also define the bill of materials below which determines the make-up of the case of 24 beers:

* Case of 24 bottles of beer: 1 unit,

* Bottle of beer: 24 units,

* Empty case of beer: 1 unit.

Each of these three products has a different price. The products ``Bottle of beer`` and ``Empty case of beer`` have a stock level that needs to be managed. The ``Case of 24 bottles of beer`` has no stock because, if you sell the product, OpenERP automatically moves the stock in two lines, one for the empty case and the other for the 24 individual bottles of beer. For more information on bills of materials,
see chapter :ref:`ch-mnf`.

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
