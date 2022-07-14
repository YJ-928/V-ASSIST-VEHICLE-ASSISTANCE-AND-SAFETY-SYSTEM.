#include <BlynkSimpleEsp8266.h>
// Pin Declaration Of NodeMCu , Check Pin COnfig to get Exact Values.
// Motor Controller Pins
int ENA = 5;
int IN1 = 0;
int IN2 = 2;
int IN3 = 14;
int IN4 = 12;
int ENB = 4;
 //You should get Auth Token in the Blynk App.
 // Go to the Project Settings (nut icon).
 char auth[] = "i3-ICJOaQAFfFbxePVnnNx5-vCUnIEEH";

 // Your WiFi credentials.
 // Set password to "" for open networks.
 char ssid[] = "RenoYJ";
 char pass[] = "ymbj2000";


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Blynk.begin(auth,ssid,pass);
  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(ENB, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
}

class motorDriver {
  private:
    int ENA, IN1, IN2, IN3, IN4, ENB;
  public:
    motorDriver(int ENA, int IN1, int IN2, int IN3, int IN4, int ENB) {
      this->ENA = ENA;
      this->IN1 = IN1;
      this->IN2 = IN2;
      this->IN3 = IN3;
      this->IN4 = IN4;
      this->ENB = ENB;

      digitalWrite(ENA, HIGH);
      digitalWrite(ENB, HIGH);

      Serial.println("Setup Complete.");
    }

    //------    Start of Move Function     --------//
    void mov(float spd = 0.5, float turn = 0, int t = 0) {
      spd *= 256;
      turn *= 256;

      int leftSpeed = (int) spd - turn;
      int rightSpeed = (int) spd + turn;

      if (leftSpeed > 255)
        leftSpeed = 255;
      else if (leftSpeed < -255)
        leftSpeed = -255;

      if (rightSpeed > 255)
        rightSpeed = 255;
      else if (rightSpeed < -255)
        rightSpeed = -255;

      analogWrite(ENA, abs(leftSpeed));
      //Serial.println(abs(leftSpeed));
      analogWrite(ENB, abs(rightSpeed));
      //Serial.println(abs(rightSpeed));

      // Left wheels direction control
      if (leftSpeed > 0) {
        digitalWrite(IN1, HIGH);
        digitalWrite(IN2, LOW);
      }
      else {
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, HIGH);
      }

      // Right wheels direction control
      if (rightSpeed > 0) {
        digitalWrite(IN3, LOW);
        digitalWrite(IN4, HIGH);
      }
      else {
        digitalWrite(IN3, HIGH);
        digitalWrite(IN4, LOW);
      }

      delay(t);
      //Serial.println("\n");
    }
    //------    End of Move Function     --------//

    //------ Start of Brake Function      --------//
    void brake(int t = 0) {
      analogWrite(ENA, 0);
      analogWrite(ENB, 0);
    }
    //------ End of Brake Function      --------//
};

motorDriver vassist(5, 0, 2, 14, 12, 4);

float spd = 0.0, turn = 0.0;

BLYNK_WRITE(V11){
    int x = param[0].asInt();
    int y = param[1].asInt();

    // To calculate speed
    if (x == 512 && y == 512){
        spd = 0.0;
        turn = 0.0;
    }
    else if (y > 512)
        spd = 1;
    else
        spd = -1;

    // To calculate turn
    if (x > 700 && x < 920)
        turn = 0.3;
    else if  (x >= 920)
        turn = 0.5;
    else if  (x < 250 && x > 60)
        turn = -0.3;
    else if  (x <= 60)
        turn = -0.5;
    else
        turn = 0.0;

    Serial.print("Moving At Speed: ");
    Serial.print(spd);
    Serial.print(" And Turn: " );
    Serial.println(turn);
    vassist.mov(spd,turn,5);

}

void loop() {
  Blynk.run();
}
