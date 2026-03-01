#We will predict Earnings Per Share (EPS) based on Apple’s financial performance.
print("Apple Sales Analysis - Task 2 Started")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#This is a Machine Learning task so we should also import these
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

sales_df = pd.read_csv(r"C:\Users\91783\Downloads\CODTECH IT SOLUTIONS - INTERNSHIP\APPLE SALES PROJECT (TASK 2)\data\Apple 2009-2024.csv")

# MAIN MENU
while(True):
    print("Main Menu")
    print("Note: Proceed SEQUENTIALLY: Execute options 3,4,5,6 in order only!")
    print("1. SETUP & LOAD SALES DATA")
    print("2. DATA STATISTICS MENU FOR SALES")
    print("3. TRAIN–TEST SPLIT")
    print("4. BUILD & TRAIN THE MODEL")
    print("5. MODEL EVALUATION")
    print("6. ACTUAL VS PREDICTED EPS - SCATTER CHART COMPARISON")
    print("7. Exit")
    choice=int(input("Enter your choice:"))

    if choice==1:
        while(True):
            print("DATA MENU")
            print("1. Display the dataset from top")
            print("2. Display the dataset from bottom")
            print("3. Exit")
            ch1=int(input("Enter your choice:"))
            #Since the datasets are very large, so instead of loading everything,I am extracting only the 5 values for analysis
            if ch1==1:
                print(sales_df.head())
            elif ch1==2:
                print(sales_df.tail())
            elif ch1==3:
                break

    elif choice==2:
        while(True):
            print("DATA STATISTICS MENU FOR SALES")
            print("1. Display the shape of the dataset")
            print("2. Display the data types of the dataset")
            print("3. Display the columns of the dataset")
            print("4. Display the missing values of the dataset")
            print("5. Exit")
            ch2=int(input("Enter your choice:"))
            if ch2==1:
                print("Dataset shape:",sales_df.shape)
            elif ch2==2:
                print("DataTypes:",sales_df.dtypes)
            elif ch2==3:
                print("Columns:",sales_df.columns)
            elif ch2==4:
                print(sales_df.isnull().sum())
            elif ch2==5:
                break

    elif choice==3:
        print("TRAIN–TEST SPLIT") #We will predict Earnings Per Share (EPS) based on Apple’s financial performance.
        df = sales_df.dropna() #Drop rows with NaN values
        # Target variable
        y=sales_df["EPS"]
        # Feature variables
        x=sales_df[["Revenue (millions)","Net Income (millions)","Gross Profit (millions)",
                "Op Income (millions)","Total Assets (millions)","Cash on Hand (millions)",
                "Long Term Debt (millions)","Employees"]]
        # Train-test split
        x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.2,random_state=42)
        print("Training data shape:", x_train.shape)
        print("Testing data shape:", x_test.shape)

    elif choice==4:
        try:
            print("BUILD & TRAIN THE MODEL")
            model=LinearRegression() #Create the Linear Regression Model
            model.fit(x_train,y_train) #Train the Model
            print("Model training completed")
            #Simple way to confirm the 'MODEL IS TRAINED'
            print("Model coefficients:")
            print(model.coef_)
            print("Model intercept:")
            print(model.intercept_)
        except NameError:
            print("ERROR: Please run TRAIN–TEST SPLIT (Option 3) first.")

    elif choice==5:
        try:
            print("MODEL EVALUATION")
            y_pred= model.predict(x_test)
            mse = mean_squared_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)
            print("Mean Squared Error (MSE):", mse)
            print("R square Score:", r2)
            print("Model Evaluation Summary")
            if r2 >= 0.9:
                print("Excellent model: R square score is close to 1")
            elif r2 >= 0.75:
                print("Very good model: Strong predictive power")
            elif r2 >= 0.5:
                print("Moderate model: Acceptable predictions")
            else:
                print("Weak model: Needs improvement")
        except NameError:
            print("ERROR: Please run Option 3&4 first.")

    elif choice==6:
        print("ACTUAL VS PREDICTED EPS - SCATTER CHART COMPARISON")
        plt.figure(figsize=(6,4))
        plt.scatter(y_test, y_pred)
        plt.xlabel("Actual EPS")
        plt.ylabel("Predicted EPS")
        plt.title("Actual vs Predicted EPS")
        plt.tight_layout()
        plt.show()

    elif choice==7:
        print("Exiting program...")
        break     

                


        


            




        


