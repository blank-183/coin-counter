import cv2 as cv

img = cv.imread('images/4.jpg')
imggray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(imggray, 220, 255, cv.THRESH_BINARY)
contours, hierarchy = cv.findContours(
    thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cfive_coin = 0
cten_coin = 0
ctfive_coin = 0
pone_coin = 0
pfive_coin = 0
pten_coin = 0

for c in contours:
    rx, ry, rw, rh = cv.boundingRect(c)
    (x, y), radius = cv.minEnclosingCircle(c)
    center = (int(x), int(y))
    radius = int(radius)
    perimeter = cv.arcLength(c, True)
    approximity = cv.approxPolyDP(c, 0.04 * perimeter, True)
    area = cv.contourArea(c)

    if(int(len(approximity)) > 5 and area > 2000):
        cv.rectangle(img, (rx, ry), (rx + rw, ry + rh), (0, 255, 0), 2)
        if(area < 2500):
            cfive_coin = cfive_coin + 1
            cv.putText(img, '5c', (rx, ry - 3),
                       cv.FONT_HERSHEY_DUPLEX, 0.3, (255, 0, 0), 1)
        elif (area > 2500 and area < 3500):
            cten_coin = cten_coin + 1
            cv.putText(img, '10c', (rx, ry - 3),
                       cv.FONT_HERSHEY_DUPLEX, 0.3, (255, 0, 0), 1)
        elif (area > 3500 and area < 5000):
            ctfive_coin = ctfive_coin + 1
            cv.putText(img, '25c', (rx, ry - 3),
                       cv.FONT_HERSHEY_DUPLEX, 0.3, (255, 0, 0), 1)
        elif (area > 5000 and area < 6000):
            pone_coin = pone_coin + 1
            cv.putText(img, '1p', (rx, ry - 3),
                       cv.FONT_HERSHEY_DUPLEX, 0.3, (255, 0, 0), 1)
        elif (area > 6000 and area < 7000):
            pten_coin = pten_coin + 1
            cv.putText(img, '10p', (rx, ry - 3),
                       cv.FONT_HERSHEY_DUPLEX, 0.3, (255, 0, 0), 1)
        else:
            pfive_coin = pfive_coin + 1
            cv.putText(img, '5p', (rx, ry - 3),
                       cv.FONT_HERSHEY_DUPLEX, 0.3, (255, 0, 0), 1)

cfive_amt = cfive_coin * 0.05
cten_amt = cten_coin * 0.10
ctfive_amt = ctfive_coin * 0.25
pone_amt = pone_coin * 1
pfive_amt = pfive_coin * 5
pten_amt = pten_coin * 10

total_coins = cfive_coin + cten_coin + \
    ctfive_coin + pone_coin + pfive_coin + pten_coin
total_amount = cfive_amt + cten_amt + \
    ctfive_amt + pone_amt + pfive_amt + pten_amt

print(f'# of five centavo coin: {cfive_coin} Amount: {cfive_amt:.2f}')
print(f'# of ten centavo coin: {cten_coin} Amount: {cten_amt:.2f}')
print(f'# of twenty-five centavo coin: {ctfive_coin} Amount: {ctfive_amt:.2f}')
print(f'# of one peso coin: {pone_coin} Amount: {pone_amt}')
print(f'# of five peso coin: {pfive_coin} Amount: {pfive_amt}')
print(f'# of ten peso coin: {pten_coin} Amount: {pten_amt}')

print(f'Total number of coins: {total_coins}')
print(f'Total amount of coins: {total_amount}')

cv.putText(img, f'No. of 5 centavo coin:    {cfive_coin}   Amount: P {cfive_amt:.2f}', (
    10, 25), cv.FONT_HERSHEY_SIMPLEX, 0.6, (16, 10, 240), 2)
cv.putText(img, f'No. of 10 centavo coin:   {cten_coin}   Amount: P {cten_amt:.2f}', (
    10, 50), cv.FONT_HERSHEY_SIMPLEX, 0.6, (16, 10, 240), 2)
cv.putText(img, f'No. of 25 centavo coin:   {ctfive_coin}   Amount: P {ctfive_amt:.2f}', (
    10, 75), cv.FONT_HERSHEY_SIMPLEX, 0.6, (16, 10, 240), 2)
cv.putText(img, f'No. of 1 peso coin:        {pone_coin}   Amount: P {pone_amt:.2f}', (
    10, 100), cv.FONT_HERSHEY_SIMPLEX, 0.6, (16, 10, 240), 2)
cv.putText(img, f'No. of 5 peso coin:        {pfive_coin}   Amount: P {pfive_amt:.2f}', (
    10, 125), cv.FONT_HERSHEY_SIMPLEX, 0.6, (16, 10, 240), 2)
cv.putText(img, f'No. of 10 peso coin:       {pten_coin}   Amount: P {pten_amt:.2f}', (
    10, 150), cv.FONT_HERSHEY_SIMPLEX, 0.6, (16, 10, 240), 2)

cv.putText(img, '-------------------------------', (
    10, 175), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
cv.putText(img, f'TOTAL AMOUNT: P {total_amount:.2f}', (
    10, 210), cv.FONT_HERSHEY_DUPLEX, 1.0, (16, 10, 240), 2)

cv.putText(img, f'NUMBER OF COINS DETECTED: {total_coins}', (
    10, 550), cv.FONT_HERSHEY_DUPLEX, 0.8, (16, 10, 240), 2)
# print(coin_count)
cv.imshow("Threshed Image", thresh)
cv.imshow("result", img)

cv.waitKey(0)
cv.destroyAllWindows()
