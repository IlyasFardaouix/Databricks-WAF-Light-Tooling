#!/usr/bin/env python3
"""
Redeploy the WAF Databricks App using the same API as install.ipynb.

Usage:
  python redeploy_app.py <app_name> [workspace_path]

  app_name       e.g. wafauto-20260219-2204
  workspace_path e.g. /Users/abhishekpratap.singh@databricks.com/wafauto-20260219-2204
                  (default: /Users/<current_user>/<app_name> if not set)

Requires: DATABRICKS_HOST and DATABRICKS_TOKEN in environment (or ~/.databrickscfg).
"""
import os
import sys
import requests

def get_app_name_from_args() -> str:
    """
    Extract the app name from the first command line argument.

    Args:
        None

    Returns:
        str: The app name extracted from the command line argument.
    """
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    return sys.argv[1].strip()

def get_workspace_path_from_args() -> str:
    """
    Extract the workspace path from the second command line argument.

    Args:
        None

    Returns:
        str: The workspace path extracted from the command line argument, or a default value if not provided.
    """
    workspace_path = (sys.argv[2].strip() if len(sys.argv) > 2 else "").strip()
    if not workspace_path:
        # Default: /Users/<user>/<app_name> — adjust if your workspace path differs
        workspace_path = f"/Users/<your_user>@databricks.com/{get_app_name_from_args()}"
        print(f"Using workspace_path: {workspace_path}")
        print("Pass workspace_path as second argument if different.")
    return workspace_path

def get_databricks_credentials() -> dict:
    """
    Extract Databricks host and token from environment variables.

    Args:
        None

    Returns:
        dict: A dictionary containing the Databricks host and token.
    """
    host = os.environ.get("DATABRICKS_HOST", "").rstrip("/")
    token = os.environ.get("DATABRICKS_TOKEN", "")
    if not host or not token:
        print("Set DATABRICKS_HOST and DATABRICKS_TOKEN (or use ~/.databrickscfg).")
        sys.exit(1)
    return {"host": host, "token": token}

def redeploy_app(app_name: str, workspace_path: str, host: str, token: str) -> None:
    """
    Redeploy the WAF Databricks App using the Databricks API.

    Args:
        app_name (str): The name of the app to redeploy.
        workspace_path (str): The path to the workspace where the app will be redeployed.
        host (str): The Databricks host.
        token (str): The Databricks token.

    Returns:
        None
    """
    api_url = host
    source_code_path = f"/Workspace{workspace_path}"
    try:
        resp = requests.post(
            url=f"{api_url}/api/2.0/apps/{app_name}/deployments",
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
            json={"source_code_path": source_code_path},
            timeout=120,
        )
        if resp.status_code in (200, 201):
            d = resp.json()
            print(f"Redeploy started: deployment_id={d.get('deployment_id')}")
            print(f"Source: {source_code_path}")
        else:
            print(f"Redeploy failed: {resp.status_code} — {resp.text[:400]}")
            sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        sys.exit(1)

def main() -> None:
    """
    The main entry point of the script.

    Args:
        None

    Returns:
        None
    """
    app_name = get_app_name_from_args()
    workspace_path = get_workspace_path_from_args()
    host, token = get_databricks_credentials()
    redeploy_app(app_name, workspace_path, host, token)

if __name__ == "__main__":
    main()