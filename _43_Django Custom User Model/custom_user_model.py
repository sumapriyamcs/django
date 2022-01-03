'''
1.Django comes with an excellent built-in User model and authentication support.
It is a primary reason most developers prefer Django over the Flask, FastAPI, AIOHttp,
and many other frameworks.

But sometimes we are not happy with the User model or we want to customize according to
the project requirements. Suppose we no longer want a username field at all. Or we want to
take the user's email instead of the default username. To do so, we need to customize our
default Django User model.

we will build the User Model from scratch. The one thing you should keep
in mind is that customizing the Django defaults adds lots of complexity to the complex system.
So try to stick with the default user model. But for the project requirements,
we can do the default changes.

We will use the Django Build-in AbastractBaseClass which inherit by the custom class name.

2.

Prerequisites
Install Latest Django (2.2 +)
Create Django project
Do the basic configuration
Create virtual environment

Creating Custom User Model in Django

Our first step is to create an app within the project using the following command.

python manage.py startapp MyUserModel

The app will be created in the project directory. Now register the app to the settings.py file.

MyUserModel/setting.py

INSTALLED_APP = [
?????
?????.
MyUserModel
]

3. Creating Model for Custom User

Now we will create the custom user model in the models.py file. Let's see the following code.

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(_('email_address'), unique=True, max_length = 200)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

   def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    def __str__(self):
        return self.email

Let's understand the above model; we created a class called CustomUser
that inherits the AbstractbaseClass. Then, we added a field for email, is_staff,
is_active, and date_joined.

The username is set to be none because we want to authenticate the user by its
unique email id instead of a username.

The is_staff returns true if the user allows login to the admin panel.

The is_active returns true if the user is currently active. If the user is not
active, he/she won't allow to log in.

The USERNAME_FIELDS defines the unique identification for the User model - to email.

The REQUIRED_FIELDS prompts the fields when we create a superuser by the createsuperuser
command. It must include any field for which blank is False.

The manager class object specifies that all objects for the class come from the
CustomeUserManager.The has_permission returns true if the user has each of the specified permission.

4. Create the Model Manager:

Django provides the built-in methods for the user manager. But if we are creating
the custom user model, we need to override the default methods. Create a new file
managers.py (can be vary) and create the User Model Manager. Below methods are provided
by the BaseUserManager.

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

    def get_full_name(self):

        #Returns the first_name plus the last_name, with a space in between.

        full_name = '%s %s' % (self.first_name, self.last_name)  
        return full_name.strip()  
  
    def get_short_name(self):  

        #Returns the short name for the user.

        return self.first_name   
        
We created CustomManagerClass that inherits the BaseUserManager. It provides the below helper methods.

The create_user() method creates, saves, and returns the User. It will automatically 
convert the email into the lowercase and the returned User object will have is_active set to true.
The create_superuser() method sets the is_staff and is_active to True.
The get_full_name() returns the user's full name.
The get_short_name returns the first_name of the user.

3.Register Custom User to setting.py:

It is necessary to register the created custom user model to setting.py file otherwise 
Django will consider it as a custom user model. It will through an error. Open the setting.py 
file and register your custom user model.

AUTH_USER_MODEL = appName.ClassName  
In our case, it will be -

AUTH _USER_MODEL = MyUserModel.CustomUser  

Now we can create and apply the make migration, which will create the new database that 
uses the custom user model. Let's run the following command.

python manage.py makemigrations  
python manage.py migrate  

We will get the migration file as below.

# Generated by Django 3.2.6 on 2021-08-09 19:55  
  
from django.db import migrations, models  
import django.utils.timezone  
  
class Migration(migrations.Migration):  
  
    initial = True  
  
    dependencies = [  
        ('auth', '0012_alter_user_first_name_max_length'),  
    ]  
  
    operations = [  
        migrations.CreateModel(  
            name='CustomerUser',  
            fields=[  
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  
                ('password', models.CharField(max_length=128, verbose_name='password')),  
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),  
                ('is_superuser', models.BooleanField(default=False, help_text='Designates 
                that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),  
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email_address')),  
                ('is_staff', models.BooleanField(default=False)),  
                ('is_active', models.BooleanField(default=True)),  
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. 
                A user will get all permissions granted to each of their groups.', related_name='user_set', 
                related_query_name='user', to='auth.Group', verbose_name='groups')),  
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions 
                for this user.', related_name='user_set', related_query_name='user', to='auth.Permission',
                verbose_name='user permissions')),  
            ],  
            options={  
                'abstract': False,  
            },  
        ),  
    ]  
As we can see that, there is no field of username because it was eliminated while creating the
custom user model.


5. Create a Superuser:

Run the below command to create superuser.

python manage.py createsuperuser  
Above command will prompt the email and password field to create a superuser.

Email address: test@test.com
Password:
Password (again):
Superuser created successfully.
Create Form to Store User Information

We will create a form using the default subclass UserCreationForm forms so that they can 
use the custom user model.

Let's create a forms.py file in "MyUserModel".

forms.py

from django.contrib.auth.forms import UserCreationForm, UserChangeForm  
from django.db.models import fields  
from django import forms  
from .models import CustomerUser  
from django.contrib.auth import get_user_model  
  
User = get_user_model()  
  
class CustomUserCreationForm(UserCreationForm):  
  
    password1 = forms.CharField(widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)  
  
    class Meta:  
        model = CustomerUser  
        fields = ('email', )  
      
    def clean_email(self):  
        email = self.cleaned_data.get('email')  
        qs = User.objects.filter(email=email)  
        if qs.exists():  
            raise forms.ValidationError("Email is taken")  
        return email  
  
    def clean(self):  

        #Verify both passwords match.

        cleaned_data = super().clean()  
        password1 = cleaned_data.get("password1")  
        password2 = cleaned_data.get("password2")  
          
        if password1 is not None and password1 != password2:  
            self.add_error("password2", "Your passwords must match")  
        return cleaned_data  
  
    def save(self, commit=True):  
        # Save the provided password in hashed format  
        user = super().save(commit=False)  
        user.set_password(self.cleaned_data["password1"])  
        if commit:  
            user.save()  
        return user          
      
  
class CustomUserChangeForm(UserChangeForm):  
    class Meta:  
        model = CustomerUser  
        fields = ('email', )  
  
    def clean_password(self):  
        # Regardless of what the user provides, return the initial value.  
        # This is done here, rather than on the field, because the  
        # field does not have access to the initial value  
        return self.initial["password1"]  
        
The CustomUserCreationForm class inherits the UsecreationForm that consists of three 
fields - username, password1, and password2. The password1 matches to the password2, 
if both password matches, the validate_password() validates the password and sets the user's 
password using set_password(). The password will be saved in the hashed format.

Now we will customize the Admin panel.

Custom Admin Panel

The default admin panel is quite useful and arranges the information efficiently 
but we can make it in our way by provides the required information. Let's see the 
following code of the admin panel.

admin.py

from django.contrib import admin  
from django.contrib.auth import authenticate  
from django.contrib.auth.admin import UserAdmin  
# Register your models here.  
class CustomUserAdmin(UserAdmin):  
    add_form = CustomUserCreationForm  
    form = CustomUserChangeForm  
    model = CustomerUser  
  
    list_display = ('email', 'is_staff', 'is_active',)  
    list_filter = ('email', 'is_staff', 'is_active',)  
    fieldsets = (  
        (None, {'fields': ('email', 'password')}),  
        ('Permissions', {'fields': ('is_staff', 'is_active')}),  
    )  
    add_fieldsets = (  
        (None, {  
            'classes': ('wide',),  
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}  
        ),  
    )  
    search_fields = ('email',)  
    ordering = ('email',)  
    filter_horizontal = ()  
  
admin.site.register(CustomerUser, CustomUserAdmin)  

Now we are ready to create the new user. Run the following command and login to the admin 
panel with the super user credentials.

Once we login into the admin panel. We see ADD CUSTOM USER button, where create new users.


'''