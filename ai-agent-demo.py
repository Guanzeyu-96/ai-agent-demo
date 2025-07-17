from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.deepseek import DeepSeekProvider

from dotenv import load_dotenv
import tools
import os

load_dotenv()
model = OpenAIModel(
    'deepseek-chat',
    provider=DeepSeekProvider(api_key=os.getenv('DEEPSEEK_API_KEY')),
)

agent = Agent(model,
              system_prompt="You are an experienced programmer",
              tools=[tools.read_file, tools.list_files, tools.rename_file])

def main():
    while True:
        user_input = input("Input: ")
        resp = agent.run_sync(user_input)
        print(resp.output)

if __name__ == "__main__":
    main()  
