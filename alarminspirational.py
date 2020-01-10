from os import listdir
import random
import pygame
import time
import schedule

def job():
    location = '/home/pi/inspirational/'
    list_of_files = listdir(location)
    list_length = len(list_of_files)
    choice = random.choice(list_of_files)
    print(list_of_files)
    print(choice)
    choicetweak =  '/home/pi/inspirational/' + choice
    print(choicetweak)


    pygame.init()
    pygame.mixer.init()

    pygame.mixer.music.load (choicetweak)
    pygame.mixer.music.play(0)

schedule.every().day.at("10:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)