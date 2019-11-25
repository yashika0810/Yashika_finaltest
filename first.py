class test:
    def char(value):
        li = list(value)
        li1 = [str(i) for i in li]
        li1.sort()
        li1 = [int(i) if i.isdigit() else i for i in li1]
        print(li1)
obj=test
obj.char([1,2,3,'yashika',3])

