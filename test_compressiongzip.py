# test_compressiongzip.py
"""
Tests for CompressionGzip module.
"""

import unittest
from compressiongzip import CompressionGzip

class TestCompressionGzip(unittest.TestCase):
    """Test cases for CompressionGzip class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CompressionGzip()
        self.assertIsInstance(instance, CompressionGzip)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CompressionGzip()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
