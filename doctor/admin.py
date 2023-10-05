from django.contrib import admin
from .models import Docprofile
admin.site.register(Docprofile)
# Register your models here.
from .models import UserProfile
admin.site.register(UserProfile)

from .models import Specialization
admin.site.register(Specialization)

from .models import Certification
admin.site.register(Certification)

from .models import PatientInfo  
admin.site.register(PatientInfo)
from .models import Timeslot  
admin.site.register(Timeslot)
