from django.shortcuts import render, HttpResponse
from translate import Translator
# Create your views here.

def home(request):
    if request.method == "POST":
        text = request.POST["translate"]
        language = request.POST["language"]
        translator = Translator(to_lang=language)
        translation = translator.translate(text)
        # Pass translation and original text/language to template for pronunciation
        return render(request, "index.html", {
            "translation": translation,
            "translated_text": translation,
            "language": language
        })
    return render(request, "index.html")