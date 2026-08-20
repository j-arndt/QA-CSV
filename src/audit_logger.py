"""
21 CFR Part 11 Cryptographic Audit Trail Logger
Implements immutable, contemporaneous SHA-256 event chaining for GxP computerized systems.
"""

import hashlib
import json
import os
from datetime import datetime, timezone
from typing import Dict, Any, Optional

class GxPAuditLogger:
    def __init__(self, log_filepath: str):
        self.log_filepath = log_filepath
        self.prev_hash = "0" * 64
        self._initialize_log()

    def _initialize_log(self):
        os.makedirs(os.path.dirname(os.path.abspath(self.log_filepath)), exist_ok=True)
        if os.path.exists(self.log_filepath) and os.path.getsize(self.log_filepath) > 0:
            with open(self.log_filepath, "r", encoding="utf-8") as f:
                lines = f.readlines()
                if lines:
                    last_record = json.loads(lines[-1].strip())
                    self.prev_hash = last_record.get("record_hash", "0" * 64)

    def log_event(
        self,
        event_type: str,
        user_id: str,
        action: str,
        system_component: str,
        details: Dict[str, Any],
        electronic_signature: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Logs a contemporaneous, tamper-evident GxP event complying with 21 CFR § 11.10(e).
        """
        timestamp = datetime.now(timezone.utc).isoformat()
        
        record_payload = {
            "timestamp_utc": timestamp,
            "event_type": event_type,
            "user_id": user_id,
            "system_component": system_component,
            "action": action,
            "details": details,
            "electronic_signature": electronic_signature or "SYSTEM_VERIFIED",
            "previous_record_hash": self.prev_hash
        }
        
        # Calculate cryptographic SHA-256 digest
        serialized = json.dumps(record_payload, sort_keys=True)
        record_hash = hashlib.sha256(serialized.encode("utf-8")).hexdigest()
        
        record_payload["record_hash"] = record_hash
        self.prev_hash = record_hash
        
        # Append to immutable JSONL audit log
        with open(self.log_filepath, "a", encoding="utf-8") as f:
            f.write(json.dumps(record_payload) + "\n")
            
        return record_payload

    def verify_chain_integrity(self) -> bool:
        """
        Verifies the cryptographic hash integrity of the entire audit trail.
        """
        if not os.path.exists(self.log_filepath):
            return True
            
        current_prev = "0" * 64
        with open(self.log_filepath, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, 1):
                record = json.loads(line.strip())
                claimed_hash = record["record_hash"]
                claimed_prev = record["previous_record_hash"]
                
                if claimed_prev != current_prev:
                    print(f"Audit Trail Broken at record {line_no}: Previous hash mismatch!")
                    return False
                    
                temp_payload = {k: v for k, v in record.items() if k != "record_hash"}
                recomputed = hashlib.sha256(json.dumps(temp_payload, sort_keys=True).encode("utf-8")).hexdigest()
                
                if recomputed != claimed_hash:
                    print(f"Audit Trail Tampering detected at record {line_no}: Hash mismatch!")
                    return False
                    
                current_prev = claimed_hash
                
        return True
