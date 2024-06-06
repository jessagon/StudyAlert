# StudyAlert
A simple Python cli application that will send you alerts when studies are available from research platforms (Prolific, Cloud Connect). StudyAlert uses the Selenium Webdriver and BeautifulSoup4 to find and parse the relative html.

StudyAlert currently only features sound notifications through the playsound module (.wav/.mp3 support) and initially comes with a 15s sound notification. You can change this to anything else by replacing the .mp3. 

I plan on adding plenty more features down the line, so stay tuned for that.

---

### Features 
+ Non intrusive scraping (checks every 2-3 minutes). :hourglass_flowing_sand:
+ Sound alerts :loud_sound:
+ Prolific support :white_check_mark:
+ Chrome support 

### Todo
+ Selenium cookies (properly store session)
+ Phone notifications
+ Cloud Connect support
+ Logging system
+ Other browser support (firefox/edge)

---

### How to Install

1) Create a venv. `python -m venv /path/to/new/virtual/environment`

2) Change directory into the scripts folder and activate the venv.
   
      a) `cd scripts` <br>
      b) `activate`

3) Return back to the root directory and install requirements.txt. `pip install -r requirements.txt`

4) You are now able to run main.py. Don't do it though.

You must configure some additional parameters before using the program. 

---

### Additional Setup 

1. Open constants.py.

You should see the following:
```
PATH_TO_FOLDER = ""
PATH_TO_CHROME_PROFILE ="" 
PROFILE_TYPE = ""       
WAIT_TIME = 35 # seconds
SOUND_ALERT = "Shikanokonokonokokoshitantan.mp3"
```

`PATH_TO_FOLDER` needs to be set to the StudyAlert root folder. You should currently be in it.
You can find the information for `PATH_TO_CHROME_PROFILE` opening a Chrome tab and entering `chrome://version/` in the search bar and pressing enter.

The profile path by default should end in `Default` if you have no other Chrome profiles. I **HIGHLY RECOMMEND** you to make an additional Chrome profile, logging into Prolific and storing your log in creditials with the new profile. **Continued in How to Use section** 

If you followed my advice, and checked the profile path of your new profile, it should end in `Profile 1`, despite it being the second profile. **This is far more likely to work and give less problems.** 

`PROFILE_TYPE` will be the last part of your path, so in most cases `Default` or `Profile 1`, etc.

`WAIT_TIME ` and `SOUND_ALERT` can be adjusted as needed. By default I've given it a large amount of time to ensure the page loads for varying connection speeds. It will also account for service interruptions out of your control and will guarantee a better long term experience over speeding it up.

---
  
### How to Use

1. Open main.py in an editor of your choice. 
2. Head to line 17, where all of the chrome options are located and comment out the `options.add_argument("--headless=new")`
Selenium doesn't store your session natively, so we have to populate it manually the first time, and in order to do that we need to turn off the headless feature initially.
3. Run main.py `python main.py`
4. You should see the Prolific website log in pop up. Ensure you're on the right profile and log in.
5. Once successful, terminate the program (ctrl+c) and exit the chrome browser.
6. Run main.py again to check to see if the program will automatically store your session. 
7. If successful, uncomment the `options.add_argument("--headless=new")`
8. StudyAlert is now set up for use.

Unfortunately this information doesn't persist the once the computer has been restarted, so until I add proper session management you'll have to do this at least once per day.

---

### Troubleshooting / Known Issues: 

+ Chromedriver might not always be shut down from a previous termination.
run `taskkill /f /im chrome.exe` and try again.
