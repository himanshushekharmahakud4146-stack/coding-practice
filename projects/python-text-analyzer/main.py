"""
Python Text Analyzer Project

Features:
- Count total words
- Count unique words
- Ignore stopwords
- Show top 10 frequent words
- Export results to file

This project is part of my Python learning journey.
"""

# Step 1: Input text

fname = input("Enter file name: ")

try:
    with open(fname, "r") as f:
        text = f.read().lower()

except FileNotFoundError:
    print("File not found.")


# Step 2: Stopwords list
stopwords = {"a", "the", "is", "and", "to", "of", "in", "on"}

# Step 3: Remove punctuation
clean_text = ""

for ch in text:
    if ch.isalpha() or ch == " ":
        clean_text += ch
    else:
        clean_text += " "

# Step 4: Split into words
words = clean_text.split()

# Step 5: Count frequency
freq = {}
filtered_words = []

for word in words:
    if word not in stopwords:
        filtered_words.append(word)
        freq[word] = freq.get(word, 0) + 1

# Step 6: Calculate statistics
total_words = len(filtered_words)
unique_words = len(freq)

# Step 7: Sort by frequency
sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)

# Step 8: Get top 10 words
top_10 = sorted_words[:10]

# Step 9: Print results
print("\nTotal words:", total_words)
print("Unique words:", unique_words)

print("\nTop 10 Most Frequent Words:\n")

for word, count in top_10:
    print(f"{word} : {count}")

# Step 10: Export results to file
with open("output.txt", "w") as f:
    for word, count in top_10:
        f.write(f"{word} : {count}\n")

print("\nResult saved to output.txt")
