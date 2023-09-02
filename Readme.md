# SuperMarket
    classes:
        -Product
    DataBase:
        -market.pkl
    Modules:
        -helper.py
    
    program to run a supermarket.
    each student has [ name, price, stock = 10 (if not provided, 10 in stock) ].
    when running program cart will be empty, you can add product to cart.
    the supermarket database won't be affected unless the user pays for his cart.

# Product Methods
    -buy - if available in stock, buy 1 product.
    -returned - return 1 product to stock.

# Main Supermarket Methods
    -Print Market
    -Add To Cart
    -Show Cart
    -Finish shopping

# Main Methods
    -Load at start
    -Save at end (if payed)