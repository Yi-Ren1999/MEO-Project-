import numpy as np
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier,DecisionTreeRegressor, plot_tree
from sklearn import preprocessing

DATABASE_PATH='test_dataset.npz'
NUMBER_OF_TRIES=5
CHOICING_THRESHOLD=0.8

class Decision_Tree_Agent():
    def __init__(self):
        self.ending=False
        self.descriptions=[]
        self.label=None
        self.dt=DecisionTreeClassifier()
        self.le_X=preprocessing.LabelEncoder()
        self.le_y=preprocessing.LabelEncoder()
    
    def load_database(self,filename):
        data=np.load(DATABASE_PATH)
        self.X=data['description']
        self.y=data['label']
        self.X_le=self.le_X.fit_transform(self.X)
        self.y_le=self.le_y.fit_transform(self.y)


    
    def fit_model(self):
        self.dt.fit(self.X_le.reshape(-1,1),self.y_le)
    
    def plot_model(self):
        plot_tree(self.dt,filled=True)
        plt.show()
        

    def save_database(self,filename):
        return 

    
    def run(self):
        self.__init__()
        self.starting()
        self.load_database(DATABASE_PATH)
        self.fit_model()
        self.predicting()
        self.ending=self.recording()

    def predicting(self):
        print('I am happy  that you have made your choice and let us start the game!')
        get_the_answer=False
        for _ in range(NUMBER_OF_TRIES):
            print('please give me some information for guessing')
            description=str(input())
            self.descriptions.append(description)
            get_the_answer,answer=self.guessing(self.descriptions)
            if get_the_answer:
                answer=self.le_y.inverse_transform([answer])
                print('Ah! I get the answer!')
                print('It is '+str(answer[0])+'!')
                print('Am I right? (y/n)')
                reply=input()
                if reply=='y':
                    self.label=answer[0]
                    break
                else:
                    print('please give the right answer.')
                    answer=input() 
                    if answer in self.y:
                        self.label=str(answer)
                break
            else:
                print('I need more information!')
        if not get_the_answer:
            print('I can get the answer')
            print('please tell me the correct answer')
            answer=input()
            self.label=str(answer)
    

    def guessing(self,description):
        description=self.my_concating(description)
        print(description)
        answer=-1
        get_answer=False
        des=0
        if description in self.X:
            des=self.le_X.transform(description)
        else:
            get_answer=False
            return get_answer,answer
        prob=self.dt.predict_proba(des.reshape(1,-1))
        if np.max(prob)>CHOICING_THRESHOLD:
            answer=np.argmax(prob)
            get_answer=True
        return get_answer,answer
        

    def my_concating(self,description):
        output=str()
        for des in description:
            output+=str(des)
        return [output]

    def recording(self):
        print('start recording the data')
        description=np.concatenate([self.X,[self.my_concating(self.descriptions)]],axis=0)
        label=np.concatenate([self.y,[[self.label]]],axis=0)
        np.savez(DATABASE_PATH,description=description,label=label)

        print('Do you wish to play it again? (y/n)')
        reply=input()
        print(reply)
        if reply=='y':
            self.run()
        else:
            print('Thank you for playing!')



    

    def starting(self):
        ready=False
        print("Hello! This is an agent for the Med Andra Ord game. To begin, you can select an entity from this three, Apple,Banana, Orange")
        print('Do not tell me!')
        print('Have you decided yet? (y/n)')
        reply1=input()
        if reply1=='y':
            ready=True
        else:
            ready=False
        while not ready:
            print('Have you decided yet? (y/n')
            reply1=input()
            if reply1=='y':
                ready=True
            else:
                ready=False


if __name__=='__main__':
    md=Decision_Tree_Agent()
    md.__init__()
    md.run()

