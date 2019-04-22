from django.db import models
from enum import Enum

__all__ = [
    'User', 'PersonalInfo', 'Address', 'Phone', 'Quality',
    'PersonalQuality', 'SeekingQuality', 'Endorsement',
    'Recommendation', 'Relationship', 'Family', 'School'
]

class StatusType(Enum):
    ACTIVE = 'Active'
    INACTIVE = 'Inactive'

class SalutationType(Enum):
    RABBI = 'Rabbi'
    MISS = 'Miss'
    MS = 'Ms.'
    MRS = 'Mrs.'
    MR = 'Mr.'
    DR = 'Dr.'

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100, unique=True)
    type = models.CharField(max_length=20, default='Dater')
    salutation = models.CharField(max_length=10, choices=[(tag.name, tag.value) for tag in SalutationType], blank=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=[(tag.name, tag.value) for tag in StatusType], default='ACTIVE')

    @property
    def full_name(self):
        return ' '.join(name for name in [self.salutation, self.first_name, self.middle_name, self.last_name] if name)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'user'

class MaritalStatusType(Enum):
    SINGLE = 'Single'
    MARRIED = 'Married'
    BUSY = 'Busy'
    ENGAGED = 'Engaged'
    DIVORCED = 'Divorced'
    WIDOWED = 'Widowed'

def headshot_file_name(instance, filename):
    return '/'.join(['headshots', str(instance.user.id), filename])

def resume_file_name(instance, filename):
    return '/'.join(['resumes', str(instance.user.id), filename])

class PersonalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    affiliation = models.CharField(max_length=20, blank=True)
    birthdate = models.DateField()
    height = models.CharField(max_length=10, blank=True)
    headshot = models.ImageField(null=True, blank=True, upload_to=headshot_file_name)
    resume = models.FileField(null=True, blank=True, upload_to=resume_file_name)
    marital_status = models.CharField(max_length=20,
                                      choices=[(tag.name, tag.value) for tag in MaritalStatusType],
                                      default='SINGLE')

    def image_tag(self):
        return u'<img src="{{ MEDIA_URL }}{path}" />'.format(path=self.headshot.upload_to)
    image_tag.short_description = 'Headshot Image'

    class Meta:
        db_table = 'personal_info'

class Address(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    addr1 = models.CharField(max_length=100, blank=True)
    addr2 = models.CharField(max_length=100, blank=True)
    addr3 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=30, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=30)
    status = models.CharField(max_length=10, choices=[(tag.name, tag.value) for tag in StatusType], default='ACTIVE')

    class Meta:
        db_table = 'address'

class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=20)
    type = models.CharField(max_length=10)
    status = models.CharField(max_length=10, choices=[(tag.name, tag.value) for tag in StatusType], default='ACTIVE')

    class Meta:
        db_table = 'phone'

class Quality(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.value

    class Meta:
        db_table = 'quality'

class PersonalQuality(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quality = models.ForeignKey(Quality, on_delete=models.CASCADE)

    class Meta:
        db_table = 'personal_quality'

class SeekingQuality(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quality = models.ForeignKey(Quality, on_delete=models.CASCADE)

    class Meta:
        db_table = 'seeking_quality'

class Endorsement(models.Model):
    id = models.AutoField(primary_key=True)
    quality = models.ForeignKey(PersonalQuality, on_delete=models.CASCADE)
    endorser = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    endorser_name = models.CharField(max_length=100, blank=True)
    visible = models.BooleanField(default=True)

    class Meta:
        db_table = 'endorsement'

class Recommendation(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=500)
    about = models.ForeignKey(User, on_delete=models.CASCADE, related_name='about')
    by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='by')
    by_name = models.CharField(max_length=100, blank=True)
    visible = models.BooleanField(default=True)

    class Meta:
        db_table = 'recommendation'


class RelationshipType(Enum):
    FRIEND = 'Friend'
    RELATIVE = 'Relative'
    MENTOR = 'Mentor'
    RAV = 'Rav'
    ENGAGED = 'Engaged'
    MARRIED = 'Married'

class RelationshipStatusType(Enum):
    PENDING = 'Pending'
    CONFIRMED = 'Confirmed'
    DENIED = 'Denied'

class Relationship(models.Model):
    id = models.AutoField(primary_key=True)
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2')
    type = models.CharField(max_length=20, choices=[(tag.name, tag.value) for tag in RelationshipType])
    status = models.CharField(max_length=20, choices=[(tag.name, tag.value) for tag in RelationshipStatusType], default='PENDING')

    class Meta:
        db_table = 'relationship'


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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    birthdate = models.DateField()
    relationship = models.CharField(max_length=20, choices=[(tag.name, tag.value) for tag in FamilyType])
    profession = models.CharField(max_length=100, blank=True)
    school = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = 'family'

class School(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=100)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField()
    major = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = 'school'

class ReferenceType(Enum):
    RELATIVE = 'Relative'
    MENTOR = 'Mentor'
    RAV = 'Rav'
    TEACHER = 'Teacher'

class Reference(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    relationship = models.CharField(max_length=20, choices=[(tag.name, tag.value) for tag in ReferenceType])
    phone1 = models.CharField(max_length=20, blank=True)
    phone2 = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    class Meta:
        db_table = 'reference'

# Experience
# Language
