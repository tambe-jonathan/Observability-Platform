# 📝 Incident Post-Mortem: [Incident Name]

**Date:** 2026-01-12
**Status:** [Resolved / Mitigated]
**SRE Lead:** @Jonathan

## 📈 Executive Summary
* **Impact:** What was the user experience? (e.g., 5s page loads)
* **Duration:** When did it start? When did it end?

## 🚨 Detection & Response
* **Alert Triggered:** Did `HostHighCpuLoad` fire?
* **MTTD (Mean Time to Detect):** How long before we knew?

## 🧐 Root Cause Analysis (The 5 Whys)
1. Why did the app fail? (Memory leak)
2. Why was there a leak? (Simulation script)
...

## ✅ Action Items
- [ ] Adjust Prometheus alert threshold
- [ ] Add auto-restart policy to Kubernetes
