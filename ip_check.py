import os
import json
import socket

def results_log(check_ip):
	name_of_log = "test_ip_output.log"
	results_file = open(name_of_log, 'a')
	results_file.write(i + " host ip is " + check_ip + "\n")
	results_file.close()


# vpn1 = 'mickey_vpn'
# vpn2 = 'gensec_vpn'
# vpn3 = 'sprod_vpn'
# vpn = vpn3

input_hosts = (open('test.json', 'r'))
list_of_hosts = json.load(input_hosts)
active_hosts = list_of_hosts["hosts_to_check"]

for i in active_hosts:
	cmd = socket.gethostbyname(i)
	check_ip = cmd.strip('\n')
	results_log(check_ip)
