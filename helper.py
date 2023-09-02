from enum import Enum
import os
import pickle


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def save_data(data, file_path='market.pkl'):
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)


def load_data(file_path='market.pkl'):
    try:
        with open(file_path, 'rb') as file:
            return (pickle.load(file))
    except FileNotFoundError:
        return []

class MarketActions(Enum):
    Print_Market = 0
    Add_To_Cart = 1
    Show_Cart = 2
    Finish_shopping = 3
    Exit = 4

class Product:
    def __init__(self, name, price, stock = 10) -> None:
        self.name = name
        self.price = price
        self.stock = stock

    def buy(self, quantity=1):
        if(self.stock > 0):
            if(self.stock - quantity > 0):
                self.stock-=quantity
                return True
        return False
    
    def returned(self):
        self.stock+=1

    def __str__(self) -> str:
        return f'{self.name} [{self.price}$] | {self.stock}'