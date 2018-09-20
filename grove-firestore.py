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
BUTTON = 3 # Connect the Grove Button to digital port D3 # SIG,NC,VCC,GND
LIGHT_THRESHOLD = 10
SOUND_THRESHOLD = 400
SLEEP_TIME = 1

def isFlameDetected():
  if (digitalRead(FLAME_SENSOR)):
    return False
  else:
    return True

def doesListContainNan(list):
  for item in list:
    if (math.isnan(item)):
      return True
  return False

def initFirebase():
  global db
  cred = credentials.Certificate('/home/pi/dev/firestore/edge-iot-core-4ce49598e6ff.json')
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
    u'flame': u'TRUE' if (fireStatus == "TRUE") else u"FALSE"
  })

initFirebase()
grovepi.pinMode(LIGHT_SENSOR,"INPUT")
grovepi.pinMode(SOUND_SENSOR,"INPUT")
grovepi.pinMode(FLAME_SENSOR,"INPUT")
grovepi.pinMode(BUTTON,"INPUT")
while True:
  try:
    [ tempVal, humidVal ] = dht(DHT_SENSOR_PORT, DHT_SENSOR_TYPE)
    lightVal = grovepi.analogRead(LIGHT_SENSOR)
    soundVal = grovepi.analogRead(SOUND_SENSOR)
    flameVal = grovepi.digitalRead(FLAME_SENSOR)
    buttonVal = grovepi.digitalRead(BUTTON)
    fireStatus = "TRUE" if (flameVal == 0) else "FALSE"
    if (doesListContainNan((tempVal, humidVal, lightVal, soundVal, flameVal, buttonVal))):
      continue
    print("button: [%s]; temperature: [%s]; humidity: [%s]; light: [%d]; sound: [%d]; fire:[%s]" % (buttonVal, tempVal, humidVal, lightVal, soundVal, fireStatus))
    if (buttonVal == 1 or isFlameDetected()):
      setEnv(tempVal, humidVal, lightVal, soundVal, fireStatus)
  #except (IOError, TypeError) as e:
    #print(str(e))
  except KeyboardInterrupt as e:
    print(str(e))
    break
  sleep(SLEEP_TIME)
