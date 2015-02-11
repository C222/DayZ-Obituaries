import regex_parse
import graphviz

class LogViz(object):
    def __init__(self, playerdict, everyone = False, engine = 'dot'):
        self.graph = graphviz.Digraph(comment='Vizualization', format='png', engine=engine)
        for p in playerdict:
            if playerdict[p].kills or playerdict[p].deaths or everyone:
                self.graph.node(p, playerdict[p].name)
                for k in playerdict[p].kills:
                    self.graph.edge(p, k.id)

class Player(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.connected = []
        self.disconnected = []
        self.kills = []
        self.deaths = []
        
    def killed(self, victim):
        self.kills += [victim]
        
    def died(self, time):
        self.deaths += [time]
        
    def dict(self):
        return {'id':self.id,
                'name':self.name,
                'connected':self.connected,
                'disconnected':self.disconnected,
                'kills':[x.id for x in self.kills],
                'deaths':self.deaths}

def main():
    
    players = {}
    
    log_f = open("./log_example.txt","r")
    
    for l in log_f.readlines():
        kill_line = regex_parse.kill_c.search(l)
        connect_line = regex_parse.connect_c.search(l)
        disconnect_line = regex_parse.disconnect_c.search(l)
        if kill_line:
            killed_name = kill_line.group(2)
            killed_id = kill_line.group(3)
            
            if killed_id not in players:
                players[killed_id] = Player(killed_name,killed_id)
                
            killer_name = kill_line.group(4)
            killer_id = kill_line.group(5)
            
            if killer_id not in players:
                players[killer_id] = Player(killer_name,killer_id)
            
            players[killer_id].killed(players[killed_id])
            players[killed_id].died(kill_line.group(1))
            
            kill_line = None
            
        if connect_line:
            
            if connect_line.group(3) not in players:
                players[connect_line.group(3)] = Player(connect_line.group(2),connect_line.group(3))
            
            players[connect_line.group(3)].connected += [connect_line.group(1)]
            
            connect_line = None
            
        if disconnect_line:
            
            if disconnect_line.group(3) not in players:
                players[disconnect_line.group(3)] = Player(disconnect_line.group(2),disconnect_line.group(3))
            
            players[disconnect_line.group(3)].disconnected += [disconnect_line.group(1)]
            
            disconnect_line = None
            
    lv = LogViz(players, True, engine='fdp')
    print lv.graph.source
    print lv.graph.render()

if __name__ == "__main__":
    main()