from django.contrib import admin
from django.urls import path
from exp_app import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Main_page , name='main_page'),
    path('login', views.Log_In, name='login'),
    # path('logout', views.Logout_view, name='logout'),
    # path('logout_owner', views.Logout_Owner_view, name='logout_owner'),
    path('user_login', views.User_Log_In, name='user_login'),
    path('owner_login', views.Owner_Log_In, name='owner_login'),
    path('user_registration', views.User_Registration, name='user_registration'),
    path('owner_registration', views.Owner_Registration, name='owner_registration'),
    path('user_home/<int:user_id>', views.User_home_page , name='user_home'),
    path('owner_home/<int:owner_id>', views.Owner_home_page , name='owner_home'),
    path('club_list/<int:user_id>/<str:club_filter>', views.Club_list_page, name='club_list'),
    path('my_history/<int:user_id>', views.My_history_page, name='my_history'),
    path('my_history/<int:user_id>/<int:payer_data>', views.Payment_page, name='payment'),
    path('about/<int:user_id>', views.About_page, name='about'),
    path('contact/<int:user_id>', views.Contact_page, name='contact'),
    path('club/<int:user_id>/<str:c_email>', views.Club_page , name='club'),
    path('inquiry_form/<int:user_id>/<str:c_email>', views.Inquiry_Form , name='inquiry_form'),
    path('owner_my_club/<int:owner_id>/<str:club_filter>', views.Owner_My_Club_Page , name='owner_my_club'),
    path('owner_analysis/<int:owner_id>', views.Owner_analysis_Page , name='owner_analysis'),
    path('owner_user_request/<int:owner_id>/<int:inq_data>', views.Owner_User_Request_Page , name='owner_user_request'),

    path('Owner_Contact/<int:owner_id>', views.Owner_Contact_Page , name='owner_contact'),
    path('add_new_club/<int:owner_id>', views.Add_new_club, name='add_new_club'),
    path('delete_club/<int:owner_id>', views.Delete_club, name='delete_club'),
    path('edit_club/<int:owner_id>', views.Edit_club, name='edit_club'),
    path('add_club_image/<int:owner_id>', views.Add_club_image, name='add_club_image'),
    path('dalete_club_image/<int:owner_id>', views.Delete_club_image, name='delete_club_image'),
    path('owner_club/<int:owner_id>/<str:c_email>', views.Owner_Club_Page , name='owner_club'),

    path ('event',views.Events, name='events'),
    path ('events_news',views.Events_News, name='events_news'),
    path ('elements',views.Elements, name='elements'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Add this line
