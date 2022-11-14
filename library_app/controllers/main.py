from odoo import http

class Book(http.Controller):
    @http.route('/library/books')
    def book_list(self, **kwargs):
        Book = http.request.env['library.book']
        books = Book.search([('active','in',[True, False])])

        return http.request.render('library_app.book_list_template', {'books': books})