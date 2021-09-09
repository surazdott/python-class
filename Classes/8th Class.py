f = open('file.text', 'w')

# Write replace the all the text
f.write('Ths is the text written through python.\nPython is awesome.')

f = open('file.text', 'r')

import webbrowser

search = input("Search: ")
webbrowser.open(f"https://www.youtube.com/results?search_query={search}")
