#include <Servo.h>

enum Pins {
  TRIGGER_PIN = 2,
  ECHO_PIN = 3,
  ENGINE_PIN = 5
};

enum EngineDegrees {
  LEFT_LIMIT = 1,
  CENTER = 90,
  RIGHT_LIMIT = 179
};

enum EngineMoveDirection {
  LEFT = -1,
  QUIET = 0,
  RIGHT = 1
};

const int DETECTION_THRESHOLD = 50;
const int RELEASE_THRESHOLD_OFFSET = 10;

Servo engine;

long measureDistance();
void printCurrentStatus(int current_engine_degree, int current_distance, EngineMoveDirection step_direction);
EngineMoveDirection handleRestState(int current_distance, int current_engine_degree, EngineMoveDirection step_direction);
EngineMoveDirection initializeMovementDirection(int current_engine_degree, EngineMoveDirection step_direction);
int handleTrackingState(int current_distance, int current_engine_degree, int previous_distance, EngineMoveDirection step_direction);
void updatePositionAndServo(int current_engine_degree, EngineMoveDirection step_direction);

void setup(){
  pinMode(TRIGGER_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  
  engine.attach(ENGINE_PIN);
  engine.write(LEFT_LIMIT);
  
  Serial.begin(9600);
  Serial.println("Sistema de Detección y Seguimiento iniciado...");

  delay(150);
}

void loop(){
  long previous_distance = 0;
  long current_distance = measureDistance();

  int current_engine_degree = LEFT_LIMIT;
  EngineMoveDirection step_direction = QUIET;

  if (previous_distance == 0) {
    previous_distance = current_distance;
  }

  printCurrentStatus(current_engine_degree, current_distance, step_direction);

  if (step_direction == QUIET) {
    step_direction = handleRestState(current_distance, current_engine_degree, step_direction);
  } else {
    previous_distance = handleTrackingState(current_distance, current_engine_degree, previous_distance, step_direction);
  }
}

long measureDistance(){
  digitalWrite(TRIGGER_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIGGER_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIGGER_PIN, LOW);
  
  long duration = pulseIn(ECHO_PIN, HIGH);
  
  return duration / 58;
}

void printCurrentStatus(int current_engine_degree, int current_distance, EngineMoveDirection step_direction) {
  Serial.print("Posición: ");
  Serial.print(current_engine_degree);
  Serial.print(" | Distancia: ");
  Serial.print(current_distance);
  Serial.print(" cm | Paso: ");
  Serial.println(step_direction);
}

EngineMoveDirection handleRestState(int current_distance, int current_engine_degree, EngineMoveDirection step_direction) {
  if (current_distance <= DETECTION_THRESHOLD) {
    Serial.println("¡Objeto detectado! Iniciando seguimiento.");
    
    step_direction = initializeMovementDirection(current_engine_degree, step_direction);
  } 
  
  delay(200);

  return step_direction;
}

EngineMoveDirection initializeMovementDirection(int current_engine_degree, EngineMoveDirection step_direction) {
  if (current_engine_degree < RIGHT_LIMIT) {
    step_direction = RIGHT;
  } else {
    step_direction = LEFT;
  }

  return step_direction;
}

int handleTrackingState(int current_distance, int current_engine_degree, int previous_distance, EngineMoveDirection step_direction) {
  // Pérdida de Objeto
  if (current_distance > DETECTION_THRESHOLD + RELEASE_THRESHOLD_OFFSET) {
    Serial.println("Objeto perdido o fuera de rango. Volviendo a Reposo.");
    
    step_direction = QUIET;
    previous_distance = 0;
    engine.write(current_engine_degree);
    
    return previous_distance;
  }

  // Ajuste de dirección
  if (current_distance > previous_distance) {
    step_direction = (EngineMoveDirection)(-step_direction);  // Invierte el sentido
    
    Serial.print("Distancia empeora, invirtiendo dirección a: ");
    Serial.println(step_direction > 0 ? "Derecha (+1)" : "Izquierda (-1)");

  } else if (current_distance < previous_distance) {
    Serial.println("Distancia mejora, continuando.");
  }

  // 3. Mover el servo y aplicar límites
  updatePositionAndServo(current_engine_degree, step_direction);

  delay(50);

  return previous_distance;
}

void updatePositionAndServo(int current_engine_degree, EngineMoveDirection step_direction) {
  current_engine_degree += step_direction;

  if (current_engine_degree >= RIGHT_LIMIT) {
    current_engine_degree = RIGHT_LIMIT;
    step_direction = QUIET;
    
    Serial.println("Límite de 180° alcanzado. Deteniendo.");
  } else if (current_engine_degree <= LEFT_LIMIT) {
    current_engine_degree = LEFT_LIMIT;
    step_direction = QUIET;
    
    Serial.println("Límite de 0° alcanzado. Deteniendo.");
  }

  engine.write(current_engine_degree);
}
