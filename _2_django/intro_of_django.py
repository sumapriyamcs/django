'''
1.DJANGO:

1. Django is a high-level Python web framework that encourages rapid development and
clean, pragmatic design.
2. Django is a web development framework that assists in building and maintaining quality
web applications.
3. Django helps eliminate repetitive tasks making the development process an easy and time
saving experience.
4. Django makes it easier to build better web apps quickly and with less code.
5. It is tells to standardize (or) structure the application related files (python) in an organised
manner.
6.The django most popular rapid application development where each and every set of
instruction need not to completely instead. We can go with the less size of code to do a
particular task.
7.Rapid development is a process of developing the application quickly and efficiently.
8.Some of the large scale applications are Instagram, Udemy, Dropbox, Uber, and Netflix.

2.History of Django:

1. 2003 − Started by Adrian Holovaty and Simon Willison as an internal project at the
Lawrence Journal-World newspaper.
2.2005 − Released July 2005 and named it Django, after the jazz guitarist Django
Reinhardt.
3.2005 − Mature enough to handle several high-traffic sites.
4.Current − Django is now an open source project with contributors across the world.

3.Django comes with the following design philosophies:

1. Loosely Coupled: Django aims to make each element of its stack independent of the others.

2.Less Coding: Less code so in turn a quick development.
3.Don't Repeat Yourself (DRY): Everything should be developed only in exactly one place instead
of repeating it again and again.
4.Fast Development: Django's philosophy is to do all it can to facilitate hyper-fast
development.
5.Clean Design: Django strictly maintains a clean design throughout its own code and
makes it easy to follow best web-development practices.

3.Advantages of Django:

Here are few advantages of using Django which can be listed out here −
1.Object-Relational Mapping (ORM) Support − Django provides a bridge between
the data model and the database engine, and supports a large set of database systems
including MySQL, Oracle, Postgres, etc. Django also supports NoSQL database
through Django-nonrel fork. For now, the only NoSQL databases supported are
MongoDB and google app engine.

2.Multilingual Support − Django supports multilingual websites through its built-in
internationalization system. So you can develop your website, which would support
multiple languages.

3.Framework Support − Django has built-in support for Ajax, RSS, Caching and
various other frameworks.

4.Administration GUI − Django provides a nice ready-to-use user interface for
administrative activities.

5.Development Environment − Django comes with a lightweight web server to
facilitate end-to-end application development and testing.

4.Github:
Github is version control tool which is used has a repository to store our projects in
centralized memory location so that the people can able to accessing from anywhere any part
of the world provide internet is present.
There are two types of github account first one public account and second one private
account.
1) Public account:
It is a type of account which can be created for free of cost and it contain in it can be
access by any one.
2) Private account:
It is a type of account which is created by paying some money and the accessibility
given only to the given persons.
The pubic account can it not safe to store our project and project related information
everybody easy the access of source code.

5.Configuring github in our system:

To configuration the git in our system we need to download and install the git-scm in
our computer.
Steps:
1. Open any browser and go to search bar and type git-scm/download.

2. Display the links of git-scm download and click on it open the git-scm download
page.
3. Choose the windows operating system and version number for windows to click on
download button.
4. After that downloaded exe file and double click on downloaded file and click on
install and given the permissions.
5. Once after installation restart the command prompt and type git and press enter.
6. It you see some information about git which get display on the cmd than its means
that git-scm is connected configuration successfully.
7. Login to github account in browser ad display the home page of github your
account and click on ―+‖ symbol in right side corner.
8. Select the new repository and specify the repository name and select the public
access and click on create repository button.
9. After that it goes to give you some set of commands that you need to use it. When
upload your project to git repository.
10. Given the commands:
The below commands is used to load the project to the newly created repository.

>> git init
>> git add path of the project file (or) .
>> git commit -m “first commit”
>> git branch –M main
>> git remote add origin (giturl)
>> git push –u origin main

The below commands is used to load the project to the existing repository.
>> git remote add origin (giturl)
>> git branch –M main
>> git push –u origin main

Git init:
It is used to create the local git container in the present directory.
Git add path of the project:
It is used to add the project files to the local git repository by converting into its own
git format.
Git commit –m “first commit”:
It is the command is used to save the changes ―first commit‖ we are comment to the
passing to name of the commit.
Git branch –M main:
It is used create a main thread of the git hub.
Git remote add origin giturl/repository:
It is used to establish a connection between the local git repository to the git
repository.
Git push –u origin main:
It is used to push the code to the repository that is present.

It is used to establish a connection between the local git repository to the git
repository.
Git push –u origin main:
It is used to push the code to the repository that is present.

Git push –u origin main:
It is used to push the code to the repository that is present.

6.Command prompt commands:
commands that is used in widows for the operation in command prompt
1. mkdir: it is command which is used to create a directory or folder
syntax:
mkdir folder_name
2. cd : it is command which is used to change the working location from the current directory
to the specified path
Syntax:
cd path_of_directory
cd.. (will get you out from current directory and keeps control in its parent directory)
cd../..(will get you out from current directory and keeps control in its grand parent
directory)

3. In unix/windows/linux/mac . means current directory
.. means parent directory
4: rmdir it is a command used to remove directory
syntax:
rmdir foldername folder should be empty
rmdir /s /q folderpath folder will be deleted forcefully
5. del: used to delete files
del filepath_with_extn
6: jumping from drive to drive
synatx: driveletter:
ex:
c:\users\venugopal\desktop\akshay_django>D:
d:\>

7.Django frame-work:
1. A web application framework is a toolkit of all components needed for application
development.

2. Django is a high-level open source python based frame work which is responsible for
rapid development of web application with clean programmatic design with more
security.
3. Django follows MVC and MVT DESIGN PATTERNS.
Design pattern:
Design patterns are used describe how the data and code segregation should be done
There are two types of Design patterns:
1.MVC------->MODEL VIEW CONTROL
2.MVT------->MODEL VIEW TEMPLATE

MVC:
It is design pattern which responsible for designing an application with the separation of data
happens in the following format
MODEL:
Model is responsible for writing all the operations related to the DATABASE.
VIEW:
This is file where we write the logic by using python program this is used for
displaying the content to the user
CONTROL:
Django frame work itself take care of this controlling part
MVT:
While designing an application we have to concentrate on three important points
1. Layout (html, css, js)
2. Logic (python programming language)
3. Data (database operations)
MVT is similar to MVC design pattern but in case of MVT design pattern we will be
responding an html layout as a response to the request sent by the client-user

8.Creation of development environment:
1.An environment is a setup that we do for the execution of project successfully.
Environment is classified into two categories:
1. The real time environment (or) actual environment
2. The virtual environment
It is the environment with the set it up inside our computer permanently to that
whenever are running a project inside our computer think should run in an efficient
way every time we use the project in different computer. We can able to create this
setup every time because is consume lot of time and effect to set it up everything.

To avoid this we create to portable environment where everything will install
along with the project to that every time. Whenever we wanted to and a project diff

computer as the environment is portable. We just need to carry it and activate it. This
is going to reduce lot of time and effect.
Virtual environment is a concept of splitting one actual environment into multiple
numbers of virtual environments splitting one pc into n virtual pc is a task of virtual
environment.
To create a virtual environment are two possible.
1. By utilizing python distribution
2. By utilizing library called virtual environment(env)

9.Installation of virtual environment:
1 step: first install python software required version and set by click on add python
path. Once after installation go to command prompt type PIP (packaging
installer python) and press enter.
Note: if pip is not their do like below steps.
2 step: if you get error message taken that python is a neither an internal or external
command than go to path where python is install and copy the path.
C: \user\username\AppData\local\programs\python\python version.
3 step: it is the place where ever python interpreter is present than
4 Step: press the start button type ENV and click on edit system environment variable
 Follow by click on ―Environment variable‖ button inside.
 Find the path both in USER VARIABLE and SYSTEM VARIABLE
environment.
 Double click on path click on NEW button than paste the path on interpreter is
pres
 One more time click on NEW button paste the path with suffix as scripts file.
 And click on ok upon ENV window is close.
 And restart your pc and go to command prompt
 Type PIP and click enter
 Check so that the environment setup is ready or not.

Process 1:
Command to create Virtual Environment:
 1.First select the folder, in that folder path will copy and after that go to search bar in
that folder type CMD
2.Than open the command prompt after that type the command and press entre
Syntax: python<space>–m<space>venv<space>env (or) any_env_name
Example: cd E:\venu_django\project1\python –m venv env
env means user given environment name
venv means virtual environment

Immediately after creating virtual environment on brand new system will be created.
Brand new system which is created will be having the following files:
1. Lib
2. Scripts
3. Environment configuration
After environment is created select the scripts folder than copy that path

1.Open the command prompt after that paste the scripts path to activate the environment
type <path of environment>\env_name\scripts\activate and press enter.
Example: cd E:\venu_django\env\scripts\activate

2.To come to the environment we need to deactivate a environment for that just type
“deactivate” press enter.
Process

Process 2: Create a third Party Virtual Environment.

1. Step: make sure your computer is connect into the internet (only by installation packages).
    1.1 Installation of any library‘s will be done by using ―PIP‖ with the
“pip install name_of_library”
2. Step: In the second process the virtual environment is created by using the library
―virtualenv‖ and we need to install the library first by using pip.
“pip install virtualenv” press enter.

3. Step: once after the install successfully of virtualenv and create a virtual environment
using below command.
virtualenv <space><path of environment>\name_of_env press enter
(Or)
virtualenv name_of_env press enter
4.Step: Activate and Deactivate environments are same as proces1.

Once activating the environment the changes that we do will have its impact only for that
environment.

Note: Once after install/creating the environment we don‘t need to have python in the global
system because already we have a dedicated interpreter pip everything in each environment.
(Note: it is not a best practice).

Installation of any third party library will be done by using: PIP
―pip install (3 diff type) ―
There are three ways to install the libraries:
1) Installing the library of current version done by using the command.

“pip install library_name”.
2) Installing the library of specific version done by using the command.
“pip install library_name == version_number”
3) Installing from a librarys that is specified in a file will be done by a install command.
“pip install –r <path of file>”
Note: name of the requirement file with path
Usually when we talk about large set of projects there will be ―n‖ no of library that
might be us need but we cannot install all the library‘s one after another because it is a
time consuming process.
The requirement file and that file will be creating and write the only library name that is
either library_name or library_name==version.

10.Installation of DJANGO:
The command of install the django
―pip install django‖ (current version)
―pip install django==2.2‖ (specific version)
1.Once after successfully installation of Django we will get a file called ―djangoadmin‖.
2.To check that type command is “django-admin” press enter
3.Display the all the django-admin files.
4.If you don‘t get django-admin files not a internal or external command error than your
installation is successfully.

How to Create a Django Project:
1. To create a Django-project we use a command
“django-admin startproject project_name”
(Create a project in current directory)

User command Django-admin startproject project_name will create a project in the
specified path with the given project name.
1.Once after the creation of project to check whether successfully created (or) not
2.In that project folder there are automatically created the project files.

Where run server using below command
Get into outer project directory using ―cd‖ command
“cd project_name”
1.To run the server use command
“python manager.py runserver”
Copy the URL /IP address that is given and paste it inside the browser and press
enter.
1.If you get a congratulation page than installation is happen successfully.

11.Three different ways to create a project:
1) Project in the specifed directory
2) Project in the current directory
3) Creating a project with the container
1) Project in the specifed directory:
Django-admin startproject project path

Example:In the specified path the project files will be created.
(env) E:\venu_django\project1>django-admin startproject project1
E:\venu_django\project1

2) Project in the current directory:
Django-admin startproject projectname .

Example:In the current directory to which the ―cmd prompt” is pointing to project file will
be created in ―django-admin startproject project2 .‖
(env) E:\venu_django\project2>django-admin startproject project2 .

3) Creating a project with the container.
Django-admin startproject projectname

Example: In this project created by the specified directory but in this project created by
outer project as well as inner project with manage.py
(env) E:\venu_django>django-admin startproject project3


12.Describe the project files inside the project.

1.__init__.py:

Initialization file in which contains the statement that is necessary for the project presetup.
It is blank python script. Because of this special file name, django treated this
folder as python package

2.Setting.py:

This file is responsible for the integration of the project related settings and
configurations such as DB setting, media settings, IP settings, other settings and
installed app settings.

3.Urls.py:

This is the file which is responsible for url navigations. Here we have to store all our
url-patterns of our project. For every view (webpage), we have to define separate urlpattern.
End user can use url-patterns to access our web pages.

4.Wsgi.py: [Web Server Gateway Interface]

Wsgi is like watchman/gatekeeper. It will be checked & authenticated the browser
requests come to the file called wsgi.py in the server. There server response will also
passing through the wsgi only. Wsgi has the capability to handle only synchronous
request [browser request]. We can use this file while deploying / hosting our
application in production on online server

5.Asgi.py: [Asynchronous Server Gateway Interface]

Similar to wsgi.py but it will handle only asynchronous request that comes from
sockets (or) web scraping algorithms. Asgi will be present only in Django 3.X above
versions.

6.Manage.py:

Maintains & manage all the operations of a project or in a project. It is a command
line utility to interact with django project in various ways like to run development
server, run tests, create migrations etc

7.Web Scraping:
It is phenomenal of extracting the information from a web application without using
browser.

13.Web Application working flow in internet using url‟s:

Whenever we need to enter into the server we should know some set of basic things and there
are:
1) Request should be readable (or) encrypted format
2) What is the address of the server
3) Entry point (or) port number
4) Where to navigate and what to display
To know about all this information the first format thing is how we do carry this information
the answer is using ―URLs‖
―URLs‖ expanded as Uniform Resource Locator that helps as to locate the required set of
resource from the specific area or specific location.

The url is return as: http://www.example.com
http://www.facebook.com/venugopal
http://www.facebook.com/venugopal/profile
http://www.pyspider.com/
The format of url will be protocol://baseurl/primarysuffix/secondary suffix/……..
Protocol:
It is a set of rules and regulations using which request will be sent to the server.
There are two types of protocols:
1) http (hyper text transfer protocol)
2) https (hyper text transfers protocol security)

14.HTTP:

HTTP (Hypertext Transfer Protocol) is the base of the data communication for the
web this is how the internet works when it comes to delivering the web pages. It is TCP/IP
based protocol and things like text, audio, videos, images can be transmitted through it.
HTTP works on request and response cycle where the client requests a web page. Suppose,
if you browse to google.com, you are requesting a web page from the server, and the server
will deliver you response.

It is basic protocol that we use to send a request from the browser to a server. In this
type request will be in readable format and it is a default protocol that developer going to
used and it is a free protocol as well.

15.HTTPS:

HTTPS (Hypertext Transfer Protocol Secure) is nothing but the HTTP working in
tandem with SSL (Secure Socket Layer) that is the ―S‖ in HTTPS. SSL takes care of
ensuring that the data goes securely over the internet. The alternative names given to HTTPS
are HTTP over TLS, HTTP over SSL and HTTP secure.

This protocol was designed to increase primarily on the internet when communicating
with web sites and sending sensitive data. This made man-in-the-middle attack increasingly
difficult as the data send is no longer in plain text.

It is protocol we use to whenever we wanted to send the data in the encrypted format
using request. Whenever we wanted to extract or sent the useful information and important
information in that case go for ‗https‘ protocol. It is paid protocol.

15.Diff between HTTP and HTTPS:

1. HTTP URL in your browser's address bar is http:// and the HTTPS URL is https://.
2. HTTP is unsecured while HTTPS is secured.
3. HTTP doesn't require domain validation, where as HTTPS requires at least domain
validation and certain certificates even require legal document validation.
4. No encryption in HTTP, with HTTPS the data is encrypted before sending on the
other hand encryption and decryption is used in https.
5. HTTP is subject to man-in-the middle and eavesdropping attacks(hacking) and
HTTPS is designed to resist man-in-the middle and eavesdropping attacks and is
considered secure against such attacks.
6. HTTP is no paid protocol and HTTPS is paid protocol.

16.Base URL:

A base URL is, basically, the consistent part of your web address. For example,
throughout this training site, you'll note that the address section http://pyspider.com always
appears in the address bar. This is the base URL. Everything that follows it is known as
a URL path.

Base URL will decide where will go server (or) it contains the address of the server
will the entry point address. The address of the server is called as IP address entry point
address is called as port number.
BaseURL format : ―http://IP address : port number‖

Ex: 120.0.0.1:8000
By default the IP address is development server is 127.0.0.1: and the port number is address
in django is 8000.

17.Suffix:

The suffix will decide to which particular function the control should be navigated to
the suffix is segregated into various sub parts is primary suffix, secondary suffix and so on…

18.How to URL navigation in client and server:

1. A browser on the web requests an origin web server web page. This generates a request
to DNS for the numeric IP address of the web server.
2. Instead of returning the origin web server numeric IP address, DNS returns the numeric
IP address of the accelerator service on the application.
3. The browser requests the web page using the numeric IP address of the accelerator
service.
4. The accelerator service obtains the web page objects from the origin web server.
5. The accelerator returns copies of the objects to the browser.


19.Coming to Django server Url Navigation:

The process of navigating the request comes from the browser to a specific function
or a class which is responsible to render the response to the client is called as URL
navigation (URL mapping).
1.URL‘s.py is a file which is responsible for url navigation.
2.Based on the suffix of the url the mapping will be decided (or) the further navigation
will be decided.
3.Url‘s will map each and every url to a particular function or a class and this is called
URL mapping.

―Path‖ is a name of the function which is responsible for the url navigation(url
mapping).

Syntax:
path(„suffix/‟, address_function, name = mapping_name),

20.Design patterns:
It is the structure that decides where to keep what (it means in which file what
contains should be return what is the purpose of the file or folder).
A Design pattern is also called as ―Architect of the project‖.
Django was initially using MVC (Model View Controller) as its design pattern.
1. ―M‖ stands for Model. It is section of in structure that is the responsible working with
the database.

2.―V‖ stands for View. It is section which consists of business logic (python files and
instructions) which is responsible for the view rendering operation.

3.―C‖ stands for Controller. It is section which consists of the instructions responsible to
maintain the project or control the project.

4.The controller part is taken care by Django application itself.

#Note:
The Model-View-Template (MVT) is slightly different from MVC. In fact the main
difference between the two patterns is that Django itself takes care of the Controller part
(Software Code that controls the interactions between the Model and View), leaving us with
the template. The template is a HTML file mixed with Django Template Language (DTL).

20.How to open the django project in visual studio code:

By open the django project directly opening to the visual studio code.
1. Open visual studio code application in your system.
2. Click on file menu.
3. Click on open folder.
4. Select the path of the project folder and click on select folder button.
5. After doing the before step whatever you select project files will open into the
visual studio code application.

21.How to create view in your project:

1.A view is nothing but a function, or it is simply called a Python function that takes a
web request and returns a web response.

2.This response can be the HTML contents of a Web page, or a redirect, or a 404 error,
or an XML document, or an image, etc. Example: You use view to create web pages,
note that you need to associate a view to a URL to see it as a web page.


'''

