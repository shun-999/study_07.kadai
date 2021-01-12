from googletrans import Translator
import eel
import desktop

app_name="web3"
end_point="index3.html"

@eel.expose
def translate(word, input_lang, output_lang):   
    tr = Translator()
    text = tr.translate(text=word, src=input_lang, dest=output_lang).text
    eel.translate_result(text)

desktop.start(app_name, end_point)