import sys

import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('en')
val = input("Enter the page name to be searched....")
val2 = val.replace(" ", "_")
page_link = wiki_wiki.page(val2)

availability = (page_link.exists())
if availability:
    wikilink = (page_link.fullurl)
    f = open("links.txt",  "r")
    if wikilink in f.read():
        print("The link for this page already exists..")
    else:
        file1 = open("links.txt", "a")  # append mode
        file1.write(wikilink + "\n")
        file1.close()
        print("The link for this page added succesfully")
else:
    print("This wikipedia page does not exist..")

