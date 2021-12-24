'''
1.Django PDF:

Here, we will learn how to design and generate PDF file using Django view.
To generate PDF, we will use ReportLab Python PDF library that creates customized dynamic PDF.

It is an open source library and can be downloaded easily by using the following command in Ubuntu.

$ pip install reportlab

After installing, we can import it by import keyword in the view file.

Below is a simple PDF example, in which we are outputting a string message
"Hello form javatpoint". This library provides a canvas and tools that are used
to generate customized PDF.

// views.py

from reportlab.pdfgen import canvas
from django.http import HttpResponse

def getpdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'
    p = canvas.Canvas(response)
    p.setFont("Times-Roman", 55)
    p.drawString(100,700, "Hello, Javatpoint.")
    p.showPage()
    p.save()
    return response

First, provide MIME (content) type as application/pdf, so that output
generates as PDF rather than HTML,

Set Content-Disposition in which provide header as attachment and output file name.

Pass response argument to the canvas and drawstring to write the string
after that apply to the save() method and return response.

// urls.py

path('pdf',views.getpdf)

Set the above code in urls.py to call view function.
Run server and access this view on the browser that creates a pdf file.

A PDF file is generated and ready to download. Download the file and open it,
it shows the string message that we wrote.
Apart from it, this library contains the lots of other methods to design
and generate PDF dynamically.


Run server and access this view on the browser that creates a pdf file.

'''