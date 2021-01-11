import os, sys, time

print("#-------------------------------------#")
print("[+] Python to exe By : NumeX")
print("[+] Github : https://github.com/NumeXx")
print("#-------------------------------------#\n")
plh = input("[1] Without Icon\n[2] With Icon\n#--> : ")
if plh == "1":
    fname = input("[/] Enter File Name (Must 1 directory with this tools & Must .py File) : ")
    time.sleep(1)
    os.system(f"pyinstaller -F {fname}")
    time.sleep(1)
    print("Successfully...")
    os.system("cls || clear")
    input("Enter any key for close....")
elif plh == '2':
    fname1 = input("[/] Enter File Name (Must 1 directory with this tools & Must .py File) : ")
    pico = input('[/] Enter icon PATH (Must .ico File) - (EX - "C:\picture.ico"): ')
    time.sleep()
    os.system(f"pyinstaller -F -i {pico} {fname1}")
    time.sleep(1)
    print("Successfully...")
    os.system("cls || clear")
    input("Enter any key for close....")
else:
    print("[x] Wrong input...")
    input("Enter any key for close....")