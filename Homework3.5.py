import simple_draw as sd

sd.resolution = (900, 600)

# нарисовать треугольник из точки (300, 300) с длиной стороны 200
#length = 200
#point = sd.get_point(300, 300)

# v1 = sd.get_vector(start_point=point, angle=0, length=200, width=3)
# v1.draw()

#v2 = sd.get_vector(start_point=v1.end_point, angle=120, length=200, width=3)
# v2.draw()

# v3 = sd.get_vector(start_point=v2.end_point, angle=240, length=200, width=3)
# v3.draw()


# определить функцию рисования треугольника из заданной точки с заданным наклоном
#def triangle(point, angle=0):
#    v1 = sd.get_vector(start_point=point, angle=angle, length=200, width=3)
#    v1.draw()

#    v2 = sd.get_vector(start_point=v1.end_point, angle= angle + 120, length=200, width=3)
#    v2.draw()

#    v3 = sd.get_vector(start_point=v2.end_point, angle= angle + 240, length=200, width=3)
#    v3.draw()

#point_0 = sd.get_point(300, 300)

#for angel in range(0, 360, 10):
#    triangle(point=point_0, angle=angel)
# triangle(point=point_0, angle=10)
# triangle(point=point_0, angle=20)
# triangle(point=point_0, angle=30)
# triangle(point=point_0, angle=40)

#sd.pause()

# сделать функцию рисования ветки из заданной точки, заданной длинны,
# с заданным наклоном

point_0 = sd.get_point(300, 5)
#def branch(point, angle, length):
#    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#    v1.draw()
#    return v1.end_point
#angle_0 = 90
#length_0 = 200
#next_point = branch(point=point_0, angle=angle_0, length=length_0)
#next_angle = angle_0 - 30
#next_length = length_0 * .75
#next_point = branch(point=next_point, angle=next_angle, length=next_length)
#next_angle = next_angle - 30
#next_length = next_length * .75
#next_point = branch(point=next_point, angle=next_angle, length=next_length)

# написать цикл рисования ветвей с постоянным уменьшением длины на 25% и отклонением
# на 30 градусов

#angle_0 = 90
#length_0 = 200

#next_angle = angle_0
#next_length = length_0
#next_point = point_0
#while next_length > 10:
#    next_point = branch(point=next_point, angle=next_angle, length=next_length)
#    next_angle = next_angle - 30
#    next_length = next_length * .75


# сделать функцию branch рекрусивной

def branch(point, angle, length, delta):
    if length < 1:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    next_point = v1.end_point
    next_angle = angle - delta
    next_length = length * .75
    branch(point=next_point, angle=next_angle, length=next_length, delta=delta)

for delta in range(0, 51, 10):
    branch(point=point_0, angle=90, length=150, delta=delta)
for delta in range(-50, 1, 10):
    branch(point=point_0, angle=90, length=150, delta=delta)
sd.pause()
