from simulator_x import __version__
from simulator_x.config import settings

def test_package_version_and_local_defaults():
    assert __version__ == "0.2.0"
    assert settings.app_name == "SIMULATOR-X"
    assert settings.host in {"127.0.0.1", "localhost"}
    assert 1 <= settings.port <= 65535
