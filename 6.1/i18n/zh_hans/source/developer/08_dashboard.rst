
.. i18n: Dashboard 
.. i18n: =========
..

Dashboard 
=========

.. i18n: OpenERP objects can be created from PostgreSQL views. The technique is as follows :
..

OpenERP objects can be created from PostgreSQL views. The technique is as follows :

.. i18n:    1. Declare your _columns dictionary. All fields must have the flag **readonly=True.**
.. i18n:    2. Specify the parameter **_auto=False** to the OpenERP object, so no table corresponding to the _columns dictionary is created automatically.
.. i18n:    3. Add a method **init(self, cr)** that creates a *PostgreSQL* View matching the fields declared in _columns.
..

   1. Declare your _columns dictionary. All fields must have the flag **readonly=True.**
   2. Specify the parameter **_auto=False** to the OpenERP object, so no table corresponding to the _columns dictionary is created automatically.
   3. Add a method **init(self, cr)** that creates a *PostgreSQL* View matching the fields declared in _columns.

.. i18n: **Example** The object report_crm_case_user follows this model.
..

**Example** The object report_crm_case_user follows this model.

.. i18n: .. code-block:: python
.. i18n: 
.. i18n:     class report_crm_case_user(osv.osv):
.. i18n:         _name = "report.crm.case.user"
.. i18n:         _description = "Cases by user and section"
.. i18n:         _auto = False
.. i18n:         _columns = {
.. i18n:             'name': fields.date('Month', readonly=True),
.. i18n:             'user_id':fields.many2one('res.users', 'User',
.. i18n:                                       readonly=True, relate=True),
.. i18n:             'section_id':fields.many2one('crm.case.section', 'Section',
.. i18n:                                          readonly=True, relate=True),
.. i18n:             'amount_revenue': fields.float('Est.Revenue',
.. i18n:                                            readonly=True),
.. i18n:             'amount_costs': fields.float('Est.Cost', readonly=True),
.. i18n:             'amount_revenue_prob': fields.float('Est. Rev*Prob.',
.. i18n:                                                 readonly=True),
.. i18n:             'nbr': fields.integer('# of Cases', readonly=True),
.. i18n:             'probability': fields.float('Avg. Probability',
.. i18n:                                         readonly=True),
.. i18n:             'state': fields.selection(AVAILABLE_STATES, 'State',
.. i18n:                                       size=16, readonly=True),
.. i18n:             'delay_close': fields.integer('Delay to close',
.. i18n:                                           readonly=True),
.. i18n:             }
.. i18n:         _order = 'name desc, user_id, section_id'
.. i18n:         
.. i18n:         def init(self, cr):
.. i18n:             cr.execute("""
.. i18n:          CREATE OR REPLACE VIEW report_crm_case_user AS (
.. i18n:          SELECT
.. i18n:              min(c.id) as id,
.. i18n:              SUBSTRING(c.create_date for 7)||'-01' as name,
.. i18n:              c.state,
.. i18n:              c.user_id,
.. i18n:              c.section_id,
.. i18n:              COUNT(*) AS nbr,
.. i18n:              SUM(planned_revenue) AS amount_revenue,
.. i18n:              SUM(planned_cost) AS amount_costs,
.. i18n:              SUM(planned_revenue*probability)::decimal(16,2)
.. i18n:                   AS amount_revenue_prob,
.. i18n:              avg(probability)::decimal(16,2) AS probability,
.. i18n:              TO_CHAR(avg(date_closed-c.create_date),
.. i18n:                      'DD"d" `HH24:MI:SS') AS delay_close
.. i18n:          FROM
.. i18n:              crm_case c
.. i18n:          GROUP BY SUBSTRING(c.create_date for 7), c.state,
.. i18n:                   c.user_id, c.section_id
.. i18n:          )""")
.. i18n:     report_crm_case_user()
..

.. code-block:: python

    class report_crm_case_user(osv.osv):
        _name = "report.crm.case.user"
        _description = "Cases by user and section"
        _auto = False
        _columns = {
            'name': fields.date('Month', readonly=True),
            'user_id':fields.many2one('res.users', 'User',
                                      readonly=True, relate=True),
            'section_id':fields.many2one('crm.case.section', 'Section',
                                         readonly=True, relate=True),
            'amount_revenue': fields.float('Est.Revenue',
                                           readonly=True),
            'amount_costs': fields.float('Est.Cost', readonly=True),
            'amount_revenue_prob': fields.float('Est. Rev*Prob.',
                                                readonly=True),
            'nbr': fields.integer('# of Cases', readonly=True),
            'probability': fields.float('Avg. Probability',
                                        readonly=True),
            'state': fields.selection(AVAILABLE_STATES, 'State',
                                      size=16, readonly=True),
            'delay_close': fields.integer('Delay to close',
                                          readonly=True),
            }
        _order = 'name desc, user_id, section_id'
        
        def init(self, cr):
            cr.execute("""
         CREATE OR REPLACE VIEW report_crm_case_user AS (
         SELECT
             min(c.id) as id,
             SUBSTRING(c.create_date for 7)||'-01' as name,
             c.state,
             c.user_id,
             c.section_id,
             COUNT(*) AS nbr,
             SUM(planned_revenue) AS amount_revenue,
             SUM(planned_cost) AS amount_costs,
             SUM(planned_revenue*probability)::decimal(16,2)
                  AS amount_revenue_prob,
             avg(probability)::decimal(16,2) AS probability,
             TO_CHAR(avg(date_closed-c.create_date),
                     'DD"d" `HH24:MI:SS') AS delay_close
         FROM
             crm_case c
         GROUP BY SUBSTRING(c.create_date for 7), c.state,
                  c.user_id, c.section_id
         )""")
    report_crm_case_user()
