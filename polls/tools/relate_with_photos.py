dbpath = r"C:\Users\umut\PycharmProjects\Anketor\db.sqlite3"
imgpath = r"C:\Users\umut\PycharmProjects\Anketor\templates\polls\assets\img"
import re

# dbdeki isimlerden parantezleri kaldırmayı unutma
from sqlalchemy import create_engine
import os
import pandas as pd

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

engine = create_engine(f'sqlite:///{dbpath}')
polls_df = pd.read_sql_table('polls_choice', engine)

for row in polls_df.iterrows():
    row = row[1]
    actorname = row['choice_text'].lower().replace(" ", "")
    # todo: re.sub('[()]', '', actorname)    -> DENE !

    if int(row['question_id']) == 1:  # erkek
        imgpath = male_dict[actorname]

    elif int(row['question_id']) == 2:  # kadin
        imgpath = female_dict[actorname]

    else:
        raise ValueError("Are you deal with transgender?")

    row['imgpath'] = imgpath
