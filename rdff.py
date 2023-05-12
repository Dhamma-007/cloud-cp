import pickle

# Load the PKL file
with open('data/classes.pkl', 'rb') as f:
    data = pickle.load(f)

# Print the loaded data
for i in data:
    print(i)
import h5py

# Open the HDF5 file
# with h5py.File('data/chatbot_model.h5', 'r') as f:
#     # List all the datasets in the file
#     print("Datasets in the file:")
#     for name in f:
#         print(name)
#         print(type(name))

    # Access a specific dataset and read its contents
    # dataset = f['./data/intents.json']
    # data = dataset[()]
    #
    # # Print the loaded data
    # print("Data in the dataset:")
    # print(data)

