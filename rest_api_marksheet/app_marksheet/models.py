from django.db import models

# Create your models here.

class Department(models.Model):
    dept_name = models.CharField(max_length=100)


    def __str__(self):
        return self.dept_name


class StudentId (models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self):
        return self.student_id


class Student (models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    student_id = models.OneToOneField(StudentId, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    

class Subject (models.Model):
    sub_name = models.CharField(max_length=100)

    def __str__(self):
        return self.sub_name


class StudentMark (models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()  


  

    
          
        

            
    