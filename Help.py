# A module to display commands for the PotatoShell


def help_text():
    print("""help()          shows this list
echo            writes the input
pecho           writes the input in to a .txt file
exit()          kills the shell
rpass           generates a random password(input is the len)
mkfile          make a file in a specified path
mkdir           make a directory in a specified path
dlt             delete a file
dldir           delete a directory
strt            opens a specified file
cmd()           starts cmd terminal
calc()          open the calculator
note()          opens notepad
exp()           opens Windows explorer
web             starts a specified website
freq            plays the input(freq(37 - 32767), length)
gith()          opens github.com
crash()         crashes the console
h.show()        shows your history
h.erase()       erases your history
cd              changes the cdw to the input
ls()            lists all files and directories in the cwd
cpunum()        returns how many CPUs are in the machine
fg.green()      turns the text green
fg.blue()       turns the text blue
c.reset()       resets the color of the text
cls()           clears the console""")
