'''
1.Django with Bootstrap:

Bootstrap is a framework which is used to create user interface in web applications.
It provides css, js and other tools that help to create required interface.

In Django, we can use bootstrap to create more user friendly applications.

To implement bootstrap, we need to follow the following steps.

1. Download the Bootstrap:

Visit the official site https://getbootstrap.com to download the bootstrap
at local machine. It is a zip file, extract it and see it contains the two folder.

2. Create a Directory

Create a directory with the name static inside the created app and place
the css and jss folders inside it. These folders contain numerous files.

3. Create a Template

First create a templates folder inside the app then create a index.html file
to implement (link) the bootstrap css and js files.

4. Load the Boostrap:

load the bootstrap files resides into the static folder. Use the following code.

{% load staticfiles %}

And link the files by providing the file location (source). See the index.html file.

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    {% load staticfiles %}
    <link href="{% static 'css/bootstrap.min.css' %}" >
    <script src="{% static 'bootstrap.min.js' %}"></script>
    <script>alert();</script>
</head>
<body>
</body>
</html>

In this template, we have link two files one is bootstrap.min.css and second
is bootstrap.min.js. Lets see how to use them in application.

Suppose, if we don't use bootstrap, our html login for looks like this:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>login</title>
</head>
<body>
 <form action="/save" method="post">
  <div class="form-group">
    <label for="email">Email address:</label>
    <input type="email" class="form-control" id="email">
  </div>
  <div class="form-group">
    <label for="pwd">Password:</label>
    <input type="password" class="form-control" id="pwd">
  </div>
  <div class="checkbox">
    <label><input type="checkbox"> Remember me</label>
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
</body>
</html>

5.After loading bootstrap files. Our code look like this:

// index.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>login</title>
    {% load staticfiles %}
    <link href="{% static 'css/bootstrap.min.css' %}" rel="stylesheet">
    <script src="{% static 'js/bootstrap.min.js' %}"></script>
</head>
<body>
 <form action="/save" method="post">
  <div class="form-group">
    <label for="email">Email address:</label>
    <input type="email" class="form-control" id="email">
  </div>
  <div class="form-group">
    <label for="pwd">Password:</label>
    <input type="password" class="form-control" id="pwd">
  </div>
  <div class="checkbox">
    <label><input type="checkbox"> Remember me</label>
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
</body>
</html>

now, our login form loos much nicer. This is advantage of bootstrap.

'''