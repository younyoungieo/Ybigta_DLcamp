class BPETokenizer:
    def __init__(self, corpus=None):
        self.corpus = corpus
    
    def add_corpus(self, corpus):
        self.corpus = corpus
    
    def train(self, n_iter):
        # Training logic here
        pass
    
    def tokenize(self, text, padding=False, max_length=None):
        # Tokenization logic here
        pass
    
    def __call__(self, text, padding=False, max_length=None):
        return self.tokenize(text, padding, max_length)

# tokenizer = BPETokenizer(
#     corpus: Optional[Union[List[str], str]] = None
# )

# tokenizer.add_corpus(
#     corpus: Union[List[str], str]
# ) -> None

# tokenizer.train(n_iter: int) -> None

# tokenizer.tokenize(
# # text str list of str
#     text: Union[List[str], str],
#     padding: bool = False,
#     max_length: Optional[int] = None
# ) -> Union[List[List[int]], List[int]]

# tokenizer(
#     text,
#     padding,
#     max_length
# ) -> Union[List[List[int]], List[int]]
    
class WordTokenizer:
    def __init__(self, corpus=None):
        self.corpus = corpus
    
    def add_corpus(self, corpus):
        self.corpus = corpus
    
    def train(self, n_iter):
        # Training logic here
        pass
    
    def tokenize(self, text, padding=False, max_length=None):
        # Tokenization logic here
        pass
    
    def __call__(self, text, padding=False, max_length=None):
        return self.tokenize(text, padding, max_length)