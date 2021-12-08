# def move_right():
#     if at_goal() is True:
#         done()
#     else:
#         turn_right()
#         move()
#         if wall_on_right() != False:
#             if wall_in_front() is True:
#                 turn_left()
#             else:
#                 move()
#         else:
#             turn_right()
#
#
# while at_goal() != True:
#     if front_is_clear() != True:
#         turn_left()
#     else:
#         move()
#         if wall_on_right() != True:
#             move_right()