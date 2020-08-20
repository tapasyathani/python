import os
import pyttsx3
print("Welcome!")

pyttsx3.speak("hey! what can i do for you")
while True:
  
  print("hey! what can i do for you-- ", end='')
  p=input()

  if (("dont" not in p) and (("run" in p) or ("execute" in p) or ("start" in p) or ("open" in p) or("launch in p")) and ("not" not in p) and (("run" in p) or ("execute" in p) or ("start" in p) or ("open" in p)or ("launch" in p))): 
      if ("chrome" in p) or ("google" in p):
        pyttsx3.speak("opening chrome please wait")
        print("opening chrome please wait")
        os.system("chrome")
        
      elif("browser" in p):
         pyttsx3.speak("which browser you want to open")
         print("browser name ", end='')
         x=input()
         if ("chrome" in x) or ("google" in x):
           pyttsx3.speak("opening chrome please wait")
           os.system("chrome")
          
         elif("firefox" in x):
           pyttsx3.speak("opening firefox please wait")
           os.system("firefox")
          
         else:
           pyttsx3.speak("program is not supported by your computer")
           print("program is not supported by your computer")

      elif("firefox" in p):
        pyttsx3.speak("opening firefox please wait")
        print("opening firefox please wait")
        os.system("firefox") 

      elif("notepad" in p) or ("editor" in p):
        pyttsx3.speak("opening notepad please wait")
        print("opening notepad please wait")
        os.system("notepad")

      elif("calculator" in p) or("cal" in p):
        pyttsx3.speak("opening calculator please wait")
        print("opening calculator please wait")
        os.system("calc")

      elif("media" in p) and ("player" in p):
        pyttsx3.speak("opening meida player please wait")
        print("opening meida player please wait")
        os.system("wmplayer")
        
        
      elif("snipping" in p) and ("tool" in p):
        pyttsx3.speak("opening snipping tool please wait")
        print("opening snipping tool please wait")
        os.system("snippingtool")

      elif("paint" in p):
        pyttsx3.speak("opening paint please wait")
        print("opening paint please wait")
        os.system("mspaint")

      else:
        pyttsx3.speak("This program is not supported by your computer")
        print("dont support")
        
  elif("dont" in p) or ("not" in p):
     pyttsx3.speak("okay!")
   
  elif("exit" in p) or ("close" in p) or ("quit" in p):
      pyttsx3.speak("thank you!")
      break
                          
  else:
    pyttsx3.speak("please type correct statement")
    print("please type correct statement")
  

     



