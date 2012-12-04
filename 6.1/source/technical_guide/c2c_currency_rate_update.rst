
.. module:: c2c_currency_rate_update
    :synopsis: Currency Rate Update 
    :noindex:
.. 

.. raw:: html

    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

Currency Rate Update (*c2c_currency_rate_update*)
=================================================
:Module: c2c_currency_rate_update
:Name: Currency Rate Update
:Version: 0.5
:Author: Camptocamp SA
:Directory: c2c_currency_rate_update
:Web: http://camptocamp.com
:Official module: no
:Quality certified: no

Description
-----------

::

  
  Import exchange rates from three different sources on the internet :
  
  1. Admin.ch
     Updated daily, source in CHF. Source type is XML based.
  
  2. Federal Reserve Bank of New York
     Daily 12 noon buying rates in New York are certified by the
     New York Federal Reserve Bank for customs purposes.
     Source in USD.
     http://www.newyorkfed.org/markets/pilotfx.html
  
  3. European Central Bank
     The reference rates are based on the regular daily concertation procedure between
     central banks within and outside the European System of Central Banks,
     which normally takes place at 2.15 p.m. (14:15) ECB time. Source in EUR.
     http://www.ecb.europa.eu/stats/exchange/eurofxref/html/index.en.html
  
  4. Google Finance
     Updated daily from Citibank N.A., source in EUR. Information may be delayed.
     This is parsed from an HTML page, so it may break in the future.
  
  5. Bank of Canada
     Updated daily at 12:30 am, source in CAD, nominal rate. Source type is CSV based.
  
  You can set time cycle for getting updates, 'first execute date' define when to start
  the import and you can add a comment that describe why you use that particular service.
  
  The module uses internal ir_cron feature from OpenERP, so the job is launched once
  the server starts if the 'first execute date' is before the current day.
  
  If in multi-company mode, the base currency will be the first company's currency
  found in database.
  
Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/c2c_currency_rate_update.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/c2c_currency_rate_update.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/c2c_currency_rate_update.zip>`_


Dependencies
------------

 * :mod:`base`

Reports
-------

None


Menus
-------


None


Views
-----


None



Objects
-------

None
