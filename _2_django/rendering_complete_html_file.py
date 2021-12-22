'''
The process of rendering the complete html file:
Steps:
1. Create a html file inside a project, type your html data in that file.
2. Read the html file and returns it as a response.

if the project is system to system the path will be keep of changing and every time cannot sort
and correcting the path so instead of we creating path we are go to generating the path
dynamically using ―OS‖ module.
Step:
1. To use ―OS‖ module first we need to import it using the statement.
Syntax:
import os
2. Some of the functions use in that are:
__file__: is variable that gives the path of the where it is present (current file).
a) os.path.abspath(file) (absolute path)
This is a function that gives the absolute path
Example:
FILE_PRO = os.path.abspath(__file__)
b) os.path.dirname(absolute path)
This is a function that path of parent directory by eliminating the child from abs path
Example:
DIR_PRO = os.path.dirname(FILE_PRO)
c) os.path.join(path1, path2)
This is functions which is joining the directory file and add the new file.
Example:
FILE_PATH = os.path.join(DIR_PRO,‖sample.html‖)


'''