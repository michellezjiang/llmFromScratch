import tiktoken
tokenizer = tiktoken.get_encoding("gpt2")
text = (
    "Hello, do you like tea? <|endoftext|> In the sunlit terraces"
     "of someunknownPlace."
)
integers = tokenizer.encode(text, allowed_special={"<|endoftext|>"})
print(integers)

strings = tokenizer.decode(integers)
print(strings)

unknownWord = "Akwirw ier"
unknownId = tokenizer.encode(unknownWord, allowed_special={"<|endoftext|>"})
print(unknownId)
for token in unknownId:
    print(tokenizer.decode([token]))

print(tokenizer.decode(unknownId))