import regex_parse
import graphviz
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Input file name")
parser.add_argument("-s", "--split", help="Split output by day",action="store_true")
parser.add_argument("-e", "--everyone", help="Graph every player on the server",action="store_true")
parser.add_argument("-g", "--engine", help="Graphing engine to use [dot, neato, twopi, circo, fdp, sfdp, osage]",default="fdp")
parser.add_argument("-f", "--format", help="Rendered file format [ps, svg, svgz, fig, png, imap, cmapx]",default="png")
args = parser.parse_args()

class LogViz(object):
	def __init__(self, playerdict, everyone = False, engine = 'dot', label = "Graph", filename="out"):
		self.graph = graphviz.Digraph(comment=label, format=args.format, engine=engine, filename = filename+".gv")
		self.graph.body.append('label="'+label+'"')
		for p in playerdict:
			if playerdict[p].kills or playerdict[p].deaths or everyone:
				self.graph.node(p, playerdict[p].name)
				for k in playerdict[p].kills:
					self.graph.edge(p, k[0].id, xlabel=k[1], fontcolor="red")

class Player(object):
	def __init__(self, name, id):
		self.name = name.strip('"')
		self.id = id
		self.connected = []
		self.disconnected = []
		self.kills = []
		self.deaths = []
		
	def killed(self, victim, time):
		self.kills += [(victim, time)]
		
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
	
	file_name = args.filename
	split_days = args.split
	everyone = args.everyone
	
	try:
		log_f = open(file_name)
	except:
		log_f = open("./log_example.txt","r")
	
	filetext = log_f.read()
	
	if split_days:
		dayz_days = filetext.split("******************************************************************************")
	else:
		dayz_days = [filetext]
	
	for d in dayz_days:
		label = file_name
		players = {}
		for l in d.split("\n"):
			kill_line = regex_parse.kill_c.search(l)
			connect_line = regex_parse.connect_c.search(l)
			disconnect_line = regex_parse.disconnect_c.search(l)
			day_line = regex_parse.day_c.search(l)
			if kill_line:
				
				time = kill_line.group(1)
				killed_name = kill_line.group(2)
				killed_id = kill_line.group(3)
				
				if killed_id not in players:
					players[killed_id] = Player(killed_name,killed_id)
					
				killer_name = kill_line.group(4)
				killer_id = kill_line.group(5)
				
				if killer_id not in players:
					players[killer_id] = Player(killer_name,killer_id)
				
				players[killer_id].killed(players[killed_id], time)
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
				
			if day_line:
				label += " " + day_line.group(1) + " " + day_line.group(2)
				print label
				
		if players:
			if not split_days:
				label = file_name
			lv = LogViz(players, everyone, engine=args.engine, label = label, filename = label.replace('-','').replace(':','').replace(' ',''))
			# print lv.graph.source
			lv.graph.render()

if __name__ == "__main__":
	main()