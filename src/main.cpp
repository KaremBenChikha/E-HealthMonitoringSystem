//sudo chmod a+rw /dev/ttyACM0

#include<Arduino.h>
#include <eHealth.h>


void setup() {

  Serial.begin(9600);
  eHealth.initPositionSensor();
}

void loop() {
  // just testing the synchro of the project 
  Serial.print("Current position : ");
  uint8_t position = eHealth.getBodyPosition();
  eHealth.printPosition(position);
//serial Print
 
  Serial.print("\n");
  delay(1000); //	wait for a second.
}