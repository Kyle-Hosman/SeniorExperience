from django.urls import path
#from .views import main, second_in
from .views import *

urlpatterns = [
    path('', main),
    path('second/', second_in),
    path('host/', host),
    path('state/', state),
    path('namesubject/', namesubject),
    path('port/', port),
    path('email/', email),
    path('bodymsg/', bodymsg),
    path('command/', command),
    path('count/', count),
    path('unit/', unit),
    path('timespec/', timespec),
    path('repo/', repo),
    path('dest/', dest)
]
