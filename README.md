# Arbitragr
A quick little program to find currency exchange arbitrage opportunities given a list of currencies to trade. With a cool -r name ending for some Web 2.0 flair!

## Explain yourself:
This program uses the Requests library and BeautifulSoup to parse the informtion on [x-rates.com](https://x-rates.com) to create a currency exchange table and then searches that table for arbitrage opportunities. 

## Disclaimer:
This program was designed for fun. It doesn't use an API because all of the currency exchange APIs are either slow or cost money. Thus, it uses webscraping and the currency-exchange rates are not commercial-grade. 

## How to use:
Download the file and its dependencies then fill the list of currencies in arbitragr.py with whatever currencies you want. It has to use a three-letter currency code that is accepted by [x-rates.com](https://www.x-rates.com/). The program will print ("Invalid matrix") if a code is not accepted. The codes also must be all-caps, though this could be easily modified if you just really wanted to write your currencies in lowercase with a line like 
```python
currencies = [c.upper() for c in currencies]
```
in the beginning of the definition of the find_arbitrage function. Once you fill in the list, just run
```bash
python arbitragr.py
```
and you're off to the races! 

I would highly recommend that you run this in a [venv](https://docs.python.org/3/library/venv.html) and then you can install all of the dependencies by running 
```bash
pip install -r requirements.txt
```

Hope you enjoy!
