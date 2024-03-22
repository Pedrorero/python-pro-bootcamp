# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    if magician == 'alice':
        print(f"{magician.title()}, that was a great trick!")
        print(f"I can't wait to see your next trick, {magician.title()}.\n")
    elif magician == 'david':
        print(f"{magician.title()}, awesome trick dude!")
        print(f"I can't wait to see your next trick, {magician.title()}.\n")
    else: 
        print(f"{magician.title()}, huge trick!")
        print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!\n")
