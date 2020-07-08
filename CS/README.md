Case Study: Symbiosis
Symbiosis is a health product manufacturing company and currently on-premises infrastructure. They have recognized the benefits of moving to a cloud infrastructure & would like to evaluate an AWS cloud solution.

Based on their priorities and internal discussions, they have provided you with some high-level requirements which they would like you to implement in the proposed solution. The high-level requirements are as follows:

A private isolated network which would best suit Symbiosis’s 2 tier architectural needs. In order to meet their internal SLA’s they require a highly available solution as well.

Symbiosis being a B2C company, would typically like their web applications to be accessible over the internet and thus handle HTTP traffic.

The database tier should have restricted access (not open to HTTP) and allow traffic only through the web tier. The database tier should allow outbound requests via NAT.

They would like to reduce the administrative burden of managing their SQL database and requires a managed database for their SQL engine in the proposed solution. They need the database to be highly available.

Currently they experience medium to high traffic on their network. The traffic to the web tier is managed by a load balancer which diverts traffic to healthy instances. They would ideally like a Load Balancer with an ability to perform layer 4 (Transport Protocol) and layer 7 (Application) checks while balancing the load. There is no requirement at this point to balance the load on the database tier.

In their current setup, the traffic being inconsistent, requires over provisioning resulting in increased costs. In order to overcome this issue, they would like the new system to allow automatic scaling in the event of a traffic spike.





Assignment deliverables
1) Included web_design.pdf
2) Included sample code (developed in python, flask)
	Pre-requisities:
		a) mysql is deployed 
                b) python v2.7 and above`
	Deployment steps:
		a) Download the folder
		b) Run pip install -r requirements.txt


