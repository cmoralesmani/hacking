#!/usr/bin/env python
#_*_ coding: utf8 _*_
import mechanize
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--buscar', help="Opción a buscar")
parser = parser.parse_args()

def main():
    if parser.buscar:
        bus = mechanize.Browser()
        # Para evitar el seguimiento de robots.txt
        bus.set_handle_robots(False)
        bus.set_handle_equiv(False)
        bus.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36')]
        bus.open("https://www.google.com")

        # for n in bus.forms():
        #     print(n)

        bus.select_form(nr=0)
        bus['q'] = parser.buscar
        bus.submit()
        # print(bus.response().read())
        p = BeautifulSoup(bus.response().read(), 'html5lib')
        for link in p.find_all('a'):
            # print(link.get('href'))
            u = str(link.get('href'))
            u = u.replace('/search?q=', '')
            print(u)
    else:
        print("Palabra a buscar")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo...")
        exit()