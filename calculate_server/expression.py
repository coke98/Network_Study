# 수식 클래스
class Expression:
    String = ""
    def __init__(self, str):
        # str이 수식이 아니면 에러
        if not self.is_expression(str):
            raise Exception("Not Expression")
        else:
            self.String = str

    def is_expression(self, str):
        # str이 수식이면 True, 아니면 False
        # 1. str의 길이가 0이면 False
        if len(str) == 0:
            return False
        # 2. str의 첫 글자 혹은 마지막이 연산자이면 False
        if str[0] in ["+", "-", "*", "/"] or str[-1] in ["+", "-", "*", "/"]:
            return False

        return True
    
    def to_string(self):
        return self.String