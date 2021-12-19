from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.about, name='about'),
    path('bookshop', views.bookshop_list, name='bookshop'),
    path('bookshop/create', views.BookShopCreate.as_view()),
    path('bookshop/<int:bookshop_record_id>/update',
    views.BookShopUpdate.as_view(), name='bookshop_update'),
    path('class/<int:bookshop_record_id>/delete',
    views.BookShopDelete.as_view(), name='bookshop_delete'),
    path('book', views.book_list, name='book'),
    path('book/create', views.BookCreate.as_view()),
    path('book/<int:book_record_id>/update', views.BookUpdate.as_view(), name='book_update'),
    path('book/<int:book_record_id>/delete', views.BookDelete.as_view(), name='book_delete'),
    path('report', views.report, name='report')
]