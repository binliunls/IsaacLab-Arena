# Write a inference code for a model which outputs a list of 16 action points

action_predictions = model.predict(input_data)

for action_point in action_points:
    robot.step(action_point)

observation = robot.get_observation()

action_points = model.predict(observation)