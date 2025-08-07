from django.db import models

genres = [
    ('Action','Action'),('Horror','Horror'),('Romance','Romance'),
    ('Thriller','Thriller'),('Drama','Drama'),('Fiction','Fiction')
]

languages = [
    ('English','English'),('Tamil','Tamil'),('Hindi','Hindi'),('Kannada','Kannada'),('Telugu','Telugu')
]
# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=300)
    genre = models.CharField(max_length=300,choices=genres,null=True, blank=True)
    language = models.CharField(max_length=300,choices=languages,null=True,blank=True)
    synopsis = models.TextField(null=True,blank=True)
    duration_minutes = models.IntegerField(null=True,blank=True)
    release_date = models.DateField(null=True,blank=True)
    trailer_url = models.URLField(null=True,blank=True)
    status = models.CharField(max_length=300, choices=[('Upcoming','Upcoming'),('Released','Released')], null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)
    movie_image = models.ImageField(upload_to='movies/',null=True,blank=True)
    slug = models.CharField(max_length=2000,null=True,blank=True)


    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = '-'.join((self.title + ' ' + str(self.release_date) + ' ' + self.genre + ' ' + self.language).split())
        super().save(*args,**kwargs)
    
class Cast(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='casts')
    name = models.CharField(max_length=300)
    role = models.CharField(max_length=300)
    image = models.ImageField(upload_to='casts/',null=True,blank=True)