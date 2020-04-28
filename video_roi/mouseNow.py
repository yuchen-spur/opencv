import pyautogui
try:
    while 1:
        x,y=pyautogui.position()
        im=pyautogui.screenshot()
        RGB=im.getpixel((x,y))
        strs='X:'+str(x)+' '+'Y:'+str(y)+'     '+'RGB:'+str(RGB)+' '*6     
        print(strs,end='')
        print('\b'*len(strs),end='',flush=True)
except KeyboardInterrupt:
    print('\nDone')
    
