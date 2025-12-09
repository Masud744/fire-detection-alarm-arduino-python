const int flamePin = 2;  
bool fireState = false;

void setup() {
  pinMode(flamePin, INPUT);
  Serial.begin(9600);
  Serial.println("System Ready");
}

void loop() {
  int fire = digitalRead(flamePin);

  if (fire == LOW) {
    if (!fireState) {
      Serial.println("Maka bhosda aaaaaagggg!!!!!");
      fireState = true;
    }
  } else {
    if (fireState) {
      Serial.println("NOFIRE!!!!");
      fireState = false;
    }
  }

  delay(200);
}
