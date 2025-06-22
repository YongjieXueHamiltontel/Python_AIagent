from pydantic_ai.models.gemini import GeminiModel
from pydantic_ai import Agent
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import MCPtools

load_dotenv()
model = GeminiModel("gemini-2.5-flash-preview-04-17")
agent = Agent(model,
              system_prompt="You are an experienced programmer",
              tools=[MCPtools.read_file, MCPtools.list_files, MCPtools.rename_file])


mcp = FastMCP("host info mcp")
mcp.add_tool(MCPtools.get_host_info) # register the tool


def demo_modify_file() -> None:
    """A demo to modify a file in the MCP server.
    """
    history = []
    while True:
        user_input = input("Input: ")
        resp = agent.run_sync(user_input,
                              message_history=history)
        history = list(resp.all_messages())
        print(resp.output)
def demo_get_host_info_in_MCP() -> None:
    mcp.run("stdio")
    """ stdio agent and MCP server should be run in the same process.
        SSE agent and MCP server can be separate, MCP server deployed in clound, but it adds more verfication steps, latency, and complexity.
    """
    # communication protocol


def main():
    demo_modify_file()
    # demo_get_host_info_in_MCP()

    


if __name__ == "__main__":
    main()


