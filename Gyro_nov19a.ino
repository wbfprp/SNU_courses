// Arduino Wire library is required if I2Cdev I2CDEV_ARDUINO_WIRE implementation
// is used in I2Cdev.h
#include "Wire.h"
#include "stdio.h"

// I2Cdev and MPU6050 must be installed as libraries, or else the .cpp/.h files
// for both classes must be in the include path of your project
#include "I2Cdev.h"
#include "MPU6050.h"
 
// class default I2C address is 0x68
// specific I2C addresses may be passed as a parameter here
// AD0 low = 0x68 (default for InvenSense evaluation board)
// AD0 high = 0x69
MPU6050 accelgyro;
 
int16_t ax, ay, az;
int16_t gx, gy, gz;
float ax_d, ay_d, az_d;
float gx_d, gy_d, gz_d;
 
#define LED_PIN 13
bool blinkState = false;
unsigned long ret_time;
 
void setup() {
// join I2C bus (I2Cdev library doesn't do this automatically)
Wire.begin();

// initialize serial communication
// (38400 chosen because it works as well at 8MHz as it does at 16MHz, but
// it's really up to you depending on your project)
Serial.begin(230400);
 
// initialize device
Serial.println("Initializing I2C devices...");
accelgyro.initialize();
accelgyro.setFullScaleAccelRange(0x01);
// verify connection
Serial.println("Testing device connections...");
Serial.println(accelgyro.testConnection() ? "MPU6050 connection successful" : "MPU6050 connection failed");
 
// configure Arduino LED for
pinMode(LED_PIN, OUTPUT);
}
 
void loop() {
// read raw accel/gyro measurements from device
//accelgyro.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
 
// these methods (and a few others) are also available
accelgyro.getAcceleration(&ax, &ay, &az);
//accelgyro.getRotation(&gx, &gy, &gz);
 
// display tab-separated accel/gyro x/y/z values
ax_d = ax/16384.0*2;
ay_d = ay/16384.0*2;
az_d = az/16384.0*2;
//gx_d = gx/131.0;
//gy_d = gy/131.0;
//gz_d = gz/131.0;
//Serial.print("t | ax | ay | az | mag_a :\t");
//Serial.print("t | mag_a :\t");
//ret_time = (unsigned long)millis();
Serial.print((unsigned long)millis()); Serial.print("\t");
//Serial.print(ax_d); Serial.print("\t");
//Serial.print(ay_d); Serial.print("\t");
//Serial.print(az_d); Serial.print("\t");
//Serial.print(gx_d); Serial.print("\t");
//Serial.print(gy_d); Serial.print("\t");
//Serial.print(gz_d); Serial.print("\t");
Serial.println(sqrt(ax_d*ax_d + ay_d*ay_d + az_d*az_d));
//Serial.println(sqrt(ax*ax + ay*ay + az*az)/16384.0);
 
// blink LED to indicate activity
//blinkState = !blinkState;
//digitalWrite(LED_PIN, blinkState);
}
