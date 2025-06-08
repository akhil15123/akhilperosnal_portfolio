from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=20)
    message = models.TextField(max_length=40)

    def __str__(self):
        return self.name


# ✅ Step 1 — Create a separate Category model
class Category(models.Model):
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
    code = models.CharField(max_length=50, choices=CATEGORY_CHOICES, unique=True)

    def __str__(self):
        return dict(self.CATEGORY_CHOICES).get(self.code, self.code)


# ✅ Step 2 — Change Project to use ManyToManyField
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/')
    categories = models.ManyToManyField(Category)
    technologies = models.CharField(max_length=200, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
