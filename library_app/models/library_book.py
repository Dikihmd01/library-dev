from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Book(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char(string='Title', required=True)
    isbn = fields.Char(string='ISBN')
    active = fields.Boolean(string='Active?', default=True)
    date_published = fields.Date()
    image = fields.Binary(string='Cover')
    publisher_id = fields.Many2one(comodel_name='res.partner', string='Publisher')
    author_ids = fields.Many2many(comodel_name='res.partner', string='Authors')    

    def _check_isbn(self):
        self.ensure_one()
        digits = [int(i) for i in self.isbn if i.isdigit()]

        if len(digits) == 13:
            ponderations = [1, 3] * 6
            terms = [a * b for a, b in zip(digits[:12], ponderations)]
            remain = sum(terms) % 10
            check = 10 - remain if remain != 0 else 0
            
            # print("===== digits", str(digits))
            # print("===== ponderations", str(ponderations))
            # print("===== terms", str(terms))
            # print("===== remain", str(remain))
            # print("===== check", str(check))
            # print("===== figinit[-1]", str(digits[-1]))

            return digits[-1] == check
    
    def button_check_isbn(self):
        for book in self:
            if not book.isbn:
                raise ValidationError("Please provide ISBN for %s" % book.name)
            
            if book.isbn and not book._check_isbn():
                raise ValidationError("%s ISBN is invalid" % book.isbn)
        
        return True
