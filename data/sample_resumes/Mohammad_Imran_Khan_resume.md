Mohammad Imran Khan
London, UK | +44 7398810660 | imran14989@gmail.com | linkedin.com/in/mohaimran | github.com/mohakhan03uk
AI Tech Lead - Cloud-Native Distributed Systems and Real-Time Telecom Billing Platforms

Professional Summary
AI Tech Lead and distributed systems engineer with 11+ years of experience building mission-critical telecom billing and monetization platforms where latency, uptime, and consistency are product-critical. Strong record across architecture, hands-on C++/Java engineering, AWS migration, Kubernetes platforms, active-active resiliency, and production performance engineering.
Delivered production designs and performance improvements for high-availability distributed systems, including 4-site active-active deployment, 70-80% faster recovery, 60% fewer event conflicts, sub-50ms replica lag, and 30% higher JVM throughput. Owns customer-facing architecture from high-level design and technical reviews through development, testing, rollout, and successful go-live.

Selected Impact
- Led architecture for on-prem to AWS migration of telecom billing workloads, covering EKS, networking, load balancing, resilience, and zero-downtime migration strategy.
- Delivered a 4-site active-active Turbo Charging platform with 2-site failover capability, removing single points of failure and enabling regional failover.
- Reduced recovery time by 70-80% using HBase and Geode snapshot-based restoration.
- Reduced event conflicts by 60% through stickiness, idempotency, and deterministic routing strategies.
- Integrated Azul Zing JVM into IMDG workloads, increasing throughput by 30% and eliminating GC-induced outages.
- Supported large-scale billing platform upgrades for Telkomsel with 165M users, Maxis with 10M users, and Korea Telecom's first 5G-ready Turbo Charging deployment.

Core Technical Skills
- Languages: C, C++, Java, Shell, C#, Assembly
- System Design: Distributed systems, microservices, active-active architecture, domain-driven design, event-driven architecture, low-latency systems
- API and Integration: API design, REST APIs, service contracts, idempotency
- Cloud and Platforms: AWS, EKS, Kubernetes, Docker, Helm, Linux, VMware
- AWS Services: IAM, EC2, S3, VPC, ALB, NLB, CloudWatch, Auto Scaling, MSK
- Data and Messaging: Kafka, Geode/GemFire, HBase, Hive, PostgreSQL, Debezium
- DevOps: Terraform, Jenkins, Ansible, CI/CD automation
- Performance and Observability: perf, gdb, valgrind, JConsole, Dynatrace, sar, netstat
- Frameworks and Tools: Spring Boot, AOP, TDD, TestNG, PlantUML, Cursor

Professional Experience
### Amdocs - London, UK and Pune, India
**Feb 2014 - Present**

Progressed from Software Developer to Software Development Specialist, Software Technical Expert, and AI Tech Lead while working on real-time telecom billing systems, distributed data platforms, cloud migration, Kubernetes adoption, and customer-facing architecture.

#### AI Tech Lead - London, UK
**May 2025 - Present**
- Leading customer architecture discussions for on-prem to AWS migration, including EKS platform design, network topology, traffic routing, and load-balancing strategy.
- Shaping cloud-native deployment patterns for mission-critical billing workloads that require low latency, high availability, and operational resilience.
- Partnering with customer and internal engineering teams to convert migration goals into executable designs, rollout plans, and production readiness decisions.

#### Software Technical Expert - London, UK
**May 2023 - May 2025**
- Designed service APIs and integration contracts between distributed C++ and Java billing/rating components, enabling reliable communication over REST, HTTPS, internal TCP/RMI, and event-driven interfaces.
- Led deployment of a 4-site active-active Turbo Charging system with 2-site failover capability, enabling zero-downtime failover across regions.
- Reduced event conflicts by 60% using stickiness, idempotency, and deterministic request routing.
- Achieved 70-80% faster recovery using HBase and Geode snapshot-based restoration.
- Optimized Geode C++ client thread synchronization, improving stability and reducing timeout rates in production workloads.

#### Software Technical Expert - Pune, India
**July 2022 - May 2023**
- Optimized containerized Turbo Charging workloads for Kubernetes deployments, improving runtime behavior and observability.
- Eliminated CPU throttling for critical containers by redesigning CPU limit strategy while maintaining workload isolation.
- Designed and delivered active-active real-time systems with replica lag consistently below 50ms.
- Built TestNG-based automation to validate event processing across IMDG and HBase layers.

#### Software Development Specialist - Pune, India
**Jan 2020 - July 2022**
- Authored low-level designs for a 10-member team during migration from monolithic architecture to domain-aligned microservices.
- Integrated Azul Zing JVM into IMDG workloads, increasing throughput by 30% and eliminating GC-induced outages.
- Resolved persistent client disconnect loops by tuning Linux TCP parameters, improving reliability of production communication paths.
- Contributed to service decomposition, cache isolation, and performance engineering for scalable billing workloads.

#### Software Developer - Pune, India
**Feb 2014 - Jan 2020**
- Introduced FlatBuffers for efficient serialization, enabling zero-downtime upgrades across distributed billing/rating components.
- Delivered Korea Telecom's first 5G-ready Turbo Charging deployment with zero downtime.
- Supported large-scale upgrades for Telkomsel with 165M users and Maxis with 10M users.
- Identified and resolved long-standing undefined C++ behavior, triggering wider adoption of static analysis practices.
- Developed features for Rating Logic Configurator, a C#/.NET desktop application used to configure telecom charging and rating logic for Online Charging Systems.

Selected Projects
### AWS Cloud Migration
**C++, Java, AWS, EKS, MSK, Geode**
- Designed migration strategy for customer production workloads moving from on-prem infrastructure to AWS with zero downtime.
- Designed secure HTTPS-based API integrations between external 5G network functions and the Online Charging System, enabling reliable real-time charging requests and responses.
- Improved platform resilience for AWS availability-zone failures and infrastructure dependency failures, including NAT Gateway unavailability.
- Authored high-level design documents and led customer architecture reviews covering platform topology, security, traffic flow, and operational readiness.

### Active-Active Billing Platform
**C++, Java, PostgreSQL, Debezium, Geode, Kafka**
- Designed and delivered a 4-site active-active production platform with real-time data synchronization.
- Enabled each site to independently handle production traffic while reducing risk of data inconsistency.
- Designed interactions between distributed C++ and Java services using REST APIs, messaging, and internal RPC mechanisms to support low-latency processing and deterministic request routing.
- Contributed across architecture, development, performance testing, deployment, and migration activities.

### Isolation and Stateless Microservices
**C++, Java, Kubernetes, Kafka, Geode**
- Decomposed monolithic billing/rating components into domain-aligned, stateless microservices with well-defined service APIs.
- Enabled horizontal scaling and independent deployments through idempotent event handling and containerized runtime patterns.
- Diagnosed and resolved performance regressions introduced during cache isolation and service decomposition.

### Write-Behind Persistence Architecture
**HBase, Hive, Java, PostgreSQL**
- Replaced Oracle-backed persistence with HBase-based write-behind architecture to improve scalability and cost efficiency.
- Integrated distributed caching and persistence layers through internal service APIs, enabling resilient asynchronous write-behind processing.
- Enabled analytics, billing, and auditing use cases through Hive queries over big-data storage.

Certification
- Certified Kubernetes Application Developer (CKAD)

Education
- Bachelor of Technology, Information Technology
- 2009 - 2013
