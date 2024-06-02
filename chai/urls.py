
from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.all_chai,name='all_chai'),
    path('<int:chai_id>/',views.chaiDetail,name='chaiDetail'),
    path('chaistores/',views.chaiStoreView,name='chaiStores')
    
    
    
    
]