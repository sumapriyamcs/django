'''
1.Django Deployment to Github:

Github is a global repository system which is used for version control.
While working with django, if there is need for version management,
it is recommended to use github.

In this tutorial, we will create and deploy a django project to the github
so that it can be accessible globally.

Before deploying, it is required to have a github account, otherwise create
an account first by visiting github.com.

Open the terminal and cd into the project, we want to deploy. For example,
our project name is djangoboot. Then

2.Install Git:

we use the following command to install git on our location machine.

$ apt-get install git

3.Initialize Git:

Use the following command to start the git.

$ git init

Provide global user name email for the project, it is only once,
we don?t need to provide it repeatedly.

4.Create File:

Create a file .gitignore inside the root folder of django project. And put the following code inside it.

// .gitignore
*.pyc
*~
__pycache__
myvenv
db.sqlite3
/static
.DS_Store

5.Git Status:

Check the git status by using the following command. It provides some detail to the screen.

$ git status

After saving, now execute the following command.

$ git add -all

$ git commit -m "my app first commit"

6.Push to Github:

First login into the git account and create a new repository and initialize with README.

My repository name is my-django-app. Click on the create repository button.
Now repository has created.

On next page, click on the clone button and copy the http url. In my case,
it is https://github.com/irfan003/my-django-app.git
https://github.com/sumapriyamcs/django

Now, use this url with the following command.

$ git remote add origin https://github.com/irfan003/my-django-app.git
https://github.com/sumapriyamcs/django

$ git push -u --force origin master

provide username and password of git account. It will start pushing project
to the repository. We can verify it.


'''