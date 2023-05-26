from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from barcode import Code128
from barcode.writer import ImageWriter
from .models import Barcodefile
from .serializers import Barcodefileserializers
import csv
import pandas as pd
from fpdf import FPDF
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import (ListCreateAPIView, CreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http import HttpResponse

def index(request):
    domain = request.get_host()
    return HttpResponse("Hello World"+domain)

class barcodelistview(ListCreateAPIView):
    queryset = Barcodefile.objects.all()
    serializer_class = Barcodefileserializers

class barcodedeleteview(RetrieveUpdateDestroyAPIView):
    queryset = Barcodefile.objects.all()
    serializer_class = Barcodefileserializers


#server path
dot = '/var/www/tables/mysite/media/output/'
# dotpathinvidualbarcode = '/var/www/tables/mysite/media/barcode/'
#localpath
# dot = './media/output/'


from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from barcode import Code128
from barcode.writer import ImageWriter
from .models import Barcodefile
from .serializers import Barcodefileserializers
import csv
import pandas as pd
from fpdf import FPDF
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http import HttpResponse
import os

def index(request):
    domain = request.get_host()
    return HttpResponse("Hello World" + domain)

class barcodelistview(ListCreateAPIView):
    queryset = Barcodefile.objects.all()
    serializer_class = Barcodefileserializers

class barcodedeleteview(RetrieveUpdateDestroyAPIView):
    queryset = Barcodefile.objects.all()
    serializer_class = Barcodefileserializers

# dot = './media/output/'

# class barcodeapiView(ListCreateAPIView):
#     serializer_class = Barcodefileserializers
#     queryset = Barcodefile.objects.all()
#     def create(self, request):
#         numberdata = request.data.get('inputcsv')
#         try:
#             data = pd.read_csv(numberdata, nrows=10)
#             datanumbers = data['sku'].str.strip().values.tolist()
#             numbers = datanumbers
#             barcode_filenames = []

#             # Generate barcodes and save them
#             for number in numbers:
#                 # Create an object of Code128 class and pass the number with the ImageWriter() as the writer
#                 my_code = Code128(number, writer=ImageWriter())
#                 barcodefilename = dot + number + '.png'
#                 filename = dot + number 
#                 my_code.save(filename)

#                 pdf = FPDF()
#                 pdf.add_page()
#                 pdf.set_auto_page_break(auto=True, margin=15)

#                 # Add file name before the barcode image
#                 pdf.set_font("Arial", "B", 12)
#                 pdf.cell(0, 10, txt=number, ln=1, align="C")

#                 # Add the barcode image
#                 pdf.image(barcodefilename, x=pdf.w / 2 - 50, y=pdf.h / 2 - 50, w=100)

#                 # Save the PDF file
#                 #pdf_filename = dot + "barcodescenter-static.pdf"
#                 pdfformat = '.pdf'
#                 pdf_filename = dot + f"{number}{pdfformat}"
#                 # pdf_filename = f"{number}.pdf"
#                 pdf.output(pdf_filename)
#                 domain = request.get_host()
#                 ## not saving into database
#                 file_paths = '/media/output/'+ f"{number}{pdfformat}"
#                 file_url = f"http://{domain}{file_paths}"

#                 # Save the barcode data to the database
#                 chat = Barcodefile.objects.create(inputcsv=number, outputlink=file_url)
#                 serializer = Barcodefileserializers(chat)
#                 return Response(serializer.data)
#                 # barcode = Barcode(number=number)
#                 # barcode.save()


#         except Exception as e:
#             return Response(str(e), status=status.HTTP_400_BAD_REQUEST)



class barcodeapiView(ListCreateAPIView):
    serializer_class = Barcodefileserializers
    queryset = Barcodefile.objects.all()

    def create(self, request):
        
        numberdata = request.data.get('inputfile')
        print(numberdata)
        if not numberdata:
            numberdata = request.query_params.get('inputfile')
        try:
            data = pd.read_csv(numberdata)
            datanumbers = data['sku'].str.strip().values.tolist()
            numbers = datanumbers
            barcode_filenames = []

            # Generate barcodes and save them
            for number in numbers:
                number = number.replace("/", "@&&")
                # Create an object of Code128 class and pass the number with the ImageWriter() as the writer
                my_code = Code128(number, writer=ImageWriter())
                barcodefilename = dot + number + '.png'
                filename = dot + number
                my_code.save(filename)
                barcode_filenames.append(barcodefilename)

            # Create a PDF file and CSV file
            pdf = FPDF()
            csv_filename = dot + 'barcode_filenames.csv'

            # Loop through barcode filenames
            for barcode_filename in barcode_filenames:
                number = barcode_filename.split('/')[-1].split('.')[0]

                # Add a page to the PDF file
                pdf.add_page()
                pdf.set_auto_page_break(auto=True, margin=15)

                # Add file name before the barcode image
                pdf.set_font("Arial", "B", 12)
                pdf.cell(0, 10, txt=number, ln=1, align="C")

                # Add the barcode image
                pdf.image(barcode_filename, x=pdf.w / 2 - 50, y=pdf.h / 2 - 50, w=100)

            # Save the PDF file
            # pdf_filename = dot + 'barcodes.pdf'
            pdf_filename = dot + f"{number}" + '.pdf'
            pdf.output(pdf_filename)

            for barcode_filename in barcode_filenames:
                os.remove(barcode_filename)

            # Save the CSV file
            with open(csv_filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Barcode Filename'])
                writer.writerows([[filename] for filename in barcode_filenames])

            domain = request.get_host()
            file_paths = '/media/output/' + f"{number}" + '.pdf'
            file_url = f"http://{domain}{file_paths}"
            # csv_url = f"http://{domain}{numberdata}"
            # csv_url = f"http://{domain}"+int(numberdata)
            # csv_url = f"http://{domain}"+'/media/csv_files/'+f"{numberdata}"

            # Save the barcode data to the database
            chat = Barcodefile.objects.create(inputfile=numberdata, pdflink=file_url)
            serializer = Barcodefileserializers(chat)
            return Response(serializer.data)

        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)



class barcodefilelistview(ListCreateAPIView):
    queryset = Barcodefile.objects.all()
    serializer_class = Barcodefileserializers

class barcodefiledeleteview(RetrieveUpdateDestroyAPIView):
    queryset = Barcodefile.objects.all()
    serializer_class = Barcodefileserializers


# class barcodefileapiView(ListCreateAPIView):
class barcodefileapiView(CreateAPIView):
    serializer_class = Barcodefileserializers
    queryset = Barcodefile.objects.all()

    def create(self, request):
        
        numberdata = request.data.get('inputfile')
        # print(numberdata)
        if not numberdata:
            numberdata = request.query_params.get('inputfile')
        try:
            data = pd.read_csv(numberdata)
            datanumbers = data['sku'].str.strip().values.tolist()
            # numbers = datanumbers
            numbers = datanumbers
            # numbers = datanumbers.replace("/", "")
       
            barcode_filenames = []

            # Generate barcodes and save them
            for number in numbers:
                # number = number.replace("/", "")
                number = number.replace("/", "@&&")
                print(number)
                # Create an object of Code128 class and pass the number with the ImageWriter() as the writer
                my_code = Code128(number, writer=ImageWriter())
                barcodefilename = dot + number + '.png'
                filename = dot + number
                my_code.save(filename)
                barcode_filenames.append(barcodefilename)

            # Create a PDF file and CSV file
            pdf = FPDF()
            csv_filename = dot + 'barcode_filenames.csv'

            # Loop through barcode filenames
            for barcode_filename in barcode_filenames:
                number = barcode_filename.split('/')[-1].split('.')[0]

                # Add a page to the PDF file
                pdf.add_page()
                pdf.set_auto_page_break(auto=True, margin=15)

                # Add file name before the barcode image
                pdf.set_font("Arial", "B", 12)
                pdf.cell(0, 10, txt=number, ln=1, align="C")

                # Add the barcode image
                pdf.image(barcode_filename, x=pdf.w / 2 - 50, y=pdf.h / 2 - 50, w=100)

            # Save the PDF file
            # pdf_filename = dot + 'barcodes.pdf'
            pdf_filename = dot + f"{number}" + '.pdf'
            pdf.output(pdf_filename)
            for barcode_filename in barcode_filenames:
                os.remove(barcode_filename)

            # Save the CSV file
            with open(csv_filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Barcode Filename'])
                writer.writerows([[filename] for filename in barcode_filenames])

            domain = request.get_host()
            file_paths = '/media/output/' + f"{number}" + '.pdf'
            file_url = f"http://{domain}{file_paths}"
            data = {
            "inputlink": numberdata,
            "outputcsv": file_url,
            }
            return Response(data)
            

        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


