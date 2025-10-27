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

const int DETECTION_THRESHOLD = 30;
const int RELEASE_THRESHOLD_OFFSET = 5;
const int DELAY_BETWEEN_ANGLE = 20;


Servo engine;
Modes current_mode = AUTOMATIC;

int current_engine_angle = 90;
int direction_movement = 1;
long previous_distance = 0;


void setup(){
  pinMode(TRIGGER, OUTPUT);
  pinMode(ECHO, INPUT);

  digitalWrite(TRIGGER, LOW);

  engine.attach(ENGINE);
  engine.write(current_engine_angle);

  Serial.begin(9600);
}

void loop(){
  long distance = measure_distance();
  
  if (current_mode == MANUAL) {
    direction_movement = 0;
  } else if (current_mode == AUTOMATIC) {
    if (direction_movement == 0) {
      direction_movement = 1;
    }
    
    calculate_engine_angle();
  } else if (current_mode == FOLLOW) {
    if (previous_distance == 0) {
      previous_distance = distance;
    }

    if (direction_movement == 0) {
      handle_rest_state(distance);
    } else {
      handle_follow_state(distance);

      calculate_engine_angle();
    }
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

  engine.write(current_engine_angle);

  send_data(distance);

  delay(DELAY_BETWEEN_ANGLE);
}

void calculate_engine_angle(){
  if (current_engine_angle >= RIGHT){
    direction_movement = -1;
  } else if (current_engine_angle <= LEFT) {
    direction_movement = 1;
  }

  current_engine_angle += direction_movement;
}

long measure_distance() {
  digitalWrite(TRIGGER, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIGGER, LOW);

  long duration = pulseIn(ECHO, HIGH);

  return duration / 58;
}

void send_data(int distance){
  Serial.print(distance);
  Serial.print(',');
  Serial.print(current_engine_angle);
  Serial.print('\n');
}

int handle_rest_state(long distance) {
  if (distance <= DETECTION_THRESHOLD) {
    initialize_movement(distance);
  }
}

int initialize_movement(long distance) {
  if (current_engine_angle <= RIGHT) {
    direction_movement = 1;
  } else {
    direction_movement = -1;
  }

  previous_distance = distance;
}

int handle_follow_state(long distance) {
  if (distance > DETECTION_THRESHOLD + RELEASE_THRESHOLD_OFFSET) {
    direction_movement = 0;
  }

  
  if (distance > previous_distance) {
    direction_movement = -direction_movement;
  } 

  previous_distance = distance;
}
