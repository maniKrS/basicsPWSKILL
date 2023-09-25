def vovel_checker():
    inp = str(input("enter:"))
    vovels = ['a','e','i','o','u']
    for i in vovels:
        if i in inp:
            print(f'{inp} have vovels{list(i)}')
vovel_checker()