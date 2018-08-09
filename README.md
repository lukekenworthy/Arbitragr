# Arbitragr
A quick little program to find currency exchange arbitrage opportunities given a list of currencies to trade. With a cool -r ending for some Web 2.0 flair!

## Explain yourself:
This program uses the Requests library and BeautifulSoup to parse the informtion on [x-rates.com](https://x-rates.com) to create a currency exchange table and then searches that table for arbitrage opportunities. 
It uses a recursive, brute-force searching algorithm that runs in O(n!) time, which is obviously not optimal but I just wanted to see if I could do this. To optimize it in the future, I could use a [Bellman-Ford algorithm](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm) to get it to run in O(n<sup>3</sup>) time.

## Disclaimer:
This program was designed for fun. It doesn't use an API because all of the currency exchange APIs are either slow or cost money. Thus, it uses webscraping and the currency-exchange rates are not commercial-grade. It also doesn't account for trading fees, though that would not be a hard addition to make. That said, if you find an arbitrage opportunity of 5% or something like that, you should totally take it. However, the highest I have been able to find is around .01%. 
Also, since it uses a brute-force algorithm, it gets really slow around more than 10 currencies.

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