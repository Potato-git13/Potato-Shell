from msvcrt import getch

try:
    def getpass(prompt):
        """Replacement for getpass.getpass() which prints asterisks for each character typed"""
        print(prompt, end='', flush=True)
        buf = b''
        while True:
            ch = getch()
            if ch in {b'\n', b'\r', b'\r\n'}:
                print('')
                break
            elif ch == b'\x08': # Backspace
                buf = buf[:-1]
                print(f'\r{(len(prompt)+len(buf)+1)*" "}\r{prompt}{"*" * len(buf)}', end='', flush=True)
            elif ch == b'\x03': # Ctrl+C
                raise KeyboardInterrupt
            else:
                buf += ch
                print('*', end='', flush=True)
        return buf.decode(encoding='utf-8')
except ImportError:
    from getpass import getpass