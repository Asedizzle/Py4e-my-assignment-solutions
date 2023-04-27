'''The code below acesses data from a website and parses lines with starting eith From and creates a sql data base that
details how many times an organization's name is seen. The code then orders the organisations according to the first ten with the highest count  then prints them
and their counts'''


import ssl,urllib.request, sqlite3

create = sqlite3.connect("orgcounting.sqlite")
wand = create.cursor()

wand.execute('''DROP TABLE IF EXISTS Counts''')
wand.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')


abc = ssl.create_default_context()
abc.check_hostname = False
abc.verify_mode = ssl.CERT_NONE


url = input("Please enter a valid url")
if len(url) < 1:
    url = "http://data.pr4e.org/mbox.txt"
url_r = urllib.request.urlopen(url, context=abc)


for line in url_r:
    line = line.decode()
    if line.startswith("From: "):
            words = line.split()
            full_org = words[1]
            div_org = full_org.split("@")
            org = div_org[1]
            #print(org)
            
            wand.execute('SELECT count FROM Counts where org = ?', (org,))
            row = wand.fetchone()
            if row is None:
                wand.execute(''' INSERT INTO Counts (org,count) VALUES (?,1)''', (org,))
            else:
                wand.execute('''UPDATE Counts SET count = count + 1 WHERE org = ? ''', (org,))
    
create.commit()

order_str = 'SELECT org,count FROM Counts ORDER BY count DESC LIMIT 10'



for row in wand.execute(order_str):
    print(str(row[0]), row[1])

wand.close()
print("All done")