#Decode.py - Freerider HD object decoder
#by maxmillion18
#http://www.github.com/maxmillion18
#http://www.freeriderhd.com/u/MaxwellNurzia

import re #need it

LINE_RE = re.compile('(?P<x1>-?\S*) (?P<y1>-?\S*) (?P<x2>-?\S*) (?P<y2>-?[^ ,#])')
PUP__RE = re.compile('(?P<type>(C|T|S|O)) (?P<x>-?\S*) (?P<y>-?[^ ,#])')
PUPR_RE = re.compile('(?P<type>(G|B)) (?P<x>-?\S*) (?P<y>-?\S*) (?P<rot>-?[^ ,#])')

def decline(ls): #Decode line
    return LINE_RE.match(ls).groupdict()

def decpup(pup): #Decode powerup
    return PUP__RE.match(pup).groupdict()

def decpupr(pupr): #Decode powerup with rotation
    return PUPR_RE.match(pupr).groupdict()

def b32d(n): #Base 32 decode
    return int(n, 32)
