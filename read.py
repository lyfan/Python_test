import serial
import binascii
import sys
import getopt
max_num=7


############################################

def usage():
  print('----------------------------------------')
  print "eg:[python read.py -d /dev/ttyS0 -w xxxx]"
  print "options:"
  print "         -d device name"
  print "         -w write data"
  print "         -h help"


############################################
def get_name(dev,num):
    return dev[:-1]+str(num)



############################################
def test_device(device,wstr):
    cur_num=0    
    while cur_num<max_num:
        curdev=get_name(device,cur_num)

        try:
          ser = serial.Serial(curdev,115200)
          ser.timeout=0;
          ret=ser.isOpen()
		
          if ret:
              print(curdev+" is opened")
              #print('write--:'+wstr)
              #ser.write(wstr)
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
def getArgs(args):
    pass
    


def main():
    if len(sys.argv) < 3:
        usage()
        sys.exit()
    device=''
    wstr=''
    opts, args = getopt.getopt(sys.argv[1:],"hw:d:")

    for op, value in opts:
        print("==============op: "+op+" value: "+value)
        if op == "-d":
            device=value
        elif op == "-w":
            wstr=value
        elif op =="-h":
            usage()
            sys.exit()	

    test_device(device,wstr)

if __name__=='__main__':main()
