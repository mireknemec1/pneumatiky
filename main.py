from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.utils import platform

# Nastavení oranžové barvy pozadí pro celé okno
Window.clearcolor = (1, 0.6, 0, 1)

class MainApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical', spacing=0)   # Nastaveno spacing = okraje kolem butonů, obrázku dole
        
        # Horní lišta
        top_bar = BoxLayout(size_hint_y=0.12, padding=5)  # Nastaveno padding = okraje kolem butonů na horní liště
        
        # Změna tlačítka na ikonu ozubeného kolečka
        left_button = Button(background_normal='settings6.png', size_hint_x=0.13, background_color=(1, 1, 1, 1))
        
        center_label = Label(text="PrezutiZdarma.CZ", size_hint_x=0.6, color=(0.65, 0.1, 0, 1), font_size='20sp', bold=True)  # Bílý text, tučně

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
            bottom_buttons = BoxLayout(size_hint_y=0.5, orientation='vertical', spacing=5, padding=0)  #spacing je mezera vodorovná mezi butony, 

            button1 = Button(text="PNEUMATIKY E-SHOP", background_color=(0.5, 0.5, 0.5, 1), bold=False, size_hint_y=0.25, font_size='18sp')
            button2 = Button(text="Pneuservisy ZDARMA", background_color=(0.5, 0.5, 0.5, 1), bold=False, size_hint_y=0.25, font_size='18sp')
            button3 = Button(text="Doporuč a ZÍSKÁVEJ", background_color=(0.5, 0.5, 0.5, 1), bold=False, size_hint_y=0.25, font_size='18sp')
            button4 = Button(text="Rady Tipy Pomoc", background_color=(0.5, 0.5, 0.5, 1), bold=False, size_hint_y=0.25, font_size='18sp')


            bottom_buttons.add_widget(button1)
            bottom_buttons.add_widget(button2)
            bottom_buttons.add_widget(button3)
            bottom_buttons.add_widget(button4)

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
