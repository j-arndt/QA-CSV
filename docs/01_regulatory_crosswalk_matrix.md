# Multi-Jurisdictional GxP Regulatory Crosswalk Matrix
### *Computerized Systems Governance for Lysergide D-Tartrate Orally Disintegrating Tablets*

This crosswalk provides the exact legal citation, operational requirement, and computerized system technical control required across all governing bodies for Definium Therapeutics' lead clinical candidate.

---

## 1. United States Food and Drug Administration (FDA)

| Regulatory Citation | Exact Statutory Requirement | Technical & Computerized System Control | Verification Deliverable |
| :--- | :--- | :--- | :--- |
| **21 CFR § 211.68(a)** | Automatic, mechanical, or electronic equipment shall be routinely calibrated, inspected, or checked according to a written program. | Calibration tracking in CMMS/LIMS; automated instrument lockout if past calibration date. | Instrument Installation & Operational Qualification (IQ/OQ). |
| **21 CFR § 211.68(b)** | Appropriate controls shall be exercised over computer or related systems to assure that changes in master production records are instituted only by authorized personnel. | Role-Based Access Control (RBAC), multi-factor authentication, electronic sign-off on batch recipe edits in MES/EBR. | Security & Access Control Test Protocols, User Requirements Specification (URS). |
| **21 CFR § 11.10(a)** | Validation of systems to ensure accuracy, reliability, consistent intended performance, and the ability to discern invalid or altered records. | End-to-end CSV/CSA qualification; positive and negative boundary testing of release calculations. | Validation Master Plan (VMP), Requirements Traceability Matrix (RTM), Validation Summary Report (VSR). |
| **21 CFR § 11.10(b)** | The ability to generate accurate and complete copies of records in both human-readable and electronic form suitable for inspection. | Validated PDF rendering engine with cryptographic hashes; standardized export formats (.pdf, .json, .csv). | Electronic Record Rendition Test Scripts. |
| **21 CFR § 11.10(e)** | Use of secure, computer-generated, time-stamped audit trails to independently record date and time of operator entries and actions. | Contemporaneous, immutable SHA-256 event chaining; stratum-1 NTP synchronization across all instruments. | Audit Trail Review SOP, Tamper-Evident Test Protocol. |
| **21 CFR § 11.50** | Signed electronic records shall contain information associated with the signing that clearly indicates printed name, date/time, and meaning. | Cryptographic digital signature manifesting signer identity, UTC timestamp, and statutory intent (e.g., "Approval", "Review"). | Electronic Signature Verification Test Script. |

---

## 2. United States Drug Enforcement Administration (DEA)

| Regulatory Citation | Exact Statutory Requirement | Technical & Computerized System Control | Verification Deliverable |
| :--- | :--- | :--- | :--- |
| **21 CFR § 1301.71** | Physical security controls for non-practitioners handling Schedule I and II controlled substances. | Automated biometric and RFID badge access to raw API vaults; automated camera trigger on door opening. | Security Access Qualification, Physical/Digital Security Interface Testing. |
| **21 CFR § 1304.22** | Maintenance of continuous records showing receipt, manufacturing, and distribution of controlled substances. | Perpetual electronic mass-balance ledger in ERP; microgram-level reconciliation with automated discrepancy gating. | Perpetual Inventory Ledger Validation Protocol, Mass Balance Stress Test. |
| **21 CFR Part 1311 (CSOS)** | Requirements for electronic orders of Schedule I and II substances (DEA Form 222 electronic equivalent). | Public Key Infrastructure (PKI) digital certificates issued by DEA; digital signature verification on API shipments. | CSOS Interface Qualification, Certificate Revocation List (CRL) Verification. |

---

## 3. European Medicines Agency (EMA) & International Standards

| Regulatory Citation | Exact Statutory Requirement | Technical & Computerized System Control | Verification Deliverable |
| :--- | :--- | :--- | :--- |
| **EudraLex Vol 4 Annex 11 § 4** | Automated validation of data entry and processing; critical data entered manually should undergo an independent second-check. | Enforced dual-operator sign-off in MES/LIMS for raw weight entry of lysergide D-tartrate active substance. | Dual-Check Verification Test Protocol. |
| **EudraLex Vol 4 Annex 11 § 9** | System audit trails must be regularly reviewed based on risk assessment. | Automated monthly exception reports filtering for baseline edits, aborted analytical sequences, and login failures. | Audit Trail Review SOP, Periodic Review Report. |
| **GDPR (Regulation EU 2016/679)** | Lawful, transparent, and secure processing of clinical subject health data (Articles 5, 9, 17, 32). | Cryptographic pseudonymization, salted token hashing, and strict role-based separation of blinding keys in EDC. | Data Protection Impact Assessment (DPIA), GDPR Security Verification Protocol. |
| **ICH Q9 (R1)** | Quality Risk Management principles applied throughout product and system lifecycle. | GAMP 5 FMEA risk scoring matrix linking system failure modes directly to patient safety and product quality. | System Risk Assessment (SRA) Workbook. |
| **ISPE GAMP® AI / ISO 42001** | Assurance and governance of artificial intelligence and machine learning models in healthcare. | Wilson Score confidence interval bounds ($\ge 0.90$), locked benchmark datasets, and Human-in-the-Loop exception queues. | AI Model Validation Plan, Drift Monitoring Protocol. |
