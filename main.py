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
        root = BoxLayout(orientation='vertical', spacing=0)   # Nastaveno spacing = okraje kolem butonů, obrázku dole
        
        # Horní lišta
        top_bar = BoxLayout(size_hint_y=0.1, padding=5)  # Nastaveno padding = okraje kolem butonů na horní liště
        
        # Změna tlačítka na ikonu ozubeného kolečka
        left_button = Button(background_normal='settings6.png', size_hint_x=0.12, background_color=(1, 1, 1, 1))
        
        center_label = Label(text="PNEUMATIKY.CZ", size_hint_x=0.6, color=(1,1,1,1), font_size='18sp', bold=True) # Bílý text, tučně

        right_button = Button(background_normal='info2.png', size_hint_x=0.14, background_color=(1, 1, 1, 1))
        
        top_bar.add_widget(left_button)
        top_bar.add_widget(center_label)
        top_bar.add_widget(right_button)
        
        root.add_widget(top_bar)
        
        # Obrázek
        image_container = BoxLayout(size_hint_y=0.7, padding=0)  # Nastaveno padding=0 okraje
        with image_container.canvas.before:
            Rectangle(source='hlavni.jpeg', size=image_container.size, pos=image_container.pos)
        image_container.bind(size=self._update_rect, pos=self._update_rect)
        root.add_widget(image_container)
        
        # Dolní část s čtyřmi tlačítky
        if platform == 'android':
            # Rozložení pro Android: 2 tlačítka vedle sebe a další 2 pod nimi
            bottom_buttons = BoxLayout(size_hint_y=0.5, orientation='vertical', spacing=5, padding=0)  #spacing je mezera vodorovná mezi butony, 
            
            top_row = BoxLayout(size_hint_y=0.5, spacing=5)    # Přidáno spacing=5 mezera mezi tlačitky
            button1 = Button(text="Servisy", background_color=(0.5, 0.5, 0.5, 1), bold=True)
            button2 = Button(text="Pneumatiky", background_color=(0.5, 0.5, 0.5, 1), bold=True)
            top_row.add_widget(button1)
            top_row.add_widget(button2)
            
            bottom_row = BoxLayout(size_hint_y=0.5, spacing=5)  # Přidáno spacing=5 mezera mezi tlačitky
            button3 = Button(text="Pomoc", background_color=(0.5, 0.5, 0.5, 1), bold=True)
            button4 = Button(text="Rádce", background_color=(0.5, 0.5, 0.5, 1), bold=True)
            bottom_row.add_widget(button3)
            bottom_row.add_widget(button4)
            
            bottom_buttons.add_widget(top_row)
            bottom_buttons.add_widget(bottom_row)
        else:
            # Rozložení pro ostatní platformy: všechna tlačítka vedle sebe
            bottom_buttons = BoxLayout(size_hint_y=0.2, spacing=10, padding=10)
            button1 = Button(text="Tlačítko 1", background_color=(0.5, 0.5, 0.5, 1))
            button2 = Button(text="Tlačítko 2", background_color=(0.5, 0.5, 0.5, 1))
            button3 = Button(text="Tlačítko 3", background_color=(0.5, 0.5, 0.5, 1))
            button4 = Button(text="Tlačítko 4", background_color=(0.5, 0.5, 0.5, 1))

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
