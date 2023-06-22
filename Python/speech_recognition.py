import speech_recognition as sr
import sys
language = 'en-US'
mic = sr.Microphone()
recognizer = sr.Recognizer()
while True:
    print("Say something...")

    if not sr.Microphone.list_microphone_names():
        print("No microphone detected. Please check your microphone connection.")
        sys.exit(0)

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language=language)
        print("You said: ", text)

        if "hello" in text.lower():
            print("hi there, How are you?")
        elif "how are you" in text.lower():
            print("I am good thank you")
        elif text.lower() in ["i am fine", "good"]:
            print("good")
        elif "nice to meet you" in text.lower():
            print("nice to meet you too")
        elif "close" in text.lower():
            sys.exit(0)

    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
