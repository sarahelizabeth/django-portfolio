from django.db import models

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=30)
    city = models.CharField(max_length=100)
    profile_img = models.ImageField()
    nav_img = models.ImageField()
    main_txt = models.TextField()
    about_txt = models.TextField(blank=True)
    nav_txt = models.TextField(blank=True)
    resume_txt = models.TextField(blank=True)
    website_link = models.URLField()
    linkedin_link = models.URLField(blank=True)
    github_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    facebook_link = models.URLField(blank=True)
    behance_link = models.URLField(blank=True)

    def __str__(self):
        return self.email

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateField()
    quote = models.TextField()
    role = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    profile_img = models.ImageField(blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    main_img = models.ImageField()
    secondary_img = models.ImageField(blank=True)
    created_date = models.DateField()
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)

    # Featured = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title
    
class Education(models.Model):
    school = models.CharField(max_length=200)
    major = models.CharField(max_length=200)
    degree_type = models.CharField(max_length=200)
    gpa = models.IntegerField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.major
    
class WorkExperience(models.Model):
    role = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.company
    
class Skill(models.Model):
    name = models.CharField(max_length=200)
    icon = models.CharField(max_length=20, blank=True)

    HACK = "HACK"
    MENTOR = "MENTOR"
    DEV = "DEV"
    GENRE_CHOICES = [
        (HACK, "Hacker"),
        (MENTOR, "Mentor"),
        (DEV, "Developer"),
    ]
    genre = models.CharField(max_length=6, choices=GENRE_CHOICES, default=DEV)

    FRAME = "FRAME"
    LANG = "LANG"
    DATA = "DATA"
    TEST = "TEST"
    TOOL = "TOOL"
    CATEGORY_CHOICES = [
        (FRAME, "Frameworks"),
        (LANG, "Programming Languages"),
        (DATA, "Data Analysis/Visualization"),
        (TEST, "Testing"),
        (TOOL, "Tools"),
    ]
    category = models.CharField(max_length=5, choices=CATEGORY_CHOICES, default=LANG)

    def __str__(self):
        return self.name
    