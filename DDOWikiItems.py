import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import numpy as np
from lxml import html
import lxml.html as lh
import re
import argparse

def get_soup(url):
    session = requests.Session()
    html = session.get(url)
    return bs(html.content, "html.parser")

def get_all_tables(soup):
    return soup.find_all("table")

def get_table_rows(table):
    rows = []
    for tr in table.find_all("tr")[1:]:
        cells = []
        tds = tr.find_all("td")
        for td in tds:
            lastcounter = 0
            tdstr = re.search('([0-9a-zA-Z\:\-\%\(\)\.,\+\'\s]+[<])', str(td))
            if tdstr is None:
                tdstr = re.search('([>][0-9]+)', str(td))
                tdstr = tdstr.group()
                tdstr = tdstr.replace("<","")
                tdstr = tdstr.replace(">","")
                tdstr = tdstr.replace("\\","")
                tdstr = tdstr.replace("n","")
                cells.append(tdstr)
            else:
                tdstr = tdstr.group()
                tdstr = tdstr.replace("<","")
                tdstr = tdstr.replace(">","")
                if tdstr == "\n":
                    lis = td.find_all("li")
                    for li in lis:
                        li = re.search('([0-9a-zA-Z\:\-\%\(\)\.,\+\'\s]+[<])', str(li))
                        if li is None:
                            cells.append("wowie")
                        else:
                            li = li.group()
                            li = li.replace("<","")
                            li = li.replace(">","")
                            if "Augment Slot" in li and lastcounter == 0:
                                li = "Augment Slot"
                                lastcounter = 1
                            if len(cells) == 3:
                                li = li.lstrip()
                                cells.append(li)
                            elif len(cells) >= 3 and lastcounter == 0:
                                if cells[3] is not None:
                                    li = li.lstrip()
                                    cells[3] += "\n"
                                    cells[3] += li   
                tdstr = tdstr.replace("\xa0"," ")
                cells.append(tdstr)
        if len(cells) >= 4:
            try:
                while cells[4] == "wowie" or cells[4] == "\n":
                    cells.pop(4)
            except:
                return
        cells.pop(0)
        cells.pop(5)
        cells[3] = cells[3][:-1]
        rows.append(cells)
    return rows
def save_as_csv(folder, rows):
    pd.DataFrame(rows).to_csv(f"{folder}.csv", header=False, index=False)

def main(url):
    soup = get_soup(url)
    tables = get_all_tables(soup)
    print(f"[+] Found a total of {len(tables)} tables.")
    for i, table in enumerate(tables, start=1):
        rows = get_table_rows(table)
        table_name = f"table-{i}"
        print(f"[+] Saving {table_name}")
        save_as_csv(folder, rows)



parser = argparse.ArgumentParser()
parser.add_argument('-u', action='store', dest='siteurl',
                    help='Sets the URL to fetch from.')

parser.add_argument('-p', action='store', dest='filepath',
                    help='Sets the file path and/or filename. Note: file extension already included.')

arguments = parser.parse_args()

folder = arguments.filepath
url = arguments.siteurl

main(url)