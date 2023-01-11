from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    ncf_validation_target = fields.Selection(
        related="company_id.ncf_validation_target",
        readonly=False,
        required=True,
    )
<<<<<<< HEAD

    ncf_validation_dgii = fields.Boolean(related="company_id.ncf_validation_dgii", readonly=False)
=======
>>>>>>> 7c4183ce94ed163916759ae4253eed777d61441b
    validate_ecf = fields.Boolean(related="company_id.validate_ecf", readonly=False)
