def main():
    try:
        a = int(input("Enter your age: "))
        print(a)
        return
        

    except Exception as e:
        print("e")
        print(e)
        return

    finally:
        print("Thank You!")

main()