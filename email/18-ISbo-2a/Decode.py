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

def Decode_config(config, names):
    with fileinput.FileInput(config, inplace=True, backup='.bak') as file:
        for line in file:
            newline = line
            for name in names:
                if line.find(name) != -1:
                    newline = name + ' = ' + "'"
                    line = line.replace(newline, '')
                    line = line.replace("'", '')
                    for symbol in line:
                        if symbol == '':
                            symbol == ''
                        else:
                            if symbol != '/n' and symbol != '/t' and symbol != '	':
                                symbol = chr(ord(symbol)-1)
                        newline = newline + symbol
                    newline = newline[:-1]
                    newline = newline + "'"
                    names.remove(name)
            print(newline)
