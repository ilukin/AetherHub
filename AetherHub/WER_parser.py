import xml.etree.cElementTree as etree
from AetherHub.onlinepairings.models import Player, Matches, Event

root = ''
tree = ''
def getXML(path):
    global tree
    global root
    tree = etree.parse(path)
    root = tree.getroot()


#class Player(object):
#   def __init__(self, ID, currentOpp, Table, Points, Name):
#        self.ID = ID
#        self.currentOpp = currentOpp
#        self.Table = Table
#        self.Points = Points
#        self.Name = Name
#    def __repr__(self): return self.ID
#    def __str__(self): return self.ID


def loadplayers(eventid):
    playerlist = tree.iterfind('./participation/person')
    seatings_table = tree.iterfind('./seats/table')
    for child in playerlist:
        Player.objects.get_or_create(id = child.attrib['id'], name = child.attrib['last'] + ' ' + child.attrib['first'])
        a = Player.objects.get(id = child.attrib['id'])
        a.eventID = eventid
        a.save()
    for child in seatings_table: #TABLE, dummy: 1 to 4
        tablenum = child.attrib['number']
        seatings_seat = tree.iterfind('./seats/table[@number=' + "'" + tablenum + "'" + ']/seat')
        for item in seatings_seat:
            if a.Otable == 0:
                a = Player.objects.get(id = item.attrib['player'])
                a.Otable = tablenum
                a.save()

     #roundstr = r"'<roundnum>'"
     #tree.iterfind('matches/round[@number="1"]/match')
def loadround(eventid, roundnum):
    roundstr = "'" + roundnum + "'"
    tablenum = 1
    findtext = './matches/round[@number=' + str(roundstr) +  ']/match'
    matches = tree.iterfind(findtext)
    for child in matches:
       Matches.objects.get_or_create(activePlayerID = child.attrib['person'],
                                     opponentID = child.attrib['opponent'],
                                     opponentName = Player.objects.get(id = child.attrib['opponent']).name,
                                     eventID = eventid,
                                     byeCheck = child.attrib['outcome'],
                                     roundNum = roundnum,
                                     tableNum = tablenum,)
       if child.attrib['win'] != '-1':
           obj = Matches.objects.get(eventID = eventid, roundNum = roundnum, activePlayerID = child.attrib['person'])
           obj.activePlayerWin = child.attrib['win']
           obj.opponentWin = child.attrib['loss']
           obj.draws =  child.attrib['draw']
           obj.save()
       tablenum = tablenum + 1
    #print('Load complete')

def findme(DCI, eventid): #listázza ki adott eventen az összes, játékoshoz tartozó meccset és az eredményét
    currentmatches = Matches.objects.filter(activePlayerID = DCI, eventID = eventid)
    return (currentmatches)

def findtables(tablenum, event):
    currentmatch = Matches.objects.filter(tableNum = tablenum, eventID = event)
    a = Player.objects.get(id = activePlayerID)
    b = Player.objects.get(id = opponentID)
    return(a.Otable, a.name, b.Otable, b.name, tablenum)
    
#print("A " + str(a[0]) + ". asztalon játszol " + a[1] + " ellen")

if __name__ == "__main__":
    findme('19292697')
