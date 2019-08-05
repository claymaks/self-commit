from datetime import datetime
from self_commit import commit
from char_to_pixel import *
import time

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
                print(line)
                if datetime.strptime(line, '%Y-%M-%d') ==\
                   datetime.now().strftime('%Y-%M-%d'):
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
                y = cur_pix_num // 7
                x = cur_pix_num % 7
                print("At coord:", x,y)
                if conversion[letter][y][x] == 1:
                    print("Committing", int(7 - (line_count % 7) * 2) + 1, "times")
                    for i in range(0, int(7 - (line_count % 7) * 2) + 1):
                        commit()
                        time.sleep(1)
                else:
                    print("No commits today")
                with open((self.msg + ".txt"), 'a') as a:
                    a.write(str(datetime.now().strftime('%Y-%M-%d')))
                a.close()
                print("Complete for the day")
            
                
                    
                
                
            
        

#n = datetime.now()
#string = n.strftime('%Y-%M-%d')
#print(string)
#print(datetime.strptime(string, '%Y-%M-%d').strftime('%Y'))

x = CommitWriter()
x.write("ABC")
x.start()
time.sleep(1)
x.start()
time.sleep(1)
x.start()
