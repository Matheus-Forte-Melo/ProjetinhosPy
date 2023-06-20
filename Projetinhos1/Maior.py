

def maior(*nums):
    if len(nums) > 0:
        mai = nums[0]
        for n in nums:
            if n > mai:
                mai = n
    else:
        mai = 0
        print('Você não insriu nada porra')
    print(f'Foram informados {len(nums)} números, e o maior deles é {mai}')
    print('==============================================================')


maior(5, 2, 5, 1, 2, 10, 11)
maior(5, 2, 5, 1, 4, 12, -1, 231, 21, 100)
maior(1, 12, 14, 16, 12, 21)
maior()