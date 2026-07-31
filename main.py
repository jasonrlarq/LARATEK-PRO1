import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.label import Label
from android.permissions import request_permissions, Permission

class LaratekApp(App):
    def build(self):
        # Request necessary Android permissions at runtime
        request_permissions([Permission.CAMERA, Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])

        layout = BoxLayout(orientation='vertical')
        
        # Title Label
        self.label = Label(text="Laratek eBay Scanner", size_hint=(1, 0.1))
        layout.add_widget(self.label)
        
        # Camera Widget (shows live feed)
        self.cam = Camera(play=True, resolution=(640, 480), size_hint=(1, 0.7))
        layout.add_widget(self.cam)
        
        # Capture Button
        btn = Button(text="Capture Item Photo", size_hint=(1, 0.2))
        btn.bind(on_press=self.capture_photo)
        layout.add_widget(btn)
        
        return layout

    def capture_photo(self, instance):
        filename = f"/sdcard/Download/ebay_item_{int(time.time())}.png"
        self.cam.export_to_png(filename)
        self.label.text = f"Saved photo to Downloads!"

if __name__ == '__main__':
    LaratekApp().run()
