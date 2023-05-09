import json
import matplotlib.pyplot as plt

def read_json(file_name):
    with open(file_name, 'r') as json_file:
        data = json.load(json_file)
    return data

# Example usage:
file_name = 'data.json'
json_data = read_json(file_name)

iterCount = [i for i in range(100)]

# Intelligence Level 0
intel0_0 = [json_data['intel0_0'][_] for _ in range(100)]
intel0_1 = [json_data['intel0_1'][_] for _ in range(100)]
intel0_2 = [json_data['intel0_2'][_] for _ in range(100)]
intel0_3 = [json_data['intel0_3'][_] for _ in range(100)]
intel0_4 = [json_data['intel0_4'][_] for _ in range(100)]

plt.plot(iterCount, intel0_0, 'r-', label='intelligence 0')
plt.plot(iterCount, intel0_1, 'r-')
plt.plot(iterCount, intel0_2, 'r-')
plt.plot(iterCount, intel0_3, 'r-')
plt.plot(iterCount, intel0_4, 'r-')

# Intelligence Level 1
intel1_0 = [json_data['intel1_0'][_] for _ in range(100)]
intel1_1 = [json_data['intel1_1'][_] for _ in range(100)]
intel1_2 = [json_data['intel1_2'][_] for _ in range(100)]
intel1_3 = [json_data['intel1_3'][_] for _ in range(100)]
intel1_4 = [json_data['intel1_4'][_] for _ in range(100)]

plt.plot(iterCount, intel1_0, 'b-', label='intelligence 1')
plt.plot(iterCount, intel1_1, 'b-')
plt.plot(iterCount, intel1_2, 'b-')
plt.plot(iterCount, intel1_3, 'b-')
plt.plot(iterCount, intel1_4, 'b-')

# Intelligence Level 2
intel2_0 = [json_data['intel2_0'][_] for _ in range(100)]
intel2_1 = [json_data['intel2_1'][_] for _ in range(100)]
intel2_2 = [json_data['intel2_2'][_] for _ in range(100)]
intel2_3 = [json_data['intel2_3'][_] for _ in range(100)]
intel2_4 = [json_data['intel2_4'][_] for _ in range(100)]

plt.plot(iterCount, intel2_0, 'g-', label='intelligence 2')
plt.plot(iterCount, intel2_1, 'g-')
plt.plot(iterCount, intel2_2, 'g-')
plt.plot(iterCount, intel2_3, 'g-')
plt.plot(iterCount, intel2_4, 'g-')

plt.xlabel('Number of food')
plt.ylabel('Time taken in 10ms')
plt.title('Figure 1.1.')
plt.legend()

plt.show()
