symptom(fever, flu).
symptom(cough, flu).
symptom(headache, flu).

symptom(fever, malaria).
symptom(chills, malaria).

symptom(sneezing, cold).
symptom(runny_nose, cold).

diagnose(Patient, Disease) :-
    patient_symptom(Patient, Symptom),
    symptom(Symptom, Disease).

patient_symptom(ravi, fever).
patient_symptom(ravi, cough).

patient_symptom(priya, sneezing).
patient_symptom(priya, runny_nose).

patient_symptom(rahul, fever).
patient_symptom(rahul, chills).