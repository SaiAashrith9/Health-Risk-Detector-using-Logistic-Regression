from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np 
import pandas as pd
#import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def mainfunction():
    data=pd.read_csv('framingham.csv')
    data=data.dropna(axis=0,how='any')
    riskfactors=data.iloc[:,-1]
    datavalues=data.iloc[:,:-1]
    datavalues=datavalues.drop(['education'],axis=1)
    #X_train,X_test,Y_train,Y_test=train_test_split(datavalues,riskfactors,random_state=9)
    #print(X_test[Y_test==1])		
    lr=LogisticRegression()
    #lr.fit(X_train,Y_train)
    lr.fit(datavalues,riskfactors)
    #Test the model if needed
    return lr
    

root=tk.Tk()
header_frame=tk.Frame(root)
header_frame.pack()

header_label=tk.Label(header_frame,text="Please Enter the details of the person",foreground="blue",font=('Arial',18))
header_label.grid(row=0,column=1)

name=StringVar()
gender=IntVar()					#CheckBox Or RadioButtons?
age=IntVar()
#education=IntVar()
currentSmoker=IntVar()
cigsPerDay=IntVar()
BPMeds=IntVar()
prevalentStroke=IntVar()
prevalentHyp=IntVar()
diabetes=IntVar()
totChol=IntVar()
sysBP=IntVar()
diaBP=IntVar()
BMI=IntVar()												#Convert to Floating number
heartRate=IntVar()
glucose=IntVar()

content_frame=tk.Frame(root)
content_frame.pack()

NameLabel=tk.Label(content_frame,text="Name   :")
NameLabel.grid(row=0,column=0)

NameEntryBox=tk.Entry(content_frame,width=9,font=('Arial',9),textvariable=name)
NameEntryBox.grid(row=0,column=3)

GenderLabel=tk.Label(content_frame,text="Gender   :")
GenderLabel.grid(row=1,column=0)

GenderRadioButton1=tk.Radiobutton(content_frame,text="Male",variable=gender,value=1)
GenderRadioButton1.grid(row=1,column=3)

GenderRadioButton2=tk.Radiobutton(content_frame,text="Female",variable=gender,value=0)
GenderRadioButton2.grid(row=2,column=3)

#GenderEntryBox=tk.Entry(content_frame,width=9,font=('Arial',9),textvariable=gender)
#GenderEntryBox.grid(row=1,column=3)

AgeLabel=tk.Label(content_frame,text="Age   :")
AgeLabel.grid(row=3,column=0)

AgeEntryBox=tk.Entry(content_frame,width=9,font=('Arial',9),textvariable=age)
AgeEntryBox.grid(row=3,column=3)

#EducationLabel=tk.Label(content_frame,text="Education   :")
#EducationLabel.grid(row=4,column=0)

#EducationEntryBox=tk.Label(content_frame,width=9,font=('Arial',9),textvariable=education)
#EducationEntryBox.grid(row=4,column=3)

CurrentSmokerLabel=tk.Label(content_frame,text="Does he/she smoke?    ")
CurrentSmokerLabel.grid(row=4,column=0)

CurrentSmokerRadioButton1=tk.Radiobutton(content_frame,text="Yes",variable=currentSmoker,value=1)
CurrentSmokerRadioButton1.grid(row=4,column=3)

CurrentSmokerRadioButton2=tk.Radiobutton(content_frame,text="No",variable=currentSmoker,value=0)
CurrentSmokerRadioButton2.grid(row=5,column=3)

#cigsPerDay=0
#if (currentSmoker==1):
CigsPerDayLabel=tk.Label(content_frame,text="Number of cigarettes per day   :")
CigsPerDayLabel.grid(row=6,column=0)
	
CigsPerDayEntryBox=tk.Entry(content_frame,width=9,font=('Arial',9),textvariable=cigsPerDay)
CigsPerDayEntryBox.grid(row=6,column=3)
			
BPMedsLabel=tk.Label(content_frame,text="Was previously on BP Medications?")
BPMedsLabel.grid(row=7,column=0)

BPMedsRadioButton1=tk.Radiobutton(content_frame,text="Yes",variable=BPMeds,value=1)
BPMedsRadioButton1.grid(row=7,column=3)

BPMedsRadioButton2=tk.Radiobutton(content_frame,text="No",variable=BPMeds,value=0)
BPMedsRadioButton2.grid(row=8,column=3)	

PrevalentStrokeLabel=tk.Label(content_frame,text="Had a Stroke previously?   ")
PrevalentStrokeLabel.grid(row=9,column=0)

PrevalentStrokeRadioButton1=tk.Radiobutton(content_frame,text="Yes",variable=prevalentStroke,value=1)
PrevalentStrokeRadioButton1.grid(row=9,column=3)

PrevalentStrokeRadioButton2=tk.Radiobutton(content_frame,text="No",variable=prevalentStroke,value=0)
PrevalentStrokeRadioButton2.grid(row=10,column=3)

PrevalentHypertensionLabel=tk.Label(content_frame,text="Was hypertensive previously?   ")
PrevalentHypertensionLabel.grid(row=11,column=0)

PrevalentHypertensionRadioButton1=tk.Radiobutton(content_frame,text="Yes",variable=prevalentHyp,value=1)
PrevalentHypertensionRadioButton1.grid(row=11,column=3)

PrevalentHypertensionRadioButton2=tk.Radiobutton(content_frame,text="No",variable=prevalentHyp,value=0)
PrevalentHypertensionRadioButton2.grid(row=12,column=3)

DiabetesLabel=tk.Label(content_frame,text="Had diabetes previously?   ")
DiabetesLabel.grid(row=13,column=0)

DiabetesRadioButton1=tk.Radiobutton(content_frame,text="Yes",variable=diabetes,value=1)
DiabetesRadioButton1.grid(row=13,column=3)

DiabetesRadioButton2=tk.Radiobutton(content_frame,text="No",variable=diabetes,value=0)
DiabetesRadioButton2.grid(row=14,column=3)

TotalCholestrolLabel=tk.Label(content_frame,text="Current Total Cholestrol Level   :")
TotalCholestrolLabel.grid(row=15,column=0)

TotalCholestrolEntryBox=tk.Entry(content_frame,width=9,font=('Arial',9),textvariable=totChol)
TotalCholestrolEntryBox.grid(row=15,column=3)

SystolicBPLabel=tk.Label(content_frame,text="Current Systolic Blood Pressure   :")
SystolicBPLabel.grid(row=16,column=0)

SystolicBPEntryBox=tk.Entry(content_frame,width=9,font=('Arial',9),textvariable=sysBP)
SystolicBPEntryBox.grid(row=16,column=3)

DiastolicBPLabel=tk.Label(content_frame,text="Current Diastolic Blood Pressure   :")
DiastolicBPLabel.grid(row=17,column=0)

DiastolicBPEntryBox=tk.Entry(content_frame,width=9,font=('Arial',9),textvariable=diaBP)
DiastolicBPEntryBox.grid(row=17,column=3)

BMILabel=tk.Label(content_frame,text="BMI   :")
BMILabel.grid(row=18,column=0)

BMIEntryBox=tk.Entry(content_frame,width=9,font=('Arial',9),textvariable=BMI)
BMIEntryBox.grid(row=18,column=3)

HeartRateLabel=tk.Label(content_frame,text="Current HeartRate:   ")
HeartRateLabel.grid(row=19,column=0)

HeartRateEntryBox=tk.Entry(content_frame,width=9,font=('Arial',9),textvariable=heartRate)
HeartRateEntryBox.grid(row=19,column=3)

GlucoseLabel=tk.Label(content_frame,text="Current Glucose Level   :")
GlucoseLabel.grid(row=20,column=0)

GlucoseEntryBox=tk.Entry(content_frame,width=9,font=('Arial',9),textvariable=glucose)
GlucoseEntryBox.grid(row=20,column=3)

def predictrisk(details):
    model=mainfunction()
    return model.predict(details)
	

def submit():
    #bmi=float(str(BMI.get()))
    risk=predictrisk(np.array([gender.get(),age.get(),currentSmoker.get(),cigsPerDay.get(),BPMeds.get(),prevalentStroke.get(),prevalentHyp.get(),diabetes.get(),totChol.get(),sysBP.get(),diaBP.get(),BMI.get(),heartRate.get(),glucose.get()]).reshape(1,-1))
    messagebox.showinfo(title="Details",message=str(risk))
    '''feedback=messagebox.askquestion('Risk Factor','Is the predicted risk factor correct?')
    if ((feedback=='yes') or (feedback=='Yes') or (feedback=='YES')):
         
        messagebox.showinfo(title="Thank You",message="Thanks for the feedback :)")

    elif ((feedback=='no') or (feedback=='No') or (feedback=='NO')):
        NewWindow=TopLevel(root)
        frame=tk.Frame(NewWindow)
	frame.pack()
	hasacurrentcondition=IntVar()
	atriskofgettingaconditioninthefuture=IntVar()
	comments=StringVar()
	CurrentMedicalConditionLabel=tk.Label(frame,text="Does the patient currently have a serious medical condition ?   ")
	CurrentMedicalConditionLabel.grid(row=1,column=0)

	CurrentMedicalConditionRadioButton1=tk.Radiobutton(frame,text="Yes",variable=hasacurrentcondition,value=1)	 	      
        CurrentMedicalConditionRadioButton.grid(row=1,column=3)

        CurrentMedicalConditionRadioButton2=tk.Radiobutton(frame,text="No",variable=atriskofgettingaconditioninthefuture,value=0)
	CurrentMedicalConditionRadioButton2.grid(row=2,column=3)

	AtRiskLabel=tk.Label(frame,text="Does the patient have a risk of facing a serious medical condition in the future ?   ")
	AtRiskLabel.grid(row=3,column=0)

	AtRiskEntryBox=tk.Entry(frame,width=9,font=('Arial',9),variable=atriskofgettingaconditioninthefuture)
	AtRiskEntryBox.grid(row=3,column=3)

	CommentsLabel=tk.Label(frame,text="Comments :   ")
	CommentsLabel.grid(row=4,column=0)

	CommentsEntryBox=tk.Entry(frame,width=9,font=('Arial',9),textvariable=comments)	
    else:
        exit()'''  			 
    print(name.get())
    print(age.get())
    print(currentSmoker.get())

submitbutton=tk.Button(content_frame,text="Submit",command=submit)
submitbutton.grid(row=108,column=1)
tk.mainloop()
