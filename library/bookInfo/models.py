from django.db import models

class BookShop(models.Model):
    bookshop_record_id = models.AutoField('bookshop_record_id', primary_key=True)
    address = models.TextField('address')
    name = models.CharField('name', max_length=30)

    def __str__(self):
        return f'{self.name}{self.address}'

class Book(models.Model):
    book_record_id = models.AutoField('book_record_id', primary_key=True)
    title = models.CharField('title', max_length=30)
    author = models.CharField('author', max_length=20)
    bookshop_record_id = models.ForeignKey('BookShop',
                                           models.DO_NOTHING,
                                           db_column='bookshop_record_id',
                                           verbose_name='bookshop')

