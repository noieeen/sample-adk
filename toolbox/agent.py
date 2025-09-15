import os
from google.adk.agents import Agent, LlmAgent
# from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
# from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
# from mcp import StdioServerParameters
# import datetime
# from zoneinfo import ZoneInfo
from google.adk.models.lite_llm import LiteLlm

from toolbox_core import ToolboxSyncClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()



toolbox = ToolboxSyncClient("http://127.0.0.1:5000")

# Good
tools = toolbox.load_toolset("my-toolset")      # list of tools

# Also good
# tools = [toolbox.load_tool("bcrm-dev")]         # list with one tool

# Not good (what you had)
# tools = (toolbox.load_toolset("my-toolset"),)   # tuple containing a list  ❌


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
