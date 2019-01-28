import random

vocabulary01={'同學':'classmate','歡迎':'welcome','起司':'cheese','派':'pie',
              '客廳':'living room','照片':'picture','警察':'police officer','護士':'nurse',
              '男演員':'actor','女演員':'actress','男服員':'waiter','女服員':'waitress',
              '醫生':'doctor','家庭':'family','農夫':'farmer','廚師':'cook',
              '家庭主婦':'housewife','歌手':'singer','寵物':'pet','可愛的':'cute',
              '小狗':'puppy',
              
              '海報':'poster','最喜愛的':'favorite','真地':'really','漂亮的；美麗的':'beautiful','很棒的':'great',
              '但是':'but','某事':'something','不對勁的':'wrong','腿':'leg','為什麼？':'How come？',
              '電腦':'computer','功能強大的':'powerful','相片':'photo','神奇的；魔術的':'magic','手機':'cellphone',
              '照相機':'camere','收音機':'radio','錄影機':'video','每個人':'everyone','世界':'world',
              '年輕的':'young','相同的':'same','人們':'people','真的嗎？':'Really？','太':'too',
              
              '漢堡':'hamburger','抱歉':'sorry','歲':'year(s) old','食物':'food','難怪':'No wonder.',
              '順便一提':'by the way','從那裡來…？':'Where... from？','加拿大':'Canada','著名的':'famous','楓樹':'maple',
              '葉子':'leaf','台灣':'Taiwan','美國':'the USA','英國':'the UK','法國':'France',
              '印度':'India', '日本':'Japan','北極熊':'polar bear','雙胞胎':'twin','非常地':'very',
              '游泳者':'swimmer',
              
              '在這邊':'overhere','女士':'lady','才藝表演':'talent show','遲到的':'late','我們走吧。':'Let\'s go.',
              '先生':'sir','兒子':'son','歌曲':'song','那麼；如此':'so','作者；作家':'writer',
              '醜的；難看的':'ugly','重的':'heavy','瘦的':'thin','胖的':'fat','明星':'star',
              '受歡迎的':'popular','女人':'woman','城鎮':'town','銷售員':'salesman','聽':'listen',
              '聲音':'voice','特別的':'special','在進行中；上演中':'on','作詞者；作曲家':'song writer',
              
              '電影院':'movie theater','黑暗的':'dark','等等我！':'Wait for me！','座位':'seat','趕快':'hurry',
              '安靜的':'quiet','坐下':'sit down','請':'please','關掉':'turn off','機器人':'robot',
              '聰明的':'smart','講話':'talk','垃圾':'trash','拿走':'take','與…一起':'with',
              '留下':'leave','站起來':'stand up','跑':'run','巧克力':'chocolate','工廠':'factory',
              '遵守':'follow','規則':'rule','製造噪音':'make noise','(站著)排隊':'stand in line','上車':'get on',
              '在那邊':'over there','結束':'over'
              } #字典是否可以合併呢？

list01=['同學','歡迎','起司','派', '客廳','照片','警察','護士','男演員','女演員',
        '男服員','女服員','醫生','家庭','農夫','廚師','家庭主婦','歌手','寵物','可愛的',
        '小狗',
        
        '海報','最喜愛的','真地','漂亮的；美麗的','很棒的','但是','某事','不對勁的','腿','為什麼？',
        '電腦','功能強大的','相片','神奇的；魔術的','手機','照相機','收音機','錄影機','每個人','世界',
        '年輕的','相同的','人們','真的嗎？','太',
        
        '漢堡','抱歉','歲','食物','難怪','順便一提','從那裡來…？','加拿大','著名的','楓樹',
        '葉子','台灣','美國','英國','法國','印度','日本','北極熊','雙胞胎','非常地',
        '游泳者',
        
        '在這邊','女士','才藝表演','遲到的','我們走吧。','先生','兒子','歌曲','那麼；如此','作者；作家',
        '醜的；難看的','重的','瘦的','胖的','明星','受歡迎的','女人','城鎮','銷售員',
        '聽','聲音','特別的','在進行中；上演中','作詞者；作曲家',
        
        '電影院','黑暗的','等等我！','座位','趕快','安靜的','坐下','請','關掉','機器人',
        '聰明的','講話','垃圾','拿走','與…一起','留下','站起來','跑','巧克力','工廠',
        '遵守','規則','製造噪音', '(站著)排隊','上車','在那邊','結束'
        ]

print('這是英文拚字練習\n')
print('請輸入你的英文名字:') #不換行怎麼做呢？
myname = input()
print('嗨！歡迎你！' + myname + '\n\n底下是英文單字測驗，準備開始！\n\n-----------------------------\n')

#我要怎麼做到，可以不按照順序的方式，顯示出這些詞呢？且，每一個都只會顯示一次。
#我現在有字典，也有串列了。我是可以，每答對一題，我就在串列中，把那個答對的詞刪掉，所以剩下的就會是還沒有答對的。
#串列有沒有方法，可以計算出，總共有幾個元素呢？有用len()方法，可以計算出這個串列有幾個元素。
count = len(list01)
#把數量用a記下來，每跑一次迴圈就減1
a=count

#跑迴圈，從0開始跑，執行到串列數量的前一個。因為串列的索引，是由0開始到count-1
for i in range(0,count):
    
    print('第'+str(i+1)+'題')
    j=random.randint(0,a-1)
    #print(j)
    #print(list01[j])
    while True:
        print('請拚出'+' \''+list01[j]+'\''+'的英文')
        youranswer = input()
        if youranswer == vocabulary01[list01[j]] :
            print('你答對了！\n')
            break
        else :
            print('你答錯了！')    
    print("  ")
    list01.remove(list01[j])
    a=a-1



