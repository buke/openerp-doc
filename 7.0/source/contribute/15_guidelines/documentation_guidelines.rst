.. _documentation-guidelines-link:

========================
Documentation Guidelines
========================

Useful and concise documentation
++++++++++++++++++++++++++++++++
Every ORM object method takes the same ``self``, ``cr``, ``uid`` parameters
and usually a list of ``ids`` and an optional ``context``, so it would be
quite redundant to copy/paste the *obvious* description for these parameters
every time:

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


