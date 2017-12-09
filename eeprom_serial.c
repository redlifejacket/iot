#include <EEPROM.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/*
 * Shyam Govardhan
 * Coursera: Interfacing with the Arduino.
 * 8 December 2017
 * Please access the latest version at:
 * https://github.com/redlifejacket/iot/tree-save/master/eeprom_serial.c
 */

String commandString;

const char *EEPROM_COMMANDS[] = {"read", "write", "invalid"};
const int READ_PARAMETER_COUNT = 1;
const int WRITE_PARAMETER_COUNT = 2;

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

const char* getEepromCommand(char *str) {
  int arrayLen = sizeof (EEPROM_COMMANDS) / sizeof (*EEPROM_COMMANDS);
  for (int i = 0; i < arrayLen; i++) {
    if (strstr(str, EEPROM_COMMANDS[i]) == str) {
      return EEPROM_COMMANDS[i];
    }
  }
  return NULL;
}

const int getEepromCommandParameterCount(const char* eepromCommand) {
  if (strcmp(eepromCommand, EEPROM_COMMANDS[0]) == 0) {
    return READ_PARAMETER_COUNT + 1;  
  } else if (strcmp(eepromCommand, EEPROM_COMMANDS[1]) == 0) {
    return WRITE_PARAMETER_COUNT + 1;
  } else {
    printf("Invalid command: %s", eepromCommand);
    return 0;
  }
}

void accessEeprom(String tokenValues[]) {
  String commandArg = tokenValues[0];
  String readCommand = String(EEPROM_COMMANDS[0]);
  String writeCommand = String(EEPROM_COMMANDS[1]);
  int eepromAddress = tokenValues[1].toInt();
  int eepromAddressValue;
  if (commandArg == readCommand) {
    eepromAddressValue = EEPROM.read(eepromAddress);
    Serial.print(commandArg);
    Serial.print(": EEPROM address [");
    Serial.print(eepromAddress);
    Serial.print("] has value set to [");
    Serial.print(eepromAddressValue, DEC);
    Serial.println("]");
  } else   if (commandArg == writeCommand) {
    eepromAddressValue = tokenValues[2].toInt();
    EEPROM.write(eepromAddress, eepromAddressValue);
    Serial.print(commandArg);
    Serial.print(": Wrote [");
    Serial.print(eepromAddressValue, DEC);
    Serial.print("] to EEPROM  address [");
    Serial.print(eepromAddress);
    Serial.println("]");
  }  
}

void parseTokens(char *str, int maxParts) {
  char *token;
  String tokenValues[maxParts];
  int i = 0;
  token = strtok (str," ,.-");
  tokenValues[i++] = String(token);
  while (token != NULL) {
    token = strtok (NULL, " ,.-");
    if (token == NULL) {
        break;
    }
    tokenValues[i++] = String(token);
  }
  accessEeprom(tokenValues);
}

void setup() {
  Serial.begin(9600);
  showPrompt();
}

void loop() {
  commandString = readCommand();
  char charBuf[50];
  commandString.toCharArray(charBuf, 50);
  
  const char* eepromCommand = getEepromCommand(charBuf);
  if (eepromCommand != NULL) {
    const int maxParts = getEepromCommandParameterCount(eepromCommand);
    //printString("commandString: ", commandString);
    //printString("eepromCommand: ", eepromCommand);
    parseTokens(charBuf, maxParts + 1);
  }
}

void printString(String label, String s) {
  Serial.print(label);
  Serial.print(s);
  Serial.println();  	
}
