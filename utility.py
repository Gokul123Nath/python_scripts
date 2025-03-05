class abc:
    self_instance = abc()
    def factorial (num):
        if num==1 or num==0:
            return 1 
        else:
            return num*(self_instance.factorial(num-1))