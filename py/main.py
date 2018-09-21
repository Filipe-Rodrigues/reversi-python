import kivy
kivy.require('1.8.0')
from kivy.app import App
from board import Board
from kivy.core.window import Window
from kivy.config import Config


__version__ = '1.0'


class TicTacToe(App):
    def build(self):
        Window.clearcolor = (.5, 0, 0, 1)
        Window.size = (600, 600)
        self.board = Board(cols=8)
        self.title = 'Velha'
        
        return self.board


if __name__ == '__main__':
    TicTacToe().run()