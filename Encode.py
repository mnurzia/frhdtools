#Encode.py - Freerider HD object encoder
#by maxmillion18
#http://www.github.com/maxmillion18
#http://www.freeriderhd.com/u/MaxwellNurzia

def encline(x1,y1,x2,y2):
        #encode line.
        return [['%s %s %s %s,' % (b32e(x1),b32e(y1),b32e(x2),b32e(y2))]]

def encpup(x,y,pupcode):
    #encode powerup without rotation
    assert pupcode in ['C','T','S','O']
    return [['%s %s %s,' % (pupcode,b32e(x),b32e(y))]]

def encpupr(x,y,rot,pupcode):
    #encode powerup with rotation
    assert pupcode in ['G','B']
    return [['%s %s %s %s,' % (pupcode,b32e(x),b32e(y),b32e(rot))]]

def b32e(numbera):
    #encode number. I struggled to find the right alphabet that frhd used for their encoding
    """Encode number in freerider base36."""
    if not isinstance(numbera, (int, long)):
        raise TypeError('number must be an integer')

    alphabet = '0123456789abcdefghijklmnopqrstuv' #DO NOT CHANGE
    number = abs(numbera)
    base32 = ''
    while number:
        number, i = divmod(number, 32)
        base32 = alphabet[i] + base32
    if numbera < 0:
        base32 = '-'+base32
    return base32 or alphabet[0]

#test stuff, use if you want
##print encline(90,12,23473,445)
##print encpup(5,6,'C')
##print encpupr(345,23475,40,'G')
