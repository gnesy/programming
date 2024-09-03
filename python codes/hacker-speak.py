def hacker_speck():
    changes = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 'u': '5'}
    messenge = input()
    list_messege = list(messenge) 

    for i in list_messege:
        for k, v  in changes.items():
            if i == k:
                break
        if i == k:
            break
    
    for i in list_messege:
        if list_messege[i] == i:
            list_messege[i] == v
            break
        
    new_messege = ''.join(list_messege)
    print(new_messege)


hacker_speck()