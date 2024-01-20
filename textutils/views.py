
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def analyze(request):
   
    djtext =  request.GET.get ('text','off')
    removepunc =  request.GET.get ('removepunc','off')
    fullcaps =  request.GET.get ('fullcaps','off')
    lower =  request.GET.get ('lower','off')
    newlineremover =  request.GET.get ('newlineremover','off')
    spaceremover =  request.GET.get ('spaceremover','off')
    charactercounter =  request.GET.get ('charactercounter','off')

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed+=char


        params = {'purpose':'Remove Punctutations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

# For Upper Case
    elif(fullcaps=='on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed+char.upper()
        params = {'purpose':'Change to UpperCase','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    
# For Lower Case
    elif(lower == 'on'):
        analyzed=""
        for char in djtext:
            analyzed = analyzed+char.lower()
        params = {'purpose':'Change to LowerCase','analyzed_text':analyzed}
        return render (request,'analyze.html',params)


# for New Line Remover
    elif(newlineremover == 'on'):
        analyzed=""
        for char in djtext:
            if char !='\n':
                analyzed = analyzed+char
        params = {'purpose':'Remove New Line ','analyzed_text':analyzed}
        return render (request,'analyze.html',params)


# for Space Remover
    elif(spaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

        # Analyze the text
        return render(request, 'analyze.html', params)
    
    
# for Counting the characters
    elif charactercounter == "on":
        analyzed = len(djtext)

        params = {'purpose': 'Count Number of Characters', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)