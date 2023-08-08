import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import os

audio = sr.Recognizer()
maquina = pyttsx3.init()
y = 0
voice = maquina.getProperty('voices') #get the available voices
    # eng.setProperty('voice', voice[0].id) #set the voice to index 0 for male voice
maquina.setProperty('voice', voice[1].id) #changing voice to index 1 for female voice
def executa_comandoi():
    try:
        with sr.Microphone() as source:
            maquina.say('estou ouvindo')
            maquina.runAndWait()
            print('Ouvindo..')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            print(comando)
            if 'neuro' in comando:
                comando = comando.replace('neuro', '')
                maquina.say(comando)
                maquina.runAndWait()
            else :
                executa_comando()

    except:
        print('Microfone não está ok')
        maquina.say('não estou ouvindo')
        maquina.runAndWait()
        executa_comando()

    return comando
def executa_comando():
    try:
        with sr.Microphone() as source:
            maquina.say('estou ouvindo')
            maquina.runAndWait()
            print('Ouvindo..')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'neuro' in comando:
                comando = comando.replace('neuro', '')
                maquina.say(comando)
                maquina.runAndWait()
            else :
                executa_comandoi()

    except:
        print('Microfone não está ok')
        maquina.say('não estou ouvindo')
        maquina.runAndWait()
        executa_comandoi()
    return comando

def comando_voz_usuario():
    comando = executa_comando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são' + hora)
        maquina.runAndWait()
    elif 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'toque' in comando:
        musica = comando.replace('toque','')
        resultado = pywhatkit.playonyt(musica)
        maquina.say('Tocando música')
        maquina.runAndWait()
    elif 'sair' in comando:
        maquina.say('estou saindo')
        os.system('exit' if os.name == 'nt' else 'quit')
        maquina.runAndWait()
    elif 'caneca' in comando:
        os.system('start cup.bat')
        maquina.say('abrindo cuphead')
        maquina.runAndWait()
    else :
        executa_comando()


comando_voz_usuario()
while y == 0 :
    executa_comando()
    comando_voz_usuario()