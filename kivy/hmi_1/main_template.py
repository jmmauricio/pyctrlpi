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
from kivy.garden import gauge


class PongGame(Widget):
    p_value = ObjectProperty(None)
    p_slider = ObjectProperty(None)
    p_gauge  = ObjectProperty(None)
    
    def update(self, dt):
        pass

    
    def on_touch_move(self, touch):
       
        print(Widget.children)
        self.p_val.text = '{:2.3f}'.format(self.p_sld.value)
        self.p_gau.value =self.p_sld.value
        
class PongApp(App):
    def build(self):
        game = PongGame()
        #g = Gauge(size_hint=(1, 2),id='gau')
        #game.add_widget(g)
        
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    PongApp().run()