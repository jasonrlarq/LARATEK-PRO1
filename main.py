import os
import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.label import Label
from android.permissions import request_permissions, Permission

class LaratekApp(App):
    def build(self):
        request_permissions([Permission.CAMERA])

        layout = BoxLayout(orientation='vertical')
        
        self.label = Label(text="Laratek eBay Scanner", size_hint=(1, 0.1))
        layout.add_widget(self.label)
        
        self.cam = Camera(play=True, resolution=(640, 480), size_hint=(1, 0.7))
        layout.add_widget(self.cam)
        
        btn = Button(text="Capture Item Photo", size_hint=(1, 0.2))
        btn.bind(on_press=self.capture_photo)
        layout.add_widget(btn)
        
        return layout

    def capture_photo(self, instance):
        # Save to the app's safe internal user data directory
        filename = os.path.join(self.user_data_dir, f"ebay_item_{int(time.time())}.png")
        self.cam.export_to_png(filename)
        self.label.text = f"Saved to app storage!"

if __name__ == '__main__':
    LaratekApp().run()
