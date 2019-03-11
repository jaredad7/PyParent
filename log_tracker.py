import time, os

#Set the filename and open the file
filename = 'example_log.txt'
file = open(filename,'r')

#Find the size of the file and move to the end
st_results = os.stat(filename)
print(st_results)
st_size = st_results[6]
print(st_size)
file.seek(st_size)

while 1:
    where = file.tell()
    line = file.readline()
    if not line:
        time.sleep(0.1)
        file.seek(where)
    else:
        print line, # already has newline