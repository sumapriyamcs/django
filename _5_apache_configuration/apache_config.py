'''
1.Django Configuration with Apache Web Server:

Django uses its built-in development server to run the web application.
To start this server, we can use python manage.py runserver command.

This command starts the server which runs on port 8000 and can be accessed at
browser by entering localhost:8000. It shows a welcome page of the application.

But if we want to run our application by using apache server rather than built-in
development server, we need to configure apache2.conf file located at /etc/apache directory.

/ apache2.conf

WSGIScriptAlias / /var/www/html/django7/django7/wsgi.py
WSGIPythonPath /var/www/html/django7/

<Directory /var/www/html/django7>
   <Files wsgi.py>
                Require all granted
   </Files>
</Directory>

After adding these lines, restart apache server by using the service apache2
restart command and then type localhost to the browser's address bar.
This time, project will run on apache server rather than a built-in server.

we should type localhost in link place while running the server.



'''