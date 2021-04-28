import numpy as np
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier,DecisionTreeRegressor, plot_tree
from sklearn import preprocessing

DATABASE_PATH='test_dataset.npz'
NUMBER_OF_TRIES=5

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
        self.X=self.le_X.fit_transform(self.X)
        self.y=self.le_y.fit_transform(self.y)

    
    def fit_model(self):
        self.dt.fit(self.X,self.y)
    
    def plot_model(self):
        plot_tree(self.dt,filled=True)
        plt.show()
        

    def save_database(self,filename):

    
    def run(self):
        self.__init__()
        self.starting()
        self.predicting()
        self.ending=self.recording()

    def predicting(self):
        print('I am happy  that you have made your choice and let us start the game!')
        get_the_answer=False
        for _ in range(NUMBER_OF_TRIES):
            print('please give me some information for guessing')
            description=str(input())
            self.descriptions.append(description)
            get_the_answer,answer=self.guessing(description)
            if get_the_answer:
                print('Ah! I get the answer!')
                print('It is '+str(answer)+'!')
                print('Am I right? (y/n)')
                reply=input()
                if reply=='y' or 'Y':
                    self.label=answer
                else:
                    print('please give the right answer.')
                    answer=input() 
                    self.label=answer
                break
    

    def guessing(self,description):
        prob=self.dt.predict_proba(description)



    def recording(self):
        print('start recording the data')


        print('Do you wish to play it again? (y/n)')
        reply=input()
        if reply=='y' or 'Y':
            self.run()
        else:
            print('Thank you for playing!')



    

    def starting(self):
        ready=False
        print("Hello! This is an agent for the Med Andra Ord game. To begin, you can select an entity from this three, Apple,Banana, Orange")
        print('Do not tell me!')
        print('Have you decided yet? (y/n)')
        reply1=input()
        if reply1=='y' or 'Y':
            ready=True
        else:
            ready=False
        while not ready:
            print('Have you decided yet? (y/n')
            reply=input()
            if reply1=='y' or 'Y':
                ready=True
            else:
                ready=False


if __name__=='__main__':
    md=Decision_Tree_Agent()
    md.__init__()
    md.run()

