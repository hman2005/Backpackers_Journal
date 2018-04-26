from kivy.config import Config
Config.set('input', 'mouse', 'mouse,disable_multitouch')

from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.button import Button
from kivy.uix.bubble import Bubble

class MarkerSelect(Bubble):
    pass

#Represents a general area where hiking has occured
class Map(Scatter):

    #Add map image to map
    def set_map_image(self, image_path):
        self.image_path = image_path

    #Create marker on right click (button placeholder for now)
    def on_touch_up(self, touch):
        if touch.button == 'right':
            mkr_select = MarkerSelect()
            mkr_select.pos = [touch.x, touch.y]
            self.add_widget(mkr_select)
            #print("Merp")

class JournalApp(App):
    def build(self):
        map = Map()
        map.set_map_image('images/TestMap.png')
        return map

if __name__ == '__main__':
    JournalApp().run()
