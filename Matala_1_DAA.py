# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 11:24:11 2023

@author: ASUS
"""

#משתנים
X1= 4.0
X2= 6.0
X3= 9.8


def my_func(x1,x2,x3):
    #Float. בדיקה האם כלל המשתנים הם מסוג -במידה והתנאי מתקיים מתבצע החישוב
    if isinstance(x1,float) and isinstance(x2, float) and isinstance(x3,float) == True:
        mone= (x1+x2+x3)*(x2+x3)*x3
        mechne= (x1+x2+x3)
#בדיקה האם המכנה == 0
        if mechne== 0:
            return "Not a number – denominator equals zero"
 #החזרת התשובה
        return mone/mechne
במידה והתנאי הראשון לא התקיים--> יש לחלק בין שני סוגי שגיאות:

    #1 אם int--> מחזיר שגיאה שנדרש flout
    elif isinstance(x1,int) or isinstance(x2, int) or isinstance(x3,int) == True:
            return "Error: parameters should be float"
  
    #2 אם גם לא int--> מחזיר ערך ריק
else:
        return None
        
# קריאה לפונקציה my_func
answer= my_func(X1,X2,X3)
print(answer)

##---------------------------------


    #  (מילה מ text) הפונקציה מקבלת מחרוזת אחתומחזירה את המחרוזת
    #כשהתווים שלה בסדר הפוך [::-1] ובאותיות קטנות .lower

def revword(word:str) -> str:
    return word[::-1].lower()


def countword() -> int:
    #  text.txt הפונקציה פותחת את הקובץ וקוראת את המילה הראשונה בקובץ.
    #.strip() יסייע לנו בלהוריד את הרווחים שקיימים בשורה
    word = ""
    with open("text.txt", "r") as f:
        word = f.readline().strip()
        count = 0
        # text.txt, הפונקציה עוברת על כל השורות של הקובץ ומחזירה את מספר "המופעים" של המילה המופיעה בשורה הראשונה בקובץ מתחילתו ועד סופו.
        for line in f:
            words_line = line.strip().split()
            for w in words_line:
                if revword(w) == word:
                    count += 1
                    # ל count  בכדי להגיע למספר המופעים *הכולל* בטקסט של המילה הראשונה -->הוספה של 1
                    #ולא רק של שאר המופעים בשאר השורות
        return count + 1
    

# "OLLEH" עם הפרמטר  test במידה ורוצים לעשות  קריאה לפונקצית המרה בלבד
#print(revword("OLLEH"))

# קריאה לפונקציה countword
print(countword())
