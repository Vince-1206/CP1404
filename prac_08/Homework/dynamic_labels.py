from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Simple Kivy app to dynamically create labels from a list of names."""

    def __init__(self, **kwargs):
        """Initialize the app with a list of names."""
        super().__init__(**kwargs)
        # List of names (our data/model)
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

    def build(self):
        """Build the Kivy GUI by dynamically creating labels."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        # Create and add labels for each name
        for name in self.names:
            temp_label = Label(text=name, font_size=24)  # Create a label with the name
            self.root.ids.main.add_widget(temp_label)  # Add it to the 'main' BoxLayout
        return self.root


DynamicLabelsApp().run()