import pickle

with open(r'C:\Users\INDHK6\Desktop\ml-api\model\model1.pickle', mode='rb') as fp:
    model = pickle.load(fp)

def return_pred(inp):
    return model.predict(inp)


if __name__ == '__main__':
    inp = [[1,2,1.1,5]]
    print(return_pred(model, inp))