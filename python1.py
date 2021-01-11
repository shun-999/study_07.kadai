from googletrans import Translator
import eel
import desktop

app_name="web"
end_point="index.html"

@eel.expose
def translate(word):   
    tr = Translator()
    text = tr.translate(text=word, src="en", dest="ja").text
    eel.translate_result(text)

desktop.start(app_name, end_point)