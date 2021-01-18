# import re
#import string
import pandas as pd # data manipulation
from sklearn.impute import SimpleImputer # missing values imputation
import numpy as np # support for n-dimensions matrices and arrays
import streamlit as st
import time


class Cleaner:
    def __init__(self, df, dataset_profile):
        self.df = df
        self.report = dataset_profile
        self.check_type()
        self.numerical_cols = [cname for cname in df.columns if
                df[cname].dtype in ['int64', 'float64']]
        self.categorical_cols = [cname for cname in df.columns if
                    df[cname].nunique() < 10 and
                    df[cname].dtype == "object"]
        self.check_emptiness()

    def check_type(self):
        aux = type(self.df)
        self.report["Type"] = str(aux)
        if isinstance(self.df, pd.DataFrame):
            text = "Type checked! Ready to go."
            print(text)
        else:
            text = "Variable inputed is not valid, please input a dataframe object"
            raise Exception(text)

    def check_emptiness(self):
        '''
        This method  checks if the dataframe is empty.
        '''
        self.report["Empty"] = self.df.empty
        if self.df.empty:
            raise Exception("Please insert a non-empty dataframe")

    def check_shape(self, expected_shape=None):
        '''
        This method checks if the shape of the dataframe is valid.
        '''
        self.report["Shape"] = self.df.shape
        print("Checking Shape...", end=" ")
        if expected_shape is None or expected_shape == self.df.shape:
            print("Ok!")
            return True
        elif self.df.shape != expected_shape:
            print("Ops!")
            raise Exception(f"\nSorry, dataframe shape not valid\nExpected shape: {expected_shape}\nGiven shape: {self.df.shape}")

    def check_required_cols(self, required_cols):
        ''' This method checks if all required columns are in the dataset provided '''
        self.report["Required Cols"] = required_cols
        print("Checking required columns...", end=" ")
        for c in required_cols:
            if c not in self.df.columns:
                print("Ops!")
                print(f"\nColumn '{c}' not found in the dataframe. This is a required column.")
                raise Exception(f"Please insert the missing column: {c}")
        print("Ok!")
        return True


    def check_col_types(self, accepted_types=["float64", "object", "int64"]):
        '''
        This method checks for supported columns types
        '''
        values = list(self.df.dtypes.unique())
        self.report["Cols type"] = str(values)
        print("Checking columns types ...", end=" ")
        for col_type in self.df.dtypes:
            if col_type not in accepted_types:
                print("Ops!")
                raise Exception(f"Column type '{col_type}' not supported")
        # st.write(f"Supported col types: **{accepted_types}**")
        print("Ok!")
        return True


    def set_timestamp_index(self, date_cols:list):
        '''
        This method get date columns and convert them to datetime format.
        Once we have datetime formats we add them as the index.
        '''
        print("Setting timestamp as index...", end=" ")
        try:
            if len(date_cols) == 1:
                self.df['datetime'] = pd.to_datetime(self.df[date_cols[0]], infer_datetime_format=True)
            else:
                self.df['datetime'] = pd.to_datetime(self.df[date_cols])
            df = self.df.set_index('datetime')
            df.drop(date_cols, axis=1, inplace=True)
#             print("Everthing ok for index validation.")
            self.df = df
            # st.write(f" Timeseries begins at **{self.df.index[0]}** and finishes at **{self.df.index[-1]}**")
            print("Ok!")

        except Exception as e:
            print("Ops!")
            print(f"Something went wrong here: {e}.",end="")
            print(" Index validation was not successful")



#     def standardise_column_names(self, df, punct=string.punctuation ,remove_punct=True):
#         '''This function returns dataframe with standard column names'''
#         df.rename(str.lower, axis='columns', inplace = True)

#         if remove_punct :
#             translator = str.maketrans(punct, ' '*len(punct))
#             for c in df.columns:
#                 c_mod = c.translate(translator)
#                 c_mod = c_mod.replace("  ","_").replace(" ","_")
#                 while c_mod[-1] == '_':
#                     c_mod = c_mod[:-1]
#                 df.rename({c: c_mod}, inplace=True, axis=1)
#         return df

    def drop_duplicates(self, option='first'):
        '''This method returns dataframe after dropping duplicates'''
        print("Dropping duplicates...", end=" ")
        aux = self.df.drop_duplicates(keep = option)
        self.report["N° of duplicates"] = self.df.shape[0] - aux.shape[0]
        # st.write(f"**{self.df.shape[0] - aux.shape[0]} duplicates** were found and removed")
        self.df = aux
        print("Ok!")

    def perc_of_missing_values(self, df):
        '''This method returns percentage of missing values in a dictionary'''
        aux = df.isnull().sum().to_dict()
        for idx, value in aux.items():
            aux[idx] = value / len(df)
        return aux

    def drop_cols(self, df, threshold):
        '''This method drop cols that have a percentage of missing values superior to the threshold'''
        aux = self.perc_of_missing_values(df)
        cols_with_missing = []
        for col, value in aux.items():
            if value > threshold:
                cols_with_missing.append(col)
        return df.drop(cols_with_missing, axis=1)

    def imputer(self, df, strategy):
        '''This method imputs missing values with the strategy choosen'''
        my_imputer = SimpleImputer(strategy=strategy)
        df_v2 = pd.DataFrame(my_imputer.fit_transform(df))
        df_v2.columns = df.columns
        df_v2.index = df.index
        return df_v2

    def add_missing_label(self, df, cols_with_missing):
        '''This method add labels for the missing values and returns the df '''
        for col in cols_with_missing:
            df[col + '_was_missing'] = df[col].isnull()
        return df

    def get_cols_with_missing(self, df):
        '''This method returns a series with the cols that have missing values'''
        s = df.isnull().sum() > 0
        return s[s==True]

    def restore_missing_values(self, strategy="constant", threshold=0.8, add_label=False):
        '''This method restore missing values and/or drop cols according to the inputed threshold and strategy'''
        missing_values = self.df.isnull().sum().sum()
        if missing_values != 0:
            print("Restoring missing values...", end=" ")
            try:
                self.df = self.drop_cols(self.df, threshold)
                cols_with_missing = self.get_cols_with_missing(self.df)
                if add_label:
                    self.df = self.add_missing_label(self.df, list(self.get_cols_with_missing(self.df).index))
                self.df = self.imputer(self.df, strategy)
                print("Ok!")
                print(f"{missing_values} missing values were found")
                self.report["N° of missing values"] = int(missing_values)
                # st.write(f"**{missing_values} missing values** were found and predicted")
            except Exception as e:
                print("Ops!")
                print(f"Something went wrong here: {e}. Missing values restoration failed!")


    def replace_outliers(self):
        '''This method replace outliers values with the median'''
        print("Replacing outliers...", end=" ")
        total_outliers = []
        try:
            for col in self.numerical_cols:
                median = self.df[col].median()
                std = self.df[col].std()
                outliers = (self.df[col] - median).abs() > std
                total_outliers.append(outliers)
                self.df[outliers] = np.nan
                self.df[col].fillna(median, inplace=True)
            print("Ok!")
            if len(total_outliers) != 0:
                print(f"{len(total_outliers)} outliers were found.")
                self.report["N° of outliers"] = len(total_outliers)
                # st.write(f"**{len(total_outliers)} outliers** were replaced.")
        except Exception as e:
            print("Ops!")
            print(f"Something went wrong here: {e}. Replacing outliers failed!")

    def __repr__(self):
        return "Cleaner()"

    def __str__(self):
        return "Cleaner class"
