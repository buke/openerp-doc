
.. _translating_software:

OpenERP Translations
--------------------

Within the OpenERP source code, all translatable terms are written in international
English (language code ``en_US``). The Administrator of an OpenERP instance can
install additional languages among the official translations. As a result the corresponding
translations of all installed modules will be loaded in the database, and used to
replace the default English terms in the application interface when a user changes her
preferred language.

Regardless of what follows, if you are considering working on the OpenERP translations,
please read the general `Launchpad Translations Guidelines <https://help.launchpad.net/Translations/Guide>`_ 
before writing your first translation, as it includes very important advice for new translators.

There are 2 ways for contributors to add or modify translations in their languages:

    #. Work on Launchpad, OpenERP's community platform, using `the dedicate Translation 
       interface on Launchpad <http://translations.launchpad.net>`_, formerly known as Rosetta.
       This guarantees to work on the latest translation, and is automatically synchronized
       with the .po files of the source code. See :ref:`translations_rosetta` for more
       details.

    #. Work directly on the PO files, considering them as regular source code files, and thus
       sending a merge proposal of the .po patch to OpenERP, just like for a regular patch.
       This is explained in more details in :ref:`translations_code` section.

The first solution is strongly recommended when you are working on official OpenERP translations,
but sometimes the second solution is more efficient when you are translating new community modules.
These two solutions also have different access rights requirements, as explained below.

.. topic:: Can I do batch translations locally and then upload the ``.po`` files in batch in Launchpad?

    You can translate locally the ``.po`` files, then upload them using the *Upload translation*
    button that appears on top of each module's translations. For example to upload a French (fr) 
    translation for "account" in the trunk branch, you can use the following URL::

        https://translations.launchpad.net/openobject-addons/trunk/+pots/account/fr/+translate

    There is also one (beta, unsupported) technical tool available to perform mass upload of
    translations on Launchpad. It may be helpful if you want to translate offline or to copy
    translations from one branch to another. It's a Python script called ``lp_upload.py``,
    used in command-line mode. It can be found
    `here <http://bazaar.launchpad.net/~odo-openerp/+junk/openerp-utils/files>`_.

    We still really recommend working directly with Launchpad's translation interface whenever possible,
    due to the numerous advantages, detailed in :ref:`translations_rosetta`.

.. _translations_rosetta:

Translating with Launchpad
++++++++++++++++++++++++++

Launchpad provides a web-based translation interface, which can be
used to translate. Its main features are:

    * Being web-based, it is accessible everywhere for anyone and does not require
      any developer skill
    * It provides all the contextual information that a translator needs, and mentions
      the place where the term comes from inside the software, a critical information
      for proper translations.
    * Making use of the thousands of other open source project hosted on Launchpad,
      it is able to suggest similar translations from all other projects, speeding
      up the translator's work.
    * It provides reviewing features, and allows marking the terms that one thinks
      should be reviewed by other translators, easing collaboration further.
    * It comes with a specific access right system, and Launchpad Teams can be assigned
      to specific languages, making them responsible for the quality of the translations.
    * It is automatically synchronized with the source code files containing the
      translations, effectively replacing completely the need for manually updating
      them as explained in :ref:`translations_code`.

After registering on Launchpad, you can access the translations for any OpenERP project
by clicking on the *Translations* or *Help Translate* links on the homepage of the project.
You may also find the list of all (official and community-driven) translatable OpenERP-related
Launchpad projects: https://translations.launchpad.net/openobject.

Some quick links to the main OpenERP projects' translations:

    * https://translations.launchpad.net/openobject-server
    * https://translations.launchpad.net/openobject-addons
    * https://translations.launchpad.net/openobject-client
    * https://translations.launchpad.net/openobject-client-web
    * https://translations.launchpad.net/openobject-client-kde

Please also have a look at the `Launchpad Translations Documentation <https://help.launchpad.net/Translations/>`_
and `FAQ <https://answers.launchpad.net/rosetta/+faqs>`_.

Permissions for Translations on Launchpad
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OpenERP uses `structured permissions <https://help.launchpad.net/Translations/YourProject/PermissionPolicies>`_ 
for the Launchpad translations, which means three things:

    * Anyone is always free to suggest translations for OpenERP modules, clients and server.
    * If no translation team is assigned to a language, anyone can review or even accept a 
      given translation.
    * If a translation team is assigned to a language, only members of that team are allowed
      to review and accept the translations in this language, but anyone can still suggest
      translations.

See also Launchpad's Translations documentation for more details:

    * https://help.launchpad.net/Translations
    * https://help.launchpad.net/Translations/StartingToTranslate
    * https://answers.launchpad.net/rosetta/+faqs

Requesting the creation of assignation of a translation team
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If your language does not yet have an assigned translation you are free to create one
yourself, and request its assignation to that language. If the team already exists,
please contact its members to join their effort.

If you decide to `create a new team <https://launchpad.net/people/+newteam>`_ (anyone can do that),
please name it *openerp-i18n-XXX* where *XXX* is your language, for example *openerp-i18n-dutch*.
Please be sure to put a complete description for the team, explaining its purpose, how to join
(if you want to make it moderated or restricted, etc.) The description can be in your language,
and you could look at the description of existing translation teams if you need examples.
Please also have a look at the
`Launchpad recommendations for running a Localization team <https://help.launchpad.net/Translations/Guide#Running a localization team>`_.

When this is done, send a message through Launchpad to https://launchpad.net/~odo-openerp, requesting
the assignation of your new team.

After this point, anyone will still be free to propose and view translations for your language, but one will
need to be a member of your new team to be able to validate/accept them.

Reviewing translations on Launchpad
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When a translation team is assigned, it is in charge of reviewing every
translation made by the contributors before they can be used in the official
packages and branches.

If you are a member of a translation team, please make sure that new
suggestions are reviewed as soon as possible.
There are few things more disappointing than contributing and having your work
ignored! Fortunately Launchpad makes it pretty easy for you to keep up.

You can see how many strings need review on the project's translation page for
your language.
Just click on the number in the column "Need review" will directly open a page
with all the contributions waiting to be reviewed:

.. image:: img/translation-lp-template-list.png
   :width: 100%

One of the neat features of Launchpad is that it can keep several suggestions
for translating the same string. Launchpad will also suggest translations made in
completely different projects if it can.
As a reviewer, you are free to either choose the translation you find best, or
to make a new translation yourself.

When  none of the suggestions are good enough, you can also discard them by
checking "Dismiss all suggestions above.". They will be removed from the review
process and fall into oblivion - use wisely.

.. image:: img/translation-lp-review.png
   :width: 100%

.. topic:: Requesting review for your own translations

    While you are in charge of reviewing other's translation, you may also
    wish to new translations of your own, and have others review them.
    To this end, launchpad will present you with an additional checkbox
    labeled "Someone should review this translation". If you check this box,
    your contribution will be considered as a suggestion rather than a
    reviewed translation.
    
    If you are making lots of translations that to want others to review, 
    just leave the "Reviewer mode" to enter the "Translator mode". Launchpad
    will then check the box automatically for you.

    .. image:: img/translation-lp-translator-mode.png
       :width: 100%

.. topic:: Why am I credited for translations when I only reviewed someone else's contribution?

    When reviewing translations, you must be careful to select the suggestion
    and not copy/paste it into the "New translation" box, otherwise Launchpad
    may consider the contribution is yours.
    
    Also, if you change even a tiny bit from the translation (like correcting
    a small type), it will be considered a new suggestion and credited to you.

.. _translations_code:

Translating in the source code
++++++++++++++++++++++++++++++

As an alternative to Launchpad, translations may also be done in directly in the
source code, considering the translation files as regular source code files.
The result of a translator's work is essentially a regular *patch*, which may
only be published according to the specific permissions allowed on each project
code. To the contrary, when using Launchpad any validated translation is directly
committed by Launchpad in the official branches, without any further delay.

As no-one outside of OpenERP's Quality Team is allowed to directly commit
patches on the official branches, this means that a translation patch for
the official OpenERP project would need to be submitted using a regular merge proposal,
as described in :ref:`merge_proposals`.
If you still want to use this technique, you will first need to understand the
:ref:`translation_files_structure`.

You can edit the ``.po`` files directly using a PO editor such
as `POEdit <http://www.poedit.net>`_, or instead update the translations directly
within OpenERP and replace the existing ``.po`` by exporting updated ones using
OpenERP's translation export wizard.

We recommend you follow these steps to ensure the best result with this technique:

    #. read everything about the :ref:`translation_files_structure`
    #. grab the latest source code and create a new OpenERP database to start with,
       to make sure you have all the latest translation terms
    #. translate locally using OpenERP's interface or any other way you like
    #. if translating in OpenERP, re-export all `.po` files of your language for all modules
       over the current ones in the source using OpenERP's export wizard
    #. at that point you basically have a version of the code where your language's
       ``.po`` files are patched. You then need to commit and push these changes into
       a public branch on LP and make a merge proposal so OpenERP's quality team can merge
       the updated .po files into the official branches. Follow the regular procedure
       as explained in :ref:`merge_proposals`.


.. _translation_files_structure:

Translation files structure
+++++++++++++++++++++++++++

.. versionchanged:: 5.0 and 6.0

As of version 5.0, OpenERP uses exclusively the GetText Portable Object (a.k.a. ``*.po`` [#f_po]_)
standard format for storing translations. Numerous tools and libraries are available on most
platforms and programming languages to deal with this widespread format.

The translations are organized in several translations *domains*, where each domain is a
topic-specific area of OpenERP. Each *domain* has a separate list of translatable terms,
described in what is called a *PO Template* file, usually called ``domain.pot`` and found
in a ``i18n`` [#i18n]_ subdirectory specific to that domain. Each OpenERP client (GTK/Native
and Web) represent a separate domain, and each OpenERP module is also a separate domain.

A domain template file does not contain any translation, but only lists the available terms
to be translated. Translations are regular ``.po`` files that should be located in the same
subdirectory as their domain template, and respect the following naming convention.

.. warning::

    Domain templates files must be named ``domain.pot`` and located in a ``po`` or ``i18n``
    subdirectory.

    For *OpenERP 5.0*, translation files must be named ``lc_CC.po`` after the corresponding
    country and language code from ISO 3166 [#iso3166]_ and ISO 639-1 [#iso639_1]_.
    For example a translation in French from France would be ``fr_FR.po`` while one for
    Brazilian Portuguese would be ``pt_BR.po``.

    For *OpenERP 6.0*, translation files must be named ``lc_CC.po`` after the corresponding
    country and language code from ISO 3166 [#iso3166]_ and ISO 639-1 [#iso639_1]_, except for
    the canonical combinations, such as French from France or Portuguese from Portugal, which
    must only have the language code.
    For example a translation in French from France would be ``fr.po`` and one for regular
    Portuguese would be ``pt.po``, but one for Brazilian Portuguese would be ``pt_BR.po``.

    If you were looking for the domain template and Belgian Dutch translation of the
    ``account`` module, you would look for the following files in the addons project::
    
        account
         i18n
           account.pot
           nl_BE.po

.. [#f_po] http://www.gnu.org/software/autoconf/manual/gettext/PO-Files.html#PO-Files
.. [#iso3166] http://www.iso.org/iso/country_codes/iso_3166_code_lists.htm
.. [#iso639_1] http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
.. [#i18n] *i18n* is a common shortcut for *Internationalization*, as there are 18 letters
           between the first i and last n in this word.

