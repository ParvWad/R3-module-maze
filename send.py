from maze  import solution
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "192.168.2.78"
print(ip)
port = 80

adress = (ip,port)
s.connect(adress)
right = "[0][255][255][0]"
left = "[255][0][0][255]"
forward = "[0][255][0][255]"
current = ""
direction = "Down"
for i in range (len(solution)-1 ):
    j = i+1
    if direction == "Down":
        if solution[i][1]<solution[j][1]:
            s.send(forward.encode())
        elif solution[i][0]<solution[j][0]:
            s.send(left.encode())
            direction = "Right"
        elif solution[i][0]>solution[j][0]:
            s.send(right.encode())
            direction= "Left"
    if direction == "Right":
        if solution[i][0]<solution[j][0]:
            s.send(forward.encode())
        elif solution[i][1]<solution[j][1]:
            s.send(left.encode())
            direction= "Up"
        elif solution[i][1]>solution[j][1]:
            s.send(right.encode())
            direction= "Down"
    if direction == "Left":
        if solution[i][0]>solution[j][0]:
            s.send(forward.encode())
        elif solution[i][1]<solution[j][1]:
            s.send(left.encode())
            direction="Down"
        elif solution[i][1]>solution[j][1]:
            s.send(right.encode())
            direction="Right"
    if direction == "Up":
        if solution[i][1]<solution[j][1]:
            s.send(forward.encode())
        elif solution[i][0]>solution[j][1]:
            s.send(left.encode())
            direction="Left"
        elif solution[i][0]<solution[j][0]:
            s.send(right.encode())
            direction="Right"
    time.sleep(1)

s.close()
