from osv import fields, osv

class mrp_repair_line(osv.osv):
	_inherit = 'mrp.repair.line'

	_columns = {
		'usuario': fields.many2one('res.users','Usuario'),
		'date':  fields.date('Fecha'),
	}
mrp_repair_line()
