'''
1.Django Image Upload | How to Upload Image with Django:

Image uploading is one of the main features of any modern web-applications.
It allows the user to upload the image or picture on the server. Fortunately,
Django provides the simple procedure of working with the images especially
uploading the images or pictures. Using this, we can create a beautiful web
application where users can upload images with captions.

In this tutorial, we will discuss how the upload the image in a Django application.
Before we are going further, make sure that you have a basic knowledge of Django.

2.Upload images to Django:

Most of the web applications deal with the file or images, Django provides the
two model fields that allow the user to upload the images and files. These
fields are FileField and ImageField; basically ImageField is a specialized version
of FileField that uses Pillow to confirm that file is an image.

models.py :

from django.db import models

class UploadImage(models.Model):
    caption = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.caption

3.We create the UploadImage model that consists of two fields - caption and image.
The image field will work as Django's file storage API. This API provides the
facility to store and retrieve the files and also read and write them.
The upload_to parameter specifies the file location where the image will be stored.

We don't need to create the media directory manually; it will be automatically
created when we upload an image.

First of all, we need to install the pillow library, which helps work with the
images. We can install it using the following pip command.

pip install Pillow

Now add the following settings to the settings.py file of your project.

settings.py

# Base url to serve media files
MEDIA_URL = '/media/'

# Path where media is stored
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

MEDIA_URL - It will serve the media files.
MEDIA_ROOT - It specifies the path of the root where file will be stored.
In the next step, we should add the following configuration in urls.py file.

Urls.py

from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('sampleapp.urls'), namespace='sampleapp'))

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

All required configurations are done; we are ready to run the following commands.

python manage.py makemigations
python manage.py migrate

After running this command, we are set to create a form that will take the
image as input from the user. Let's create a form.

forms.py

from django.db import models
from django.forms import fields
from .models import UploadImage
from django import forms


class UserImage(forms.ModelForm):
    class meta:
        # To specify the model to be used to create form
        models = UploadImage
        # It includes all the fields of model
        fields = '__all__'

The advantage of creating the Django model form is that it can handle the form
verification without declaring it explicitly in the script. It will also create
the form fields on the page according to the model fields mentioned in the model.py file.

To display this form, we need to create the image_form.html file under the template folder.

template/image.form.html

{% extends 'base.html' %}

{% block content %}
    <form method="post" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Upload</button>
    </form>

    {% if img_obj %}
        <h3>Succesfully uploaded : {{img_obj.caption}}</h3>
        <img src="{{ img_obj.image.url}}" alt="connect" style="max-height:300px">
    {% endif %}

{% endblock content %}


Note - We use the enctype = "multipart/form-data" which allows files to be sent
through a POST. Without enctype, the user cannot send the file through a POST request.
It is necessary to include in the form to work with the files or image.

Now we will create the view to handle the requests.

View.py

from django.shortcuts import redirect, render
from sampleapp.forms import UserImageForm
from .models import UploadImage

def image_request(request):
    if request.method == 'POST':
        form = UserImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            # Getting the current instance object to display in the template
            img_object = form.instance

            return render(request, 'image_form.html', {'form': form, 'img_obj': img_object})
    else:
        form = UserImageForm()

    return render(request, 'image_form.html', {'form': form})

The above view is simple and handling images the same as a normal form. When
we upload the image, the post request will be generated. The form is automatically
validated and saved in the media folder. One point to be noted, we get the image
object using form.instance and it will be used to display the image to web page.

Let's create the URL for this view.

sampleapp/urls.py

from django.urls import path
from .views import image_request

app_name = 'sampleapp'
urlpatterns = [
    path('', image_request, name = "image-request")

we have discussed how to upload images using Django. Django provides the simple
interface to perform image or file uploading. We just need to do some configuration
and define an ImageField in the model form's field. We can also upload any file
(.xml, .pdf, .word, .etc) by following the same procedure, but we will need to
convert ImageField to FileField in the model's field.


'''