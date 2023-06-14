from django.db import models


class Home(models.Model):
    """Home section"""
    name = models.CharField(max_length=20)
    greetings_1 = models.CharField(max_length=5)
    greetings_2 = models.CharField(max_length=5)
    picture = models.ImageField(upload_to='images/')

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """To display in django admin"""
        return self.name


class About(models.Model):
    """About section, person information"""
    heading = models.CharField(max_length=50)
    career = models.CharField(max_length=20)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='images/')

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career


class Profile(models.Model):
    """Social links section"""
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    social_name = models.CharField(max_length=10)
    link = models.URLField(max_length=200)


class Category(models.Model):
    """Category for skills name"""
    name = models.CharField(max_length=20)

    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name


class Skills(models.Model):
    """Information about particular skill"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=20)


class Portfolio(models.Model):
    """Links with images to projects"""
    image = models.ImageField(upload_to='images/')
    about = models.CharField(max_length=500)
    link = models.URLField(max_length=200)
    link_code = models.URLField(max_length=200)

    def __str__(self):
        return f'Portfolio {self.id}'
