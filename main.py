from dotenv import load_dotenv
import os
from openai import OpenAI
from typing_extensions import override
from openai import AssistantEventHandler

load_dotenv()
API_KEY = os.environ['OPENAI_API_KEY_DEFAULT_PROJECT']
ASSISTANT_ID = os.environ['ASSISTANT_ID']
THREAD_ID = os.environ['THREAD_ID']

class EventHandler(AssistantEventHandler):    
  @override
  def on_text_created(self, text) -> None:
    print(f"\nassistant > ", end="", flush=True)
      
  @override
  def on_text_delta(self, delta, snapshot):
    print(delta.value, end="", flush=True)
      
  def on_tool_call_created(self, tool_call):
    print(f"\nassistant > {tool_call.type}\n", flush=True)
  
  def on_tool_call_delta(self, delta, snapshot):
    if delta.type == 'code_interpreter':
      if delta.code_interpreter.input:
        print(delta.code_interpreter.input, end="", flush=True)
      if delta.code_interpreter.outputs:
        print(f"\n\noutput >", flush=True)
        for output in delta.code_interpreter.outputs:
          if output.type == "logs":
            print(f"\n{output.logs}", flush=True)

client = OpenAI(api_key=API_KEY)



# Retrieve the message object
message = client.beta.threads.messages.retrieve(
  thread_id=THREAD_ID,
  message_id="msg_NNJJA7i5CeYRToed1zoaJ8Vp"
)
# Extract the message content
message_content = message.content[0].text
print(message_content.value)
