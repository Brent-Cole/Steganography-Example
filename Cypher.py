
class Cypher():
    """ This class is used for the purpose of using the caeser cypher to perform basic encrypting and decrypting processes.

    Functions:
    caeser(arg1,int,arg2)
    revCaeser(arg1,int,arg2)
    """

    def caeser(words, num, args):
        """caeser(words,num,args)   this function will use the caeser cypher to transform what is passed into it

        :param words: this is what will be processed
        :param num: the key
        :param args: the alphabet or characters that the cypher will be using ex: 'abcdefghijklmnopqrstuvwxyz'
        :return: words has been encoded
        """
        encoded = ""
        ALPHABET = args
        i = 0
        if words == '':
            words = "you typed an empty string"
        for ch in words:
            if words[i] == ' ':
                encoded += ' '
            else:
                index = ALPHABET.find(words[i])
                next_index = (index + int(num)) % 26
                encoded += ALPHABET[next_index]
            i = i + 1
        return encoded

    def revCaeser(words, num, args):
        """revCaeser(words,num,args)   this function will use the caeser cypher to transform what is passed into it

                :param words: this is what will be processed
                :param num: the key
                :param args: the alphabet or characters that the cypher will be using ex: 'abcdefghijklmnopqrstuvwxyz'
                :return: words has decoded
                """
        decode = ""
        ALPHABET = args
        i = 0
        for ch in words:
            if words[i] == ' ':
                decode += ' '
            else:
                index = ALPHABET.find(words[i])
                next_index = (index - int(num)) % 26
                decode += ALPHABET[next_index]
            i = i + 1
        return decode

