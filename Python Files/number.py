import csv
from collections import defaultdict

def unique_buyers_from_csv(csv_file):
    firm_buyers = defaultdict(set)
    politicians_who_sold = set()

    with open(csv_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Trans'] == 'Buy':
                firm = row['Name']
                buyer = row['Last Name']  # Assuming 'Buyer' is the column containing individual names
                firm_buyers[firm].add(buyer)
            elif row['Trans'] == 'Sell':
                politicians_who_sold.add((row['Name'], row['Last Name']))

    # Remove politicians who sold shares
    for firm, buyers in firm_buyers.items():
        for politician in politicians_who_sold:
            if politician[0] == firm and politician[1] in buyers:
                buyers.remove(politician[1])

    # Sort firms by the number of unique buyers
    sorted_firms = sorted(firm_buyers.items(), key=lambda x: len(x[1]), reverse=True)

    print("Top 10 firms based on unique buyers (excluding politicians who sold shares):")
    for rank, (firm, buyers) in enumerate(sorted_firms[:10], start=1):
        buyer_list = ", ".join(buyers)
        print(f"{rank}. {firm}: {len(buyers)} individuals ({buyer_list})")

# Example usage:
csv_file = 'Congress Data.csv'
unique_buyers_from_csv(csv_file)