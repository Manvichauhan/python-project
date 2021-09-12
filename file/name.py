with open(".vscode/file/manvi.txt",'r') as f:
    a=f.read()
print(a)
if 'MANVI' in a:
    print("name is present")
else:
    print("name is not present")