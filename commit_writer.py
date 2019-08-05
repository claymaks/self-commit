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
        if datetime.today().weekday() == 6:
            self.begin = True
            with open((self.msg + ".txt"), 'w') as w:
                w.write(self.msg)
        if self.begin:
            r = open((self.msg + ".txt"), 'r')
            commit_ready = True
            line_count = -1
            for line in r.readline():
                line_count += 1
                if datetime.strptime(line, '%Y-%M-%d') ==\
                   datetime.now().strftime('%Y-%M-%d'):
                    commit_ready = False
            if commit_ready:
                cur_pix_num = line_count
                for i in self.msg:
                    if cur_pix_num - 7 * length[i] < 0:
                        letter = i
                        break
                    else:
                        cur_pix_num -= 7 * length[i]
                y = cur_pix_num // 7
                x = cur_pix_num % 7
                if conversion[letter] == 1:
                    for i in range(0, int(7 - (line_count % 7) * 2) + 1):
                        commit()
                        time.sleep(1)
                
                    
                
                
            
        

#n = datetime.now()
#string = n.strftime('%Y-%M-%d')
#print(string)
#print(datetime.strptime(string, '%Y-%M-%d').strftime('%Y'))



