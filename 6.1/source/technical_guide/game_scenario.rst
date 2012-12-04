
.. module:: game_scenario
    :synopsis: Scenario of games 
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

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/game_scenario"></div>
    <script src="http://js-kit.com/ratings.js"></script>

Scenario of games (*game_scenario*)
===================================
:Module: game_scenario
:Name: Scenario of games
:Version: 5.0.1.0
:Author: Tiny
:Directory: game_scenario
:Web: 
:Official module: no
:Quality certified: no

Description
-----------

::

  Allows to check the scenario of games

Download links
--------------

You can download this module as a zip file in the following version:

  * `5.0 <http://www.openerp.com/download/modules/5.0/game_scenario.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/game_scenario.zip>`_


Dependencies
------------

 * :mod:`base`

Reports
-------

None


Menus
-------

 * Administration/Game Scenario
 * Administration/Game Scenario/Configuration
 * Administration/Game Scenario/Configuration/Scenario Steps
 * Administration/Game Scenario/Configuration/Scenario

Views
-----

 * game.scenario.step.tree (tree)
 * game.scenario.step.form (form)
 * game.scenario.tree (tree)
 * game.scenario.form (form)


Objects
-------

Object: game.scenario (game.scenario)
#####################################



:note: Note, text





:state: State, selection, required





:name: Name, char, required




Object: game.scenario.step (game.scenario.step)
###############################################



:menu_id: Menu, many2one, required





:post_process_object: Postprocess Object, char





:description: Description, text





:pre_process_method: Preprocess Method, char





:error: Error, text





:tip: Tip, text





:scenario_id: Scenario, many2one, required





:name: Name, char, required





:state: State, selection, required





:post_process_method: Postprocess Method, char





:step_next_ids: Next Steps, many2many





:pre_process_object: Preprocess Object, char


