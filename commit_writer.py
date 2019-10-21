from datetime import datetime
from self_commit import commit
from char_to_pixel import *
import hashlib
import time

date_chars = ['-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

class CommitWriter(object):
    """Write a 50x7 pixel message on GitHub over the course of a year."""

    def __init__(self):
        self.initialized = False
        self.begin = False
        
    def write(self, msg):
        self.pix_num = 0
        for c in msg:
            self.pix_num += length[c]
        if self.pix_num > 50:
            print("Greater than 50! Try again")
            self.initialized = False
        else:
            self.msg = msg
            self.initialized = True

    

    def start(self):
        if datetime.today().weekday() == 0 and not self.begin:
            self.begin = True
            with open((self.msg + ".txt"), 'w') as w:
                w.close()
            print("Our first commit is today!")
        if not self.begin:
            print("You have", 6 - datetime.today().weekday(), "days until the first commit")

        if self.begin:
            r = open((self.msg + ".txt"), 'r')
            commit_ready = True
            line_count = 0
            for line in r.readlines():
                line_count += 1
                if datetime.strptime(line[:-1], '%Y-%m-%d').strftime('%Y-%m-%d') ==\
                   datetime.now().strftime('%Y-%m-%d'):
                    commit_ready = False
                    
            r.close()
            print("Linecount:", line_count)
            if commit_ready:
                cur_pix_num = line_count
                for i in self.msg:
                    if cur_pix_num - 7 * length[i] < 0:
                        letter = i
                        break
                    else:
                        cur_pix_num -= 7 * length[i]
                print("Working on the letter:", letter)
                y = (datetime.today().weekday() - 6) % 7
                x = 0
                while cur_pix_num >= 0:
                    cur_pix_num -= 7
                    x += 1
                cur_pix_num += 7
                x -= 1
                print("At coord:", x,y)
                if conversion[letter][y][x] == 0:
                    print("Committing", int(7 - (line_count % 7) * 2) + 1, "times")
                    for i in range(0, int(7 - (line_count % 7) * 2) + 1):
                        nm = hash_object = hashlib.md5(str(datetime.now()).encode())
                        nm = nm.hexdigest()
                        with open(("force_commit/" + nm + ".txt"), 'w') as w:
                            w.close()
                        commit()
                        print("Commit")
                        time.sleep(60)
                else:
                    print("No commits today")
                with open((self.msg + ".txt"), 'a') as a:
                    a.write(str(datetime.now().strftime('%Y-%m-%d')))
                    a.write("\n")
                a.close()
                print("Complete for the day")
            
                
                    
                
                
            
        

#n = datetime.now()
#string = n.strftime('%Y-%M-%d')
#print(string)
#print(datetime.strptime(string, '%Y-%M-%d').strftime('%Y'))

x = CommitWriter()
x.write("ABC")
#x.begin = True
x.start()
time.sleep(1)
x.start()
time.sleep(1)
x.start()
