def main():
    message=input("enter a sequence of numbers(space,):")
    answer=""
    for i in message.split():
        num_answer=int(i)
        answer=answer+chr(num_answer)
    print(f"the decoded message is:{answer}")
main()