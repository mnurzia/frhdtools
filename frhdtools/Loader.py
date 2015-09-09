#Loader.py - Freerider HD Track Loader
#by maxmillion18
#http://www.github.com/maxmillion18
#http://www.freeriderhd.com/u/MaxwellNurzia

import Decode as De #Decode.py - if you haven't already
                                   #go take a look ;)

def loadTrack(track):
    track[0] = track[0].split('#')
    track[0] = track[0][0].split(',')
    print(track[0])
    for obj in range(0,len(track[0])):
        track[0][obj] = De.decline(track[0][obj])
    print(track)

if __name__ == "__main__":
    tdata = open('tests/test.ft').read()
    loadTrack(tdata)