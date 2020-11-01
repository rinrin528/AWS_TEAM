from function import *

# ==================================================
# 첫번째 매개변수는 str 타입의 xml 파일 경로
# 읽어오고 싶은 xml 파일의 경로
file_path = './realtime_data_xml/realtime.xml'
tmp_list = parsing_XML(file_path)
# 반환된 리스트의 첫번째 값은 엣지넘버
# 반환된 리스트의 두번째 값은 신호등 번호
# 반환된 리스트의 세번째 값은 신호등 유지 시간
print("realtime.xml 에서 parsing한 값")
print("edgeNo : " + tmp_list[0])
print("traffic_light : " + tmp_list[1])
edgeNo = tmp_list[0]
traffic_light = tmp_list[1]
time = tmp_list[2]
# ==================================================
# 첫번째 매개변수는 str 타입의 edgeNo
# 두번째 매개변수는 str 타입의 traffic_light
salt_value = get_salt_value(edgeNo, traffic_light)
# 반환된 값은 str타입의 salt_value
print("salt_value " + salt_value)
# ==================================================
# 첫번째 매개변수는 str 타입의 파일경로
# 두번째 매개변수는 str 타입의 솔트값
file_path = './realtime_data_xml/realtime.xml'
hash_value = make_hash(file_path, salt_value)
# 반환된 값은 str 타입의 솔트가 추가된 hash 값
print("hash_value : " + hash_value)
# ==================================================
# 라파로부터 받은 hash값이라고 가정
Raspberry_hash_value = "64fa17a678e981140b6f151152b6cb922e8859b45d071e36396a12bcaf66a1b4"
# ==================================================
# json 파일 만들기
# 첫번째 매개변수는 str 타입의 edgeNo
# 두번째 매개변수는 str 타입의 traffic_light
# 세번째 매개변수는 str 타입의 time
# 만들고 싶은 파일의 경로를 str 타입으로 작성
file_path = './realtime_data_json/realtime.json'
make_Json_file(edgeNo, traffic_light, time, file_path)
# ==================================================
# 무결성 검사 후 EC2(라파통신) => EC2(관리자페이지) 파일 넘기기
result = integrity_check(hash_value, Raspberry_hash_value)
print(result)
# ==================================================
