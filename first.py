class test:
    def char(value):
        li = list(value)
        li1 = [str(i) for i in li]
        li1.sort()
        li1 = [int(i) if i.isdigit() else i for i in li1]
        print(li1)
obj=test
obj.char([1,2,3,'yashika',3])


class res:
    def vow(s):
        li= list(s) 
        i= 0 
        le= len(s)-1 
        v=set('aeiouAEIOU')
        while i < le:
            if li[i] in v: 
                li[i]= 'X'
                i=i+1
                continue
            if li[i] not in v: i += 1
        print(''.join(li))
obj=res
obj.vow("Consultadd")

