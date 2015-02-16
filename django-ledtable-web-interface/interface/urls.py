from django.conf.urls import patterns, url

from interface import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.AnimationBuilderView.as_view(), name='animation_builder'),
    #url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^build/$', views.build, name='build'),
)