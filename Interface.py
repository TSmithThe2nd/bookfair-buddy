#Todo import classes
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

import student
import pythonCrudFunctions

#todo set up interface tabs

    #Create student
class CreateStudent(GridLayout):
    def __init__(self, **kwargs):
        super(CreateStudent, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="First Name: "))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Last Name: "))
        self.lastName = TextInput(multiline=False)
        self.inside.add_widget(self.lastName)

        self.inside.add_widget(Label(text="Grade Level: "))
        self.gradeLevel = TextInput(multiline=False)
        self.inside.add_widget(self.gradeLevel)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        name = self.name.text
        last = self.lastName.text
        grade_level = self.gradeLevel.text
        test_student=student.create_student(name, last, grade_level, 2)
        connection = pythonCrudFunctions.create_db_connection()
        pythonCrudFunctions.execute_query(connection,test_student)




class MyApp(App):
    def build(self):
        return CreateStudent()


if __name__ == "__main__":
    MyApp().run()

    #create teacher

    #Add author
     #add book

    #Add book to list
     #teacher
     #student

    #Veiw reports
     #Student books
     #Teacher books
     #Student books By teacher
      #by grade
    #export list

    #admin
    #delete student
    #delete book
    #edit student
    #edit teacher
