class TestcasesKeyword(object):
    CASE_ID = '0'
    CASE_NAME = '1'
    IS_EXECUTE = '2'
    INTERFACE_URL = '3'
    METHOD = '4'
    HEADER = '5'
    PAYLOAD = '6'
    EXPECTED_RESULT = '7'
    ACTUAL_RESULT = '8'


# 获取自动化用例 ID
def get_case_id():
    return TestcasesKeyword.CASE_ID

def get_case_name():
    return TestcasesKeyword.CASE_NAME

def get_is_execute():
    return TestcasesKeyword.IS_EXECUTE

def get_interface_url():
    return TestcasesKeyword.INTERFACE_URL

def get_method():
    return TestcasesKeyword.METHOD

def get_header():
    return TestcasesKeyword.HEADER

def get_payload():
    return TestcasesKeyword.PAYLOAD

def get_expected_result():
    return TestcasesKeyword.EXPECTED_RESULT

def get_actual_result():
    return TestcasesKeyword.ACTUAL_RESULT


if __name__ == "__main__":
    print(get_case_id())