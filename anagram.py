def anagram_sol(s1,s2):
    c1=[0]*26
    c2=[0]*26

    for i in range(len(s1)):
        pos=ord(s1[i])-ord('a')#97 is associated with 'a'
        c1[pos]=c1[pos]+1

    for i in range(len(s2)):
        pos=ord(s2[i])-ord('a')# Integer associated with particular value is subtracted
        c2[pos]=c2[pos]+1

    j=0
    still_ok=True

    while j<26 and still_ok:
        if c1[j]==c2[j]:
            j=j+1
        else:
            still_ok=False


    return still_ok


print(anagram_sol('apple','pleap'))
