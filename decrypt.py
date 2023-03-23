#!/usr/bin/env python
# coding: utf-8

# In[8]:





# In[7]:


def decrypt(encrypted_text, key):
    decrypted_text = ""
    i = 0
    while i < len(encrypted_text):
        decrypted_text += encrypted_text[i]
        i += key + 1
    return decrypted_text


# In[8]:


import time

def decrypt_text():
    encrypted_text = input("Enter the encrypted text: ")
    key = int(input("Enter the key: "))
    
    if key not in range(1, 10):
            print("You entered a wrong key")
    
    start_time = time.time()
    decrypted_text = decrypt(encrypted_text, key)
    end_time = time.time()
    
    print("Decrypted text: " + decrypted_text)
    print("Time taken: " + str(end_time - start_time) + " seconds")

def more_input():
    answer = input("Do you want to decrypt another text? (y/n): ")
    if answer == "y":
        decrypt_text()
        more_input()
    else:
        print("Exiting program.")

decrypt_text()
more_input()

