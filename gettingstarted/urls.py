from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
	
	#The data incabuator 12 day related links
	path('tdi12/', hello.views.loadmain, name='tdi12'),
	path('tdi12vkeyword_search/', hello.views.keyword_search, name='tdi12vkeyword_search'),
	path('tdi12vshow_plot/', hello.views.show_plot, name='tdi12vshow_plot'),
]
