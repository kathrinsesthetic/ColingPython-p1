import pickle
from tqdm import tqdm


class UnigramMorphAnalyzer:

    def __init__(self):
        self.stats = {}
        self.train_data = []
        self.eval_data = []

    def __getitem__(self, item):
        return self.stats[item]

    def save(self):
        with open('pos_statistics.pkl', 'wb') as file:
            pickle.dump(self.stats, file)

    def load(self):
        try:
            with open('pos_statistics.pkl', 'rb') as stat:
                self.stats = pickle.load(stat)
                return self.stats
        except FileNotFoundError:
            self.train()
            return self.stats

    def train(self, a=None, b=None):
        if not (a and b):
            self.train_data, self.eval_data, data = [], [], []
            with open('pos_data.txt', 'r', encoding="utf-8") as file:
                for line in tqdm(file):
                    token, pos = line.strip().split(' ')
                    data.append((token, pos))
            self.train_data = data[:4 * len(data) // 5]
            self.eval_data = data[4 * len(data) // 5:]
        else:
            data = list(zip(a, b))
            self.train_data = data[:4 * len(data) // 5]
            self.eval_data = data[4 * len(data) // 5:]
        for token, pos in self.train_data:
            if token.isalnum():
                for i in range(1, min(len(token) + 1, 5)):
                    ending = token[-i:]
                    if ending not in self.stats:
                        self.stats[ending] = {}
                    if pos not in self.stats[ending]:
                        self.stats[ending][pos] = 1
                    else:
                        self.stats[ending][pos] += 1
            else:
                if token not in self.stats:
                    self.stats[token] = {}
                if pos not in self.stats[token]:
                    self.stats[token][pos] = 1
                else:
                    self.stats[token][pos] += 1

    def predict(self, token: str):
        if not self.stats:
            pos_data = self.load()
        else:
            pos_data = self.stats
        ending = token[-min(len(token), 4):]
        try:
            total = sum(pos_data[ending].values())
            result = dict()
            for tag, value in pos_data[ending].items():
                probability = value / total
                result[tag] = probability
        except KeyError:
            return {0: 0}
        return dict(sorted(result.items(), key=lambda item: item[1], reverse=True))

    def eval(self, a=None, b=None):
        if not (a and b and self.eval):
            data, self.eval_data = [], []
            with open('pos_data.txt', 'r', encoding="utf-8") as file:
                for line in tqdm(file):
                    token, pos = line.strip().split(' ')
                    data.append((token, pos))
            self.eval_data = data[4 * len(data) // 5:]
            # Start evaluation
            correct = 0
            for token, tag in tqdm(self.eval_data):
                prediction = tuple(self.predict(token))[0]
                if prediction == tag:
                    correct += 1
            return correct / len(self.eval_data)
        elif a and b:
            correct = 0
            for token, tag in zip(a, b):
                prediction = tuple(self.predict(token))[0]
                if prediction == tag:
                    correct += 1
            return correct / len(b)
        elif self.eval:
            correct = 0
            for token, tag in tqdm(self.eval_data):
                prediction = tuple(self.predict(token))[0]
                if prediction == tag:
                    correct += 1
            return correct / len(self.eval_data)


if __name__ == '__main__':
    tagger = UnigramMorphAnalyzer()
    tagger.train()
    tagger.save()
    tagger.load()
    print(tagger.predict('стекло'))
    print(tagger['гла'])
    print(tagger.eval())
