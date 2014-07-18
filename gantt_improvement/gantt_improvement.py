from openerp.osv import fields, osv

class gantt_improvement(osv.osv):
    _inherit = 'res.users'
    #_name = 'gantt_improvement'

    def _get_day_offset(self, cr, uid, ids, field_name, arg, context=None):
        if isinstance(ids, (int, long)):
            ids = [ids]
        res = {}
        for so in self.browse(cr, uid, ids, context=context):
            res[so.id] = 555
        return res

    _columns = {
        'day_offset': fields.integer('Gant Offset'),
        #'day_offset': fields.function(_get_day_offset, type='integer', method=True, string="day_offset"),
    }