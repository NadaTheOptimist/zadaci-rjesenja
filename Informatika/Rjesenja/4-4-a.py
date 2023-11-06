# 4.4.a)
# --- kopirani kod iz 4.4. ---

s = input()

s = s.replace("e", "3").replace("a", "4").replace("i", "1").replace("o", "0")
# --- kraj kopiranog koda iz 4.4. ---
broj = ""

for i in s:
    if i in "1234567890": # provjerava je li i znamenka
        broj+=i

print(broj)
