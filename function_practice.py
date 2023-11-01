def hello():
    print("hello user")

hello()

def pack(arg1, arg2, arg3):
    lunch = [arg1, arg2, arg3]
    print(lunch)
    return lunch

pack("yes", "no", "maybe")

def eat_lunch(*args):
    if not args:
        print("My lunchbox is empty")
    else:
        for i in range(len(args)):
            if i == 0:
                print("First I eat", args[i])
            else:
                print("Next I eat", args[i])


eat_lunch()
eat_lunch("popcorn", "burger", "pizza")
