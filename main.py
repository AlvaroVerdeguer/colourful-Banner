#reg add HKEY_CURRENT_USER\Console /v VirtualTerminalLevel /t REG_DWORD /d 0x00000001 /f

colors = {\
    'OKBLUE' : '\033[94m',
    'OG' : '\033[92m',
    'W' : '\033[93m',
    'RED' : '\033[1;31;40m',
    'R' : '\033[0m', #reset
}

def colorText(text):
    for color in colors:
        text = text.replace("[[" + color + "]]", colors[color])
    return text



banner='''                                                                
                                                                    
                                                                    
[[OG]] GREEN [[OG]] [[W]] WARNING [[R]]

'''
                                                                                                               

             
print(colorText(banner))

