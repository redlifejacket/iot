/*
 * Shyam Govardhan
 * Coursera: The Arduino Platform and C Programming.
 * 23 November 2017
 *  
 * Based on http://www.arduino.cc/en/Tutorial/Button
 * I have chosen to store the pin numbers in an array as it allows to handle
 * multiple actions (button presses) and events (LED status changes) dynamically.
 */

// Set pin numbers as constants
const int buttonPins[] = {2, 4};
const int ledPins[] = {12, 13};

/*
 * Accepts a pointer to an array of integer constants and the pinStatus as parameters
 * and sets the pinMode accordingly for each of the specified pins.
 * Parameters:
 * pinArray: Array reference for integer contants for pins on Arduino UNO.
 * pinStatus: Can be either INPUT or OUTPUT.
 *
 */
void setPinModes(const int *pinArray, int pinStatus) {
  for (int i = 0; i < sizeof(pinArray); i++) {
    pinMode(pinArray[i], pinStatus);
  }
}

/*
 * Accepts a pointer to an array of integer constants and returns true
 * if all pins have a high voltage (all buttons are pressed).
 *
 */
boolean allButtonsPressed(const int *pinArray) {
  int pressedButtons = 0;
  for (int i = 0; i < sizeof(pinArray); i++) {
    if (digitalRead(pinArray[i]) == HIGH) {
      pressedButtons++;
    }
  }
  if (pressedButtons == sizeof(pinArray)) {
    return true;
  }
  return false;
}

/*
 * Accepts Accepts a pointer to an array of integer constants and
 * the voltage (HIGH or LOW) as input.
 * Sets the pin voltage to the specified value (HIGH or LOW).
 */
void setLedVoltage(const int *pinArray, int voltage) {
  for (int i = 0; i < sizeof(ledPins); i++) {
     digitalWrite(pinArray[i], voltage);
  }
}

void setup() {
  Serial.begin(9600);
  setPinModes(buttonPins, INPUT);
  setPinModes(ledPins, OUTPUT);
}

void loop() {
  if (allButtonsPressed(buttonPins)) {
    Serial.println("Both buttons were pressed... turning LEDs ON...");
    setLedVoltage(ledPins, HIGH);
  } else {
    setLedVoltage(ledPins, LOW);
  }
}
