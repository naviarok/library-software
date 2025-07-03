from django.urls import path
from .views import Home, Success, Error, HomeRedirect, ExportExcel, LoginUser, Table, LogoutUser

urlpatterns = [
    path('home/', Home, name='home'),
    path('', HomeRedirect, name='homeRedirect'),
    path('success/', Success, name='success'),
    path('error/', Error, name='error'),
    path('excel/', ExportExcel, name='excel'),
    path('login/', LoginUser, name='login'),
    path('logout/', LogoutUser, name='logout'),
    path('table/', Table, name='table'),
]