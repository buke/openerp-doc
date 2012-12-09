.. i18n: .. _documentation-guidelines-link:
.. i18n: 
.. i18n: ========================
.. i18n: Documentation Guidelines
.. i18n: ========================
..

.. _documentation-guidelines-link:

========================
文档指南
========================

.. i18n: Useful and concise documentation
.. i18n: ++++++++++++++++++++++++++++++++
.. i18n: Every ORM object method takes the same ``self``, ``cr``, ``uid`` parameters
.. i18n: and usually a list of ``ids`` and an optional ``context``, so it would be
.. i18n: quite redundant to copy/paste the *obvious* description for these parameters
.. i18n: every time:
..

实用和简洁的文档
++++++++++++++++++++++++++++++++
Every ORM object method takes the same ``self``, ``cr``, ``uid`` parameters
and usually a list of ``ids`` and an optional ``context``, so it would be
quite redundant to copy/paste the *obvious* description for these parameters
every time:

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     def action_send(self, cr, uid, ids, context=None):
.. i18n:         """ This sends an email to ALL the addresses of the selected partners.
.. i18n:         @param self: The object pointer
.. i18n:         @param cr: the current row, from the database cursor,
.. i18n:         @param uid: the current user ID for security checks
.. i18n:         @param ids: List of Phonecall to Opportunity's IDs
.. i18n:         @param context: A standard dictionary for contextual values
.. i18n:         """
.. i18n: 
.. i18n:     def action_send(self, cr, uid, ids, context=None):
.. i18n:         """ This sends an email to ALL the addresses of the selected partners.
.. i18n:         @param context['mail']: 'new' to send a new mail or 'reply' if to reply to the last case_history
.. i18n:         """
..

.. code-block:: python

    def action_send(self, cr, uid, ids, context=None):
        """ This sends an email to ALL the addresses of the selected partners.
        @param self: The object pointer
        @param cr: the current row, from the database cursor,
        @param uid: the current user ID for security checks
        @param ids: List of Phonecall to Opportunity's IDs
        @param context: A standard dictionary for contextual values
        """

    def action_send(self, cr, uid, ids, context=None):
        """ This sends an email to ALL the addresses of the selected partners.
        @param context['mail']: 'new' to send a new mail or 'reply' if to reply to the last case_history
        """
