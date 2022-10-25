O='r'
N='dos'
M='nt'
L='ce'
K='posix'
J='\n'
I='red'
H='white'
from os import name as A,system as D,stat
from sys import stdout as B
from time import sleep
try:os.system('pip install datetime >nul && cls');from datetime import datetime
except:from datetime import datetime
from random import choice as E
C={H:'\x1b[1;37m','green':'\x1b[0;32m',I:'\x1b[0;31m','yellow':'\x1b[1;33m','bblue':'\x1b[1;34;40m','bcyan':'\x1b[1;36;40m'}
def P():
    if A==K:D('clear')
    elif A in(L,M,N):D('cls')
    else:print(J)*120
def Q(title):
    C=title
    if A==K:B.write(f"]2;{C}\a")
    elif A in(L,M,N):D(f"title {C}")
    else:B.write(f"]2;{C}\a")
def F(bracket_color,text_in_bracket_color,text_in_bracket,text):C=text;A=bracket_color;B.flush();C=C.encode('ascii','replace').decode();B.write(A+'['+text_in_bracket_color+text_in_bracket+A+'] '+A+C+J)
def G(filename,method):
    E='ERROR';A=filename
    try:
        if stat(A).st_size!=0:
            with open(A,method,encoding='utf8')as B:D=[A.strip(J)for A in B];return D
        else:F(C[I],C[H],E,f"{A} is empty!");sleep(2);raise SystemExit
    except FileNotFoundError:F(C[I],C[H],E,'File not found!')
def R():A=datetime.now();B=A.strftime('%Y-%m-%d %H:%M:%S');return B
def S(path):A=G(path,O);return E(A)
def T(use_proxy,proxy_type,path):
    K=None;J='socks5://{0}';I='socks4://{0}';F=proxy_type;D='https';C='http';B={}
    if use_proxy==1:
        H=G(path,O);A=E(H)
        if F==1:B={C:'http://{0}'.format(A),D:'https://{0}'.format(A)}
        elif F==2:B={C:I.format(A),D:I.format(A)}
        else:B={C:J.format(A),D:J.format(A)}
    else:B={C:K,D:K}
    return B