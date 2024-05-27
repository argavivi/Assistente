import json
from difflib import get_close_matches
from icecream import ic
import random

def get_tag(user_input: str) -> int | None:
    knowledge1 = loadknowledge('ai_test_01/chatbot/database.json')
    knowledge = knowledge1['intents']
    for w in range(37):
       
       knowledge_user = knowledge[w]
       for i in knowledge_user['patterns']:
        if str(i).lower() in user_input.lower():
            
            return w
        
    new = knowledge[38]
    new['patterns'].append(user_input)
    saveknowledge('ai_test_01/chatbot/database.json', knowledge1)
    return 38
      

def loadknowledge(file_path : str) -> dict:  
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
        file.close()

    return data

def saveknowledge(file_path : str, data : dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)
        file.close()

def find_best_match(user_question : str, intents : list[str]) -> str | None:
    matches: list = get_close_matches(user_question, intents, n=1, cutoff=0.2)
    return matches

def get_answer(question: str, knowledge_base: dict, tag: int) -> str | None:
        
        question = str(question).replace('[', '')
        question = question.replace(']', '')
        question = question.replace("'", '')
        knowledge_base = knowledge_base['intents']
        knowledge_base = knowledge_base[tag]
        for q in knowledge_base['patterns']:
            
            
            if str(q).lower() in question.lower():
                answer = knowledge_base['responses']
                return answer[random.randrange(0, len(answer))]
        
def chat_bot():
    
    while True:
        knowledge_base: dict = loadknowledge('ai_test_01/chatbot/database.json')
        knowledge = knowledge_base['intents']
        user_input: str = input('you: ')



        if user_input.lower() == 'quit':
            break

        tag = get_tag(user_input)
        #best_match: str | None = find_best_match(user_input.lower, knowledge)
    
        #if best_match:
        knowledge1 = knowledge[tag]
        knowledge_patterns = knowledge1['patterns']
        val = True
        for i in range(len(knowledge_patterns)):

         if str(knowledge_patterns[i]).lower() in user_input.lower():
            answer: str = get_answer(user_input, knowledge_base, tag)
            print(f'chat: {answer}')
            val = False
        if val:
           print('chat: eu não sei a resposta ainda, poderia me ensinar?')
           new_answer: str = input('escreva a resposta ou "skip" para pular: ')

           if new_answer.lower() != 'skip':
                print('chat: obrigado, eu aprendi uma resposta nova!')
           else:
                print('chat: obrigado mesmo assim!')

if __name__ == '__main__':
    chat_bot()