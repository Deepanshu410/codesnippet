def kbc(Q, A):
    for i in Q:
        print('Your Question is:\n' + i)
        n= []
        a = input('Answer:\n\t')  
        n.extend(a)
    return n
Q = queslist = ['one','two','three']
A = anslist = ['1','2','3']

# a = kbc()
print(kbc(Q,A))
# if kbc(a==A[0]):
#     print("correct answer")
# else:
#     print("Wrong answer")
# if a==A[1]:
#     print("correct answer")
# else:
#     print("Wrong answer")    
# if a==A[2]:
#     print("correct answer")
# else:
#     print("Wrong answer")