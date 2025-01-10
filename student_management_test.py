import unittest 
from student_management import add_student,update_student,delete_student,view_student,load_students_from_file,save_students_to_file # Import your main class
from unittest import mock

class StudentManagementTest(unittest.TestCase):    
   
 @mock.patch('student_management.input', create=True) 
 def test_add_student(self,mocked_input):    
      list_students = [];
      mocked_input.side_effect = [1,'Albert Einstein', 42, 4,"['english','telugu']"]
      add_student(list_students)
      self.assertEqual(1,len(list_students))       

 @mock.patch('student_management.input', create=True)
 def test_update_student_name(self,mocked_input):    
      list_students = [];   
      mocked_input.side_effect = [1,'Albert Einstein', 42, 4,"['english','telugu']",1,1,'ratna']
      add_student(list_students)
      update_student(list_students)
      self.assertEqual(1,len(list_students))   
      self.assertEqual('ratna',list_students[0].name)         

 @mock.patch('student_management.input', create=True)
 def test_update_student_age(self,mocked_input):    
      list_students = [];   
      mocked_input.side_effect = [1,'Albert Einstein', 42, 4,"['english','telugu']",1,2,23]
      add_student(list_students)
      update_student(list_students)
      self.assertEqual(1,len(list_students))   
      self.assertEqual(23,list_students[0].age)     

 @mock.patch('student_management.input', create=True)
 def test_update_student_grade(self,mocked_input):    
      list_students = [];   
      mocked_input.side_effect = [1,'Albert Einstein', 42, 4,"['english','telugu']",1,3,7]
      add_student(list_students)
      self.assertEqual(4,list_students[0].grade)         
      update_student(list_students)
      self.assertEqual(1,len(list_students))   
      self.assertEqual(7,list_students[0].grade)         

 @mock.patch('student_management.input', create=True)
 def test_update_student_subjects(self,mocked_input):    
      list_students = [];   
      mocked_input.side_effect = [1,'Albert Einstein', 42, 4,"['english','maths']",1,4,"['science']"]
      add_student(list_students)
      update_student(list_students)
      self.assertEqual(1,len(list_students))  
      print("****** ",list_students[0].subjects)
      self.assertEqual(["['science']"],list_students[0].subjects)         

 @mock.patch('student_management.input', create=True)
 def test_delete_student(self,mocked_input):    
      list_students = [];   
      mocked_input.side_effect = [1,'Albert Einstein', 42, 4,"['english','maths']",1]
      add_student(list_students)
      self.assertEqual(1,len(list_students))  
      delete_student(list_students)
      self.assertEqual(0,len(list_students))   
      
 @mock.patch('student_management.input', create=True)
 def test_view_student(self,mocked_input):    
      list_students = [];   
      mocked_input.side_effect = [1,'Albert Einstein', 42, 4,"['english','maths']",1]
      add_student(list_students)
      self.assertEqual(1,len(list_students))  
      view_student(list_students)

 @mock.patch('student_management.input', create=True)
 def test_save_student(self,mocked_input):    
      list_students = [];   
      mocked_input.side_effect = [5,'Albert Einstein', 42, 4,"['english','maths']"]
      add_student(list_students)
      self.assertEqual(1,len(list_students))  
      save_students_to_file(list_students,"students_test.json");

 def test_load_student_from_file(self):              
      loaded_students = load_students_from_file("students_test.json")      
      self.assertEqual(4,len(loaded_students))     
      
      
if __name__ == '__main__':
    unittest.main()
                                                                                                  