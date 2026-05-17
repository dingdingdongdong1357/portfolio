'''
承上題，美術館多了一項新的規定，每個人所購買的票券總張數不可以超過b張。
假設你要買x1張全票與 x2張學生票，請判斷你購買的總張數會不會超過購票上限。
同時，一張全票的售價是 p1元，一張學生票則是 p2元。若你拿出 t元鈔票給櫃臺，
請判斷是否足夠，以及若足夠，櫃臺會找你多少錢。
兩個判斷是獨立運作的，不論是否超過購票上限，都要判斷支付金額是否足夠，反之亦然。

每個檔案中會有六列，每列依序裝著一個非負整數 x1、p1、x2、p2、t、b。
已知 x1 和 x2 介於 0 到 20 之間、 p1 和 p2 介於 0 到 100 之間、 b介於 0 到 40 之間。
請依題目指示，判斷購買總張數會不會超過 b，如果超過則印出一個 -1，不超過則印出尚可購買的張數。

在關於總張數的判斷與輸出結束後，無論如何都印出一個逗號，接著判斷 t 是否足夠支付票價，
如果不夠則印出一個 -2，夠則先印出一個錢字號「$」，接著印出櫃台找錢的金額。
整個輸出中不應有任何其他字元（包括空白字元）。

5
60
7
30
1000
15

3,$490

'''

x1 = int(input())
p1 = int(input())
x2 = int(input())
p2 = int(input())
t = int(input())
ticket_constraint = int(input())

# 判斷有沒有買太多

n_ticket = x1 + x2

if n_ticket > ticket_constraint :
    quota_ticket = -1
else:
    quota_ticket = ticket_constraint - n_ticket

#　print(quota_ticket)

# 判斷找錢夠不夠

# 總花費
total_cost = x1*p1 + x2*p2

# 找錢
change = t - total_cost


# 把字串提早串接 避免$-2
if change < 0:
    display_change = -2
else:
    display_change = "$" + str(change)

print(str(quota_ticket) + "," + str(display_change))