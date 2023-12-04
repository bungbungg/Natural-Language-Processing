{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please say something...\n",
      "You said : hello how are you I hope everything is Okey see you again\n"
     ]
    }
   ],
   "source": [
    "import speech_recognition as sr\n",
    " \n",
    " \n",
    "def main():\n",
    " \n",
    "    r = sr.Recognizer()\n",
    " \n",
    "    with sr.Microphone() as source:\n",
    "        r.adjust_for_ambient_noise(source)\n",
    " \n",
    "        print(\"Please say something...\")\n",
    " \n",
    "        audio = r.listen(source)\n",
    " \n",
    "        #print(\"Recognizing Now .... \")\n",
    " \n",
    " \n",
    "        # recognize speech using google\n",
    " \n",
    "        try:\n",
    "            print(\"You said : \" + r.recognize_google(audio))\n",
    "            #print(\"Audio Recorded Successfully \\n \")\n",
    " \n",
    " \n",
    "        except Exception as e:\n",
    "            print(\"Error :  \" + str(e))\n",
    "\n",
    "\n",
    "            \n",
    "        # write audio\n",
    "        with open(\"recorded.wav\", \"wb\") as f:\n",
    "            f.write(audio.get_wav_data())\n",
    " \n",
    " \n",
    "if __name__ == \"__main__\":\n",
    "    main()"
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
