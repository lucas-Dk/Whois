# Rode essa build somente se você estiver no proot ubuntu no termux
# caso contrário, rode a outra build

import sys
import os
sistema_operacional = sys.platform()

if sistema_operacional == "linux":
        os.system("apt install python3-bs4")
else:
        pass