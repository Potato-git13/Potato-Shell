# A module to display commands for the PotatoShell


def help_text():
    print("""help()          shows this list
mhelp()         shows help for python modules
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
web             opens the specified website
incognito       opens the specified website in incognito mode
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
c.w&b()         turns the background white and the foreground black
c.reset()       resets the color of the text
cls()           clears the console
cat             reads the specified file
fwrite          creates or opens a specified file (depending on if it
                already exists) and writes the input in it
                (use '~' instead of spaces in the path)
                (use '$' instead of enter in text)
gsend()         send a email using gmail. Sender's address has to have
                less secure apps turned on(files are not necessary)
.ins()          instantiates a new window of the Potato shell""")
