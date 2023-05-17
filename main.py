PTLL = lambda filex : __import__('pivottablejs').pivot_ui(__import__('pandas').read_csv(filex)) and __import__('webbrowser').open('pivottablejs.html')
PTLL('example.csv')