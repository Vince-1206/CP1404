from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class BoxLayoutDemo(BoxLayout):
    pass

class BoxLayoutApp(App):
    def build(self):
        return BoxLayoutDemo()

    def handle_greet(self):
        print("greet")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = ''

if __name__ == '__main__':
    BoxLayoutApp().run()
