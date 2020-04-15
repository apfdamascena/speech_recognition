from os import listdir
from os.path import isfile, join
import time
import speech_recognition as sr

"""list comprehension was used in main() because later it would be necessary to use another "for" loop to iterate all 
names. So, I decided to do everything in the list comprehension. """


def main():
    my_path = "/Users/alexdamascena/Desktop/speech/audios/phrase"
    rec = sr.Recognizer()
    start = time.time()
    all_files_processed = [process_google(file, rec, my_path) for file in listdir(my_path) if
                           isfile(join(my_path, file)) and file[len(file) - 1] == 'v']
    end = time.time()

    print(all_files_processed)
    print(accuracy(all_files_processed))
    print(time_min(start, end))
    print(percentage_word("bed", all_files_processed))


"""this process is still basic, but I tried to look for possible errors like the environment 
in which the audio is recorded.

I created 3 different types of processes to analyze, from a txt file, which would be the most viable to use.
"""


def process_google(file_name, recognizer, my_path):
    with sr.AudioFile(my_path + "/" + file_name) as data:
        recognizer.adjust_for_ambient_noise(data, duration=0.40)
        audio = recognizer.record(data)
        try:
            return recognizer.recognize_google(audio)
        except:
            return "WDU"


def process_sphinx(file_name, recognizer, my_path):
    with sr.AudioFile(my_path + "/" + file_name) as data:
        recognizer.adjust_for_ambient_noise(data, duration=0.40)
        audio = recognizer.record(data)
        try:
            return recognizer.recognize_sphinx(audio)
        except:
            return "WDU"


def process_ibm(file_name, recognizer, my_path):
    with sr.AudioFile(my_path + "/" + file_name) as data:
        recognizer.adjust_for_ambient_noise(data, duration=0.40)
        audio = recognizer.record(data)
        try:
            return recognizer.recognize_sphinx(audio)
        except:
            return "WDU"


"""this process is just to get an idea about the efficiency of the recognizers. The errors can be divided into: 
1) the audio is really unrecognizable
2) fails in the recognizer"""


def accuracy(all_files_processed):
    size = len(all_files_processed)
    quantity_wdn = all_files_processed.count("WDU")
    return 100 - (quantity_wdn * 100) / size


"""this function will help us to compare the time between recognizers, emphasizing efficiency."""


def time_min(start, end):
    return (end - start) / 60.0


def percentage_word(word, struct):
    size = len(struct)
    number_word = struct.count(word)
    return (number_word * 100) / size


if __name__ == '__main__':
    main()
