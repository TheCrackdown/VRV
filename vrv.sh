#!/bin/bash
#
# Tracking - System Enumeration - And Off Course Pentesting Too
#
# Version : 1.0 | Codename : VRV 
# Coded by : VAIBHAV VARUN RISHABH | VIT BHOPAL
#
# Tested on : Kali Linux 
# I highly recommend using this tool by using Kali Linux OS
# If You using another OS dont forget to install python and perl requirements
#
# 
# This Tool Designed For Lazy Way To Pentest :)
# Remember Educational Purpose only Not For Crime
# Im Not Responsible If Something Bad Thing Happen
# Use At Your Own Risk
#

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                                                                ║"   
echo "║  Tracking - System Enumeration - And Off Course Pentesting Too ║"
echo "╚════════════════════════════════════════════════════════════════╝"            
echo "╔════════════════════════════════════════════════════════════════╗"
echo " ║                  Version : 1.0                               ║"
echo "   ║    Coded by : VAIBHAV VARUN RISHABH | VIT BHOPAL         ║"
echo "    ║                 Tested on : Kali Linux                 ║"
echo "     ║                                                      ║"              
echo "      ╚════════════════════════════════════════════════════╝"
echo "══════════════════════════════════════════════════════════════════"
echo "Enter domain of your Target Below example site.com :"
read TARGET
echo ""
echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                                                                ║"
echo "║                           WARNING                              ║"
echo "║                                                                ║"
echo "║      I highly recommend using this tool by using Kali Linux OS ║"
echo "║                                                                ║"
echo "║      By using this tool it means you agree with terms,         ║"
echo "║      conditions, and risks                                     ║"
echo "║                                                                ║"
echo "║      By using this tool you agree that                         ║"
echo "║      1. use for legitimate security testing                    ║"
echo "║      2. not for crime                                          ║"
echo "║      3. the use of this tool solely for                        ║"
echo "║         educational reasons only                               ║"
echo "║         Thank you and happy pentest                            ║"
echo "║                                                                ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""
echo ""
echo ""
echo ""
echo ""
echo "█[1]█"
echo ""
echo ""
echo ""
echo "█[2]█"
echo ""
echo ""
echo ""
echo "█[3]█"
echo ""
echo ""
echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                    VRV STARTED                                 ║"              
echo "╚════════════════════════════════════════════════════════════════╝"

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║            Let's Find Who The Hell Is This Owner               ║"              
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""
echo "whois looking up (if not run maybe not installed in your OS)"
whois $TARGET
echo "whois looking up finished"
echo ""
echo "nslooking up (if not run maybe not installed in your OS)"
nslookup $TARGET
echo "nslooking up finished"
echo ""
echo "scanning with nmap (if not run maybe not installed in your OS)"
nmap -v -O -oN output.txt $TARGET
echo "scanning with nmap finished"
echo ""
echo "starting the harvester for gathering email and subdomain information"
python modules/theHarvester/theHarvester.py -d $TARGET -l 500 -b google
echo "the harvester finished"
echo ""
echo "starting metagoofil for gathering document maybe important"
python modules/metagoofil/metagoofil.py -d $TARGET -t doc,pdf,xls,csv,txt -l 200 -n 50 -o metagoofiles -f data.html
echo "metagoofil finished"
echo ""
echo ""
dig -x $TARGET
python modules/sublist3r/sublist3r.py --output output.txt --domain $TARGET
echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                    Got It :v wkwkwkwkwk                        ║"              
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""
echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                   XSS Scanning Starting                        ║"              
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""
python modules/XssPy.py -u $TARGET -v
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                   XSS Scanning Finished                        ║"              
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                   Scan Wordpress Starting                      ║"              
echo "╚════════════════════════════════════════════════════════════════╝"
python modules/wpscanner.py -s http://$TARGET -n 20
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                   Scan Wordpress Finished                      ║"              
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""
echo ""
echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                   Moving Metagoofil Files                      ║"              
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""
echo "Moving Metagoofil Folder"
mv metagoofiles /root/Desktop 
echo "Moving Metagoofil Folder Finished"
echo ""
echo "Moving Metagoofile data.html"
mv data.html /root/Desktop
echo "Moving Metagoofil data.html finished"
echo ""
echo ""
echo ""
echo ""
echo "█[1]█"
echo ""
echo ""
echo ""
echo "█[2]█"
echo ""
echo ""
echo ""
echo "█[3]█"
echo ""
echo ""
echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                       VRV FINISHED                             ║"
echo "║                    HOPE YOU ENJOYED IT                         ║"
echo "║                       AND AS ALWAYS                            ║"
echo "║                      HAVE A NICE DAY                           ║"              
echo "╚════════════════════════════════════════════════════════════════╝"
