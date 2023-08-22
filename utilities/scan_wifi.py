from scapy.all import ARP, Ether, srp

# Set target IP range
target_ip = "192.168.2.0/16"

# Create ARP request packet
arp = ARP(pdst=target_ip)

# Create Ethernet frame packet
ether = Ether(dst="ff:ff:ff:ff:ff:ff")

# Combine Ethernet and ARP packets
packet = ether/arp

# Send packets and collect response
result = srp(packet, timeout=3, verbose=0)[0]

# Extract device IP and MAC addresses from response
devices = []
for sent, received in result:
    devices.append({'ip': received.psrc, 'mac': received.hwsrc})

# Print out results
print("Devices on the network:")
print("-----------------------")
for device in devices:
    print("IP Address: {}\tMAC Address: {}".format(device['ip'], device['mac']))
