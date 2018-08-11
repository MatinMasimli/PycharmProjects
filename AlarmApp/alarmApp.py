from os import listdir
from os.path import isfile, join
from time import strftime, localtime
from datetime import datetime
import os, pygame, sched, time, webbrowser, timeit

def setAlarmTime():
    start = time.time()
    print('CURRENT TIME:', time.ctime(start))
    alarmTime = int(input("Set an alarm time with seconds: "))

    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(alarmTime, 1, play_song)
    scheduler.run()

def play_song():

    if localtime().tm_hour < 15:
        controller = webbrowser.get()
        controller.open("https://www.youtube.com/watch?v=CoyzywqGXKw")
    else:
        pwd = ""
        onlyfiles = goToDir(pwd)
        print(strftime("%H:%M:%S", localtime()))

        for file in onlyfiles:
            if file.endswith('.mp3'):
                pygame.init()
                pygame.mixer.init()
                pygame.mixer.music.load(file)
                pygame.mixer.music.play()

                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
        #            print(strftime("%H:%M:%S", localtime()))

def goToDir(pwd):
    # this will change directory to pwd path.
    os.chdir(pwd)

    # print your current working directory
    os.getcwd()

    # print all files in that location
    onlyfiles = [f for f in listdir(pwd) if isfile(join(pwd, f))]
    return onlyfiles


startTime = datetime.now()
setAlarmTime()
print("endTime: " + str(datetime.now() - startTime))



