import speech_recognition as sr

def transcribe_audio(wav_file):
    # Crear un reconocedor de audio
    recognizer = sr.Recognizer()

    try:
        # Cargar el archivo de audio
        with sr.AudioFile(wav_file) as source:
            print("Cargando archivo de audio...")
            audio_data = recognizer.record(source)  # Lee todo el archivo de audio

        # Transcribir el audio a texto
        print("Transcribiendo el archivo de audio...")
        text = recognizer.recognize_google(audio_data, language='es-ES')  # Cambia 'es-ES' si el idioma no es español
        print("Transcripción completada:")
        return text

    except sr.UnknownValueError:
        return "No se pudo entender el audio."
    except sr.RequestError as e:
        return f"Error al conectar con el servicio de reconocimiento: {e}"

# Archivo WAV
wav_file_path = "grabacion.wav"
transcription = transcribe_audio(wav_file_path)

# Imprime la transcripción
print(transcription)
