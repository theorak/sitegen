# Comcave College - AWS Cloud Practitioner

**Notizen Kappes Kurs**

**Anwesenheiten:**
UE = 45 Minuten x 10 pro Tag ab 08:00 Uhr

**Zertifiatsprüfung:**
[cert cloud practitioner](https://aws.amazon.com/de/certification/certified-cloud-practitioner/)
90 Minuten - 65 Fragen / Verlängerung max. 30 Minuten.
700/1000 Punkten für Bestehen
Pearson-Vue-Prüfungszentrum oder Online-Beaufsichtigung - finden?

**AWS console (Example Account):**
[AWS console](https://kurs-account-3.signin.aws.amazon.com/console)
Roensch - User

#### Questions and Examples:

TYPO3 on AWS
- [typo3 scalability](https://typo3.com/blog/typo3-on-aws-scalability-and-performance)
- [typo3 on aws](https://t3planet.de/en/blog/install-typo3-on-aws/)

## Benefits of the Cloud

- agility
- fixed/upfront expenses become variable expenses
- elastic, horizontal scalabilty
- pay by usage

## Instance Access Management (IAM)

- accounts stored globally (your whole AWS setup)
- to use IAM Identity Center is new best practice
**root user** - only owner (should create admin for permissions)
**user** - any admins, should use MFA, can be assigned roles, can be grouped
**roles** - only assumed for specific permissions/tasks, temporary
**format** - acount@account-group

#### IAM Policy

- JSON format document/ruleset
- allows and denies access to AWS services and resources

#### IAM Roles

- sets of IAM policies that result in roles
- can be account agnostic, but must choose one
- can be restricted to specific cloud services
- can be defaults or custom permissions
- ARN key as role ID
- saved internally as JSON configuration
- 'assume a role' is a required permission to hand it out

**Console user access** - User ID + password + MFA
**Programatic user access** - access key ID + secret access key, max 2 per user
**AWS Acceptable Use Policy** - Guidelines what is allowed within AWS usage

#### AWS Organizations

- contain multiple accounts and organizational units (these are NOT groups)
- can add organizational units (OU) to create IAM group hierachy
- consolidated billing AND
- service control policies (SCPs) for single account or OU, as umbrella definition of maximum permissions
- each comes with full access control policy, stacked with other deny policies

#### Identities and Providers

**Principal** - entity allowed or denied access, IAM user, IAM root user, IAM role, service, defined in policy doc
**Identity** - the principal's credentials, identifier, access key or password/username, verifier
**Federated Identity** - single-sign on (SSO), access for groups, additional access without logins
- can use SAML 2.0 or OpenID, add application
- create in IAM center, as federated user to gain SSO domain data
- add identity source connect personal information from AWS Managed Active Directory or Microsoft AD or other external providers (Google Workspace, Okta, Cyber Ark, ...)

#### AWS Managed Active Directory

**Directory Services** - store and mange access to resources, can be AWS Cloud, MS or other providors
- AD Connector is self-managed MS AD, allows to add Win user identities to instances
- simple AD is legacy tech (based on region)
- Windows Instance could use this (Domain join directory and IAM instance profile)
- multiple domain controller possible, for extra cost
- can be useed for RDP access

#### Control Tower

- setup multi-account environments
- automated account distribution
- distribute identities

#### Cognito

**User Pools** - add sign-ins and sign-up **Identities**
**Identity Pools** - distribute **Federated Identities**
**Cognito Sync** - cross device syncronization, also can use AppSynch
- authorization for web and mobile apps
- so either create AWS managed users or translate access credentials into AWS credentials

#### Policy Builder:

[policy builder](https://awspolicygen.s3.amazonaws.com/policygen.html)

## EC2 Instances

#### Browsing EC2 Instances

[instance types](https://aws.amazon.com/ec2/instance-types/)
- instances in various sizes with unique keys (Kennungen)

#### Pricings

**On-Demand** - per instance hour, second accurate, pilots and poc
**Spot** - save price by using spare capacity, stateless workloads, can be interrupted
**Reserved** - specific workloads, by increasing price: Standard, Convertible, Scheduled, Third-Party
**Saving plan** - specific workloads and availability, can't be resold

#### Tenancy options

**Dedicated Instance** - instance reserved
**Dedicated Host** - hardware reserved, costs most
*=> pick price and payment options, based on availability
*=> only with running instance costs are tracked

#### Launching an Instance

- Name it, tag it
- Pick Amazon Machine Image (AMI), which OS to use
- instance type, fitted for your requirements and price
- key pair for login
- Network settings, for multiple instances and remote access
- Storage, as per your application requirements
- Details, adding domain, IAM profile for this instance, launch and restart, tenancy, launch scripts
- Save and Launch possible

#### Running Instance:

- can't change type
- change security options, access roles, clone, ...

#### AWS CloudFormation:

- stores templates for launching EC2 instances, VPC, S3 buckets
- Configurations templates in YAML/XHTML with instructions to build from
- see Architecture - Solutions Library for example templates

**Access Key Pairs** - see access key created for instances
**Network Interfaces** - see wich networks are connected for each instance, eni>subnet>VPC routing

#### Terraform

- not AWS exclusive, can deploy accross different Clouds

## Networking

#### Virtual Private Cloud (VPC)

- **virtual networks**
- **subnet rules for VPC**
- Region > Availability Zone > VPC (cross-zones) > Private Subnet/s (IP addressable, assigned to AZ)
- can have NAT, CIDR (notation for subnet mask), identifying tag

#### Internet Gateway

- add to VPC
- allows internet access per VPC
- opening for traffic

#### Routing Table

- define Subnets with routing tables
- destination for traffic
- public IP-Addresses for Instances (can be elastic)
- so far IPV4 based, that cost
- adding both a IGW and subnet to the same table, makes that subnet public
- first 5 IPs are reserved for routing, gateway, DNS, broadcast, spare

#### NAT Gateway

- lies in public subnet
- allows to share internet access to private subnet
- should be reduncdant across AZs as well
- costs

#### Network settings of EC2 instance

- select VPC
- assign the instance to a subnet
- assign a security group (max 5)
- additional IPs possible

#### Security Group:

- **virtual firewall for EC2 instance**
- default deny inbound
- default allow outbound
- stateful package recognition

#### Network Firewall

- **virtual firewall as subnet** (its own)
- to chain before other subnets
- based on surica firewall rules
- stateful and stateless rules

#### Network Access Control List (network ACL)

- **virtual firewall for subnet** (attached)
- default ACL allows interaction with the subnet
- default allow all
- custom starts with deny all
- rules matched top to bottom
- stateless, no traffic recognition

#### Connection Options for EC2 instance:

- security groups should first open ports for used protocols
- **SSH connections** are available via generated key-pass
**Instance Connect** - IP-based service into instance console

#### Systems Manager 

- can **create sessions to SSM agent within the instance** (AWS-provided images)
- can group instances to give all the same commands
- that requires user permissions via IAM (SSMManagedInstanceCore)
- add this role to instance
- does not need additional SSH, port or Security Group rules
- interaction will be as ssm-user

## Storage Services

#### Storage Overview:

**Block Storage** - Elastic Block Storage (EBS), Instance Store - stores on networked or dedicated drives
**File Storage** - Elastic File System (EFS), FSx - stores across AZ, single region
**Object Storage** - Simple Storage Service (S3), S3 Glacier - stores in region, can clone across region

#### Elastic Block Store (EBS)

- **block storage**
- **networked distance drive**
- storage for instance
- equal-sized block of data
- will cost additionally
- root volumes terminate with instance, additional volumes don't
- volumes can be snapshotted, saved, restored, cloned
- single availabilty zone, same as the instance

#### Instance Store:

- **dedicated block storage**
- **physical drive close by**
- storage for instance
- usually SSDs for fastest operation
- only temporarely, deleted with instance shutdown, never stored

#### Elastic File System (EFS)

- **file storage system**
- shared access possible
- **scalabe file system (NFS v4)**
- can open linux mount points for your applications or EC instances
- multiple availabilty zones, for high redundancy
- storage classes: Standard, Infrequent Access, One-Zone (single AZ)
- offer ready for compliance laws

#### Amazon FSx:

- for non-Linux file systems
- **Windows File Server, Lustre, NetApp ONTAP, Open ZFS**

#### Amazon Simple Storage Service (S3):

- **object storage**
- **create buckets as needed**
- AWS controlls creation and management
- optimized for different data use cases
- bucket names must be unique, becomes part of domain
- can use **IAM roles/user or bucket access policies**
- allows versioning, tagging, encryption and external access
- keeps all files with their metadata
- object lock forces WORM (write once read many)

#### Bucket Access Policy:

- needs statements
- will enforce access via tokens
- could (not recommended anymore) host static websites

#### Bucket Access Lists and Access Points:

- grant access with sub path per IAM role/user

#### S3 storage classes:

**Standard** - frequently accessed, high redundancy
**Standard-IA** - infrequenly accessed, lower storage price, higher retrieval price
**One Zone-IA** - infrequenly accessed, store data in a single AZ, lower storage price
**Intelligent-Tiering** - monitored, adjusted on access behavior, automation fee cost
**Glacier Instant/Flexible/Deep Arcive** - access in milliseconds < minutes to hours < 12 hours for retrieval
	- fastest is most expensive, last being cheapest
	- Glacier interaction usually via SDK

#### S3 Pricing:

- based on **storage type, space and access fequency, object size**
- more space, deeper storage, higher price
- less frequency, lower price
- larger transfers, volume discount
- reading data costs, into other regions costs

#### S3-Multipart-Upload:

- uses multiple network connections to upload in parts
- speed-up
- can be paused

#### S3 Events:

- tagging, creation, deletion
- sends SQS messages to lambda functions
- eg. creating thumbnails, informing changes, event tracking

#### S3 Transfer Acceleration

- get edge locations for specific buckets
- for faster access to this bucket
- if you often have large transfers to this bucket

## EC2 Autoscaling and Elastic Load Balancing

#### Architecture Plan

- **target architecture**, your instances and storages should be scalable and elastic
- **n-tier web application architecture**
- architecture should split into **purpose built/configured servers**
	- eg: Browser <> Web Server <> Application Server <> Data Server
	- secured separatly as well
	- load balancer can then be established in multiples
	
**Example Solutions:** [solutions](https://aws.amazon.com/solutions/=
	
#### AWS Load Balancing

- **IP, instance and protocol health checkup**
- **all in single VPCs**
- accross subnets, access to instances
- tier for each web or app instances separatly
- security group for instances in same tier must allow load balancer
- network ACL already allows access to subnets
- can tage Certificates from ACM, IAM or imported personal (still needs Route 53 for domain name of that certificate)

#### Application LB

- **network layer 7, applications**
- IP, instance and lambta
- round-robin algorithm
- ports 800, 443

#### Network LB 

- **network layer 4, transport**
- IP, instance and ALB
- flow hash

#### Gateway LB 

- **Network layer 4 and 7**
- IP and instance
- proxy does not terminate
- routint table lookup

#### Classic Load Balancer

- **legacy load balancing service**
- for old applications of the EC2-classic network

#### Creating Load Balancer config

- choose type of **ALB, NLB, GLB**
- network, pick one VPC and AZs
- target group, instances and protocol to check, specific IPs or sub URL paths
- connection to other services
- creates subgroups automatically to start managing (results in public IPs that cost)

#### EC2 Autoscaling Group

- **configuration for instances**
- **adds more instance clones of instance**
- can set minimum, desired and maximum, as well as temporal plan
- no extra cost, as long as maximum is defined
- also provides redundancy, by replacing instances
- target tracking scaling, automtic change desired capacity by metric

#### Creating Autoscaling config

- **requires launch template**, containing descriptions for instance launch (can create from existing instance), at least Amazon Machine Instance
- **network settings that matches the instances**
- add script to show metadata, this helps to separate them
- launch options to control hardware extensions in line with reservation/billing plan
- network should select subnets from at least 2 zones
- set size minimum, desired, maximum

## Billing and Pricing

#### Cost Control

- creating estimates [calculator](https://calculator.aws/#/)
- services and instances, storage, transfer inbound, IPs, Monitoring, ... 
- IAM access to billing [iam access](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started-account-iam.html)

**Cost Explorer - shows accumelated cost by date, and especially usage, forecasting
**Cost Explorer Reports - can save filters as report
**Bill - per account, shows cost per service usage as tree
**Cost allocation tag - management can create tags for users, to group cost
**Free Tier - overview of free contingents used
**Budgets
	- set budget limit and warnings
	- budget warnings can be set for thresholds
	- threshold warning can follow with action to shutdown instance or prevent IAM role from starting new

## Databases

- should be chosen on use case, **relational (more commmon)** vs **non-relational databases**
- SQL language also used most commonly
- should have main username and password

#### Managed Services vs Unmanaged Services

- AWS handels up to scaling, unmaged only up to OS install
- you handle only Application optimization, unmanaged down ot OS updates
- **either you install DBs in EC2 instances, or use a DB Service by AWS**

#### Amazon RDS

- selection of commonly used engines, version and license can be provided
- Deployment options single AZ (free tier), multiple AZs or with reading endpoints, for redundancy and faster access
- selection of Storage type SSD/HDD/speed
- assign VPC and group of subnets
- Encryption and backups possible
- patching by AWS, with control over major versions, costs maintenance fee
- comes with default subnet, routing should be set to connect with your active security groups or even load balancer group
- **NOT global** need read copies or CloudFront

#### Amazon Aurora

- **DB engine choice**
- managable like other RDS, **extends into managed by AWS by:**
- creation of clusters for extreme redundancy, backups, failure response in multiple AZs
- up to 5 replicas, readonly, but help with availability in another AZ
- **can be created serverless**
- reduces to access cost instead of upkeep
- adds speed
- can use AWS DMS for hetrogenous (mapping/conversion) migration
- can be used to create asyncrhonous cross-region replication (for pilot light)

#### Amazon DynmoDB

- **non-relational, non-SQL, flexible scheme DB, serverless**
- good for fast and lots of access
- tables have one key (or composite) and additional attributes
- AWS managed redundancy and availability
- controlled by write capacity units (WCUs)

#### Amazon ElastiCache

- add fast caching to other DB solutions
- must get caching orders from application

#### Amazon DynamoDB Accelerator

- add even faster access other DB solutions
- automatically adds acellerating instances to DynmoDB

#### Databse Migration Service (DMS)

- DMS can map and migrate existing MySQL Sources to AWS DB Services

## Monitoring and Analytics


#### CloudWatch

- **live data monitoring**
- metrics, can add alarms and actions to trigger with tresholds
- see network, hardware usage, disk writing, health checks, interactions, ...
- groupabe per instance or auto scaling groups
- additional data from the OS could be tracked by seting up an agent on the OS
- serverless services can show at least WCUs and RCUs
- network interface tracable, Flow logs to CW logs

#### CloudTrail

- **track user activities throughout API request** (same-source tracking)
- get interactions accross all services
- discover irregularities

#### Event history 

- already provides some default actions overview (e.g. instance terminations)
- event records give detail about the whole interaction

#### Event Types 

- Management
- Data
- Insights
- Network activity

#### AWS X-Ray

- **track usage patterns of AWS services** (NOT users)
- for auditing user-requests
- from request point through networks into storages and back

#### Trusted Advisor

- **provides checks based well-architected framework guidelines**
- optimization for performance, cost optimization, fault tolerance, service limits, operational excellence
- automatic but real-time
- can achieve best practicies
- way more check in paid version, at least AWS Support plan
- **service limits/quotas** especially **can control how and when limits for your plan are reached**
	- to request limit increase, like for vCPUs => contact AWS, adjust plan
[vpc service](https://docs.aws.amazon.com/general/latest/gr/vpc-service.html)

#### AWS Well-Architected Framework

[well-architected](https://aws.amazon.com/architecture/well-architected/)
- **Pillars of Best practices**
- can lookup guidelines here
**Scalability and Stabilty** - Decoupling: Messages and queues, asynchronus processing, tolerance for failed steps, absorbing spikes in demand
**Operational Excellence** - has monitory, is running, processes work
**Security** - access and permissions set as needed, never too many, has MFA
**Reliability** - workloads and availability balance works
**Performance Efficiency** - performance is fast, workload requirements (speed not size)
**Cost Optimization** - budget and plans are not exceeded, unneccessary spending avoided, think of auto-scaling (downscaling only) to reduce cost
**Sustainability** - environmental impact is minimized, downstream reduced, properly terminated unused space, SIZING workloads

## Network Scaling

- all these can be layered to **create more secure or centralized network structures**

#### Service Direct Endpoints

- **Gateway Endpoint for multiple services possible**
- do not need additional internet access
- allows subnets to talk accross VPCs, within the region
- for S3, Dynamo DB this Gateway allows regional access
- **Elastic Network Interface allows this from AZ to AZ** for many services

#### Create Endpoint

- give name
- choose type of: SDE, EC2 Instance Connect, use NLB and GWLBs, PrivateLink

#### Connect VPCs - VPC Peering

- if address ranges do NOT overlap, otherwise this will be disabled
- **ONLY in pairs (non-transitive / Edge-to-Edge)**
- then all traffic can be routed to other VPC
- accross regions

#### VPC Transit Gateway

- **multiple VPCs can be connected**
- routing config of TG controls directions
- can passthrough internet access from a single public subnet
- saves money on public IPs, only extra cost from TG
- limited to region

#### Virtual Private Gateway

- **VPN** between personal router and VPN Gateway of the VPC

#### AWS Direct Connect (DX)

- **dedicated connection** via locations between private router (on-premise) and AWS Cloud
- endpoints meet at that location

#### CDN Network - CloudFront

- **using edge locations** with closer proximity to users
- provides faster access
- restricted access groups
- global service (across all regions)
- can enforce features like HTTPS, Caching, Domain features
- uses the AWS Backbone to open Edge-to-Edge closer to request origin instead of Internet

#### Route 53 - DNS Services

- **DNS server, IP lookup for AWS cloud services**
- connects to Load Balancers
- Variants: Simple Routing, Weighted, Geolocation, Latency, Failover, Multivalue answer, IP-based, Geoproximity
- all are HTTPS, thus needs TLS certificate

#### Global Accellerator

- can **add more edge locations** to speed up access to your services
- routing to more regions
- like inter-regional load balancing

## Security

- all of these cost extra

#### Web Application Firewall (WAF)

- create **Web Access Control List (wACL)**
- **Allow and control Lists**, plus managed rule group from AWS, plus 3rd Party
- can limit access rate
- protection agains SQL Injections, DDoS, ...
- attached to Load Balancer for example

#### AWS Shield:

- Protect additionally **against DDoS**
**Standard** - using CloudFront, behavioral
**Advanced** - adding WAF and Route 53 in conjunction - can mitigate more sophisticated attacks

#### Amazon GuardDuty

- **Log checkup, whitelisting and blacklisting using WAF**
- analyzes network and account activity

#### Amazon inspector

- **looks into EC2, Container and Lambda functions for irregularities**
- checks subgroups

#### Amazon Detective

- analyzes security config itself

#### AWS Config

- checks all your configuration
- track configuration changes
- changes on services

#### AWS Key Management Service (KMS)

- a**dd encryption to transfers and key services**
- requests and traffic is grouped into secure sources 
- sinage as protection

#### Amazon Macie

- for S3
- **protect data by discovering sensitive data using machine learning** (let AWS scrub your data, sure)
- generates data reviews for you to check
- Security Hub and GuardDuty can also show you Macie data

#### AWS Security Hub

- **new central point to consolidate all Security event messages**

#### Secrets Manager

- **for your Databases and API Keys, Oauth token**
- encrypted by manager or custom options
- backup replicas in other regions
- can add automatic rotation
- programatic access to secret

#### Systems Manager / Parameter Store

- **can store enviroment variables for your Instances**
- also secure keys

## Serverless Services and Event Services

- **part of the decoupling**

#### Simple Notification Service (SNS)

- **Messages are not directional send, but pulished under topics**
- subscribers to topics get messages immediatly
- various services: JSON, email, SMS, mobile push, http/https, AWS Lambda, Amazon SQS, Amazon Data Firehose

#### Simple Queue System (SQS)

- **send, store and recieve messages between components**
- **can hold messages** for failures, retries, waiting order

#### AWS Lambda

- **simple single purpose function/service**
- can take messages and respond
- some code (Java, Python, Node, C#### )
- only costs for execution time, you should set limits!
- can connect to Databases or Buckets, various Services
- should NOT be chained, but call SNS/SQS
- has size limits at some point
- Firecracker (3rd party) micro VMs could be used to have mini containers
- can use SAM, SAM Repo or CDK to launch

#### Step functions / state machines

- allows well-formed lambda: chaining, catch/retry, parallelism, branching
- state machine: next step should only be reachable after state changes
- Coordination OR Collaboration
	- have central control through step functions
	- OR have event driven via message services

#### API Gateway

- **makes Lambda functions available outside**
- has response cache
- monitored by CloudWatch

#### AWS Serverless Application Model (AWS SAM)

- templates to start your Lambda applications
- using CLI instructions to interact via the API Gateway
(simpler than Cloud Formation templates 1:50)

#### Elastic Container Registry

- **required location to set up container images**
- can then be usesd by the others

#### Elastic Container Service (ECS)

- **runs and scale Docker containerized applications**, set platform and container configuration
- can interact via API

#### Elastic Kubernates Service (EKS)

- **run and scale Kubernates container cluster**, as ECS but auto-deploy more containers
- Kubernetes updating of applications

#### AWS Fargate

- **allow Fargate managers to manage ECS and EKS services for you**
- turns container usage into serverless, paying only for usage
- removes choice of instance types though!

#### AWS AppSync

- without server config, **great for proof of concept applications (POC)**

#### AWS Kinesis Data Streams

- **real-time data streams**
- dashboard application that can run on EC2 instances

#### AWS Developer Tools Suite

**CodeBuild:**
- compiles and runs codes, runs unit tests, produces artifacts for deploy
- server build tools like Apace, Maven, Grade, etc.
**CodeCommit:**
- source control service (SVC)
- host private git repositories
- deprecated
**CodeDeploy:**
- deployment serves to compute services like EC2, Lambda or Servers
**CodePipeline:**
- delivery servie, visualices, builds test and triggers deploy
**CodeStar:**
- notifications service to triccer the others
- thus managinc, creating and allowing to work with software
**AWS Cloud9:**
- API in the cloud, for lambda, etc.
- deprecated
**AWS Code Whisperer**
- AI assisted AWS coding
- compatible with the services

#### Elastic Beanstalk

- service to scale application building
- automate launching applications
- a mix of resource configuration and automation
- dedicated console

#### AWS Service Health Dashboard

- **view all services**

#### AWS Personal Health Dasboard 

- **proactive warnings, event base**

## Migration

#### Snow Family
[see skill builder notes](/aws/notes_skillbuilder.html)

#### Storage Gateway

[storage gateway](https://docs.aws.amazon.com/storagegateway/)
- per service/source type S3 Files, FSx Files, Tapes, Volumes
- APi available
- programattic entrance to storage

#### AWS DataSync

- **discovery and migration service**
- automated transfers 
- for edge storage and cloud to cloud
- replication
- can use on-premise agend to automate long uploads

#### AWS Transfer Family

- **secure transfer from AWS Storage**
- using SFTP, AS2, FTPS, FTP, etc.

## Cloud Apoption Framework (CAF)

- **model** that informs about **adopting cloud services and best practices**
- view under different specific **perspectives**
- Foundational > Transformational > Business Targets
- highlighting benefits when using more Cloud tools and automation, doing refactoring
- have company wide plan rather than department solutions
[cloud adoption framework](https://aws.amazon.com/cloud-adoption-framework/)

#### CAF Percpektives

**Business** - shareholders and chief are happy
**People** - organized teams to AWS specialists, learning possible
**Governance** - stakeholders are happy, organizational benefit
**Platform** - technology fits scale and level of integration
**Security** - complience and access control 
**Operations** - technical requirements

#### Transformation Domains

**Technology** - use cloud only services
**Process** - digitizing, automation, use new technologies
**Organization** - new teams and methods for them to interaction, improved agile deployment
**Product** - improve the product and how it is served

## Analytics in AWS

[datalakes and analytics](https://aws.amazon.com/de/big-data/datalakes-and-analytics/?nc2=h_ql_prod_an_a)
- former Amazon Kinesis services
- streaming liv data for transformation and analysis and saving it

#### Amazon Kinesis

- transfer video, sensor and audio streams
- directly readable
**Video streams** - video, analytics and machine learning, re-streaming to other methods
**Data Streams** - data, scales for real-time data
**Data Firehose** - buffering, transform, before sending to other storage services like AWS file storage or analytics
**Managed Service** for Apache Flink/Kafka - transform with SQL or Apache Flink into Databases

#### AWS Glue Crawler and Glue Catalog

- crawls already transformed data
- creates catalog to referens data and informs transformation-
- the Catalog can be used by Athena
- can create database schema from CSV data
- can be configured with ETL jobs, what each step should do with the data

#### Amazon Athena

- for protocol data in S3 via SQL
- creates analysis of that datastructure

#### Amazon QuickSight

- visualizes data, from Athena e.g.
- end-user friendly

#### Amazon EMR

- analytics with additional services
- adding 3rd party and machine learning or technologies
- also now serverless

#### Amazon Data Lake

- combine Warehouse, Lakehouse and Data Lake for more different types of data
learn the differences: [warehouse vs lakehouse](https://aws.amazon.com/de/compare/the-difference-between-a-data-warehouse-data-lake-and-data-mart/)

#### Amazon Sage Maker Unified Studio

- AI assisted analytics
- Prepare, integrate, and orchestrate data for analytics and AI at petabyte scale with Amazon EMR, Amazon Athena, and AWS Glue
- Discover, govern, and collaborate on data and AI securely, with a unified catalog, built on Amazon DataZone

## AWS Backup

- plan backup strategie, fitting data and service
- assign resources, instances and storage services to use
- recovery access, plan for RPU and RTO, monitor auto-recovery

#### Recovery Point Objective (RPO) and Recovery Time Objective (RTO)

- how often backups happen, availablity, time lost with recovery
- how long until recovery, downtime limit

#### Pilot light

- resource to jump in, to avoid downtime
- cloned resources, only database replica/snapshots
- does not run most of the time
- get failover data form Aurora for example

#### Warm Standby

- similar replica to pilot light
- but only half is already running, only switch on to scale with production traffic

#### Multi-site

- fully running replica, direct routing switch over
- most expensive
- for most critical applications
- DynamoDB for Global Tables, automatic replication

## AWS AI Services

**Polly** - text to speech
**Transcribe** - speech to text
**Translate** - translation of text
**Amazon Lex** - voice recognition, used for Alexa and chat bots
**Textract** - automatically extracts text and details from documents
**Comprehend** - natural language processiong (NPL), use ML to find text relationships
**Augmented AI** - conduct a human review of ML systems, interface for checking in with AI services, can react to their results
**Kendra** - intelligent file storage crawler, can search in documents
**Personalize** - build and deploy, user segmentation for targeted ads and recommendations
**Fraud Detector** - business metrics, find suspicious usage of application/payment services
**Bedrock** - build reg AI applications
**Q** - reg AI assistant

## Computing for Endusers

- provide streamable environments for your users

#### App Stream 2.0

- turn DaaS into SaaS, no full desktop 
- provides application to stream, encrypted
- can be Always-On, On-Demand or Elastic
- also browser accessible
- BYOL only if vendor allows

#### WorkSpaces

- Personal (persistent) oder Pool (no-persistent)
- full DaaS
- provides a desktop experience as stream
- BYOL eligible and AWS provided

#### WorkSpaces Web

- access to internal and SaaS Websites (like CRM, Salesforce, Jira)
- no app hosting, just your web resources
- in AWS instace, not website needed
- not full capabilities
- not CPU enabled