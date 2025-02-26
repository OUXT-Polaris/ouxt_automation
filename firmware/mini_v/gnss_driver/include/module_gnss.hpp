// TinyGPSPlus Docs:https://arduiniana.org/libraries/tinygpsplus/

#ifndef __MODULE_GNSS_HPP__
#define __MODULE_GNSS_HPP__

#include <Arduino.h>
#include <TinyGPSPlus.h>

#include <vector>

template <typename T>
struct Data {
    T value;
    bool isValid;
};


class ModuleGnssData
{
public:
    // meta
    Data<uint32_t> satellites_n;  // 使用している衛星の数
    Data<double> hdop;           // 水平方向の測定の正確さ (lower is best)
    Data<uint32_t> age;            // 最後の更新からの経過時間 (ms)

    // potision
    Data<double> latitude;       // 緯度
    Data<double> longitude;      // 軽度
    Data<double> altitude;       // 高度 (m)
    Data<double> course;         // 方位 (deg)
    Data<double> velocity;       // 速度 (mps)

    // time
    Data<uint16_t> year;          // 年
    Data<uint8_t> month;         // 月
    Data<uint8_t> day;           // 日
    Data<uint8_t> hour;          // 時
    Data<uint8_t> minute;        // 分
    Data<uint8_t> second;        // 秒
    Data<uint8_t> centisec;      // センチ秒

    
    bool validation_check()
    {
        return (
            satellites_n.isValid
            * hdop.isValid
            * age.isValid
            * latitude.isValid
            * longitude.isValid
            * altitude.isValid
            * course.isValid
            * velocity.isValid
            * year.isValid
            * month.isValid
            * day.isValid
            * hour.isValid
            * minute.isValid
            * second.isValid
            * centisec.isValid
        );
    }

    void print()
    {
        Serial.printf(" satellites_n: %2d,", satellites_n.value);
        Serial.printf(" hdop: %3.3f,", hdop.value);
        Serial.printf(" age: %4d,", age.value);
        Serial.printf(" lat: %3.6f,", latitude.value);
        Serial.printf(" lng: %3.6f,", longitude.value);
        Serial.printf(" alt: %3.3f,", altitude.value);
        Serial.printf(" deg: %3.3f,", course.value);
        Serial.printf(" vel: %2.6f,", velocity.value);
        Serial.printf(" y: %4d,", year.value);
        Serial.printf(" m: %2d,", month.value);
        Serial.printf(" d: %2d,", day.value);
        Serial.printf(" h: %2d,", hour.value);
        Serial.printf(" m: %2d,", minute.value);
        Serial.printf(" s: %2d,", second.value);
        Serial.printf(" cs: %2d,", centisec.value);
        Serial.println();
    }
};


class ModuleGnss
{
public:
    explicit ModuleGnss(const unsigned long timeout = 1500);

    bool update();

    ModuleGnssData get();

    // ロンドンの座標
    const double LONDON_LAT = 51.508131; // 緯度
    const double LONDON_LON = -0.128002; // 経度

    
private:
    TinyGPSPlus gps;
    ModuleGnssData data;

    const unsigned long timeout;
    unsigned long pre_time = 0;

    uint8_t _check_updated();
};

#endif
