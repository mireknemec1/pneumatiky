from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.utils import platform

# Nastavení oranžové barvy pozadí pro celé okno
Window.clearcolor = (1, 0.5, 0, 1)

class MainApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical', spacing=10)
        
        # Horní lišta
        top_bar = BoxLayout(size_hint_y=0.1, padding=5)
        
        left_button = Button(text=".", size_hint_x=0.2)
        center_label = Label(text="PNEUMATIKY", size_hint_x=0.6, color=(1,1,1,1), font_size='20sp') # Bílý text
        right_button = Button(text=".", size_hint_x=0.2)
        
        top_bar.add_widget(left_button)
        top_bar.add_widget(center_label)
        top_bar.add_widget(right_button)
        
        root.add_widget(top_bar)
        
        # Obrázek
        image_container = BoxLayout(size_hint_y=0.7, padding=0)  # Nastaveno padding=0
        with image_container.canvas.before:
            Rectangle(source='hlavni.jpeg', size=image_container.size, pos=image_container.pos)
        image_container.bind(size=self._update_rect, pos=self._update_rect)
        root.add_widget(image_container)
        
        # Dolní část s čtyřmi tlačítky
        if platform == 'android':
            # Rozložení pro Android: 2 tlačítka vedle sebe a další 2 pod nimi
            bottom_buttons = BoxLayout(size_hint_y=0.5, orientation='vertical', spacing=10, padding=10)  # Změněno na 0.3
            
            top_row = BoxLayout(size_hint_y=0.5, spacing=10)    # Přidáno spacing=10 mezera mezi tlačitky dole
            button1 = Button(text="Tlačítko 1")
            button2 = Button(text="Tlačítko 2")
            top_row.add_widget(button1)
            top_row.add_widget(button2)
            
            bottom_row = BoxLayout(size_hint_y=0.5, spacing=10)  # Přidáno spacing=10 mezera mezi tlačitky dole
            button3 = Button(text="Tlačítko 3")
            button4 = Button(text="Tlačítko 4")
            bottom_row.add_widget(button3)
            bottom_row.add_widget(button4)
            
            bottom_buttons.add_widget(top_row)
            bottom_buttons.add_widget(bottom_row)
        else:
            # Rozložení pro ostatní platformy: všechna tlačítka vedle sebe
            bottom_buttons = BoxLayout(size_hint_y=0.2, spacing=10, padding=10)
            button1 = Button(text="Tlačítko 1")
            button2 = Button(text="Tlačítko 2")
            button3 = Button(text="Tlačítko 3")
            button4 = Button(text="Tlačítko 4")
            bottom_buttons.add_widget(button1)
            bottom_buttons.add_widget(button2)
            bottom_buttons.add_widget(button3)
            bottom_buttons.add_widget(button4)
        
        root.add_widget(bottom_buttons)
        
        return root

    def _update_rect(self, instance, value):
        instance.canvas.before.clear()
        with instance.canvas.before:
            Rectangle(source='hlavni.jpeg', size=instance.size, pos=instance.pos)

if __name__ == '__main__':
    MainApp().run()
