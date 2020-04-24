dbpath = r"C:\Users\umut\PycharmProjects\Anketor\db.sqlite3"
imgpath = r"C:\Users\umut\PycharmProjects\Anketor\templates\polls\assets\img"

import os

import pandas as pd
from sqlalchemy import create_engine

femalepath = os.path.join(imgpath, 'females')
malepath = os.path.join(imgpath, 'males')


def get_name_and_path(pathlist):
    dicto = {}
    for i in pathlist:
        dicto[os.path.split(i)[-1].split(".")[0]] = i

    return dicto


female_images = [os.path.join(femalepath, i) for i in os.listdir(femalepath)]
female_dict = get_name_and_path(female_images)

male_images = [os.path.join(malepath, i) for i in os.listdir(malepath)]
male_dict = get_name_and_path(male_images)

sqlite_engine = create_engine(f'sqlite:///{dbpath}')
pg_engine = create_engine('postgresql+psycopg2://postgres:123456@localhost/anketdb')

choice_df = pd.read_sql_table('polls_choice', sqlite_engine)
question_df = pd.read_sql_table('polls_question', sqlite_engine)

choice_df.to_sql('polls_choice', pg_engine, if_exists='replace')
question_df.to_sql('polls_question', pg_engine, if_exists='replace')

# for row in polls_df.iterrows():
#     row = row[1]
#     actorname = row['choice_text']
#     actorname = re.sub(r" ?\([^)]+\)", "", actorname).lower().replace(" ", "")
#
#     if int(row['question_id']) == 1:  # erkek
#         imgpath = male_dict[actorname]
#
#     elif int(row['question_id']) == 2:  # kadin
#         imgpath = female_dict[actorname]
#
#     else:
#         raise ValueError("Are you deal with transgender?")
#
#     row['imgpath'] = imgpath
