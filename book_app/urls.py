from django.urls import path
from .views import *

urlpatterns=[
    path('indexpage/',indexpageone),
    path('regpage/',register.as_view(),name='regpage'),
    path('login/',loginview.as_view(),name='login'),
    path('regdisplay/',dis.as_view(),name='regdisplay'),
    path('profilepage/<pk>',bookprofile.as_view(),name='profilepage'),
    path('bookpro/',userbookdetails.as_view(),name='bookpro'),
    path('deletesinglepro/<pk>',delsinglepro.as_view(),name='deletesinglepro'),
    path('bookprofileup/<pk>',bookprofileupdate.as_view(),name='bookprofileup'),
    path('about/',aboutpage),
    path('contactus/',contactus),
    path('homepage/',homepage),
    path('userpro/',profileview.as_view(),name='userpro'),
    path('userprodisp/',displayuserprofile.as_view(),name='userprodisp'),
    path('del/<pk>',deleteprofile.as_view(),name='del'),
    path('updatepro/<pk>',updateviewprofile.as_view(),name='updatepro'),
    path('detailpro/<pk>',detailprofile.as_view(),name='detailpro'),
    path('audiobookup/',audioview.as_view(),name='audiobookup'),
    path('audiobookdisp/',audiobookdisplay.as_view(),name='audiobookdisp'),
    path('audiodeta/<pk>',audiodetailview.as_view(),name='audiodeta'),
    path('updatebook/<pk>',audiopdate.as_view(),name='updatebook'),
    path('audiodel/<pk>',audiodelete.as_view(),name='audiodel'),
    path('bookprofiledetails/<pk>',detailbookone.as_view(),name='bookprofiledetails')


]