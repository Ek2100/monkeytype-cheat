# Auto Typing Bot for MonkeyType

This Python script serves as an automated bot for MonkeyType (https://monkeytype.com), a popular typing test website. The bot is designed to read words from a file named "words.txt," simulate typing while occasionally making typos, and type the words into the MonkeyType typing test.

## ⚠️ WARNING: Use at your own risk! ⚠️
### Please note that using this bot is against MonkeyType's terms of service, and it may result in consequences, such as getting your account banned or other actions taken against you. The author of this code is not responsible for any such consequences.

How to use:
1. Open inspect element in your Web-Browser.
2. Open MonkeyType (https://monkeytype.com) and click the keyboard icon in the top menubar to start a new test.
3. Locate the "words" div element on the website.
4. Copy the contents of the "words" div element, including the opening and closing tags, and paste it into a new file named "words.txt".
5. Save "words.txt" in the same directory as this Python script.
6. Make any desired changes to the configuration in this script (e.g., typo_chance, character_entry_time_min, character_entry_time_max, test_time).
7. Run the Python script. It will read the words from "words.txt," simulate typing with occasional typos, and type them into the typing test.
8. Sit back and watch the bot take the typing test for you! (Remember, using this bot is against MonkeyType's website's terms of service, so use it at your own risk).

### Note: The words.txt file currently contains a demo set of data from a test. You should change it for it work correctly

Configuration:
- typo_chance: Percentage chance of making a typo (default: 15%).
- character_entry_time_min: Minimum time delay between typing each character (default: 0.07 seconds).
- character_entry_time_max: Maximum time delay between typing each character (default: 0.13 seconds).
- test_time: The time duration for the typing test to run (default: 15 seconds).

### Remember to use this script responsibly and be aware of the risks involved when using automated bots on websites. The author provides this code for educational purposes and does not encourage or endorse any misuse.

## ⚠️ USE AT YOUR OWN RISK!! You have been warned. ⚠️
