from rest_framework import routers

from api.apps.companies.views import CompanyViewSet

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
