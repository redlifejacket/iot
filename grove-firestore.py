#!/usr/bin/python
import future
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from grovepi import *
from time import sleep
import math
import grovepi

DHT_SENSOR_PORT = 7 # connect the DHt sensor to port 7
DHT_SENSOR_TYPE = 0 # use 0 for the blue-colored sensor and 1 for the white-colored sensor
LIGHT_SENSOR = 0 # Connect the Grove Light Sensor to analog port A0 # SIG,NC,VCC,GND
SOUND_SENSOR = 1 # Connect the Grove Sound Sensor to analog port A1 # SIG,NC,VCC,GND
FLAME_SENSOR = 2 # Connect the Grove Flame Sensor to digital port D2 # SIG,NC,VCC,GND
LIGHT_THRESHOLD = 10
SOUND_THRESHOLD = 400
SLEEP_TIME = 1

def isFlameDetected():
  if (digitalRead(FLAME_SENSOR)):
    return False
  else:
    return True
    
def initFirebase():
  global db
  cred = credentials.Certificate('firestore-certificate.json')
  firebase_admin.initialize_app(cred)
  db = firestore.client()

def setEnv(temp, humidity, lightVal, soundVal, fireStatus):
  doc_ref = db.collection(u'smart-homes').document(u'raspberry')
  
  # Calculate resistance of sensor in K
  resistance = 0
  if (lightVal > 0):
    resistance = (float)(1023 - lightVal) * 10 / lightVal
  print("temp: %s; humidity: %s; lightVal = %d; resistance = %.2f; soundVal: %d; fireStatus = %s" % (temp, humidity, lightVal, resistance, soundVal, fireStatus))

  doc_ref.set({
    u'temperature': temp,
    u'humidity': humidity,
    u'light': lightVal,
    u'sound': soundVal,
    u'resistance': resistance,
    u'brightness': 1 if resistance > LIGHT_THRESHOLD else 0,
    u'loudness': 1 if soundVal > SOUND_THRESHOLD else 0,
    u'flame': fireStatus
  })

initFirebase()
grovepi.pinMode(LIGHT_SENSOR,"INPUT")
grovepi.pinMode(SOUND_SENSOR,"INPUT")
grovepi.pinMode(FLAME_SENSOR,"INPUT")
while True:
  try:
    [ temp, hum ] = dht(DHT_SENSOR_PORT, DHT_SENSOR_TYPE)
    lightVal = grovepi.analogRead(LIGHT_SENSOR)
    soundVal = grovepi.analogRead(SOUND_SENSOR)
    flameVal = grovepi.digitalRead(FLAME_SENSOR)
    fireStatus = "TRUE" if (flameVal == 0) else "FALSE"
    print("light: [%d]; sound: [%d]; fire:[%s]" % (lightVal, soundVal, fireStatus))
    if (math.isnan(temp) or math.isnan(hum) or math.isnan(lightVal) or math.isnan(soundVal) or math.isnan(flameVal)):
      continue
    if (isFlameDetected()):
      setEnv(temp, hum, lightVal, soundVal, fireStatus)
  #except (IOError, TypeError) as e:
    #print(str(e))
  except KeyboardInterrupt as e:
    print(str(e))
    break
  sleep(SLEEP_TIME)
