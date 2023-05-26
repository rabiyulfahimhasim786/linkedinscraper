# from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404
# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World!")


# def index(request):
    # return HttpResponse("Hello World!")

#restframework imports
from .models import Spellchecker
from .serializers import Spellcheckerserializers
from rest_framework.views import APIView
from rest_framework import status, serializers
from rest_framework.generics import (ListCreateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

#importing gingerit library, importing multi threads using concurrent features 
# import concurrent.futures
# from gingerit.gingerit import GingerIt

# import concurrent.futures
# from gingerit.gingerit import GingerIt
#pyaspeller documentation - https://pypi.org/project/pyaspeller/
#importing gingerit, language tool and pyaspeller library, importing multi threads using concurrent features 
from pyaspeller import YandexSpeller
import language_tool_python
def errorcorrecting(text):
    tool = language_tool_python.LanguageTool('en-US')  # use a local server
    #tool = language_tool_python.LanguageToolPublicAPI('en-US') # or use public API
    datasets = tool.correct(text)
    return datasets

# pip install pyaspeller
def errocorrectpyspeller(sampletext):
    speller = YandexSpeller()
    fixed = speller.spelled(sampletext)
    return fixed
    
# def process_chunk(chunk):
#     parser = GingerIt()
#     result = parser.parse(chunk)
#     return result


# def process_large_text(text):
#     chunks = text.split('\n')  # Splitting by newlines assuming paragraphs
    
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         # Process the chunks concurrently using threads
#         results = executor.map(process_chunk, chunks)
#     resulttext =[]
#     for result in results:
#         corrected_text = result['text']
#         corrections = result['result']
#         corrections_count = result['corrections']
        
#         # Process the results as per your requirements
#         print("Corrected Text:", corrected_text)
#         print("Corrections:", corrections)
#         print("Corrections Count:", corrections_count)
#         print()
#         resulttext.append(corrected_text)
#         error_corrected_text = ' '.join(corrected_text)
#     # return corrected_text, corrections, corrections_count
#     return error_corrected_text

# def process_large_text(text):
#     chunks = text.split('\n')  # Splitting by newlines assuming paragraphs

#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         # Process the chunks concurrently using threads
#         results = executor.map(process_chunk, chunks)
#     corrected_text = []
#     for result in results:
#         corrected_text.append(result['text'])
#     corrected_text = '\n'.join(corrected_text)
#     return corrected_text

# def process_chunk(chunk):
#     # parser = GingerIt()
#     parser = GingerIt(context_window=5)
#     result = parser.parse(chunk)
#     return result['text']

# def process_large_text(text):
#     chunks = text.split('\n')  # Splitting by newlines assuming paragraphs

#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         # Process the chunks concurrently using threads
#         results = executor.map(process_chunk, chunks)

#     corrected_text = '\n'.join(results)

#     return corrected_text

class SpellcheckListview(ListCreateAPIView):
    queryset = Spellchecker.objects.all()
    serializer_class = Spellcheckerserializers

    def post(self, request):
        input_text = request.data.get('inputtext')
        if not input_text:
            input_text = request.queryparams.get('inputtext')
        output_data = errorcorrecting(input_text)
        print(output_data)
        # output_text =  process_large_text(output_data)
        output_text = errocorrectpyspeller(output_data)
        # output_text = errocorrectpyspeller(input_text)
        print(output_text)
        print(output_text)
        spellcheckerapi = Spellchecker.objects.create(inputtext=input_text, outputtext=output_text)
        serializers = Spellcheckerserializers(spellcheckerapi)
        return Response(serializers.data)


class SpellcheckDeleteview(RetrieveUpdateDestroyAPIView):
    queryset = Spellchecker.objects.all()
    serializer_class = Spellcheckerserializers