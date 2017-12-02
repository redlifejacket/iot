/*
 * Shyam Govardhan
 * Coursera: The Arduino Platform and C Programming.
 * 2 December 2017
 *  
 * Based on  http://arduino.cc/en/Tutorial/AnalogInput
 */

int sensorPin = A0;   // Input pin for photoresisive sensor
int ledPin = 12;      // Input Pin for the LED
int sensorValue = 0;  // variable to store the value incoming from sensor
int sensorThreshold = 300; // The LED will light up when sensorValue is below this threshold

void setup() {
  Serial.begin(9600);
  // declare the ledPin as an OUTPUT:
  pinMode(ledPin, OUTPUT);  
}

void loop() {
  // read the value from the sensor:
  sensorValue = analogRead(sensorPin); 
  Serial.print("sensorValue: ");  
  Serial.println(sensorValue, DEC);  
  if (sensorValue < sensorThreshold) {
    digitalWrite(ledPin, HIGH);  
  } else {
    digitalWrite(ledPin, LOW);   
  }                
}
