import csv
import datetime

def get_last_id():
    with open('database.csv', 'rb') as file:
        file.seek(-3, 2)
        last_str = file.readlines()[-1].decode('utf-8')
        last_id = ''
        for char in last_str:
            if char != ',':
                last_id += char
            else: break
    return int(last_id)

def append_to_csv(last_id, data_new_note):
    notes = read_csv()
    temp={}
    temp["id"] = last_id + 1
    temp["title_note"] = data_new_note[0]["title_note"]
    temp["text_note"] = data_new_note[0]["text_note"]
    temp["date_note"] = datetime.datetime.now()
    notes.append(temp)
    write_csv(notes)

def read_csv() -> list:
    notes = []
    with open('database.csv', 'r', encoding='utf-8') as fin:
        csv_reader = csv.reader(fin)
        for row in csv_reader:
            temp = {}
            temp["id"] = int(row[0])
            temp["title_note"] = row[1]
            temp["text_note"] = row[2]
            temp["date_note"] = row[3]
            notes.append(temp)
    return notes

def write_csv(notes: list):
    with open('database.csv', 'w', encoding='utf-8', newline="") as fout:
        csv_writer = csv.writer(fout)
        for note in notes:
            csv_writer.writerow(note.values())