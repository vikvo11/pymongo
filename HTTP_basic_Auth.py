users = {
    "vorovik": "python123",
    "susan": "bye"
}

def auths(user,password):
    if user in users and password == users[user]:
        return True
    return False


#print (auths('vorovik','python123'))
