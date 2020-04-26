message = input('> ')


def emoji_converter(phrase):
    words = phrase.split(' ')
    emojis = {
        ':)': '😊',
        ':(': '😢'
    }
    output = ''
    for word in words:
        output += emojis.get(word, word) + " "

    return output


print(emoji_converter(message))

