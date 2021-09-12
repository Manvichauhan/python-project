with open(".vscode/file/manvi.txt",'r') as f:
    a=f.read()
print(a)

with open(".vscode/file/manvi.txt",'a') as f:
    a=f.write('hello itm')
print(a)
with open(".vscode/file/manvi.txt",'r') as f:
    a=f.read()
print(a)