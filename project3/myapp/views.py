from django.http import HttpResponse
import os
file_path=os.path.abspath(__file__)
pro_dir_path=path=os.path.dirname(file_path)
dir_path=os.path.dirname(pro_dir_path)

def html_respo(request):
    file_addr=os.path.join(dir_path,"sample.html")
    fp=open(file_addr,"r")
    data=fp.need()
    return httpresponse(data)
