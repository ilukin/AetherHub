import xml.etree.cElementTree as etree
from AetherHub.onlinepairings.models import Player

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
        a.table = 0
        a.currentOpp = 0
        a.save()
    for child in seatings_table: #TABLE, dummy: 1 to 4
        tablenum = child.attrib['number']
        seatings_seat = tree.iterfind('./seats/table[@number=' + "'" + tablenum + "'" + ']/seat')
        for item in seatings_seat:
            a = Player.objects.get(id = item.attrib['player'])
            a.Otable = tablenum
            a.save()

     #roundstr = r"'<roundnum>'"
     #tree.iterfind('matches/round[@number="1"]/match')
def loadround(roundstr):
    tablenum = 1
    findtext = './matches/round[@number=' + str(roundstr) +  ']/match'
    matches = tree.iterfind(findtext)
    for child in matches:
        a = Player.objects.get(id = child.attrib['person'])
        #a = Players[playerindex(child.attrib['person'])]
        if child.attrib['outcome']=='3':
            a.currentOpp = "BYE"
            a.table = 0
            a.save()
        else:
            b = Player.objects.get(id = child.attrib['opponent'])
            #b = Players[playerindex(child.attrib['opponent'])]
            a.table = tablenum
            b.table = tablenum
            a.currentOpp = b.name
            b.currentOpp = a.name
            a.save()
            b.save()
            tablenum = tablenum + 1
    #print('Load complete')

def findme(DCI):
    a = Player.objects.get(id = DCI)
    return (a.table, a.currentOpp)

def findtables(tablenum, event):
    players = Player.objects.filter(table = tablenum, eventID = event)
    a = players[0]
    b = players[1]
    return(a.Otable, a.name, b.Otable, b.name, tablenum)
    
#print("A " + str(a[0]) + ". asztalon játszol " + a[1] + " ellen")

if __name__ == "__main__":
    findme('19292697')
