from odoo.tests.common import TransactionCase


class TestBook(TransactionCase):
    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)
        self.Book = self.env['library.book']
        self.book1 = self.Book.create({
            'name': "Odoo dev",
            'isbn': '879-1-78439-279-6'
        })
    
    def test_book_create(self):
        "New Books are active by default"
        self.assertAlmostEqual(
            self.book1.active, True
        )