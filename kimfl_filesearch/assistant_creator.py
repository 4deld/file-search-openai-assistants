from openai import OpenAI
client = OpenAI(api_key="")

file = "file/2023_movie_rank.pdf"

def file_upload(file):
    file = client.files.create(
    file=open(file, "rb"),
    purpose="assistants"
    )
    # print(file)
    return file.id
# file_id = file_upload(file)

def assistant_creator():
    my_assistant = client.beta.assistants.create(
        instructions="당신은 유능한 비서입니다. 제공한 파일에 접근 할 권한이 있으며 대답은 한국어로 사용합니다. 파일에는 2024년 한국에서 개봉한 영화 정보가 1위부터 50위 까지 순서대로 기록되어 있습니다. 각 행은 8칸으로 되어있는데 순위, 영화명, 스크린수, 매출액, 관객수,장르 순서로 되어 있습니다. 예를 들어 순위에 해당하는 칸에 15라고 적혀있으면 그 칸이 포함된 행에 있는 정보가 15위 영화에 대한 정보입니다.",
        name="HR Helper",
        tools=[{"type": "file_search"}],
        model="gpt-4-turbo",
    )

    print(my_assistant)
    return my_assistant

# my_assistant_id=assistant_creator()



empty_thread = client.beta.threads.create()
print(empty_thread)