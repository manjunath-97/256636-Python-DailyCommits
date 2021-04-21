def devision(devidend,devisor):
    assert devisor != 0 , "Devisor cant be zero"
    return devidend/devisor

a = int(input("Enter Devidend: "))
b = int(input("Enter Devisor:" ))

print(a,"/",b,"=",devision(a,b))