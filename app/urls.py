from django.contrib import admin
from django.urls import path
from . import views 
from .views import export_to_excel

urlpatterns = [
    #path('', views.home, name="home"),
    path('', views.index, name='index'),
    path('service/', views.service, name="service"),
    path('service_low/', views.service_low, name="service_low"),
    path('service_high/', views.service_high, name="service_high"),
    path('warning_spider/', views.warning_spider, name="warning_spider"),  
    path('warning_dspm/', views.warning_dspm, name="warning_dspm"),
    path('warning_scada/', views.warning_scada, name="warning_scada"),
    path('warning_mtmn/', views.warning_mtmn, name="warning_mtmn"),
    path('warning_data/', views.warning_data, name="warning_data"),    
    path('base/', views.base, name="base"),
    path('chart_system/', views.chart_system, name="chart_system"),    
    path('chart_fee/', views.chart_fee, name="chart_fee"),
    path('chart_fee_system/', views.chart_fee_system, name="chart_fee_system"),    
    # Other URL patterns
    path('export/', export_to_excel, name='export_to_excel'),
    # Other URL patterns
    path('export_query_to_csv/', views.export_query_to_csv, name='export_query_to_csv'),
    #tạo table
    path('addnew',views.addnew, name='addnew'),  
    path('edit/<int:serial>', views.edit, name='edit'),  
    path('update/<int:serial>', views.update, name='update'),  
    path('delete/<int:serial>', views.destroy, name='destroy'),  
]
