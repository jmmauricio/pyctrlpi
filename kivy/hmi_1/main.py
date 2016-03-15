# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 00:06:52 2016

@author: jmmauricio
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock


class HMI(Widget):
    eta_d_label = ObjectProperty(None)
    slider_d = ObjectProperty(None)
    #slider_eta_q = ObjectProperty(None)
    p_gauge  = ObjectProperty(None)
    
    def update(self, dt):
        pass

    
    def on_touch_move(self, touch):
       
        self.eta_d_label.text = '{:2.3f}'.format(self.sld_d.value)
        self.eta_q_label.text = '{:2.3f}'.format(self.sld_q.value)
 
        
class Ctrl_guiApp(App):
    def build(self):
        hmi = HMI()
        #g = Gauge(size_hint=(1, 2),id='gau')
        #game.add_widget(g)
        
        Clock.schedule_interval(hmi.update, 1.0 / 60.0)
        return hmi


if __name__ == '__main__':
    Ctrl_guiApp().run()