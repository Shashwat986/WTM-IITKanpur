# Lecture notes for my Python talk at Women Tech-Makers Group @ IIT Kanpur

### Reading Order/File Descriptions

So, this should help you understand what all these files are about so you can decide how to get around it.

* `notes1.py`, `notes2.py` : These files will explain the basic syntax of Python for newbies.
* `evolutionText.py` : This program uses a string, modified randomly to acheive a target text. It demonstrates strings and the `random` module.
* `hangman.py` : This program creates the Hangman game. Demonstrates strings, lists, functions, and conditions.
* `next_word_v0.py`, `next_word_v1.py` : This program processes a raw text corpus to store the words that come immediately after a target word, and return the most frequent next word. The `v0` version uses no external libraries and demonstrates dictionaries, loops, and, to some extent exceptions. The `v1` version uses built-in libraries to increase efficiency and readability, and demonstrates how to store variables in Python to files.
* `pi.py` : Calculates the value of PI up to different degrees of accuracy using a recurrence relation. Demonstrates the `math` module, functions, and loops.
* `plot.py` : A simple example program for the `matplotlib` and `pyplot` libraries.
* `reddit.py` : This program accesses the `http://www.reddit.com/r/todayilearned` page and displays a randomly-selected submission. Demonstrates web-scraping using the `requests` module, JSON parsing, and `random`.
* `sql.py` : Demonstrates how the `sqlite3` module can allow us to create an SQL table in our database and execute queries on it.
* `tk.py` : Demonstrates how to use the `Tkinter` module to make Graphical interfaces in Python.
* `wiki.py` : This program gets a random Wikipedia page using Special:Random, and uses the BeautifulSoup module to access the title of the page. It then allows the user to open this page using his/her default web browser. Demonstrates web-scraping using the `requests` module, the `BeautifulSoup` module, and the `webbrowser` module.

### Clarifications:

`text8` dataset is a subset of the dataset available here:
http://mattmahoney.net/dc/textdata

`evolutionText.py` is taken from http://usingpython.com

`hangman.py` is taken from http://inventwithpython.com/chapter9.html

`pi.py` is taken from http://www.craig-wood.com/nick/articles/pi-archimedes/

`notes1.py` and `notes2.py` are inspired from http://www.learnxinyminutes.com/docs/python
Much of the text has been altered, however.

All other codes are written by *Shashwat Chandra*.

### Resources:

For someone interested in learning Python, I have found the following resources to be the most helpful:

* https://docs.python.org/2/tutorial/
* https://docs.python.org/2/index.html
* http://learnpythonthehardway.org/book/
* http://www.codecademy.com/en/tracks/python
* http://www.diveintopython.net/

For any specific modules (ex. `requests` or `BeautifulSoup`, look at the relevant documentation)
