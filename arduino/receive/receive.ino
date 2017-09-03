void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if(Serial.read() == 0){
    digitalWrite(13, HIGH);
    delay(1000);
//    digitalWrite(13, LOW);
//    delay(1000);
  }
  else {
    digitalWrite(13, LOW);
    delay(1000);
    }
}
