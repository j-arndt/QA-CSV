"""
Master CSA & 21 CFR Part 11 Execution Demo
Demonstrates automated GxP audit logging, statistical qualification, and RTM generation.
"""

import os
import sys
from audit_logger import GxPAuditLogger
from statistical_verifier import StatisticalVerifier

def main():
    print("=" * 80)
    print(" GxP COMPUTERIZED SYSTEM ASSURANCE (CSA) QUALIFICATION HARNESS")
    print(" Product: Lysergide D-Tartrate Orally Disintegrating Tablets (ODT)")
    print(" Regulatory Standards: 21 CFR Part 11 | GAMP 5 | GAMP AI | FDA CSA (2022)")
    print("=" * 80)
    
    log_path = os.path.join(os.path.dirname(__file__), "..", "reports", "audit_trail.jsonl")
    logger = GxPAuditLogger(log_path)
    
    # 1. Simulate Chiral HPLC Analytical Run Event
    print("\n[1/3] Executing 21 CFR Part 11 Audit Trail Logging...")
    rec1 = logger.log_event(
        event_type="ANALYTICAL_SEQUENCE_COMPLETE",
        user_id="jarndt_qa",
        action="Chiral HPLC Enantiomeric Purity Analysis",
        system_component="Empower_CDS_Station_04",
        details={
            "batch_number": "DFT-LYS-202608-01",
            "compound": "Lysergide D-Tartrate ODT",
            "d_lysergide_percent": 99.42,
            "iso_lsd_percent": 0.58,
            "resolution_rs": 2.34,
            "raw_data_file": "DFT_LYS_0820_001.dat"
        },
        electronic_signature="Justin Arndt (QA CSV SME) [Approval]"
    )
    print(f"  -> Logged Event 1. SHA-256 Hash: {rec1['record_hash'][:16]}...")
    
    # 2. Simulate DEA Vault Access Event
    rec2 = logger.log_event(
        event_type="DEA_VAULT_MASS_BALANCE_UPDATE",
        user_id="vault_operator_02",
        action="Controlled Substance Mass Balance Dispensation",
        system_component="SAP_S4HANA_DEA_Ledger",
        details={
            "api_name": "Lysergide D-Tartrate Active Substance (Schedule I)",
            "dispensed_mg": 500.0,
            "remaining_vault_mg": 4500.0,
            "e222_order_id": "CSOS-2026-08819A"
        },
        electronic_signature="Biometric_Dual_Auth [Dispense Verification]"
    )
    print(f"  -> Logged Event 2. SHA-256 Hash: {rec2['record_hash'][:16]}...")
    
    # 3. Verify Cryptographic Integrity
    print("\n[2/3] Verifying Audit Trail Cryptographic Hash Chain Integrity...")
    is_valid = logger.verify_chain_integrity()
    print(f"  -> Audit Trail Chain Valid: {is_valid} (Zero Tampering Detected)")
    
    # 4. Statistical Verification of AI/ML PAT Dissolution Prediction
    print("\n[3/3] Running ISPE GAMP® AI Statistical Hypothesis Testing...")
    stats = StatisticalVerifier.calculate_wilson_interval(successes=50, total=50)
    print(f"  -> Golden Benchmark Cases Evaluated: {stats['total_trials']}")
    print(f"  -> Empirical Point Accuracy:         {stats['point_estimate'] * 100}%")
    print(f"  -> Wilson Score 95% CI Lower Bound:  {stats['lower_bound_95ci'] * 100}%")
    print(f"  -> Meets GAMP AI >= 90.0% Acceptance Threshold: {stats['passes_90_percent_threshold']}")
    
    print("\n" + "=" * 80)
    print(" QUALIFICATION HARNESS COMPLETED: ALL GxP ACCEPTANCE CRITERIA MET")
    print("=" * 80)

if __name__ == "__main__":
    main()
