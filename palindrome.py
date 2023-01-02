def main():


    def palindrome(n):
        print("Original string : " , n)
        print('Reversed string or Palindrome :' , n[::-1])
        if n == n[::-1]:
            print(n ,'is a palindrome')
        else:
            print(n ,'is not a palindrome')

    c = input('Enter the string :')
    palindrome(c)

    
if __name__ == "__main__":
    main()
