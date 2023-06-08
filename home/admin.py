from django.contrib import admin
from .models import PersonalInfo, Testimonial, Project, Education, WorkExperience, Skill

admin.site.register(PersonalInfo)
admin.site.register(Testimonial)
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(Skill)