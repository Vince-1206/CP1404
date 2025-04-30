"""
CP1404 Week 11 Workshop - GUI program to convert miles to kilometres
Lindsay Ward, IT@JCU
06/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934  # Constant for conversion

class MilesConverterApp(App):
    """MilesConverterApp is a Kivy App for converting miles to kilometres"""
    output_text = StringProperty("0.0")

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """Handle conversion from miles to kilometers"""
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.output_text = str(result)

    def handle_increment(self, change):
        """Handle up/down button press, update input and calculate"""
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        """Convert text input to float, return 0 if invalid"""
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0

MilesConverterApp().run()

MilesConverterApp().run()
