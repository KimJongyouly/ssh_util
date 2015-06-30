#!/usr/bin/python

from paramiko import SSHClient, AutoAddPolicy
from scp import SCPClient
import cmd

class RunCommand(cmd.Cmd):
    prompt = 'ssh > '
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.hosts = []
        self.connections = []

    def do_add_host(self, args):
        if args:
            self.hosts.append(args.split(','))
        else:
            print "usage: host "


    def do_add_host_file(self, filename): 
        if filename : 
            f = open(filename, 'r') 
            lines = f.readlines() 
            for line in lines : 
                self.hosts.append((line.strip()).split(',')) 
            f.close()    


    def do_scp_put(self, source):
        target_path = "/home/dba_admin/"	
        for host, conn in zip(self.hosts, self.connections) : 
            scp = SCPClient(conn.get_transport()) 
            scp.put(source, target_path + source) 
            print 'host : %s => %s' % (host[0], source) 
            scp.close()         


    def do_connect(self, args):
        for host in self.hosts:
            client = SSHClient()
            client.set_missing_host_key_policy(AutoAddPolicy())
            client.connect(host[0],username=host[1],password=host[2])
            print 'connect : %s' % (host[0])   
            self.connections.append(client)


    def do_run(self, command):
        if command:
            for host, conn in zip(self.hosts, self.connections):
                stdin, stdout, stderr = conn.exec_command(command)
                stdin.close()
                for line in stdout.read().splitlines():
                    print 'host: %s: %s' % (host[0], line)
        else:
            print "usage: run "


    def do_close(self, args):
        for conn in self.connections:
            conn.close()

if __name__ == '__main__':
    RunCommand().cmdloop()

