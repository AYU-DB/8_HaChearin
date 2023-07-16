class Unit: # 부모 클래스
    def __init__(self):
        print("Unit 생성자")

class Flyable: # 부모 클래스
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit): # 자식 클래스
    def __init__(self):
        # super().__init__() // 앞에 있는 매개 변수(현 상태에서는 \\
        # FlyableUnit 의 Flyable)만 실행됨.
        # super()는 자식 클래스에서 부모 클래스를 접근할 수 있게 한다.
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽
dropship = FlyableUnit()