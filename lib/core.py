#Import
import os



def Banner():

    print("""
    
    
                     Payload Generator Script 
        
                        Named : 'AccessMe'
            
        This program will be used as part of a security audit
    
                         Version : 1.0.0
                          
                          
    """)



def Clear():
    os.system("clear")



def Bad_Choice():
    print("Bad choice !!! Try again\n")



def core_input():
    Input = input("Enter you choice : ")
    return Input



def core_input_pass():
    Input = input("Press any key to continue.")
    return Input



def Exit_Program():
    Clear()
    print("Exiting...")
    os.system("exit")



def Module_Choice():
    print("""
 |----------------------|
 | [1] Windows Stagers; |
 | [0] Exit Software;   |
 |----------------------|
    """)



def Windows_Arch_Choice():
    print("""
 |------------------|
 | [1] x86 Stagers; | 
 | [2] x64 Stagers; |
 | [0] Back;        |
 |------------------|
    """)



def x86_Windows_Stager_Choice():
    print("""
 |------------------------------------------------|
 | [1] Windows x86 Meterpreter Reverse TCP   (C); |
 | [2] Windows x86 Meterpreter Reverse HTTP  (C); |
 | [3] Windows x86 Meterpreter Reverse HTTPS (C); |
 | [0] Back;                                      |
 |------------------------------------------------|      
    """)



def x64_Windows_Stager_Choice():
    print("""
 |------------------------------------------------|
 | [1] Windows x64 Meterpreter Reverse TCP   (C); |
 | [2] Windows x64 Meterpreter Reverse HTTP  (C); |
 | [3] Windows x64 Meterpreter Reverse HTTPS (C); |
 | [0] Back;                                      |
 |------------------------------------------------| 
    """)



def x86_Windows_Features():
    print("""
 |----------------------------------------------|
 | Decoil   : Memory Alloc, Waiting Time;       |
 | Junkcode : Friendly Function;                |
 | Evasion  : Check VM, OS, Language;           |
 | Language : Adding foreign language comments; |
 |----------------------------------------------|
    """)



def x64_Windows_Features():
    print("""
 |----------------------------------------------|
 | Decoil   : Memory Alloc, Waiting Time;       |
 | Junkcode : Friendly Function;                |
 | Evasion  : Check VM, OS, Language;           |
 | Language : Adding foreign language comments; |
 |----------------------------------------------|
    """)