from selenium import webdriver
from bs4 import BeautifulSoup
import time
from datetime import datetime
import playsound
from constants import *
import os
# import webbrowser

os.system("cls")

# chrome options
options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir="+PATH_TO_CHROME_PROFILE)     # chrome user data
options.add_argument("--profile-directory="+PROFILE_TYPE)           # directory should match with profile, e.g - default or profile 1
options.add_argument("--log-level=3")                               # only fatal errors reported
options.add_argument("--headless=new")                              # UNCOMMENT THIS FOR FIRST BOOT
driver = webdriver.Chrome(options)

# helper functions
def last_checked():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("Last time checked:", dt_string)
    
# global conditional
continue_to_wait = True

def launchBrowser():
    driver.get("https://app.prolific.com/studies")
    print("\n")
    print(f"Driver launched... waiting for page load ({WAIT_TIME}s)")
    time.sleep(WAIT_TIME)

    # omfg I somehow deleted this and could not figure out why it wasn't saving beyond the log in page..
    with open(PATH_TO_FOLDER+"/page_source.html", "w", encoding='utf-8') as f:
        f.write(driver.page_source)

    # beautiful soup 
    with open("page_source.html", "r", encoding='utf-8') as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        # print("Making da yummy soup")

    # print(soup.prettify())
    print("\n-------------------------------------")
    print("Searching for DIV")

    waiting_for_studies = soup.find_all("div", {"class" : "waiting-for-studies"})
    # waiting_for_study_list = soup.find_all("div", {"class" : "study-list"})  # actually don't think this one will work, go with falsy condition instead

    # don't think this sleep is necessary
    time.sleep(3.5)

    # parse the html 
    if waiting_for_studies:
        print("No studies to be found. :(")
        continue_to_wait = True
        return continue_to_wait
    elif not waiting_for_studies:
        print(f"{GREEN}There should be a study! Keep browser open! Press any enter when complete{ENDC}")
        
        # if by chance it doesn't open a browser -- you will know you got a study. shikanoko.mp3 is a 15s clip. blocks the thread for the duration.
        playsound.playsound(SOUND_ALERT)

        # attempt to pull the website up
        # driver.get will call the same driver and crash, perhaps just open it using the default web browser module and log in manually

        # if by chance it doesn't open a browser -- you will know you got a study. 

        input("Press any enter to EXIT BROWSER...")
        input("Press enter again key to CONFIRM EXIT... don't lose that survey!")
      
if __name__ == '__main__':
    while continue_to_wait:
        launchBrowser()
        print("Going to sleep for 2 mins... ")
        last_checked()
        print("-------------------------------------")
        time.sleep(120)



