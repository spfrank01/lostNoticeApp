from django.conf.urls import url

from lostnotice import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),

    #lost notice
    url(r'^(?P<user_id>[0-9]+)/add_new_lost_item/$', views.add_new_lost_item, name='add_new_lost_item'),
    url(r'^save_new_item_lost/$', views.save_new_item_lost, name='save_new_item_lost'),
    url(r'^lost_notice/(?P<id>[0-9]+)/$', views.detail_lost_item, name='detail_lost_item'),
    #found owner
    url(r'^(?P<user_id>[0-9]+)/add_new_found_owner/$', views.add_new_found_owner, name='add_new_found_owner'),
    url(r'^save_new_found_owner/$', views.save_new_found_owner, name='save_new_found_owner'),
    url(r'^found_owner/(?P<id>[0-9]+)/$', views.detail_found_owner, name='detail_found_owner'),

    #register
    url(r'^register_page/$', views.register_page, name='register_page'),
    url(r'^register_complete/$', views.register_complete, name='register_check'),

    #login
    url(r'^login_page/$', views.login_page, name='login_page'),
    url(r'^login_check/$', views.login_check, name='login_check'),
    url(r'^profile/(?P<user_id>[0-9]+)/$', views.profile, name='profile'),
    #About
    url(r'^about/$', views.about, name='about'),
]