import gspread  # библиотека для работы с гугл таблицами
from config import KEY_DRAFT_LIST, KEY_RECONCILIATION_LIST, KEY_SCREENS_BALANCE, SHEETNAME_SCREENS_BALANCE
import datetime
import pytz


def get_all_values_from_sheet(gs: gspread.client.Client, key_to_googlesheet: str) -> gspread.worksheet.Worksheet: #list[list[str]]
    spreadsheet = gs.open_by_key(key_to_googlesheet)
    worksheet = spreadsheet.sheet1
    return worksheet


def make_string_for_table() -> list:
    moscow_tz = pytz.timezone('Europe/Moscow')
    # Get the current Moscow time
    moscow_now = datetime.datetime.now(moscow_tz)

    # Форматирование даты в раздельные строки
    date_str = moscow_now.strftime("%Y-%m-%d")
    time_str = moscow_now.strftime("%H:%M:%S")
    data_row = [date_str, time_str]
    return data_row


def save_to_sheet(key_to_googlesheet: str):
    spreadsheet = gs.open_by_key(key_to_googlesheet)
    worksheet = spreadsheet.worksheet("New Sheet")
    worksheet.insert_row([1,2,3,4,5])


def read_balance_data(key_to_googlesheet: str) -> list[list]:
    spreadsheet = gs.open_by_key(key_to_googlesheet)
    worksheet = spreadsheet.worksheet(SHEETNAME_SCREENS_BALANCE)
    return worksheet.get_all_values()




if __name__ == "__main__":

    gs = gspread.service_account(filename='credits.json')  # подключаем файл с ключами и пр.
    print(f"{type(gs) = }")

# Работа с таблицей сверок провайдеров
    worksheet_reconciliation = get_all_values_from_sheet(gs, KEY_RECONCILIATION_LIST)
    print(f"{type(worksheet_reconciliation) =}") # 
    res_reconciliation1 = worksheet_reconciliation.get_all_values()
   # print(f"{res_reconciliation1 = }")

    try:
        res_reconciliation2 = worksheet_reconciliation.get_all_records()
        print(f"{type(res_reconciliation2)=}")
        for item in res_reconciliation2:
            print(item)
    except gspread.exceptions.GSpreadException:
        print("Заголовки таблицы не уникальные!")    


    res_reconciliation3 = worksheet_reconciliation.get('A2')
    print(f"{type(res_reconciliation3)=}")
    print(f"{res_reconciliation3=}")                                                    

    save_to_sheet(KEY_DRAFT_LIST)

    data_row = make_string_for_table()
    print(f"{data_row = }")


    values_course = read_balance_data(KEY_DRAFT_LIST)
    print(f"{len(values_course) = }")

  #  worksheet_draft = get_all_values_from_sheet(KEY_DRAFT_LIST)  # подключаем таблицу по ID,  # получаем первый лист
  #  res_draft = worksheet_draft.get_all_values() # получить все данные в виде списка списков (одна строка=один список)
  #  print(f"{type(res_draft) = }")
  #  for item in res_draft:
  #      print(item)
#
  #  try:
  #      res_draft = worksheet_draft.get_all_records() # получить все данные в виде списка списков (одна строка=один список)
  #  except gspread.exceptions.GSpreadException:
  #      print("Заголовки таблиц не уникальные!")    
  #  print(f"{type(res_draft) = }")
  #  for item in res_draft:
  #      print(item)
#
  #  res_draft3 = worksheet_draft.get('A2:C3')
  #  print(f"{type(res_draft3)=}")
  #  print(f"{res_draft3=}")    


#   newRec = ["This", "is", "a", "new",  "string"] # добавить новые данные в строкуc2
#   worksheet_draft.insert_row(newRec, 2)
#   print("Добавлена новая строка (insert_row)")
#
#   worksheet_draft.append_row(["Append", "_", "row"]) # добавить новую строку в конец
#   print("Добавлена новая строка (append_row)")
#
#   worksheet_draft.update_cell(1, 1, "New_Meaning") # Изменить значение ячейки (номер строки, номер столбца, новое значение)