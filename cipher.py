
class Cipher():
    def __init__(self, filename):
        self.filename = filename

    def creat_ascii_dic(self):
        ascii_dic=[]
        for a in range(97, 123):
            for b in range(97, 123):
                for c in range(97, 123):
                    ascii_dic.append([a,b,c])
        return ascii_dic

    def xor(self, ascii_disc):
        cipher=open('cipher1.txt').read().strip().split(',')
        #print cipher
        maybe=[]
        #code_ascii=0
        #w=0
        #a = 0
        #s = 0
        for code_ascii in ascii_disc:
            #print code_ascii
            str = ''
            for i,cipher_word in enumerate(cipher):
                s = code_ascii[i%3]
                w = int(cipher_word)
                a = w ^ s
                if a in range(31, 124):
                    str += chr(a)
                else:
                    str=''
                    break
            if str != '' and 'the' in str and 'and' in str:
                maybe.append(str)
                print str
                code = ''
                code=chr(code_ascii[0])+chr(code_ascii[1])+chr(code_ascii[2])
                print code
                    
        return maybe

t = Cipher('cipher1.txt')
dic = t.creat_ascii_dic()
res = t.xor(dic)
#print res
#print dic


            
