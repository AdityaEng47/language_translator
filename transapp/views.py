from django.shortcuts import render
from translate import Translator
import os
import gtts  

def index(request):
    return render(request, 'index.html')

def con_btn(request):
    return render(request, 'index2.html')

def trans_btn(request):
    if request.method == "POST":
        text = request.POST['text']
        srclang = request.POST['srclanguage']
        destlang = request.POST['destlanguage']
        translator = Translator(to_lang=destlang, from_lang=srclang)
        translation = translator.translate(text)
        context = {'translated_text': translation}
        return render(request, 'txt_opt.html', context)

def again_btn(request):
    return render(request, 'trans.html')

def t_to_t(request):
    return render(request, 'txt_to_txt.html')

def v_to_v(request):
    return render(request, 'voice_to_voice.html')

def trans_btn2(txt, srclang, destlang):
    text = txt
    src_lang = srclang
    dest_lang = destlang
    translator = Translator(to_lang=dest_lang, from_lang=src_lang)
    translation = translator.translate(text)
    return translation

def voice_recog(request):
    if request.method == "POST":
        text = request.POST['text']
        srclang = request.POST['srclanguage']
        destlang = request.POST['destlanguage']

        translation = trans_btn2(text, srclang, destlang)
        converted_audio = gtts.gTTS(text=translation, lang=destlang, slow=False)
        audio_file_path = os.path.join('static/audio/', 'audio.mp3')
        converted_audio.save(audio_file_path)
        
        play_dict = {
            'audio': converted_audio.save(audio_file_path),
            'text':translation,
        }


    return render(request, "voice_opt.html", context = play_dict) 

def again_btn1(request):
    return render(request, 'voice_opt.html')

