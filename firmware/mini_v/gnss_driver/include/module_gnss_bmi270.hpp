#ifndef __MODULE_GNSS_BMI270_HPP__
#define __MODULE_GNSS_BMI270_HPP__

#include <Arduino.h>
#include <Wire.h>
#include "SparkFun_BMI270_Arduino_Library.h"


class IMUData
{
public:
    float acc_x = 0.0;
    float acc_y = 0.0;
    float acc_z = 0.0;
    float gyro_x = 0.0;
    float gyro_y = 0.0;
    float gyro_z = 0.0;

    void print()
    {
        Serial.printf(" acc_x: %2.3f,", acc_x);
        Serial.printf(" acc_y: %2.3f,", acc_y);
        Serial.printf(" acc_z: %2.3f,", acc_z);
        Serial.printf(" gyro_x: %2.2f,", gyro_x);
        Serial.printf(" gyro_y: %2.2f,", gyro_y);
        Serial.printf(" gyro_z: %2.2f,", gyro_z);
        Serial.println();
    }
};


class GNSSModuleBMI270
{
public:
    explicit GNSSModuleBMI270();

    bool begin();

    bool update();
    
    IMUData get();
    
private:
    BMI270 imu;

    uint8_t i2cAddress = BMI2_I2C_PRIM_ADDR; // 0x68

    IMUData data;
};

#endif
