
.. i18n: .. index::
.. i18n:    single: Financial Analysis
.. i18n:    single: taxation
.. i18n:    single: financial reporting
..

.. index::
   single: Financial Analysis
   single: taxation
   single: financial reporting

.. i18n: .. _ch-financial:
.. i18n: 
.. i18n: ******************
.. i18n: Financial Analysis
.. i18n: ******************
..

.. _ch-financial:

******************
Financial Analysis
******************

.. i18n:  *This chapter is dedicated to statutory taxation and financial reporting from OpenERP.
.. i18n:  Whether you need reports about customers and suppliers, or statements for various statutory purposes,
.. i18n:  OpenERP enables you to carry out a whole range of parametric analyses regarding the financial health of
.. i18n:  your company.*
..

 *This chapter is dedicated to statutory taxation and financial reporting from OpenERP.
 Whether you need reports about customers and suppliers, or statements for various statutory purposes,
 OpenERP enables you to carry out a whole range of parametric analyses regarding the financial health of
 your company.*

.. i18n: Whether you want to analyze the general health of your company or review the status of an Account
.. i18n: Receivable in detail, your company's accounts are the place to define your various business
.. i18n: indicators.
..

Whether you want to analyze the general health of your company or review the status of an Account
Receivable in detail, your company's accounts are the place to define your various business
indicators.

.. i18n: To show you the most accurate picture of your business, OpenERP's accounting reports
.. i18n: are flexible, and the results are calculated in real time. This enables you to automate recurring
.. i18n: actions and to change your operations quickly when a company-wide problem (such as cash reserves
.. i18n: dropping too low or receivables climbing too high) or a local problem (a customer that has not paid,
.. i18n: or a project budget overspend) occurs.
..

To show you the most accurate picture of your business, OpenERP's accounting reports
are flexible, and the results are calculated in real time. This enables you to automate recurring
actions and to change your operations quickly when a company-wide problem (such as cash reserves
dropping too low or receivables climbing too high) or a local problem (a customer that has not paid,
or a project budget overspend) occurs.

.. i18n: This chapter describes the various reports and financial statements supplied by OpenERP's
.. i18n: accounting modules. It also describes how OpenERP handles purchase and sales taxation, and the
.. i18n: related tax reporting.
..

This chapter describes the various reports and financial statements supplied by OpenERP's
accounting modules. It also describes how OpenERP handles purchase and sales taxation, and the
related tax reporting.

.. i18n: For this chapter you should start with a fresh database that includes demo data,
.. i18n: with :mod:`sale` and its dependencies installed and no particular chart of accounts configured.
..

For this chapter you should start with a fresh database that includes demo data,
with :mod:`sale` and its dependencies installed and no particular chart of accounts configured.

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <div class="all-toctree">
..

.. raw:: html

    <div class="all-toctree">

.. i18n: .. toctree::
.. i18n: 
.. i18n:     statutory_taxes
.. i18n:     company_financial_analysis
.. i18n:     accounts_fin_ana
..

.. toctree::

    statutory_taxes
    company_financial_analysis
    accounts_fin_ana

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     </div>
..

.. raw:: html

    </div>

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
