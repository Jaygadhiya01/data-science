def deco(res):
    def destication(marks):
        for i in marks :
            if i>=80:
                print(i,"dicstion")
        else:
            res(marks)

    return destication

@deco
def result(marks):
    for i in marks:
        if i <=35:
            print("sorry!, you are failed in exam ")
            break
    else:
        print("you pass in exam ")


result([26,78,39,99,70,85])