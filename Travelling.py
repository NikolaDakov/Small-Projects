while True:
    destination = input()
    if destination == "End":
        break
    budget = float(input())
    savings = 0
    while savings < budget:
        savings += float(input())
    print(f"Going to {destination}!")
