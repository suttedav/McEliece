print("Start running my test Code :-)")
import numpy as np

#set the three parameters (ev. we should use the Niederreiter crypto system)
n=12
k=4
t=8

m=np.random.randint(2, size=(1,k))
print("Bob's message", m)

#-------------------------------------
# Key generation step (done by Alice)
#-------------------------------------

# Generate a (n,k) Goppa Code
G=[[1,1,1,1,0,1,0,1,0,1,0,0],[0,1,0,0,1,1,1,1,0,0,1,0],[0,0,1,0,1,0,1,1,1,0,0,0],[0,1,0,1,0,0,1,1,0,0,0,1]]

S=np.random.randint(2, size=(k, k))  #generates a random binary (k,k)-matrix

while np.linalg.det(S)==0:
    S = np.random.randint(2, size=(k, k))  # makes sure S is non-singular

tem=np.random.permutation(n)
buf=np.eye(n)
per=buf[tem[0]]
for k in range(1,n):
    per=np.vstack((per, buf[tem[k]]))
P=per  #random (n,n)-permutation matrix

G_hat=np.matmul(S,np.matmul(G,P))

#print("=============================")
#print("Alice's public key is:")
#print("G_hat = ", G_hat)
#print("t = ",t)
#print("=============================")

#print("=============================")
#print("Alice's private key is (don't tell anyone :-)):")
#print("S = ", S)
#print("G = ", G)
#print("P = ", P)
#print("=============================")


#-------------------------------------
# Message encryption step (done by Bob)
#-------------------------------------
c_prime=np.matmul(m,G_hat)

tem=np.random.permutation(n)
z=np.zeros(n)
for k in range(0,t): #generates a random string z of length n with exactly t ones.
    z[tem[k]]=1

c=(c_prime + z)%2  #modulo 2 addtion

print("ciphertext is", c)

#-------------------------------------
# Message decryption step (done by Alice)
#-------------------------------------
c_hat=np.matmul(c, np.linalg.inv(P))
print(c_hat)



print("Test code completed :-)" )
print("test GitHub")






# ========== read in txt file
# some function to transform text stings to binary strings and vice versa
import binascii

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

# read in from a txt file
f = open('test_input.txt','r')
message = f.read()
print(message)
f.close()

# transfer it to binary and back
message_bin=text_to_bits(message)
print(message_bin)
print("length of binary string is", len(message_bin))
message_normal=text_from_bits(message_bin)
print(message_normal)

# write output to another txt file
f = open('test_output.txt','w')
f.write(message_normal)
f.close()