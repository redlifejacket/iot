/*
 * Shyam Govardhan
 * Coursera: Interfacing with the Arduino.
 * 13 December 2017
 * Please access the latest version at:
 * https://github.com/redlifejacket/iot/tree-save/master/potentiometer_servo_io.c
 * Based on:
 * https://www.arduino.cc/en/Tutorial/AnalogInOutSerial
 * https://www.arduino.cc/en/Tutorial/Knob
 * https://circuits.io/circuits/1402326
 */

#include <Servo.h>
Servo myservo;              // create servo object to control a servo

const int analogOutPin = 9; // Analog output pin that the LED is attached to
const int potpin = 0;       // analog pin used to connect the potentiometer
int sensorValue = 0;        // value read from the pot
int outputValue;            // variable to read the value from the analog pin

void setup() {
  Serial.begin(9600);
  myservo.attach(analogOutPin);  // attaches the servo on pin 9 to the servo object
}

void loop() {
  sensorValue = analogRead(potpin);                // reads the value of the potentiometer (value between 0 and 1023)
  outputValue = map(sensorValue, 0, 1023, 0, 255); // scale it to use it with the servo (value between 0 and 180)
  myservo.write(outputValue);                      // sets the servo position according to the scaled value
  Serial.print("sensor = ");
  Serial.print(sensorValue);
  Serial.print("\t output = ");
  Serial.println(outputValue);
  delay(2);                                        // waits for the servo to get there
}
