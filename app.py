# product in grocery (name, price, stock)
# method to add data
# print all products
# method to buy (which product, quantity) - add to cart
# print cart - sum prices, and quantity (description)
from helper import *
import logging

# Create a logger instance
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

# Create a handler and formatter
handler = logging.FileHandler('market_log.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# # Writing log messages
# logger.debug('This is a debug message')
# logger.info('This is an info message')
# logger.warning('This is a warning message')
# logger.error('This is an error message')
# logger.critical('This is a critical message')

# market = [
#     Product('milk', 7.99, 30),
#     Product('banana', 3.99, 20),
#     Product('apples', 5.89, 20),
#     Product('corn', 1.59, 30),
#     Product('water', 2.39, 50),
#     Product('ham', 10.99, 25),
#     Product('beef', 22.69, 20),
#     Product('choco', 2.99, 15),
#     Product('coffee', 1.99, 60)
# ]
market = []

def addProduct():
    market.append(Product(input('product name: '),float(input('product price: ')), int(input('product quantity: '))))

cart = [] #starts a new cart for each customer

def menu():
    global market
    while(True):
        for x in MarketActions:
            print(x.value, x.name)
        slc = MarketActions(int(input('select action: ')))
        if slc == MarketActions.Print_Market: printMarket()
        if slc == MarketActions.Add_To_Cart: addToCart()
        if slc == MarketActions.Show_Cart: showCart()
        if slc == MarketActions.Finish_shopping: 
            done()
            return
        if slc == MarketActions.Exit: 
            market = load_data()
            return

def printMarket():
    if market:    
        for i,prd in enumerate(market):
            print (i+1, prd)
        logger.info('tried printMarket(), printed all market products')
    else: 
        print('market has no products')
        logger.error('tried printMarket(), market has no products')

def addToCart():
    printMarket()
    slc = int(input('select product: '))
    quan = int(input('select quantity to buy: '))
    if cart:
        for p in cart: #in case existing in cart
            if(market[slc - 1].name == p.name): 
                res = market[slc - 1].buy(quan) #check if can buy
                if res: p.stock+=quan #if can buy, at quantity to existing product in cart
                else: 
                    print(f'We dont have {quan} in stock. you can buy up to {market[slc - 1].stock}')
                    logger.info(f'tried addToCart(), added quantity to existing product in cart')
                return
    #in case cart empty / if new product to existing cart
    res = market[slc - 1].buy(quan) #check if can buy
    if res: 
        cart.append(Product(market[slc - 1].name,market[slc - 1].price,quan)) #add new product to cart
        logger.info(f'tried addToCart(), added new product to cart')
    else: 
        print(f'We dont have {quan} in stock. you can buy up to {market[slc - 1].stock}')
        logger.error(f'tried addToCart(), no {quan} in stock for {slc} - only {market[slc - 1].stock}')

            
    

def showCart():
    if(cart):
        sumCart()
    else: 
        print('empty cart')
        logger.error('tried showCart(), cart has no products')


def done():
    if(cart):
        sumCart()
        input('would you like to finish your purchase?') 
        logger.info('tried done(), empty cart - finished shopping')
        return
    else: 
        print('empty cart')
        logger.error('tried done(), cart has no products')


def sumCart():
    sum = 0
    for prd in cart:
        print (prd)
        sum += (prd.price * prd.stock)
    print (f'Total: {sum}$')
    logger.info('tried sumCart(), printed all cart with summary of product prices')

if __name__=='__main__':
    market = load_data()
    menu()
    save_data(market)
