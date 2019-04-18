from django.db import models
from enum import Enum

__all__ = [
    'User', 'PersonalInfo', 'Address', 'Phone', 'Quality',
    'PersonalQuality', 'SeekingQuality', 'Endorsement',
    'Recommendation', 'Relationship', 'Family', 'School'
]

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100)
    type = models.CharField(max_length=20)
    salutation = models.CharField(max_length=10, null=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=50)
    status = models.CharField(max_length=10, default='Active')

class PersonalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    affiliation = models.CharField(max_length=20, null=True)
    birthdate = models.DateField()
    marital_status = models.CharField(max_length=20, default='Single')

class Address(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    addr1 = models.CharField(max_length=100, null=True)
    addr2 = models.CharField(max_length=100, null=True)
    addr3 = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=30, null=True)
    country = models.CharField(max_length=30)
    status = models.CharField(max_length=10, default='Active')

class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=20)
    type = models.CharField(max_length=10)
    status = models.CharField(max_length=10, default='Active')

class Quality(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.CharField(max_length=50)

class PersonalQuality(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quality = models.ForeignKey(Quality, on_delete=models.CASCADE)

class SeekingQuality(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quality = models.ForeignKey(Quality, on_delete=models.CASCADE)

class Endorsement(models.Model):
    id = models.AutoField(primary_key=True)
    quality = models.ForeignKey(PersonalQuality, on_delete=models.CASCADE)
    endorser = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    endorser_name = models.CharField(max_length=100, null=True)
    visible = models.BooleanField(default=True)

class Recommendation(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=500)
    about = models.ForeignKey(User, on_delete=models.CASCADE, related_name='about')
    by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='by')
    by_name = models.CharField(max_length=100, null=True)
    visible = models.BooleanField(default=True)


class RelationshipType(Enum):
    FRIEND = 'Friend'
    RELATIVE = 'Relative'
    MENTOR = 'Mentor'
    RAV = 'Rav'

class Relationship(models.Model):
    id = models.AutoField(primary_key=True)
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2')
    type = models.CharField(max_length=20, choices=[(tag, tag.value) for tag in RelationshipType])
    status = models.CharField(max_length=20, default='Pending')


class FamilyType(Enum):
    FATHER = 'Father'
    MOTHER = 'Mother'
    BROTHER = 'Brother'
    SISTER = 'Sister'
    STEP_FATHER = 'Step-Father'
    STEP_MOTHER = 'Step-Mother'
    CHILD = 'Child'

class Family(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    birthdate = models.DateField()
    relationship = models.CharField(max_length=20, choices=[(tag, tag.value) for tag in FamilyType])
    profession = models.CharField(max_length=100, null=True)
    school = models.CharField(max_length=100, null=True)

class School(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=100)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField()
    major = models.CharField(max_length=100, null=True)

class ReferenceType(Enum):
    RELATIVE = 'Relative'
    MENTOR = 'Mentor'
    RAV = 'Rav'
    TEACHER = 'Teacher'

class Reference(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    relationship = models.CharField(max_length=20, choices=[(tag, tag.value) for tag in ReferenceType])
    phone1 = models.CharField(max_length=20, null=True)
    phone2 = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)

# Experience
# Language
