import speech_recognition as sr 
r = sr.Recognizer()
with sr.Microphone() as source:
	print('Bienvenido. Por favor di algo.')
	audio = r.listen(source)

	try:
		text = r.recognize_google(audio, language='es-ES')
		print('Has dicho: {}'.format(text))
	except:
		print('Lo lamento, no he entendido.')



