##3-4 guest list
guests = ['marie curie', 'Albert einstein', 'kobe Bryant', 'NINA simone']
print(len(guests))
# message_mc = f"Hello Madam {guests[0].title()}. This message is an invitation for you and a +1 to a dinner party"
# message_ae = f"Hello Mr {guests[-3].title()}. We wan to invite you to a special dinner party."
# message_kb = f"Hello Mr {guests[-2].title()} aka Champion. This is an invitation to dinner"
# message_ns = f"Hello Mrs {guests[3].title()}. We would like you and your art to join us for dinner."
# print(message_ae)
# print(message_kb)
# print(message_mc)
# print(message_ns)

##3-5 Changing guest_list
##changing guests
print(f"{guests[0].title()} will not be able to join us")
guests[0] = 'frida khalo'
# print(guests)
# message_ae = f"Hello Mr {guests[-3].title()}. We wan to invite you to a special dinner party."
# message_kb = f"Hello Mr {guests[-2].title()} aka Champion. This is an invitation to dinner"
# message_ns = f"Hello Mrs {guests[3].title()}. We would like you and your art to join us for dinner."
# message_fk = f"Hola señora {guests[0].title()}. La invitamos a cenar"
# print(message_ae)
# print(message_fk)
# print(message_kb)
# print(message_ns)

##3-6 more guests
guests.insert(0, 'Ayrton senna')

guests.insert(2, 'John eintwistle')

guests.append('Emily dickinson')

###missing: print new messages for each

##3-7 shrinking guests
popped_guest1 = guests.pop(0)
print(f"We are sorry {popped_guest1.title()} but we can't invite you to dinner")
popped_guest2 = guests.pop(2)
print(f"We are sorry {popped_guest2.title()} but we can't invite you to dinner")
popped_guest3 = guests.pop(4)
print(f"We are sorry {popped_guest3.title()} but we can't invite you to dinner")
popped_guest4 = guests.pop(-2)
print(f"We are sorry {popped_guest4.title()} but we can't invite you to dinner")
popped_guest5 = guests.pop(-1)
print(f"We are sorry {popped_guest5.title()} but we can't invite you to dinner")
print(f"Hello {guests[0].title()} and {guests[1].title()}, you are still invited to dinner")
print(guests)
del guests[0]
del guests[-1]





