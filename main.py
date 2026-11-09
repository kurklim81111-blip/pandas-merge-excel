import pandas as pd
import glob


all_files = glob.glob("Shop*.xlsx")

if not all_files:
    print("Файлы для объединения не найдены в папке со скриптом")
    exit()

dataframes = []

for filename in all_files:
    print(f"Читаю файл {filename}")
    df = pd.read_excel(filename)
    dataframes.append(df)

combined_df = pd.concat(dataframes, ignore_index=True)

# Обработка пустых строк
num_col = combined_df.select_dtypes(include=["number"]).columns
combined_df[num_col] = combined_df[num_col].fillna(0)

combined_df = combined_df.fillna("Нет данных")

combined_df.to_excel("All_shops.xlsx", index=False)


print(f"\nГотово! Объединено {len(all_files)} файлов")
print("Результат сохранён в файл All_shops.xlsx")