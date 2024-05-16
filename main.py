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



a='''
최근 당신의 기록을 보면서, 여러 감정의 흐름과 변화를 볼 수 있었습니다. 여기 몇 가지 주요 포인트들이 있습니다:

1. 시험과 학업 스트레스: 일단 많은 내용에서 시험과 학업에 대한 스트레스가 눈에 띄네요. 예를 들어, 중간고사나 기말고사 준비, 과제 등 
으로 인해 심리적인 부담이 커지셨던 것 같습니다【6:11†source】【6:17†source】. 시험 기간의 압박이 상당히 컸고, 그로 인한 불안감과 걱 
정이 많이 나타났습니다【6:1†source】.

2. 성취와 성장: 그럼에도 불구하고 긍정적인 결과도 많았네요. 예를 들어, 예상치 못한 좋은 성적을 받았거나 프로젝트에서 성과를 거두었을
 때 느끼는 기쁨이 기록되어 있습니다【6:4†source】【6:14†source】. 이런 순간들이 당신에게 큰 동기부여가 되었을 것 같아요.

3. 삶의 불확실성과 불안: 또한 삶에 대한 깊은 고민과 불안감도 엿보입니다. 미래에 대한 걱정이나 자신의 선택에 대한 의문 등으로 인해 마
음이 흔들리는 순간들도 많이 느껴졌습니다【6:1†source】【6:10†source】.

4. 사회적 관계와 취미: 사회적 관계와 새로운 취미 활동들이 당신에게 큰 즐거움과 위안이 되었습니다. 예를 들어, 친구들과 함께 보내는 시
간이나 새로운 취미를 시작하면서 느끼는 즐거움이 분명하게 드러나 있습니다【6:8†source】【6:16†source】.

이러한 다양한 감정의 흐름 속에서, 당신이 느끼는 복합적인 감정들이 잘 드러납니다. 이를 바탕으로 좀 더 구체적인 조언이나 질문을 드리자
면:

### 조언:
1. **스트레스 관리**: 학업 스트레스는 누구나 겪는 문제지만, 효율적인 스트레스 관리 방법을 찾아보는 것이 좋을 것 같아요. 예를 들어,  
명상이나 규칙적인 운동이 도움이 될 수 있습니다.
2. **목표 설정**: 구체적이고 달성 가능한 목표를 설정해보세요. 이는 성취감을 제공하고 동기를 부여하는 데 도움이 될 것입니다.
3. **사회적 지원**: 친구나 가족과 더 많은 시간을 보내면서 정서적인 지지를 받아보세요. 이는 당신의 불안을 줄이는 데 크게 도움이 될 수
 있습니다.

### 질문:
1. 최근에 가장 만족스러웠던 순간은 무엇이었나요? 그 순간이 주는 동기를 어떻게 지속할 수 있을까요?
2. 현재 가장 고민이 되는 문제는 무엇인가요? 그 문제를 해결하기 위해 어떤 자원을 활용할 수 있을까요?
3. 학업과 개인 생활의 균형을 맞추기 위해 어떤 노력을 하고 계신가요?

### 템플릿:
각 상황에 따라 사용할 수 있는 템플릿은 다음과 같습니다.

**스트레스가 있을 때:**
- 현재 나를 가장 힘들게 하는 요인은 무엇인가?
- 그 문제를 해결하기 위해 어떤 방법이 있을까?
- 내가 사용할 수 있는 자원은 무엇인가?

**긍정적인 감정을 기록할 때:**
- 최근에 가장 기뻤던 일은 무엇인가?
- 그 일로 인해 내가 얻은 긍정적인 변화는 무엇인가?
- 앞으로 더 많은 이런 긍정적인 순간을 만들기 위해 무엇을 할 수 있을까?

이러한 템플릿들을 사용해서 일기를 작성해보시면 좀 더 체계적으로 감정을 정리할 수 있을 것 같아요. 도움이 필요하시거나 추가로 공유하고 
싶은 내용이 있으면 언제든지 알려주세요!😊
'''
b='''
최근 기록을 바탕으로 보면, 요즘의 기분과 감정은 다음과 같습니다:

1. **스트레스와 피로감**: 중간고사와 기말고사를 준비하면서 공부에 대한 부담과 스트레스가 지속적으로 느껴집니다. 특히, 시험 준비가 어 
렵거나 예상대로 되지 않을 때 피로감이 크게 나타납니다【10:0†source】.

2. **성취와 만족감**: 친구들과 시간을 보내거나 새로운 취미를 시작하면서 느끼는 작은 성취감과 즐거움도 있습니다. 예를 들어, 1월에는 친
구를 만나고 해외여행을 다녀오면서 많은 것을 느끼고 만족감을 기록한 점이 돋보입니다【10:1†source】.

3. **불안과 고민**: 삶에 대한 불확실성과 선택에 대한 고민 역시 자주 나타납니다. 시험 성적, 학업, 미래에 대한 불안이 반복적으로 기록되
고 있습니다【10:8†source】.

전체적으로, 학업과 관련된 스트레스가 크지만, 그 속에서 작은 성취와 즐거움을 찾으며 균형을 맞추고자 노력하는 모습이 보입니다. 좀 더 긍
정적인 감정을 많이 느낄 수 있도록, 스트레스 관리 방법을 찾아보는 것이 도움이 될 것입니다.'''
c='''
최근 기록을 종합해 보았을 때, 요즘 당신의 기분은 다음과 같습니다:

1. **성취감과 기쁨**: 친구들을 만나고 해외여행을 다녀오며 많은 것을 경험했습니다. 특히, 학업에서는 필수 교과목에서의 감면 소식을 들으
면서 상당한 기쁨을 느꼈습니다【14:0†source】.

2. **스트레스와 불안감**: 시험과 학업에 대한 스트레스로 인해 여전히 부담감을 느끼고 있습니다. 예를 들어, 과제와 프로젝트 마감이 다가 
오면서 짐이 무겁게 느껴진다는 기록이 있습니다【14:1†source】.

3. **성장과 기대**: 성장하는 자신을 인식하고 있으며, 다가올 미래에 대한 기대감도 나타납니다. 특히 새해를 맞아 새로운 사람들을 만나고 
긍정적인 변화를 기대하는 모습이 보입니다【14:4†source】.

요약하자면, 최근엔 긍정적인 경험과 성취로 인해 기쁨과 만족을 느끼지만, 여전히 시험과 학업 스트레스로 인한 불안이 공존하는 시기입니다.'''


#localdb=[]
#localdb.append(["0516 bot short","안녕","안녕하세요! 어떻게 지내세요? 요즘 기분이나 생각은 어떠신가요? 공유하고 싶은 이야기가 있으면 언제든 자유롭게 말씀해 주세요. 😊",847])
#localdb.append(["0516 bot short","요즘 나의 기분 어떤지 알려줘",a ,12234])
#localdb.append(["0516 bot short","요즘 나의 기분 알려줘",b ,"?"])
#localdb.append(["0516 bot short","요즘 나의 기분 알려줘",c ,14107])
#localdb.append(["0516 bot","요즘 나의 기분 알려줘",요즘 기분이 전반적으로 즐겁지만 약간의 고민과 스트레스가 섞여 있는 듯해요. 최근 일상과 다양한 활동 속에서 재미를 느끼고 있지만, 동시에 공부나 과제에 대한 부담도 느끼고 있네요[1]``[2]. 어쨌든 새로운 도전들과 활발한 사회활동으로 인해 활기찬 하루하루를 보내고 있는 것 같아요[3]``[4]. ,11717])
#localdb.append(["0516 bot short","최근 기록에 따르면 불안함과 동요가 있는 것 같아요[1]``[2]. 그러나 바쁠 때에는 오히려 집중이 잘 되어 잡생각이 줄어드는 것을 느꼈어요[3]. 전반적으로 인생과 자신의 선택에 대한 많은 고민이 느껴지지만, 성장하고 있는 부분도 인식하고 있어요[4]``[5].. ,11771])
#print(localdb)