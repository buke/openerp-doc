
.. i18n: .. module:: idea
.. i18n:     :synopsis: Idea Manager (Official, Quality Certified)
.. i18n:     :noindex:
.. i18n: .. 
..

.. module:: idea
    :synopsis: Idea Manager (Official, Quality Certified)
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
.. i18n:     <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/idea"></div>
.. i18n:     <script src="http://js-kit.com/ratings.js"></script>
..

.. raw:: html

    <div class="js-kit-rating" title="" permalink="" standalone="yes" path="/idea"></div>
    <script src="http://js-kit.com/ratings.js"></script>

.. i18n: Idea Manager (*idea*)
.. i18n: =====================
.. i18n: :Module: idea
.. i18n: :Name: Idea Manager
.. i18n: :Version: 5.0.0.1
.. i18n: :Author: Tiny
.. i18n: :Directory: idea
.. i18n: :Web: http://openerp.com
.. i18n: :Official module: yes
.. i18n: :Quality certified: yes
..

Idea Manager (*idea*)
=====================
:Module: idea
:Name: Idea Manager
:Version: 5.0.0.1
:Author: Tiny
:Directory: idea
:Web: http://openerp.com
:Official module: yes
:Quality certified: yes

.. i18n: Description
.. i18n: -----------
..

Description
-----------

.. i18n: ::
.. i18n: 
.. i18n:   This module allows your user to easily and efficiently participate in the innovation of the enterprise. It allows everybody to express ideas about different subjects. Then, others users can comment these ideas and vote for particular ideas. Each idea as a score based on the different votes. The managers can obtain an easy view on best ideas from all the users. Once installed, check the menu 'Ideas' in the 'Tools' main menu.
..

::

  This module allows your user to easily and efficiently participate in the innovation of the enterprise. It allows everybody to express ideas about different subjects. Then, others users can comment these ideas and vote for particular ideas. Each idea as a score based on the different votes. The managers can obtain an easy view on best ideas from all the users. Once installed, check the menu 'Ideas' in the 'Tools' main menu.

.. i18n: Download links
.. i18n: --------------
..

Download links
--------------

.. i18n: You can download this module as a zip file in the following version:
..

You can download this module as a zip file in the following version:

.. i18n:   * `5.0 <http://www.openerp.com/download/modules/5.0/idea.zip>`_
.. i18n:   * `trunk <http://www.openerp.com/download/modules/trunk/idea.zip>`_
..

  * `5.0 <http://www.openerp.com/download/modules/5.0/idea.zip>`_
  * `trunk <http://www.openerp.com/download/modules/trunk/idea.zip>`_

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

.. i18n: None
..

None

.. i18n: Menus
.. i18n: -------
..

Menus
-------

.. i18n:  * Tools
.. i18n:  * Tools/Configuration
.. i18n:  * Tools/Configuration/Ideas
.. i18n:  * Tools/Configuration/Ideas/Categories
.. i18n:  * Tools/Ideas
.. i18n:  * Tools/Ideas/Ideas by Categories
.. i18n:  * Tools/Ideas/All Ideas
.. i18n:  * Tools/Ideas/All Ideas/Open Ideas
.. i18n:  * Tools/Ideas/My Ideas
.. i18n:  * Tools/Ideas/My Ideas/My Draft Ideas
.. i18n:  * Tools/Ideas/My Ideas/My Open Ideas
.. i18n:  * Tools/Ideas/Reporting
.. i18n:  * Tools/Ideas/Reporting/Vote Statistics
.. i18n:  * Tools/Configuration/Ideas/All Votes
..

 * Tools
 * Tools/Configuration
 * Tools/Configuration/Ideas
 * Tools/Configuration/Ideas/Categories
 * Tools/Ideas
 * Tools/Ideas/Ideas by Categories
 * Tools/Ideas/All Ideas
 * Tools/Ideas/All Ideas/Open Ideas
 * Tools/Ideas/My Ideas
 * Tools/Ideas/My Ideas/My Draft Ideas
 * Tools/Ideas/My Ideas/My Open Ideas
 * Tools/Ideas/Reporting
 * Tools/Ideas/Reporting/Vote Statistics
 * Tools/Configuration/Ideas/All Votes

.. i18n: Views
.. i18n: -----
..

Views
-----

.. i18n:  * idea.category.form (form)
.. i18n:  * idea.category.tree (tree)
.. i18n:  * idea.stat.form (form)
.. i18n:  * idea.vote.tree (tree)
.. i18n:  * idea.vote.form (form)
.. i18n:  * idea.idea.form (form)
.. i18n:  * idea.idea.tree (tree)
.. i18n:  * idea.comment.tree (tree)
.. i18n:  * idea.vote_stat.graph (graph)
.. i18n:  * idea.vote.stat.form (form)
.. i18n:  * idea.vote.stat.tree (tree)
..

 * idea.category.form (form)
 * idea.category.tree (tree)
 * idea.stat.form (form)
 * idea.vote.tree (tree)
 * idea.vote.form (form)
 * idea.idea.form (form)
 * idea.idea.tree (tree)
 * idea.comment.tree (tree)
 * idea.vote_stat.graph (graph)
 * idea.vote.stat.form (form)
 * idea.vote.stat.tree (tree)

.. i18n: Objects
.. i18n: -------
..

Objects
-------

.. i18n: Object: Category for an idea (idea.category)
.. i18n: ############################################
..

Object: Category for an idea (idea.category)
############################################

.. i18n: :parent_id: Parent Categories, many2one
..

:parent_id: Parent Categories, many2one

.. i18n: :child_ids: Child Categories, one2many
..

:child_ids: Child Categories, one2many

.. i18n: :name: Category, char, required
..

:name: Category, char, required

.. i18n: :summary: Summary, text
..

:summary: Summary, text

.. i18n: Object: idea.idea (idea.idea)
.. i18n: #############################
..

Object: idea.idea (idea.idea)
#############################

.. i18n: :comment_ids: Comments, one2many
..

:comment_ids: Comments, one2many

.. i18n: :create_date: Creation date, datetime, readonly
..

:create_date: Creation date, datetime, readonly

.. i18n: :description: Description, text, required
..

:description: Description, text, required

.. i18n:     *Content of the idea*
..

    *Content of the idea*

.. i18n: :title: Idea Summary, char, required
..

:title: Idea Summary, char, required

.. i18n: :my_vote: My Vote, selection
..

:my_vote: My Vote, selection

.. i18n: :vote_avg: Average Score, float, readonly
..

:vote_avg: Average Score, float, readonly

.. i18n: :vote_ids: Vote, one2many
..

:vote_ids: Vote, one2many

.. i18n: :state: Status, selection, readonly
..

:state: Status, selection, readonly

.. i18n: :stat_vote_ids: Statistics, one2many, readonly
..

:stat_vote_ids: Statistics, one2many, readonly

.. i18n: :count_comments: Count of comments, integer, readonly
..

:count_comments: Count of comments, integer, readonly

.. i18n: :user_id: Creator, many2one, required, readonly
..

:user_id: Creator, many2one, required, readonly

.. i18n: :category_id: Category, many2one, required
..

:category_id: Category, many2one, required

.. i18n: :count_votes: Count of votes, integer, readonly
..

:count_votes: Count of votes, integer, readonly

.. i18n: Object: Comments (idea.comment)
.. i18n: ###############################
..

Object: Comments (idea.comment)
###############################

.. i18n: :content: Comment, text, required
..

:content: Comment, text, required

.. i18n: :idea_id: Idea, many2one, required
..

:idea_id: Idea, many2one, required

.. i18n: :create_date: Creation date, datetime, readonly
..

:create_date: Creation date, datetime, readonly

.. i18n: :user_id: User, many2one, required
..

:user_id: User, many2one, required

.. i18n: Object: idea.vote (idea.vote)
.. i18n: #############################
..

Object: idea.vote (idea.vote)
#############################

.. i18n: :idea_id: Idea, many2one, required
..

:idea_id: Idea, many2one, required

.. i18n: :score: Score, selection, required
..

:score: Score, selection, required

.. i18n: :user_id: User, many2one
..

:user_id: User, many2one

.. i18n: Object: Idea Votes Statistics (idea.vote.stat)
.. i18n: ##############################################
..

Object: Idea Votes Statistics (idea.vote.stat)
##############################################

.. i18n: :nbr: Number of Votes, integer, readonly
..

:nbr: Number of Votes, integer, readonly

.. i18n: :score: Score, selection, readonly
..

:score: Score, selection, readonly

.. i18n: :idea_id: Idea, many2one, readonly
..

:idea_id: Idea, many2one, readonly
