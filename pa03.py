from socket import *
import os
import sys
import struct
import time
import select
import binascii

ICMP_ECHO_REQUEST = 8

rtt_min = 100000
rtt_max = 0
rtt_count = 0
rtt_sum = 0
global numPings
pingsSent = 0
pingsRcvd = 0
packetsLost = 0

def checksum(string):
    csum = 0
    countTo = (len(string) // 2) * 2
    count = 0
    while count < countTo:
        thisVal = string[count+1] * 256 + string[count]
        csum = csum + thisVal
        csum = csum & 0xffffffff
        count = count + 2
        
    if countTo < len(string):
        csum = csum + string[len(string) - 1]
        csum = csum & 0xffffffff
        
    csum = (csum >> 16) + (csum & 0xffff)
    csum = csum + (csum >> 16)
    answer = ~csum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer

def receiveOnePing(mySocket, ID, timeout, destAddr):
    global rtt_min, rtt_max, rtt_count, rtt_sum, pingsRcvd, packetsLost
    pingsRcvd += 1  #incrememt # of packets received
    timeLeft = timeout
    while 1:
        startedSelect = time.time()
        whatReady = select.select([mySocket], [], [], timeLeft)
        howLongInSelect = (time.time() - startedSelect)
        print(whatReady[0])
        if whatReady[0] == []: # Timeout
            return "Request timed out."
        timeReceived = time.time()
        recPacket, addr = mySocket.recvfrom(1024)
        #return recPacket
        #Fill in start
        #Fetch the ICMP header from the IP packet
        icmpHeader = recPacket[20:28]   #get the ICMP header
        icmptype, code, checksum, idnum, seqnum = struct.unpack('bbHHh', icmpHeader)    #unpack ICMP header to get fields
        if (ID == idnum) and (code == 0) and (icmptype == 0):   #if header info is correct:
            numBytes = struct.calcsize("d")    #bytesInDouble = size of the data in the echo ping "d"
            time_sent = struct.unpack("d", recPacket[28:28 + numBytes])[0]  #get time that the packet got sent to calculate rtt of current packet
            current_rtt = timeReceived - time_sent    #set rtt of current ping
            rtt_count += 1 #increase rtt count
            rtt_min = min(rtt_min, current_rtt) #calculate new rtt_min, taking current_rtt into account
            rtt_max = max(rtt_max, current_rtt) #calculate new rtt_max, taking current_rtt into account
            rtt_sum += current_rtt      #add current_rtt to the sum of all rtt's
            return "Round trip time for this ping: " + str(current_rtt*1000) + " ms\n"  #return rtt for this ping in ms

        timeLeft = timeLeft - howLongInSelect
        if timeLeft <= 0:
            packetsLost += 1    #if time out, increment num packets lost
            return "Request timed out, packet lost."

def sendOnePing(mySocket, destAddr, ID):
    # Header is type (8), code (8), checksum (16), id (16), sequence (16)
    # Note that the numbers in parentheses are not values, but sizes in bits
    global pingsSent
    pingsSent += 1  #increment pingsSent count (to print at end of ping simulation)
    myChecksum = 0

    # Make a dummy header with a 0 checksum
    # struct -- Interpret strings as packed binary data
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    data = struct.pack("d", time.time())
    
    # Calculate the checksum on the data and the dummy header.
    myChecksum = checksum(header + data)
    
    # Get the right checksum, and put in the header
    if sys.platform == 'darwin':
        # Convert 16-bit integers from host to network byte order
        myChecksum = htons(myChecksum) & 0xffff
    else:
        myChecksum = htons(myChecksum)

    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    packet = header + data
    
    mySocket.sendto(packet, (destAddr, 1)) # AF_INET address must be tuple, not str
    # Both LISTS and TUPLES consist of a number of objects
    # which can be referenced by their position number within the object.

def doOnePing(destAddr, timeout):
    #if statement to end the program and print out the overall stats of ping messages when desired number of pings have been completed
    if (rtt_count == numPings):
        print("\nPing Statistics:")
        print("Num pings sent: " + str(pingsSent) + ", Num pings received: " + str(pingsRcvd) + ", Minimum RTT: " + str(rtt_min*1000) + " ms, Maximum RTT: " + str(rtt_max*1000) + " ms, Average RTT: " + str((rtt_sum/rtt_count)*1000) + " ms, Packet Loss %: " + str(packetsLost/rtt_count))
        exit(0)
    icmp = getprotobyname("icmp")
    
    # SOCK_RAW is a powerful socket type. For more details: http://sockraw.org/papers/sock_raw
    mySocket = socket(AF_INET, SOCK_RAW, icmp)

    myID = os.getpid() & 0xFFFF # Return the current process i
    sendOnePing(mySocket, destAddr, myID)
    delay = receiveOnePing(mySocket, myID, timeout, destAddr)
    mySocket.close()
    return delay

def ping(host, timeout=1):
    # timeout=1 means: If one second goes by without a reply from the server,
    # the client assumes that either the client's ping or the server's pong is lost
    dest = gethostbyname(host)
    print("Pinging host: " + host + " at: " + dest + " using Python:")
    print("")

    # Send ping requests to a server separated by approximately one second
    while 1 :
        delay = doOnePing(dest, timeout)
        print(delay)
        time.sleep(1)# one second
    return delay

if __name__ == "__main__":
    global numPings 
    host = sys.argv[1] if len(sys.argv) > 1 else 'localhost'
    numPings = input("How many pings would you like to complete?\n")    #set numPings to the number of pings the user wants to complete
    numPings = int(numPings)
    ping(host)