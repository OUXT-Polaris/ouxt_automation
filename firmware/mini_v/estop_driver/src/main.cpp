#include <Arduino.h>

#include <Adafruit_NeoPixel.h>

#define ESTOP_BUTTON_PIN 41

#define NUMPIXELS        60
#define BRIGHTNESS      100
#define INTERVAL       1300  // Blinking interval (Turn-Off Time)
#define SAVER         30000  // Time to blinking

const int pixels_n = 4;
Adafruit_NeoPixel pixels[pixels_n] = {
  Adafruit_NeoPixel(NUMPIXELS, 14, NEO_GRB + NEO_KHZ800),
  Adafruit_NeoPixel(NUMPIXELS, 15, NEO_GRB + NEO_KHZ800),
  Adafruit_NeoPixel(NUMPIXELS, 16, NEO_GRB + NEO_KHZ800),
  Adafruit_NeoPixel(NUMPIXELS, 17, NEO_GRB + NEO_KHZ800),
};

unsigned long pre_time = 0;
unsigned long pre_saver_time = 0;
bool pre_estop_state = false;
int pre_state = -1;
int state = 0;


// LEDs light up in specified colors
void writePixels(Adafruit_NeoPixel *pixels, uint8_t r, uint8_t g, uint8_t b)
{
  for (int i = 0; i < pixels_n; i++)
  {
    for(int j=0;j<NUMPIXELS;j++)
    {
      pixels[i].setPixelColor(j, pixels[i].Color(r, g, b));
      pixels[i].show();
    }
  }
}


void setup()
{
  Serial.begin(9600);

  pinMode(ESTOP_BUTTON_PIN, INPUT);

  // Neopixel initalize
  for (int i = 0; i < pixels_n; i++)
  {
    pixels[i].begin();
    pixels[i].setBrightness(BRIGHTNESS);
    pixels[i].clear();
    pixels[i].show();
  }
}


void loop()
{
  bool estop_state = !digitalRead(ESTOP_BUTTON_PIN);

  if (estop_state == true && millis() - pre_saver_time < SAVER)
    state = 2;
  else if (millis() - pre_time > INTERVAL)
  {
    pre_time = millis();
    if (estop_state == true) state = 2;
    else state = 1;
  }
  else 
    state = 0;

  // Update estop param
  if (estop_state == false) pre_saver_time = millis();
  else if(pre_estop_state == false) pre_saver_time = millis();
  pre_estop_state = estop_state;
  
  
  // State execution
  if (state != pre_state)
  {
    pre_state = state;
    switch(state)
    {
      case 0:
      writePixels(pixels, 0, 0, 0);    // Turn-off
      break;
      case 1:
      writePixels(pixels, 0, 0, 255);  // normal (blue)
      break;
      case 2:
      writePixels(pixels, 255, 0, 0);  // EStop (red)
      break;
    }
    Serial.println(state);
  }
}
