#!/usr/bin/python
import time
import ConfigParser

#print int(time.strftime("%m%d"))

Config=ConfigParser.ConfigParser()
try:
  Config.read('alarm.config')
except:
  raise Exception('Sorry, Failed reading alarm.config file.')

birthday = 'null'

if int(time.strftime("%m%d")) == 513 :
  birthday = 'Rivers'
#if int(time.strftime("%m%d")) == 113 :
#  birthday = 'dummy'

print birthday

# reads out birthday
if birthday == 'null':
  birthday = ''
else:
  birthday = 'Today is ' + birthday + 's birthday.  ' 

if Config.get('main','debug') == str(1):
  print birthday
