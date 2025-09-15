import os
import yaml
from google.adk.agents import Agent, LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters
import datetime
from zoneinfo import ZoneInfo
from google.adk.models.lite_llm import LiteLlm


from toolbox_core import ToolboxSyncClient
import pyodbc


toolbox = ToolboxSyncClient("http://127.0.0.1:5000")

# Load a specific set of tools
tools = (toolbox.load_toolset("my-toolset"),)
# Load single tool
# tools = (toolbox.load_tool("bcrm-dev"),)


# cnxn_str = (
#     "DRIVER={ODBC Driver 18 for SQL Server};"
#     "SERVER=host"
#     "DATABASE=db_name;"
#     "UID=user;"
#     "PWD=password"  # replace with the actual password
# )

# try:
#     conn = pyodbc.connect(cnxn_str)
#     cursor = conn.cursor()
#     cursor.execute("SELECT COUNT(*) AS TotalCustomers FROM CRM_Customer")
#     row = cursor.fetchone()
#     print(f"TotalCustomers: {row.TotalCustomers}")
# except Exception as e:
#     print("Connection failed:", e)
# finally:
#     if conn:
#         conn.close()


# # Load database configuration from tools.yaml
# def load_config():
#     """Load configuration from tools.yaml"""
#     config_path = os.path.join(os.path.dirname(__file__), "tools.yaml")
#     try:
#         with open(config_path, "r") as f:
#             return yaml.safe_load(f)
#     except Exception as e:
#         print(f"Warning: Could not load tools.yaml: {e}")
#         return {}


# config = load_config()


# # Simple database query tool function
# def query_database(query: str) -> dict:
#     """Execute a SQL query against the configured database.

#     Args:
#         query (str): The SQL query to execute.

#     Returns:
#         dict: Result of the query or error message.
#     """
#     # For now, return a placeholder since we don't have the actual database connection
#     # This would need proper SQL Server connection implementation
#     return {
#         "status": "info",
#         "message": f"Database query received: {query}",
#         "note": "Database connection not implemented yet. Configure with proper SQL Server credentials.",
#     }


# def get_database_info() -> dict:
#     """Get information about the configured database.

#     Returns:
#         dict: Database configuration information.
#     """
#     if "sources" in config and "bcrm-dev" in config["sources"]:
#         db_config = config["sources"]["bcrm-dev"]
#         # Don't expose the password in the response
#         safe_config = {k: v for k, v in db_config.items() if k != "password"}
#         safe_config["password"] = "***HIDDEN***"
#         return {"status": "success", "database_config": safe_config}
#     else:
#         return {
#             "status": "error",
#             "message": "No database configuration found in tools.yaml",
#         }


model = os.getenv("OLLAMA_MODEL", "")

root_agent = Agent(
    model=LiteLlm(model=model),
    name="toolbox_agent",
    description="Agent for database operations and toolbox functionality",
    instruction=(
        "You are a helpful agent that can provide information about databases and execute queries. "
        "You have access to database configuration and can help with database-related tasks."
    ),
    tools=tools,
)
