#Track.py - Freerider HD track creation and manipulation
#by maxmillion18
#http://www.github.com/maxmillion18
#http://www.freeriderhd.com/u/MaxwellNurzia

from frhdtools import Encode as En #import Encode.py (for encoding base32)

class Track():
    """Create a freerider track instance."""

    def __init__(self):
        self.trackdata = '' #This will hold the track's mathematical parts
        self.tracklist = [[],[],[]] #3 lists: one for physics lines, one for scenery, and one for powerups

    def insLine(self,x1,y1,x2,y2,typeofline):
        if typeofline == 'p': #physics
            self.tracklist[0] += [[x1,y1,x2,y2]]
        if typeofline == 's': #scenery
            self.tracklist[1] += [[x1,y1,x2,y2]]

    def insStar(self,x,y):
        self.tracklist[2] += [['C',x,y]]

    def insCheck(self,x,y):
        self.tracklist[2] += [['T',x,y]]

    def insSlowMo(self,x,y):
        self.tracklist[2] += [['S',x,y]]

    def insBomb(self,x,y):
        self.tracklist[2] += [['O',x,y]]

    def insGravity(self,x,y,rot):
        assert rot in range(360) #gravity has rotation too
        self.tracklist[2] += [['G',x,y,rot]]

    def insBoost(self,x,y,rot):
        assert rot in range(360)
        self.tracklist[2] += [['B',x,y,rot]]

    def genCode(self):
        self.trackdatalist = [[],[],[]] #holds raw data to be joined into frhd text

        for pline in self.tracklist[0]: #physics
            self.trackdatalist[0] += En.encline(pline[0],pline[1],pline[2],pline[3])

        for sline in self.tracklist[1]: #scenery
            self.trackdatalist[1] += En.encline(sline[0],sline[1],sline[2],sline[3])

        for pup in self.tracklist[2]: #powerups
            if len(pup) == 3: #if powerup does not have the rotation attribute
                self.trackdatalist[2] += En.encpup(pup[1],pup[2],pup[0])
            if len(pup) == 4: #if powerup does have rotation attribute
                self.trackdatalist[2] += En.encpupr(pup[1],pup[2],pup[3],pup[0])

        self.finalData = '' #this will be put into frhd

        for typ in self.trackdatalist: #type of object
            for indiv in typ: #individual object
                self.finalData += indiv[0]
            self.finalData += '#'#add object end marker

        return self.finalData

if __name__ == '__main__':
    my_track = Track()
    my_track.insLine(6,6,6,6,'p')
    my_track.insLine(6,6,6,6,'s')
    my_track.insStar(6,6)
    my_track.insCheck(6,6)
    my_track.insSlowMo(6,6)
    my_track.insBomb(6,6)
    my_track.insGravity(6,6,6)
    my_track.insBoost(6,6,6)
    my_track.genCode()
    print(my_track.genCode())
