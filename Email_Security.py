import math
import numpy as np
import random

def adjoint_matrix(matrix):

    try:
        determinant = np.linalg.det(matrix)
        if(determinant!=0):
            cofactor = None
            cofactor = np.linalg.inv(matrix).T * determinant
            # return cofactor matrix of the given matrix
            
            return np.transpose(cofactor)
        else:
            raise Exception("singular matrix")
    except Exception as e:
        print("could not find cofactor matrix due to",e)


def encrypt(x,Key):

    ascii=[]
    messageKey=[]
    # converting message into ascii values
    for character in x:
        ascii.append(ord(character))   


    #finding the length fof the message for matrix generation
    size=math.floor(math.sqrt(len(ascii)))+1


    #Encryption

    # ascii list is multplied with public key value 
    messageKey = [element * Key for element in ascii]

    # converting list to matrix on size n*n
    n, m = size,size

    k = 0
    #here msgMatrix is Message Matrix
    msgMatrix = []

    while n*m != len(ascii):

        # checking if Matrix Possible else append 32 in remaining position
        ascii.append(32)

        # Constructing enciphered Matrix
    for idx in range(0, n):
        sub = []
        for jdx in range(0, m):
            sub.append(ascii[k])
            k += 1
        msgMatrix.append(sub)

    while n*m != len(messageKey):
            # checking if Matrix Possible else append 32 in remaining position
        messageKey.append(32*Key)

    n, m = size,size
    l=0
    #keyMsg is enciphered Matrix
    keyMsg=[]
    for idx1 in range(0, n):
        sub1 = []
        for jdx1 in range(0, m):
            sub1.append(messageKey[l])
            l += 1
        keyMsg.append(sub1)
    return keyMsg


def decrypt(keyMsg,Key):
    final=[]
    # decreption
    # uisng key value construction of a matrix 
    #genrating random matrix according to size of key value
    n=len(keyMsg)
    random_matrix = [[random.random() for e in range(len(keyMsg))] for e in range(len(keyMsg))]



    # converting random matrix into lower triangular matrix 
    for i in range(n):
        for j in range(n):
            if(i<j):
                random_matrix[i][j]=0



    for i in range(n):
        for j in range(n):
            if(i==j):
                random_matrix[i][j]=1
    random_matrix[0][0]=Key


    det = np.linalg.det(random_matrix)
    round(det)


    adj_random=[]
    inverse_random_Matrix=[]
    inverse_adj_random=[]
    adj_random=adjoint_matrix(random_matrix)


    inverse_random_Matrix=np.linalg.inv(random_matrix)

    inverse_adj_random=np.linalg.inv(adj_random)


    Product_rand_adjrand=[]
    Product_rand_adjrand=np.dot(inverse_random_Matrix,inverse_adj_random) 

    decoded_matrix=[]
    decoded_matrix=np.dot(keyMsg,Product_rand_adjrand)


    dec_list=[]
    dec_list=decoded_matrix.flatten()

    dec_list = [int(round(x)) for x in dec_list]
    decrepted_Message = "".join([chr(value) for value in dec_list])


    #printing deciphered Message
    final.append(decrepted_Message)
    return decrepted_Message.strip()

def main():
    decrypt(encrypt("Hello User",123),123)

if __name__=="__main__":
    main()