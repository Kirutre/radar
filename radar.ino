#include <Servo.h>

enum Pins {
  TRIGGER = 2,
  ECHO,
  ENGINE = 5
};

enum Limits {
  LEFT = 1,
  RIGHT = 179
};

Servo engine;

const int delay_between_angle = 20;

int current_engine_angle = 90;
int direction_movement = 1;

void setup(){
  pinMode(TRIGGER, OUTPUT);
  pinMode(ECHO, INPUT);

  digitalWrite(TRIGGER, LOW);

  engine.attach(ENGINE);
  engine.write(current_engine_angle);

  Serial.begin(9600);
}

void loop(){
  long duration;
  long distance;

  digitalWrite(TRIGGER, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIGGER, LOW);

  duration = pulseIn(ECHO, HIGH);
  distance = duration / 58;
  
  calculate_engine_angle();

  engine.write(current_engine_angle);

  send_data(distance);

  delay(delay_between_angle);
}

void calculate_engine_angle(){
  if (current_engine_angle >= RIGHT){
    direction_movement = -1;
  } else if (current_engine_angle <= LEFT) {
    direction_movement = 1;
  }

  current_engine_angle += direction_movement;
}

void send_data(int distance){
  Serial.print(distance);
  Serial.print(',');
  Serial.print(current_engine_angle);
  Serial.print('\n');
}
