from googletrans import Translator


tr = Translator()
word = input("Enter text >>")
text = tr.translate(text=word, src="en", dest="ja").text
print(text)