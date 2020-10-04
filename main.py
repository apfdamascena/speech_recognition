from os import listdir
from os.path import isfile, join
from pprint import pprint
import time, json, requests
import speech_recognition as sr

def main():
    dir_path = join("audios", "bed")

    rec = sr.Recognizer()  # use this only for the process_google and process_sphinx functions
    all_files = [file_name for file_name in listdir(dir_path) 
                if  isfile(join(dir_path, file_name)) 
                    and file_name.endswith('.wav')]
    
    processes = [
        {"name": "WIT.AI RECOGNIZER", "function": process_wit}, 
        {"name": "GOOGLE RECOGNIZER", "function": process_google}, 
        {"name": "SPHINX RECOGNIZER", "function": process_sphinx}
    ]

    for process in processes:
        print("\n", process["name"])

        start = time.time()
        all_files_processed = [
            process["function"](file_name, dir_path, rec) 
            for file_name in all_files
        ]
        end = time.time()

        generates_report(start. end. all_files_processed)

def generates_report(start, end, all_files_processed):
    '''
    Shows the runtime and the percentage of WDU/bed
    '''
    pprint(all_files_processed)
    print("runtime:", time_min(start, end))
    print("percentage of \"WDU\":", 
        accuracy("WDU", all_files_processed))
    print("percentage of \"bed\":", 
        accuracy("bed", all_files_processed))

"""this process is still basic, but I tried to look for possible errors like the environment 
in which the audio is recorded.
I created 3 different types of processes to analyze, from a txt file, which would be the most viable to use.
"""

def read_audio(file_path, file_name):
    """
    Returns the audio of a given file.
    Params
        file_path: file directory string
        file_name: file name string
    Returns
        audio as byte string
    """
    with open(join(file_path, file_name), 'rb') as source:
        audio = source.read()
    return audio


def process_google(file_name, file_path, recognizer):
    """
    Read and transcribe a audio file using Google recognizer
    Params
        file_name: file name string
        recognizer: file name string
        file_path: file directory string
    Returns
        result text or WDU if unrecognizable
    """
    with sr.AudioFile(join(file_path, file_name)) as data:
        recognizer.adjust_for_ambient_noise(data, duration=0.40)
        audio = recognizer.record(data)
        try:
            return recognizer.recognize_google(audio)
        except:
            return "WDU"

def process_sphinx(file_name, file_path, recognizer):
    """
    Read and transcribe a audio file using Sphinx recognizer
    Params
        file_name: file name string
        recognizer: file name string
        file_path: file directory string
    Returns
        result text or WDU if unrecognizable
    """
    with sr.AudioFile(join(file_path, file_name)) as data:
        recognizer.adjust_for_ambient_noise(data, duration=0.40)
        audio = recognizer.record(data)
        try:
            return recognizer.recognize_sphinx(audio)
        except:
            return "WDU"

def process_wit(file_name, file_path, recognizer = None):
    """
    Read and transcribe a audio file using WIT recognizer
    Params
        file_name: file name string
        recognizer: file name string
        file_path: file directory string
    Returns
        result text or WDU if unrecognizable
    """
    wit_access_token = "3IQLXQY4VVE5MQQ77HO6JKZ5T24KO7FK"
    endpoint = "https://api.wit.ai/speech"

    audio = read_audio(file_path, file_name)
    headers = {'Authorization': 'Bearer ' + wit_access_token,
               'Content-Type': 'audio/wav'}
    post_request = requests.post(endpoint, data=audio, headers=headers)
    data = json.loads(post_request.content)
    return data['_text']


"""this process is just to get an idea about the efficiency of the recognizers. The errors can be divided into: 
1) the audio is really unrecognizable
2) fails in the recognizer"""

def time_min(start, end):
    """ 
    Compare the time between recognizers, emphasizing efficiency.
    """
    return (end - start) / 60.0

def accuracy(word, struct):
    '''
    Calculates the percentage of correct answers on a given word.
    Params
        word: answer string
        struct: attempt list
    Returns
        percentage float
    '''
    size = len(struct)
    number_word = struct.count(word)
    return (number_word * 100) / size

if __name__ == '__main__':
    main()
