import pyttsx3
import os

print("chat with me with your requirement:",end='')
p=input()

if (("run" in p) or ("execute" in p)) and (("notepad" in p) or ("editor" in p)):
  os.system("notepad")

elif (("run" in p) or ("execute" in p)) and ("chrome" in p):
  os.system("chrome")

elif (("run" in p) or ("execute" in p)) and ("wmplayer" in p):
  os.system("wmplayer")

elif (("run" in p) or ("execute" in p)) and ("vlc" in p):
  os.system("vlc")

elif (("run" in p) or ("execute" in p)) and ("internet explorer" in p):
  os.system("iexplore")

elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("computer management" in p):
  os.system("compmgmtlauncher")

elif (("run" in p) or ("execute" in p) or ("open" in p) or ("change" in p)) and ("printing settings" in p):
  os.system("printui")

elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("compare files command" in p):
  os.system("comp")

elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("authorization manager" in p):
  os.system("azman.msc")

elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("personalization settings" in p):
  os.system("control desktop")

elif (("run" in p) or ("execute" in p) or ("open" in p)) and (("system properties" in p) or ("Change Computer Settings" in p)):
  os.system("sysdm.cpl")

elif (("run" in p) or ("execute" in p) or ("open" in p)) and (("performance options" in p) or ("Change Data Execution Prevention Settings" in p)):
  os.system("systempropertiesdataexecutionprevention")

elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("clear type text tuner" in p):
  os.system("cttune")

elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("component services" in p):
  os.system("comexp.msc")

elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("Diagnostics Troubleshooting Wizard" in p):
  os.system("msdt")

elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("disk management" in p):
  os.system("diskmgmt.msc")

elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("task manager" in p):
  os.system("taskmgr")

elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("character map" in p):
  os.system("charmap")

elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("default apps" in p):
  os.system("computerdefaults")

elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("devices and printers" in p):
  os.system("control printers")

elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("device manager" in p):
  os.system("devmgmt.msc")

elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("bluetooth file transfer" in p):
  os.system("fsquirt")

elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("administrative tools" in p):
  os.system("control admintools")

elif (("run" in p) or ("execute" in p) or ("open" in p)) and (("date and time" in p) or ("time and date" in p)):
  os.system("timedate.cpl")

elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("system configuration" in p):
  os.system("msconfig")

elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("Remote Desktop" in p):
  os.system("mstsc")

elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("resource monitor" in p):
  os.system("resmon")

elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("color management" in p):
  os.system("colorcpl")

elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("windows dialog" in p):
  os.system("winver")

elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("disk cleanup" in p):
  os.system("cleanmgr")

elif (("adjust" in p) or ("execute" in p) or ("open" in p)) and ("mouse setting" in p):
  os.system("main.cpl")

elif (("run" in p) or ("execute" in p) or ("open" in p) or ("access" in p)) and ("system information" in p):
  os.system("msinfo32")

elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("program and features" in p):
  os.system("appwiz.cpl")

elif (("run" in p) or ("execute" in p)) and ("paint" in p):
  os.system("mspaint")

elif (("run" in p) or ("execute" in p)) and ("powershell" in p):
  os.system("powershell")

elif (("run" in p) or ("execute" in p)) and ("service" in p):
  os.system("services.msc")

elif (("run" in p) or ("execute" in p)) and ("anaconda" in p):
  os.system("anaconda")

elif (("run" in p) or ("execute" in p)) and ("calculator" in p):
  os.system("calc")

elif (("run" in p) or ("execute" in p)) and ("control panel" in p):  
  os.system("control panel")

elif (("run" in p) or ("execute" in p)) and (" adobe photoshop" in p):  
  os.system("photoshop")

elif (("run" in p) or ("execute" in p)) and ("wordpad" in p):  
  os.system("wordpad")

elif (("run" in p) or ("execute" in p)) and ("local group policy editor" in p):
  os.system("gpedit.msc")

elif (("run" in p) or ("execute" in p)) and ("winscp" in p):  
  os.system("winscp")

elif (("run" in p) or ("execute" in p)) and ("windows security" in p):  
  os.system("windowsdefender://update/")

elif (("run" in p) or ("execute" in p)) and ("command prompt" in p):  
  os.system("cmd")

elif (("run" in p) or ("execute" in p)) and ("DirectX Diagnostic Tool" in p):  
  os.system("dxdiag")

elif (("run" in p) or ("execute" in p) or ("display" in p)) and ("settings" in p):  
  os.system("dpiscaling")

elif (("run" in p) or ("execute" in p) or ("display" in p)) and ("color calibration" in p):  
  os.system("dccw")

else:
  print("don't support")