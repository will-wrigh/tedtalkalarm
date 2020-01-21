import schedule
import subprocess
import datetime

def job():
    print("voice assistant ready")
    day_of_week = datetime.datetime.now().strftime("%A")
    day_of_week_number = datetime.datetime.now().strftime("%w")
    day_of_week_number = int(day_of_week_number)

    print(day_of_week)
    print(day_of_week_number)

    #days of week, number of classes, time of first class
    List1 = [[0, 1, 2, 3, 4, 5, 6], [0, 3, 1, 2, 1, 1, 0], ["zero", "one", "eleven thirty", "one", "eleven thirty", "one", "zero"]]

    number_of_classes = str(List1[1][day_of_week_number])
    print(number_of_classes)

    if number_of_classes == "0":
        text = "Good Morning Will. The day is " + day_of_week + ". You have " + number_of_classes + " classes today. Enjoy your weekend."
        print(text)
    else:
        text = "Good Morning Will. The day is " + day_of_week + ". You have " + number_of_classes + " classes today, the first starting at " + List1[2][day_of_week_number] + "."
        print(text)

    subprocess.call('echo '+text+'|festival --tts', shell=True)

schedule.every().day.at("09:00").do(job)

job()