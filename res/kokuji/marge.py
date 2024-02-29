from pypinyin import pinyin as func_pinyin
import getPinyin as gp

class Info:
    def __init__(self, reading, pinyin):
        self.reading = reading
        self.pinyin  = pinyin

    def getReading(self):
        self.reading = [a for a in self.reading if a != ""]
        return list(set(self.reading))

    def getPinyin(self):
        self.pinyin = [a for a in self.pinyin if a != ""]
        return list(set(self.pinyin))

    def addReading(self, reading):
        self.reading += reading
    
    def addPinyin(self, pinyin):
        self.pinyin += pinyin


files = {
        'kokuji_list_of_jigen-net.md', 
        'kokuji-no-jiten.md',
        'nihonjin-no-tsukutta-kanji.md',
        # 'waseikanji-no-jiten.md'
        }

hanzi_dict = {}
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()

        for li in lines[3:]:
            zi_uni  = li.split("|")[2]
            reading = li.split("|")[5] if li.split("|")[5]!="NONE" else ""
            pinyin  = li.split("|")[6] if li.split("|")[6]!="NONE" else ""

            if zi_uni == "NONE":
                continue
            if zi_uni in hanzi_dict:
                hanzi_dict[zi_uni].addReading(reading.split(","))
                hanzi_dict[zi_uni].addPinyin(pinyin.split(","))
            else:
                hanzi_dict[zi_uni] = Info(reading.split(","), pinyin.split(","))

output_file_path = "marged-kokuji.md"
idx = 1
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write( "|No|character|読み|拼音|拼音(hancibao)|拼音(pypinyin)|備考|\n" )
    output_file.write( "|:---|:--|:--|:--|:--|:--|\n" )
    for k, v in sorted(hanzi_dict.items()):
        hanzi = k.split(' ')[0]
        unicode = k.split('+')[1].lower()
        output_file.write( 
            "|{:04}|{}|{}|{}|{}|{}||\n".format(
                idx, 
                k, 
                ",".join(v.getReading()), 
                ",".join(set(v.getPinyin())), 
                gp.get_pinyin_from_hancibao(unicode),
                ",".join(func_pinyin(hanzi, heteronym=True)[0])
            )
        )
        idx += 1
        print(idx)
