import os
import time
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from android.permissions import request_permissions, Permission

class LaratekApp(App):
    def build(self):
        # Request required permissions at runtime
        request_permissions([
            Permission.CAMERA, 
            Permission.WRITE_EXTERNAL_STORAGE, 
            Permission.READ_EXTERNAL_STORAGE
        ])

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Title
        self.label = Label(text="Laratek eBay Price Checker", size_hint=(1, 0.08))
        layout.add_widget(self.label)
        
        # Camera Feed
        self.cam = Camera(play=True, resolution=(640, 480), size_hint=(1, 0.5))
        layout.add_widget(self.cam)
        
        # Keyword input for search query
        self.search_input = TextInput(text='Enter search keyword', multiline=False, size_hint=(1, 0.1))
        layout.add_widget(self.search_input)
        
        # Action Button
        btn = Button(text="Snap Photo & Check eBay Price", size_hint=(1, 0.15))
        btn.bind(on_press=self.process_item)
        layout.add_widget(btn)
        
        # Results Display
        self.result_label = Label(text="Results will appear here...", size_hint=(1, 0.17))
        layout.add_widget(self.result_label)
        
        return layout

    def process_item(self, instance):
        # 1. Save photo to accessible public storage path
        try:
            storage_path = "/sdcard/Pictures/Laratek"
            if not os.path.exists(storage_path):
                os.makedirs(storage_path, exist_ok=True)
            filename = os.path.join(storage_path, f"item_{int(time.time())}.png")
            self.cam.export_to_png(filename)
            self.result_label.text = "Photo saved to Pictures/Laratek! Querying eBay..."
        except Exception as e:
            self.result_label.text = f"Save error: {str(e)}"
            return

        # 2. Trigger eBay API Request logic
        query = self.search_input.text
        self.fetch_ebay_pricing(query)

    def fetch_ebay_pricing(self, keyword):
        # Framework ready for your eBay Browse API integration
        # api_url = f"https://api.ebay.com/buy/browse/v1/item_summary/search?q={keyword}"
        # headers = {"Authorization": "Bearer YOUR_EBAY_OAUTH_TOKEN"}
        
        # Placeholder response loop for verification
        self.result_label.text = f"Searched eBay for '{keyword}': Avg Price: $--.--"

if __name__ == '__main__':
    LaratekApp().run()
