#!/bin/bash

# deklarasi array ID
distroLinuxDekstop[0]=BlankOn
distroLinuxDekstop[1]=Ubuntu
distroLinuxDekstop[2]=Debian
distroLinuxDekstop[3]=ArchLinux
distroLinuxDekstop[4]=LinuxMint

distroLinuxServer[0]=UbuntuServer
distroLinuxServer[1]=CentOS
distroLinuxServer[2]=FedoraServer

# cara mengambil nilai array
echo ${distroLinuxDekstop[*]}
echo ${distroLinuxServer[*]}
