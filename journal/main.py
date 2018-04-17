from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout


#Represents a general area where hiking has occured
class Map(RelativeLayout):

    #Add map image to map
    def set_map_image(self, image_path):
        self.image_path = image_path


class JournalApp(App):
    def build(self):
        map = Map()
        map.set_map_image('images/TestMap.png')
        return map

if __name__ == '__main__':
    JournalApp().run()
