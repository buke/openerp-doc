Dashboard 
=========

OpenERP objects can be created from PostgreSQL views. The technique is as follows :

   1. Declare your _columns dictionary. All fields must have the flag **readonly=True.**
   2. Specify the parameter **_auto=False** to the OpenERP object, so no table corresponding to the _columns dictionary is created automatically.
   3. Add a method **init(self, cr)** that creates a *PostgreSQL* View matching the fields declared in _columns.

**Example** The object report_crm_case_user follows this model.


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
