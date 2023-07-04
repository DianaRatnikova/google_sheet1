import gspread  # библиотека для работы с гугл таблицами
from config import KEY_DRAFT_LIST, KEY_RECONCILIATION_LIST



if __name__ == "__main__":


    gs = gspread.service_account(filename='credits.json')  # подключаем файл с ключами и пр.

    sh_reconciliation = gs.open_by_key(KEY_RECONCILIATION_LIST)  # подключаем таблицу по ID
    worksheet_reconciliation = sh_reconciliation.sheet1  # получаем первый лист
    res_reconciliation1 = worksheet_reconciliation.get_all_values()
    print(f"{type(res_reconciliation1)=}")
    #for item in res_reconciliation1:
    #    print(item)

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


    sh_draft = gs.open_by_key(KEY_DRAFT_LIST)  # подключаем таблицу по ID
    worksheet_draft = sh_draft.sheet1  # получаем первый лист
    res_draft = worksheet_draft.get_all_values() # получить все данные в виде списка списков (одна строка=один список)
    print(f"{type(res_draft) = }")
    for item in res_draft:
        print(item)

    try:
        res_draft = worksheet_draft.get_all_records() # получить все данные в виде списка списков (одна строка=один список)
    except gspread.exceptions.GSpreadException:
        print("Заголовки таблиц не уникальные!")    
    print(f"{type(res_draft) = }")
    for item in res_draft:
        print(item)

    res_draft3 = worksheet_draft.get('A2:C3')
    print(f"{type(res_draft3)=}")
    print(f"{res_draft3=}")    


    newRec = ["This", "is", "a", "new",  "string"] # добавить новые данные в строкуc2
    worksheet_draft.insert_row(newRec, 2)
    print("Добавлена новая строка (insert_row)")

    worksheet_draft.append_row(["Append", "_", "row"]) # добавить новую строку в конец
    print("Добавлена новая строка (append_row)")

    worksheet_draft.update_cell(1, 1, "New_Meaning") # Изменить значение ячейки (номер строки, номер столбца, новое значение)