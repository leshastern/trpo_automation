import os

def Decode_files(file_names):
    for name in file_names:
        with open(name, 'r') as bak:
            newname = name.replace('.bak', '')
            text = bak.readlines()
            with open(newname, 'w') as decoded:
                for line in text:
                    newline = ''
                    for symbol in line:
                        if symbol == '':
                            symbol == ''
                        elif symbol != '/n' and symbol != '/t' and symbol != '	':
                            symbol = chr(ord(symbol)-1)
                        newline = newline + symbol
                    decoded.write(newline + '\n')

def Finish(file_names):
    for name in file_names:
        os.unlink(name)

def Decode_config(config, names):
    with open(config, 'r') as bak:
            newname = config.replace('.bak', '')
            text = bak.readlines()
            with open(newname, 'w') as decoded:
                for line in text:
                    newline = line
                    for name in names:
                        if line.find(name) != -1:
                            newline = name + ' = ' + "'"
                            line = line.replace(newline, '')
                            line = line.replace("'", '')
                            for symbol in line:
                                if symbol == '':
                                    symbol == ''
                                elif symbol != '/n' and symbol != '/t' and symbol != '	':
                                    symbol = chr(ord(symbol)-1)
                                newline = newline + symbol
                            newline = newline[:-1]
                            newline = newline + "'"
                            names.remove(name)
                    decoded.write(newline + '\n')

