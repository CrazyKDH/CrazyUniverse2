class Student:
    def __init__(self, 국어, 영어, 수학):
        self.국어 = 국어
        self.영어 = 영어
        self.수학 = 수학

    def average(self):
        avg = (self.국어 + self.영어 + self.수학) / 3
        return avg

N = int(input('학생 수 입력(N) :'))

for i in range(N):
    국어 = int(input(f'{i+1}번째 학생의 국어 성적 입력 : '))
    영어 = int(input(f'{i+1}번째 학생의 영어 성적 입력 : '))
    수학 = int(input(f'{i+1}번째 학생의 수학 성적 입력 : '))
    student = Student(국어, 영어, 수학)
    avg = student.average()
    print(f'{i+1}번째 학생의 평균 점수 : {avg}')
    i+=1





