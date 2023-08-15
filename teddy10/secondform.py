# import openpyxl and tkinter modules
from openpyxl import *
from tkinter import *
 
# globally declare wb and sheet variable
 
# opening the existing excel file
wb = load_workbook('C:\\xampp\\htdocs\\teddyhub\\teddy10\\excel.xlsx')
 
# create the sheet object
sheet = wb.active

def excel():
     
    # resize the width of columns in
    # excel spreadsheet
    sheet.column_dimensions['A'].width = 30
    sheet.column_dimensions['B'].width = 10
    sheet.column_dimensions['C'].width = 10
    sheet.column_dimensions['D'].width = 20
    sheet.column_dimensions['E'].width = 20
    sheet.column_dimensions['F'].width = 40
    sheet.column_dimensions['G'].width = 50
 
    # write given data to an excel spreadsheet
    # at particular location
    sheet.cell(row=1, column=1).value = "Name"
    sheet.cell(row=1, column=2).value = "Course"
    sheet.cell(row=1, column=3).value = "Semester"
    sheet.cell(row=1, column=4).value = "Form Number"
    sheet.cell(row=1, column=5).value = "Contact Number"
    sheet.cell(row=1, column=6).value = "Email id"
    sheet.cell(row=1, column=7).value = "Address"
    
# Function to set focus (cursor)
def focus1(event):
    # set focus on the course_field box
    course_field.focus_set()
 
 
# Function to set focus
def focus2(event):
    # set focus on the sem_field box
    sem_field.focus_set()
 
 
# Function to set focus
def focus3(event):
    # set focus on the form_no_field box
    form_no_field.focus_set()
 
 
# Function to set focus
def focus4(event):
    # set focus on the contact_no_field box
    contact_no_field.focus_set()
 
 
# Function to set focus
def focus5(event):
    # set focus on the email_id_field box
    email_id_field.focus_set()

# Function to set focus
def focus6(event):
    # set focus on the address_field box
    address_field.focus_set()
     