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

