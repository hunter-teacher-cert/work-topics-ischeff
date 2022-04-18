#In Class Demo
# Note, as per the HW instructions, this file has been updated
# to complete the encrypt function and to encrypt lower case letters (HW)
# and there has been a decryption function added (HW - mild/bell pepper level)
#encrypt letters such that capital Z shifted 1 is capital A and lowercase z shifted 1 is lowercase a
def encrypt(text,s):
  result = ""
  for i in range(len(text)):
    char = text[i]
  # traverse the plain text
    if(char.isupper()):
    # Encrypt uppercase characters in plain text
    # convert letter into unicode
    # make A unicode 0 by subtracting 65
    # add shift
    # allow wraparound by mod 26
    # make A's unicode 65 again by adding 65
    # convert unicode to letter
      result += chr((ord(char) - 65 + s) % 26 + 65)
    else:
    # Async Work: Encrypt lowercase characters in plain text
    # convert letter into unicode
    # make a unicode 0 by subtracting 97
    # add shift
    # allow wraparound by mod 26
    # move a's unicode 97 again by adding 97
    # convert unicode to letter
      result += chr((ord(char) - 97 + s) % 26 + 97)
  return result

  #enter alphabetic text without spaces and a desired shift
text = "AZaz"
s = 27

print("Plain Text : " + text)
print("Shift pattern : " + str(s))
print("Encrypted Text: " + encrypt(text,s))

#Homework Bell Pepper Version: Write a function that decrypts a symmetric cipher with a given shift
text = "BAba" # made this the same text I just encrypted so it's easy to check if it decrypts correctly
s = 27

def decrypt(text,s):
  result = ""
  for i in range(len(text)):
      char = text[i]
      #traverse the encrypted text
      if(char.isupper()):
          result += ord(char)
      else:
          result+= ord(char)
  return result

print("Encrypted Text : " + text)
print("Shift pattern : " + str(s))
print("Decrypted Text: " + decrypt(text,s))
