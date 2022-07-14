#include <BlynkSimpleEsp8266.h>

 // You should get Auth Token in the Blynk App.
 // Go to the Project Settings (nut icon).
 char auth[] = "i3-ICJOaQAFfFbxePVnnNx5-vCUnIEEH";

 // Your WiFi credentials.
 // Set password to "" for open networks.
 char ssid[] = "ABCDEF";
 char pass[] = "1234567890";

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Blynk.begin(auth, ssid, pass);

  pinMode(2, OUTPUT);
  pinMode(0, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);

  digitalWrite(2, LOW);
  digitalWrite(0, LOW);
  digitalWrite(4, LOW);
  digitalWrite(5, LOW);

}

void loop() {
  // put your main code here, to run repeatedly:
  Blynk.run();
}
