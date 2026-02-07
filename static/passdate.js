
let date;
let doctor;
const selectElement = document.getElementById('slot');

function pass_date()
{
    date = document.getElementById('date').value
    doctor = document.getElementById('doctor').value
    
    const content = {
        Date: date,
        Doctor: doctor
    }
    const csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;

    fetch('/hospital/slot/',{
            method: 'POST',
            headers: {
                'content-Type': 'application/json',
                'X-CSRFToken':csrfToken,
                'X-Requested-With' : 'XMLHttpRequest'
            },
        body: JSON.stringify(content)
    })
    .then(response => response.json())
    .then(data =>{
        console.log('success', data)
        selectElement.innerHTML = ''
        for(let i in data.available)
        {
            if(data.available[i].length <= 19)
            {
                const option = document.createElement('option');
                option.value = data.available[i].slot_id;
                option.textContent = data.available[i].time;
                selectElement.appendChild(option);
                let time = data.available[i].time
            }
            else
            {
                const option = document.createElement('option');
                option.value = data.available[i].slot_id;
                option.textContent = data.available[i].time;
                option.disabled = true;
                selectElement.appendChild(option);
            }
        }
        let options = selectElement.getElementsByTagName('option')
    })
    .catch((error)=>{
        console.log('error', error)
    });
}




