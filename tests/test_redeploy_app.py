# tests/test_redeploy_app.py
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from tempfile import TemporaryDirectory
from your_module import redeploy_app, get_app_name_from_args, get_workspace_path_from_args, get_databricks_credentials

def test_get_app_name_from_args():
    """Test get_app_name_from_args function."""
    with patch.object(sys, 'argv', ['test_redeploy_app.py', 'app_name']):
        assert get_app_name_from_args() == 'app_name'

    with patch.object(sys, 'argv', ['test_redeploy_app.py']):
        with pytest.raises(SystemExit):
            get_app_name_from_args()

def test_get_workspace_path_from_args():
    """Test get_workspace_path_from_args function."""
    with patch.object(sys, 'argv', ['test_redeploy_app.py', 'app_name', '/path/to/workspace']):
        assert get_workspace_path_from_args() == '/path/to/workspace'

    with patch.object(sys, 'argv', ['test_redeploy_app.py', 'app_name']):
        assert get_workspace_path_from_args() == f'/Users/<your_user>@databricks.com/app_name'

def test_get_databricks_credentials():
    """Test get_databricks_credentials function."""
    with patch.dict('os.environ', {'DATABRICKS_HOST': 'https://example.com', 'DATABRICKS_TOKEN': 'token'}):
        assert get_databricks_credentials() == {'host': 'https://example.com', 'token': 'token'}

    with patch.dict('os.environ', {'DATABRICKS_HOST': '', 'DATABRICKS_TOKEN': ''}):
        with pytest.raises(SystemExit):
            get_databricks_credentials()

def test_redeploy_app():
    """Test redeploy_app function."""
    with patch.object(requests, 'post') as mock_post:
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {'deployment_id': 'deployment_id'}
        redeploy_app('app_name', '/path/to/workspace', 'https://example.com', 'token')
        mock_post.assert_called_once()

    with patch.object(requests, 'post') as mock_post:
        mock_post.return_value.status_code = 500
        mock_post.return_value.text = 'error'
        with pytest.raises(SystemExit):
            redeploy_app('app_name', '/path/to/workspace', 'https://example.com', 'token')

    with patch.object(requests, 'post') as mock_post:
        mock_post.side_effect = requests.exceptions.RequestException('error')
        with pytest.raises(SystemExit):
            redeploy_app('app_name', '/path/to/workspace', 'https://example.com', 'token')

def test_main():
    """Test main function."""
    with patch.object(sys, 'argv', ['test_redeploy_app.py', 'app_name']):
        with patch.object(redeploy_app, 'redeploy_app') as mock_redeploy_app:
            main()
            mock_redeploy_app.assert_called_once()

    with patch.object(sys, 'argv', ['test_redeploy_app.py']):
        with pytest.raises(SystemExit):
            main()

def test_main_with_workspace_path():
    """Test main function with workspace path."""
    with patch.object(sys, 'argv', ['test_redeploy_app.py', 'app_name', '/path/to/workspace']):
        with patch.object(redeploy_app, 'redeploy_app') as mock_redeploy_app:
            main()
            mock_redeploy_app.assert_called_once()

def test_get_app_name_from_args_empty_argv():
    """Test get_app_name_from_args function with empty argv."""
    with patch.object(sys, 'argv', []):
        with pytest.raises(SystemExit):
            get_app_name_from_args()

def test_get_workspace_path_from_args_empty_argv():
    """Test get_workspace_path_from_args function with empty argv."""
    with patch.object(sys, 'argv', []):
        with pytest.raises(SystemExit):
            get_workspace_path_from_args()

def test_get_databricks_credentials_empty_env():
    """Test get_databricks_credentials function with empty environment."""
    with patch.dict('os.environ', {}):
        with pytest.raises(SystemExit):
            get_databricks_credentials()