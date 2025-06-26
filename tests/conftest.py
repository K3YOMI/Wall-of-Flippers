"""Shared pytest fixtures and configuration for all tests."""

import os
import tempfile
import shutil
from pathlib import Path
from unittest.mock import Mock, MagicMock
import pytest


@pytest.fixture
def temp_dir():
    """Create a temporary directory for test files."""
    temp_path = tempfile.mkdtemp()
    yield Path(temp_path)
    shutil.rmtree(temp_path)


@pytest.fixture
def mock_config():
    """Provide a mock configuration object."""
    config = Mock()
    config.debug = False
    config.verbose = True
    config.timeout = 30
    config.retry_count = 3
    return config


@pytest.fixture
def mock_bluetooth_device():
    """Mock a Bluetooth device object."""
    device = MagicMock()
    device.addr = "00:11:22:33:44:55"
    device.rssi = -65
    device.connectable = True
    device.getValueText = Mock(return_value="Test Device")
    device.getScanData = Mock(return_value=[
        (1, "Flags", "06"),
        (9, "Complete Local Name", "Test Device")
    ])
    return device


@pytest.fixture
def mock_bluetooth_scanner():
    """Mock a Bluetooth scanner object."""
    scanner = MagicMock()
    scanner.scan = Mock(return_value=[])
    scanner.clear = Mock()
    scanner.start = Mock()
    scanner.stop = Mock()
    scanner.process = Mock()
    return scanner


@pytest.fixture
def sample_packet_data():
    """Provide sample Bluetooth packet data for testing."""
    return {
        "address": "AA:BB:CC:DD:EE:FF",
        "rssi": -70,
        "name": "Sample Device",
        "manufacturer_data": bytes.fromhex("4c001005031c276a3d"),
        "service_uuids": ["0000180a-0000-1000-8000-00805f9b34fb"],
        "service_data": {},
        "local_name": "Sample Device",
        "tx_power": 10,
        "connectable": True
    }


@pytest.fixture
def mock_display():
    """Mock display object for testing output."""
    display = MagicMock()
    display.print = Mock()
    display.clear = Mock()
    display.update = Mock()
    display.show_device = Mock()
    display.show_stats = Mock()
    return display


@pytest.fixture
def mock_cache():
    """Mock cache object for testing caching functionality."""
    cache = MagicMock()
    cache.get = Mock(return_value=None)
    cache.set = Mock()
    cache.delete = Mock()
    cache.clear = Mock()
    cache.exists = Mock(return_value=False)
    return cache


@pytest.fixture
def test_data_dir(temp_dir):
    """Create a test data directory with sample files."""
    data_dir = temp_dir / "test_data"
    data_dir.mkdir()
    
    # Create sample test files
    (data_dir / "devices.json").write_text('{"devices": []}')
    (data_dir / "config.json").write_text('{"debug": false}')
    
    return data_dir


@pytest.fixture(autouse=True)
def reset_environment():
    """Reset environment variables before each test."""
    original_env = os.environ.copy()
    yield
    os.environ.clear()
    os.environ.update(original_env)


@pytest.fixture
def mock_async_context():
    """Provide a mock async context for testing async functions."""
    import asyncio
    
    class AsyncContextManager:
        async def __aenter__(self):
            return self
        
        async def __aexit__(self, exc_type, exc_val, exc_tb):
            pass
    
    return AsyncContextManager()


@pytest.fixture
def capture_logs():
    """Capture log messages during tests."""
    import logging
    from io import StringIO
    
    log_capture = StringIO()
    handler = logging.StreamHandler(log_capture)
    handler.setLevel(logging.DEBUG)
    
    # Get root logger
    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    
    yield log_capture
    
    logger.removeHandler(handler)
    log_capture.close()