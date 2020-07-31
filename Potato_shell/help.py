# A module to display commands for the PotatoShell


def help_text():
    print("""help()          shows this list
mhelp()         shows help for python modules
license()       shows the license
echo            writes the input
pecho           writes the input in to a .txt file
exit()          kills the shell
rpass           generates a random password(input is the len)
mkfile          make a file in a specified path
mkdir           make a directory in a specified path
dlt             delete a file
dltdir           delete a directory
strt            opens a specified file
cmd()           starts cmd terminal
calc()          open the calculator
note()          opens notepad
exp()           opens Windows explorer
web             opens the specified website
incognito       opens the specified website in incognito mode
search          searches the specified terms on google
isearch         searches the specified terms on google with incognito mode
freq            plays the input(freq(37 - 32767), length)
gith()          opens github.com
crash()         crashes the console
h.show()        shows your history
h.erase()       erases your history
cd              changes the cdw to the input
ls()            lists all files and directories in the cwd
cpunum()        returns how many CPUs are in the machine
cls()           clears the console
cat             reads the specified file
fwrite          creates or opens a specified file (depending on if it
                already exists) and writes the input in it
                (use '~' instead of spaces in the path)
                (use '$' instead of enter in text)
gsend()         send a email using gmail. Sender's address has to have
                less secure apps turned on(files are not necessary)
.ins()          instantiates a new window of the Potato shell
tasklist()      shows the list of tasks currently running
tkill           kill or stop a running process or application
                (tkill /? for more information)
tree()          graphically shows the directory structure
color           changes the color of the foreground
time()          shows the current time (Y, m, d, H, M, S)
mb()            runs the Music bot (songs in the music_list.txt required)
md5             hashes the input text to md5
audio.log       prints out what you say. (input is the amount of loops)
unicode()       opens the table with all of the unicode chars
sudo            runs the .exe program as administrator (may not work)
cmd             runs the specified command in cmd""")
