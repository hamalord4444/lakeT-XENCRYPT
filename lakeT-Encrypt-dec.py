# Decompile by 
# File: laka-encrypt  (Python 3.10)
#my id 
#my telegram channel 
import base64
import zlib
import marshal
import os
os.system('clear')
password = 'X0000'
print('\x1b[91m\n              _        _______ _________\n    |\\     /|( (    /|(  ___  )\\__   __/\n    ( \\   / )|  \\  ( || (   ) |   ) (\n     \\ (_) / |   \\ | || |   | |   | |\n      ) _ (  | (\\ \\) || |   | |   | |\n     / ( ) \\ | | \\   || |   | |   | |\n    ( /   \\ )| )  \\  || (___) |   | |\n    |/     \\||/    )_)(_______)   )_(,XENCRYPT...\n    # Obfuscator Created By X NOT FOUND X\n    # My Telegram Account @xXx_not_found_xXx\n    # My Telegram Channel @Cracker_Team_Kurd\n    # My Github Account @hamalord4444\n-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_--_-_-_-_--_-_-_-_-_-_-\n-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_--_-_-_-_--_-_-_-_-_-_-\n-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_--_-_-_-_--_-_-_-_-_-_-\n')
p = input('\x1b[91m Enter Password > ')

x1 = ' '
print(x1[::-1])
print('\x1b[91m\n              _        _______ _________\n    |\\     /|( (    /|(  ___  )\\__   __/\n    ( \\   / )|  \\  ( || (   ) |   ) (\n     \\ (_) / |   \\ | || |   | |   | |\n      ) _ (  | (\\ \\) || |   | |   | |\n     / ( ) \\ | | \\   || |   | |   | |\n    ( /   \\ )| )  \\  || (___) |   | |\n    |/     \\||/    )_)(_______)   )_(,XENCRYPT...\n    # Obfuscator Created By X NOT FOUND X\n    # My Telegram Account @xXx_not_found_xXx\n    # My Telegram Channel @Cracker_Team_Kurd\n    # My Github Account @hamalord4444\n-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_--_-_-_-_--_-_-_-_-_-_-\n-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_--_-_-_-_--_-_-_-_-_-_-\n-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_--_-_-_-_--_-_-_-_-_-_-\n')
file = input('\x1b[91m  Enter The File > ')
if file == '':
    os.system('clear')
    print('Error: Could not open the file\n\n')
out = file.replace('.py', '') + '-enc.py'
file = open(file).read()
cc = compile(file, '<X>', 'exec')
dn = marshal.dumps(cc)
z = zlib.compress(dn)
b = base64.b64encode(z)
m = marshal.dumps(b)
b2 = base64.b64encode(m)
m2 = marshal.dumps(b2)
b3 = base64.b64encode(m2)
m3 = marshal.dumps(b3)
b4 = base64.b64encode(m3)
m4 = marshal.dumps(b4)
b5 = base64.b64encode(m4)
m5 = marshal.dumps(b5)
b6 = base64.b64encode(m5)
m6 = marshal.dumps(b6)
b7 = base64.b64encode(m6)
m7 = marshal.dumps(b7)
b8 = base64.b85encode(m7)
a1 = repr(b8)
s = open(out, 'w')
s.write('# Encrypt By xXx_not_found_xXx\n# My Telegram Account @xXx_not_found_xXx\n# My Telegram Channel @Cracker_Team_Kurd\n# https://github.com/hamalord4444\n_ = lambda __ : __import__("marshal").loads(__import__("zlib").decompress(__import__("base64").b64decode(__import__("marshal").loads(__import__("base64").b64decode(__import__("marshal").loads(__import__("base64").b64decode(__import__("marshal").loads(__import__("base64").b64decode(__import__("marshal").loads(__import__("base64").b64decode(__import__("marshal").loads(__import__("base64").b64decode(__import__("marshal").loads(__import__("base64").b64decode(__import__("marshal").loads(__import__("base64").b85decode(__[::-1])))))))))))))))));exec((_)(' + str(a1)[::-1] + '))')
s.close()
print('\x1b[1;94m[\x1b[1;92m\x1b[1;94m] \x1b[1;97  File saved as \x1b[1;96m{ \x1b[1;92m%s \x1b[1;96m}' % out)
