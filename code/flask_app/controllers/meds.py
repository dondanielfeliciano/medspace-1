from ..models.med import Med
from flask_app.models.patient import Patient
from flask_app.models.pharmacy import Pharmacy
from flask_app import app
from flask import redirect, render_template, session, request, flash


@app.route("/patient_profile/<int:patient_id>/<int:pharmacy_id>")
def show_all_meds_one_patient_one_pharmacy(patient_id,pharmacy_id):
    if 'patient_id' in session and session['patient_id'] == patient_id:
        Patient.add_pharmacy({"patient_id":patient_id, "pharmacy_id": pharmacy_id})
        all_meds = Med.get_all_meds_one_patient_one_pharmacy(patient_id, pharmacy_id)
        return render_template("patient_meds.html", all_meds = all_meds, one_pharmacy = Pharmacy.get_one_pharmacy({"id":pharmacy_id}), one_patient = Patient.get_one_patient({"id": patient_id}))
    else:
        flash('Please sign in to access your profile!','patient_login')
        return redirect('/patients')

