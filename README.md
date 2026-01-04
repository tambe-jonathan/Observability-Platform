# Observability Platform

## Overview

SentinelOps is a production-grade observability and incident response platform deployed on Kubernetes.
It is designed to simulate how large enterprises monitor, alert, and respond to failures in real-world
environments using SRE best practices.

This platform goes beyond tool installation and focuses on:
- Reliability engineering
- Alert discipline
- Incident detection and response
- Continuous validation via stress testing

---

## Objectives

- Detect service degradation before customer impact
- Reduce Mean Time To Detect (MTTD) and Mean Time To Recover (MTTR)
- Enforce SRE Golden Signals and SLO-driven alerting
- Simulate on-call and incident workflows found in large organizations

---

## Architecture Overview

### High-Level Flow

User traffic is served by Kubernetes workloads running in the `applications` namespace.

Metrics, logs, and synthetic probes are collected and processed by a centralized observability stack.

# User Traffic
     ↓
Kubernetes Service
     ↓
Application Pods
     ↓
Metrics (/metrics) ─────┐
Logs (stdout)           │
                         ↓
               ┌────────────────────┐
               │ Prometheus          │
               │ - App Metrics       │
               │ - K8s Metrics       │
               │ - Node Metrics      │
               └────────────────────┘
                         ↓
               ┌────────────────────┐
               │ Alertmanager        │
               │ - Routing           │
               │ - Escalation        │
               └────────────────────┘
                         ↓
         Email / Slack / On-call Simulation

Logs ───────────────▶ Loki ─────────▶ Grafana

Blackbox Exporter ─▶ External Probes

---


---

## Tooling Stack

| Layer | Tool | Purpose |
|------|------|--------|
| Metrics | Prometheus | Metrics collection and alert evaluation |
| Visualization | Grafana | Dashboards for execs, SREs, and app teams |
| Alerting | Alertmanager | Alert routing and escalation |
| Logs | Loki + Promtail | Centralized log aggregation |
| Infra Metrics | node-exporter | Node-level metrics |
| K8s State | kube-state-metrics | Desired vs actual cluster state |
| Synthetic Monitoring | Blackbox Exporter | External availability checks |

---

## Namespace & Ownership Model

Namespaces are strictly separated to reflect enterprise environments:

| Namespace | Ownership |
|---------|-----------|
| monitoring | SRE / Platform Team |
| observability | SRE Team |
| applications | Product Teams |

This separation enables RBAC enforcement and blast-radius control.

---

## Monitoring Philosophy (SRE Model)

### Golden Signals

Each service is monitored using the four Golden Signals:
- Latency (P95 / P99)
- Traffic (requests per second)
- Errors (5xx rate)
- Saturation (CPU / memory)

### Alert Severity Levels

| Severity | Meaning | Action |
|--------|--------|--------|
| Critical | Customer impact | Page on-call |
| Warning | Degradation risk | Slack / email |
| Info | Observation | No action |

Alerts are symptom-based, not noise-based.

---

sentinelops-observability/
├── README.md
├── architecture/
│   ├── diagrams.drawio
│   └── system-overview.md
├── namespaces/
│   └── monitoring.yaml
├── prometheus/
│   ├── prometheus.yaml
│   ├── rules/
│   │   ├── app-alerts.yaml
│   │   ├── infra-alerts.yaml
│   │   └── slo-alerts.yaml
├── alertmanager/
│   ├── alertmanager.yaml
│   └── receivers/
├── grafana/
│   ├── dashboards/
│   │   ├── executive.json
│   │   ├── sre.json
│   │   └── application.json
│   └── datasources.yaml
├── loki/
├── blackbox/
├── apps/
│   └── sample-app/
│       └── metrics-enabled.yaml
└── runbooks/
    ├── api-latency.md
    ├── pod-crashloop.md
    └── node-memory.md


---

## Dashboards

### Executive Dashboard
- Availability (SLO %)
- Error budget remaining
- Active incidents
- High-level service health

### SRE Dashboard
- Latency percentiles
- Pod restarts
- CPU throttling
- Memory pressure
- Node health

### Application Dashboard
- Request rate
- Error rate
- Response times
- Dependency health

Dashboards are separated by audience to avoid information overload.

---

## Alerting & Incident Response

Alertmanager routes alerts based on severity:
- Critical alerts simulate paging the on-call engineer
- Warning alerts notify team channels

Each alert is linked to dashboards and logs to enable rapid diagnosis.

---

## Stress Testing & Validation

This platform is actively tested to validate observability effectiveness.

### Stress Scenarios
- High traffic load
- CPU saturation
- Memory exhaustion
- Pod restarts
- Application error injection

Expected outcomes:
- Metrics reflect system stress
- Alerts fire within defined thresholds
- Dashboards surface root cause signals
- Logs provide actionable context

---

## Incident Simulation

Incidents are documented using real corporate post-incident templates, including:
- Impact analysis
- Root cause
- Timeline
- Corrective actions
- Lessons learned

This validates both tooling and operational readiness.

---

## Repository Structure



---
| Layer         | Tool               | Purpose                               |
| ------------- | ------------------ | ------------------------------------- |
| Metrics       | Prometheus         | Metrics collection & alert evaluation |
| Visualization | Grafana            | Dashboards for execs, SREs, app teams |
| Alerting      | Alertmanager       | Alert routing & escalation            |
| Logs          | Loki + Promtail    | Centralized log aggregation           |
| Infra Metrics | node-exporter      | Node health                           |
| K8s State     | kube-state-metrics | Desired vs actual state               |
| Synthetic     | Blackbox Exporter  | External availability checks          |

---

## Monitoring Philosophy (Corporate SRE Model)
Golden Signals (Tracked Per Service)

- Latency (P95 / P99)
- Traffic (RPS)
- Errors (5xx rate)
- Saturation (CPU / memory)

---
## Alert Severity Model
| Severity | Meaning         | Action             |
| -------- | --------------- | ------------------ |
| Critical | Customer impact | Page on-call       |
| Warning  | Degradation     | Slack notification |
| Info     | Observation     | No action          |

--- 
# Dashboards

| Dashboard Type  | Key Metrics                                                                               |
| --------------- | ----------------------------------------------------------------------------------------- |
| **Executive**   | Availability (SLO %), Error budget remaining, Active incidents, Service health overview   |
| **SRE**         | Latency percentiles (P95/P99), Pod restarts, CPU throttling, Memory pressure, Node health |
| **Application** | Request rate (RPS), Error rate, Response times, Dependency performance                    |

## Security and Access
| Area                | Implementation                                |
| ------------------- | --------------------------------------------- |
| Namespace Isolation | `monitoring`, `observability`, `applications` |
| Access Control      | Kubernetes RBAC                               |
| Secrets Management  | No hardcoded credentials                      |
| Dashboard Access    | Read-only Grafana access for non-SRE users    |

## Validation & Stress Testing

| Scenario           | Purpose                                    |
| ------------------ | ------------------------------------------ |
| High traffic load  | Validate latency and error-rate monitoring |
| CPU saturation     | Test saturation and throttling alerts      |
| Memory exhaustion  | Trigger OOM and restart detection          |
| Pod restarts       | Validate crash and recovery alerts         |
| Application errors | Ensure error-rate alert accuracy           |

## Expected Observability Outcomes

| Outcome   | Description                               |
| --------- | ----------------------------------------- |
| Metrics   | System behavior reflected in Prometheus   |
| Alerts    | Correct alerts fired within thresholds    |
| Logs      | Root-cause context available in Loki      |
| Diagnosis | Rapid issue identification via dashboards |

## 
---

