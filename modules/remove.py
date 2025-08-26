import os
if os.path.exists("stt.txt"):
    os.remove('stt.txt')
else:
    print("not exists")
