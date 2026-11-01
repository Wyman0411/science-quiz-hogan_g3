import time

def print_header(title):
    print("\n" + "="*55)
    print(f"✨ {title} ✨")
    print("="*55)

def show_core_review():
    print_header("📚 核心重點複習 (收折區)")
    choice = input("👉 想要展開閱讀「核心重點複習」嗎？\n(輸入 'y' 展開，或直接按 [Enter] 保持收折並開始測驗)：")
    
    if choice.lower() == 'y':
        print("\n" + "-"*50)
        print("📖 【第一課：打招呼】")
        print("  - 呼：呼吸、呼叫、歡呼")
        print("    * 造句：弟弟在操場上開心地大聲歡呼。")
        print("  - 塗：塗色、塗鴉、塗藥")
        print("    * 造句：妹妹喜歡在圖畫紙上開心地塗鴉。")
        
        print("\n📖 【第二課：爬梯子】")
        print("  - 梯：樓梯、梯子、電梯")
        print("    * 造句：我們一起搭電梯上樓。")
        print("  - 紙：色紙、報紙、白紙")
        print("    * 造句：哥哥用色紙摺了一架飛機。")
        
        print("\n📖 【第三課：勇氣樹】")
        print("  - 勇：勇敢、勇氣、勇士")
        print("    * 造句：遇到困難時，我們要勇敢的面對。")
        print("  - 樹：大樹、樹木、樹葉")
        print("    * 造句：公園裡有許多高大的樹木。")
        
        print("\n📖 【第四課：一天的時間】")
        print("  - 圓：圓形、圓圈、湯圓")
        print("    * 造句：大家圍成一個大圓圈玩遊戲。")
        print("  - 課：上課、下課、課本")
        print("    * 造句：鐘聲響了，大家趕快回教室上課。")
        
        print("\n📖 【第五課：小書蟲】")
        print("  - 蟲：昆蟲、毛毛蟲、甲蟲")
        print("    * 造句：弟弟很喜歡觀察大自然裡的昆蟲。")
        print("  - 停：停止、停車、停下")
        print("    * 造句：紅燈亮了，所有的車子都停下來。")
        
        print("\n📖 【第六課：從自己開始】")
        print("  - 沙：沙灘、沙子、泥沙")
        print("    * 造句：夏天時，我們全家去海邊的沙灘玩水。")
        print("  - 撿：撿起、撿到、撿垃圾")
        print("    * 造句：他把地上的垃圾撿起來丟進桶子裡。")
        print("-"*50)
        input("\n👉 複習完畢！請按 [Enter] 鍵準備開始闖關測驗...")
    else:
        print("🚀 太棒了！看來你已經準備好了，我們直接進入測驗！")

def run_quiz_section(questions):
    for i, q in enumerate(questions):
        print(f"\n{q['question']}")
        if 'options' in q:
            print(q['options'])
        input("👉 請想好答案後，按 [Enter] 鍵看解答...")
        print(f"✅ 正確解答：{q['answer']}")
        time.sleep(0.5)

def main():
    print("🎉 歡迎來到國小二年級國語（南一版）模擬考大挑戰！ 🎉")
    print("準備好了嗎？我們開始囉！\n")

    # === 核心重點複習區 (可收折) ===
    show_core_review()

    # === 題庫區 ===
    part1_questions = [
        {"question": "1. 妹妹在紙上( )顏色。", "options": "(A)呼 (B)塗 (C)雲 (D)朵", "answer": "(B) 塗"},
        {"question": "2. 這裡的風景真( )。", "options": "(A)美麗 (B)用力 (C)白雲 (D)往前", "answer": "(A) 美麗"},
        {"question": "3. 週末天氣很好，我們全家去( )山。", "options": "(A)爬 (B)跑 (C)待 (D)站", "answer": "(A) 爬"},
        {"question": "4. 哥哥用色( )摺了一架飛機。", "options": "(A)線 (B)梯 (C)格 (D)紙", "answer": "(D) 紙"},
        {"question": "5. 遇到困難時，我們要( )敢的面對。", "options": "(A)勇 (B)怕 (C)黑 (D)樹", "answer": "(A) 勇"},
        {"question": "6. 公園裡有很多高大的( )木。", "options": "(A)葉 (B)樹 (C)時 (D)事", "answer": "(B) 樹"},
        {"question": "7. 媽媽買了一個( )形的蛋糕。", "options": "(A)做 (B)課 (C)圓 (D)洗", "answer": "(C) 圓"},
        {"question": "8. 鐘聲響了，準備回教室上( )。", "options": "(A)飯 (B)課 (C)戲 (D)包", "answer": "(B) 課"},
        {"question": "9. 弟弟很喜歡觀察大自然裡的昆( )。", "options": "(A)蟲 (B)動 (C)物 (D)森", "answer": "(A) 蟲"},
        {"question": "10. 夏天時，大家去海邊的( )灘玩水。", "options": "(A)沙 (B)垃 (C)圾 (D)留", "answer": "(A) 沙"}
    ]

    part2_questions = [
        {"question": "1. 這裡的風景真美立。 (____)", "answer": "麗"},
        {"question": "2. 弟弟不小心把色只撕破了。 (____)", "answer": "紙"},
        {"question": "3. 他是一個永敢的警察。 (____)", "answer": "勇"},
        {"question": "4. 妹妹畫了一個園形。 (____)", "answer": "圓"},
        {"question": "5. 哥哥喜歡看書，是一隻小書虫。 (____)", "answer": "蟲"},
        {"question": "6. 我們在海邊的沙攤上玩沙。 (____)", "answer": "灘"},
        {"question": "7. 紅燈亮了，車子要廷下來。 (____)", "answer": "停"},
        {"question": "8. 媽媽煮的晚反真好吃。 (____)", "answer": "飯"},
        {"question": "9. 晚上好黑，我有點白。 (____)", "answer": "怕"},
        {"question": "10. 鐘聲響了，大家準備上客。 (____)", "answer": "課"}
    ]

    part3_questions = [
        {"question": "1. 多「少」___ / 「少」年___", "answer": "ㄕㄠˇ / ㄕㄠˋ"},
        {"question": "2. 方「便」___ / 「便」宜___", "answer": "ㄅㄧㄢˋ / ㄆㄧㄢˊ"},
        {"question": "3. 「種」子___ / 「種」樹___", "answer": "ㄓㄨㄥˇ / ㄓㄨㄥˋ"},
        {"question": "4. 「將」來___ / 「將」軍___", "answer": "ㄐㄧㄤ / ㄐㄧㄤˋ"},
        {"question": "5. 等「待」___ / 「待」在___", "answer": "ㄉㄞˋ / ㄉㄞ"},
        {"question": "6. 「覺」得___ / 睡「覺」___", "answer": "ㄐㄩㄝˊ / ㄐㄧㄠˋ"},
        {"question": "7. 音「樂」___ / 快「樂」___", "answer": "ㄩㄝˋ / ㄌㄜˋ"},
        {"question": "8. 「長」大___ / 很「長」___", "answer": "ㄓㄤˇ / ㄔㄤˊ"},
        {"question": "9. 「教」室___ / 「教」書___", "answer": "ㄐㄧㄠˋ / ㄐㄧㄠ"},
        {"question": "10. 重「要」___ / 「要」求___", "answer": "ㄧㄠˋ / ㄧㄠ"}
    ]

    part4_questions = [
        {"question": "1. 呼 (___部，造詞：_______)", "answer": "口部，呼吸 (或其他合理造詞)"},
        {"question": "2. 雲 (___部，造詞：_______)", "answer": "雨部，白雲"},
        {"question": "3. 梯 (___部，造詞：_______)", "answer": "木部，樓梯"},
        {"question": "4. 紙 (___部，造詞：_______)", "answer": "糸部，色紙"},
        {"question": "5. 勇 (___部，造詞：_______)", "answer": "力部，勇敢"},
        {"question": "6. 樹 (___部，造詞：_______)", "answer": "木部，大樹"},
        {"question": "7. 飯 (___部，造詞：_______)", "answer": "食部，吃飯"},
        {"question": "8. 圓 (___部，造詞：_______)", "answer": "囗部，圓形"},
        {"question": "9. 蟲 (___部，造詞：_______)", "answer": "虫部，昆蟲"},
        {"question": "10. 沙 (___部，造詞：_______)", "answer": "水部，沙灘"}
    ]

    part5_questions = [
        {"question": "1. ( ) 1.多「少」 2.減「少」 3.「少」年", "answer": "3"},
        {"question": "2. ( ) 1.方「便」 2.「便」利 3.「便」宜", "answer": "3"},
        {"question": "3. ( ) 1.「種」樹 2.「種」花 3.「種」子", "answer": "3"},
        {"question": "4. ( ) 1.「將」來 2.「將」軍 3.即「將」", "answer": "2"},
        {"question": "5. ( ) 1.等「待」 2.接「待」 3.「待」在", "answer": "3"},
        {"question": "6. ( ) 1.「覺」得 2.發「覺」 3.睡「覺」", "answer": "3"},
        {"question": "7. ( ) 1.快「樂」 2.歡「樂」 3.音「樂」", "answer": "3"},
        {"question": "8. ( ) 1.「長」大 2.生「長」 3.很「長」", "answer": "3"},
        {"question": "9. ( ) 1.「教」室 2.「教」練 3.「教」書", "answer": "3"},
        {"question": "10. ( ) 1.重「要」 2.主「要」 3.「要」求", "answer": "3"}
    ]

    part6_questions = [
        {"question": "1. 弟弟是愛畫畫的[__]小畫家[__][__]", "answer": "「 」 。"},
        {"question": "2. 天氣真好[__]我們去公園玩吧[__]", "answer": "， ！"},
        {"question": "3. 妹妹問[__][__]你喜歡吃蘋果還是香蕉呢[__][__]", "answer": "： 「 ？ 」"},
        {"question": "4. 媽媽說[__][__]今天晚上吃咖哩飯[__][__]", "answer": "： 「 。 」"},
        {"question": "5. 哇[__]這朵花好香啊[__]", "answer": "！ ！"}
    ]

    # === 執行測驗流程 ===
    print_header("第一關：生字造詞應用選擇題")
    run_quiz_section(part1_questions)

    print_header("第二關：短文改錯字")
    run_quiz_section(part2_questions)
    
    print_header("第三關：多音字測驗 (請唸出注音)")
    run_quiz_section(part3_questions)
    
    print_header("第四關：寫出部首並造詞")
    run_quiz_section(part4_questions)
    
    print_header("第五關：字音字形 (選出讀音不同的選項)")
    run_quiz_section(part5_questions)
    
    print_header("第六關：填標點符號練習")
    run_quiz_section(part6_questions)

    print("\n" + "*"*55)
    print("🏆 恭喜你完成所有的挑戰！你真的太棒了！考試一定沒問題！ 🏆")
    print("*"*55 + "\n")

if __name__ == "__main__":
    main()