#Decode.py - Freerider HD object decoder
#by maxmillion18
#http://www.github.com/maxmillion18
#http://www.freeriderhd.com/u/MaxwellNurzia

import re #need it

#These regexes match power ups, and power ups with rotation.
PUP_RE  = re.compile('(?P<type>(C|T|S|O)) (?P<x>-?\S*) (?P<y>-?[^ ,#])')
PUPR_RE = re.compile('(?P<type>(G|B)) (?P<x>-?\S*) (?P<y>-?\S*) (?P<rot>-?[^ ,#])')

def decline(ls): #Decode line
    ls = ls.split(' ')
    ls = filter(None, ls)
    print(ls)
    for obj in range(0,len(ls)):
        ls[obj] = b32d(ls[obj])
    return ls

def decpup(pup): #Decode powerup
    return PUP_RE.match(pup).groupdict()

def decpupr(pupr): #Decode powerup with rotation
    return PUPR_RE.match(pupr).groupdict()

def b32d(n): #Base 32 decode
    return int(n, 32)

if __name__ == '__main__':
    print(decline('-18 1i 18 1i 4m 1i'))