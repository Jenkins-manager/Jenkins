"""
    Question analysis class: breaks down user questions and 
    selects appropriate database item
"""
class QuestionAnalysis():

    @staticmethod
    def question_destroy(question):
        q_arr = question.split()
        return list(filter(lambda w : len(w) > 3, q_arr))

    @staticmethod
    def non_keywords_list():
        return ['what', 'where', 'when', 'will', 'does', 'like', 'been', ]

    @staticmethod
    def remove_non_keywords(question):
        return 

    @staticmethod
    def get_question_keywords(question_class):
        return True
    
    @staticmethod
    def process_user_question(question):
        q_arr = QuestionAnalysis.question_destroy(question)