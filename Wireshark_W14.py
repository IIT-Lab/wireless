import os
import re
import csv
values=[]
framesize=[]
count=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
tot=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
frames=["Beacon","Data","Acknowledgement","Probe Response","Request-to-send","Clear-to-send","Radiotap Capture","Probe Request"," Assosiation Request","Assosiation Response","Reassosiation Request","Reassosiation Response","Disassociation","Authentication","Deauthentication","Action","Null data","Power Save","Contention-Free","Block Ack","Block Ack Request"] 

for x in range(0,1000):
	os.system("tshark -I -T fields -E separator=/t -E quote=d -e _ws.col.Info -e _ws.col.Length > t.csv")
	with open('t.csv', 'rt') as f:
     		reader = csv.reader(f,skipinitialspace=True,delimiter="\t")
     		for row in reader:
          		values.append(row[0])
			framesize.append(row[1])
for i in range(len(values)):
     for j in range(len(frames)):
	if frames[j] in values[i]:
           count[j]+=1
	   tot[j]+=int(framesize[i])
	   
print frames
print count
print tot


