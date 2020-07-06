
Challenge
=========

1) Apache webserver; Configure it to start at server boot, and listening on all interfaces on port 80;
2) Tomcat application server;Configure it to start at server boot, and listening on all interfaces on port 8080;
3) MySQL database server;Configure it to start at server boot, and listening on all interfaces on port 3306;
4) Install the following:
   -- Telnet 
   -- Curl
   -- Nslookup
   -- Oracle JDK  (Alternatively used OpenJDK)

5) Disable firewalls on "ec2_devops" or allow ports 80, 8080, 3306 from anywhere to access the 3 services configured above;


Requirements
------------
Refer to INFO.md

Dependencies
------------
1) Update the inventories/hosts file with your IP address
2) Ensure proper ansible user is accessible password less (optional) 

Playbook Uasge
----------------
1) ansible-playbook -i inventories/hosts httpd-setup.yml
2) ansible-playbook -i inventories/hosts tomcat-setup.yml
3) ansible-playbook -i inventories/hosts mysql-setup.yml


Author Information
------------------
Name: Dinesh
Email: dinesh4k@hotmail.com

