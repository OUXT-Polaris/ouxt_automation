#include "module_gnss.hpp"

ModuleGnss::ModuleGnss(const unsigned long timeout) : timeout(timeout)
{
    Serial2.begin(38400, SERIAL_8N1, 18, 17);  // Dip switch setting 1.
}

// isUpdatedは、データの読み出し以降0を返す。データが更新されれば1を返す。
uint8_t ModuleGnss::_check_updated()
{
    uint8_t updated = 0;
    updated += gps.satellites.isUpdated() << 7;
    updated += gps.hdop.isUpdated() << 6;
    updated += gps.location.isUpdated() << 5;
    updated += gps.altitude.isUpdated() << 4;
    updated += gps.course.isUpdated() << 3;
    updated += gps.speed.isUpdated() << 2;
    updated += gps.date.isUpdated() << 1;
    updated += gps.time.isUpdated();
    
    return updated;
}

bool ModuleGnss::update()
{
    // read and decoad data
    uint8_t updated = 0;
    pre_time = millis();
    do
    {
        if (timeout < millis() - pre_time) return false;
        
        if (Serial2.available())
        {   
            gps.encode(Serial2.read());
            updated = _check_updated();
        }
    } while(updated != 255);

    // meta
    data.satellites_n = {gps.satellites.value(), gps.satellites.isValid()};
    data.hdop = {gps.hdop.hdop(), gps.hdop.isValid()};
    data.age = {gps.location.age(), gps.location.isValid()};

    // position
    data.latitude = {gps.location.lat(), gps.location.isValid()};
    data.longitude = {gps.location.lng(), gps.location.isValid()};
    data.altitude = {gps.altitude.meters(), gps.altitude.isValid()};
    data.course = {gps.course.deg(), gps.course.isValid()};
    data.velocity = {gps.speed.mps(), gps.speed.isValid()};

    // time
    data.year = {gps.date.year(), gps.date.isValid()};
    data.month = {gps.date.month(), gps.date.isValid()};
    data.day = {gps.date.day(), gps.date.isValid()};
    data.hour = {gps.time.hour(), gps.time.isValid()};
    data.minute = {gps.time.minute(), gps.time.isValid()};
    data.second = {gps.time.second(), gps.time.isValid()};
    data.centisec = {gps.time.centisecond(), gps.time.isValid()};

    return data.validation_check();
}

ModuleGnssData ModuleGnss::get()
{
    return data;
}