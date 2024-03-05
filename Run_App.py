from interfaces import Cmd_Interface, Graphic_Interface
import time

to_run = int(input("Chose: 1 = Run cmd interface 2 = Run graphic interface: "))
if to_run == 1:
    print("Start cmd interface...")
    Cmd_Interface.launch()
elif to_run == 2:
    print("Start graphic interface...")
    print("Sorry graphic interface is in build :(")
    #if __name__ == '__main__':
    #    Graphic_Interface.launch()

print("The app have been closed. Bye ! :)")
print("Program will finish in 3 seconds")
time.sleep(3)