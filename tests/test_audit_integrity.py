import pytest
import os
import tempfile
from src.audit_logger import GxPAuditLogger

def test_audit_trail_logging_and_chaining():
    with tempfile.NamedTemporaryFile(suffix=".jsonl", delete=False) as tf:
        temp_path = tf.name
        
    try:
        logger = GxPAuditLogger(temp_path)
        
        # Log two events
        rec1 = logger.log_event("TEST_EVENT_1", "user_1", "Action 1", "System_A", {"key": "val1"})
        rec2 = logger.log_event("TEST_EVENT_2", "user_2", "Action 2", "System_B", {"key": "val2"})
        
        assert rec1["record_hash"] == rec2["previous_record_hash"]
        assert logger.verify_chain_integrity() is True
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

def test_tamper_detection():
    with tempfile.NamedTemporaryFile(suffix=".jsonl", delete=False) as tf:
        temp_path = tf.name
        
    try:
        logger = GxPAuditLogger(temp_path)
        logger.log_event("TEST_EVENT_1", "user_1", "Action 1", "System_A", {"potency": 100.0})
        logger.log_event("TEST_EVENT_2", "user_2", "Action 2", "System_B", {"potency": 99.5})
        
        # Tamper with file
        with open(temp_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            
        tampered_line = lines[0].replace("100.0", "120.0")
        with open(temp_path, "w", encoding="utf-8") as f:
            f.write(tampered_line + lines[1])
            
        # Verify failure detected
        assert logger.verify_chain_integrity() is False
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)
