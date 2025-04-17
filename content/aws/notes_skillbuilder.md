# Comcave College - AWS Cloud Practitioner

**Notizen AWS Skill Builder**

**About:** [About](https://aws.amazon.com/training/learn-about/cloud-practitioner/)

## 1) Basics

#### Roles

**Solutions Architect** - Envisions and manages architecture and demand for cloud services
**Systems Admin** - Configures performance requirements and monitors systems
**Security Admin** - Controlls access and security parameters
**DevOps Engineer** - Configures and makes available deployment piplines
**Developer** - Creates applications to interact with cloud services

## AWS EC2 - Amazon Elastic Compute Cloud

#### What is Cloud Computing?

*=> Computing on-demand with pay-as-you-go pricing
**Infrastructure as a Service (IaaS)**
**Platform as a Service (PaaS)**
**Software as a Service (SaaS)**

#### What it is NOT

**Desktop and Application Streaming (DaaS)

#### Entails

Run all parts of the application in the cloud.
Migrate existing applications to the cloud.
Design and build new applications in the cloud.
**AWS Acceptable Use Policy** - Guidelines what is allowed within AWS usage

## 2) Compute in the cloud - Resources from AWS

#### EC2 Instance Types

**General purpose** - balanced workloads with equal requirements
**Compute optimized** - CPU based batch processing workloads
**Memory optimized** - large data computation with high access rates
**Accelerated computing** - GPU/rendering workloads
**Storage optimized** - large data sets with low access rates
*=> multiple or bigger possible

#### EC2 Pricing

**On-Demand** - no-contract deal to pay by usage, good for pilots, proof of concepts
**Spot Instances** - usage of free capacities, can also give up capacity (allow interruptions)
**Reserved Instances** - contract deal to reserve capacity at fixed up-front price
	- **Standard** - cheapest, 1-3 years
	- **Convertible** - change OS, expensive, 1-3 years
	- **Scheduled** - new, price by usage, high performance short term
	- **Third Party** - most expensive
**Savings Plans** - long-term contract to save on price, 1 or 3 years

#### Elastic Load Balancing (ELB) 

- Disconnects requests from instances by using load balancers on the cloud side
- ensuring no instance has too many requests
- network and instance access monitoring

#### Auto Scaling 

- removes and adds instances as needed
- defined with desired capacity

**Simple Queue Service (SQS)** - allows request queueing to decuple applications/components
**Simple Notification Service (SNS)** - use of microservices, publising and subscribe service structure, allows for multiple but correct recipients

#### Compute Services

**AWS EC2 (just EC2)** - OS level access to Linux/Windows virtualization
**(Serverless) AWS Lambda function** - flexible function run by trigger, runs quick proccesses (<15 mins), no OS level access
**AWS Container Service (ECS)** - Provides single Docker containers, set platform and container configuration
**AWS Kubernates Service (EKS)** - Tool for ECS to provide Kubernates container cluster, as ECS but auto-deploy more containers
**AWS Fargate** - Tool for ECS and EKS to allow Fargate managers to container services for you

## 3) Global Infrastructure

#### Regions

- geographically isolated
- can permit data to be regional or inter-regional
- pick your region with priority:
	1) lawful compliance 
	2) distance 
	3) features needed and available 
	4) tax on price

#### Availability Zones (AZ)

- sets of single or multiple Datascenters within a region, close fibre connections
- regions have 3 minimum zones
- should use at least 2 zones, default by selecting one region

#### Edge Locations

- Cached copies of data to bring closer to customer
**AWS CloudFront Service** local region AZ that extends your other regions, provides these to AWS Datacenters globally, could be used for CDN
**AWS Outpost** add this service to customer locally, special hardware to use AWS at home, low latency, private environment, strech VPC onto this

#### Local Zones

- extensions of regions
- the VPCs can be streched to there
- specific services per region, may have specific new hardware
- capacity extensions, some closer to you, thus lower latency
- for regulatory complience

#### Provisioning (using AWS resources)

*=> AWS provides an API that takes orders from the following
**Console (Browser Interface)** - Gui, for human user interaction, can be fault-prone
*=> use these to build your instance environments, programatically
**Command Line (CLI)** - terminal and scripted instructions
**Software Development Kit (SDK)** - program access, supports C++, Java and .NET

#### Managed Tools for provisioning

**AWS Elastic Beanstalk** - Provide Code and Instruction
**AWS CloudFormation** - Configurations templates in YAML/XHTML with instructions to build from

## 4) Networking

#### Amazon Virtual Private Cloud (VPC)

- private IP range for instances and storages
- contain subnets
- opened up with internet gateway (IGW) for public
- or virtual private gateway (VPN)
- or AWS Direct Connect (in conjuction with provider) fully privatizing access with on-premise connection

#### Subnets and Network Access Control Lists (nACL) and Security Groups

**Subnet in VPC:**
- can be multiple, private or public

#### Network Access Control Lists

- access check packages in- and outbound
- list of denial and allow rules (allows external first)
- stateless without recognition

#### Security Groups

- package checked for access to EC2 instances
- based on protocolls/ports, basically firewall
- only inbound denial, outbound allowed (denies external first)
- stateful recognition, no recheck

#### Route 53 (DNS Service for AWS)

- resolves domain names to IPs
- by Name, Geolocation, Geoproximity or weighted

#### CloudFront (close proximity copy)

- provide CDN for example

## 5) Storage and Databases

**General:**
- all block storage, updating only changes

#### Instance Store

- Instances are NOT permanent storage
- terminated with the instance

#### Elastic Block Store (EBS)

- can store instance data, but permanently
- single Availabilty Zone, instantce must be in same AZ
- Volume defined by size, type and configurations
- drives separated physically from host of instance
- for often changing data

#### Amazon Simple Storage Service (S3)

- just storage, for almost unchanging data, in buckets
- max 5 TB objects
- versioning
- access to single buckets via policies
- varies by access frequency and size of file transfers
- can add lock and write policies to ensure singular writes and many accesses
- data could move between storage solutions to behave as archiving

#### Amazon Elastic File System (EFS)

- multiple Availabilty Zones
- further improves access by making data concurrently available
- thus instance AZ independent

#### Amazon Relational Database Service (RDS)

- allows table parity for databases
- offers automatic patching, backups, reduncancy, failover and recovery
- backup to S3
- supports all major DB engines

#### Amazon DynamoDB

- dynamic tables, non-relational, serverless
- networking and storage solution is scaling and managed automatically
- also handling backups
- good for fast tables
- flexible scheme, has single key (composite possible) and attributes can be added
- only simple queries from single tables
- used by Amazon Aurora

#### Amazon Redshift

- warhousing service for data accross multiple sources
- can create relations between multiple datasets
- Amazon gets insight into the data

#### AWS Database Migration Service

- take existing databases to Amazon DB services
- testing, developing, consolidating
- can access on-going copies (backup like)
- DMS mapping can help translate schemas

**Amazon DocumentDB** - CMS of files and customers, MongoDB
**Amazon Neptune** - graphs and social network data with high relations
**Amazon Blockchain** - mumbo jumbo
**Amazon Quantum Ledger Database** - immovable data
**Amazon ElastiCache** - add fast caching to other DB solutions
**Amazon DynamoDB Accelerator** - add even faster access other DB solutions

## 6) Security

#### Shared Responsiblity Model

Customer for Data **IN** the Cloud, AWS for Security **OF** the Cloud
**Customer** => Data, Applications, OS and UP (who controls updates?)
**AWS** => Physical Location, Hardware and Networking, Performance of Components

#### User Permissions and Access

#### Root user

- is Owner
- should only do limited tasks
- should have MFA
- add admin user with the power to serve permissions

#### Identity and Access Management (IAM) policy

- gives permissions just for specific tasks
- rules written in JSON configuration

#### IAM Groups

- define groups to organize users, roles and sub-groups

#### Role

- temporary access rules
- given not on identity basis, but adoptable by user identity

#### AWS Organizations

- central place to organize multiple accounts
- hierarchial grouping by **Organizational Units (OU)**
- consolidated billing AND
- use **Service Control Policies (SCPs)** to define maximum permissions for individual accounts and OUs

#### Compliance

- rules by law and audits
- both access and logging of access
- **can already be provided by AWS and locked to region**
- set on creation as AWS Artifact Agreements, and require documentaiton via **AWS Artifact Reports**

#### Key Management Service (KMS)

- requests and traffic is grouped into secure sources - using encryption Keys
- sinage as protection

#### AWS Shield

**Standard** - analyses in real time, behavioral traffic watch
**Advanced** - using CloudFront, Route 53 and ELB to mitigate DDoS attacks, can add WAF

#### Web Application Firefall (WAF) 

- to only allow listed requests
- managed rules group from AWS, plus custom rules, plus 3rd party
- can limit access rate

#### Additional Sercurity Services

- encryption keys for resting data
- SSL protocol for in-transit data
**Amazon Inspector** - automated security audit of EC2, reports irregularities in software
**Amazon GuardDuty** - Log checkup, whitelisting and blacklisting using WAF

## 7) Monitoring and Analytics

#### Amazon Cloud Watch

- watching live metrics, centralized
- can create alerts/alarm on tresholds
- this can trigger an action, messages via SNS included
- add metrics to your dashboard

#### AWS CloudTrail

- auditing all interactions with cloud systems
- every request is recorded by user, with results and states, big brotha
- What, Who, When, How
- filtering and searching these logs

#### AWS Trusted Advisor

- see warnings for best practices and general optimizations
- Cost, Performance, Security, Fault Tolerance, Service Limits or Sustainability
- Green check show no issues, Yellow warnings and Red Errors

#### AWS X-Ray

- track single requests/messages/calls
- error tracing

## 8) Pricing, Billing and Support

#### Free Tier

- choice between always free services, 12 month deal, trial/test periods for services

#### Pricing Concepts

- pay for what you use
- pay less when reserving
- pay less with volume-discounts
[calculator](https://calculator.aws/#/)
**Example:** 
[example](https://calculator.aws/#/estimate?id=0b8763ce9ee96dc24d8b825845e3a227d7f3778b)

#### Billing Dashboard

[what is billing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-what-is.html)
- current and forecast amounts
- Bills show usage by service as tree
- summary of bills accross services
- highest costing service
- account cost trend

#### Consolidated billing

- AWS Organisations (IAM) can be assigned single bill for all accounts under
- also combines usage for bulk/volume discounts

#### Budgets

- **prevent overspend**
- Budget amount, with renewal and interval
- create alert tresholds, could even use forcast
- actions on threshold
- updates 3 times a day

#### Cost Anomaly Detection

- **prevent overspend**
- reduce cost surprises with ML

#### Cost Explorer

- **visibility**
- cost over time, by date
- monthly trend
- visualizes cost accross services
- can create reports and CSV download
- group by region, or tags (services can be tagged to show cost responsibility)

#### Cost and Usage Reports

- **visibility**
- reports created by Cost Explorer
- transferable as CSV download

#### Support Plans

[support plans](https://aws.amazon.com/de/premiumsupport/plans/)
**Basic** - customer service, forums, limited Trusted Advisor, Documentation
**Developer Support** - best practices, client-side Diagnostigs, building out projects in tandem
**Business Support** - **all AWS Trusted Advisor checks**, < 1h response time, single TAM max
**AWS Enterprise On-Ramp Support** - 30 min, access to **Techinal Account Managers (TAMs)**
**AWS Enterprice** - all above, 15 min response time, **designated TAM**

#### Techinal Account Managers (TAMs)

- built AWS Architecture, test and provide best practices
- secure systems
- check costs

#### Market Place

- 3rd Party**!**
- get established software solutions that run on AWS
- find contractors and managers to run projects
- one-click products

## 9) Migration and Innovation

#### AWS Cloud Adoption Framework (AWS CAF)

- Perspectives to view adoption for
**Business** - Boss CEO and Owners, Shareholders, Finance managers, Strategy matches IT
**People** - Employee requirements, Skills, positions
**Governance** - Investments, Stakeholders, Shares Manager, auditing risk and cost, IT matches Strategy Budget
**Platform** - Technical requirements, limits and solutions
**Security** - Identities, Accesses, Control and Visibility
**Operations** - Business years/quaters, flow of operation, Support

#### Migration Strategies:

**Rehost** - Lift&Shift, move for just base improvements or savings
**Replatforming** - add tinkering to adopt new platforms, no logic changes, staying up-to-date
**Refactore/Re-architect** - rebuilding program, for massive feature and performance improvements, very costly
**Repurchase** - buying new software to adapt, with almost not logic changes, expensive up front
**Retain** - keeping some applications around to re-reference or archive before shutdown 
**Retire** - deciding which applications to shut down, discontinue
**(Re-architect)** - technically different from refactoring, changing service architecture, HOW the applications/services interconnect
**(Relocate)** - move within AWS hosts to new region, VPC, edge location

#### AWS Snow Family

- collecting **physical devices** to move giant datasets physically instead of upload strain and cost
- Secure devices varied by size, all are secure:
**Snowcone** - Small device handle AWS request in-house, 2 CPUs, 4GB mem, 14TB storage
**Snowball** 
	- Storage Optimized - 40 vCPUs, 80 GiB memory, 1 TB SSD, 80 TB storage
	- Compute Optimized - 104 vCPUs, 416 GiB memory, Tesla V100 GPU , 28TB NVMe, 80TB storage
**Snowmobile** - Exabytes of storage, can transfers 100 PB per Snowmobile

#### Innovation with AWS

- make use of:
- virtualization, testing and readonly environments, serverless
- artifical intelligence, machine learning, AI job replacements (Amazon SageMaker)
- connected devices IoT
- satellites

## 10) The Cloud Journey

#### The AWs Well-ARchitected Framework
**Operational Excellence** - run and moonitor system, smooth operation, automation, run things with code
**Security** - protection, recovery, and access
**Performance Efficiency** - Performance is met and up-to-date
**Reliabilty** - backup and load balance, growing with demand
**Cost Optimization** - Only run as needed, lowest price possible
**Sustainability** - Environmental impact consideration
*=> Trusted Advisor is the checking tool for all these

#### Benefits of the AWS Cloud

- Service variety
- **Variable expense** instead of **upfront cost**
- **economy at scale**, paying only what you use, not direct size of datacenter
- capacity growing with AWS
- **speed and agility** to further update and migrate
- **global accessebilty** and improvement in **latency**

## Cloud Aquisition

**CSP** Cloud Service Provider

#### Cloud Procurment

**Procurements** - shifting to pay by usage, upfront cost replaced by variable cost
**Legal** - define terms exactly and early to determine cloud services, avoid hardware terms and adopt cloud/global reach
**Security** - know audit schedules, know service access permissions and capabilties rather than hardware access
**Gevernance** - bring over existing management standards into the cloud
**Finance** - evaluate cost accross CSPs
**Complience** - early determine your CSP can fulfill your compliance needs

#### AWS Partner Network (APN)

- Partners specialized on each service
- help with adoption and best practices
- consider requirements and migration steps
- managed services, competency or service specialists
- can be consulting, management, full support,... in nature

#### Rethinking Procurement

Fixed => flexible
Single purpose => New Outcomes
Traditional Goals => Innovation

#### Educating Stakeholders on Buying Cloud

**Security Professionals** - get assurance of control and audits
**Human resources** - inform about training and roles
**Finance** - prepare for usage cost, spending is less fix and can peak
**Program managers** - need to learn shared responsibility model, deploy with greater visibility

#### Procurement of Experts

*=> you are only buying cloud infrastructure
- not for the infrastructure, but of it's use
- solution design
- management of services
- migration and implementation

#### Key Aspects of Procurement

**Pricing** - avoid over procurement by knowing your demand
**Security** - Infrasturcture, Software and Platform as a Service requires knowing each responsibility
**Governance** - have no required minimum commitments or long-term contracts, remain owerner of your data, and flexibilty to move CSPs
**Terms and conditions** - Cloud computing is a commercial item and be treated as such, term and conditions with the CSP must suit your needs

#### AWS Activate

- special offer for Startups
- maybe