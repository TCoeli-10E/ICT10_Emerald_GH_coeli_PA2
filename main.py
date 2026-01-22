from pyscript import display, document

def julias_answer(e):
    document.getElementById("output").innerHTML = ""
    response = document.getElementById("input1").value.lower()

    if response == "yes":
        display(f'kian will be her valentine', target="output")
    elif response == "no":
        display(f'kian will be rejected/heartbroken', target="output")
    elif response == "maybe":
        display(f'dont give up, try again', target="output")
    else:
        display(f'ur an invalid', target="output")

def grade_response(e):
    document.getElementById("output2").innerHTML = ""
    grade = float(document.getElementById("input2").value)

    if 100 == grade >= 95:
        display(f'Bergamo 1', target="output2")
    elif 91 <= grade < 95:
        display(f'Bergamo 2', target="output2")
    elif 86 <= grade <= 90:
        display(f'Bergamo 3', target="output2")
    elif 75 <= grade <= 85:
        display(f'Perugia 1', target="output2")
    elif 65 <= grade <= 75:
        display(f'Perugia 2', target="output2")
    elif grade > 100:
        display(f'no it isnt', target="output2")
    else:

        display(f'failed', target="output2")
