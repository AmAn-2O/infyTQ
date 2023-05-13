def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    #Write your logic here
    children_cost= 1/3*37550
    total_ticket=37550*no_of_adults+children_cost*no_of_children
    service=total_ticket*0.07
    discount=(total_ticket+service)*0.10
    total_ticket_cost=total_ticket+service-discount
    return total_ticketcost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(5,2)
print("Total Ticket Cost:",total_ticket_cost)

ticket_status="Confirmed"
luggage_weight=32
weight_limit=30  #Weight limit for the airline
extra_luggage_charge=0
if(ticket_status=="Confirmed"):
    if(luggage_weight>0 and luggage_weight<=weight_limit):
        print("Check-in cleared")
    elif(luggage_weight<=(weight_limit+10)):
        extra_luggage_charge=300*(luggage_weight-weight_limit)
    else:
        extra_luggage_charge=500*(luggage_weight-weight_limit)
    if(extra_luggage_charge>0):
        print("Extra luggage charge is Rs.", extra_luggage_charge)
        print("Please make the payment to clear check-in")
else:
    print("Sorry, ticket is not confirmed")

for passenger in "A","A", "FC" "FC", "C", "FA",  "SP", "A", "A":
    if(passenger=="FC" or passenger=="FA"):
        print("No check required")
        continue
    if(passenger=="SP"):
        print("Declare emergency in the airport")
        break
    if(passenger=="A" or passenger=="C"):
        print("Proceed with normal security check")
    print("Check the person")
    print("Check for cabin baggage")

for i in range(1,5,-1):
    print("executed")

def find_product(num1,num2,num3):
    product=0
    for i in range(0,3):
        if(num1==7):
            product=num2*num3
        elif(num2==7):
            product=num3
        elif(num3==7):
            product=-1
        else:
            product=num1*num2*num3
    return product

#Provide different values for num1, num2, num3 and test your program
product=find_product (8,6,2)
print(product)


