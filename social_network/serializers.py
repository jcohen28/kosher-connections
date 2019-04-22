from rest_framework.serializers import ModelSerializer
from social_network.models import User, PersonalInfo, Address, Phone, Quality, PersonalQuality, SeekingQuality, Endorsement, Recommendation, Relationship, Family, School, Reference


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class PersonalInfoSerializer(ModelSerializer):

    class Meta:
        model = PersonalInfo
        fields = '__all__'


class AddressSerializer(ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'


class PhoneSerializer(ModelSerializer):

    class Meta:
        model = Phone
        fields = '__all__'


class QualitySerializer(ModelSerializer):

    class Meta:
        model = Quality
        fields = '__all__'


class PersonalQualitySerializer(ModelSerializer):

    class Meta:
        model = PersonalQuality
        fields = '__all__'


class SeekingQualitySerializer(ModelSerializer):

    class Meta:
        model = SeekingQuality
        fields = '__all__'


class EndorsementSerializer(ModelSerializer):

    class Meta:
        model = Endorsement
        fields = '__all__'


class RecommendationSerializer(ModelSerializer):

    class Meta:
        model = Recommendation
        fields = '__all__'


class RelationshipSerializer(ModelSerializer):

    class Meta:
        model = Relationship
        fields = '__all__'


class FamilySerializer(ModelSerializer):

    class Meta:
        model = Family
        fields = '__all__'


class SchoolSerializer(ModelSerializer):

    class Meta:
        model = School
        fields = '__all__'


class ReferenceSerializer(ModelSerializer):

    class Meta:
        model = Reference
        fields = '__all__'
