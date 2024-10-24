from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('providers/', views.providers, name='providers'),
    path('services/', views.home_services, name='home_services'),

    
    #ADMIN PATHS
    path('dashboard/', views.dashboard, name='admin-dashboard'),


    #Service Provider Paths


    path('service-provider/<int:provider_id>/', views.service_provider, name='service-provider'),
    path('add-service/', views.create_service, name='create_service'),
    path('create-post/', views.create_post, name='create_post'),
    path('bookings/', views.provider_bookings, name='provider-bookings'),
    path('update-provider/', views.update_service_provider, name='update-provider'),






    #HOME PAGE PATHS
    path('service-details/<int:service_id>/', views.service_details, name='service-details'),



    #CUSTOMER PATHS
    path('customer/account/', views.customer_account, name='customer-account'),
    path('create-new-event/', views.create_new_event, name='create-new-event'),
    path('update-event/', views.update_event, name='update-event'),
    path('remove-event/', views.remove_event, name='remove-event'),
    path('customer/added-service/', views.added_service_page, name='added-service-page'),
    path('update-customer-information/', views.update_customer_profile, name="update-customer-information"),

        # other URL patterns
    path('fetch-events/', views.fetch_events, name='fetch_events'),

    path('add-service-to-event/', views.add_service_to_event, name='add_service_to_event'),
    path('remove-service-from-event/<int:event_service_id>/', views.remove_service_from_event, name='remove_service_from_event'),



    path('comment-post/', views.add_comment_post, name='add_comment_post'),



    path('submit-booking-request/<int:event_id>/', views.submit_booking_request, name='submit_booking_request'),

    path('inquire/', views.inquire_service, name="inquire_service"),


    path('accept-booking/', views.accept_booking_request, name='accept-booking'),
    path('cancel-request/', views.cancel_booking_request, name='cancel-request'),


    path('add-ratings/', views.add_rating, name='add-rating'),



]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)