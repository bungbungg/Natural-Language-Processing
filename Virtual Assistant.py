{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "initializing tiwi\n",
      "speak...\n",
      "You : find locate\n",
      "\n",
      "speak...\n",
      "You : find location\n",
      "\n",
      "speak...\n",
      "Say that again please\n",
      "speak...\n",
      "You : YouTube\n",
      "\n",
      "speak...\n",
      "You : open YouTube\n",
      "\n",
      "Done!\n",
      "speak...\n",
      "You : open Google\n",
      "\n",
      "Done!\n",
      "speak...\n",
      "You : play this is all we know\n",
      "\n",
      "speak...\n",
      "Say that again please\n",
      "speak...\n",
      "Say that again please\n",
      "speak...\n",
      "You : tell me about Asia\n",
      "\n"
     ]
    },
    {
     "ename": "PageError",
     "evalue": "Page id \"as8a\" does not match any pages. Try another id!",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mPageError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-8ae97dbabe4b>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m    110\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    111\u001b[0m \u001b[1;32mwhile\u001b[0m \u001b[1;32mTrue\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 112\u001b[1;33m     \u001b[0massistant\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmyCommand\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m<ipython-input-1-8ae97dbabe4b>\u001b[0m in \u001b[0;36massistant\u001b[1;34m(command)\u001b[0m\n\u001b[0;32m     94\u001b[0m     \u001b[1;32melif\u001b[0m \u001b[1;34m'tell me about'\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mcommand\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     95\u001b[0m         \u001b[0mwiki\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mcommand\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mreplace\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'tell me about'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m''\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 96\u001b[1;33m         \u001b[0minfo\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mwikipedia\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msummary\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mwiki\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m3\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     97\u001b[0m         \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0minfo\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     98\u001b[0m         \u001b[0mspeak\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0minfo\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\wikipedia\\util.py\u001b[0m in \u001b[0;36m__call__\u001b[1;34m(self, *args, **kwargs)\u001b[0m\n\u001b[0;32m     26\u001b[0m       \u001b[0mret\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_cache\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     27\u001b[0m     \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 28\u001b[1;33m       \u001b[0mret\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_cache\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfn\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     29\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     30\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0mret\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\wikipedia\\wikipedia.py\u001b[0m in \u001b[0;36msummary\u001b[1;34m(title, sentences, chars, auto_suggest, redirect)\u001b[0m\n\u001b[0;32m    229\u001b[0m   \u001b[1;31m# use auto_suggest and redirect to get the correct article\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    230\u001b[0m   \u001b[1;31m# also, use page's error checking to raise DisambiguationError if necessary\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 231\u001b[1;33m   \u001b[0mpage_info\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpage\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtitle\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mauto_suggest\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mauto_suggest\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mredirect\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mredirect\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    232\u001b[0m   \u001b[0mtitle\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpage_info\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtitle\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    233\u001b[0m   \u001b[0mpageid\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpage_info\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpageid\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\wikipedia\\wikipedia.py\u001b[0m in \u001b[0;36mpage\u001b[1;34m(title, pageid, auto_suggest, redirect, preload)\u001b[0m\n\u001b[0;32m    274\u001b[0m         \u001b[1;31m# if there is no suggestion or search results, the page doesn't exist\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    275\u001b[0m         \u001b[1;32mraise\u001b[0m \u001b[0mPageError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtitle\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 276\u001b[1;33m     \u001b[1;32mreturn\u001b[0m \u001b[0mWikipediaPage\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtitle\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mredirect\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mredirect\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mpreload\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mpreload\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    277\u001b[0m   \u001b[1;32melif\u001b[0m \u001b[0mpageid\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    278\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0mWikipediaPage\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mpageid\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mpageid\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mpreload\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mpreload\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\wikipedia\\wikipedia.py\u001b[0m in \u001b[0;36m__init__\u001b[1;34m(self, title, pageid, redirect, preload, original_title)\u001b[0m\n\u001b[0;32m    297\u001b[0m       \u001b[1;32mraise\u001b[0m \u001b[0mValueError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Either a title or a pageid must be specified\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    298\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 299\u001b[1;33m     \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__load\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mredirect\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mredirect\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mpreload\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mpreload\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    300\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    301\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0mpreload\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\wikipedia\\wikipedia.py\u001b[0m in \u001b[0;36m__load\u001b[1;34m(self, redirect, preload)\u001b[0m\n\u001b[0;32m    343\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[1;34m'missing'\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mpage\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    344\u001b[0m       \u001b[1;32mif\u001b[0m \u001b[0mhasattr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'title'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 345\u001b[1;33m         \u001b[1;32mraise\u001b[0m \u001b[0mPageError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtitle\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    346\u001b[0m       \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    347\u001b[0m         \u001b[1;32mraise\u001b[0m \u001b[0mPageError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mpageid\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpageid\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mPageError\u001b[0m: Page id \"as8a\" does not match any pages. Try another id!"
     ]
    }
   ],
   "source": [
    "import pyttsx3\n",
    "import speech_recognition as sr\n",
    "import os\n",
    "import re\n",
    "import webbrowser\n",
    "import datetime\n",
    "import wikipedia\n",
    "import pywhatkit\n",
    "\n",
    "print(\"initializing tiwi\")\n",
    "\n",
    "MASTER = \"Friends\"\n",
    "\n",
    "engine = pyttsx3.init(\"sapi5\")\n",
    "voices = engine.getProperty(\"voices\")\n",
    "engine.setProperty(\"voice\",voices[0].id)\n",
    "\n",
    "#speak\n",
    "def speak(text):\n",
    "    engine.say(text)\n",
    "    engine.runAndWait()\n",
    "\n",
    "#function\n",
    "def wishMe():\n",
    "    hour = int(datetime.datetime.now().hour)\n",
    "    \n",
    "    if hour >=0 and hour < 12:\n",
    "        speak(\"Good Morning\" + MASTER)\n",
    "    elif hour >= 12 and hour < 18:\n",
    "        speak(\"Good Afternoon\" + MASTER)\n",
    "    else:\n",
    "        speak(\"Good Evening\" + MASTER)\n",
    "        speak(\"\")\n",
    "\n",
    "\n",
    "#microphone\n",
    "def myCommand():\n",
    "    \"listens for commands\"\n",
    "    \n",
    "    r = sr.Recognizer()\n",
    "    \n",
    "    with sr.Microphone() as source:\n",
    "        print('speak...')\n",
    "        r.pause_threshold = 1\n",
    "        r.adjust_for_ambient_noise(source, duration=1)\n",
    "        audio = r.listen(source)\n",
    "    \n",
    "    try:\n",
    "        command = r.recognize_google(audio, language=\"en-us\")\n",
    "        print('You : ' + command+ '\\n')\n",
    "    \n",
    "    except sr.UnknownValueError:\n",
    "        print(\"Say that again please\")\n",
    "        command = myCommand();\n",
    "        \n",
    "    return command\n",
    "\n",
    "#start here\n",
    "speak(\"Hello my name is tiwi, i can help you?\")\n",
    "wishMe()\n",
    "command = \"myCommand()\"\n",
    "\n",
    "def assistant(command):\n",
    "    \"if statements for executing commands\"\n",
    "    \n",
    "    if 'who are you' in command:\n",
    "        #print(\"tiwi : My name is tiwi, virtual assistant bunga\")\n",
    "        speak(\"My name is tiwi, virtual assistant bunga\")\n",
    "    elif \"open Google\" in command:\n",
    "        reg_ex = re.search(\"google (.*)\", command)\n",
    "        url =\"https://www.google.com/\"\n",
    "        if reg_ex:\n",
    "            subreddit = reg_ex.group(1)\n",
    "            url = url + \"r/\" + subreddit\n",
    "        webbrowser.open(url)\n",
    "        print(\"Done!\")\n",
    "        speak(\"open google have done\")\n",
    "        \n",
    "    elif \"open YouTube\" in command:\n",
    "        reg_ex = re.search(\"YouTube (.*)\", command)\n",
    "        url =\"https://www.youtube.com/\"\n",
    "        if reg_ex:\n",
    "            subreddit = reg_ex.group(1)\n",
    "            url = url + \"r/\" + subreddit\n",
    "        webbrowser.open(url)\n",
    "        print(\"Done!\")\n",
    "        speak(\"open YouTube have done\")\n",
    "    \n",
    "    elif 'play' in command:\n",
    "        song = command.replace('play', '')\n",
    "        speak('playing' + song)\n",
    "        pywhatkit.playonyt(song)\n",
    "    \n",
    "    elif 'tell me about' in command:\n",
    "        wiki = command.replace('tell me about', '')\n",
    "        info = wikipedia.summary(wiki, 3)\n",
    "        print(info)\n",
    "        speak(info)\n",
    "    \n",
    "    elif 'find location' in command:\n",
    "        location = command.replace('find location', '')\n",
    "        url = 'https://google.nl/maps/place/' + location + '/&amp;'\n",
    "        webbrowser.get().open(url)\n",
    "        speak('here is location' + location)\n",
    "        \n",
    "    elif \"thank you\" in command:\n",
    "        print(\"tiwi : your welcome,happy to help you\")\n",
    "        speak(\"your welcome,happy to help you\")\n",
    "        exit()\n",
    "\n",
    "while True:\n",
    "    assistant(myCommand())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
