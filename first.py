
from main import fn     #csak adott részt olvas másik fájlból, így kell használni utána
print(fn(3, 4))


import main             #import main #az egész másik fájt olvassa, ezt pedig így kell használni utána
print(main.fn(4, 5))

