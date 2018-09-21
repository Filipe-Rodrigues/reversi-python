from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.modules._webdebugger import background_jpg


class Board(GridLayout):

    def __init__(self, **kwargs):
        super(Board, self).__init__(**kwargs) 
        self.cols = 8     
        self.rows = 8   
        # rows_cols = [self.rows][self.cols]
        self.padding = 40
        self.spacing = 2
        self.row_default_height = 80
        self.col_default_width = 80
        self.col_force_default = True     
        list_of_buttons = []
        image_behavior = ImageButton()    
        
        for i in range(64):
            button = Button(text = ' ', size=(80, 80), background_normal="Images//empty.png")
            list_of_buttons.append(button)

        for i in range(self.cols * self.rows):
            self.add_widget(list_of_buttons[i])
            image_behavior.on_press()
        # self.change_board()
            
    def change_board(self):
        self.clear_widgets()
           
        for i in range(63):
            self.add_widget(Image(source=("Images//empty.png"), allow_stretch=True, keep_ratio=False))
  
        self.add_widget(Image(source=("Images//black0.png"), allow_stretch=True, keep_ratio=False), 33, None)      

            
class CompleteWindow(FloatLayout, ButtonBehavior):

    def __init__(self, **kwargs):
        super(CompleteWindow, self).__init__(**kwargs)
        gl = Board()
        self.orientation = 'horizontal'
        btn_new_game = Button(text='New Game', size_hint=(.20, .12), pos=(950, 500))
        btn_easy = Button(text='Easy', size_hint=(.10, .12), pos=(950, 410))
        btn_hard = Button(text='Hard', size_hint=(.10, .12), pos=(1088, 410))
        btn_player_x_player = Button(text='Player x Player', size_hint=(.20, .12), pos=(950, 320))
        btn_player_x_computer = Button(text='Player x Computer', size_hint=(.20, .12), pos=(950, 230))
        btn_computer_x_computer = Button(text='Computer x Computer', size_hint=(.20, .12), pos=(950, 140))
        self.add_widget(gl)
        self.add_widget(btn_new_game)
        self.add_widget(btn_easy)
        self.add_widget(btn_hard)
        self.add_widget(btn_player_x_player)
        self.add_widget(btn_player_x_computer)
        self.add_widget(btn_computer_x_computer)


class ImageButton(ButtonBehavior):

    def __init__(self):
        super(ImageButton, self).__init__
        
    def on_press(self):
        print("pressed")


class MyApp(App):

    def build(self):
            return CompleteWindow()


if __name__ == '__main__':
    MyApp().run()