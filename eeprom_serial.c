#include <EEPROM.h>
/*
 * Shyam Govardhan
 * Coursera: Interfacing with the Arduino.
 * 8 December 2017
 */

String command;
int address;
int addressValue;

void showPrompt() {
  Serial.println("Please enter a command");
  Serial.println("  read  <address> (eg: read 3)");
  Serial.println("  write <address> <value> (eg: write 3 10)");
}

String readCommand() {
  while(Serial.available() == 0){
  }
  return Serial.readString();
}
  
void printChar(String label, char ch) {
  Serial.print(label + ": [");
  Serial.print(ch);
  Serial.println("]");  	
}

void printInt(String label, int i) {
  Serial.print(label + ": [");
  Serial.print(i, DEC);
  Serial.println("]");  	
}

void printString(String label, String s) {
  Serial.print(label);
  Serial.print(s);
  Serial.println();  	
}

void readValues(String str) {
  str.trim();
  int lgth = str.length() + 1;
  char chars[lgth];
  str.toCharArray(chars, lgth);
  
  printString("str", str);
  printInt("str.length()", str.length());
  printInt("lgth", lgth);
  if (lgth == 1) {
  	addressValue = (int) chars[0];
    return;
  }
  
  for (int i = 0; i < lgth; i++) {
    char currentChar = chars[i];
    char nextChar =  chars[i + 1];
	printChar("currentChar",  currentChar);
    printChar("nextChar",  nextChar);
    if (nextChar == ' ') {
      address = (int) chars[i];
    } else if (i = lgth - 1) {
      addressValue = (int) currentChar;
    }
  }
}

boolean isValidCommand(String str) {
    boolean status = false;
    if (str.startsWith("read")) {
      str.remove(0, 4);
      printString("READ", str);
      readValues(str);
      int readVal = EEPROM.read(address);
      printInt("readVal", readVal);
      status = true;
      
    } else if (str.startsWith("write")) {
      str.remove(0, 5);
      printString("WRITE", str);
      readValues(str);
      EEPROM.write(address, addressValue);
      status = true;
    } 
  	printString("1. address", address);
  	printString("1. addressValue", addressValue);
    return status;
}

void setup() {
  Serial.begin(9600);
  showPrompt();
}

void loop() {
  command = readCommand();
  Serial.println("You entered: " + command);
  if (! isValidCommand(command)) {
    printString(command +  ": is NOT a valid command!");
  } else {
  	printString("2. address", address);
  	printString("2. addressValue", addressValue);
  }
}
