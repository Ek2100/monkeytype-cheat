# ------------------------------------------------------------------------------
# WARNING: USE AT YOUR OWN RISK
# ------------------------------------------------------------------------------
# © Copyright 2023
# ------------------------------------------------------------------------------
# DISCLAIMER: This bot is in violation of MonkeyType's terms of service. 
# Use it at your own risk! As the owner of this code, I am not responsible for
# any consequences that may arise from using this bot, including but not limited 
# to getting your account banned or any other actions taken against you.
# ------------------------------------------------------------------------------
# USE AT YOUR OWN RISK!! You have been warned.
# ------------------------------------------------------------------------------

import time
import random
from pynput.keyboard import Controller
from bs4 import BeautifulSoup

# ------------------------------------------------------------------------------
# How to use
# ------------------------------------------------------------------------------
# 1. Open inspect element in your Web-Browser
# 2. Open the MonkeyType (https://monkeytype.com) and click the keyboard icon in the top menubar to open a new test.
# 3. Locate the "words" div element on the website.
# 4. Copy the contents of the "words" div element, including the opening and closing
#    tags, and paste it into a new file named "words.txt".
# 5. Save "words.txt" in the same directory as this Python script.
# 6. Make any desired changes to the configuration in this script (e.g., typo_chance,
#    character_entry_time_min, character_entry_time_max, test_time).
# 7. Run this Python script (make sure to import all required imports) and quickly go back to MonkeyType and put your curser 
#    inside the textbox. It will read the words from "words.txt," simulate typing
#    while occasionally making typos to prevent detection, and type them into the typing test.
# 8. Sit back and watch the bot take the typing test for you! (Remember, using this
#    bot is against MonkeyType's website's terms of service, so use it at your own risk).
# ------------------------------------------------------------------------------
# CONFIGURATION (change if you want)
# ------------------------------------------------------------------------------
typo_chance = 15  # Percentage chance of making a typo (10% chance)
character_entry_time_min = 0.07  # Minimum time delay between typing each character (low amount, 0.05 seconds)
character_entry_time_max = 0.13  # Maximum time delay between typing each character (high amount, 0.09 seconds)
test_time = 15  # The time the typing test goes for (in seconds)
# ------------------------------------------------------------------------------
# END OF CONFIGURATION (dont change)
# ------------------------------------------------------------------------------



# ------------------------------------------------------------------------------
# Start Of Code
# ------------------------------------------------------------------------------

keyboard = Controller() 

def type_string_with_delay(string):
    start_time = time.time()  
    for character in string: 
        keyboard.type(character) 
        sleeptime = random.uniform(character_entry_time_min, character_entry_time_max)
        time.sleep(sleeptime)
        elapsed_time = time.time() - start_time 
        if elapsed_time > test_time:
            quit() 

with open('words.txt', 'r') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')

words_divs = soup.find_all('div', class_='word')
words = [div.get_text() for div in words_divs]

for i in range(len(words)):
    if random.randint(1, 100) <= typo_chance:  
        word = words[i]
        misspelled_word = ''.join(random.sample(word, len(word)))
        words[i] = misspelled_word

string_to_type = ' '.join(words)

time.sleep(2)
type_string_with_delay(string_to_type)



# ------------------------------------------------------------------------------
# WARNING: USE AT YOUR OWN RISK
# ------------------------------------------------------------------------------
# © Copyright 2023
# ------------------------------------------------------------------------------
# DISCLAIMER: This bot is in violation of MonkeyType's terms of service. 
# Use it at your own risk! As the owner of this code, I am not responsible for
# any consequences that may arise from using this bot, including but not limited 
# to getting your account banned or any other actions taken against you.
# ------------------------------------------------------------------------------
# USE AT YOUR OWN RISK!! You have been warned.
# ------------------------------------------------------------------------------
