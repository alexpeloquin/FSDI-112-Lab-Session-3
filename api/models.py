from django.db import models
from tastypie.resources import ModelResource, ALL
from movies.models import Movie, Genre

# Create your models here.
# Model the data that will go into the front end
# API aka resources

class MovieResource(ModelResource):
    class Meta:
        resource_name = "movies"
        # What query to be run to get data
        queryset = Movie.objects.all()
        #excludes = ['price']
        # Filtering is done with a ? at the end of the URL address
        # ?stock__gt=11
        filtering = {'price':ALL,"stock":ALL,}

class GenreResource(ModelResource):
    class Meta:
        resource_name = "genres"
        # What query to be run to get data
        queryset = Genre.objects.all()
        #excludes = ['price']
        # Filtering is done with a ? at the end of the URL address
        # ?stock__gt=11
        filtering = {'name':ALL}

