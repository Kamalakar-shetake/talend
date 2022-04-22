

def get_input():
    print("Enter number of tuple you want to provide - ")
    all_tuples = []
    try:
        number = eval(input("Enter Number - "))
        for i in range(number):
            name, age, score = input("Enter name,age,score values: ").split()
            temp = tuple([name, age, score])
            all_tuples.append(temp)
        else:
            return all_tuples
    except Exception as e:
        print("Error in input function..{}".format(str(e)))

def get_output(all_tuples):
    print("output is ..")
    try:
        result =  (sorted(all_tuples,key=lambda x:(x[0],x[1],x[2])))
        return result
    except Exception as e:
        print("Error in output function..{}".format(str(e)))

def main():
    all_tuples = get_input()
    print(get_output(all_tuples))

if __name__ == '__main__':
    main()

