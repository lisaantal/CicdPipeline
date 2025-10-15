# test_cicdpipeline.py
"""
Tests for CicdPipeline module.
"""

import unittest
from cicdpipeline import CicdPipeline

class TestCicdPipeline(unittest.TestCase):
    """Test cases for CicdPipeline class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CicdPipeline()
        self.assertIsInstance(instance, CicdPipeline)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CicdPipeline()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
