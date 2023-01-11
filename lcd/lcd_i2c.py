from os import close
import RPi.GPIO as GPIO
import sys

from lcd.libs import I2C_LCD_driver

from logger.JournalLogger import Logger

GPIO.setmode(GPIO.BOARD)

log = Logger()

lcd = I2C_LCD_driver.lcd()
EMPTY_CONTENT="               "

class Lcd:
    def __init__(self, columns, lines):
        #log.info("Initializing LCD with {0} columns and {1} lines".format(columns, lines))
        self.columns = columns
        self.lines = lines

    def __del__(self):
        GPIO.cleanup()

    
    def clear():
        log.info("Clearing LCD")
        lcd.lcd_clear()
    

    def print(self, content, column, position, clear = False):
        try:
            if clear:
                clear()

            log.info("Printing text [{text}] at line [{line}] position [{position}]".format(text = content, line = column, position = position))
            lcd.lcd_display_string(EMPTY_CONTENT, column, 0)
            lcd.lcd_display_string(content, column, position)
        except:
            log.error("Error while printing text on screen: |{text}|".format(text = content))
            log.error(sys.exc_info()[0])
    
    def turn_on_backlight():
        log.info("Turning backlight on")
        lcd.backlight(1)

    def turn_off_backlight():
        log.info("Turning backlight off")
        lcd.backlight(0)
