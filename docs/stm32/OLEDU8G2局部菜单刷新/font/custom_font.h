#ifndef CUSTOM_FONT_H
#define CUSTOM_FONT_H
// #include "Arduino.h"

typedef struct 
{
    uint8_t *data;
    uint8_t width;
    uint8_t height;
}custom_font_t;





extern custom_font_t eF_10_14;
extern custom_font_t exte_font_10x12[];

#endif