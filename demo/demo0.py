def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = first+' '+last
    return full_name.title()
#
# # from name_function import get_formatted_name
# print("Enter 'q' at any time to quit.")
# while True:
#     first = input("\nPlease give me a first name: ")
#     if first == 'q':
#         break
#     last = input("Please give me a last name: ")
#     if last == 'q':
#         break
#     formatted_name = get_formatted_name(first, last)
#     print("\tNeatly formatted name: "+formatted_name+'.')

# import unittest
#
# class NamesTestCase(unittest.TestCase):
#     """测试name_function.py"""
#     def test_first_last_name(self):
#         """能够正确地处理像Janis Joplin这样的姓名吗？"""
#         formatted_name = get_formatted_name('janis', 'joplin')
#         self.assertEqual(formatted_name, 'Janis Joplin')
# unittest.main()


class AnonymousSurvey():
    """收集匿名调查问卷的答案"""
    def __init__(self, question):
        """存储一个问题，并为存储答案做准备"""
        self.question = question
        self.responses = []
    def show_question(self):
        """显示调查问卷"""
        print(self.question)
    def store_response(self, new_response):
        """存储单份调查答卷"""
        self.responses.append(new_response)
    def show_results(self):
        """显示收集到的所有答卷"""
        print("Survey results:")
        for response in self.responses:
            print('- '+response)
# from survey import AnonymousSurvey
#定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)
#显示问题并存储答案
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)
# 显示调查结果
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()