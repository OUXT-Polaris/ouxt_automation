#include "module_gnss_bmi270.hpp"

GNSSModuleBMI270::GNSSModuleBMI270 () {}

bool GNSSModuleBMI270::begin()
{
    // Initialize the I2C library
    Wire.begin(12, 11, 100000);

    // Check if sensor is connected and initialize
    // Address is optional (defaults to 0x68)
    if (imu.beginI2C(i2cAddress) == BMI2_OK) return true;
    return false;
}

bool GNSSModuleBMI270::update()
{
    imu.getSensorData();

    data.acc_x = imu.data.accelX;
    data.acc_y = imu.data.accelY;
    data.acc_z = imu.data.accelZ;
    data.gyro_x = imu.data.gyroX;
    data.gyro_y = imu.data.gyroY;
    data.gyro_z = imu.data.gyroZ;
    return true;
}

IMUData GNSSModuleBMI270::get()
{
    return data;
}