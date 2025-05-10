import os
from dotenv import load_dotenv
import google.generativeai as genai
from typing import Dict, Any, Callable, Optional
import inspect


load_dotenv()
# Creating personlized tool detection and registration system.


class Tool:
    def __init__(self, name: str, description: str, function: Callable):
        self.name = name
        self.description = description
        self.function = function
        self.parameters = self._extract_parameters()

    def _extract_parameters(self) -> Dict[str, Any]:
        """Extracts parameter information from the function signature."""
        sig = inspect.signature(self.function)
        parameters = {}

        for name, param in sig.parameters.items():
            if name == 'self':
                continue
            parameters[name] = {
                'type': param.annotation.__name__ if param.annotation != inspect.Parameter.empty else 'str',
                'required': param.default == inspect.Parameter.empty,
                'description': f"Parameter {name}"
            }

        return parameters

    def execute(self, **kwargs) -> str:
        """Executes the tool with given parameters."""
        return str(self.function(**kwargs))


class ToolManager:
    def __init__(self):
        self.tools: Dict[str, Tool] = {}

    def register_tool(self, tool: Tool):
        """Registers a new tool with the manager."""
        self.tools[tool.name] = tool

    def get_tool(self, name: str) -> Optional[Tool]:
        """Retrieves a tool by name."""
        return self.tools.get(name)

    def list_tools(self) -> Dict[str, str]:
        """Returns a dictionary of tool names and their descriptions."""
        return {name: tool.description for name, tool in self.tools.items()}

# Math Tools


def calculator(a: float, b: float, operation: str = 'add') -> str:
    """Performs basic arithmetic calculations with two numbers.

    Args:
        a: The first number
        b: The second number
        operation: The operation to perform (add, subtract, multiply, divide)
    """
    operations = {
        'add': a + b,
        'subtract': a - b,
        'multiply': a * b,
        'divide': a / b if b != 0 else 'undefined'
    }
    result = operations.get(operation.lower(), 'invalid operation')
    return f"The result of {a} {operation} {b} is {result}"

# Web Tools


def get_weather(city: str, country: str = None) -> str:
    """Gets the current weather for a specified city.

    Args:
        city: The city to check weather for
        country: Optional country name for more specific location
    """
    # In a real implementation, this would call a weather API
    location = f"{city}, {country}" if country else city
    return f"Weather in {location}: Sunny, 25°C (simulated response)"

# File Tools


def read_file(filename: str) -> str:
    """Reads the content of a specified file.

    Args:
        filename: The name of the file to read
    """
    try:
        with open(filename, 'r') as file:
            return file.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"


def initialize_tools() -> ToolManager:
    """Initializes and registers all available tools."""
    manager = ToolManager()

    # Register math tools
    manager.register_tool(Tool(
        name="calculator",
        description="Performs basic arithmetic calculations",
        function=calculator
    ))

    # Register web tools
    manager.register_tool(Tool(
        name="get_weather",
        description="Gets the current weather for a specified location",
        function=get_weather
    ))

    # Register file tools
    manager.register_tool(Tool(
        name="read_file",
        description="Reads the content of a specified file",
        function=read_file
    ))

    return manager


def main():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("GEMINI_API_KEY not found in .env")
        return

    genai.configure(api_key=api_key)

    # This is the correct way — do not prefix with 'models/'
    model = genai.GenerativeModel("gemini-1.5-flash")

    print("Welcome! I'm your AI assistant. Type 'quit' to exit.")
    print("You can ask me to perform calculations or chat with me.")

    tool_manager = initialize_tools()

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == 'quit':
            break

        try:
            # First try to match with tools
            tool_used, tool_response = try_use_tools(user_input, tool_manager)

            if tool_used:
                print("\nAssistant:", tool_response)
            else:
                # If no tool matched, use the model
                response = model.generate_content(user_input)
                print("\nAssistant:", response.text.strip())

        except Exception as e:
            print("\nError:", e)


def try_use_tools(user_input: str, tool_manager: ToolManager) -> tuple[bool, str]:
    """Attempts to use tools based on user input."""
    # Simple keyword matching - in production you'd use more sophisticated NLP
    input_lower = user_input.lower()

    # Check for calculator
    if any(word in input_lower for word in ['calculate', 'add', 'subtract', 'multiply', 'divide', '+', '-', '*', '/']):
        try:
            # Extract numbers - this is simplified
            numbers = [float(n) for n in user_input.split()
                       if n.replace('.', '').isdigit()]
            if len(numbers) >= 2:
                operation = 'add'
                if 'subtract' in input_lower or '-' in input_lower:
                    operation = 'subtract'
                elif 'multiply' in input_lower or '*' in input_lower:
                    operation = 'multiply'
                elif 'divide' in input_lower or '/' in input_lower:
                    operation = 'divide'

                tool = tool_manager.get_tool('calculator')
                result = tool.execute(
                    a=numbers[0], b=numbers[1], operation=operation)
                return True, result
        except:
            pass

    # Check for weather requests
    if 'weather' in input_lower:
        # Simple extraction - in reality you'd use proper NLP
        words = user_input.split()
        city_index = words.index('in') + 1 if 'in' in words else -1
        if city_index != -1 and city_index < len(words):
            city = words[city_index]
            country = words[city_index + 1] if city_index + \
                1 < len(words) else None
            tool = tool_manager.get_tool('get_weather')
            result = tool.execute(city=city, country=country)
            return True, result

    # Check for file operations
    if 'read file' in input_lower or 'open file' in input_lower:
        # Simple filename extraction
        filename = user_input.split('file')[-1].strip().strip('"\'')
        if filename:
            tool = tool_manager.get_tool('read_file')
            result = tool.execute(filename=filename)
            return True, result

    return False, ""

# Future tool Addition Process:

# Create Tool function:

    # def new_tool(param1: type, param2: type) -> str:
    # """Description of what the tool does."""
    # Implementation
    # return "Result"


# Regitster the tool:
    # manager.register_tool(Tool(
    # name="new_tool",
    # description="What this tool does",
    # function=new_tool
    # ))

# Add Detection logic:
    # if 'keyword' in input_lower:
    # Extract parameters
    # tool = tool_manager.get_tool('new_tool')
    # result = tool.execute(param1=value1, param2=value2)
    # return True, result

if __name__ == "__main__":
    main()
