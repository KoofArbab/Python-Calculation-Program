import sys ,os
class Calculater :
    """
     print("hello There you are using calculations program version 1.0\nto quit type q")
    """
    on=1
    user_input=''
    def __init__(self):
        system_name= os.uname().sysname
        release_name = os.uname().release
        print("Hello There you are using the lculations program version 1.0\non "+system_name+" "+release_name   +"\ntype q or exit or quit to quit")
        while self.on > 0:
            user_input = input(
                "lets to do some calculations :")
            if user_input in ["q", "exit", "quit"]:
                print("exit")
                self.on = 0
            #checking for the operator
            if "/" in user_input:
                nums=user_input.split("/")
                num1=int(nums[0])
                num2=int(nums[1])
                result =num1/num2
                print(f"the result of diving %s/%d is =%s"%(num1 ,num2 ,result))
            elif  "+" in user_input:
                nums = user_input.split("+")
                num1 = int(nums[0])
                num2 = int(nums[1])
                result =num1+num2
                print(f"the result of adding %s+%d is =%s"%(num1 ,num2 ,result))
            elif  "-" in user_input:
                nums = user_input.split("-")
                num1 = int(nums[0])
                num2 = int(nums[1])
                result =num1-num2
                print(f"the result of subtract %s-%d is =%s"%(num1 ,num2 ,result))
            elif  "*" in user_input:
                nums = user_input.split("*")
                num1 = int(nums[0])
                num2 = int(nums[1])
                result =num1*num2
                print(f"the result of multiply %s*%d is =%s"%(num1 ,num2 ,result))
if __name__=="__main__":
    Calculater()