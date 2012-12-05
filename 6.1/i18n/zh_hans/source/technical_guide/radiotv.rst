
.. i18n: .. module:: radiotv
.. i18n:     :synopsis: TV & Radio Program Grid Module 
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: radiotv
    :synopsis: TV & Radio Program Grid Module 
    :noindex:
.. 

.. i18n: .. raw:: html
.. i18n: 
.. i18n:       <br />
.. i18n:     <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />
..

.. raw:: html

      <br />
    <link rel="stylesheet" href="../_static/hide_objects_in_sidebar.css" type="text/css" />

.. i18n: .. tip:: This module is part of the OpenERP software, the leading Open Source 
.. i18n:   enterprise management system. If you want to discover OpenERP, check our 
.. i18n:   `screencasts <http://openerp.tv>`_ or download 
.. i18n:   `OpenERP <http://openerp.com>`_ directly.
..

.. tip:: This module is part of the OpenERP software, the leading Open Source 
  enterprise management system. If you want to discover OpenERP, check our 
  `screencasts <http://openerp.tv>`_ or download 
  `OpenERP <http://openerp.com>`_ directly.

.. i18n: .. raw:: html
.. i18n: 
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/radiotv"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/radiotv"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: TV & Radio Program Grid Module (*radiotv*)
.. i18n: ===================================================
.. i18n: :Module: radiotv
.. i18n: :Name: TV & Radio Program Grid Module
.. i18n: :Version: 5.0.1.1
.. i18n: :Author: Zikzakmedia
.. i18n: :Directory: radiotv
.. i18n: :Web: www.zikzakmedia.com
.. i18n: :Official module: no
.. i18n: :Quality certified: no
..

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

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module allows control of TV & Radio channels, programs, grid of date/time of broadcasting and podcasts
.. i18n:   
.. i18n:   channel <--n---m--> program <--1---n--> broadcast <--1---n--> podcast
.. i18n:   
.. i18n:   Features:
.. i18n:       * Menu entries to see daily and weekly broadcasts
.. i18n:       * The end date/time of each broadcast is automatically calculated
.. i18n:       * The broadcasts can be copied from one range of days to another
.. i18n:       * A cron is provided to copy broadcasts daily
.. i18n:       * Several broadcasting reports are included
.. i18n:       * Several wizards to synchronise the channels, programs and broadcasts to a
.. i18n:         mysql-php web site are included. They can be also synchronized automatically.
..

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

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `4.2 <http://www.openerp.com/download/modules/4.2/radiotv.zip>`_
.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/radiotv.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/radiotv.zip>`_
..

  * `4.2 <http://www.openerp.com/download/modules/4.2/radiotv.zip>`_
  * `5.0 <http://www.openerp.com/download/modules/5.0/radiotv.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/radiotv.zip>`_

.. i18n: Dependencies
.. i18n: ------------
..

Dependencies
------------

.. i18n:  * :mod:`base`
..

 * :mod:`base`

.. i18n: Reports
.. i18n: -------
..

Reports
-------

.. i18n:  * Radio TV broadcast report
.. i18n: 
.. i18n:  * Radio TV broadcast compact report
.. i18n: 
.. i18n:  * Radio TV broadcast declaration report
..

 * Radio TV broadcast report

 * Radio TV broadcast compact report

 * Radio TV broadcast declaration report

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Radio TV/Channels
.. i18n:  * Radio TV/Program categories
.. i18n:  * Radio TV/Programs
.. i18n:  * Radio TV/Programs/Archive programs
.. i18n:  * Radio TV/Programs/Published programs
.. i18n:  * Radio TV/Programs/Unpublished programs
.. i18n:  * Radio TV/Broadcasts
.. i18n:  * Radio TV/Broadcasts/Yesterday broadcasts
.. i18n:  * Radio TV/Broadcasts/Today broadcasts
.. i18n:  * Radio TV/Broadcasts/Tomorrow broadcasts
.. i18n:  * Radio TV/Broadcasts/Previous week broadcasts
.. i18n:  * Radio TV/Broadcasts/This week broadcasts
.. i18n:  * Radio TV/Broadcasts/Next week broadcasts
.. i18n:  * Radio TV/Podcasts
.. i18n:  * Radio TV/Configuration/Website configuration
.. i18n:  * Radio TV/Copy broadcasts from a day to other
.. i18n:  * Radio TV/Export channels and programs
.. i18n:  * Radio TV/Export broadcasts
.. i18n:  * Radio TV/Export podcasts
.. i18n:  * Radio TV/Broadcasts compact report
.. i18n:  * Radio TV/Broadcasts declaration report
..

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

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * radiotv.channel.tree (tree)
.. i18n:  * radiotv.channel (form)
.. i18n:  * radiotv.program.tree (tree)
.. i18n:  * radiotv.program (form)
.. i18n:  * radiotv.category.tree (tree)
.. i18n:  * radiotv.category (form)
.. i18n:  * radiotv.broadcast.tree (tree)
.. i18n:  * radiotv.broadcast (form)
.. i18n:  * radiotv.podcast.tree (tree)
.. i18n:  * radiotv.podcast (form)
.. i18n:  * radiotv.web.tree (tree)
..

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

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: radiotv.program (radiotv.program)
.. i18n: #########################################
..

Object: radiotv.program (radiotv.program)
#########################################

.. i18n: :production_year: Production year, integer
..

:production_year: Production year, integer

.. i18n: :description: Description, text
..

:description: Description, text

.. i18n: :classification: Classification, selection, required
..

:classification: Classification, selection, required

.. i18n: :introduction: Introduction, text, required
..

:introduction: Introduction, text, required

.. i18n: :channel_ids: Channels, many2many
..

:channel_ids: Channels, many2many

.. i18n: :approx_duration: Approx. duration, integer
..

:approx_duration: Approx. duration, integer

.. i18n:     *Approximate duration in minutes*
..

    *Approximate duration in minutes*

.. i18n: :production_country_id: Production country, many2one
..

:production_country_id: Production country, many2one

.. i18n: :broadcast_language: Broadcast language, char
..

:broadcast_language: Broadcast language, char

.. i18n: :original_language: Original language, char
..

:original_language: Original language, char

.. i18n: :state: State, selection, required
..

:state: State, selection, required

.. i18n: :production_type: Production type, selection, required
..

:production_type: Production type, selection, required

.. i18n: :editor: Editor, char
..

:editor: Editor, char

.. i18n: :team: Team, text
..

:team: Team, text

.. i18n: :category_id: Category, many2one
..

:category_id: Category, many2one

.. i18n: :email: Email, char
..

:email: Email, char

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: Object: radiotv.category (radiotv.category)
.. i18n: ###########################################
..

Object: radiotv.category (radiotv.category)
###########################################

.. i18n: :program_ids: Programs, one2many
..

:program_ids: Programs, one2many

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :description: Description, text
..

:description: Description, text

.. i18n: Object: radiotv.broadcast (radiotv.broadcast)
.. i18n: #############################################
..

Object: radiotv.broadcast (radiotv.broadcast)
#############################################

.. i18n: :dt_end: End, datetime
..

:dt_end: End, datetime

.. i18n: :description: Description, text
..

:description: Description, text

.. i18n: :url: URL, text
..

:url: URL, text

.. i18n: :dt_start: Start, datetime, required
..

:dt_start: Start, datetime, required

.. i18n: :program_id: Program, many2one, required
..

:program_id: Program, many2one, required

.. i18n: :channel_id: Channel, many2one, required
..

:channel_id: Channel, many2one, required

.. i18n: Object: radiotv.channel (radiotv.channel)
.. i18n: #########################################
..

Object: radiotv.channel (radiotv.channel)
#########################################

.. i18n: :program_ids: Programs, many2many
..

:program_ids: Programs, many2many

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :description: Description, text
..

:description: Description, text

.. i18n: Object: radiotv.podcast (radiotv.podcast)
.. i18n: #########################################
..

Object: radiotv.podcast (radiotv.podcast)
#########################################

.. i18n: :category: Category, char
..

:category: Category, char

.. i18n: :subtitle: Subtitle, char
..

:subtitle: Subtitle, char

.. i18n: :description: Description, text
..

:description: Description, text

.. i18n: :author: Author, char
..

:author: Author, char

.. i18n: :file_name: File name, char, required
..

:file_name: File name, char, required

.. i18n: :explicit: Explicit, boolean
..

:explicit: Explicit, boolean

.. i18n: :duration: Duration, char
..

:duration: Duration, char

.. i18n: :broadcast_id: Broadcast, many2one, required
..

:broadcast_id: Broadcast, many2one, required

.. i18n: :keywords: Keywords, char
..

:keywords: Keywords, char

.. i18n: :pub_date: Publication, datetime, required, readonly
..

:pub_date: Publication, datetime, required, readonly

.. i18n: :block: Block, boolean
..

:block: Block, boolean

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: Object: RadioTV website configuration (radiotv.web)
.. i18n: ###################################################
..

Object: RadioTV website configuration (radiotv.web)
###################################################

.. i18n: :url: URL, char, required
..

:url: URL, char, required

.. i18n: :active: Active, boolean
..

:active: Active, boolean

.. i18n: :name: Name, char, required
..

:name: Name, char, required

.. i18n: :sync: Synchronize, boolean
..

:sync: Synchronize, boolean

.. i18n:     *The changes in channels, programs and broadcasts are synchronized automatically to the website*
..

    *The changes in channels, programs and broadcasts are synchronized automatically to the website*
