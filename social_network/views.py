from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.viewsets import ModelViewSet

from social_network.serializers import UserSerializer, PersonalInfoSerializer, AddressSerializer, PhoneSerializer, QualitySerializer, PersonalQualitySerializer, SeekingQualitySerializer, EndorsementSerializer, RecommendationSerializer, RelationshipSerializer, FamilySerializer, SchoolSerializer, ReferenceSerializer
from social_network.models import User, PersonalInfo, Address, Phone, Quality, PersonalQuality, SeekingQuality, Endorsement, Recommendation, Relationship, Family, School, Reference

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return

class UserModelViewSet(ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PersonalInfoModelViewSet(ModelViewSet):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer


class AddressModelViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class PhoneModelViewSet(ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer


class QualityModelViewSet(ModelViewSet):
    queryset = Quality.objects.all()
    serializer_class = QualitySerializer


class PersonalQualityModelViewSet(ModelViewSet):
    queryset = PersonalQuality.objects.all()
    serializer_class = PersonalQualitySerializer


class SeekingQualityModelViewSet(ModelViewSet):
    queryset = SeekingQuality.objects.all()
    serializer_class = SeekingQualitySerializer


class EndorsementModelViewSet(ModelViewSet):
    queryset = Endorsement.objects.all()
    serializer_class = EndorsementSerializer


class RecommendationModelViewSet(ModelViewSet):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer


class RelationshipModelViewSet(ModelViewSet):
    queryset = Relationship.objects.all()
    serializer_class = RelationshipSerializer


class FamilyModelViewSet(ModelViewSet):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer


class SchoolModelViewSet(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class ReferenceModelViewSet(ModelViewSet):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer
