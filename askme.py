from transformers import pipeline

question_answerer = pipeline("question-answering")

#assumes file is of type ".txt". Questions is a list holding the relevant questions to ask.
def asking(questions):
    f=open('file_name.txt', 'r').read()
    for i in questions:
        result = question_answerer(question=i, context=f)
        print(i)
        print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}")
        print('**************')
