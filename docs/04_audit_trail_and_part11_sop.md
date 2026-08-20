# Standard Operating Procedure: Audit Trail Review & Data Integrity Oversight
### *SOP-QA-CSV-042 | Version 3.0*

**Effective Date:** August 20, 2026  
**Applicability:** All GxP Computerized Laboratory, Manufacturing, and Clinical Systems  
**Regulatory References:** FDA 21 CFR Part 11, EU Annex 11, ALCOA+ Data Integrity Principles  

---

## 1. Purpose & Scope
This Standard Operating Procedure (SOP) defines the mandatory requirements for conducting, documenting, and archiving routine and event-triggered audit trail reviews across computerized systems supporting the manufacture, testing, and release of lysergide D-tartrate ODT and pipeline therapeutics.

---

## 2. ALCOA+ Data Integrity Principles

```
┌───────────────┬──────────────────────────────────────────────────────────────────────────────────┐
│ PRINCIPLE     │ OPERATIONAL CONTROLS IN COMPUTERIZED SYSTEMS                                     │
├───────────────┼──────────────────────────────────────────────────────────────────────────────────┤
│ Attributable  │ Unique personal MFA logins; zero generic shared user accounts.                   │
│ Legible       │ Human-readable electronic records and audit trail logs preserved indefinitely.   │
│ Contemporaneous│ Automatic stratum-1 NTP time stamping at moment of event execution.             │
│ Original      │ Raw chromatographic files (.raw/.dat) preserved in write-protected WORM storage. │
│ Accurate      │ Automated calibration lockouts and verified mathematical calculation engines.    │
│ Complete      │ Mandatory capture of all sample runs, including aborted runs and test sequences. │
│ Consistent    │ Chronologically linked audit trails using cryptographic SHA-256 event chaining.  │
│ Enduring      │ Validated electronic archiving with periodic backup and disaster recovery tests. │
│ Available     │ Readily retrievable within 2 hours during FDA / health authority inspections.    │
└───────────────┴──────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Audit Trail Review Cadence & Triggers

### 3.1 Pre-Batch Release Review (Batch-Specific)
Prior to the Quality Assurance release of any commercial or clinical batch of lysergide D-tartrate ODT:
1. The QA CSV Reviewer shall inspect the CDS audit trail for all injections associated with the batch sequence.
2. Verify that no manual baseline integration occurred without documented, pre-approved scientific justification.
3. Confirm that all aborted sequences have a documented deviation ticket.

### 3.2 Routine Periodic Review (System-Level)
* **Monthly:** QA review of system administrative audit trails (user creation, privilege modifications, role changes).
* **Quarterly:** Review of security and failed login exception logs ($\ge 3$ failed attempts).
* **Annual:** Comprehensive steady-state evaluation and user access reconciliation.

---

## 4. Automated Exception Alerting
Computerized systems shall be configured to generate immediate high-priority notifications to the QA Lead upon detection of:
* Attempted deletion of any raw data file or audit trail log.
* Changes to system clock or NTP server configuration.
* Modification of master calculation methods or integration algorithms.
