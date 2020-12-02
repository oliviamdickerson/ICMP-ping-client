For this assignment, I implemented a number of global variables in order to keep track of the various RTT variables as well as the counter variables for the number of pings sent and received, and the number of packets lost. In the receivedOnePing method, I unpacked the ICMP header to get the type, code, checksum, id number, and sequence number. I then proceeded to get the time that the ping packet was sent to calculate the RTT of the current packet in question. Then, I updated the various RTT variables (add to RTT sum, check for new max or min RTT, and increment the count), then I printed the round trip time of the current packet to the terminal. 

Terminal Output For Ping to oxford.ac.uk (Europe):
Olivias-MacBook-Pro:downloads oliviadickerson$ sudo python3 pa03.py
Password:
How many pings would you like to complete?
10
Pinging host: oxford.ac.uk at: 151.101.130.133 using Python:

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 9.798049926757812 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 9.264945983886719 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 8.381843566894531 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 9.999990463256836 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 9.540081024169922 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 10.390996932983398 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 9.947061538696289 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 9.071111679077148 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 9.530067443847656 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 9.930133819580078 ms


Ping Statistics:
Num pings sent: 10, Num pings received: 10, Minimum RTT: 8.381843566894531 ms, Maximum RTT: 10.390996932983398 ms, Average RTT: 9.585428237915039 ms, Packet Loss %: 0.0

Terminal Output for Ping to sydney.edu.au (Australia):
Olivias-MacBook-Pro:downloads oliviadickerson$ sudo python3 pa03.py
Password:
How many pings would you like to complete?
10
Pinging host: sydney.edu.au at: 129.78.5.8 using Python:

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 293.5307025909424 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 228.62911224365234 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 225.9979248046875 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 228.03497314453125 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 229.0501594543457 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 225.2798080444336 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 227.11610794067383 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 227.97608375549316 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 227.69975662231445 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 228.5158634185791 ms


Ping Statistics:
Num pings sent: 10, Num pings received: 10, Minimum RTT: 225.2798080444336 ms, Maximum RTT: 293.5307025909424 ms, Average RTT: 234.18304920196533 ms, Packet Loss %: 0.0

Terminal Output for Ping to uba.ar (South America):
Olivias-MacBook-Pro:downloads oliviadickerson$ sudo python3 pa03.py
How many pings would you like to complete?
10
Pinging host: uba.ar at: 157.92.5.15 using Python:

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 204.25987243652344 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 228.18398475646973 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 188.12203407287598 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 174.79205131530762 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 216.48883819580078 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 205.49893379211426 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 251.2490749359131 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 170.72677612304688 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 277.63986587524414 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 223.22320938110352 ms


Ping Statistics:
Num pings sent: 10, Num pings received: 10, Minimum RTT: 170.72677612304688 ms, Maximum RTT: 277.63986587524414 ms, Average RTT: 214.01846408843994 ms, Packet Loss %: 0.0

Terminal Output for Ping to stonybrook.edu (North America):
Olivias-MacBook-Pro:downloads oliviadickerson$ sudo python3 pa03.py
How many pings would you like to complete?
10
Pinging host: stonybrook.edu at: 129.49.2.176 using Python:

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 2.9659271240234375 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 4.520893096923828 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 5.900144577026367 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 4.856109619140625 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 5.005836486816406 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 5.705833435058594 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 9.201288223266602 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 5.094766616821289 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 5.164146423339844 ms

[<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=1, laddr=('0.0.0.0', 0)>]
Round trip time for this ping: 5.059719085693359 ms


Ping Statistics:
Num pings sent: 10, Num pings received: 10, Minimum RTT: 2.9659271240234375 ms, Maximum RTT: 9.201288223266602 ms, Average RTT: 5.347466468811035 ms, Packet Loss %: 0.0