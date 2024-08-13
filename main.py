def main():
    user_input=int(input("enter a number here which double streak you want to see:\n"))
    current_value=user_input
    while current_value<=100:
        double_it=2*current_value
        current_value=double_it
    #the current value is equal to user input ,when it goes through the loop the loop will double it using double_it 
    #its value will be stored as the current value now this current value goes out and repeat the process till condition satisfy

        print(current_value)
if __name__=='__main__':
    main()