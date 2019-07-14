from django.conf.urls import url, include
from . import views  


urlpatterns = [
    url(r'^$', views.index),
    url(r'^books$', views.books),
    url(r'^authors$', views.authors),
    url(r'^books/(?P<book_id>\d+)$', views.book_descrip),
    url(r'^authors/(?P<author_id>\d+)$', views.author_descrp),
    url(r'^add_book$', views.add_book),
    url(r'^add_author$',views.add_author),
    url(r'^add_authors_to_book/(?P<book_id>\d+)$', views.add_author_to_book),
    url(r'^add_book_to_author/(?P<author_id>\d+)$', views.add_book_to_author),
    url(r'^delete_book/(?P<book_id>\d+)$', views.delete_book),
    url(r'^delete_author/(?P<author_id>\d+)$', views.delete_author),
]