from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from .models import *
from datetime import datetime


def about(request):
    return render(request, 'bookInfo/about.html')


def book_list(request):
    books = Book.objects.all().values()
    params = {'entity': 'Book', 'objects': books}
    return render(request, 'bookInfo/list.html', params)


def bookshop_list(request):
    bookshops = BookShop.objects.all().values()
    params = {'entity': 'Bookshop', 'objects': bookshops}
    return render(request, 'bookInfo/list.html', params)


class BookShopCreate(CreateView):
    model = BookShop
    fields = ['address', 'name']
    success_url = '/bookshop'
    template_name = 'bookInfo/bookshop_form.html'


class BookShopUpdate(UpdateView):
    model = BookShop
    fields = ['address', 'name']
    pk_url_kwarg = 'bookshop_record_id'
    success_url = '/bookshop'
    template_name = 'bookInfo/bookshop_form.html'


class BookShopDelete(DeleteView):
    model = BookShop
    pk_url_kwarg = 'bookshop_record_id'
    success_url = '/bookshop'
    template_name = 'bookInfo/bookshop_delete_form.html'


def report(request):
    books = Book.objects.all()
    params = {'books': books, 'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    return render(request, 'bookInfo/report.html', params)


class BookCreate(CreateView):
    model = Book
    fields = ['title', 'author', 'bookshop_record_id']
    success_url = '/book'
    template_name = 'bookInfo/book_form.html'

    def get_context_data(self, **kwargs):
        context = super(BookCreate, self).get_context_data(**kwargs)
        context['form'].fields['bookshop_record_id'] = \
            forms.ModelChoiceField(queryset=BookShop.objects.all(),
            empty_label=None, label='Bookshop')
        return context


class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'author', 'bookshop_record_id']
    pk_url_kwarg = 'book_record_id'
    success_url = '/book'
    template_name = 'bookInfo/book_form.html'

    def get_context_data(self, **kwargs):
        context = super(BookUpdate, self).get_context_data(**kwargs)
        context['form'].fields['book_record_id'] = \
        forms.ModelChoiceField(queryset=BookShop.objects.all(),
        empty_label=None, label='Bookshop')
        return context


class BookDelete(DeleteView):
    model = Book
    pk_url_kwarg = 'book_record_id'
    success_url = '/book'
    template_name = 'bookInfo/book_delete_form.html'
