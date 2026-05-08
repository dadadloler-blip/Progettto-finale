import sounddevice as sd
import random
import time
import scipy.io.wavfile as wav
import speech_recognition as sr
from deep_translator import GoogleTranslator
import asyncio

async def gioco_traduzione_2():
  
    traduttore = GoogleTranslator(source='it', target='en')
    
    livelli = {
        1: ["cane", "gatto", "casa", "albero", "libro"],
        2: ["bicicletta", "macchina", "finestra", "scuola", "telefono"],
        3: ["crepuscolo", "biblioteca", "astronave", "giungla", "arcobaleno"],
        4: ["Ciclopentanoperidrofenantrene", "Elettroneuroencefalografista", "Psiconeuroendocrinoimmunologia", "Incommensurabilmente"]
    }

    print(" BENVENUTO NEL MIO GIOCO DI TRADUZIONE 📎")
    print("Scegli un livello di difficoltà:")
    print("1: facile", "2: medio", "3: difficile", "4: ☠️")
    
    try:
        livello = int(input("Inserisci il livello: "))
    except ValueError:
        print("Inserisci un numero valido!")
        return

    if livello in livelli:
        parola_data = random.choice(livelli[livello])
        print(f"\nHai scelto il livello: {livello}")
        print(f"Come si traduce in inglese la parola: {parola_data.upper()}?")
        
 
        traduzione_corretta = traduttore.translate(parola_data).lower().strip()

        input("\nPremi INVIO quando sei pronto a parlare...")
        print("3, 2, 1, PARLA!")
        
        fs = 44100 
        secondi = 5 
        registrazione = sd.rec(int(secondi * fs), samplerate=fs, channels=1, dtype='int16')
        sd.wait()
        wav.write("output.wav", fs, registrazione)
        
        print("Registrazione completata!")

    
        r = sr.Recognizer()
        with sr.AudioFile("output.wav") as source:
            audio = r.record(source)
        
        try:
            parola_detta = r.recognize_google(audio, language="en-US").lower().strip()
            print(f"Tu hai detto: {parola_detta}")

            if parola_detta == traduzione_corretta:
                print("✅ Esatto!")
            else:
                print(f"❌La traduzione era: {traduzione_corretta}")
        
        except sr.UnknownValueError:
            print("Non ho capito cosa hai detto.")
        except sr.RequestError:
            print("Errore di connesione")
            
    else:
        print("Livello non valido!")

if __name__ == "__main__":
    asyncio.run(gioco_traduzione_2())
