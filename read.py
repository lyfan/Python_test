import serial
import binascii
import sys
import getopt
max_num=7


############################################

def usage():
  print "python read.py -d /dev/ttyxxx"

############################################

def get_name(dev,num):
    return dev[:-1]+str(num)

############################################
#ser = serial.Serial(sys.argv[1],115200)
def test_device(device):
    cur_num=0    
    while cur_num<max_num:
        curdev=get_name(device,cur_num)

        try:
          ser = serial.Serial(curdev,115200)
          ser.timeout=0;
          ret=ser.isOpen()
		
          if ret:
              print(curdev+" is opened")
              numrd=0
              while numrd<3:
                print("read "+curdev)
                data = ser.read(30).replace(binascii.unhexlify("00"), "")
                hex_list = [hex(ord(i)) for i in data]
                print hex_list
                numrd+=1
              ser.close()        
        except:
              print(curdev+" open failed")
        cur_num+=1

#############################################
print "len: ",len(sys.argv)

device=""
opts, args = getopt.getopt(sys.argv[1:],"hdt:")
for op, value in opts:
    if op == "-d":
        device=value
    elif op == "-t":
        device=value
        test_device(device)
        sys.exit()
    elif op =="-h":
        usage()
        sys.exit()	
    else:
        print "no args=========="
        usage()
        sys.exit()




