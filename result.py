import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('students.csv')
print("Sabhi Students ka Data:")
print(df)

df['Result'] = df['Percentage'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')
result_count = df['Result'].value_counts()
print("\nResult Summary:")
print(result_count)

topper = df.loc[df['Percentage'].idxmax()]
print(f"\nClass Topper: {topper['Name']} with {topper['Percentage']}%")

plt.figure(figsize=(8, 6))
plt.pie(result_count, labels=result_count.index, autopct='%1.1f%%', 
        colors=['#4CAF50', '#F44336'], startangle=90)
plt.title('Class Result Analysis - Pass vs Fail', fontsize=16, fontweight='bold')
plt.axis('equal')
plt.savefig('result_pie_chart.png')
print("\nGraph save ho gaya: result_pie_chart.png")
plt.show()