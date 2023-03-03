"""
__init__.py 파일은 해당 디렉터리가 패키지의 일부임을 알려주는 역할을 한다. 
만약 game, sound, graphic 등 패키지에 포함된 디렉터리에 
__init__.py 파일이 없다면 패키지로 인식되지 않는다.

https://cuorej.tistory.com/entry/PYTHON-%EC%97%AC%EB%9F%AC-%EA%B2%BD%EB%A1%9C%EC%9D%98-%EB%AA%A8%EB%93%88-import-%ED%95%98%EA%B8%B0-1

"""
from . import amount_discount_policy_
from . import percent_discount_policy_
from . import non_discount_policy_
from . import sequence_condition_
from . import period_condition_
