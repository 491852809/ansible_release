from django.conf.urls import patterns, url, include

from rest_framework import routers
from api.api_setviews import *
from views import *

router = routers.SimpleRouter()
router.register(r'place_api', PlaceViewSet)
router.register(r'ip_info_api', Ip_InfoViewSet)
router.register(r'project_info_api', Project_InfoViewSet)
router.register(r'database_addr_api', Database_AddrViewSet)
router.register(r'database_conn_api', Database_ConnViewSet)
router.register(r'database_info_api', Database_InfoViewSet)
router.register(r'login_mode_api', Login_ModeViewSet)
router.register(r'log_save_api', Log_SaveViewSet)


urlpatterns = [
        url(r'', include(router.urls)),
]

# deploy page
urlpatterns += [
        url(r'^ip_info_add/\d*', ip_info_add),
        url(r'^ip_add_place', ip_add_place),
        url(r'^ip_info_main', ip_info_main),
]
