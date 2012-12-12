
.. _bazaar-faq-link:

F.A.Q on Bazaar version control system
--------------------------------------

.. contents::

How to install bazaar ?
+++++++++++++++++++++++

To install bazaar on any ubuntu distribution, you can use::

  apt-get install bzr

To work correctly, bzr version must be at least 1.3. Check it with the command::

  bzr --version

If you have an older version check this url: http://bazaar-vcs.org/Download

On debian, in any distribution, the 1.5 version is working, you can get it on
this url: http://backports.org/debian/pool/main/b/bzr/bzr_1.5-1~bpo40+1_i386.deb

How to create a login on launchpad ?
++++++++++++++++++++++++++++++++++++

Before you can commit on launchpad, you need to create a login.

Go to: https://launchpad.net --> log in / register on top right.

You enter your e-mail address and you wait for an e-mail which will guide you trough the process needed to create your login.

This login is only needed if you intend to commit on bazaar on openerp-commiter or on your own branch.

How to commit ?
+++++++++++++++

Once your login is created, you need to create some ssh keys and insert them on
your login page (see create ssh keys on the left). These ssh keys are needed to
commit.

I advice you to follow these instructions to complete the creation of your
ssh keys: https://help.launchpad.net/YourAccount/CreatingAnSSHKeyPair

How to use Bazaar ?
+++++++++++++++++++

There are two ways to work on bzr. Either, you make a checkout, either you create a local branch.

Checkout method::

  bzr co lp:~openerp/openobject-addons/trunk -- to make a checkout
  bzr up                                     -- to make an update
  bzr ci                                     -- to commit

Creating a branch::

  bzr branch lp:~<url> <local dir>             -- to create a branch locally
  bzr pull                                     -- to update the branch
  bzr push lp:~<url>                           -- to include your changes in the remote branch

In any cases, when you experience some problems, you can do::

  bzr help

or ``bzr help <command>``. e.g.::

  bzr help branch

Some problems
+++++++++++++

Checkout does not work, I have this message error::

  bzr lp:~<url> 
  bzr: ERROR: Repository KnitPackRepository is not compatible with repository RemoteRepository

There are two ways to correct it.

Instead of using ``bzr co lp:~<url>``, use ``bzr co bzr+ssh://<yourlaunchpad login>@bazaar.launchpad.net/~<url>``

check this url: https://bugs.launchpad.net/bzr/+bug/205579. Generally, you do::

 bzr branch lp:~<url> 
 bzr reconfigure --checkout

