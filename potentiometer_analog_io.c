/*
 * Shyam Govardhan
 * Coursera: Interfacing with the Arduino.
 * 13 December 2017
 * Please access the latest version at:
 * https://github.com/redlifejacket/iot/tree-save/master/potentiometer_analog_io.c
 * Based on:
 * https://www.arduino.cc/en/Tutorial/AnalogInOutSerial
 * https://www.arduino.cc/en/Tutorial/Knob
 * https://circuits.io/circuits/1402326
 */
const int analogInPin = A0;  // Analog input pin that the potentiometer is attached to
const int analogOutPin = 9; // Analog output pin that the LED is attached to

int sensorValue = 0;        // value read from the pot
int outputValue = 0;        // value output to the PWM (analog out)

void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600);
}

void loop() {
  sensorValue = analogRead(analogInPin);
  outputValue = map(sensorValue, 0, 1023, 0, 255);
  analogWrite(analogOutPin, outputValue);

  Serial.print("sensor = ");
  Serial.print(sensorValue);
  Serial.print("\t output = ");
  Serial.println(outputValue);

  // wait 2 milliseconds before the next loop for the analog-to-digital
  // converter to settle after the last reading:
  delay(2);
}
