#딕셔너리 생성
IT_CEO = {"guido":"python", "jobs":"iphone", "bill":"windows"}

IT_CEO["mark"] = "facebook"  #새로운 key:value 추가
print(IT_CEO)

print(IT_CEO.get('bill', 'unknown'))

print(IT_CEO.get('jobs','unknown'))

del IT_CEO["jobs"]  #key "jobs" 삭제, value "iphone"도 삭제

print(IT_CEO.get('jobs','unknown'))

IT_CEO.clear()   #딕셔너리의 모든 키-벨류 쌍 삭제
print(IT_CEO)

for key in IT_CEO :
    print("key: \t" + key + "\t | value: \t" + IT_CEO[key])