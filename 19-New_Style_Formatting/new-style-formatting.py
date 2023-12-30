# New Style Formatting
import re
def solution(s):
    s = re.sub(r"\%{2}", '##', s)
    s = re.sub(r"\%{1}[a-z]{1}", '{}', s)
    return re.sub(r"\#{2}", '%', s)