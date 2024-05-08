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
from .models import Slots  
admin.site.register(Slots)

from .models import Appointments  
admin.site.register(Appointments)

from .models import Payment  
admin.site.register(Payment)

from .models import LeaveRequest  
admin.site.register(LeaveRequest)

from .models import Blog  
admin.site.register(Blog)

from .models import ReferPatient  
admin.site.register(ReferPatient)

from .models import Donation  
admin.site.register(Donation)

from .models import Prescription  
admin.site.register(Prescription)