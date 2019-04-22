from django.views.decorators.csrf import csrf_exempt
from rest_framework.routers import SimpleRouter

from social_network import views

router = SimpleRouter()

router.register(r'user', views.UserModelViewSet)
router.register(r'personalinfo', views.PersonalInfoModelViewSet)
router.register(r'address', views.AddressModelViewSet)
router.register(r'phone', views.PhoneModelViewSet)
router.register(r'quality', views.QualityModelViewSet)
router.register(r'personalquality', views.PersonalQualityModelViewSet)
router.register(r'seekingquality', views.SeekingQualityModelViewSet)
router.register(r'endorsement', views.EndorsementModelViewSet)
router.register(r'recommendation', views.RecommendationModelViewSet)
router.register(r'relationship', views.RelationshipModelViewSet)
router.register(r'family', views.FamilyModelViewSet)
router.register(r'school', views.SchoolModelViewSet)
router.register(r'reference', views.ReferenceModelViewSet)

urlpatterns = router.urls
