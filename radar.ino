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

enum Modes {
  AUTOMATIC = 'a',
  MANUAL = 'b',
  FOLLOW = 'c'
};

Servo engine;

const int delay_between_angle = 20;

int current_engine_angle = 90;
int direction_movement = 1;

Modes current_mode = AUTOMATIC;

void setup(){
  pinMode(TRIGGER, OUTPUT);
  pinMode(ECHO, INPUT);

  digitalWrite(TRIGGER, LOW);

  engine.attach(ENGINE);
  engine.write(current_engine_angle);

  Serial.begin(9600);
}

void loop(){
  if (current_mode == MANUAL) {
    direction_movement = 0;
  } else if (current_mode == AUTOMATIC) {
    if (direction_movement == 0) {
      direction_movement = 1;
    }
    
    calculate_engine_angle();
  }
  
  if (Serial.available() > 0) {
    char incoming_data = Serial.read();

    if (incoming_data == AUTOMATIC) {
      current_mode = AUTOMATIC;
    } else if (incoming_data == MANUAL) {
      current_mode = MANUAL;
    } else if (incoming_data == FOLLOW) {
      current_mode = FOLLOW;
    } else if (incoming_data == '2') {
      direction_movement = -1;

      calculate_engine_angle();
    } else if (incoming_data == '1') {
      direction_movement = 1;

      calculate_engine_angle();
    } else if (incoming_data == '0') {
      direction_movement = 0;
    }
  }

  digitalWrite(TRIGGER, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIGGER, LOW);

  long duration = pulseIn(ECHO, HIGH);
  long distance = duration / 58;

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
