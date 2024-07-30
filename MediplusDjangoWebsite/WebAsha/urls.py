from django.urls import *
from .views import *


urlpatterns = [
    path('home/',view_home, name='home'),
    path('doctos/',view_doctos, name='doctos'),
    path('sevice/',view_service,name='service'),  #http:127.0.0.1:800/webasha/
    path('contact/',view_contact,name='contact'),
    path('appointment/',view_appointment,name='appointment'),
    path('thankyou/',view_thakyou,name='thankyou'),
    path('thanks/',view_thanks,name='thanks'),
    path('ear/', ear_treatment, name='ear'),
    path('blood/', blood_treatment, name='blood'),
    path('heart/', heart_treatment, name='heart'),
    path('vision/', vision_treatment, name='vision'),
    path('teeth/', teeth_treatment, name='teeth'),
    path('general/', general_treatment, name='general'),
    path('hearthealth',view_heart_health,name='hearthealth'),
    path('diabeties',view_diabeties,name='diabeties'),
    path('management',view_management,name='management'), 
    path('visioncare',view_vision_care,name='vision'), 
    path('earhealth',view_ear_health,name='earhealth'), 
    path('testimonials/', view_testimonials, name='testimonials'),
    path('finance/', view_finance, name='finance'),
    path('consulting/', view_consulting, name='consulting'),
    path('faq/',view_faq,name='faq'),
    path('othercases/',view_our_cases,name='ourcases'),
    path('about/',view_about,name='about'),
    path('doctors/',view_doctors,name='doctors'),
    path('newsletter/', subscribe_newsletter, name='newsletter'),

    
   
]
    
    
    
