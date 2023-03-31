from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    major = models.CharField(max_length=20)
    phone_number = models.TextField()

    def __str__(self): # 0309.md의 OOP 참고. 
        return f'({self.pk}) => {self.name}'

if __name__ == '__main__':  # 솔직히 무슨 의민지 모르겠는데, 함수로 작용하려고 쓴게 아니라 메모장으로 생각하라고 하시네. 메모장인가부다ㅋㅋ

    # CRUD operations

    # 생성 Create
    s = Student()
    s.name = 'tlawldud'
    s.age = 24
    s.major = '심리'
    s.phone_number = '01012345678'
    s.save()  # 위에서 models.Model (= ORM)를 상속받았기 때문에 save가 가능함

    s = Student(name='wjsdnjsdn', age=28, major='k-pop', phone_number= '01012345678')
    s.save()

    Student.objects.create(name = 'dlwlgns', age=28, major='k-pop', phone_number ='01012345678')
    

    # 조회 Read/Retrieve
    
    # 레코드 전체조회
    Student.objects.all()

    # 레코드 단일조회
    s1 = Student.objects.get(pk=2) 
    
    # 레코드의 컬럼별 조회
    s1.name
    s1.age
    s1.major

    # 수정 Update -> 모든 레코드의 모든 컬럼 수정가능. id는 수정하면 안 됨.
    s1 = Student.objects.get(pk=1)
    s1.phone_number = '01012345678'
    s1.save()

    # 삭제 Delete
    s3 = Student.objects.get(pk=3)
    s3.delete

class Product(models.Model):
    name = models.CharField(max_length=10)
    price = models.IntegerField()
    year = models.IntegerField()
    quantity = models.IntegerField()



