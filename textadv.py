user_input = input("Type START to begin your adventure!")
if user_input == "START":
    print("You find a huge field with many strange creatures you have never seen before.")

first_option = input("Do you 'go forward' or 'avoid the field'?")
if first_option == "avoid the field":
    print("You decide to walk around the field instead. There is a dark and scary jungle that looks impossible to navigate. After entering the jungle, you fall into a deep pit and have no chance of escape. You lose.")
    
elif first_option == "go forward":
    print("After walking into the field, you see a threatening monster that towers over you.")
    first_choice = input("Will you 'run' or will you try to 'approach the monster'?")
    if first_choice == "run":
        print("By running forward you startle the monster and it attacks you. You lose.")
    elif first_choice == "approach the monster":
        print("You walk slowly up to the beast. Despite its appearance, it is actually very kind and becomes your friend. You win!")
