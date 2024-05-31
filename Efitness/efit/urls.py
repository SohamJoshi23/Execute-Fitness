from django.urls import path
from efit import views
# from django.contrib import admin

urlpatterns = [
    path('', views.Home, name='Home'),
    path('trainers/',views.Trainers,name='Trainers'),
    path('About/', views.about, name='about'),
    path('Gallery/',views.Gallery,name='Gallery'),
    path('Membership/',views.MembershipData,name='Membership'),
    path('BMI/',views.Bmical,name='Bmical'),
    path('Diet/',views.Diet1,name='Diet1'),
    path('FG/',views.FG,name='FG'),
    path('TF/',views.TF,name='TF'),
     path('price/',views.price,name='price'),
    path('bmi/',views.bmi,name='bmi'),
    # path('admin/', admin.site.urls),
    
    # path('submit-membership-form/', views.submit_membership_form, name='submit_membership_form'),
]