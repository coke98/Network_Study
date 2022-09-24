# 수식 클래스
class expression:

    string = ""

    def __init__(self, str):
        # str이 수식이 아니면 에러
        if not self.is_expression(str):
            raise Exception("수식이 아닙니다.")
        else:
            self.string = str

    # 수식 검증 함수
    def is_expression(self, str):
        # str이 수식이면 True, 아니면 False
        # 1. str의 길이가 0이면 False
        if len(str) == 0:
            return False
        # 2. str의 첫 글자 혹은 마지막이 연산자이면 False
        if str[0] in ["+", "-", "*", "/"] or str[-1] in ["+", "-", "*", "/"]:
            return False
        # 3. str에 연산자가 1개가 아니라면 False
        if str.count("+") + str.count("-") + str.count("*") + str.count("/") != 1:
            return False
        # 4. str에 숫자가 없으면 False
        if not any(char.isdigit() for char in str):
            return False

        return True
    
    # 수식을 문자열로 반환
    def to_string(self):
        return self.string