# Computer Software Assurance (CSA) Risk Assessment Framework
### *Intended-Use Decision Logic and Automated Testing Allocation*

This document operationalizes the **FDA 2022 Draft Guidance on Computer Software Assurance for Production and Quality System Software** across enterprise GxP platforms.

---

## 1. Risk-Based Decision Algorithm

```
                           [IDENTIFY COMPUTERIZED SYSTEM]
                                         │
                                         ▼
                      [EVALUATE INTENDED USE IN GxP PROCESS]
                                         │
                 ┌───────────────────────┴───────────────────────┐
                 ▼                                               ▼
     [DIRECT PATIENT SAFETY /                        [INDIRECT / QUALITY MANAGEMENT
      PRODUCT QUALITY IMPACT]                         SUPPORT WORKFLOWS]
                 │                                               │
                 ▼                                               ▼
       [ASSESS CUSTOMIZATION]                          [ASSESS VENDOR QUALITY]
      • Cat 3: COTS (Standard)                        • Supplier Audit / SOC 2
      • Cat 4: Configured                             • Pre-release Validation Evidence
      • Cat 5: Custom Scripting                                  │
                 │                                               ▼
                 ▼                                    [UNSCRIPTED ASSURANCE]
      [SCRIPTED RIGOROUS TESTING]                     • Exploratory Testing
      • Functional Positive / Negative                • Process-oriented verification
      • Boundary & Stress Tests                       • High efficiency (60% time saved)
      • Formal 21 CFR Part 11 Audit
```

---

## 2. Enterprise System Risk Classification Matrix

| System Name | Primary GxP Function | GAMP Category | Direct vs. Indirect Impact | Assurance Strategy |
| :--- | :--- | :--- | :--- | :--- |
| **Waters Empower CDS** | Analytical release calculations for lysergide potency and chiral purity | Category 4 (Configured) | **DIRECT IMPACT** | Full Scripted IQ/OQ/PQ + Boundary + Part 11 Audit Verification |
| **SAP S/4HANA ERP (Vault Module)** | DEA Schedule API inventory mass balance and CSOS order reconciliation | Category 4 (Configured) | **DIRECT IMPACT** | Scripted Mass Balance Stress + Biometric Vault Interface Testing |
| **Veeva Vault QMS** | Deviation, CAPA, and Change Control routing and approvals | Category 3 (Configured SaaS) | **INDIRECT IMPACT** | Unscripted Process Verification + Vendor SOC 2 / ISO 27001 Review |
| **Medidata Rave EDC** | Clinical trial electronic case report forms and patient visit data | Category 4 (Configured SaaS) | **DIRECT (Clinical)** | Scripted Blinding Hash Verification + Unscripted User Workflow Test |
| **Mettler Toledo LabX** | Analytical balance data capture and tare weight logging | Category 4 (Configured) | **DIRECT IMPACT** | Scripted Interface & Calibration Lockout Verification |
| **Learning Management (LMS)** | GxP training compliance tracking for manufacturing technicians | Category 3 (COTS SaaS) | **INDIRECT IMPACT** | Unscripted Exploratory Verification + Vendor Attestation Review |

---

## 3. Unscripted vs. Scripted Assurance Protocols

### Scripted Assurance Protocol (High Risk Direct Systems)
* Explicit step-by-step test execution steps with expected results predefined.
* Complete requirement traceability from URS to OQ step.
* Documented pass/fail criteria with mandatory discrepancy logs for any deviation.

### Unscripted Assurance Protocol (Indirect / Low Risk Systems)
* Defined testing objective and intended-use operational scenario.
* Tester explores system boundaries, edge cases, and typical workflows without rigid step-by-step script writing.
* Objective evidence captured via consolidated summary reports and automated system logs rather than manual screenshots of every screen.
