# Hacking Team Sweeper

Hacking Team has developed a large amount of malware that is being used to target activists around the world. A hacker has recently released a 400+ GB data dump of internal HackingTeam source code. Currently there is a possibility that HT clients are attempting to wipe traces off their victim's computers. **We need your aid to help perserve evidence.** If you have technical skills we urge to contribute, time is of the essence.

Step 1: Reporting signatures
--------------
**This is currently where we need help.** If you know of any signatures unique to the Hacking Team trojans, please document them in the respective file in the 'signatures' subdirectory and submit a pull request. If possible, also link to the file where you got this information from.

Step 2: Detection
--------------
Once we know what to look for, writing native scripts (powershell, bash, etc) for each of the three major OSes should be straight forward.

Step 3: Preservation
--------------
If HT malware is detected on the system, all relevant files should be saved to a ZIP, with the user advised to save it offline.
