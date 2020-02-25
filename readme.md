# Project Overview

Great-Reads

## Project Description

My project idea was to create a site where people can go to add free campsites and look for free campsites.  I created an app called Free Camping with Django.  You can go on the site and search for campsites, add campsites, and review campsites.  You can add images of the campsite as well.  

The application has been deployed to Heroku


## Project Links

- [front end and back end repo](https://github.com/hrocco25/camping)
- [deployment](https://dispersed-camping.herokuapp.com/)



## Wireframes

- [wire frame](https://github.com/viviRbi/Great-reads/blob/master/plan/pr3_main.png)



#### MVP

- Campsites
    - See all campsites
    - Add new campsite
        -Name, description, days, sites, road condition, and location
    - View campsite details
    - Search Campsites
- Reviews
    - View reviews on a campsites
    - Add a new review
        -Title, name, content
-Fetch data from the backend 





#### PostMVP

- Interactive Map
- User Auth 
- Search by multiple things in search bar [complete]
- Image upload on campsites [complete]
- Additional Pages
    -FAQ, about, and how to find free camping
-Testing
-Distance between campsites

## Components


| Component | Description | 
| --- | :---: |  
| Apps |  Camping and Search | 
| Camping Views | camp list, camp detail, camp create, review list, review detail, and review create | 
| Camping Models | Camp and Review| 
| Search Views| Search Results| 
| Camping Forms | Review and Camp Form | 
| Camp Templates| Base, Camp Detail, Camp form, Camp List, and Review Form| 
| Search Template | Search | 

## Technology

-Django

## New Technologies

-Pillow
-AWS
-Bootstrap




## Code Snippets

Created a second app in my project for search and I used django's Q lookup to search for certain criteria.
```

def searchResult(request):
    camp=None
    query=None
    if "q" in request.GET:
        query = request.GET.get("q")
        camps = Camp.objects.all().filter(Q(name__icontains=query)| Q(location__icontains=query) | Q(description__icontains=query)).distinct()
    return render(request, 'search.html',{"query": query,"camps":camps})


I used images in my model and used Pillow and AWS for the images to work on Heroku
```
class Camp(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    description = models.TextField()
    road = models.CharField(default="Paved, Gravel, Dirt, or 4x4", max_length=100)
    management = models.CharField(max_length=100, default="Public or Private Land")
    number_of_campsites = models.PositiveIntegerField()
    number_of_days = models.PositiveIntegerField()
    image=models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name

```


## Issues and Resolutions

**ERROR**
  - Heroku does not work with images

**RESOLUTION**
  I created an AWS account with a bucket and user.  Attached my information to settings.py.  I have two different spots to score my secret key info one to use on heroku and one to use on localhost.  The one for heroku is in the config vars.  

   ``
    # local
    # from key import ACCESS, KEY

    # heroku
    ACCESS = os.environ['ACCESS']
    KEY = os.environ['KEY']

    AWS_ACCESS_KEY_ID = ACCESS
    AWS_SECRET_ACCESS_KEY = KEY

    AWS_STORAGE_BUCKET_NAME= 'camp-free'

    AWS_S3_FILE_OVERWRITE = False
    AWS_DEFAULT_ACL = None

    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


  ``

---


