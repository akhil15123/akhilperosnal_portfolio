from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=20)
    message = models.TextField(max_length=40)

    def __str__(self):
        return self.name

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('python', 'Python'),
        ('django', 'Django'),
        ('odoo', 'Odoo'),
        ('javascript', 'JavaScript'),
        ('bootstrap', 'Bootstrap'),
        ('dataengineering', 'Data Engineering'),
        ('webdevelopment', 'Web Development'),
        ('ml', 'Machine Learning'),
    ]
    ...
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    technologies = models.CharField(max_length=200, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
