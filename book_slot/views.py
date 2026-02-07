from django.shortcuts import render
from .models import Doctor, Slot, Patient, Booking
from django.http import JsonResponse
from datetime import datetime
import uuid, json

def form(request):
    doctorlist = ['',]
    doctors = Doctor.objects.all().values()
    for doctor in doctors:
        doctor_name = doctor.get('name')
        doctor_id = doctor.get('id')
        data = {
            'doctor_id': doctor_id,
            'doctor_name': doctor_name
        }
        doctorlist.append(data)
    content = {'data': doctorlist}
    return render(request, 'form.html', content)


def get_details(request):    
    
    # content = {}
    if request.method == 'POST':
        full_name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        disease = request.POST.get('disease')
        number = request.POST.get('number')
        date = request.POST.get('date')
        doctor = request.POST.get('doctor')
        slot = request.POST.get('slot')
        doctor_id = Doctor.objects.get(id= doctor)
        slot_id = Slot.objects.get(id = slot)
        condition = Patient.objects.filter(number= number).exists()
        slot_date = str(slot_id.start_time) + ' - ' + str(slot_id.end_time)
        
        if not  condition:
            patient_id = str(uuid.uuid4())
            new_patient = Patient.objects.create(id = patient_id, name = full_name, dob = dob, age = age, gender = gender, disease = disease, number = number)
            patient_instance_id = Patient.objects.get(id = patient_id)
            new_booking = Booking.objects.create(id = str(uuid.uuid4()), slot_date = date, Is_booked = True, doctor_id = doctor_id, patient_id = patient_instance_id, slod_id = slot_id)
            new_patient.save()
            new_booking.save()
        else:
            patient_instance_id = Patient.objects.get(id = patient_id)
            new_booking = Booking.objects.create(id = str(uuid.uuid4()), slot_date = date, Is_booked = True, doctor_id = doctor_id, patient_id = patient_instance_id, slod_id = slot_id)
            new_booking.save()

        content = {
            'data':{ 
                'full_name': full_name,
                'dob': dob,
                'age': age,
                'gender': gender,
                'disease': disease,
                'number': number,
                'date': date,
                'doctor': doctor_id.name,
                'slot': slot_date
            }
        }
        return render(request, 'confirm.html',content)


def availabe_slots(request):
    slots = Slot.objects.all().values()
    availabe_slot_list=['']
    format_string = "%Y-%m-%d"
    user_data = json.loads(request.body)
    user_date = user_data.get('Date')
    format_user_date = datetime.strptime(user_date, format_string)
    user_doctor_id = user_data.get('Doctor')

    for db_slot in slots:
        slot_id = db_slot.get('id')
        start_time = db_slot.get('start_time')
        end_time = db_slot.get('end_time')
        time = str(start_time) + ' - ' + str(end_time)
        
        condition  = Booking.objects.filter(doctor_id = user_doctor_id, slot_date = format_user_date, slod_id = slot_id).exists()
        if condition :
            data = {
                
                'slot_id' : slot_id,
                'time' : time +' '+'(Booked)',
                'length' : len(time +' '+'(Booked)')                 
            }
            availabe_slot_list.append(data)
        else: 
            data = {
                'slot_id' : slot_id,
                'time' : time,
                'length': len(time)
            }  
            availabe_slot_list.append(data)
        
    content = {'available': availabe_slot_list}
    return JsonResponse(content)
        

    