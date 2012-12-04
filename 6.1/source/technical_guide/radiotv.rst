
.. module:: radiotv
    :synopsis: TV & Radio Program Grid Module 
    :noindex:
.. 

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. tip:: This module is part of the OpenERP software, the leading Open Source 
  enterprise management system. If you want to discover OpenERP, check our 
  `screencasts <http://openerp.tv>`_ or download 
  `OpenERP <http://openerp.com>`_ directly.

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/radiotv"></div>
    <script src="http://js-kit.com/ratings.js"></script>

TV & Radio Program Grid Module (*radiotv*)
===================================================
:Module: radiotv
:Name: TV & Radio Program Grid Module
:Version: 5.0.1.1
:Author: Zikzakmedia
:Directory: radiotv
:Web: www.zikzakmedia.com
:Official module: no
:Quality certified: no

Description
-----------

::

  This module allows control of TV & Radio channels, programs, grid of date/time of broadcasting and podcasts
  
  channel <--n---m--> program <--1---n--> broadcast <--1---n--> podcast
  
  Features:
      * Menu entries to see daily and weekly broadcasts
      * The end date/time of each broadcast is automatically calculated
      * The broadcasts can be copied from one range of days to another
      * A cron is provided to copy broadcasts daily
      * Several broadcasting reports are included
      * Several wizards to synchronise the channels, programs and broadcasts to a
        mysql-php web site are included. They can be also synchronized automatically.

Download links
--------------

You can download this module as a zip file in the following version:

  * `4.2 <http://www.openerp.com/download/modules/4.2/radiotv.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/radiotv.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/radiotv.zip>`_


Dependencies
------------

 * :mod:`base`

Reports
-------

 * Radio TV broadcast report

 * Radio TV broadcast compact report

 * Radio TV broadcast declaration report

Menus
-------

 * Radio TV/Channels
 * Radio TV/Program categories
 * Radio TV/Programs
 * Radio TV/Programs/Archive programs
 * Radio TV/Programs/Published programs
 * Radio TV/Programs/Unpublished programs
 * Radio TV/Broadcasts
 * Radio TV/Broadcasts/Yesterday broadcasts
 * Radio TV/Broadcasts/Today broadcasts
 * Radio TV/Broadcasts/Tomorrow broadcasts
 * Radio TV/Broadcasts/Previous week broadcasts
 * Radio TV/Broadcasts/This week broadcasts
 * Radio TV/Broadcasts/Next week broadcasts
 * Radio TV/Podcasts
 * Radio TV/Configuration/Website configuration
 * Radio TV/Copy broadcasts from a day to other
 * Radio TV/Export channels and programs
 * Radio TV/Export broadcasts
 * Radio TV/Export podcasts
 * Radio TV/Broadcasts compact report
 * Radio TV/Broadcasts declaration report

Views
-----

 * radiotv.channel.tree (tree)
 * radiotv.channel (form)
 * radiotv.program.tree (tree)
 * radiotv.program (form)
 * radiotv.category.tree (tree)
 * radiotv.category (form)
 * radiotv.broadcast.tree (tree)
 * radiotv.broadcast (form)
 * radiotv.podcast.tree (tree)
 * radiotv.podcast (form)
 * radiotv.web.tree (tree)


Objects
-------

Object: radiotv.program (radiotv.program)
#########################################



:production_year: Production year, integer





:description: Description, text





:classification: Classification, selection, required





:introduction: Introduction, text, required





:channel_ids: Channels, many2many





:approx_duration: Approx. duration, integer

    *Approximate duration in minutes*



:production_country_id: Production country, many2one





:broadcast_language: Broadcast language, char





:original_language: Original language, char





:state: State, selection, required





:production_type: Production type, selection, required





:editor: Editor, char





:team: Team, text





:category_id: Category, many2one





:email: Email, char





:name: Name, char, required




Object: radiotv.category (radiotv.category)
###########################################



:program_ids: Programs, one2many





:name: Name, char, required





:description: Description, text




Object: radiotv.broadcast (radiotv.broadcast)
#############################################



:dt_end: End, datetime





:description: Description, text





:url: URL, text





:dt_start: Start, datetime, required





:program_id: Program, many2one, required





:channel_id: Channel, many2one, required




Object: radiotv.channel (radiotv.channel)
#########################################



:program_ids: Programs, many2many





:name: Name, char, required





:description: Description, text




Object: radiotv.podcast (radiotv.podcast)
#########################################



:category: Category, char





:subtitle: Subtitle, char





:description: Description, text





:author: Author, char





:file_name: File name, char, required





:explicit: Explicit, boolean





:duration: Duration, char





:broadcast_id: Broadcast, many2one, required





:keywords: Keywords, char





:pub_date: Publication, datetime, required, readonly





:block: Block, boolean





:name: Name, char, required




Object: RadioTV website configuration (radiotv.web)
###################################################



:url: URL, char, required





:active: Active, boolean





:name: Name, char, required





:sync: Synchronize, boolean

    *The changes in channels, programs and broadcasts are synchronized automatically to the website*
