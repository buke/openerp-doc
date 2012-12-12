**************
Google Earth
**************

Name of module: 
``google_earth``

**Features:**

1. See partners information on google map(name, code, address,...) with icon on map

2. And Turnover of country by partners, country appears in light red color => low turnover and with dark red color => high turnover.

3. Delivery routes from Warehouse location to Customer location by cities with 10 different colors (by number of delivery to that city from warehouse).

4. It can create network link kml file for dynamic updates of data on google earth.

5. It can directly open google map in your browser with different information.

6. It generates KML file so you can save it on your computer and upload it on google map/ google earth.

**Menus**

.. figure::  images/menu_earth.jpg
   :scale: 50
   :align: center

You can find 5 wizards on Partners/ Google Map/Earth.

**KML File:**

To use the google_earth module you must know what a kml file is and how to use it on google/map.

.. tip::  KML

    KML is a file format used to display geographic data in an Earth browser such as Google Earth, Google Maps and Google Maps for mobile. KML uses a tag-based structure with nested elements and attributes and is based on the XML standard. All tags are case-sensitive and must appear exactly as they are listed in the KML Reference. The Reference indicates which tags are optional. Within a given element, tags must appear in the order shown in the Reference.

For more information: 

http://code.google.com/apis/kml/documentation/kml_tut.html

http://code.google.com/apis/kml/documentation/topicsinkml.html

http://code.google.com/apis/kml/documentation/kmlreference.html


**Now How to upload kml file on Google Map:**

Step1: go to create map link

Step2: import

Step3: upload kml


**Difference between Google Maps and Google Earth:**

Google Maps is available through the window of your browser, Google Earth is a downloadable application which can be installed on your computer in order to view the satellite imagery straight from your desktop. However, the super giant Google updates the two products every once in a while so they have almost the same functions


After uploading KML files to google map look below:

(1) KML for ``Partner-Country``

.. figure::  images/google_map.jpg
   :scale: 50
   :align: center

This is the screen shot which shows the partner's country, turnover of partners reside in that country. Here we can see country wise partners and country wise turnover. By clicking on selected country we can get Number of partners, Number of invoices made and Turnover of the country.

.. note:: High Turnover => Dark red & Low Turnover => Light red

(2) KML for ``Delivery Route``

.. figure::  images/earth_delivery.jpg
   :scale: 50
   :align: center

This is the screen shot for finding the delivery routes from warehouse location to customer location. Here we can see there are different routes in different colours. By clicking on particular route we get the information about Customer Location, Warehouse Location, Number of Products sent and Number of deliveries made.

(3) KML for ``Partners``

.. figure::  images/partner_map.jpg
   :scale: 50
   :align: center

This is the screen shot showing all partners from different countries. This will make a point on particular partner address on map. By clicking on any point we can get the information about the partner, e.g. Name of partner, Code, Type(customer/supplier), Address, Turnover of Partner, Number of customer invoice, Number of supplier invoice, Total receivable, etc...


(4) Wizard for KML for ``Network link``

.. figure::  images/earth_wizard.jpg
   :scale: 50
   :align: center
 
.. tip:: Network link kml: 

        A special kind of kml file which has network link tag inside it which contains link of your kml file.

This wizard will create network link in kml for different objects and save it to your computer and then you have to upload network link kml to google earth/map. It can update data periodically by looking network link kml files parameters(refreshtime,interval....). For example if you have inserted new partner then google earth can fetch that new partner from webservice of etiny.

.. note:: If you ticked partner and country, wizard will create two link tag with url/path of two kml file. Now when you upload this kml file it will show both partner and country information on earth and update that information by given interval time (using url/path ).
	
	
**The wizard of network link shown above:**

First, ``path`` shows a url (HTTP address) means your web-client path with port number where your etiny services running.
	
``RefreshMode`` specifies a time-based refresh mode, which can be one of the following: 

    onChange - refresh when the file is loaded and whenever the Link parameters change (default).
    
    onInterval - refresh every n seconds (specified in <refreshInterval>).
    
    onExpire - refresh the file when the expiration time is reached.

``RefreshInterval`` indicates to refresh the file every n seconds. 

``ViewRefreshMode`` specifies how the link is refreshed when the "camera" changes.

    never(default) - Ignore changes in the view. Also ignore <viewFormat> parameters, if any. 
		
    onStop - Refresh the file n seconds after movement stops, where n is specified in <viewRefreshTime>. 
        
    onRequest - Refresh the file only when the user explicitly requests it. (For example, in Google Earth, the user right-clicks and selects Refresh in the Context menu.) 
        
    onRegion - Refresh the file when the Region becomes active.

``View Refresh Time`` specifies the number of seconds to wait before refreshing the view, after 	camera movement stops.
     

(5) Wizard for Open *Google Map*

.. figure::  images/open_map.jpg
   :scale: 50
   :align: center

This wizard will directly open google map in browser.

For example, if you want to open that map for partner-country, then it will directly open google map for partner with countries in browser.

In above figure, You can see Path field. In that, http://maps.google.com/maps?q=, will be common and later is shown your web-client path with port. Another field is Map For which is selection for Partner, Partner-Country and Delivery-Route. Whatever option you select from Map For field, it will directly open map for that option and with that url(Path).

Url looks like ``http://maps.google.com/maps?q=http://yourserver.com:port/kml?model=res.partner`` when you open the browser.

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

