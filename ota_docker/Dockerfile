
FROM 32bit/ubuntu:16.04

RUN touch $(date +%s)

RUN sudo apt-get update -y
RUN sudo apt-get install git -y
RUN sudo apt-get install vim -y
RUN sudo apt-get install iptables -y
RUN sudo apt-get install libxml2:i386 -y
RUN sudo apt-get install unzip -y

RUN git clone https://github.com/owen198/afs-sdk.git /root/afs-sdk/
RUN chmod 755 /root/afs-sdk/ota/otapackager-cli

RUN sudo apt-get install software-properties-common -y
RUN sudo apt-get install python-pip -y
RUN pip install flask

EXPOSE 80:80
