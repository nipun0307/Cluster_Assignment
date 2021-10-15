from django.db import models
from django.core.validators import MinValueValidator

# Class - 1
class Instructor(models.Model):
    instructor_name = models.CharField(max_length=40)

    def __str__(self):
        return str(self.id)
    

# Class - 2
class Student(models.Model):
    student_roll_num = models.IntegerField(primary_key=True, validators=[MinValueValidator(1)])
    student_name = models.CharField(max_length=40)

    def __str__(self):
        return str(self.student_roll_num)


# Class - 3
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.SlugField(max_length=30, unique=True)
    instructor_id =  models.ForeignKey(Instructor, on_delete=models.CASCADE)
    is_pub = models.BooleanField(default=False)
    is_created  = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        unique_together = ["course_code", "course_name"]


# Class - 4
class Project(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_id_project')
    project_name = models.CharField(max_length=200)
    project_description = models.TextField()
    team_size = models.IntegerField(validators=[MinValueValidator(1)])
    num_teams = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return str(self.id)


# Class - 5
class Peer_edges (models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_id_peer')
    student_roll_num = models.ForeignKey (Student, on_delete=models.CASCADE, related_name='student_id_peer')
    peer_roll_num = models.ForeignKey (Student, on_delete=models.CASCADE, related_name='peer_id_peer')
    status = models.SlugField(max_length=1, default="N")   
    # N - Neutral , F - Friends , E - enemy
    def __str__ (self):
        return str(self.course_id) + "\t:\t(" + str(self.student_roll_num) + " , " + str(self.peer_roll_num) + ")\t:\t" + str(self.status)


# Class - 6
class Projects_pref (models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_id_pref')
    student_roll_num = models.ForeignKey (Student, on_delete=models.CASCADE, related_name='student_id_pref')
    project_id = models.ForeignKey (Project, on_delete=models.CASCADE, related_name= 'project_id_pref')

    def __str__ (self):
        return str(self.course_id) + "\t:\t" + str(self.student_roll_num) + "\t:\t" + str(self.project_id)


# Class - 7
class Student_Enrollment(models.Model):
    student_roll_num = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_roll_enrolled')
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_id_enrolled')

    def __str__(self):
        return str(self.student_roll_num)+ ": " + str(self.course_id)
