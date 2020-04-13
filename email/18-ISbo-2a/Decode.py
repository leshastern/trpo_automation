import fileinput
import os

def Decode_files(file_names):
    for name in file_names:
        with fileinput.FileInput(name, inplace = True, backup='.bak') as file:
            for line in file:
                newline = ''
                for symbol in line:
                    if symbol == '':
                        symbol == ''
                    else:
                        if symbol != '/n' and symbol != '/t' and symbol != '	':
                            symbol = chr(ord(symbol)-1)
                    newline = newline + symbol
                print(newline)

def Finish(file_names):
    for name in file_names:
        oldname = name
        newname = name.replace('.bak', '')
        os.unlink(newname)
        os.rename(oldname, newname)
