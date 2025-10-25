# text_summarizer.py
import nltk, re
from nltk.corpus import stopwords
from collections import Counter
nltk.download('stopwords')

def summarize(text, n=2):
    words = [w.lower() for w in re.findall(r'\w+', text) if w.lower() not in stopwords.words('english')]
    freq = Counter(words)
    top = [w for w,_ in freq.most_common(n)]
    return " ".join(top)

print(summarize("Hacktoberfest is amazing. You learn and grow by contributing."))
