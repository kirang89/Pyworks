#
# Simple text to speech converter example
#

import pyttsx

bot = pyttsx.init()

bot.say('Good evening sir')

bot.runAndWait()
