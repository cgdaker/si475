import drive, pickle

r = robot()
while True:
    angle = float(input("Angle: "))
    while ( abs(r.getAngle() - angle) > .05 ):
        r.drive(angularSpeed=pid_speed(-.1, 0, 0, angleDiff(r.getAngle()[2], angle)))
    img = r.getImage()
    img.save('image_' + str(angle))
