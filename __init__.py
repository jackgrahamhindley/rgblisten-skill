from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler, intent_file_handler
from mycroft.util import LOG
from requests import post
import time
from pixel_ring import pixel_ring
from gpiozero import LED

power = LED(5)
power.on()

pixel_ring.set_brightness(10)


class Rgblisten(MycroftSkill):
    def __init__(self):
        super(Rgblisten, self).__init__(name="Rgblisten")
        
    def initialize(self):
        self.add_event('recognizer_loop:record_begin', self.record_begin_handler)
        

    def record_begin_handler(self, message):
        pixel_ring.wakeup()
        time.sleep(2)
        pixel_ring.think()
        time.sleep(2)
        pixel_ring.speak()
        time.sleep(3)
        pixel_ring.off()
        time.sleep(2)
        pixel_ring.off()

    
def create_skill():
    return Rgblisten()
