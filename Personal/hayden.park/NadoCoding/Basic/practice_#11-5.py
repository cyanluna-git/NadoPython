# 패키지, 모듈 위치 확인
from travel import *
trip_to = thailand.ThailandPackage()
trip_to.detail()
import inspect
import random

print(inspect.getfile(random))

print(inspect.getfile(thailand))