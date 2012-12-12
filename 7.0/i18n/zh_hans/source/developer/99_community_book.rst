
.. i18n: =============
.. i18n: Collaboration
.. i18n: =============
..

=============
Collaboration
=============

.. i18n: Launchpad and bazaar
.. i18n: --------------------
..

Launchpad and bazaar
--------------------

.. i18n: Before you can commit on launchpad, you have to create a login. This login is needed if you intend to commit on openerp-comiter or on your own branch via bazaar. Go to: https://launchpad.net --> log in / register on top right.
..

Before you can commit on launchpad, you have to create a login. This login is needed if you intend to commit on openerp-comiter or on your own branch via bazaar. Go to: https://launchpad.net --> log in / register on top right.

.. i18n: Enter your e-mail address and wait for an e-mail which will guide you trough the login creation process.
..

Enter your e-mail address and wait for an e-mail which will guide you trough the login creation process.

.. i18n: You can then refer to this link :
.. i18n: https://help.launchpad.net/YourAccount/NewAccount
..

You can then refer to this link :
https://help.launchpad.net/YourAccount/NewAccount

.. i18n: Any contributor who is interested to become a committer must show his interest
.. i18n: on working for openerp project and ability to do it properly as
.. i18n: selection is based on merit. It can be by proposing bug
.. i18n: fixes, features requested on our :ref:`bug tracker <bug-tracker-link>` system.
.. i18n: You can even suggest additional modules and/or functionality on our :ref:`bug
.. i18n: tracker <bug-tracker-link>` system.
..

Any contributor who is interested to become a committer must show his interest
on working for openerp project and ability to do it properly as
selection is based on merit. It can be by proposing bug
fixes, features requested on our :ref:`bug tracker <bug-tracker-link>` system.
You can even suggest additional modules and/or functionality on our :ref:`bug
tracker <bug-tracker-link>` system.

.. i18n: You can contribute or join OpenERP team, : https://help.launchpad.net/Teams/Joining
..

You can contribute or join OpenERP team, : https://help.launchpad.net/Teams/Joining

.. i18n: Contributors are people who want to help the project improve, add
.. i18n: functionality and improve stability. Anyone can contribute to the project
.. i18n: by reporting bugs, proposing improvements and
.. i18n: posting patches.
..

Contributors are people who want to help the project improve, add
functionality and improve stability. Anyone can contribute to the project
by reporting bugs, proposing improvements and
posting patches.

.. i18n: The community team is available on launchpad: https://launchpad.net/~openerp-community
..

The community team is available on launchpad: https://launchpad.net/~openerp-community

.. i18n: Members of the quality and committer team are automatically members of the community.
..

Members of the quality and committer team are automatically members of the community.

.. i18n: Once you have configured your Launchpad account, get Bazaar version control to pull the source from Launchpad.
..

Once you have configured your Launchpad account, get Bazaar version control to pull the source from Launchpad.

.. i18n: NoteThib: viré les explications sur comment installer bazaar, je propos de mettre le lien vers le site qui expliquera comment l'installer si besoin est
..

NoteThib: viré les explications sur comment installer bazaar, je propos de mettre le lien vers le site qui expliquera comment l'installer si besoin est

.. i18n: If you experience problems with Bazaar, please read the :ref:`bazaar-faq-link` before asking any questions.
..

If you experience problems with Bazaar, please read the :ref:`bazaar-faq-link` before asking any questions.

.. i18n: Working with Branch
.. i18n: -------------------
..

Working with Branch
-------------------

.. i18n: The combination of Bazaar branch hosting and Launchpad's teams infrastructure gives you a very powerful capability to collaborate on code. Essentially, you can push a branch into a shared space and anyone on that team can then commit to the branch.
..

The combination of Bazaar branch hosting and Launchpad's teams infrastructure gives you a very powerful capability to collaborate on code. Essentially, you can push a branch into a shared space and anyone on that team can then commit to the branch.

.. i18n: This means that you can use Bazaar in the same way that you would use something like SVN, i.e. centrally hosting a branch that many people commit to. You have the added benefit, though, that anyone outside the team can always create their own personal branch of your team branch and, if they choose, upload it back to Launchpad. 
..

This means that you can use Bazaar in the same way that you would use something like SVN, i.e. centrally hosting a branch that many people commit to. You have the added benefit, though, that anyone outside the team can always create their own personal branch of your team branch and, if they choose, upload it back to Launchpad. 

.. i18n: This is the official and proposed way to contribute on OpenERP and OpenObject.
..

This is the official and proposed way to contribute on OpenERP and OpenObject.

.. i18n: Quick Summary
.. i18n: +++++++++++++
..

Quick Summary
+++++++++++++

.. i18n: To download the latest sources and create your own local branches of OpenERP, do this::
.. i18n: 
.. i18n:   mkdir openerp
.. i18n:   cd openerp
.. i18n:   bzr branch lp:~openerp/openobject-server/trunk server
.. i18n:   bzr branch lp:~openerp/openobject-addons/trunk addons
.. i18n:   bzr branch lp:~openerp-commiter/openobject-addons/trunk-extra-addons addons-extra
.. i18n:   bzr branch lp:~openerp-community/openobject-addons/trunk-addons-community addons-community
.. i18n:   bzr branch lp:~openerp/openerp-web/trunk web
.. i18n:   bzr branch lp:~openerp/openobject-client/trunk client
.. i18n:   bzr branch lp:~openerp-community/openobject-doc/6.1 doc
..

To download the latest sources and create your own local branches of OpenERP, do this::

  mkdir openerp
  cd openerp
  bzr branch lp:~openerp/openobject-server/trunk server
  bzr branch lp:~openerp/openobject-addons/trunk addons
  bzr branch lp:~openerp-commiter/openobject-addons/trunk-extra-addons addons-extra
  bzr branch lp:~openerp-community/openobject-addons/trunk-addons-community addons-community
  bzr branch lp:~openerp/openerp-web/trunk web
  bzr branch lp:~openerp/openobject-client/trunk client
  bzr branch lp:~openerp-community/openobject-doc/6.1 doc

.. i18n: This will download all components of openerp (server, client, addons) and create links of modules in addons on your server so that you can use it directly. You can change the bzr_set.py file to select what you want to download exactly. Now, you can edit the code and commit in your local branch.::
.. i18n: 
.. i18n:   EDIT addons/account/account.py
.. i18n:   cd addons
.. i18n:   bzr ci -m "Testing Modifications"
..

This will download all components of openerp (server, client, addons) and create links of modules in addons on your server so that you can use it directly. You can change the bzr_set.py file to select what you want to download exactly. Now, you can edit the code and commit in your local branch.::

  EDIT addons/account/account.py
  cd addons
  bzr ci -m "Testing Modifications"

.. i18n: Once your code is good enough and follow the :ref:`coding-guidelines-link`, you
.. i18n: can push your branch to launchpad. You may have to create an account on
.. i18n: launchpad first, register your public key, and subscribe to the `openerp-community <https://launchpad.net/~openerp-community>`_ team. Then, you
.. i18n: can push your branch. Suppose you want to push your addons::
.. i18n: 
.. i18n:   cd addons
.. i18n:   bzr push lp:~openerp-community/openobject-addons/YOURLOGIN_YOURBRANCHNAME
.. i18n:   bzr bind lp:~openerp-community/openobject-addons/YOURLOGIN_YOURBRANCHNAME
..

Once your code is good enough and follow the :ref:`coding-guidelines-link`, you
can push your branch to launchpad. You may have to create an account on
launchpad first, register your public key, and subscribe to the `openerp-community <https://launchpad.net/~openerp-community>`_ team. Then, you
can push your branch. Suppose you want to push your addons::

  cd addons
  bzr push lp:~openerp-community/openobject-addons/YOURLOGIN_YOURBRANCHNAME
  bzr bind lp:~openerp-community/openobject-addons/YOURLOGIN_YOURBRANCHNAME

.. i18n: After having done that, your branch is public on Launchpad, in the `OpenObject
.. i18n: project <https://code.launchpad.net/openobject>`_, and committers can work on
.. i18n: it, review it and propose for integration in the official branch. The last line
.. i18n: allows you to rebind your branch to the one on launchpad, after having
.. i18n: done this, your commit will be applied on launchpad directly (unless you use ``--local``)::
.. i18n: 
.. i18n:   bzr pull    # Get modifications on your branch from others
.. i18n:   EDIT STUFF
.. i18n:   bzr ci    # commit your changes on your public branch
..

After having done that, your branch is public on Launchpad, in the `OpenObject
project <https://code.launchpad.net/openobject>`_, and committers can work on
it, review it and propose for integration in the official branch. The last line
allows you to rebind your branch to the one on launchpad, after having
done this, your commit will be applied on launchpad directly (unless you use ``--local``)::

  bzr pull    # Get modifications on your branch from others
  EDIT STUFF
  bzr ci    # commit your changes on your public branch

.. i18n: If your changes fix a public bug on launchpad, you can use this to mark the bug as fixed by your branch::
.. i18n: 
.. i18n:   bzr ci --fixes=lp:453123   # Where 453123 is a bug ID
..

If your changes fix a public bug on launchpad, you can use this to mark the bug as fixed by your branch::

  bzr ci --fixes=lp:453123   # Where 453123 is a bug ID

.. i18n: Once your branch is mature, mark it as mature in the web interface of launchpad
.. i18n: and request for merging in the official release. Your branch will be reviewed
.. i18n: by a committer and then the quality team to be merged into the official release.
..

Once your branch is mature, mark it as mature in the web interface of launchpad
and request for merging in the official release. Your branch will be reviewed
by a committer and then the quality team to be merged into the official release.

.. i18n: [Read more about :ref:`OpenERP Team <openerp-team>`]
..

[Read more about :ref:`OpenERP Team <openerp-team>`]

.. i18n: Pushing a new branch
.. i18n: ++++++++++++++++++++
..

Pushing a new branch
++++++++++++++++++++

.. i18n: If you want to contribute on OpenERP or OpenObject, here is the proposed method:
..

If you want to contribute on OpenERP or OpenObject, here is the proposed method:

.. i18n:   * You create a branch on launchpad on the project that interests you. It's
.. i18n:     important that you create your branch on launchpad and not on your local
.. i18n:     system so that we can easily merge, share code between projects and
.. i18n:     centralize future developments.
.. i18n:   * You develop your own features or bugfixes
.. i18n:     in your own branch on launchpad. Don't forget to set the status of your
.. i18n:     branch (new, experimental, development, mature, ...) so that contributors
.. i18n:     know what they can and cannot use.
.. i18n:   * Once your code is good enough, propose your branch for merging
.. i18n:   * Your work will be evaluated by a member of the committers team.
.. i18n: 
.. i18n:     - If they accept your branch for integration in the official version, they
.. i18n:       will submit to the quality team that will review and merge in the official
.. i18n:       branch.
.. i18n:     - If the committer team refuses your branch, they will explain why
.. i18n:       so that you can review the code to better fit the guidelines (problem for
.. i18n:       future migrations, ...)
..

  * You create a branch on launchpad on the project that interests you. It's
    important that you create your branch on launchpad and not on your local
    system so that we can easily merge, share code between projects and
    centralize future developments.
  * You develop your own features or bugfixes
    in your own branch on launchpad. Don't forget to set the status of your
    branch (new, experimental, development, mature, ...) so that contributors
    know what they can and cannot use.
  * Once your code is good enough, propose your branch for merging
  * Your work will be evaluated by a member of the committers team.

    - If they accept your branch for integration in the official version, they
      will submit to the quality team that will review and merge in the official
      branch.
    - If the committer team refuses your branch, they will explain why
      so that you can review the code to better fit the guidelines (problem for
      future migrations, ...)

.. i18n: The extra-addons branch, that stores all extra modules, is directly accessible
.. i18n: to all committers. If you are a committer, you can work directly on this branch
.. i18n: and commit your own work. This branch does not require a validation of the
.. i18n: quality team. You should put there your special modules for your own customers.
..

The extra-addons branch, that stores all extra modules, is directly accessible
to all committers. If you are a committer, you can work directly on this branch
and commit your own work. This branch does not require a validation of the
quality team. You should put there your special modules for your own customers.

.. i18n: If you want to propose or develop new modules, we suggest creating your
.. i18n: own branch in the `openobject-addons project <https://launchpad.net/openobject-addons>`_
.. i18n: and develop within your branch. You can fill in a bug to request that
.. i18n: your modules are integrated in one of the two branches:
..

If you want to propose or develop new modules, we suggest creating your
own branch in the `openobject-addons project <https://launchpad.net/openobject-addons>`_
and develop within your branch. You can fill in a bug to request that
your modules are integrated in one of the two branches:

.. i18n:   * extra-addons : if your module touches a few companies
.. i18n:   * addons : if your module will be useful for most of the companies
..

  * extra-addons : if your module touches a few companies
  * addons : if your module will be useful for most of the companies

.. i18n: We invite all our partners and contributors to work in that way so that we can
.. i18n: easily integrate and share the work done between the different projects.
..

We invite all our partners and contributors to work in that way so that we can
easily integrate and share the work done between the different projects.

.. i18n: After having done that, your branch is public on Launchpad, in the `OpenObject
.. i18n: project <https://code.launchpad.net/openobject>`_, and committers can work on
.. i18n: it, review it and propose for integration in the official branch. The last line
.. i18n: allows you to rebind your branch to the one which is on launchpad, after having
.. i18n: done this, your commit will be applied on launchpad directly (unless you use ``--local``)::
.. i18n: 
.. i18n:   bzr pull    # Get modifications on your branch from others
.. i18n:   EDIT STUFF
.. i18n:   bzr ci    # commit your changes on your public branch
..

After having done that, your branch is public on Launchpad, in the `OpenObject
project <https://code.launchpad.net/openobject>`_, and committers can work on
it, review it and propose for integration in the official branch. The last line
allows you to rebind your branch to the one which is on launchpad, after having
done this, your commit will be applied on launchpad directly (unless you use ``--local``)::

  bzr pull    # Get modifications on your branch from others
  EDIT STUFF
  bzr ci    # commit your changes on your public branch

.. i18n: If your changes fix a public bug on launchpad, you can use this to mark the bug as fixed by your branch::
.. i18n: 
.. i18n:   bzr ci --fixes=lp:453123   # Where 453123 is a bug ID
..

If your changes fix a public bug on launchpad, you can use this to mark the bug as fixed by your branch::

  bzr ci --fixes=lp:453123   # Where 453123 is a bug ID

.. i18n: Once your branch is mature, mark it as mature in the web interface of launchpad
.. i18n: and request for merging in the official release. Your branch will be reviewed
.. i18n: by a committer and then the quality team to be merged in the official release.
..

Once your branch is mature, mark it as mature in the web interface of launchpad
and request for merging in the official release. Your branch will be reviewed
by a committer and then the quality team to be merged in the official release.

.. i18n: How to commit Your Work
.. i18n: +++++++++++++++++++++++
..

How to commit Your Work
+++++++++++++++++++++++

.. i18n: If you want to contribute on OpenERP or OpenObject, here is the proposed method:
..

If you want to contribute on OpenERP or OpenObject, here is the proposed method:

.. i18n:   * You create a branch on launchpad on the project that interests you. It's
.. i18n:     important that you create your branch on launchpad and not on your local
.. i18n:     system so that we can easily merge, share code between projects and
.. i18n:     centralize future developments.
.. i18n:   * You develop your own features or bugfixes
.. i18n:     in your own branch on launchpad. Don't forget to set the status of your
.. i18n:     branch (new, experimental, development, mature, ...) so that contributors
.. i18n:     know what they can and cannot use.
.. i18n:   * Once your code is good enough, propose your branch for merging
.. i18n:   * Your work will be evaluated by a member of the committers team.
.. i18n: 
.. i18n:     - If they accept your branch for integration in the official version, they
.. i18n:       will submit to the quality team that will review and merge in the official
.. i18n:       branch.
.. i18n:     - If the committer team refuses your branch, they will explain why
.. i18n:       so that you can review the code to better fit the guidelines (problem for
.. i18n:       future migrations, ...)
..

  * You create a branch on launchpad on the project that interests you. It's
    important that you create your branch on launchpad and not on your local
    system so that we can easily merge, share code between projects and
    centralize future developments.
  * You develop your own features or bugfixes
    in your own branch on launchpad. Don't forget to set the status of your
    branch (new, experimental, development, mature, ...) so that contributors
    know what they can and cannot use.
  * Once your code is good enough, propose your branch for merging
  * Your work will be evaluated by a member of the committers team.

    - If they accept your branch for integration in the official version, they
      will submit to the quality team that will review and merge in the official
      branch.
    - If the committer team refuses your branch, they will explain why
      so that you can review the code to better fit the guidelines (problem for
      future migrations, ...)

.. i18n: The `extra-addons branch <https://code.launchpad.net/~openerp-commiter/openobject-addons/trunk-extra-addons>`_,
.. i18n: that stores all extra modules, is directly accessible to all committers. If you
.. i18n: are a committer, you can work directly on this branch and commit your own work.
.. i18n: This branch does not require validation by the quality team. You should put
.. i18n: there your special modules for your own customers.
..

The `extra-addons branch <https://code.launchpad.net/~openerp-commiter/openobject-addons/trunk-extra-addons>`_,
that stores all extra modules, is directly accessible to all committers. If you
are a committer, you can work directly on this branch and commit your own work.
This branch does not require validation by the quality team. You should put
there your special modules for your own customers.

.. i18n: If you want to propose or develop new modules, we suggest creating your
.. i18n: own branch in the `openobject-addons project <https://launchpad.net/openobject-addons>`_
.. i18n: and develop within your branch. You can fill in a bug to request that
.. i18n: your modules are integrated in one of the two branches:
..

If you want to propose or develop new modules, we suggest creating your
own branch in the `openobject-addons project <https://launchpad.net/openobject-addons>`_
and develop within your branch. You can fill in a bug to request that
your modules are integrated in one of the two branches:

.. i18n:   * `extra-addons branch <https://code.launchpad.net/~openerp-commiter/openobject-addons/trunk-extra-addons>`_ : if your module touches a few companies
.. i18n:   * `addons <https://code.launchpad.net/~openerp/openobject-addons/trunk>`_ : if your module will be useful for most of the companies
..

  * `extra-addons branch <https://code.launchpad.net/~openerp-commiter/openobject-addons/trunk-extra-addons>`_ : if your module touches a few companies
  * `addons <https://code.launchpad.net/~openerp/openobject-addons/trunk>`_ : if your module will be useful for most of the companies

.. i18n: We invite all our partners and contributors to work in that way so that we can
.. i18n: easily integrate and share the work done between the different projects.
..

We invite all our partners and contributors to work in that way so that we can
easily integrate and share the work done between the different projects.

.. i18n: Registration and Configuration
.. i18n: ------------------------------
..

Registration and Configuration
------------------------------

.. i18n: Before you can commit on launchpad, you need to create a login.
..

Before you can commit on launchpad, you need to create a login.

.. i18n: Go to: https://launchpad.net --> log in / register on top right.
..

Go to: https://launchpad.net --> log in / register on top right.

.. i18n: You enter your e-mail address and you wait for an e-mail which will guide you trough the process needed to create your login.
..

You enter your e-mail address and you wait for an e-mail which will guide you trough the process needed to create your login.

.. i18n: This login is only needed if you intend to commit on bazaar on openerp-commiter or on your own branch.
..

This login is only needed if you intend to commit on bazaar on openerp-commiter or on your own branch.

.. i18n: You can refer to this link :
.. i18n: https://help.launchpad.net/YourAccount/NewAccount
..

You can refer to this link :
https://help.launchpad.net/YourAccount/NewAccount

.. i18n: Any contributor who is interested to become a committer must show his interest
.. i18n: on working for openerp project and ability to do it properly as
.. i18n: selection is based on merit. It can be by proposing bug
.. i18n: fixes, features requested on our :ref:`bug tracker <bug-tracker-link>` system.
.. i18n: You can even suggest additional modules and/or functionality on our :ref:`bug
.. i18n: tracker <bug-tracker-link>` system.
..

Any contributor who is interested to become a committer must show his interest
on working for openerp project and ability to do it properly as
selection is based on merit. It can be by proposing bug
fixes, features requested on our :ref:`bug tracker <bug-tracker-link>` system.
You can even suggest additional modules and/or functionality on our :ref:`bug
tracker <bug-tracker-link>` system.

.. i18n: You can contribute or join OpenERP team, : https://help.launchpad.net/Teams/Joining
..

You can contribute or join OpenERP team, : https://help.launchpad.net/Teams/Joining

.. i18n: Contributors are people who want to help the project improve, add
.. i18n: functionality and improve stability. Anyone can contribute on the project
.. i18n: by reporting bugs, proposing some improvement and
.. i18n: posting patch.
..

Contributors are people who want to help the project improve, add
functionality and improve stability. Anyone can contribute on the project
by reporting bugs, proposing some improvement and
posting patch.

.. i18n: The community team is available on launchpad: https://launchpad.net/~openerp-community
..

The community team is available on launchpad: https://launchpad.net/~openerp-community

.. i18n: Member of the quality and committer team are automatically members of the community.
..

Member of the quality and committer team are automatically members of the community.

.. i18n: Installing Bazaar
.. i18n: +++++++++++++++++
..

Installing Bazaar
+++++++++++++++++

.. i18n: .. index::
.. i18n:    single: Bazaar; installation
.. i18n:    single: Installation; Bazaar
.. i18n: .. 
..

.. index::
   single: Bazaar; installation
   single: Installation; Bazaar
.. 

.. i18n: Get Bazaar version control to pull the source from Launchpad.
..

Get Bazaar version control to pull the source from Launchpad.

.. i18n: To install bazaar on any ubuntu distribution, you can edit /etc/apt/sources.list by
..

To install bazaar on any ubuntu distribution, you can edit /etc/apt/sources.list by

.. i18n: ::
.. i18n: 
.. i18n:   sudo gedit /etc/apt/sources.list
..

::

  sudo gedit /etc/apt/sources.list

.. i18n: and put these lines in it:
..

and put these lines in it:

.. i18n: ::
.. i18n:  
.. i18n:   (for ubuntu intrepid 8.10)
.. i18n:   deb http://ppa.launchpad.net/bzr/ubuntu intrepid main
.. i18n:   deb-src http://ppa.launchpad.net/bzr/ubuntu intrepid main
.. i18n:   
.. i18n:   or (for ubuntu jaunty 9.04)
.. i18n:   deb http://ppa.launchpad.net/bzr/ubuntu jaunty main
.. i18n:   deb-src http://ppa.launchpad.net/bzr/ubuntu jaunty main
.. i18n:   
.. i18n:   or (for ubuntu karmic 9.10)  
.. i18n:   deb http://ppa.launchpad.net/bzr/ubuntu karmic main
.. i18n:   deb-src http://ppa.launchpad.net/bzr/ubuntu karmic main
.. i18n:   
.. i18n: Here, intrepid, jaunty and karmic are version names of ubuntu, replace it with your ubuntu version.
..

::
 
  (for ubuntu intrepid 8.10)
  deb http://ppa.launchpad.net/bzr/ubuntu intrepid main
  deb-src http://ppa.launchpad.net/bzr/ubuntu intrepid main
  
  or (for ubuntu jaunty 9.04)
  deb http://ppa.launchpad.net/bzr/ubuntu jaunty main
  deb-src http://ppa.launchpad.net/bzr/ubuntu jaunty main
  
  or (for ubuntu karmic 9.10)  
  deb http://ppa.launchpad.net/bzr/ubuntu karmic main
  deb-src http://ppa.launchpad.net/bzr/ubuntu karmic main
  
Here, intrepid, jaunty and karmic are version names of ubuntu, replace it with your ubuntu version.

.. i18n: Then, do the following
..

Then, do the following

.. i18n: ::
.. i18n: 
.. i18n:   sudo apt-get install bzr
..

::

  sudo apt-get install bzr

.. i18n: To work correctly, bzr version must be at least 1.3. Check it with the command:
..

To work correctly, bzr version must be at least 1.3. Check it with the command:

.. i18n: ::
.. i18n: 
.. i18n:   bzr --version
..

::

  bzr --version

.. i18n: If you have an older version check this url: http://bazaar-vcs.org/Download
.. i18n: On debian, in any distribution, the 1.5 version is working, you can get it on this url: http://backports.org/debian/pool/main/b/bzr/bzr_1.5-1~bpo40+1_i386.deb
..

If you have an older version check this url: http://bazaar-vcs.org/Download
On debian, in any distribution, the 1.5 version is working, you can get it on this url: http://backports.org/debian/pool/main/b/bzr/bzr_1.5-1~bpo40+1_i386.deb

.. i18n: If you experience problems with Bazaar, please read the :ref:`bazaar-faq-link` before asking any questions.
..

If you experience problems with Bazaar, please read the :ref:`bazaar-faq-link` before asking any questions.

.. i18n: Branch
.. i18n: ------
..

Branch
------

.. i18n: The combination of Bazaar branch hosting and Launchpad's teams infrastructure gives you a very powerful capability to collaborate on code. Essentially, you can push a branch into a shared space and anyone on that team can then commit to the branch.
..

The combination of Bazaar branch hosting and Launchpad's teams infrastructure gives you a very powerful capability to collaborate on code. Essentially, you can push a branch into a shared space and anyone on that team can then commit to the branch.

.. i18n: This means that you can use Bazaar in the same way that you would use something like SVN, i.e. centrally hosting a branch that many people commit to. You have the added benefit, though, that anyone outside the team can always create their own personal branch of your team branch and, if they choose, upload it back to Launchpad. 
..

This means that you can use Bazaar in the same way that you would use something like SVN, i.e. centrally hosting a branch that many people commit to. You have the added benefit, though, that anyone outside the team can always create their own personal branch of your team branch and, if they choose, upload it back to Launchpad. 

.. i18n: This is the official and proposed way to contribute on OpenERP and OpenObject.
..

This is the official and proposed way to contribute on OpenERP and OpenObject.

.. i18n: How to commit
.. i18n: -------------
..

How to commit
-------------

.. i18n: If you want to contribute on OpenERP or OpenObject, here is the proposed method:
..

If you want to contribute on OpenERP or OpenObject, here is the proposed method:

.. i18n:   * You create a branch on launchpad on the project that interests you. It's
.. i18n:     important that you create your branch on launchpad and not on your local
.. i18n:     system so that we can easily merge, share code between projects and
.. i18n:     centralize future developments.
.. i18n:   * You develop your own features or bugfixes
.. i18n:     in your own branch on launchpad. Don't forget to set the status of your
.. i18n:     branch (new, experimental, development, mature, ...) so that contributors
.. i18n:     know what they can and cannot use.
.. i18n:   * Once your code is good enough, propose your branch for merging
.. i18n:   * Your work will be evaluated by a member of the committers team.
.. i18n: 
.. i18n:     - If they accept your branch for integration in the official version, they
.. i18n:       will submit to the quality team that will review and merge in the official
.. i18n:       branch.
.. i18n:     - If the committer team refuses your branch, they will explain why
.. i18n:       so that you can review the code to better fit the guidelines (problem for
.. i18n:       future migrations, ...)
..

  * You create a branch on launchpad on the project that interests you. It's
    important that you create your branch on launchpad and not on your local
    system so that we can easily merge, share code between projects and
    centralize future developments.
  * You develop your own features or bugfixes
    in your own branch on launchpad. Don't forget to set the status of your
    branch (new, experimental, development, mature, ...) so that contributors
    know what they can and cannot use.
  * Once your code is good enough, propose your branch for merging
  * Your work will be evaluated by a member of the committers team.

    - If they accept your branch for integration in the official version, they
      will submit to the quality team that will review and merge in the official
      branch.
    - If the committer team refuses your branch, they will explain why
      so that you can review the code to better fit the guidelines (problem for
      future migrations, ...)

.. i18n: The extra-addons branch, that stores all extra modules, is directly accessible
.. i18n: to all committers. If you are a committer, you can work directly on this branch
.. i18n: and commit your own work. This branch does not require a validation of the
.. i18n: quality team. You should put there your special modules for your own customers.
..

The extra-addons branch, that stores all extra modules, is directly accessible
to all committers. If you are a committer, you can work directly on this branch
and commit your own work. This branch does not require a validation of the
quality team. You should put there your special modules for your own customers.

.. i18n: If you want to propose or develop new modules, we suggest creating your
.. i18n: own branch in the `openobject-addons project <https://launchpad.net/openobject-addons>`_
.. i18n: and develop within your branch. You can fill in a bug to request that
.. i18n: your modules are integrated in one of the two branches:
..

If you want to propose or develop new modules, we suggest creating your
own branch in the `openobject-addons project <https://launchpad.net/openobject-addons>`_
and develop within your branch. You can fill in a bug to request that
your modules are integrated in one of the two branches:

.. i18n:   * extra-addons : if your module touches a few companies
.. i18n:   * addons : if your module will be useful for most of the companies
..

  * extra-addons : if your module touches a few companies
  * addons : if your module will be useful for most of the companies

.. i18n: We invite all our partners and contributors to work in that way so that we can
.. i18n: easily integrate and share the work done between the different projects.
..

We invite all our partners and contributors to work in that way so that we can
easily integrate and share the work done between the different projects.

.. i18n: After having done that, your branch is public on Launchpad, in the `OpenObject
.. i18n: project <https://code.launchpad.net/openobject>`_, and committers can work on
.. i18n: it, review it and propose for integration in the official branch. The last line
.. i18n: allows you to rebind your branch to the one which is on launchpad, after having
.. i18n: done this, your commit will be applied on launchpad directly (unless you use ``--local``)::
.. i18n: 
.. i18n:   bzr pull    # Get modifications on your branch from others
.. i18n:   EDIT STUFF
.. i18n:   bzr ci    # commit your changes on your public branch
..

After having done that, your branch is public on Launchpad, in the `OpenObject
project <https://code.launchpad.net/openobject>`_, and committers can work on
it, review it and propose for integration in the official branch. The last line
allows you to rebind your branch to the one which is on launchpad, after having
done this, your commit will be applied on launchpad directly (unless you use ``--local``)::

  bzr pull    # Get modifications on your branch from others
  EDIT STUFF
  bzr ci    # commit your changes on your public branch

.. i18n: If your changes fix a public bug on launchpad, you can use this to mark the bug as fixed by your branch::
.. i18n: 
.. i18n:   bzr ci --fixes=lp:453123   # Where 453123 is a bug ID
..

If your changes fix a public bug on launchpad, you can use this to mark the bug as fixed by your branch::

  bzr ci --fixes=lp:453123   # Where 453123 is a bug ID

.. i18n: Once your branch is mature, mark it as mature in the web interface of launchpad
.. i18n: and request for merging in the official release. Your branch will be reviewed
.. i18n: by a committer and then the quality team to be merged in the official release.
..

Once your branch is mature, mark it as mature in the web interface of launchpad
and request for merging in the official release. Your branch will be reviewed
by a committer and then the quality team to be merged in the official release.

.. i18n: Answer and bug tracking and management
.. i18n: --------------------------------------
..

Answer and bug tracking and management
--------------------------------------

.. i18n: We use launchpad on the openobject project to track all bugs and features
.. i18n: request related to openerp and openobject. the bug tracker is available here:
..

We use launchpad on the openobject project to track all bugs and features
request related to openerp and openobject. the bug tracker is available here:

.. i18n:   * Bug Tracker : https://bugs.launchpad.net/openobject
.. i18n:   * Ideas Tracker : https://blueprints.launchpad.net/openobject
.. i18n:   * FAQ Manager : https://answers.launchpad.net/openobject
..

  * Bug Tracker : https://bugs.launchpad.net/openobject
  * Ideas Tracker : https://blueprints.launchpad.net/openobject
  * FAQ Manager : https://answers.launchpad.net/openobject

.. i18n: Every contributor can report bug and propose bugfixes for the bugs.
.. i18n: The status of the bug is set according to the correction.
..

Every contributor can report bug and propose bugfixes for the bugs.
The status of the bug is set according to the correction.

.. i18n: When a particular branch fixes the bug, a committer (member of the `Commiter
.. i18n: Team <https://launchpad.net/~openerp-commiter>`_) can set the status to "Fix
.. i18n: Committed". Only committers have the right to change the status to "Fix
.. i18n: Committed.", after they validated the proposed patch or branch that fixes the
.. i18n: bug.
..

When a particular branch fixes the bug, a committer (member of the `Commiter
Team <https://launchpad.net/~openerp-commiter>`_) can set the status to "Fix
Committed". Only committers have the right to change the status to "Fix
Committed.", after they validated the proposed patch or branch that fixes the
bug.

.. i18n: The `Quality Team <https://launchpad.net/~openerp>`_ have a look every day to
.. i18n: bugs in the status "Fix Committed". They check the quality of the code and merge
.. i18n: in the official branch if it's OK. To limit the work of the quality team, it's
.. i18n: important that only committers can set the bug in the status "Fix Committed".
.. i18n: Once quality team finish merging, they change the status to "Fix Released".
..

The `Quality Team <https://launchpad.net/~openerp>`_ have a look every day to
bugs in the status "Fix Committed". They check the quality of the code and merge
in the official branch if it's OK. To limit the work of the quality team, it's
important that only committers can set the bug in the status "Fix Committed".
Once quality team finish merging, they change the status to "Fix Released".

.. i18n: Translation
.. i18n: -----------
..

Translation
-----------

.. i18n: Translations are managed by 
.. i18n: the `Launchpad Web interface <https://translations.launchpad.net/openobject>`_. Here, you'll
.. i18n: find the list of translatable projects.
..

Translations are managed by 
the `Launchpad Web interface <https://translations.launchpad.net/openobject>`_. Here, you'll
find the list of translatable projects.

.. i18n: Please read the `FAQ <https://answers.launchpad.net/rosetta/+faqs>`_ before asking questions.
..

Please read the `FAQ <https://answers.launchpad.net/rosetta/+faqs>`_ before asking questions.

.. i18n: Blueprints
.. i18n: ----------
..

Blueprints
----------

.. i18n: Blueprint is a lightweight way to manage releases of your software and to track the progress of features and ideas, from initial concept to implementation. Using Blueprint, you can encourage contributions from right across your project's community, while targeting the best ideas to future releases. 
..

Blueprint is a lightweight way to manage releases of your software and to track the progress of features and ideas, from initial concept to implementation. Using Blueprint, you can encourage contributions from right across your project's community, while targeting the best ideas to future releases. 

.. i18n: Launchpad Blueprint helps you to plan future release with two tools:
..

Launchpad Blueprint helps you to plan future release with two tools:

.. i18n:     * milestones: points in time, such as a future release or development sprint
.. i18n:     * series goals: a statement of intention to work on the blueprint for a particular series. 
..

    * milestones: points in time, such as a future release or development sprint
    * series goals: a statement of intention to work on the blueprint for a particular series. 

.. i18n: Although only drivers can target blueprints to milestones and set them as series goals, anyone can propose a blueprint as a series goal. As a driver or owner, you can review proposed goals by following the Set goals link on your project's Blueprint overview page. 
..

Although only drivers can target blueprints to milestones and set them as series goals, anyone can propose a blueprint as a series goal. As a driver or owner, you can review proposed goals by following the Set goals link on your project's Blueprint overview page. 

.. i18n: By following the Subscribe yourself link on a blueprint page, you can ask Launchpad to send you email notification of any changes to the blueprint. In most cases, you'll receive notification only of changes made to the blueprint itself in Launchpad and not to any further information, such as in an external wiki.
..

By following the Subscribe yourself link on a blueprint page, you can ask Launchpad to send you email notification of any changes to the blueprint. In most cases, you'll receive notification only of changes made to the blueprint itself in Launchpad and not to any further information, such as in an external wiki.

.. i18n: However, if the wiki software supports email change notifications, Launchpad can even notify you of changes to the wiki page.
..

However, if the wiki software supports email change notifications, Launchpad can even notify you of changes to the wiki page.

.. i18n: If you're a blueprint owner and want Launchpad to know about updates to the related wiki page, ask the wiki admin how to send email notifications. Notifications should go to notifications@specs.launchpad.net. 
..

If you're a blueprint owner and want Launchpad to know about updates to the related wiki page, ask the wiki admin how to send email notifications. Notifications should go to notifications@specs.launchpad.net. 

.. i18n: The Blueprints for OpenERP are listed here:
.. i18n: 	
.. i18n: * https://blueprints.launchpad.net/openerp
.. i18n: * https://blueprints.launchpad.net/~openerp-commiter
..

The Blueprints for OpenERP are listed here:
	
* https://blueprints.launchpad.net/openerp
* https://blueprints.launchpad.net/~openerp-commiter
