import os, sys, time, pickle
def label(arg):
	if not arg:
		print """ 

	 $$$$$$\                      $$\       $$\                     
	$$  __$$\                     $$ |      \__|                    
	$$ /  \__| $$$$$$\   $$$$$$\  $$ |  $$\ $$\  $$$$$$\   $$$$$$$\ 
	$$ |      $$  __$$\ $$  __$$\ $$ | $$  |$$ |$$  __$$\ $$  _____|
	$$ |      $$ /  $$ |$$ /  $$ |$$$$$$  / $$ |$$$$$$$$ |\$$$$$$\  
	$$ |  $$\ $$ |  $$ |$$ |  $$ |$$  _$$<  $$ |$$   ____| \____$$\ 			
	\$$$$$$  |\$$$$$$  |\$$$$$$  |$$ | \$$\ $$ |\$$$$$$$\ $$$$$$$  |
	 \______/  \______/  \______/ \__|  \__|\__| \_______|\_______/ 

	__________________________________________________________________

	 
	                            .-'''''-.
	                            |'-----'|		
	                            |-.....-|		Cookies: %s
	                            |       |		Total Cookies: %s
	                            |       |		Hand-Made Cookies: %s
	           _,._             |       |		Cookies Per Second: %s
	      __.o`   o`"-.         |       |		Buildings: %s
	   .-O o `"-.o   O )_,._    |       |
	  ( o   O  o )--.-"`O   o"-.`'-----'`
	   '--------'  (   o  O    o)  
	                `----------`
	""" % (format(int(cookies), ",d"), format(int(total), ",d"), format(hand_made, ",d"), cps,
		format(buildings, ",d"))
	elif arg:
		print """
 .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. |
| |    _______   | || |  ____  ____  | || |     ____     | || |   ______     | |
| |   /  ___  |  | || | |_   ||   _| | || |   .'    `.   | || |  |_   __ \   | |
| |  |  (__ \_|  | || |   | |__| |   | || |  /  .--.  \  | || |    | |__) |  | |
| |   '.___`-.   | || |   |  __  |   | || |  | |    | |  | || |    |  ___/   | |
| |  |`\____) |  | || |  _| |  | |_  | || |  \  `--'  /  | || |   _| |_      | |
| |  |_______.'  | || | |____||____| | || |   `.____.'   | || |  |_____|     | |
| |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------' 
		
Cookies: %s
""" % format(int(cookies), ",d")

clear = lambda: os.system('clear')
servant, mother, plant, bakery, factory, alchemy, shipment, planet, universe = [None for i in range(9)]

class building(object):
	def __init__(self, prod, cost, inc, amount, desc):
		self.prod = prod
		self.cost = cost
		self.inc = inc
		self.amount = amount
		self.desc = desc
	def bake(self):
		global cookies, total
		cookies += self.prod * self.amount
		total += self.prod * self.amount
	def add(self):
		global cookies, total, buildings, cps
		self.amount += 1
		cookies -= self.cost
		self.cost += self.inc
		buildings += 1
		cps += self.prod
	def __repr__(self):
		return """%s
---------------------------
Produces %s Cookies Per Second
Costs %d Cookies
You have %d of this item""" % (self.desc, str(self.prod), self.cost, self.amount)
class switch(object):
    def __init__(self, value):
        self.value = value
    def __iter__(self):
        yield self.match
    def match(self, *args):
        if not args:
            return True
        elif self.value in args:
            return True
        else:
            return False

ask = " "
clear()
print """Welcome to the Cookie Clicker Game (Python Version)!
This Game is basically about exponential growth. To start off, you need to bake cookies
To do so, press Control-C (^C). Cookies are used as currency, which can buy buildings that
automatically bake cookies for you! To visit the Shop, hold Control-C (^C)! Have Fun!"""
print """
Type [Y] If You Would Like to Import a Saved Game.
If Not, Type [N]."""
while ask.lower() not in ["y", "n"]:
	ask = raw_input("")
if ask.lower() == "y":
	with open("cookie.txt", "r") as myfile:
		pack = pickle.load(myfile)
		servant, mother, plant, bakery, factory, alchemy, shipment, planet, universe, \
		cookies, total, hand_made, buildings, cps = pack
else:
	cookies, total, hand_made, buildings, cps= 0, 0, 0, 0, 0
	servant = building(0.1, 15, 15, 0, "Servant")
	mother = building(0.5, 100, 20, 0, "Mother")
	plant = building(3, 500, 100, 0, "Plant")
	bakery = building(10, 3000, 200, 0, "Bakery")
	factory = building(40, 10000, 500, 0, "Factory")
	alchemy = building(400, 200000, 10000, 0, "Alchemy")
	shipment = building(5000, 500000, 50000, 0, "Shipment")
	planet = building(100000, 1500000, 100000, 0, "Planet")
	universe = building(1000000, 50000000, 5000000, 0, "Universe")
task = 0
object_val = {
	0: 0, 1:servant.cost, 2:mother.cost, 3:plant.cost, 4:bakery.cost, 5:factory.cost,
	6:alchemy.cost, 7:shipment.cost, 8:planet.cost, 9:universe.cost, 10:0
}
objects = [servant, mother, plant, bakery, factory, alchemy, shipment, planet, universe]
while True:
	try:
		time.sleep(1)
		clear(), label(0)
		for i in objects:
			i.bake()
	except KeyboardInterrupt:
		cookies += 1
		total += 1
		hand_made += 1
		clear(), label(0)
		try:
			time.sleep(0.1)
		except KeyboardInterrupt:
			clear(), label(1)
			for i in objects:
				if cookies >= i.cost:
					print """Type [%d] to buy a %s
					""" % (task, i)
					task += 1
			task = 1
			print """Type [0] to Exit the Program.
			"""
			print """Press [^C] To Exit.
			"""
			i = None
			try:
				while i not in range(10) or cookies <= object_val[i]:
					try:
						i = int(raw_input(""))
						if i == 10:
							print "*Sigh* I guess you found this program's secret."
							print "Remember: Cheated Cookies taste bad."
							amn = int(raw_input("Amount:"))
							cookies += amn
							total += amn
							i = 10
							break
					except ValueError:
						i = None
				for case in switch(i):
					if case(1):
						servant.add()
					elif case(2):
						mother.add()
					elif case(3):
						plant.add()
					elif case(4):
						bakery.add()
					elif case(5):
						factory.add()
					elif case(6):
						alchemy.add()
					elif case(7):
						shipment.add()
					elif case(8):
						planet.add()
					elif case(9):
						universe.add()
					elif case(10):
						pass
					elif case(0):
						clear()
						ask = " "
						print "Type [Y] If You Would Like to Save Your Progress to a File."
						print "If Not, Type [N]."
						while ask.lower() not in ["y", "n"]:
							ask = raw_input("")
						if ask.lower() == "y":
							with open("cookie.txt", "w") as myfile:
								pack = [i for i in objects]
								for i in [cookies, total, hand_made, buildings, cps]:
									pack.append(i)
								pickle.dump(pack, myfile)
							print "Exiting the Program..."
						sys.exit()
			except KeyboardInterrupt:
				continue
