import regex_parse

class Player(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.connected = None
        self.disconnected = None
        self.kills = []
        self.deaths = []

def main():
    
    players = {}
    
    log_f = open("./log_example.txt","r")
    
    for l in log_f.readlines():
        kill_line = regex_parse.kill_c.search(l)
        connect_line = regex_parse.connect_c.search(l)
        disconnect_line = regex_parse.disconnect_c.search(l)
        if kill_line:
            
            if kill_line.group(3) not in players:
                players[kill_line.group(3)] = Player(kill_line.group(2),kill_line.group(3))
                
            if kill_line.group(5) not in players:
                players[kill_line.group(5)] = Player(kill_line.group(4),kill_line.group(5))
            
            kill_line = None
            
        if connect_line:
            
            if connect_line.group(3) not in players:
                players[connect_line.group(3)] = Player(connect_line.group(2),connect_line.group(3))
                
            connect_line = None
            
        if disconnect_line:
            
            if disconnect_line.group(3) not in players:
                players[disconnect_line.group(3)] = Player(disconnect_line.group(2),disconnect_line.group(3))
                
            disconnect_line = None
            
    print players

if __name__ == "__main__":
    main()