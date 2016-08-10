### Author: emuboy
### Description: A Test app for the NeoPixel LED
### Category: Other
### License: MIT
### Appname: NeoPixTest

import ugfx, pyb, buttons ,machine , time 

#init
ugfx.init()
ugfx.clear()
buttons.init()
ugfx.set_default_font(ugfx.FONT_SMALL)
pin = machine.Pin("PB13", machine.Pin.OUT)
neo = pyb.Neopix(pin)

#vars
colors = 0x000000
old_color = 0x000001
R_value = 0x00
G_value = 0x00 
B_value = 0x00 
    

while True:
    #Read inputs and manipulate the color

    if buttons.is_pressed("JOY_LEFT"):
        R_value = R_value - 1    
        
        if(R_value < 0):
            R_value = 0   
    
    if buttons.is_pressed("JOY_RIGHT"):
        R_value = R_value + 1
        
        if(R_value > 255):
            R_value = 255    
    
    if buttons.is_pressed("BTN_A"):
        G_value = G_value - 1      
        
        if(G_value < 0):
            G_value = 0        
    
    if buttons.is_pressed("BTN_B"):
        G_value = G_value + 1

        if(G_value > 255):
            G_value = 255

    if buttons.is_pressed("JOY_DOWN"):
        B_value = B_value - 1      
        
        if(B_value < 0):
            B_value = 0 

    if buttons.is_pressed("JOY_UP"):
        B_value = B_value + 1
        
        if(B_value > 255):
            B_value = 255

    if buttons.is_triggered("BTN_MENU"):
        break;  

    #we put all the colors in one value for the NeoPixel

    color = (R_value << 16) | (G_value << 8) | B_value 

    #We tell to the NeoPixel to show the color
    neo.display(color)

    #we update the display only where is a change to avoid flickering 

    if(old_color != color):
        old_color = color    
        ugfx.clear(ugfx.html_color(0x7c1143))
        ugfx.text(1, 10, "NeoPixel LED Test ", ugfx.WHITE)
        ugfx.text(1, 30, "Press Menu to exit ", ugfx.WHITE)
        ugfx.text(1, 50, "Left/Right\tto change Red ", ugfx.WHITE)
        ugfx.text(1, 70, "A/B\tto change Green ", ugfx.WHITE)
        ugfx.text(1, 90, "Up/down\tto change Blue ", ugfx.WHITE)    
        ugfx.text(1, 110, "Red\tis: "+str(R_value)+" ", ugfx.WHITE)
        ugfx.text(1, 130, "Green\tis: "+str(G_value)+" ", ugfx.WHITE)
        ugfx.text(1, 150, "Blue\tis: "+str(B_value)+" ", ugfx.WHITE)


ugfx.clear()



