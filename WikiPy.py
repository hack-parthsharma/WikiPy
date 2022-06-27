from tkinter import *
from tkinterhtml import *
import sys
import requests
import json

class WikiPy:
    def __init__(self):

        # figlet used for ASCII

        icon = open('icon.txt', 'r')
        
        icon_contents = icon.read()

        print(icon_contents)

        icon.close()

        word = ""

        if len(sys.argv) < 2:
            print("ERROR: Syntax : python3 WikiPy.py WORD_FOR_SEARCH")
            return
        else:
            word = " ".join(sys.argv[1:])

        # Wikipedia API URL : https://en.wikipedia.org/w/api.php?action=query&list=search&format=json&srsearch=WORD

        API_URL = "https://en.wikipedia.org/w/api.php?action=query&list=search&format=json&srsearch=" + word

        response = requests.get(API_URL).text
        data = json.loads(response)

        query = data["query"]

        resultArray = query["search"]

        self.titles = []
        self.descs = []

        for element in resultArray:
            self.titles.append(element["title"])
            self.descs.append(element["snippet"])
        
        print("Showing the results window ...")

        root = Tk()

        root.title("WikiPy: Results")
        root.geometry("500x500")

        self.resultsList = Listbox(root, selectmode = SINGLE, width = 60, height = 20)

        # Showing titles in the listbox

        for i,j in enumerate(self.titles):
            self.resultsList.insert(i,j)

        # The listbox will change the description frame when you change selection

        self.resultsList.bind('<<ListboxSelect>>', self.onSelect)

        # The listbox will select the first item

        self.resultsList.selection_set(0)
        
        self.descFrame = HtmlFrame(root, horizontal_scrollbar = "auto")

        # The HTML frame will show the first item's description

        self.descFrame.set_content(self.descs[0])
        
        self.resultsList.pack()
        self.descFrame.pack()

        root.mainloop()

    def onSelect(self, evt):
        
        widget = evt.widget
        index = int(widget.curselection()[0])
        desc = self.descs[index]
        
        self.descFrame.set_content(desc)

def main():
    WikiPy()

if __name__ == "__main__":
    main()
