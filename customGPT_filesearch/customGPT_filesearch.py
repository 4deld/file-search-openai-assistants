# Then, import the necessary modules:
from openai import OpenAI
from dotenv import load_dotenv
import os
from typing_extensions import override
from openai import AssistantEventHandler

OPENAI_API_KEY=os.environ['OPENAI_API_KEY']
client = OpenAI(api_key=OPENAI_API_KEY)

assistant = client.beta.assistants.create(
    name="Real Estate Agent",
    instructions="You are an expert real estate agent. Use your knowledge base to answer questions about provided properties.",
    model="gpt-4-turbo",
    tools=[{"type": "file_search"}],
)

from google.colab import files
import io
import pandas as pd

# Upload the CSV file and read it
uploaded = files.upload()
filename = next(iter(uploaded))  # Get the name of the uploaded file

# Convert the uploaded file content into a stream and set the filename attribute
file_stream = io.BytesIO(uploaded[filename])
file_stream.name = filename  # Ensure the filename (with extension) is retained

# Create a vector store called "Financial Statements"
vector_store = client.beta.vector_stores.create(name="real estate")

# Upload and index the files using the stream with the correct filename
file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
    vector_store_id=vector_store.id, files=[file_stream]
)

# Print the status and file counts to see the result of the operation
print(file_batch.status)
print(file_batch.file_counts)

assistant = client.beta.assistants.update(
    assistant_id=assistant.id,
    tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
)

# Creating a thread and attaching the file
thread = client.beta.threads.create(
    messages=[
        {
            "role": "user",
            "content": "what properties are similar to 130 DARLIN ST"
        }
    ]
)

print(thread.tool_resources.file_search)

# Setting up an event handler to manage responses

class EventHandler(AssistantEventHandler):
    @override
    def on_text_created(self, text) -> None:
        print(f"\nassistant > ", end="", flush=True)

    @override
    def on_tool_call_created(self, tool_call):
        print(f"\nassistant > {tool_call.type}\n", flush=True)

    @override
    def on_message_done(self, message) -> None:
        # Example of how to handle and print file citations
        message_content = message.content[0].text
        # citations = [f"[{i}] {citation.file_citation.filename}" for i, citation in enumerate(message_content.annotations)]
        print(message_content.value)
        # print("\n".join(citations))

# Start the assistant's run
with client.beta.threads.runs.stream(
    thread_id=thread.id,
    assistant_id=assistant.id,
    event_handler=EventHandler(),
) as stream:
    stream.until_done()
